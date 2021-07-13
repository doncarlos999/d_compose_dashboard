# d_compose_dashboard

split monolith dashboard into microservices in anticipation of needing autoscaling

docker-compose.yaml was converted using `kompose convert`

To launch kubernetes:

`kubectl apply -f nginx-service.yaml,nginx-deployment.yaml,streamlit-deployment.yaml,cellxgene-deployment.yaml,streamlit-service.yaml,cellxgene-service.yaml`


TODO:
** add https to nginx for security
** create containers for azimuth
** Set autoscaling up
