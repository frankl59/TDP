from gruppo14.circular_positional_list import CircularPositionalList


if __name__ == "__main__":
    l = CircularPositionalList()

    print("Lista vuota?", l.is_empty())
    p = l.add_last(50)
    print('\nTest before e after sul singolo')
    print(l.before(p))
    print(l.after(p))
    l.add_last(60)
    print(l.after(p).element())
    print("\nLista vuota?", l.is_empty())
    l.add_first(40)
    l.add_first(30)
    l.add_last(70)
    l.add_last(80)
    print("\nelementi della lista:")
    for e in l:
        print(e)
    print('\nTesting find.......')
    p = l.find(60)
    print("con successo", p.element())
    p = l.find(90)
    print("senza successo", p)
    print('\nTesting delete.......')
    print('\tdelete con add_first')
    p = l.add_first(20)
    l.delete(p)
    for e in l:
        print(e)
    print('\tdelete con add_last')
    p = l.add_last(100)
    l.delete(p)
    for e in l:
        print(e)
    print('\tdelete con add_after')
    p = l.add_after(l.first(), 78)
    l.delete(p)
    for e in l:
        print(e)
    print('\tdelete con add_before')
    p = l.add_before(l.first(), 78)
    l.delete(p)
    for e in l:
        print(e)
    print('\nTest count........')
    print(l.count(30))
    print(l.count(180))
    print("\nTest circolare")
    print("\tcon add_first")
    # l.add_first(60)
    # l.add_first(50)
    # l.add_first(40)
    # l.add_first(30)
    # l.add_first(20)
    # l.add_first(10)
    p = l.first()
    q = l.last()
    print("Before di first", l.before(p).element())
    print("After di last", l.after(q).element())
    print("\n\tcon add_last")
    # l.add_last(10)
    # l.add_last(20)
    # l.add_last(30)
    # l.add_last(40)
    # l.add_last(50)
    # l.add_last(60)
    p = l.first()
    q = l.last()
    print("Before del first", l.before(p).element())
    print("After del last", l.after(q).element())
    print("\nTesting reverse.......")
    l.reverse()
    for e in l:
        print(e)
    # l.add_last(22)
    print(l.is_sorted())

    print("Test add")
    list2 = CircularPositionalList()
    list2.add_first(500)
    list2.add_first(200)
    list2.add_first(300)
    list2.add_first(900)
    list2.add_first(400)
    l = l + list2
    for e in l:
        print(e)

    print("Test copy")
    list_copy = l.copy()
    for e in list_copy:
        print(e)
    print(l)
    print(list_copy)
    print("Test __str__")
    print(l)
