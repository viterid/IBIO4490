
# read kaggle facial expression recognition challenge dataset (fer2013.csv)
# https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge
import numpy as np
import matplotlib.pyplot as plt
import sys
import pickle
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.utils.multiclass import unique_labels
from sklearn.metrics import precision_recall_curve
from sklearn.utils.fixes import signature

def sigmoid(x):
    return 1/(1+np.exp(-x))

def get_data():
    # angry, disgust, fear, happy, sad, surprise, neutral
    with open("fer2013.csv") as f:
        content = f.readlines()

    lines = np.array(content)
    num_of_instances = lines.size
    print("number of instances: ",num_of_instances)
    print("instance length: ",len(lines[1].split(",")[1].split(" ")))

    x_train, y_train, x_test, y_test = [], [], [], []

    for i in range(1,num_of_instances):
        emotion, img, usage = lines[i].split(",")
        pixels = np.array(img.split(" "), 'float32')
        emotion = 1 if int(emotion)==3 else 0 # Only for happiness
        if 'Training' in usage:
            y_train.append(emotion)
            x_train.append(pixels)
            
        elif 'PublicTest' in usage:
            y_test.append(emotion)
            x_test.append(pixels)
            
 
    #Validation set is the last 30% of the train set
    setenta= round(len(x_train)*0.7)
        
    x_val= x_train[setenta:-1] 
    y_val= y_train[setenta:-1] 
    
    x_train= x_train[0:(setenta-1)]
    y_train= y_train[0:(setenta-1)]
        
        
        
        

    #------------------------------
    #data transformation for train and test sets
    x_train = np.array(x_train, 'float64')
    y_train = np.array(y_train, 'float64')
    x_test = np.array(x_test, 'float64')
    y_test = np.array(y_test, 'float64')
    x_val = np.array(x_val, 'float64')
    y_val = np.array(y_val, 'float64')

    x_train /= 255 #normalize inputs between [0, 1]
    x_test /= 255
    x_val /= 255

    x_train = x_train.reshape(x_train.shape[0], 48, 48)
    x_test = x_test.reshape(x_test.shape[0], 48, 48)
    x_val = x_val.reshape(x_val.shape[0],48,48)
    y_train = y_train.reshape(y_train.shape[0], 1)
    y_test = y_test.reshape(y_test.shape[0], 1)
    y_val = y_val.reshape(y_val.shape[0],1)

    print(x_train.shape[0], 'train samples')
    print(x_test.shape[0], 'test samples')
    print(x_val.shape[0], 'validation samples')

    # plt.hist(y_train, max(y_train)+1); plt.show()

    return x_train, y_train, x_test, y_test, x_val, y_val

class Model():
    def __init__(self):
        params = 48*48 # image reshape
        out = 1 # smile label
        self.lr = 0.00001 # Change if you want
        self.W = np.random.randn(params, out)
        self.b = np.random.randn(out)

    def forward(self, image):
        image = image.reshape(image.shape[0], -1)
        out = np.dot(image, self.W) + self.b
        
        w= self.W
        b= self.b
        
        return out, w, b

    def compute_loss(self, pred, gt):
        J = (-1/pred.shape[0]) * np.sum(np.multiply(gt, np.log(sigmoid(pred))) + np.multiply((1-gt), np.log(1 - sigmoid(pred))))
        return J

    def compute_gradient(self, image, pred, gt):
        image = image.reshape(image.shape[0], -1)
        W_grad = np.dot(image.T, pred-gt)/image.shape[0]
        self.W -= W_grad*self.lr

        b_grad = np.sum(pred-gt)/image.shape[0]
        self.b -= b_grad*self.lr
        
        return 

def train(model, batch_size):
    x_train, y_train, _ , _ , x_val, y_val = get_data()
    #batch_size = 100 # Change if you want
    epochs = 10000 # Change if you want
    loss_test = []
    for i in range(epochs):
        stop= loss_test
        loss = []
        for j in range(0,x_train.shape[0], batch_size):
            _x_train = x_train[j:j+batch_size]
            _y_train = y_train[j:j+batch_size]
            out, _, _ = model.forward(_x_train)
            loss.append(model.compute_loss(out, _y_train))
            model.compute_gradient(_x_train, out, _y_train)
        out, w, b = model.forward(x_val)                
        loss_val = model.compute_loss(out, y_val)
        print('Epoch {:6d}: {:.5f} | test: {:.5f}'.format(i, np.array(loss).mean(), loss_val))
        loss_train= np.array(loss).mean()
        
        if (abs(loss_val-stop) < 0.000005) and (epochs > 2):
            
            break
        
        
        
    return loss_train, loss_val, w, b, i
	# plot()

