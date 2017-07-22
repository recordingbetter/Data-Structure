def adder(a, b):
    c = a + b
    return c

def main():
    a = 10
    b = 20
    c = adder(a, b)
    print('c: {}'.format(c))

if __name__ == "__main__":
    main()

    import dis
    bytecode = dis.Bytecode(adder)
    for instruction in bytecode:
        print(instruction.opname)

