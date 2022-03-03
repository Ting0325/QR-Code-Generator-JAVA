import numpy as np
import cv2
class Driver :
    @staticmethod
    def main( args) :
        size = 21
        pattern = [[0] * (size) for _ in range(size)]
        pattern = Driver.patternGen()
        Driver.printArr2d(pattern)
        a = np.array(pattern)
        a = a - 1
        a = a * (-1)
        a = a * 255
        print(a)
        a = np.stack((a,a,a),axis=-1)
        cv2.imwrite('my_qrcode.jpg',a)
        img = cv2.imread('my_qrcode.jpg')
        #img = cv2.resize(img,(210,210))
        cv2.imshow('test',img)
        cv2.waitKey(0)
    @staticmethod
    def printArr( arr) :
        i = 0
        while (i < len(arr)) :
            print(str(arr[i]) + " ", end ="")
            i += 1
    @staticmethod
    def printArr2d( arr) :
        i = 0
        while (i < len(arr)) :
            j = 0
            while (j < len(arr[i])) :
                print(str(arr[i][j]) + " ", end ="")
                j += 1
            print()
            i += 1
    @staticmethod
    def  patternGen() :
        # Scanner sc = new Scanner(System.in);
        pattern = [[0] * (21) for _ in range(21)]
        # String encodedWord = "0100000100010100100001100101011011000110110001101111001011000010000001110111011011110111001001101100011001000010000100100000001100010011001000110011000010000101101010010101111000000111000010100011011011001001";
        # String encodedWord = "0100000011100100111001110101011101000111001100100000010010010110111001110011011101000110100101110100011101010111010001100101000011101100000100011110110011010000100011111000010110111000000010011001101100010101";
        text = "Hello, world! 123"
        # String text = "nuts.epass2u.com/";
        print("INPUT TEXT:")
        # String text = sc.next();
        if (len(text) > 17) :
            text = text[0:18]
        #print("text.length(): " + str(len(text)))
        #print("text.length() binary: " + Driver.toBinaryFixLength(len(text), 8))
        # String text = "google.com";
        encodedWord = ""
        # mode
        encodedWord = "0100"
        # character count 17
        # encodedWord = encodedWord + "00010001";
        # encodedWord = encodedWord + "00001010";
        encodedWord = encodedWord + Driver.toBinaryFixLength(len(text), 8)
        # encode characters
        # 		System.out.println(text.charAt(0));
        # 		System.out.println((int)(text.charAt(0)));
        # 		System.out.println(toBinaryFixLength((int)text.charAt(0),8));
        i = 0
        while (i < len(text)) :
            encodedWord = encodedWord + Driver.toBinaryFixLength(ord(text[i]), 8)
            i += 1
        # 		for(int i = 0; i < 10;i ++) {
        # 			encodedWord = encodedWord + toBinaryFixLength((int)text.charAt(i),8);
        # 		}
        # byte padding to 152 bits = 19 bytes
        i = 0
        while (i < 17 - len(text)) :
            encodedWord = encodedWord + "00000000"
            i += 1
        # end sequence
        encodedWord = encodedWord + "0000"
        # get message poly
        # System.out.println("len: "+encodedWord.length());
        message = [0] * (19)
        i = 0
        while (i < 19) :
            #message[18 - i] = Integer.parseInt(encodedWord[i * 8:i * 8 + 8],2)
            message[18 - i] = int(encodedWord[i * 8:i * 8 + 8], 2)
            i += 1
        # System.out.println("message poly");
        # printArr(message);
        # System.out.println("encodedWord:"+encodedWord);
        # ECC codewords
        # String ecc = "10000101101010010101111000000111000010100011011011001001";
        # String ecc = "11010000100011111000010110111000000010011001101100010101";
        # int[] message = {17,236,17,236,17,236,64,67,77,220,114,209,120,11,91,32};
        ten = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        seven = [0, 0, 0, 0, 0, 0, 0, 1]
        # int[] generatorExp = {45,32,94,64,70,118,61,46,67,251,0};
        generatorExp = [21, 102, 238, 149, 146, 229, 87, 0]
        polyMessage = Polynomial(message, None, False)
        polyTen = Polynomial(seven, None, False)
        polyGen = Polynomial(None, generatorExp, True)
        b0 = int(243)
        b1 = int(159)
        print("GF")
        print(GF256.table[24])

        polyMessage = polyMessage.mul(Driver.sengleTermPoly(1, 7))
        polyEcc = polyMessage.div(polyGen)[1]
        ecc = ""
        i = 0
        while (i < 7) :
            ecc = Driver.toBinaryFixLength(polyEcc.coefficients[i], 8) + ecc
            i += 1
        # System.out.println("ecc:\n"+ecc);
        encodedWord = encodedWord + ecc
        # System.out.println(encodedWord);
        Driver.drawBrick(pattern, 0, 0)
        Driver.drawBrick(pattern, 14, 0)
        Driver.drawBrick(pattern, 0, 14)
        # drawCodeWord(pattern, 17, 19, 1, "hello");
        Driver.drawCodeWordNoConvert(pattern, 17, 19, 0, encodedWord[0:8])
        Driver.drawCodeWordNoConvert(pattern, 13, 19, 0, encodedWord[8:16])
        Driver.drawCodeWordNoConvert(pattern, 9, 19, 0, encodedWord[16:24])
        Driver.drawCodeWordNoConvert(pattern, 9, 17, 1, encodedWord[24:32])
        Driver.drawCodeWordNoConvert(pattern, 13, 17, 1, encodedWord[32:40])
        Driver.drawCodeWordNoConvert(pattern, 17, 17, 1, encodedWord[40:48])
        Driver.drawCodeWordNoConvert(pattern, 17, 15, 0, encodedWord[48:56])
        Driver.drawCodeWordNoConvert(pattern, 13, 15, 0, encodedWord[56:64])
        Driver.drawCodeWordNoConvert(pattern, 9, 15, 0, encodedWord[64:72])
        Driver.drawCodeWordNoConvert(pattern, 9, 13, 1, encodedWord[72:80])
        Driver.drawCodeWordNoConvert(pattern, 13, 13, 1, encodedWord[80:88])
        Driver.drawCodeWordNoConvert(pattern, 17, 13, 1, encodedWord[88:96])
        Driver.drawCodeWordNoConvert(pattern, 17, 11, 0, encodedWord[96:104])
        Driver.drawCodeWordNoConvert(pattern, 13, 11, 0, encodedWord[104:112])
        Driver.drawCodeWordNoConvert(pattern, 9, 11, 0, encodedWord[112:120])
        Driver.drawCodeWordNoConvertSpecial(pattern, 4, 11, 0, encodedWord[120:128])
        Driver.drawCodeWordNoConvert(pattern, 0, 11, 0, encodedWord[128:136])
        Driver.drawCodeWordNoConvert(pattern, 0, 9, 1, encodedWord[136:144])
        Driver.drawCodeWordNoConvertSpecial(pattern, 4, 9, 1, encodedWord[144:152])
        Driver.drawCodeWordNoConvert(pattern, 9, 9, 1, encodedWord[152:160])
        Driver.drawCodeWordNoConvert(pattern, 13, 9, 1, encodedWord[160:168])
        Driver.drawCodeWordNoConvert(pattern, 17, 9, 1, encodedWord[168:176])
        Driver.drawCodeWordNoConvert(pattern, 9, 7, 0, encodedWord[176:184])
        Driver.drawCodeWordNoConvert(pattern, 9, 4, 1, encodedWord[184:192])
        Driver.drawCodeWordNoConvert(pattern, 9, 2, 0, encodedWord[192:200])
        Driver.drawCodeWordNoConvert(pattern, 9, 0, 1, encodedWord[200:208])
        # drawCodeWord(pattern, 17, 19, 1, "hello");
        mask = Driver.maskGen()
        Driver.printArr2d(mask)
        Driver.XOR(pattern, mask)
        Driver.drawFormatBits(pattern)
        Driver.drawTimingBits(pattern)
        print()
        return pattern
    @staticmethod
    def drawBrick( arr,  x,  y) :
        i = 0
        while (i < 7) :
            j = 0
            while (j < 7) :
                if ((i == 1 and j > 0 and j < 6) or (i == 5 and j != 0 and j != 6) or (i > 0 and i < 6 and (j == 1 or j == 5))) :
                    arr[i + x][j + y] = 0
                else :
                    arr[i + x][j + y] = 1
                j += 1
            i += 1
    @staticmethod
    def drawCodeWordNoConvert( arr,  x,  y,  type,  word) :
        if (type == 1) :
            c = 7
            i = 3
            while (i >= 0) :
                j = 0
                while (j < 2) :
                    # System.out.println(i*2+j);
                    if (word[c] == '1') :
                        arr[i + x][j + y] = 1
                    else :
                        arr[i + x][j + y] = 0
                    c -= 1
                    j += 1
                i -= 1
        else :
            i = 0
            while (i < 4) :
                j = 0
                while (j < 2) :
                    if (word[(len(word) - 1) - (i * 2 + j)] == '1') :
                        arr[i + x][j + y] = 1
                    else :
                        arr[i + x][j + y] = 0
                    j += 1
                i += 1
    @staticmethod
    def drawCodeWord( arr,  x,  y,  type,  word) :
        word = Driver.toBinaryFixLength(137, 8)
        if (type == 1) :
            c = 7
            i = 3
            while (i >= 0) :
                j = 0
                while (j < 2) :
                    print(i * 2 + j)
                    if (word[c] == '1') :
                        arr[i + x][j + y] = 1
                    else :
                        arr[i + x][j + y] = 0
                    c -= 1
                    j += 1
                i -= 1
        else :
            i = 0
            while (i < 4) :
                j = 0
                while (j < 2) :
                    if (word[(len(word) - 1) - (i * 2 + j)] == '1') :
                        arr[i + x][j + y] = 1
                    else :
                        arr[i + x][j + y] = 0
                    j += 1
                i += 1
    @staticmethod
    def drawCodeWordNoConvertSpecial( arr,  x,  y,  type,  word) :
        if (type == 1) :
            c = 7
            i = 3
            while (i >= 0) :
                j = 0
                while (j < 2) :
                    # System.out.println(i*2+j);
                    if (i > 1) :
                        if (word[c] == '1') :
                            arr[i + x + 1][j + y] = 1
                        else :
                            arr[i + x + 1][j + y] = 0
                    else :
                        if (word[c] == '1') :
                            arr[i + x][j + y] = 1
                        else :
                            arr[i + x][j + y] = 0
                    c -= 1
                    j += 1
                i -= 1
        else :
            i = 0
            while (i < 4) :
                j = 0
                while (j < 2) :
                    if (i < 2) :
                        if (word[(len(word) - 1) - (i * 2 + j)] == '1') :
                            arr[i + x][j + y] = 1
                        else :
                            arr[i + x][j + y] = 0
                    else :
                        if (word[(len(word) - 1) - (i * 2 + j)] == '1') :
                            arr[i + x + 1][j + y] = 1
                        else :
                            arr[i + x + 1][j + y] = 0
                    j += 1
                i += 1
    @staticmethod
    def  toBinaryFixLength( num,  len) :
        return format(num,'08b')
    @staticmethod
    def  maskGen() :
        mask = [[0] * (21) for _ in range(21)]
        i = 0
        while (i < len(mask)) :
            j = 0
            while (j < len(mask)) :
                if (i % 2 == 0 and j % 2 == 0) :
                    mask[i][j] = 1
                elif(i % 2 == 1 and j % 2 == 1) :
                        mask[i][j] = 1
                j += 1
            i += 1
        i = 0
        while (i < 9) :
            j = 0
            while (j < 9) :
                mask[i + 0][j + 0] = 0
                j += 1
            i += 1
        i = 0
        while (i < 8) :
            j = 0
            while (j < 8) :
                mask[i + 13][j + 0] = 0
                mask[i + 0][j + 13] = 0
                j += 1
            i += 1
        return mask
    @staticmethod
    def XOR( arr,  mask) :
        i = 0
        while (i < len(arr)) :
            j = 0
            while (j < len(arr[i])) :
                if ((arr[i][j] == 1 and mask[i][j] == 0) or (arr[i][j] == 0 and mask[i][j] == 1)) :
                    arr[i][j] = 1
                else :
                    arr[i][j] = 0
                j += 1
            i += 1
    @staticmethod
    def drawFormatBits( arr) :
        horizontal0 = [1, 1, 1, 0, 1, 1]
        horizontal1 = [1, 1]
        horizontal2 = [1, 1, 0, 0, 0, 1, 0, 0]
        vertical0 = [0, 0, 1, 0, 0, 0, 0]
        vertical1 = [1, 1]
        vertical2 = [1, 1, 1, 1, 0, 1, 1, 1]
        i = 0
        while (i < len(horizontal0)) :
            arr[8][i] = horizontal0[i]
            i += 1
        i = 0
        while (i < len(horizontal1)) :
            arr[8][i + 7] = horizontal1[i]
            i += 1
        i = 0
        while (i < len(horizontal2)) :
            arr[8][i + 13] = horizontal2[i]
            i += 1
        i = 0
        while (i < len(vertical0)) :
            arr[i][8] = vertical0[i]
            i += 1
        i = 0
        while (i < len(vertical1)) :
            arr[i + 7][8] = vertical1[i]
            i += 1
        i = 0
        while (i < len(vertical2)) :
            arr[i + 13][8] = vertical2[i]
            i += 1
    @staticmethod
    def drawTimingBits( arr) :
        bits = [1, 0, 1, 0, 1]
        i = 0
        while (i < len(bits)) :
            arr[6][i + 8] = bits[i]
            i += 1
        i = 0
        while (i < len(bits)) :
            arr[i + 8][6] = bits[i]
            i += 1
    @staticmethod
    def  sengleTermPoly( coefficient,  order) :
        coe = [0] * (order + 1)
        coe[order] = coefficient
        return Polynomial(coe,None,False)
