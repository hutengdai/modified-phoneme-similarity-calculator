import re
import numpy as np

def segsFeats(featfilepath):
    '''
    input argument: path to Features.txt.
    output 1: segsFeats, a dictionary of segments along with all the feature values (+cont, 0str, etc.)
    output 2: segsnozero, a dictionary of segments with only the non-zero feature values (+cont but not 0str)
    output 3: features, a list of feature names

    the Features.txt file needs to be in the standard 2009 UCLAPL GUI format, i.e., tab separated, no 'word_boundary' segment defined in the list of segments, and the first line starts with an empty tab and then feature names.
    '''
    with open(featfilepath, 'r', encoding='utf-8') as featurefile:
        feat_file = featurefile.readlines()
    features = feat_file.pop(0).lstrip("\t").rstrip("\n").split("\t")

    segsFeats = {}
    for line in feat_file:
        line = line.rstrip("\n").split("\t")
        seg = line[0]
        segsFeats[seg] = []
        for feature in features:
            i = features.index(feature)
            segsFeats[seg].append(str(line[i+1])+str(feature))
            # tuple(segsFeats[seg])
    segsFeatsnozero = {}
    for line in feat_file:
        line = line.rstrip("\n").split("\t")
        seg = line[0]
        segsFeatsnozero[seg] = []
        for feature in features:
            i = features.index(feature)
            if line[i+1] != '0':
                segsFeatsnozero[seg].append(str(line[i+1])+str(feature))
    if 'wb' not in features:
        features.append('word_boundary')
    return(segsFeats)


def wlist2feature(word, segsFeats):
    '''
        input argument: each line in a wlist and features (segsFeats)
    output: res, a list of the lists of feature bundles;
    '''

    res = []
    for segment in word:
        a = [segsFeats.get(segment)]
        for val in a:
            if val != None:
                res.append(val)
            else:
                pass
    return res


def simiarity(segment1, segment2,total_feature):
    m = 0
    n = 0
    shared_features = []
    unshared_features_a = []
    unshared_features_b = []
    a = segsFeats.get(segment1)
    b = segsFeats.get(segment2)
    
    for feature_a in a:
        for feature_b in b:
            if feature_a == feature_b:
                m+=1
                shared_features.append(feature_a)
            else:

                n+=1
    similarity = m/total_feature 
    
    unshared_features_a = np.setdiff1d(a,shared_features)
    unshared_features_b = np.setdiff1d(b,shared_features)
    #pair each feature class with a weight
    print("shared features include "+str(shared_features))
    print("unshared features in first segment include "+ str(unshared_features_a))
    print("unshared features in second segment include "+ str(unshared_features_b))
    # for unshared_f in unshared_features_a:
        
   
    return similarity
                
                
if __name__ == '__main__':
    with open("Features.txt", 'r', encoding='utf-8') as featurefile:
        feat_file = featurefile.readlines()
        features = feat_file.pop(0).lstrip("\t").rstrip("\n").split("\t")
        segsFeats = segsFeats("Features.txt")  
    print(features)
    dlist = {'+cg': 0.4,
             '-cg': ,
             '0cg': ,
             '+sg': 0.2,
             '-sg':,
             '0sg':,
             }          
    print(simiarity("p","p'",14))
