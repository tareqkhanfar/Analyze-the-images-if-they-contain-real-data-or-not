
import re
import numpy as np

class Model:
    @staticmethod
    def messageToBinary ( message):
      if (type(message)==str):
        return "".join([format(ord(i) , "08b") for i in message])
      elif (type(message)==bytes or type(message)==np.ndarray):
          return [format (i , "08b") for i in message]
      elif (type(message)==int or type (message) == np.uint8):
        return format (message , "08b")
      else :
        raise TypeError ("Error Message !! ")
#######################################################################################################
    @staticmethod
    def showData (image):
        print ("TEST 4 ")

        binary_data = ""
        for values in image :
            for pixel in values :
                r , g, b =  Model.messageToBinary(pixel)
                binary_data += r[-1]
                binary_data += g[-1]
                binary_data += b[-1]


        all_bytes = [binary_data[i:i+8] for i in range (0 , len (binary_data ) , 8)]
        decoded_data = ""
        for byte in all_bytes :
            decoded_data += chr (int (byte , 2))
            if (decoded_data[-5:] == "#####"):
                break
        #print (decoded_data[-5:])
        return decoded_data[:-5]
#######################################################################################################
    @staticmethod
    def similarity(  string1, string2):
        m = len(string1)
        n = len(string2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif string1[i - 1] == string2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] ) + 1

        distance = dp[m][n]
        max_len = max(m, n)
        similarity = 100.0 - (distance / max_len) * 100
        return similarity
#######################################################################################################
    @staticmethod
    def Data_IS_REAL(plainText) :
        print("TEST 99")
        text=""
        with open('data.txt') as f:
            text = f.readlines()
        
        text = ''.join(text)
        x = Model.generate_ngrams(text , len(text))
        max_sim = 0
        str=""
        for i in x :
            percentage = Model.similarity(plainText , i)
            if (percentage > max_sim) :
                max_sim = percentage
                str = i
         

        return str , max_sim
      #print ("the Percentage is = " , max_sim) 
        #print ("the Word is = " , str) 
#######################################################################################################
    @staticmethod
    def generate_ngrams( text, max_n):
        sentences = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', text)
        output = []
        for sentence in sentences:
            words = sentence.split()
            for n in range(1, max_n+1):
                for i in range(len(words)-n+1):
                    output.append(" ".join(words[i:i+n]))
        return output

#######################################################################################################


    @staticmethod
    def jaccardAlgorithm (PlainText , DummyData) :
        #print (DummyData)
        print (PlainText)


        #DummyData = re.sub(r'[\|]', '', DummyData)
        #PlainText = re.sub(r'[\|/]', '', PlainText)

       
        set1 = set(DummyData)
        set2 = set(PlainText)
        intersection = len(set1 & set2)
        union = len(set1 | set2)

        result = float(intersection) / union

        print(intersection)
        print(union)

        return result * 100











