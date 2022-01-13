def reverse_string(in_string):
  return in_string[::-1]
  
def test_reverse_string():
    assert reverse_string("power") == "rewop", "Should be rewop"

if __name__ == "__main__":
    #in_string = input("Enter the string you want to reverse: ")
    test_reverse_string()
    print("Everything passed")
