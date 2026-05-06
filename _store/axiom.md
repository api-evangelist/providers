---
aid: axiom
name: Axiom
description: Axiom is a serverless log management and analytics platform that provides real-time insights into structured and unstructured data with fast querying capabilities for logs, events, and telemetry data.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Log Management
  - Logging
  - Observability
  - Real-Time
  - Serverless
url: https://raw.githubusercontent.com/api-evangelist/axiom/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: axiom:axiom-api
    name: Axiom API
    description: RESTful API for ingesting, querying, and managing logs and events in Axiom.
    humanURL: https://axiom.co/docs/restapi/introduction
    baseURL: https://api.axiom.co
    tags:
      - Analytics
      - Logging
      - Observability
    properties:
      - type: Documentation
        url: https://axiom.co/docs/restapi/introduction
      - type: Authentication
        url: https://axiom.co/docs/restapi/token
common:
  - type: Portal
    url: https://axiom.co/
  - type: StatusPage
    url: https://status.axiom.co
  - type: Blog
    url: https://axiom.co/blog
  - type: GitHubOrganization
    url: https://github.com/axiomhq
  - type: TermsOfService
    url: https://axiom.co/terms
  - type: PrivacyPolicy
    url: https://axiom.co/privacy
  - type: SignUp
    url: https://app.axiom.co/register
  - type: Pricing
    url: https://axiom.co/pricing
  - type: Documentation
    url: https://axiom.co/docs
  - type: GettingStarted
    url: https://axiom.co/docs/get-started
  - type: Features
    data:
      - name: Serverless Log Management
        description: Manage logs without managing servers or storage infrastructure.
      - name: Real-Time Querying
        description: Query billions of events in seconds with APL (Axiom Processing Language).
      - name: Dataset Organization
        description: Organize data into datasets with role-based access control.
      - name: Monitors and Alerts
        description: Create monitors with alert notifications to Slack, PagerDuty, and email.
      - name: OpenTelemetry Native
        description: Native OTLP ingestion for logs, metrics, and traces.
      - name: Endless Retention
        description: Store data indefinitely with query-optimized cold storage.
      - name: Dashboards
        description: Build and share monitoring dashboards with rich visualization options.
      - name: Annotations
        description: Mark events like deployments on dashboards for correlation analysis.
  - type: UseCases
    data:
      - name: Application Logging
        description: Centralize application logs for debugging and error analysis.
      - name: DevOps Observability
        description: Monitor CI/CD pipelines, deployments, and infrastructure health.
      - name: Security Analytics
        description: Analyze audit logs and detect security anomalies.
      - name: Edge Function Monitoring
        description: Monitor Vercel, Cloudflare, and other edge function execution.
      - name: Distributed Tracing
        description: Trace requests across services using OpenTelemetry OTLP.
  - type: Integrations
    data:
      - name: Vercel
        description: Official Vercel integration for log drains and deployment tracking.
      - name: OpenTelemetry
        description: Ingest OTLP telemetry from any OTel-compatible source.
      - name: AWS Lambda
        description: Forward Lambda logs to Axiom via log subscriptions.
      - name: Kubernetes
        description: Collect pod and node logs using the Axiom DaemonSet or Helm chart.
      - name: GitHub Actions
        description: Send CI/CD logs from GitHub Actions to Axiom for analysis.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
