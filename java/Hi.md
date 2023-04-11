# Java 기본

## 운영체제와 프로그램

JDK - 개발자 도구 = JRE + 개발에 필요한 도구(컴파일러, 디버거)
JRE - 자바 실행 환경 JVM이 들어있다?

```bash
import java.lang.*; # << 첫줄은 생략 가능?
public class Hello{
    public static void main(String[] args){
        system.out.println("Hello SSAFY!");
    }
}
```

메모장 - C -> temp -> .java(모든파일)
자바 깔렸나 확인 - cmd켜고 java -version
실행 - cmd 켜고 temp 폴더로 이동 -> javac Hi(파일명).java