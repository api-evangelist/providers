---
aid: amazon-managed-prometheus
url: https://raw.githubusercontent.com/api-evangelist/amazon-managed-prometheus/refs/heads/main/apis.yml
apis:
- aid: amazon-managed-prometheus:amazon-managed-prometheus-api
  name: Amazon Managed Service for Prometheus API
  description: The Amazon Managed Service for Prometheus API provides programmatic access to create and manage workspaces, alert manager definitions, rule groups namespaces, and scrapers for Prometheus-compatible monitoring.
  humanURL: https://aws.amazon.com/prometheus/
  baseURL: https://aps.amazonaws.com
  tags:
  - Containers
  - Monitoring
  - Prometheus
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference.html
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/amp/2020-08-01/openapi.yaml
  - type: Getting Started
    url: https://aws.amazon.com/prometheus/getting-started/
  - type: Pricing
    url: https://aws.amazon.com/prometheus/pricing/
  - type: FAQ
    url: https://aws.amazon.com/prometheus/faqs/
name: Amazon Managed Service for Prometheus
tags:
- AWS
- Containers
- Monitoring
- Observability
- Prometheus
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon Managed Service for Prometheus is a serverless, Prometheus-compatible monitoring service for container metrics. It automatically scales as your monitoring needs increase, works with open-source tools, and integrates with Amazon EKS and other container environments.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

