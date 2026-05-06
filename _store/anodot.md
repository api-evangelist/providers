---
aid: anodot
name: Anodot
description: Anodot is an AI-powered business monitoring and cloud cost management platform providing autonomous anomaly detection, cost optimization, and real-time alerts for cloud infrastructure, business metrics, and FinOps workflows.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI
  - Anomaly Detection
  - Business Monitoring
  - Cloud Cost Management
  - FinOps
  - Machine Learning
  - Observability
url: https://raw.githubusercontent.com/api-evangelist/anodot/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: anodot:anodot-business-monitoring-api
    name: Anodot Business Monitoring API
    description: The Anodot Business Monitoring API provides REST endpoints for anomaly detection, alert management, forecasting, metric submission, user management, and data integration. It supports bearer token authentication and basic authentication with a data collection key. Regional deployments cover US, EU (Frankfurt), Asia Pacific, India, and US West Coast. Rate limits are 500 calls/minute by default (5,000 RPM for metric posting).
    humanURL: https://docs.anodot.com/
    baseURL: https://app.anodot.com
    tags:
      - AI
      - Alerts
      - Anomaly Detection
      - Business Monitoring
      - Forecasting
      - Machine Learning
      - Metrics
      - REST
      - Webhooks
    properties:
      - url: https://docs.anodot.com/
        type: Documentation
      - url: https://docs.anodot.com/reference/authentication
        type: Authentication
      - url: https://www.anodot.com/
        type: Website
  - aid: anodot:anodot-cloud-cost-api
    name: Anodot Cloud Cost Management API
    description: The Anodot Cloud Cost Management API provides programmatic access to cloud cost data, anomaly detection for cost spikes, cost allocation, budget management, and optimization recommendations across AWS, Azure, and GCP.
    humanURL: https://cloudcost.anodot.com/
    baseURL: https://cloudcost.anodot.com
    tags:
      - AWS
      - Azure
      - Cloud Cost Management
      - Cost Allocation
      - Cost Optimization
      - FinOps
      - GCP
      - Multi-Cloud
    properties:
      - url: https://cloudcost.anodot.com/hc/en-us/articles/9796736183964-What-s-New-in-Anodot-Cost
        type: Changelog
      - url: https://www.anodot.com/cloud-cost-management/
        type: Documentation
common:
  - url: https://www.anodot.com/
    name: Anodot Website
    type: Website
  - url: https://docs.anodot.com/
    name: Anodot API Documentation
    type: Documentation
  - url: https://cloudcost.anodot.com/
    name: Anodot Cloud Cost Portal
    type: Portal
  - url: https://www.anodot.com/resources/
    name: Anodot Resources
    type: Resources
  - url: https://www.anodot.com/cloud-cost-management/
    name: Cloud Cost Management
    type: Features
  - url: https://www.anodot.com/cloud-cost-management/reporting/
    name: Cost Reporting
    type: Features
  - url: https://www.anodot.com/blog/
    name: Anodot Blog
    type: Blog
  - url: https://www.anodot.com/privacy-policy/
    name: Privacy Policy
    type: PrivacyPolicy
  - url: https://www.anodot.com/terms-of-service/
    name: Terms of Service
    type: TermsOfService
  - url: https://github.com/anodot
    name: Anodot GitHub Organization
    type: GitHubOrganization
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
