import numpy as np

def kl_divergence_normal(mu_p, sigma_p, mu_q, sigma_q):
	term_1 = np.log(sigma_q / sigma_p)
	term_2 = sigma_p ** 2 + (mu_p - mu_q) ** 2
	term_2 /= (2 * sigma_q ** 2)
	term_3 = 0.5
	return term_1 + term_2 - term_3
