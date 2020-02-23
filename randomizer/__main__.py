from randomizer import shuffle


def main():
    output = " ".join(str(x) for x in shuffle())
    print(output)


if __name__ == "__main__":
    main()
