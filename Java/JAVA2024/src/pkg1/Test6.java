package pkg1;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
public class Test6 {
	public static void mailmerge1(String fname1, String fname2)throws IOException {
		String fwname="";
		LocalDateTime ldt1=LocalDateTime.now();
		DateTimeFormatter dtf1=DateTimeFormatter.ofPattern("yyyyMMdd_hhmmss");
		String timestamp=dtf1.format(ldt1);
		System.out.println(timestamp);
		File f1=new File(fname1);
		File f2=new File(fname2);
		String[]arr2=fname1.split("\\.");
		String[]arr3=fname2.split("\\.");
		fwname=arr2[0]+"_"+arr3[0]+"_"+timestamp+"_out."+arr2[1];
		
		FileWriter fw1=new FileWriter(fwname);
		Scanner sc1=new Scanner(f1);
		Scanner sc2=new Scanner(f2);
		String str1="";
		String str2="";
		String template=sc2.nextLine();
		int count1=0;
		for(int i=0;i<template.length();i++) {
			if (template.substring(i,i+1).equals("$")) {
				count1=count1+1;
			}
		}
		String prefix="";
		while(sc1.hasNext()) {
			str2=template;
			str1=sc1.nextLine();
			String[]arr1=str1.split(",");
			for(int i=1;i<count1+1;i++) {
				str2=str2.replace("$"+i,arr1[i-1]);
			}
			System.out.println(str2);
			fw1.write(str2+"\n");		
		}
		fw1.close();

	}

	public static void main(String[] args)throws IOException{
		mailmerge1("names1.txt","template1.txt");
		mailmerge1("names1.txt","template2.txt");
		mailmerge1("names2.txt","template3.txt");
		
	}

}
