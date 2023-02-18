Owner: Sriram Ranganathan

References:
- [KRISH_NAIK_YT_CHANNEL](https://www.youtube.com/@krishnaik06)
- [AWS_EC2_HOSTING_BY_Kim_Huiyeon](https://medium.com/techfront/step-by-step-visual-guide-on-deploying-a-flask-application-on-aws-ec2-8e3e8b82c4f7)
- [CONTAINERIZING_FLASK_APP](https://www.youtube.com/@HiteshChoudharydotcom)


# Boston_house_pricing

Objectives of the project:
1. Analysis of the Boston House Pricing dataset
2. Performing training using simple linear regression model
3. Saving the best model
4. Calculating the performance metrics
5. Implementation of web based API for the model and deploying it in the local server
6. Using AWS EC2 free tier Instance host the web application
7. Containerize the Flask web application using docker

# Software and tools required
1. [Github Account](https://github.com)
2. [VS code IDE](https://code.visualstudio.com)
3. [AWS Account](https://aws.amazon.com)
4. [Git CLI](https://git-scm.com/)
5. [docker](https://docker.com)



# Running the Project
- Create a New Environment for the project

```
conda create -p venv python==3.7.10 -y
```
- Installing the project requirements
```
pip install -r requirements.txt
```
- Run the following command
```
python app.py
```
- Open any web browser and open the following URL [localhost](localhost:3000) "localhost:3000"


# Hosting the web application in AWS accout

- Referred: [step_by_step_implementation_of_hosting_webapp_in_AWS_EC2](https://medium.com/techfront/step-by-step-visual-guide-on-deploying-a-flask-application-on-aws-ec2-8e3e8b82c4f7)

- Currently hosted website: [Link_to_app](http://34.204.69.28/)

# Containerizing The application
(Replace the user name with your username in docker
- Once creating the dockerfile creating ```dockerfile``` key in the following commands inside the working directory
```
docker build -t user_name/house-pricing:latest . 
```
This creates an image of the application.

- Inorder to start the application the image has to be created into a container. Once the container is running you can open th emapped port in the local system, In order to host the application in local port 5000 key in the ecommand below.

```
docker run -d -p 5000:3000 username/house-pricing:latest
```
- To push the application to the docker hub, key in the following command
```
docker push username/house-pricing:latest
```







