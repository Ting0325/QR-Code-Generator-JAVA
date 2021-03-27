import java.awt.Color;
import java.util.Random;
import java.util.Scanner;

import javax.swing.JFrame;

public class Driver {
	public static void main(String[] args) {
		JFrame frame = new JFrame();
		//frame.getContentPane().setBackground(Color.black);
		//frame.setBackground(Color.black);
		frame.setSize(800,800);
		
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		Panel panel = new Panel();
		frame.add(panel);
		frame.setVisible(true);
		Scanner sc = new Scanner(System.in);
		int size = 21;
		Random rand = new Random();
		//while(true) {
			//size = sc.nextInt();
			
			int[][] pattern = new int[size][size];
			
			for(int i = 0; i < pattern.length;i ++) {
				for(int j = 0; j < pattern[i].length;j++) {
					pattern[i][j] = rand.nextInt(2);
				}
			}
			
			pattern = patternGen();
			printArr2d(pattern);
			panel.pattern = pattern;
			panel.repaint();
		//}
		
		
	}
	
	static void printArr2d(int[][] arr) {
		for(int i = 0; i < arr.length;i ++) {
			for(int j = 0; j < arr[i].length;j++) {
				System.out.print(arr[i][j]+" ");
			}
			System.out.println();
		}
	}
	
	static int[][]  patternGen() {
		int[][] pattern = new int[21][21];
		//String encodedWord = "0100000100010100100001100101011011000110110001101111001011000010000001110111011011110111001001101100011001000010000100100000001100010011001000110011000010000101101010010101111000000111000010100011011011001001";
		//String encodedWord = "0100000011100100111001110101011101000111001100100000010010010110111001110011011101000110100101110100011101010111010001100101000011101100000100011110110011010000100011111000010110111000000010011001101100010101";
								
		String text = "Hello, world! 123";
		String encodedWord = "";
		//mode
		encodedWord = "0100";
		//character count 17
		encodedWord = encodedWord + "00010001";
		//encode characters
		/*
		System.out.println(text.charAt(0));
		System.out.println((int)(text.charAt(0)));
		System.out.println(toBinaryFixLength((int)text.charAt(0),8));
		*/
		
		for(int i = 0; i < 17;i ++) {
			encodedWord = encodedWord + toBinaryFixLength((int)text.charAt(i),8);
		}
		//byte padding to 152 bits = 19 bytes
		//end sequence
		encodedWord = encodedWord + "0000";
		//ECC codewords
		String ecc = "10000101101010010101111000000111000010100011011011001001";
		//String ecc = "11010000100011111000010110111000000010011001101100010101";
		encodedWord = encodedWord+ecc;
		System.out.println(encodedWord);
		drawBrick(pattern, 0, 0);
		drawBrick(pattern, 14, 0);
		drawBrick(pattern, 0, 14);
		//drawCodeWord(pattern, 17, 19, 1, "hello");
		
		drawCodeWordNoConvert(pattern, 17, 19, 0, encodedWord.substring(0, 8));
		drawCodeWordNoConvert(pattern, 13, 19, 0, encodedWord.substring(8, 16));
		drawCodeWordNoConvert(pattern, 9, 19, 0, encodedWord.substring(16, 24));
		
		drawCodeWordNoConvert(pattern, 9, 17, 1, encodedWord.substring(24, 32));
		drawCodeWordNoConvert(pattern, 13, 17, 1, encodedWord.substring(32, 40));
		drawCodeWordNoConvert(pattern, 17, 17, 1, encodedWord.substring(40, 48));
		
		drawCodeWordNoConvert(pattern, 17, 15, 0, encodedWord.substring(48, 56));
		drawCodeWordNoConvert(pattern, 13, 15, 0, encodedWord.substring(56, 64));
		drawCodeWordNoConvert(pattern, 9, 15, 0, encodedWord.substring(64, 72));
		
		drawCodeWordNoConvert(pattern, 9, 13, 1, encodedWord.substring(72,80));
		drawCodeWordNoConvert(pattern, 13, 13, 1, encodedWord.substring(80,88));
		drawCodeWordNoConvert(pattern, 17, 13, 1, encodedWord.substring(88,96));
		
		drawCodeWordNoConvert(pattern, 17, 11, 0, encodedWord.substring(96,104));
		drawCodeWordNoConvert(pattern, 13, 11, 0, encodedWord.substring(104,112));
		drawCodeWordNoConvert(pattern, 9, 11, 0, encodedWord.substring(112,120));	
		drawCodeWordNoConvertSpecial(pattern, 4, 11, 0, encodedWord.substring(120,128));
		drawCodeWordNoConvert(pattern, 0, 11, 0, encodedWord.substring(128,136));
		
		
		drawCodeWordNoConvert(pattern, 0, 9, 1, encodedWord.substring(136,144));
		drawCodeWordNoConvertSpecial(pattern, 4, 9, 1, encodedWord.substring(144,152));
		drawCodeWordNoConvert(pattern, 9, 9, 1, encodedWord.substring(152,160));
		drawCodeWordNoConvert(pattern, 13, 9, 1, encodedWord.substring(160,168));
		drawCodeWordNoConvert(pattern, 17, 9, 1, encodedWord.substring(168,176));
		
		drawCodeWordNoConvert(pattern, 9, 7, 0, encodedWord.substring(176,184));
		drawCodeWordNoConvert(pattern, 9,4, 1, encodedWord.substring(184,192));
		drawCodeWordNoConvert(pattern, 9,2, 0, encodedWord.substring(192,200));
		drawCodeWordNoConvert(pattern, 9,0, 1, encodedWord.substring(200,208));
		
		//drawCodeWord(pattern, 17, 19, 1, "hello");
		int[][] mask = maskGen();
		printArr2d(mask);
		XOR(pattern,mask);
		drawFormatBits(pattern);
		drawTimingBits(pattern);
		System.out.println();
		return pattern;
	}
	
