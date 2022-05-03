from imageai.Classification import ImageClassification
import os
#               0               1               2           3         4            5            6
testPics = ['sample1.png', 'sample2.jpg','building.jpg','dog.jpg','flag.jpg','musician.jpg','usi.png']
#               0               1                  2                3           
models = ['DenseNet121.h5','InceptionV3.h5','Mobilenet_V2.h5','ResNet50.h5']

def getPrecisePrediction(imageFileName):
    execution_path = os.getcwd()
    prediction = ImageClassification()
    prediction.setModelTypeAsDenseNet()
    prediction.setModelPath(execution_path +'\\model\\' + models[0])
    prediction.loadModel() #Normal speed is default
    imagePath = execution_path +"//images//" + imageFileName 
    predictions, probabilities = prediction.classifyImage(imagePath,result_count=2)
    myPrediction = predictions[0] + " " + str(round(probabilities[0]))
    print('////////////////////////////////////////')
    #print(myPrediction)
    print(imageFileName)
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction , " : " , eachProbability)
    print('////////////////////////////////////////')
    return myPrediction


def getFastPrediction(imageFileName):
    execution_path = os.getcwd()
    prediction = ImageClassification()
    prediction.setModelTypeAsMobileNetV2()
    prediction.setModelPath(execution_path + "\\model\\"+ models[2])
    prediction.loadModel() #Default is Normal. We have other speeds available. "Faster" is available tho it is not very accurate
    predictions, probabilities = prediction.classifyImage(execution_path +"//images//" + imageFileName, result_count=2)
    myPrediction = predictions[0] + " " + str(round(probabilities[0]))
    print('////////////////////////////////////////')
    #print(myPrediction)
    print(imageFileName)
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction , "  : " , eachProbability)
    print('////////////////////////////////////////')
    return myPrediction

def getPrediction(isPrecise):
    if isPrecise == True:
        print("Precision Prediction")
        predict = getPrecisePrediction()
    else:
        print("Fast Prediction")
        predict = getFastPrediction()
        print(predict)

#getPrediction(isPrecise=True)

def ImageArray():
    return getSinglePrediction()

def getSinglePrediction():
    execution_path = os.getcwd()
    prediction = ImageClassification()
    prediction.setModelTypeAsInceptionV3()
    prediction.setModelPath(execution_path +'\\model\\'+models[1])
    prediction.loadModel() #Normal speed is default
    predictions, probabilities = prediction.classifyImage(execution_path +"//images//" + testPics[0], result_count=3)
    return predictions[0]
    print ('Picture: ' + currentPicture + " is " +predictions[0] + " " + str(round(probabilities[0])))

for image in testPics:
    getFastPrediction(image)