def plot(): # Add arguments
    # CODE HERE
    # Save a pdf figure with train and test losses
    pass

def test(model):
    # _, _, x_test, y_test = get_data()
    
    
    # YOU CODE HERE
    # Show some qualitative results and the total accuracy for the whole test set
    pass

#Function taken from https://www.kaggle.com/grfiv4/plot-a-confusion-matrix
def plot_confusion_matrix(cm,
                          target_names,
                          title='Confusion matrix',
                          cmap=None,
                          normalize=True):
    """
    given a sklearn confusion matrix (cm), make a nice plot

    Arguments
    ---------
    cm:           confusion matrix from sklearn.metrics.confusion_matrix

    target_names: given classification classes such as [0, 1, 2]
                  the class names, for example: ['high', 'medium', 'low']

    title:        the text to display at the top of the matrix

    cmap:         the gradient of the values displayed from matplotlib.pyplot.cm
                  see http://matplotlib.org/examples/color/colormaps_reference.html
                  plt.get_cmap('jet') or plt.cm.Blues

    normalize:    If False, plot the raw numbers
                  If True, plot the proportions

    Usage
    -----
    plot_confusion_matrix(cm           = cm,                  # confusion matrix created by
                                                              # sklearn.metrics.confusion_matrix
                          normalize    = True,                # show proportions
                          target_names = y_labels_vals,       # list of names of the classes
                          title        = best_estimator_name) # title of graph

    Citiation
    ---------
    http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html

    """
    import matplotlib.pyplot as plt
    import numpy as np
    import itertools

    accuracy = np.trace(cm) / float(np.sum(cm))
    misclass = 1 - accuracy

    if cmap is None:
        cmap = plt.get_cmap('Blues')

    plt.figure(figsize=(8, 6))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()

    if target_names is not None:
        tick_marks = np.arange(len(target_names))
        plt.xticks(tick_marks, target_names, rotation=45)
        plt.yticks(tick_marks, target_names)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]


    thresh = cm.max() / 1.5 if normalize else cm.max() / 2
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        if normalize:
            plt.text(j, i, "{:0.4f}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")
        else:
            plt.text(j, i, "{:,}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")


    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label\naccuracy={:0.4f}; misclass={:0.4f}'.format(accuracy, misclass))
    plt.show()

if __name__ == '__main__':
   
    #model = Model()
    #loss_train, _, _, _ = train(model)
    #test(model)
    
    
    if sys.argv[1] == '--batch':
        print('siiii')
        lossTr = []
        lossVal = [] 
        loss_val = 0
        a= np.arange(50,1000,50)
        
        for batchNum in a:
            
            tempError= loss_val
            model = Model()
            loss_train, loss_val, w, b, epochs = train(model, batchNum)
            
            lossTr.append(loss_train)
            lossVal.append(loss_val)
            
            
            if abs(loss_val - tempError) and (batchNum > 50):
                
                minError = tempError
                W = w
                B = b
                pickle.dump(W, open('batchW','wb')) #b= pickle.load(open('filename', 'rb'))
                pickle.dump(B, open('batchB','wb')) 
                pickle.dump(batchNum, open('batchParam','wb')) 
                pickle.dump(epochs, open('batchEpochs','wb')) 
                
    if sys.argv[1] == '--test':
        
        W= pickle.load(open('batchW', 'rb'))
        b= pickle.load(open('batchB', 'rb'))
        
       
        _, _, x_test, y_test, _, _ = get_data()
        
        pred= []
        i=0
        
       # while i < len(x_test):
            
            #out, _, _ = model.forward(x_test[i])
        image= x_test
        image = image.reshape(image.shape[0], -1)
        out = sigmoid(np.dot(image, W) + b)
        
        while i < len(out):
        
            if out[i] < 0.99:
                
                out[i] = 0
                
            else:
                
                out[i]= 1
            
            i+=1
            
        
        conf= confusion_matrix(y_test, out)
        classes = ['Other','Happy' ]  
        ACA= accuracy_score(y_test, out)
        print('ACA')
        print(ACA)
        plot_confusion_matrix(conf, classes, title='Normalized confusion matrix', normalize= True)
        
        
        
        
        
            
            
            
            
        
        
    
                
                
    
        
            
    

    
    
