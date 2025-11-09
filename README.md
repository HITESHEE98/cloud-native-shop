# Cloud-Native Shop (EKS • Docker • Terraform • GitHub Actions)

A production-style microservices project:
- **Infrastructure as Code:** Terraform → VPC + EKS
- **Containers:** Docker for each service
- **Orchestration:** Kubernetes (EKS)
- **CI/CD:** GitHub Actions → Build, Push (ECR), Deploy (kubectl)
- **Monitoring:** Prometheus + Grafana

## Structure
- `microservices/` — user, product, order, frontend
- `kubernetes/` — K8s manifests
- `terraform/` — infra setup (VPC, EKS)
- `.github/workflows/` — CI/CD pipelines
- `docs/` — architecture and runbook
