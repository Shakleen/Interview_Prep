import torch
from torch import nn


class CausalMultiHeadAttention(nn.Module):
    def __init__(self, input_dim: int, qk_dim: int, v_dim: int, num_heads) -> None:
        assert qk_dim % num_heads == 0 and v_dim % num_heads == 0

        super().__init__()

        self.input_dim = input_dim
        self.qk_dim = qk_dim
        self.v_dim = v_dim
        self.num_heads = num_heads

        self.W_q = nn.Parameter(torch.rand(self.input_dim, self.qk_dim))
        self.W_k = nn.Parameter(torch.rand(self.input_dim, self.qk_dim))
        self.W_v = nn.Parameter(torch.rand(self.input_dim, self.v_dim))

        self.scale = self.qk_dim**0.5

    def forward(self, X: torch.Tensor) -> torch.Tensor:
        # Input shape: (Batch Size, Seq Length, Input Dim)
        batch_size, seq_len, _ = X.shape

        # Calculate Q, K, and V
        queries = X @ self.W_q  # (Batch Size, Seq Length, QK Dim)
        keys = X @ self.W_k  # (Batch Size, Seq Length, QK Dim)
        values = X @ self.W_v  # (Batch Size, Seq Length, V Dim)

        # Reshape Q, K, and V to split out head dimension
        queries = queries.view(
            batch_size, seq_len, self.num_heads, int(self.qk_dim / self.num_heads)
        ).transpose(2, 1)
        keys = keys.view(
            batch_size, seq_len, self.num_heads, int(self.qk_dim / self.num_heads)
        ).transpose(2, 1)
        values = values.view(
            batch_size, seq_len, self.num_heads, int(self.v_dim / self.num_heads)
        ).transpose(2, 1)

        # Unnormalized Attention Scores
        # (Batch Size, Seq Length, Seq Length)
        attention_scores = queries @ keys.transpose(-2, -1)

        # Masking 
        mask = torch.triu(torch.ones(seq_len, seq_len), diagonal=1)
        attention_scores = torch.masked_fill(attention_scores, mask, -torch.inf)

        # Normalized Attention Scores
        attention_scores = torch.softmax(attention_scores / self.scale, dim=-1)

        # Contextualized output
        # (Batch Size, Num Heads, Seq Length, Head Dim)
        output = attention_scores @ values

        # Reshape back
        output = output.transpose(2, 1)
        output = output.contiguous().view(batch_size, seq_len, self.v_dim)

        return output


if __name__ == "__main__":
    BATCH_SIZE = 4
    SEQ_LEN = 32
    EMB_SIZE = 128
    NUM_HEADS = 4

    X = torch.rand(BATCH_SIZE, SEQ_LEN, EMB_SIZE)
    print(X.shape)

    attn = CausalMultiHeadAttention(EMB_SIZE, 16, 16, NUM_HEADS)
    out = attn(X)
    print(out.shape)
