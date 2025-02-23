import torch
from torch import nn


class SelfAttention(nn.Module):
    def __init__(self, input_dim: int, qk_dim: int, v_dim: int) -> None:
        super().__init__()

        self.input_dim = input_dim
        self.qk_dim = qk_dim
        self.v_dim = v_dim

        self.W_q = nn.Parameter(torch.rand(self.input_dim, self.qk_dim))
        self.W_k = nn.Parameter(torch.rand(self.input_dim, self.qk_dim))
        self.W_v = nn.Parameter(torch.rand(self.input_dim, self.v_dim))

        self.scale = self.qk_dim**0.5

    def forward(self, X: torch.Tensor) -> torch.Tensor:
        # Input shape: (Batch Size, Seq Length, Input Dim)
        queries = X @ self.W_q  # (Batch Size, Seq Length, QK Dim)
        keys = X @ self.W_k  # (Batch Size, Seq Length, QK Dim)
        values = X @ self.W_v  # (Batch Size, Seq Length, V Dim)

        # Unnormalized Attention Scores
        # (Batch Size, Seq Length, Seq Length)
        attention_scores = queries @ keys.transpose(-2, -1)

        # Normalized Attention Scores
        attention_scores = torch.softmax(attention_scores / self.scale, dim=-1)

        # Contextualized output
        # (Batch Size, Seq Length, V Dim)
        output = attention_scores @ values

        return output


if __name__ == "__main__":
    BATCH_SIZE = 4
    SEQ_LEN = 32
    EMB_SIZE = 128

    X = torch.rand(BATCH_SIZE, SEQ_LEN, EMB_SIZE)
    print(X.shape)

    attn = SelfAttention(EMB_SIZE, 16, 16)
    out = attn(X)
    print(out.shape)
