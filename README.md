# Mnist (Flask) webapp demo

**[Heroku live web-app][heroku-app-url]**


**Table of Contents**
- [Pre-request][pre-request]
- [Usage / Installation][usage]
- [Code structure][code_structure]
- [Deep Learning Model][ml-model]
- [Flask Webapp & Integrating DL model][web-app]


# <a name="pre-request"></a>Pre-request

You should have basic understanding of:
- Python, pip, virtual environment, Flask
- Machine Learning / Deep Learning
- HTML, CSS, JavaScript



# <a name="usage"></a>Usage / Installation

### Local

Clone/download code for this demo from [mnist-demo github repo][repo_url]

```bash
git clone https://github.com/sumit-kothari/mnist-demo.git
```

Navigate to root of the project and install required dependencies

```bash
cd mnist-demo
pip install -r requirements.txt
```

Run Flask app locally
```bash
python app.py
```

### Deploy to heroku

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/sumit-kothari/mnist-demo/tree/master)



# <a name="code_structure"></a>Code Structure

![_config.yml](https://sumit-kothari.github.io/images/code_structure.png)



# <a name="ml-model"></a>DL Model

### Training deeplearning model

[train-mnist.py][train-mnist.py] contains the code to train a deeplearning model.

**Last line** in the code helps us in **saving our keras/tensorflow model**.

<script src="https://gist-it.appspot.com/github/sumit-kothari/mnist-demo/blob/master/tensorflow_model/train-mnist.py?slice=-6:"></script>


### Testing deeplearning model

The model saved during training, is used for testing purpose.

Also we have created our testing script (i.e [predict.py][predict.py]) as a module, therefore we can load it easily in other python scripts which we can use during prediction.

Following is the **logic used in [predict.py][predict.py]:**

- Load the model and graph 

<script src="https://gist-it.appspot.com/github/sumit-kothari/mnist-demo/blob/master/tensorflow_model/predict.py?slice=7:13"></script>


- Method `predict_image` takes **image as input** and **returns image label with confidence/probability** 

- In `predict_image`, first we convert image to gray-scale, save in numpy array and re-shape it to 1x28x28  

- Finally in `predict_image`, we pass this test image array to `model.predict` method, which help us in predicting the most probable label with its probability

<script src="https://gist-it.appspot.com/github/sumit-kothari/mnist-demo/blob/master/tensorflow_model/predict.py?slice=14:34"></script>



# <a name="web-app"></a>Flask Webapp & Integrating DL model

The main python file for our webapp is `app.py`, which contains following major logic.


We have method `upload_file()` which handles the index/root route path, for both GET and POST request type.

<script src="https://gist-it.appspot.com/github/sumit-kothari/mnist-demo/blob/master/app.py?slice=19:21"></script>

If the request type is GET we display [index.html][index.html] template file.

<script src="https://gist-it.appspot.com/github/sumit-kothari/mnist-demo/blob/master/app.py?slice=49:51"></script>

When request type is POST, user is trying to upload the image file.

We validate the name, type of the uploaded image and redirect to error page if any validation error.

<script src="https://gist-it.appspot.com/github/sumit-kothari/mnist-demo/blob/master/app.py?slice=21:32"></script>

We have also loaded our `predict_image` (as `model_predict`) method from [predict.py][predict.py], which helps us in predicting label for the given image.

<script src="https://gist-it.appspot.com/github/sumit-kothari/mnist-demo/blob/master/app.py?slice=3:4"></script>

So, if image valid we call our `model_predict` which takes input parameter as image file and return label & label's confidence probabilty.

And finally we redirect to new route method (`file_predict()`) where we display the predictions.

<script src="https://gist-it.appspot.com/github/sumit-kothari/mnist-demo/blob/master/app.py?slice=32:46"></script>

We also have a method called `file_predict()` which helps us in displaying the prediction result using [predict.html][predict.html] template file.

<script src="https://gist-it.appspot.com/github/sumit-kothari/mnist-demo/blob/master/app.py?slice=57:67"></script>

[predict.html][predict.html] has the template which displays predicted label value, predicted label confidence and original image.

<script src="https://gist-it.appspot.com/github/sumit-kothari/mnist-demo/blob/master/templates/predict.html?slice=10:17"></script>


Similarly, [index.html][index.html] has the template which allows us to upload the image, on which to predict.

<script src="https://gist-it.appspot.com/github/sumit-kothari/mnist-demo/blob/master/templates/index.html?slice=11:15"></script>


---

#### The End

[pre-request]: #pre-request
[usage]: #usage
[code_structure]: #code_structure
[ml-model]: #ml-model
[web-app]: #web-app
[integration]: #integration
[deployment]: #deployment
[train-mnist.py]: https://github.com/sumit-kothari/mnist-demo/blob/master/tensorflow_model/train-mnist.py
[predict.py]: https://github.com/sumit-kothari/mnist-demo/blob/master/tensorflow_model/predict.py
[index.html]: https://github.com/sumit-kothari/mnist-demo/blob/master/templates/index.html
[predict.html]: https://github.com/sumit-kothari/mnist-demo/blob/master/templates/predict.html
[heroku-app-url]: https://mnist-demo-app.herokuapp.com/
[repo_url]: https://github.com/sumit-kothari/mnist-demo