	static void drawBrick(int arr[][],int x,int y) {
		for(int i = 0;i < 7;i ++) {
			for(int j =0 ; j < 7;j ++) {
				if((i == 1 && j > 0 && j < 6) || (i == 5 && j!=0 && j!=6) || (i>0 && i<6 && (j==1 || j==5) ))
					arr[i+x][j+y] = 0;
				else
					arr[i+x][j+y] = 1;
			}
		}
	}
	

	
	static void drawCodeWordNoConvert(int arr[][],int x,int y,int type,String word) {

		
		if(type == 1){
			int c = 7;
			for(int i = 3; i >= 0;i --) {
				for(int j = 0; j < 2;j++) {
					//System.out.println(i*2+j);
					if(word.charAt(c) == '1')
						arr[i+x][j+y] = 1;
					else
						arr[i+x][j+y] = 0;
					c --;
				}
				
			}
		}else {
			for(int i = 0; i < 4;i ++) {
				for(int j = 0; j < 2;j++) {
					if(word.charAt((word.length()-1)-(i*2+j)) == '1')
						arr[i+x][j+y] = 1;
					else
						arr[i+x][j+y] = 0;
				}
			}
		}
	}
	static void drawCodeWord(int arr[][],int x,int y,int type,String word) {
		word = toBinaryFixLength(137,8);
		
		if(type == 1){
			int c = 7;
			for(int i = 3; i >= 0;i --) {
				for(int j = 0; j < 2;j++) {
					System.out.println(i*2+j);
					if(word.charAt(c) == '1')
						arr[i+x][j+y] = 1;
					else
						arr[i+x][j+y] = 0;
					c --;
				}
				
			}
		}else {
			for(int i = 0; i < 4;i ++) {
				for(int j = 0; j < 2;j++) {
					if(word.charAt((word.length()-1)-(i*2+j)) == '1')
						arr[i+x][j+y] = 1;
					else
						arr[i+x][j+y] = 0;
				}
			}
		}
	}
	static void drawCodeWordNoConvertSpecial(int arr[][],int x,int y,int type,String word) {
		
		if(type == 1){
			int c = 7;
			for(int i = 3; i >= 0;i --) {
				for(int j = 0; j < 2;j++) {
					//System.out.println(i*2+j);
					if(i > 1) {
						if(word.charAt(c) == '1')
							arr[i+x+1][j+y] = 1;
						else
							arr[i+x+1][j+y] = 0;
					} else {
						if(word.charAt(c) == '1')
							arr[i+x][j+y] = 1;
						else
							arr[i+x][j+y] = 0;
					}

					c --;
				}
				
			}
		}else {
			for(int i = 0; i < 4;i ++) {
				for(int j = 0; j < 2;j++) {
					if(i < 2) {
						if(word.charAt((word.length()-1)-(i*2+j)) == '1')
							arr[i+x][j+y] = 1;
						else
							arr[i+x][j+y] = 0;
					}else {
						if(word.charAt((word.length()-1)-(i*2+j)) == '1')
							arr[i+x+1][j+y] = 1;
						else
							arr[i+x+1][j+y] = 0;
					}

				}
			}
		}
	}
	static String toBinaryFixLength(int num,int len) {
		String str = Integer.toBinaryString(num);
		if(str.length() > len) {
			return str.substring(str.length() - len);
		}else {
			for(int i = str.length();i < len ; i++) {
				str  = "0"+str;
			}
		}

		return str;
	}
	