class Polynomial :
    order = 0
    coefficients = None
    '''
    def __init__(self, coefficients) :
        self.coefficients = coefficients
        self.order = len(coefficients)
    '''
    def __init__(self, coefficients, coefficientsExp,  isExp) :
        if isExp:
            coefficients = [0] * (len(coefficientsExp))
            i = 0
            while (i < len(coefficientsExp)) :
                coefficients[i] = GF256.table[coefficientsExp[i]]
                i += 1
        self.coefficients = coefficients
        self.order = len(coefficients)
    
    def  add(self, poly) :
        resultCoefficients = None
        resultCoefficients = [0] * (len(self.coefficients)) if (len(self.coefficients) > len(poly.coefficients)) else [0] * (len(poly.coefficients))
        i = 0
        while (i < len(resultCoefficients)) :
            if (i < len(self.coefficients)) :
                resultCoefficients[i] += self.coefficients[i]
            if (i < len(poly.coefficients)) :
                resultCoefficients[i] += poly.coefficients[i]
            i += 1
        result = Polynomial(resultCoefficients,None,False)
        return result
    def  sub(self, poly) :
        resultCoefficients = None
        resultCoefficients = [0] * (len(self.coefficients)) if (len(self.coefficients) > len(poly.coefficients)) else [0] * (len(poly.coefficients))
        i = 0
        while (i < len(resultCoefficients)) :
            if (i < len(self.coefficients)) :
                if (i < len(poly.coefficients)) :
                    resultCoefficients[i] = self.coefficients[i] - poly.coefficients[i]
                else :
                    resultCoefficients[i] = self.coefficients[i]
            else :
                if (i < len(poly.coefficients)) :
                    resultCoefficients[i] = 0 - poly.coefficients[i]
                else :
                    resultCoefficients[i] = 0
            i += 1
        result = Polynomial(self.removeLeadingZero(resultCoefficients))
        return result
    def  xor(self, poly) :
        resultCoefficients = None
        resultCoefficients = [0] * (len(self.coefficients)) if (len(self.coefficients) > len(poly.coefficients)) else [0] * (len(poly.coefficients))
        i = 0
        while (i < len(resultCoefficients)) :
            if (i < len(self.coefficients)) :
                if (i < len(poly.coefficients)) :
                    resultCoefficients[i] = int((int(self.coefficients[i]) ^ int(poly.coefficients[i]))) & 255
                    if (resultCoefficients[i] < 0) :
                        print("resultCoefficients[i]+ " + str(resultCoefficients[i]))
                        print("(byte)this.coefficients[i] ^ (byte)poly.coefficients[i]+ " + str((int((int(self.coefficients[i]) ^ int(poly.coefficients[i]))) & 255)))
                else :
                    resultCoefficients[i] = self.coefficients[i]
            else :
                if (i < len(poly.coefficients)) :
                    resultCoefficients[i] = 0 - poly.coefficients[i]
                else :
                    resultCoefficients[i] = 0
            i += 1
        result = Polynomial(self.removeLeadingZero(resultCoefficients),None,False)
        return result
    def  mul(self, poly) :
        resultCoefficients = [0] * (poly.order + self.order - 1)
        i = 0
        while (i < self.order) :
            j = 0
            while (j < poly.order) :
                resultCoefficients[i + j] += self.coefficients[i] * poly.coefficients[j]
                j += 1
            i += 1
        result = Polynomial(resultCoefficients,None,False)
        return result
    def  mulGF(self, poly) :
        resultCoefficients = [0] * (poly.order + self.order - 1)
        i = 0
        while (i < self.order) :
            j = 0
            while (j < poly.order) :
                if (self.coefficients[i] != 0 and poly.coefficients[j] != 0) :
                    resultCoefficients[i + j] += GF256.table[(GF256.antiTable(self.coefficients[i]) + GF256.antiTable(poly.coefficients[j])) % 255]
                else :
                    resultCoefficients[i + j] += 0
                j += 1
            i += 1
        result = Polynomial(resultCoefficients,None,False)
        return result
    def  div(self, poly) :
        quotientCoefficients = [0] * (self.order - poly.order)
        remainder = Polynomial(self.coefficients,None,False)
        quotent = Polynomial(quotientCoefficients,None,False)
        ans = [quotent, remainder]
        order = self.order - poly.order + 1
        while (order > 0) :
            # for(int order = this.order - poly.order + 1;order >= this.order - poly.order; order --) {
            c = [0] * (order)
            c[order - 1] = remainder.coefficients[len(remainder.coefficients) - 1]
            q = Polynomial(c,None,False)
            quotent = quotent.add(q)
            remainder = remainder.xor(poly.mulGF(q))
            ans[0] = quotent
            ans[1] = remainder
            order -= 1
        return ans
    def  removeLeadingZero(self, arr) :
        offset = 0
        i = len(arr) - 1
        while (i >= 0) :
            if (arr[i] != 0) :
                break
            offset += 1
            i -= 1
        newCoefficients = [0] * (len(arr) - offset)
        i = 0
        while (i < len(newCoefficients)) :
            newCoefficients[i] = arr[i]
            i += 1
        return newCoefficients
    def  toString(self) :
        str0 = ""
        str1 = ""
        i = 0
        while (i < len(self.coefficients)) :
            str0 = str(self.coefficients[i]) + "x" + str(i) + " " + str0
            i += 1
        str0 = str0 + "\n"
        i = 0
        while (i < len(self.coefficients)) :
            str1 = str(GF256.antiTable(self.coefficients[i])) + "ax" + str(i) + " " + str1
            i += 1
        return str0 + str1
