import java.util.Scanner; 
import java.util.HashMap;

public class MyClass {
    public static void main(String args[]) {
        // Linhas acima ignoradas
        // Caracteres: 286
        Scanner s=new Scanner(System.in);
        String[] r=s.nextLine().split(" ");
        HashMap<Character,Integer> w=new HashMap<Character,Integer>();
        w.put('d',0);
        w.put('p',1);
        w.put('s',2);
        int v=(3+w.get(r[0].charAt(2))-w.get(r[1].charAt(2)))%3;
        System.out.println((v != 0)?"Jogador "+v:"Não há vencedores");
        //Linhas abaixo ignoradas
    }
}