	static int[][] maskGen(){
		int[][] mask = new int[21][21];
		for(int i = 0;i < mask.length;i ++) {
			for(int j = 0;j < mask.length;j ++) {
				if(i%2==0 && j%2==0)
					mask[i][j] = 1;
				else if(i%2==1 && j%2==1) {
					mask[i][j] = 1;
				}
			}
		}
		for(int i = 0;i < 9;i ++) {
			for(int j =0 ; j < 9;j ++) {
				mask[i+0][j+0] = 0;
			}
		}
		for(int i = 0;i < 8;i ++) {
			for(int j =0 ; j < 8;j ++) {
				mask[i+13][j+0] = 0;
				mask[i+0][j+13] = 0;
			}
		}
		return mask;
	}
	
	static void XOR(int[][] arr,int[][] mask) {
		for(int i = 0; i < arr.length;i ++) {
			for(int j = 0; j < arr[i].length;j++) {
				if((arr[i][j]==1 && mask[i][j]==0)||(arr[i][j]==0 && mask[i][j]==1))
					arr[i][j] = 1;
				else
					arr[i][j] = 0;
					
			}
		}
	}
	
	static void drawFormatBits(int[][] arr) {
		int[] horizontal0 = {1,1,1,0,1,1};
		int[] horizontal1 = {1,1};
		int[] horizontal2 = {1,1,0,0,0,1,0,0};
		int[] vertical0 = {0,0,1,0,0,0,0};
		int[] vertical1 = {1,1};
		int[] vertical2 = {1,1,1,1,0,1,1,1};
		
		for(int i = 0;i < horizontal0.length;i ++) {
			arr[8][i] = horizontal0[i];
		}
		for(int i = 0;i < horizontal1.length;i ++) {
			arr[8][i+7] = horizontal1[i];
		}
		for(int i = 0;i < horizontal2.length;i ++) {
			arr[8][i+13] = horizontal2[i];
		}
		for(int i = 0;i < vertical0.length;i ++) {
			arr[i][8] = vertical0[i];
		}
		for(int i = 0;i < vertical1.length;i ++) {
			arr[i+7][8] = vertical1[i];
		}
		for(int i = 0;i < vertical2.length;i ++) {
			arr[i+13][8] = vertical2[i];
		}
	}
	static void drawTimingBits(int[][] arr) {
		int[] bits = {1,0,1,0,1};
		for(int i = 0;i < bits.length;i ++) {
			arr[6][i+8] = bits[i];
		}
		for(int i = 0;i < bits.length;i ++) {
			arr[i+8][6] = bits[i];
		}
	}
}
