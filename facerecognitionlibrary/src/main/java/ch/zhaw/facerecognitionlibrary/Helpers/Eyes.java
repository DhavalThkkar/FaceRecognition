/* Copyright 2016 Michael Sladoje and Mike Schälchli. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/

package ch.zhaw.facerecognitionlibrary.Helpers;

import org.opencv.core.MatOfFloat;

public class Eyes {
    double dist;
    MatOfFloat rightCenter;
    MatOfFloat leftCenter;
    double angle;

    public Eyes(double dist, MatOfFloat rightCenter, MatOfFloat leftCenter, double angle) {
        this.dist = dist;
        this.rightCenter = rightCenter;
        this.leftCenter = leftCenter;
        this.angle = angle;
    }

    public double getDist() {
        return dist;
    }

    public MatOfFloat getRightCenter() {
        return rightCenter;
    }

    public MatOfFloat getLeftCenter() {
        return leftCenter;
    }

    public double getAngle() {
        return angle;
    }
}
