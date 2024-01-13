<h><b>Country App</b></h>

Using the following API https://www.travel-advisory.info/api
Given the country code it returns the country name example:
lookup --countryCode=AU
Australia

Save the data from https://www.travel-advisory.info/api to a file called
data.json and add functionality to your program to work with a file instead of
real API endpoint
This program supports multiple country codes as input

Bonus:

This tool exposes its functionality via REST.
written in Craft demo to a REST service with two routes
 /health returns the health of your service
 /diag check returns the status of the API https://www.travel-advisory.info/api return
{&quot;api_status&quot;:{... &quot;code&quot;:200,&quot;status&quot;:&quot;ok&quot;} that you obtained from
hitting an API
 /convert – converts country name to country code
 Create a local k8s cluster on your workstation
 Deploy your service to the local k8s cluster

If you're running on your local system, app is accessible through this API `http://localhost:5001`

Before running this app through the container. Please use the below code to build your docker cotainer image

`docker build -t country-lookup-service:latest .`

If you want to use this image to deploy in your K8S cluster. Make sure the image should be pushed to any registry(local/dokcer hub registry)

`docker pull registry:latest`

`docker run -itd -p 6000:5000 --restart=always --name registry registry:latest`

`docker tag country-lookup-service localhost:6000/country-lookup-service:latest`

`docker push localhost:6000/country-lookup-service:latest`

change the name of the container image in deployment manifest file accoring to the registry image name.

I'm using

`image: localhost:6000/country-lookup-service:latest`
_________
Operating at an optimal level

TBD: Setup basic monitoring
