---
name: Amazon EKS
description: Amazon Elastic Kubernetes Service (Amazon EKS) is a managed Kubernetes service that makes it easy to run Kubernetes on AWS without needing to install, operate, and maintain your own Kubernetes control plane or nodes. Amazon EKS runs upstream Kubernetes and is certified Kubernetes conformant, so you can use existing tools and plugins from partners and the Kubernetes community.
url: https://aws.amazon.com/eks/
baseURL: https://eks.amazonaws.com
humanURL: https://aws.amazon.com/eks/
tags:
  - AWS
  - Container Orchestration
  - Containers
  - EKS
  - Kubernetes
properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/eks/latest/APIReference/
  - type: OpenAPI
    url: openapi/amazon-eks-openapi.yml
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/eks/2017-11-01/openapi.yaml
  - type: JSONSchema
    url: json-schema/amazon-eks-cluster-schema.json
  - type: JSONLD
    url: json-ld/amazon-eks-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/eks/pricing/
  - type: GettingStarted
    url: https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/eks/faqs/
  - type: UserGuide
    url: https://docs.aws.amazon.com/eks/latest/userguide/
  - type: APIReference
    url: https://docs.aws.amazon.com/eks/latest/APIReference/
  - type: CLIReference
    url: https://docs.aws.amazon.com/cli/latest/reference/eks/
  - type: Security
    url: https://docs.aws.amazon.com/eks/latest/userguide/security.html
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: DeveloperPortal
    url: https://aws.amazon.com/eks/
  - type: Docs
    url: https://docs.aws.amazon.com/
  - type: Terms
    url: https://aws.amazon.com/service-terms/
  - type: Privacy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/support/
  - type: Blog
    url: https://aws.amazon.com/blogs/containers/
  - type: GitHub
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/eks/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/amazon-eks
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: Security
    url: https://aws.amazon.com/security/
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: Features
    data:
      - name: Managed Control Plane
        description: AWS manages the Kubernetes control plane across multiple Availability Zones with automatic upgrades.
      - name: EKS Auto Mode
        description: Automates cluster infrastructure management for compute, storage, and networking with machine learning optimization.
      - name: EKS Hybrid Nodes
        description: Connect on-premises and edge infrastructure to EKS clusters for unified management.
      - name: Fargate Integration
        description: Run Kubernetes pods on serverless compute without managing EC2 node groups.
      - name: Managed Node Groups
        description: Automate provisioning and lifecycle management of EC2 nodes for Kubernetes clusters.
      - name: EKS Anywhere
        description: Deploy and manage Kubernetes clusters on customer-managed infrastructure including on-premises.
      - name: Add-Ons Management
        description: Manage operational software add-ons like VPC CNI, CoreDNS, and kube-proxy through EKS.
  - type: UseCases
    data:
      - name: Generative AI Applications
        description: Scale production-grade AI deployments with GPU nodes for distributed training and inference.
      - name: Microservices Architecture
        description: Deploy and manage containerized microservices with Kubernetes-native service discovery and scaling.
      - name: Internal Developer Platforms
        description: Standardized Kubernetes environments combining open source with AWS managed services.
      - name: Hybrid Cloud Applications
        description: Unified Kubernetes management across AWS cloud and on-premises infrastructure.
      - name: Data Processing Platforms
        description: Scalable batch processing and streaming data workloads using Spark, Flink, or Ray.
  - type: Integrations
    data:
      - name: Amazon ECR
        description: Pull container images from ECR for Kubernetes workloads with native IAM authentication.
      - name: AWS Load Balancer Controller
        description: Manage Application and Network Load Balancers for Kubernetes Ingress resources.
      - name: Amazon EFS CSI Driver
        description: Mount EFS file systems as Kubernetes persistent volumes for stateful applications.
      - name: AWS IAM Roles for Service Accounts
        description: Grant Kubernetes pods fine-grained IAM permissions using OIDC-based service account annotations.
      - name: Amazon CloudWatch Container Insights
        description: Collect and analyze metrics, logs, and traces from EKS clusters and workloads.
  - type: SpectralRules
    url: rules/amazon-eks-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-eks-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/eks-management.yaml
maintainer:
  name: Kin Lane
modified: '2026-04-19'
apis: []
---
