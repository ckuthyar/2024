package pkg1;

public class Test4 {

	public static void main(String[] args) {
		String[] arr1= {"A","B","C"};
		String[] arr2= {"01","02","03"};
		String input1="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA";
		int len1=input1.length();
		String output1="";
		String c1="";
		int position=0;
		for(int j=0;j<len1;j++) {
			c1=input1.substring(0,1);
			for (int i=0;i<3;i++) {
				if(arr1[i].equals(c1)) {
					position=i;
					output1=output1+arr2[position];
				}
				break;
			}
		}
		System.out.println(output1);
		
		
		
		

	}

}
