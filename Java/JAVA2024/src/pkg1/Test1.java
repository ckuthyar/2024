package pkg1;
import java.util.List;
import java.util.stream.Collectors;
import java.util.ArrayList;


.  
public class Test1 {

	public static void main(String[] args) {
		// To learn use of a Lambda operator
		int[]arr1= {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
		ArrayList<Integer>list1=new ArrayList<>();
		List<Integer>list2=new ArrayList<>();
		for(int i=0;i<arr1.length;i++) {
			list1.add(arr1[i]);
		}
		list2=list1.stream().filter(n -> n%3==0).collect(Collectors.toList());
		System.out.println(list2);
	}
}