class GF256 :
    table = [1, 2, 4, 8, 16, 32, 64, 128, 29, 58, 116, 232, 205, 135, 19, 38, 76, 152, 45, 90, 180, 117, 234, 201, 143, 3, 6, 12, 24, 48, 96, 192, 157, 39, 78, 156, 37, 74, 148, 53, 106, 212, 181, 119, 238, 193, 159, 35, 70, 140, 5, 10, 20, 40, 80, 160, 93, 186, 105, 210, 185, 111, 222, 161, 95, 190, 97, 194, 153, 47, 94, 188, 101, 202, 137, 15, 30, 60, 120, 240, 253, 231, 211, 187, 107, 214, 177, 127, 254, 225, 223, 163, 91, 182, 113, 226, 217, 175, 67, 134, 17, 34, 68, 136, 13, 26, 52, 104, 208, 189, 103, 206, 129, 31, 62, 124, 248, 237, 199, 147, 59, 118, 236, 197, 151, 51, 102, 204, 133, 23, 46, 92, 184, 109, 218, 169, 79, 158, 33, 66, 132, 21, 42, 84, 168, 77, 154, 41, 82, 164, 85, 170, 73, 146, 57, 114, 228, 213, 183, 115, 230, 209, 191, 99, 198, 145, 63, 126, 252, 229, 215, 179, 123, 246, 241, 255, 227, 219, 171, 75, 150, 49, 98, 196, 149, 55, 110, 220, 165, 87, 174, 65, 130, 25, 50, 100, 200, 141, 7, 14, 28, 56, 112, 224, 221, 167, 83, 166, 81, 162, 89, 178, 121, 242, 249, 239, 195, 155, 43, 86, 172, 69, 138, 9, 18, 36, 72, 144, 61, 122, 244, 245, 247, 243, 251, 235, 203, 139, 11, 22, 44, 88, 176, 125, 250, 233, 207, 131, 27, 54, 108, 216, 173, 71, 142, 1]
    @staticmethod
    def  antiTable( integer) :
        i = 0
        while (i < len(GF256.table)) :
            if (GF256.table[i] == integer) :
                return i
            i += 1
        return 0
    

if __name__=="__main__":
    Driver.main([])