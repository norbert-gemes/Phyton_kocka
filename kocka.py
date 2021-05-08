def kv(a: int) -> float:
    KV: float = a * a * a
    return KV


def ka(a: int) -> int:
    KA: int = 6 * (a * a)
    return KA


def main() -> None:
    print('Kocka térfogat, felszín!')

    a: int = int(input('Adja meg a kocka egy oldalát:'))

    térfogat: float = kv(a)
    felszín: int = ka(a)
    print(f'A kocka térfogata: {térfogat}cm^3')
    print(f'A kocka felszíne: {felszín} cm^2')


if __name__ == '__main__':
    main()
