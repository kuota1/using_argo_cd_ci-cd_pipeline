# Currency Converter - CI/CD with GitHub Actions & Argo CD

This project demonstrates a complete CI/CD pipeline for a Python-based currency conversion API using GitHub Actions, Docker, and Argo CD.

---

##  Project Overview

A Flask API that converts currencies using [RapidAPI](https://rapidapi.com).  
The application is containerized with Docker, tested and deployed using GitHub Actions, and automatically delivered to a Kubernetes cluster via Argo CD (GitOps).

---

##  Technologies Used

- Python 3.11 / Flask 3.0
- Docker & Docker Hub
- GitHub Actions for CI/CD
- Kubernetes (Minikube)
- Argo CD for GitOps CD
- Kustomize for environment overlays

---

##  Project Structure

.
├── app.py
├── requirements.txt
├── Dockerfile
├── tests/
│ └── test_app.py
├── k8s/
│ ├── base/
│ │ └── deployment.yaml
│ └── overlays/
│ └── production/
│ └── kustomization.yaml
├── .github/
│ └── workflows/
│ └── ci-cd.yaml

yaml
Copy
Edit

---

##  CI/CD Pipeline Overview

###  CI
- Runs on every `push` to `main` or on new tags (`v*.*.*`)
- Executes `unittest` to validate the application
- Builds the Docker image
- Pushes the image to Docker Hub with the short SHA and `latest` tags

###  CD
- Automatically updates the `deployment.yaml` image tag
- Commits and pushes the change back to GitHub
- Argo CD detects the change and deploys the new version

---

##  Secrets Management with Sealed Secrets

This project uses **Bitnami Sealed Secrets** to securely store Kubernetes secrets inside Git repositories.

Instead of committing raw `Secret` manifests (which can expose sensitive data), the `kubeseal` CLI encrypts the secret using the cluster's public key, producing a `sealedsecret.yaml` that is safe to version control.

### Steps used:

1. Install Sealed Secrets controller in the Kubernetes cluster.
2. Export the cluster’s public cert:
   ```bash
   kubeseal --fetch-cert
Create a Kubernetes Secret with needed values (API keys, DockerHub credentials).

Run kubeseal to generate a sealed version:

bash
Copy
Edit
kubeseal --format=yaml --cert=cert.pem < secret.yaml > sealedsecret.yaml
Commit only sealedsecret.yaml to Git.

Argo CD automatically decrypts and applies the secret at runtime, keeping credentials safe while enabling full GitOps workflow.

✅ Results
Fully automated CI/CD process using modern DevOps practices

Zero manual deployment steps

GitOps compliance using Argo CD

 Testing
bash
Copy
Edit
python -m unittest discover -s tests
 Docker
bash
Copy
Edit
docker build -t rober0010/currencyconverter .
docker push rober0010/currencyconverter:latest
 Contact
Roberto Rodriguez
GitHub: @kuota1

This project is part of my DevOps learning journey and portfolio. All secrets and credentials have been removed for security.