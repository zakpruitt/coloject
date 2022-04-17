from imageai.Classification import ImageClassification
from heapq import heappop, heappush, heapify
import os


def getNormalPrediction():
    execution_path = os.getcwd()
    prediction = ImageClassification()
    prediction.setModelTypeAsInceptionV3()
    #prediction.setModelPath(os.path.join(execution_path, "\model\resnet50_imagenet_tf.2.0.h5"))
    #prediction.setModelPath(execution_path+"\\model\\InceptionV3.h5")
    print(execution_path +'\\model\\InceptionV3.h5')
    prediction.setModelPath(execution_path +'\\model\\InceptionV3.h5')
    prediction.loadModel()

    predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, "sample1.png"), result_count=5 )
    myPrediction = predictions[0] + " " + str(round(probabilities[0]))
    return myPrediction

    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction , " : " , eachProbability)

def getFastPrediction():
    execution_path = os.getcwd()
    prediction = ImageClassification()
    prediction.setModelTypeAsResNet50()
    prediction.setModelPath(os.path.join(execution_path, "resnet50_imagenet_tf.2.0.h5"))
    prediction.loadModel(prediction_speed="fastest")

    predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, "model/sample1.png"), result_count=5 )
    myPrediction = predictions[0] + " " + str(round(probabilities[0])+"%")
    return myPrediction

    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction , " : " , eachProbability)

def getPrediction(isPrecise):
    if isPrecise == True:
        print("Precision Prediction")
        predict = getNormalPrediction()
    else:
        print("Fast Prediction")
        predict = getFastPrediction()
        print(predict)

getPrediction(isPrecise=True)