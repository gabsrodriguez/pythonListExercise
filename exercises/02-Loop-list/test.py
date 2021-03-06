import io
import sys
sys.stdout =  buffer = io.StringIO()



import pytest
import app
import os

@pytest.mark.it("Print the all items from the list")
def test_output():
    captured = buffer.getvalue()
    assert "232\n32\n1\n4\n55\n4\n3\n32\n3\n24\n5\n5\n5\n34\n2\n35\n5365743\n52\n34\n3\n55\n" in captured

@pytest.mark.it("Be sure that you use the for loop in the exercises")
def test_use_forLoop():

    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("for") > 0