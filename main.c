#include<stdio.h>

// 함수 선언을 올바르게 수정
void input_str(char* x) {
    scanf("%s", x);
}

void print_str(char* x) {
    printf("%s", x);
}

int main() {
    char q[88888];
    char *c_s = "S";
    printf(c_s);
    char *c_m = "M";
    printf(c_m);
    
    // i, p 함수 호출 수정
    input_str(q);
    print_str("");
    
    // 나머지 문자열 출력 부분
    char *K = "K", *I = "I", *C = "C", *O = "O";
    char *H = "H", *S = "S", *N = "N", *A = "A";
    
    print_str(C);
    print_str(H);
    print_str(O);
    print_str(O);
    print_str(N);
    print_str(S);
    print_str(I);
    print_str(K);
    print_str(I);
    print_str(S);
    print_str(A);
    print_str(q);
    
    return 0;
}