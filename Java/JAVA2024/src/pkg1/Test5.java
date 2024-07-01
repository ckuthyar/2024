package pkg1;
import java.util.ArrayList;
public class Test5 {

	public static void main(String[] args) {
		ArrayList<String> list1=new ArrayList<>();
		ArrayList<String> list2=new ArrayList<>();
		list1.add("A");
		list1.add("B");
		list1.add("C");
		list1.add("D");
		
		list2.add("01");
		list2.add("02");
		list2.add("03");
		list2.add("04");
		
		String input1="DCBA DCBA";
		int len1=input1.length();
		String output1="";
		String c1="";
		int pos=0;
		for(int i=0; i<len1;i++) {
			c1=input1.substring(i,i+1);    
			pos=list1.indexOf(c1);       
			output1=output1+list2.get(pos);
		}
		System.out.println(output1);
		
		
		
		

	}

}
