#include <stdio.h>
void reverse(*str){
	char* end=str;
	char temp;
	if (str){
		while *end{
			++end;
		}
	}
	--end;
	while(str<end){
		temp= *str;
		*str++= *end;
		*end--=temp;
	}
	printf("%s\n", str);
}
void main(){
	reverse("nithnkumar");
}