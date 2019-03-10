# ParallelOCR
trying to speed up ocr using parallel computing in python

primarily optimising for scanned boooks

## Steps  

### Create dataset  
list all fonts on google fonts with web api.  
create template html file with all required letters.  
iterate over list of fonts and take screenshots. (process parallely)  
Seperate letters from screenshots with opencv.  
apply Preprocess on all letters and change resolution if required.  

### Preprocess File  
get Scanned File.  
get page.  
apply transforms - *process paralely if faster*:  
    grayscale *using otsu thresholding*  
    contrast  
    brightness  
    sharpen edges  
compile File.  
or  
perform next step per page.  
### Seperate Lines  
find horizontal whitespace.  
divide image by horizontal whitespace.  
    return cropped image of line.  
or  
pass y coordinate of start and end of line.  
    crop image by line in next step.  
assign index no to line.  
assign line to process.  
save processid with index no of line.  
### Recognize Text - parallel processes  
Tensorflow  
    Train
        use CNN-RNN with CTC loss to train model on dataset .  
            (similar to SimpleHTR but optimised for printed Text)  
        OR  
        use SVMs (because dataset would be relatively small)  
    Execute
        blob detection for letters (group vertical blobs)  
        pass letters to trained model  
        Detect spaces  
        compile Text  
return text  
### Compile Page  
arrange returned text according to index and process id  
save as txt or pdf  
