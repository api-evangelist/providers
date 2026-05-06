---
aid: argo-cd
name: Argo CD
description: Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes that automates the deployment of applications by using Git repositories as the source of truth for defining the desired application state. It supports multiple config management tools (Helm, Kustomize, Jsonnet, plain YAML), multi-cluster deployments, RBAC, SSO integrations, and a fully-loaded web UI. Part of the CNCF ecosystem and the Argo Project, governed by the Linux Foundation.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Continuous Delivery
  - Containers
  - Deployment
  - GitOps
  - Kubernetes
  - CNCF
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/argo-cd/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: argo-cd:argo-cd
    name: Argo CD API
    description: The Argo CD REST API provides programmatic access to all Argo CD functionality including application management, cluster registration, repository configuration, project RBAC, account management, notifications, and settings. Authentication uses JWT bearer tokens obtained via the session endpoint.
    humanURL: https://argo-cd.readthedocs.io/en/stable/developer-guide/api-docs/
    tags:
      - Continuous Delivery
      - GitOps
      - Kubernetes
      - REST API
    properties:
      - type: Documentation
        url: https://argo-cd.readthedocs.io/en/stable/developer-guide/api-docs/
      - type: OpenAPI
        url: openapi/argo-cd-openapi.json
      - type: GettingStarted
        url: https://argo-cd.readthedocs.io/en/stable/getting_started/
      - type: Authentication
        url: https://argo-cd.readthedocs.io/en/stable/developer-guide/api-docs/#authentication
      - type: APIReference
        url: https://cd.apps.argoproj.io/swagger-ui
common:
  - type: Website
    url: https://argoproj.github.io/cd/
  - type: Documentation
    url: https://argo-cd.readthedocs.io/en/stable/
  - type: GettingStarted
    url: https://argo-cd.readthedocs.io/en/stable/getting_started/
  - type: GitHubOrganization
    url: https://github.com/argoproj
  - type: GitHubRepository
    url: https://github.com/argoproj/argo-cd
  - type: Blog
    url: https://blog.argoproj.io/
  - type: ReleaseNotes
    url: https://github.com/argoproj/argo-cd/releases
  - type: ChangeLog
    url: https://github.com/argoproj/argo-cd/blob/master/CHANGELOG.md
  - type: CLI
    url: https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd/
  - type: SDK
    url: https://github.com/argoproj/argo-cd/tree/master/pkg/apiclient
  - type: Support
    url: https://github.com/argoproj/argo-cd/issues
  - type: SpectralRules
    url: rules/argo-cd-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/gitops-delivery.yaml
  - type: Vocabulary
    url: vocabulary/argo-cd-vocabulary.yaml
  - type: Features
    data:
      - name: Declarative GitOps Delivery
        description: Defines application deployment state in Git repositories and automatically reconciles cluster state to match.
      - name: Multi-Cluster Deployment
        description: Deploy and manage applications across multiple Kubernetes clusters from a single control plane.
      - name: ApplicationSet Controller
        description: Automates creation of Argo CD Applications from templates across many clusters and namespaces.
      - name: Multiple Config Management Tools
        description: Supports Helm, Kustomize, Jsonnet, plain YAML, and custom plugins for application templating.
      - name: Web UI
        description: Fully-loaded graphical interface for visualizing application sync status, resource trees, and deployment history.
      - name: RBAC and Multi-Tenancy
        description: Fine-grained role-based access control with project-level isolation for multi-team environments.
      - name: SSO Integration
        description: Built-in SSO support for OIDC, OAuth2, LDAP, SAML 2.0, GitHub, GitLab, Microsoft, and LinkedIn.
      - name: Automated Sync
        description: Continuously monitors Git and automatically syncs application state to match the desired state.
      - name: Sync Hooks
        description: PreSync, Sync, and PostSync hooks for complex rollout strategies including blue/green and canary.
      - name: Webhook Support
        description: Receives webhooks from GitHub, GitLab, and Bitbucket for instant sync on push events.
      - name: Audit Trail
        description: Complete audit log of all deployment events and configuration changes.
      - name: Health Assessment
        description: Built-in and custom health checks for Kubernetes resources to assess application health status.
      - name: Notifications
        description: Configurable notifications via email, Slack, and other channels on sync events and health changes.
      - name: GPG Commit Verification
        description: Verifies GPG signatures on Git commits for enhanced supply chain security.
  - type: UseCases
    data:
      - name: Continuous Deployment to Kubernetes
        description: Automate application releases to Kubernetes clusters with every Git commit triggering a reconciliation cycle.
      - name: Multi-Environment Promotion
        description: Promote application versions across dev, staging, and production environments using Git branch strategies.
      - name: Multi-Cluster GitOps
        description: Manage application deployments consistently across dozens of Kubernetes clusters from a central Argo CD instance.
      - name: Cluster Add-On Management
        description: Automatically deploy infrastructure add-ons (CNI, CSI, monitoring) to all clusters using ApplicationSet.
      - name: Tenant Self-Service
        description: Allow development teams to manage their own applications within project-scoped RBAC boundaries.
      - name: Disaster Recovery
        description: Quickly restore application state to any prior Git commit in case of production incidents.
      - name: Compliance and Auditability
        description: Maintain a complete audit trail of all deployment changes via Git history and Argo CD event logs.
  - type: Integrations
    data:
      - name: Helm
        description: Native support for Helm chart rendering and deployment with value overrides.
      - name: Kustomize
        description: Native support for Kustomize overlays for environment-specific configuration.
      - name: HashiCorp Vault
        description: Integrates with Vault for secret management using the argocd-vault-plugin.
      - name: GitHub Actions
        description: Trigger Argo CD syncs or check sync status as part of GitHub Actions CI pipelines.
      - name: Jenkins
        description: Integrate Argo CD sync steps into Jenkins CI/CD pipelines.
      - name: Prometheus
        description: Exposes metrics for Prometheus scraping to monitor application sync health and performance.
      - name: Grafana
        description: Pre-built dashboards for visualizing Argo CD metrics in Grafana.
      - name: Open Policy Agent
        description: Enforce admission policies via OPA and Gatekeeper before Argo CD syncs resources.
      - name: Argo Rollouts
        description: Native integration with Argo Rollouts for progressive delivery (canary, blue/green).
      - name: Argo Workflows
        description: Trigger Argo Workflows as part of sync hooks for complex multi-step pipelines.
      - name: Slack
        description: Send deployment notifications and alerts to Slack channels.
      - name: AWS EKS
        description: Manage applications on Amazon EKS clusters with AWS IAM authentication support.
      - name: Google GKE
        description: Deploy to Google Kubernetes Engine clusters with GKE authentication.
      - name: Azure AKS
        description: Manage applications on Azure Kubernetes Service with Azure AD authentication.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
