from imageai.Classification import ImageClassification
import os

testPics = ['sample1.png', 'sample2.jpg','building.jpg','dog.jpg','flag.jpg','musician.jpg']
models = ['DenseNet121.h5','InceptionV3.h5','Mobilenet_V2.h5','ResNet50.h5']


def getPrecisePrediction(imageFileName):
    execution_path = os.getcwd()
    prediction = ImageClassification()
    prediction.setModelTypeAsInceptionV3()
    prediction.setModelPath(execution_path +'\\model\\'+models[2])
    prediction.loadModel() #Normal speed is default
    imagePath = execution_path +"//images//" + testPics[5] 
    predictions, probabilities = prediction.classifyImage(imagePath,result_count=2)
    myPrediction = predictions[0] + " " + str(round(probabilities[0]))
    return myPrediction
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction , " : " , eachProbability)

def getFastPrediction():
    execution_path = os.getcwd()
    prediction = ImageClassification()
    prediction.setModelTypeAsResNet50()
    prediction.setModelPath(execution_path + "\\model\\ResNet50.h5")
    prediction.loadModel("fast") #Default is Normal. We have other speeds available. "Faster" is available tho it is not very accurate
    predictions, probabilities = prediction.classifyImage(execution_path +"//images//" + testPics[4], result_count=3)
    myPrediction = predictions[0] + " " + str(round(probabilities[0]))
    return myPrediction
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction , " : " , eachProbability)

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
    