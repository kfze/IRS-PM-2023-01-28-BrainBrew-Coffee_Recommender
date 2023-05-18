# IRS_Project
IRS_Project

## To Run Front End
- Access into Frontend folder in terminal
= python -m flask --app main run

## To Run Back End
- To install packages to use jupyter notebook as rest api, run following in cmd
- pip install jupyter_kernel_gateway
- jupyter kernelgateway --generate-config
- run the the next line in terminal to start server, at folder containing this file
- jupyter kernelgateway --KernelGatewayApp.api='kernel_gateway.notebook_http' --KernelGatewayApp.seed_uri='Backend.ipynb' --KernelGatewayApp.port=8899

## Testing Back End Example
- Install Postman
- Import collection in Backend folder
- Check URL
- Get Return