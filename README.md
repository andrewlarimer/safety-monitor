# Safety Monitor


**![](https://lh6.googleusercontent.com/XljfDs5aHjuXzJ1stLrq7vlzyIRkeP4hckQ8vvVqI1_2NNMuEuzy0fXc7qBDiigUYDw9u-OsNh8ysc-6tTKZGNYD5_wiDmxI7P7N_BnS0vH6UxGJwwhvXJakSE-MnEeCCwsiRuWUYTA)**


**Occupational Safety is the most important aspect for any construction site or field engineering work. Safety Monitor serves as a tool that reinforces workplace safety by monitoring that its workers are wearing personal protective equipment (PPE) onsite. This tool uses Deep Learning to identify if the worker at site is wearing protective equipment such as Safety Vest, Hard Hat. **


**About the Model**
Our model is currently trained on 1109 images from construction sites and has been trained using YOLOv3 to detect these PPE from live feed. It then processes the images read in from a camera and alerts supervisor when it detects non-compliance.

**Running the Model**
1. Clone the repo: `git clone https://github.com/andrewlarimer/safety-monitor.git`.
2. Download the model weights (in Keras format) [here](https://drive.google.com/open?id=1rkJjuLAvg4x8rwKHbDmxdkvQEi3EwkAp). 
3. Move model weights to`safety-monitor/logs/000` directory [shown here](https://github.com/andrewlarimer/safety-monitor/tree/master/logs/000).
4. In a Jupyter Notebooks, run `Visualizing_Predictions.ipynb'` notebook [here](https://github.com/andrewlarimer/safety-monitor/blob/master/scripts/Visualizing%20Predictions.ipynb).
> Note: `Requires latest versions of Keras, Tensorflow, Numpy, Pandas, Matplotlib, OpenCV, Pillow, Signalwire, and MoviePy.`



**Reporing Features**
Safety Monitor sends an automated report to a designated supervisor with an alert when safety equipment is not being worn on site. 

To check out the reporting features in Safety Monitors In a Jupyter Notebooks, run `Visualizing_Predictions.ipynb'` notebook [here](https://github.com/andrewlarimer/safety-monitor/blob/master/scripts/Visualizing%20Predictions.ipynb).

 
