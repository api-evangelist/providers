---
aid: amazon-managed-prometheus
name: Amazon Managed Service for Prometheus
description: Amazon Managed Service for Prometheus is a serverless, Prometheus-compatible monitoring service for container metrics. It automatically scales as your monitoring needs increase, works with open-source tools, and integrates with Amazon EKS and other container environments. The service provides fully managed workspaces, alert manager definitions, and rule group namespaces for Prometheus-compatible monitoring at scale.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Containers
  - Monitoring
  - Observability
  - Prometheus
url: https://raw.githubusercontent.com/api-evangelist/amazon-managed-prometheus/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-managed-prometheus:amazon-managed-prometheus-api
    name: Amazon Managed Service for Prometheus API
    description: The Amazon Managed Service for Prometheus API provides programmatic access to create and manage workspaces, alert manager definitions, rule groups namespaces, logging configurations, and scrapers for Prometheus-compatible monitoring. Covers the full workspace lifecycle and monitoring configuration management.
    humanURL: https://aws.amazon.com/prometheus/
    baseURL: https://aps.amazonaws.com
    tags:
      - Containers
      - Monitoring
      - Observability
      - Prometheus
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference.html
      - type: OpenAPI
        url: openapi/amazon-managed-prometheus-openapi-original.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/prometheus/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/prometheus/pricing/
      - type: FAQ
        url: https://aws.amazon.com/prometheus/faqs/
      - type: JSONSchema
        url: json-schema/amazon-managed-prometheus-workspace-summary-schema.json
      - type: JSONStructure
        url: json-structure/amazon-managed-prometheus-workspace-summary-structure.json
      - type: JSON-LD
        url: json-ld/amazon-managed-prometheus-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/prometheus/
  - type: Documentation
    url: https://docs.aws.amazon.com/prometheus/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/mt/tag/amazon-managed-service-for-prometheus/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/prometheus/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-managed-prometheus-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-managed-prometheus-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/metrics-monitoring-workflow.yaml
  - type: Features
    data:
      - name: Serverless Prometheus
        description: Run Prometheus-compatible monitoring without managing servers, scaling, or high availability.
      - name: Alert Manager Definitions
        description: Configure Prometheus AlertManager rules for routing, grouping, and suppressing alerts.
      - name: Rule Groups Namespaces
        description: Define and manage Prometheus recording and alerting rules organized in namespaces.
      - name: Managed Scrapers
        description: Create managed scrapers to automatically collect metrics from Amazon EKS clusters.
      - name: Logging Configuration
        description: Configure logging for Prometheus workspaces to capture operational events.
      - name: Prometheus-Compatible APIs
        description: Use standard Prometheus remote write and query APIs with existing tooling and clients.
  - type: UseCases
    data:
      - name: Kubernetes Cluster Monitoring
        description: Monitor EKS clusters and Kubernetes workloads with Prometheus metrics at any scale.
      - name: Container Performance Metrics
        description: Collect and analyze container CPU, memory, and network metrics for performance optimization.
      - name: Microservices Observability
        description: Monitor distributed microservices with Prometheus metrics and custom alert rules.
      - name: Infrastructure Capacity Planning
        description: Track resource utilization trends over time for infrastructure capacity planning.
      - name: SLA Monitoring
        description: Define SLO-based alerting rules to monitor service level agreements in real time.
  - type: Integrations
    data:
      - name: Amazon EKS
        description: Collect metrics from EKS clusters using managed scrapers and Prometheus remote write.
      - name: Amazon Managed Grafana
        description: Visualize Prometheus metrics in Grafana dashboards using AMP as a data source.
      - name: AWS Distro for OpenTelemetry
        description: Use ADOT collectors to send metrics to AMP workspaces via remote write.
      - name: Amazon CloudWatch
        description: Forward Prometheus alerts and metrics to CloudWatch for cross-service monitoring.
      - name: Prometheus Alertmanager
        description: Use native Prometheus Alertmanager configuration for alert routing and notification.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
