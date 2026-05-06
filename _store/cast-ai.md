---
aid: cast-ai
url: https://raw.githubusercontent.com/api-evangelist/cast-ai/refs/heads/main/apis.yml
name: CAST AI
tags:
  - Autoscaling
  - Cloud Infrastructure
  - Cost Optimization
  - DevOps
  - FinOps
  - Kubernetes
  - Observability
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/swagger-ui-n0PWZL5D.png
access: 3rd-Party
created: '2024-07-02'
modified: '2026-04-23'
position: Consumer
description: CAST AI is an Application Performance Automation (APA) platform for Kubernetes that automates cost optimization, autoscaling, workload rightsizing, GPU/LLM workload placement, spot instance selection, and security posture analysis. The platform works across AWS, GCP, Azure, Oracle Cloud, IBM Cloud, AliCloud and on-premises distributions (EKS, GKE, AKS, OpenShift, Rancher, kOps). Everything available in the console UI is also accessible via the REST API at api.cast.ai.
apis:
  - aid: cast-ai:kubernetes-cost-optimization-api
    name: CAST AI Kubernetes Cost Optimization API
    tags:
      - Autoscaling
      - Clusters
      - Cost Optimization
      - FinOps
      - Hibernation
      - Karpenter
      - Kubernetes
      - LLM
      - Metrics
      - Node Templates
      - Nodes
      - Policies
      - Pricing
      - Rebalancing
      - Security
      - Spot Instances
      - Workloads
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/swagger-ui-n0PWZL5D.png
    baseURL: https://api.cast.ai
    humanURL: https://docs.cast.ai/docs/api
    properties:
      - url: https://docs.cast.ai/docs/api
        type: Documentation
      - url: openapi/cast-ai-kubernetes-cost-optimization-openapi.yml
        type: OpenAPI
      - url: https://api.cast.ai/v1/spec/
        type: Swagger
      - url: https://docs.cast.ai/docs/authentication
        type: Authentication
      - url: https://docs.cast.ai/changelog
        type: ChangeLog
      - url: json-schema/cluster.json
        type: JSONSchema
      - url: json-schema/node.json
        type: JSONSchema
      - url: json-schema/node-template.json
        type: JSONSchema
      - url: json-schema/workload.json
        type: JSONSchema
      - url: json-schema/rebalancing-schedule.json
        type: JSONSchema
      - url: json-schema/cost-report.json
        type: JSONSchema
      - url: json-ld/cast-ai-context.jsonld
        type: JSONLD
    description: 'The CAST AI REST API provides comprehensive access to the Kubernetes cost optimization platform: cluster management, autoscaling and Karpenter integration, node configuration and templates, workload rightsizing, scheduled rebalancing, cost reporting, security insights, hibernation schedules, AI enabler / LLM workload optimization, and GPU/OMNI compute features. Authentication uses API keys and the API is served at api.cast.ai.'
common:
  - type: Website
    url: https://cast.ai/
  - type: Documentation
    url: https://docs.cast.ai/docs/
  - type: GettingStarted
    url: https://docs.cast.ai/docs/getting-started
  - type: Authentication
    url: https://docs.cast.ai/docs/authentication
  - type: ChangeLog
    url: https://docs.cast.ai/changelog
  - type: Pricing
    url: https://cast.ai/pricing/
  - type: Blog
    url: https://cast.ai/blog/
  - type: CaseStudies
    url: https://cast.ai/case-studies/
  - type: Customers
    url: https://cast.ai/case-studies/
  - type: Partners
    url: https://cast.ai/partners/
  - type: Support
    url: https://cast.ai/support/
  - type: StatusPage
    url: https://status.cast.ai/
  - type: SecurityPolicy
    url: https://cast.ai/security/
  - type: TermsOfService
    url: https://cast.ai/terms-of-service/
  - type: PrivacyPolicy
    url: https://cast.ai/privacy-policy/
  - type: GitHub
    url: https://github.com/castai/
  - type: Slack
    url: https://castai-community.slack.com/
  - type: X
    url: https://x.com/cast_ai/
  - type: LinkedIn
    url: https://www.linkedin.com/company/cast-ai/
  - type: YouTube
    url: https://www.youtube.com/@CASTAI
  - name: Features
    type: Features
    data:
      - name: Kubernetes Automation
      - name: Cluster Autoscaling
      - name: Karpenter Integration
      - name: Workload Rightsizing
      - name: Bin Packing
      - name: Spot Instance Automation
      - name: Spot Interruption Prediction
      - name: GPU Optimization
      - name: LLM Optimization
      - name: Database Optimization
      - name: Cost Monitoring
      - name: Cost Reporting
      - name: Savings Analysis
      - name: Security Insights
      - name: Posture Management
      - name: Hibernation Scheduling
      - name: Node Templates
      - name: Rebalancing
      - name: Self-Healing
      - name: Policy Enforcement
      - name: Drift Remediation
      - name: Container Insights
      - name: SLO Monitoring
      - name: Performance Observability
      - name: Multi-Cloud
      - name: Air-Gapped Support
  - name: UseCases
    type: UseCases
    data:
      - name: Kubernetes Cost Reduction
      - name: Cluster Right-Sizing
      - name: Automated Spot Instance Adoption
      - name: GPU Workload Placement
      - name: LLM Inference Cost Optimization
      - name: FinOps Reporting
      - name: Security Posture Assessment
      - name: Reserved Instance Planning
      - name: Multi-Cluster Management
      - name: Hibernation of Non-Production Clusters
  - name: Integrations
    type: Integrations
    data:
      - name: AWS
      - name: Google Cloud
      - name: Azure
      - name: Oracle Cloud
      - name: IBM Cloud
      - name: AliCloud
      - name: EKS
      - name: GKE
      - name: AKS
      - name: OpenShift
      - name: Rancher
      - name: kOps
      - name: Karpenter
      - name: Terraform
      - name: Prometheus
      - name: Grafana
      - name: Datadog
      - name: OpenTelemetry
      - name: Jira
      - name: Slack
      - name: PagerDuty
      - name: ServiceNow
      - name: PostgreSQL
      - name: MySQL
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---
