#include <iostream>
#include <string>
#include <sstream>
#include <exception>
using namespace std;

/* Define the exception here */

class BadLengthException : public exception
{
public:
  BadLengthException(int n) : length(n) {}
  void test_length() { cout << length; }
  virtual const char* what()
  {
    switch(length)
    {
      case 0: return("0");
              break;
    case 1: return("1");
      break;
    case 2: return("2");
      break;
    case 3: return("3");
      break;
    case 4: return("4");
      break;
    }
    return("");
  }
private:
  int length;
};


bool checkUsername(string username) {
	bool isValid = true;
	int n = username.length();
	if(n < 5) {
		throw BadLengthException(n);
	}
	for(int i = 0; i < n-1; i++) {
		if(username[i] == 'w' && username[i+1] == 'w') {
			isValid = false;
		}
	}
	return isValid;
}

int main() {
	int T; cin >> T;
	while(T--) {
		string username;
		cin >> username;
		try {
			bool isValid = checkUsername(username);
			if(isValid) {
				cout << "Valid" << '\n';
			} else {
				cout << "Invalid" << '\n';
			}
		} catch (BadLengthException e) {
			cout << "Too short: " << e.what() << '\n';
		}
	}
	return 0;
}
