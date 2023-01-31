from bot import create_dispatcher, run_bot


def main():
    dp = create_dispatcher()
    run_bot(dp)


if __name__ == '__main__':
    main()
