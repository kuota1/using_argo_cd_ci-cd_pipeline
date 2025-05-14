Currency Converter - CI/CD with GitHub Actions & Argo CD

This project demonstrates a complete CI/CD pipeline for a Python-based currency conversion API using GitHub Actions, Docker, and Argo CD.

Project Overview

A Flask API that converts currencies using RapidAPI. The application is containerized with Docker, tested and deployed using GitHub Actions, and automatically delivered to a Kubernetes cluster via Argo CD (GitOps).

Technologies Used

Python 3.11 / Flask 3.0

Docker & Docker Hub

GitHub Actions for CI/CD

Kubernetes (Minikube)

Argo CD for GitOps CD

Kustomize for environment overlays

 Project Structure

.
├── app.py
├── requirements.txt
├── Dockerfile
├── tests/
│   └── test_app.py
├── k8s/
│   ├── base/
│   │   └── deployment.yaml
│   └── overlays/
│       └── production/
│           └── kustomization.yaml
├── .github/
│   └── workflows/
│       └── ci-cd.yaml

CI/CD Pipeline Overview

CI

Runs on every push to main or on new tags (v*.*.*)

Executes unittest to validate the application

Builds the Docker image

Pushes the image to Docker Hub with the short SHA and latest tags

CD

Automatically updates the deployment.yaml image tag

Commits and pushes the change back to GitHub

Argo CD detects the change and deploys the new version


Results

Fully automated CI/CD process using modern DevOps practices

Zero manual deployment steps

GitOps compliance using Argo CD

Testing

python -m unittest discover -s tests

Docker

docker build -t rober0010/currencyconverter .
docker push rober0010/currencyconverter:latest

Contact

Roberto RodriguezGitHub: @kuota1

This project is part of my DevOps learning journey and portfolio. All secrets and credentials have been removed for security.