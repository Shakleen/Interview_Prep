def relu(z: float) -> float:
	return max(z, 0)


if __name__ == "__main__":
    print(relu(0)) 
    print(relu(1)) 
    print(relu(-1))