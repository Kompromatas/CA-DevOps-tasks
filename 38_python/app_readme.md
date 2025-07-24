# 📆 Flask Date App with Prometheus & Grafana Monitoring

This project is a simple **Flask web application** running in Docker, displaying the current date and time, with full **monitoring setup** using:

- **Prometheus** for metrics collection  
- **Blackbox Exporter** for HTTP endpoint monitoring  
- **Grafana** for visualization

---

## 🚀 Features

✅ Prints current date and time on access  
✅ `/health` endpoint for health checks  
✅ Logging to stdout/stderr (container logs)  
✅ Docker Compose stack with Prometheus and Grafana  
✅ Blackbox Exporter probes application health

---

## ⚙️ Requirements

- [Docker](https://docs.docker.com/get-docker/)  
- [Docker Compose v2](https://docs.docker.com/compose/)

---

## 💻 Running the Application

Clone this repository and navigate into it:

```bash
git clone <repo-url>
cd <to cloned repo>
docker compose up -d 


## 🔎 Accessing Services

| **Service**    | **URL**                                        | **Default Credentials** |
| -------------- | ---------------------------------------------- | ----------------------- |
| **app-38   **  | [http://localhost:5000](http://localhost:5000) | –                       |
| **Prometheus** | [http://localhost:9090](http://localhost:9090) | –                       |
| **Grafana**    | [http://localhost:3000](http://localhost:3000) | admin / admin           |


## Helth checks on Grafana

Grafana dashboard showing a time series panel visualizing probe success metric for an HTTP health endpoint. The graph displays probe success values over time, with occasional drops indicating failed health checks. The Prometheus query probe_success is used, filtered for the instance http://app:5000/health and job blackbox. The interface includes options for data source selection, query editing, and refresh intervals. The environment is a dark-themed Grafana workspace with navigation sidebar and query builder visible. The emotional tone is neutral and technical.text](image.png)