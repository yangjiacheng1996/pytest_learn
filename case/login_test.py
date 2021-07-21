import pytest
import time

class TestLogin():
    @pytest.mark.run(order=3)
    @pytest.mark.smoke
    def test_01_haha(self):
        time.sleep(3)
        print("hahahaha")

    @pytest.mark.run(order=1)
    def test_02_hoho(self):
        time.sleep(3)
        print("hohohoho")

    @pytest.mark.run(order=2)
    def test_03_fail(self):
        time.sleep(3)
        assert 1==2


if __name__ =="__main__":
    pytest.main(["-vs"])
    #pytest.main(["-vs","-n 3","--reruns=2","-k hoho"])
    # pytest.main(["-vs","login_test.py"]) # 这里可以指定文件或文件夹，main方法可以放在系统的任何地方。
    #pytest.main(["-vs", "login_test.py::TestLogin::test_01_haha"])