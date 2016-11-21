#Android Face Recognition with Deep Learning - Library
##Acknowledgements
This library was developed by Michael Sladoje and Mike Schälchli during a bachelor thesis at the Zurich University of Applied Sciences.

Acknowledgements go to the thesis supervisors Dr. Martin Loeser, Dr. Oliver Dürr, Diego Browarnik and all the contributors of our code sources.

Code has been derived from the following sources:
- OpenCV - https://github.com/opencv/opencv
- LIBSVM - https://github.com/cjlin1/libsvm
- AndroidLibSvm - https://github.com/yctung/AndroidLibSvm
- TensorFlow - https://github.com/tensorflow/tensorflow
- TensorFlow Android Demo - https://github.com/miyosuda/TensorFlowAndroidDemo
- Caffe - https://github.com/BVLC/caffe
- caffe-android-demo - https://github.com/sh1r0/caffe-android-demo
- caffe-android-lib - https://github.com/sh1r0/caffe-android-lib

##App architecture
![alt tag](https://github.com/Qualeams/Android-Face-Recognition-with-Deep-Learning/blob/master/AppArchitecture.png)

##Usage
###Include as an Android module
1. git clone https://github.com/Qualeams/Android-Face-Recognition-with-Deep-Learning-Library.git
2. Import the openCV library in an existing Android Studio project
3. Import the facerecognitionlibrary in the existing Android Studio project (has dependencies to the openCV library)

###Parameters
Most parameters are set in the settings/preferences.
###Train, Classify
Either train and classify by passing images (OpenCV Mat object) to the library or if features already obtained from the image (getFeatureVector), the feature vector can be passed (OpenCV Mat object) together with the flag "featuresAlreadyExtracted" set to 'true'.

###Android NDK - C++
The libs for LIBSVM and TensorFlow can be compiled outside of Android Studio with the make command (the Makefile is located under /jni-build).
There are 3 different usages:
- make clean (executes ndk-build clean)
- make (executes ndk-build)
- make install (copies the libs to the folder /src/main/jniLibs/armeabi-v7a)
