---
name: Scalability
description: A subject-matter collection covering APIs, tools, frameworks, and data sources related to application scalability, infrastructure scaling, performance optimization, and elastic resource management. This topic spans cloud provider auto-scaling, event-driven autoscaling (KEDA), load balancing, database scaling, and observability for scale.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/scalability/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-05-02'
specificationVersion: '0.18'
tags:
  - Auto Scaling
  - Cloud Computing
  - DevOps
  - Distributed Systems
  - Elasticity
  - High Availability
  - Infrastructure
  - Load Balancing
  - Performance
  - Scalability
apis:
  - name: KEDA (Kubernetes Event-Driven Autoscaling) API
    description: KEDA is a Kubernetes-based event-driven autoscaling component and CNCF graduate project. It provides fine-grained autoscaling (including to/from zero) for event-driven Kubernetes workloads by bridging over 70 built-in scalers to message brokers, cloud services, and databases. KEDA extends the Kubernetes Horizontal Pod Autoscaler (HPA) with custom resource definitions for ScaledObjects and ScaledJobs.
    image: https://keda.sh/img/logos/keda-icon-color.png
    humanUrl: https://keda.sh/
    baseUrl: https://api.keda.sh
    tags:
      - Auto Scaling
      - CNCF
      - Event-Driven
      - Kubernetes
      - Scale To Zero
    properties:
      - type: Documentation
        url: https://keda.sh/docs/
      - type: GitHub
        url: https://github.com/kedacore/keda
      - type: OpenAPI
        url: https://raw.githubusercontent.com/kedacore/keda/main/apis/keda/v1alpha1/
      - type: Changelog
        url: https://github.com/kedacore/keda/releases
      - type: Blog
        url: https://keda.sh/blog/
    contact:
      - type: GitHub Issues
        url: https://github.com/kedacore/keda/issues
      - type: Slack
        url: https://kubernetes.slack.com/archives/CKZJ36A5D
  - name: AWS Auto Scaling API
    description: Amazon Web Services Auto Scaling monitors applications and automatically adjusts capacity to maintain steady, predictable performance at the lowest possible cost. Supports EC2 Auto Scaling, Application Auto Scaling for ECS, DynamoDB, Lambda, and more. Part of the AWS SDK and REST API surface.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanUrl: https://aws.amazon.com/autoscaling/
    baseUrl: https://autoscaling.amazonaws.com
    tags:
      - Amazon Web Services
      - Auto Scaling
      - Cloud
      - EC2
      - Elasticity
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/autoscaling/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/APIs-guru/openapi-directory/main/APIs/amazonaws.com/autoscaling/2011-01-01/openapi.yaml
      - type: Pricing
        url: https://aws.amazon.com/autoscaling/pricing/
      - type: Getting Started
        url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/get-started-with-ec2-auto-scaling.html
    contact:
      - type: Support
        url: https://aws.amazon.com/contact-us/
  - name: Google Cloud Compute Engine Autoscaler API
    description: Google Cloud's Autoscaler API enables automatic scaling of managed instance groups based on CPU utilization, load balancing capacity, or Cloud Monitoring metrics. Integrates with Google Kubernetes Engine (GKE) for cluster autoscaling and node auto-provisioning.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanUrl: https://cloud.google.com/compute/docs/autoscaler
    baseUrl: https://compute.googleapis.com/compute/v1
    tags:
      - Auto Scaling
      - Cloud
      - GKE
      - Google Cloud
      - Instance Groups
    properties:
      - type: Documentation
        url: https://cloud.google.com/compute/docs/autoscaler
      - type: OpenAPI
        url: https://raw.githubusercontent.com/APIs-guru/openapi-directory/main/APIs/googleapis.com/compute/v1/openapi.yaml
      - type: Pricing
        url: https://cloud.google.com/compute/pricing
      - type: SDK
        url: https://cloud.google.com/sdk/docs
    contact:
      - type: Support
        url: https://cloud.google.com/support
  - name: Azure Autoscale REST API
    description: Microsoft Azure Autoscale provides a REST API for managing autoscale settings on Azure resources including Virtual Machine Scale Sets, App Service, and Azure Container Apps. Supports schedule-based and metric-based scaling rules with notification capabilities.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanUrl: https://learn.microsoft.com/en-us/azure/azure-monitor/autoscale/autoscale-overview
    baseUrl: https://management.azure.com
    tags:
      - Auto Scaling
      - Azure
      - Cloud
      - Microsoft
      - Virtual Machine Scale Sets
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/azure-monitor/autoscale/autoscale-overview
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/monitor/resource-manager/Microsoft.Insights/stable/2022-10-01/autoScale_API.json
      - type: SDK
        url: https://learn.microsoft.com/en-us/azure/developer/
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/
    contact:
      - type: Support
        url: https://azure.microsoft.com/en-us/support/
  - name: CloudWatch Application Signals API
    description: Amazon CloudWatch Application Signals provides application performance monitoring (APM) to help detect and diagnose performance issues and automatically correlate them with infrastructure metrics for scaling decisions. Part of the AWS observability suite used in scalability engineering.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanUrl: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals.html
    baseUrl: https://monitoring.amazonaws.com
    tags:
      - Amazon Web Services
      - Observability
      - APM
      - Monitoring
      - Performance
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/APIs-guru/openapi-directory/main/APIs/amazonaws.com/monitoring/2010-08-01/openapi.yaml
      - type: Getting Started
        url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GetStarted.html
    contact:
      - type: Support
        url: https://aws.amazon.com/contact-us/
  - name: Prometheus HTTP API
    description: Prometheus is the de-facto open-source monitoring and alerting toolkit for cloud-native applications and a CNCF graduate project. The Prometheus HTTP API provides access to time series data, metadata, and administrative functions used extensively in scalability engineering to track metrics and inform autoscaling decisions.
    image: https://prometheus.io/assets/prometheus_logo_grey.svg
    humanUrl: https://prometheus.io/
    baseUrl: https://prometheus.io/api/v1
    tags:
      - CNCF
      - Metrics
      - Monitoring
      - Observability
      - Open Source
      - Prometheus
      - Time Series
    properties:
      - type: Documentation
        url: https://prometheus.io/docs/prometheus/latest/querying/api/
      - type: GitHub
        url: https://github.com/prometheus/prometheus
      - type: OpenAPI
        url: https://raw.githubusercontent.com/prometheus/prometheus/main/web/api/v1/api.go
      - type: Getting Started
        url: https://prometheus.io/docs/introduction/first_steps/
    contact:
      - type: GitHub Issues
        url: https://github.com/prometheus/prometheus/issues
  - name: Grafana HTTP API
    description: Grafana is the open-source platform for monitoring and observability, providing a REST HTTP API for managing dashboards, data sources, users, and alerts. Widely used alongside Prometheus for scalability metrics visualization and alerting workflows.
    image: https://grafana.com/static/assets/img/fav32.png
    humanUrl: https://grafana.com/
    baseUrl: https://grafana.com/api
    tags:
      - Dashboards
      - Grafana
      - Metrics
      - Monitoring
      - Observability
      - Open Source
    properties:
      - type: Documentation
        url: https://grafana.com/docs/grafana/latest/developers/http_api/
      - type: GitHub
        url: https://github.com/grafana/grafana
      - type: Getting Started
        url: https://grafana.com/docs/grafana/latest/getting-started/
      - type: Pricing
        url: https://grafana.com/pricing/
    contact:
      - type: Community
        url: https://community.grafana.com/
common:
  - type: GitHub Organization
    url: https://github.com/kedacore
  - type: CNCF Landscape
    url: https://landscape.cncf.io/card-mode?category=auto-scaling
  - type: Blog
    url: https://kubernetes.io/blog/
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/scalability/main/json-schema/scalability-scaling-policy-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/scalability/main/json-schema/scalability-load-balancer-schema.json
  - type: JSONLd
    url: https://raw.githubusercontent.com/api-evangelist/scalability/main/json-ld/scalability-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/scalability/main/vocabulary/scalability-vocabulary.yml
maintainers:
  - FN: API Evangelist
    email: kin@apievangelist.com
    url: https://apievangelist.com
include:
  - name: Cloud Infrastructure Providers
    url: https://raw.githubusercontent.com/api-evangelist/scalable-infrastructure/refs/heads/main/apis.yml
  - name: Container Orchestration
    url: https://raw.githubusercontent.com/api-evangelist/scalable-architecture/refs/heads/main/apis.yml
  - name: Monitoring and Observability
    url: https://raw.githubusercontent.com/api-evangelist/scalable-platforms/refs/heads/main/apis.yml
---
