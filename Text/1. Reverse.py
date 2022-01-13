def reverse_string(in_string):
  length = i = len(in_string)
  output = ""
  while(i > 0):
    i -= 1
    output += in_string[i]
    #print(in_string[i], end="")
  return output
  
def test_reverse_string():
    assert reverse_string("power") == "rewop", "Should be rewop"

if __name__ == "__main__":
    #in_string = input("Enter the string you want to reverse: ")
    test_reverse_string()
    print("Everything passed")
