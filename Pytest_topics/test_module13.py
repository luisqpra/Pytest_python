
def test_argtest01(CmdOpt):
    print("Read config file: " + CmdOpt.readline())
    environment = CmdOpt.readline()
    print(environment)
    assert (1 == 1)
