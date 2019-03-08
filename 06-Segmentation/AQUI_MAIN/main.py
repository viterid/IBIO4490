if _name_ == '_main_':
    import argparse
    import imageio
    from seg import segmentByClustering # Change this line if your function has a different name
    from val import evaluation
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--color', type=str, default='rgb', choices=['rgb', 'lab', 'hsv', 'rgb+xy', 'lab+xy', 'hsv+xy']) # If you use more please add them to this list.
    parser.add_argument('--k', type=int, default=4)
    parser.add_argument('--method', type=str, default='watershed', choices=['kmeans', 'gmm', 'hierarchical', 'watershed'])
    parser.add_argument('--img_file', type=str, required=True)
    
    img = imageio.imread(opts.img_file)
    seg = segmentByClustering(rgbImage=img, colorSpace=opts.color, clusteringMethod=opts.method, numberOfClusters=opts.k)
    imshow(img, seg, title='Prediction')
    
    path.replace('jpg', 'mat')
    per, cob = evaluation(seg, path)
    
    print ('presición = ',pres)
    print ('cobertura =' cob)
