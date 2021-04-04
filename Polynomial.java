
public class Polynomial {
	int order;
	int[] coefficients;
	
	
	Polynomial(int[] coefficients){
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
	
	Polynomial mul(Polynomial poly) {
		int[] resultCoefficients = new int[poly.order * this.order];
		for(int i = 0; i < this.order;i++) {
			for(int j = 0; j < poly.order;j++) {
				resultCoefficients[i+j] =  coefficients[i] * poly.coefficients[j];
			}
		}
		Polynomial result = new Polynomial(resultCoefficients);
		return result;
	}
	
	Polynomial xor(Polynomial poly) {
		int[] resultCoefficients = new int[poly.order * this.order];
		for(int i = 0; i < this.order;i++) {
			resultCoefficients[i] =  (int)((byte)coefficients[i] ^ (byte)poly.coefficients[i]);
		}
		Polynomial result = new Polynomial(resultCoefficients);
		return result;
	}
	
	Polynomial[] div(Polynomial poly) {
		for(int order = this.order;order <= poly.order; order --) {
			
		}
	}
	
	int[] removeLeadingZero(int[] arr) {
		boolean nonZeroFound = false;
		int[] newCoefficients = null;
		for(int i = arr.length -1;i >= 0; i--) {
			if(arr[i] != 0 || nonZeroFound) {
				nonZeroFound = true;
				newCoefficients = new int[i+1];
				newCoefficients[i] = arr[i];
			}
		}
		return newCoefficients;
	}
	
	public String toString() {
		String str = "";
		for(int i = 0; i < this.coefficients.length; i++) {
			str = this.coefficients[i] + " " + str;
		}
		return str;
	}
}
