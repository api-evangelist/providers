---
aid: amazon-managed-grafana
name: Amazon Managed Grafana
description: Amazon Managed Grafana is a fully managed service for open source Grafana developed in collaboration with Grafana Labs. It enables interactive data visualizations and dashboards for operational metrics, logs, and traces from multiple sources including AWS services, third-party ISVs, and on-premises data. The service handles provisioning, setup, scaling, and maintenance of Grafana, allowing teams to focus on creating dashboards and analyzing data.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Dashboards
  - Monitoring
  - Observability
  - Visualization
url: https://raw.githubusercontent.com/api-evangelist/amazon-managed-grafana/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-managed-grafana:amazon-managed-grafana-api
    name: Amazon Managed Grafana API
    description: The Amazon Managed Grafana API provides programmatic access to create and manage Grafana workspaces, users, SAML configurations, and workspace API keys for managed Grafana deployments. Covers workspace lifecycle management, authentication configuration, license association, and access control across all managed Grafana resources.
    humanURL: https://aws.amazon.com/grafana/
    baseURL: https://grafana.amazonaws.com
    tags:
      - Dashboards
      - Monitoring
      - Observability
      - Visualization
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/grafana/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-managed-grafana-openapi-original.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/grafana/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/grafana/pricing/
      - type: FAQ
        url: https://aws.amazon.com/grafana/faqs/
      - type: JSONSchema
        url: json-schema/amazon-managed-grafana-workspace-summary-schema.json
      - type: JSONStructure
        url: json-structure/amazon-managed-grafana-workspace-summary-structure.json
      - type: JSON-LD
        url: json-ld/amazon-managed-grafana-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/grafana/
  - type: Documentation
    url: https://docs.aws.amazon.com/grafana/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/mt/tag/amazon-managed-grafana/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/grafana/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-managed-grafana-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-managed-grafana-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/observability-dashboard-workflow.yaml
  - type: Features
    data:
      - name: Fully Managed Grafana
        description: Provision and manage Grafana workspaces without infrastructure setup, patching, or scaling.
      - name: SSO and SAML Integration
        description: Configure SAML-based single sign-on for workspace authentication and user management.
      - name: Multi-Source Data Visualization
        description: Connect to AWS services, third-party ISVs, and on-premises data sources in a single dashboard.
      - name: Workspace API Keys
        description: Create and manage API keys for programmatic access to Grafana workspace resources.
      - name: License Management
        description: Associate and manage Grafana Enterprise licenses for advanced features.
      - name: VPC Integration
        description: Deploy workspaces within a VPC for secure private access to data sources.
      - name: Role-Based Access Control
        description: Manage user and group permissions within Grafana workspaces using role assignments.
  - type: UseCases
    data:
      - name: Infrastructure Monitoring
        description: Visualize AWS infrastructure metrics from CloudWatch, EC2, RDS, and other services in unified dashboards.
      - name: Container Observability
        description: Monitor Kubernetes and ECS workloads using Prometheus and CloudWatch Container Insights data sources.
      - name: Application Performance Monitoring
        description: Track application latency, error rates, and throughput with custom dashboards and alerting.
      - name: Business Metrics Dashboards
        description: Build executive dashboards combining operational and business metrics from multiple data sources.
      - name: Security and Compliance Monitoring
        description: Visualize security findings and compliance metrics from AWS Security Hub and GuardDuty.
  - type: Integrations
    data:
      - name: Amazon CloudWatch
        description: Visualize CloudWatch metrics and logs natively in Grafana dashboards.
      - name: Amazon Managed Service for Prometheus
        description: Query Prometheus metrics from AMP workspaces as a Grafana data source.
      - name: AWS X-Ray
        description: Trace application requests and visualize distributed tracing data in Grafana.
      - name: Amazon OpenSearch Service
        description: Query OpenSearch indices for log analytics and visualization.
      - name: Amazon Timestream
        description: Visualize time-series data stored in Amazon Timestream.
      - name: AWS IAM Identity Center
        description: Integrate with IAM Identity Center for centralized user authentication.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
