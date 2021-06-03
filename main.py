from sklearn.datasets import load_iris
import math

class m_KNN:
    gaits = [] # gait's list

#제곱근을 이용해 각센서값의 x, y, z축에 거리 값을 산출
    def CalculateDistance(self, gait1, gait2): # Get gait <-> gait distance
        gx = math.pow(gait1.GyroscopeX - gait2.GyroscopeX, 2)
        gy = math.pow(gait1.GyroscopeY - gait2.GyroscopeY, 2)
        gz = math.pow(gait1.GyroscopeZ - gait2.GyroscopeZ, 2)
        ax = math.pow(gait1.AccelerometerX - gait2.AccelerometerX, 2)
        ay = math.pow(gait1.AccelerometerY - gait2.AccelerometerY, 2)
        az = math.pow(gait1.AccelerometerZ - gait2.AccelerometerZ, 2)
        mx = math.pow(gait1.MagnetometerX - gait2.MagnetometerX, 2)
        my = math.pow(gait1.MagnetometerY - gait2.MagnetometerY, 2)
        mz = math.pow(gait1.MagnetometerZ - gait2.MagnetometerZ, 2)
        return math.sqrt(gx+gy+gz+ax+ay+az+mx+my+mz)

    def GetNearestList(self, gait, k): # Get the nearest data list number of K from test data
        distanceDataList = []
        nearestDataList = []

        for i in range(len(self.gaits)): # for making test data <-> training data's distance list
            distanceDataList.append(self.CalculateDistance(self.gaits[i], gait))

        for i in range(k): # for making the NearestDataList number of K
            nearestDataList.append(distanceDataList.index(min(distanceDataList)))
            distanceDataList.remove(min(distanceDataList))

        return nearestDataList

    def ObtainMajorityVote(self, answer): # Get test data's class by obtain-majority-vote
        targetClassList = []

        for i in range(len(answer)):
            targetClassList.append(self.gaits[answer[i]].targetClass)

        maxIdx = 0
        maxCount = targetClassList.count(0)

        for i in range(1, 3):
            if(maxCount < targetClassList.count(i)):
                maxIdx = i
                maxCount = targetClassList.count(i)

        return targetClassList[maxIdx]

    def WeightedMajorityVote(self, answer): # Get test data's class by weighted-majority-vote
        targetClassList = []

        bias = -0.5 #편향

        weight0 = 0.2 # 가중치
        weight1 = 0.3
        weight2 = 0.5

        length = len(answer)
        for i in range(length):
            targetClassList.append(self.gaits[answer[i]].targetClass)

        setosaCount = targetClassList[:length//3].count(0) * weight2 + targetClassList[length//3:2*length//3].count(0) * weight1 + targetClassList[2*length//3:].count(0) * weight0 + bias
        versicolorCount = targetClassList[:length//3].count(1) * weight2 +targetClassList[length//3:2*length//3].count(1) * weight1 + targetClassList[2*length//3:].count(1) * weight0 + bias
        virginicaCount = targetClassList[:length//3].count(2) * weight2 +targetClassList[length//3:2*length//3].count(2) * weight1 + targetClassList[2*length//3:].count(2) * weight0 + bias

        maxIdx = 0

        if(versicolorCount > setosaCount and versicolorCount > virginicaCount) :
            maxIdx = 1

        if(virginicaCount > setosaCount and virginicaCount > versicolorCount):
            maxIdx = 2

        return targetClassList[maxIdx]



class GaitData: # gaitdata 1 row
    def __init__(self, data, targetClass):
        self.GyroscopeX = data[0]
        self.GyroscopeY = data[1]
        self.GyroscopeZ = data[2]
        self.AccelerometerX = data[3]
        self.AccelerometerY = data[4]
        self.AccelerometerZ = data[5]
        self.MagnetometerX = data[6]
        self.MagnetometerY = data[7]
        self.MagnetometerZ = data[8]
        self.targetClass = targetClass

m_knn = m_KNN()

#knn알고리즘의 사용자 정의함수 = k정의(하드코딩)
#홀수 중 작은 값이 대체로 이상적이므로 적절히 수정 필요
k = 3

print("\nObtain Majority Vote\n\n")

for t in range(10): # test data push and print - obtain majority vote
    print("Test Data Index is", t, end = ' / ')
    print("Computed Class is", m_knn.ObtainMajorityVote(m_knn.GetNearestList(GaitData(iris.data[iter], iris.target[iter]), k)), end = ' / ')
    print("True Class is", iris.target_names[iris.target[iter]], "\n")

print("\nWeighted Majority Vote\n\n")

for t in range(10): # test data push and print - weighted majority vote
    print("Test Data Index is", t, end=' / ')
    print("Computed Class is", m_knn.WeightedMajorityVote(m_knn.GetNearestList(GaitData(iris.data[iter], iris.target[iter]),k)), end = ' / ')
    print("True Class is", targetClassList[iris.target[iter]], "\n")
