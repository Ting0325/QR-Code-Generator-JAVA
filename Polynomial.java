
public class Polynomial {
	int order;
	int[] coefficients;
	
	Polynomial(int[] coefficients){
		this.coefficients = coefficients;
		this.order = coefficients.length;
	}
	
	Polynomial(int[] coefficientsExp,boolean isExp ){
		int[] coefficients = new int[coefficientsExp.length];
		for(int i = 0; i < coefficientsExp.length;i ++) {
			coefficients[i] = GF256.table[coefficientsExp[i]];		
		}
		this.coefficients = coefficients;
		this.order = coefficients.length;
	}
	
	Polynomial add(Polynomial poly) {
		int[] resultCoefficients = null;		
		resultCoefficients = (this.coefficients.length>poly.coefficients.length)? new int[this.coefficients.length]:new int[poly.coefficients.length];
		for(int i = 0; i < resultCoefficients.length;i++) {
			if( i < this.coefficients.length)
				resultCoefficients[i] += this.coefficients[i];
			if( i < poly.coefficients.length)
				resultCoefficients[i] += poly.coefficients[i];	
		}
		Polynomial result = new Polynomial(resultCoefficients);
		return result;		
	}
	
	Polynomial sub(Polynomial poly) {
		int[] resultCoefficients = null;		
		resultCoefficients = (this.coefficients.length>poly.coefficients.length)? new int[this.coefficients.length]:new int[poly.coefficients.length];
		for(int i = 0; i < resultCoefficients.length;i++) {
			if( i < this.coefficients.length) {
				if(i < poly.coefficients.length) {
					resultCoefficients[i] = this.coefficients[i] - poly.coefficients[i];
				}else {
					resultCoefficients[i] = this.coefficients[i];
				}
			}else {
				if(i < poly.coefficients.length) {
					resultCoefficients[i] = 0 - poly.coefficients[i];
				}else {
					resultCoefficients[i] = 0;
				}
			}
				
				
		}
		Polynomial result = new Polynomial(resultCoefficients);
		return result;		
	}
	
	Polynomial xor(Polynomial poly) {
		int[] resultCoefficients = null;		
		resultCoefficients = (this.coefficients.length>poly.coefficients.length)? new int[this.coefficients.length]:new int[poly.coefficients.length];
		for(int i = 0; i < resultCoefficients.length;i++) {
			if( i < this.coefficients.length) {
				if(i < poly.coefficients.length) {
					resultCoefficients[i] = (int)((byte)this.coefficients[i] ^ (byte)poly.coefficients[i]);
				}else {
					resultCoefficients[i] = this.coefficients[i];
				}
			}else {
				if(i < poly.coefficients.length) {
					resultCoefficients[i] = 0 - poly.coefficients[i];
				}else {
					resultCoefficients[i] = 0;
				}
			}
				
				
		}
		Polynomial result = new Polynomial(resultCoefficients);
		return result;		
	}
	
	Polynomial mul(Polynomial poly) {
		int[] resultCoefficients = new int[poly.order + this.order - 1];
		for(int i = 0; i < this.order;i++) {
			for(int j = 0; j < poly.order;j++) {
				resultCoefficients[i+j] +=  coefficients[i] * poly.coefficients[j];
			}
		}
		Polynomial result = new Polynomial(resultCoefficients);
		return result;
	}
	
	Polynomial mulGF(Polynomial poly) {
		int[] resultCoefficients = new int[poly.order + this.order - 1];
		for(int i = 0; i < this.order;i++) {
			for(int j = 0; j < poly.order;j++) {
				resultCoefficients[i+j] +=  (GF256.antiTable(this.coefficients[i]) * GF256.antiTable(poly.coefficients[j])) % 255;
			}
		}
		Polynomial result = new Polynomial(resultCoefficients);
		return result;
	}
	
	
	Polynomial[] div(Polynomial poly) {
		int[] quotientCoefficients = new int[this.order - poly.order];
		Polynomial remainder = new Polynomial(this.coefficients);
		Polynomial quotent = new Polynomial(quotientCoefficients);
		Polynomial[] ans = {quotent,remainder};
		for(int order = this.order - poly.order + 1;order >= 0; order --) {
			int[] c = new int[order];
			c[order -1] = remainder.coefficients[remainder.coefficients.length -1];
			Polynomial q =  new Polynomial(c);
			quotent = quotent.add(q);
			System.out.println("previous remainder:");
			System.out.println(remainder);
			System.out.println("poly.mul(q):");
			System.out.println(poly.mulGF(q));
			System.out.println("poly:");
			System.out.println(poly);
			remainder = remainder.xor(poly.mul(q));
			System.out.println("quotent:");
			System.out.println(quotent);
			System.out.println("remainder:");
			System.out.println(remainder);
		}
		return ans;
	}
	
	int[] removeLeadingZero(int[] arr) {
		int offset = 0;
		for(int i = arr.length - 1 ;i >= 0; i--){
			if(arr[i] != 0)
				break;
			offset ++;
		}
		int[] newCoefficients = new int[arr.length - offset];
		for(int i = 0; i< newCoefficients.length;i ++){
			newCoefficients[i] = arr[i];
		}
		return newCoefficients;
	}
	
	public String toString() {
		String str = "";
		for(int i = 0; i < this.coefficients.length; i++) {
			str = this.coefficients[i] +"x"+i+" " + str;
		}
		return str;
	}
}
