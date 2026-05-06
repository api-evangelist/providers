---
aid: axiom-controller
name: Axiom Controller
description: Axiom is a cloud-native observability platform providing APIs for ingesting, querying, and managing telemetry data including logs, traces, and metrics with support for datasets, monitors, and organization management.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Cloud Native
  - Logging
  - Monitoring
  - Observability
  - Telemetry
url: https://raw.githubusercontent.com/api-evangelist/axiom-controller/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: axiom-controller:axiom-ingest-api
    name: Axiom Ingest API
    description: API for ingesting logs, events, and telemetry data into Axiom datasets.
    humanURL: https://axiom.co/docs/restapi/ingest
    baseURL: https://api.axiom.co/v1
    tags:
      - Events
      - Ingest
      - Logs
      - Telemetry
    properties:
      - type: Documentation
        url: https://axiom.co/docs/restapi/ingest
  - aid: axiom-controller:axiom-query-api
    name: Axiom Query API
    description: API for querying and analyzing data stored in Axiom datasets using APL (Axiom Processing Language).
    humanURL: https://axiom.co/docs/restapi/query
    baseURL: https://api.axiom.co/v1
    tags:
      - Analytics
      - APL
      - Query
    properties:
      - type: Documentation
        url: https://axiom.co/docs/restapi/query
common:
  - type: Portal
    url: https://axiom.co/
  - type: Authentication
    url: https://axiom.co/docs/restapi/token
  - type: StatusPage
    url: https://status.axiom.co
  - type: Blog
    url: https://axiom.co/blog
  - type: TermsOfService
    url: https://axiom.co/terms
  - type: PrivacyPolicy
    url: https://axiom.co/privacy
  - type: GitHubOrganization
    url: https://github.com/axiomhq
  - type: Pricing
    url: https://axiom.co/pricing
  - type: Documentation
    url: https://axiom.co/docs
  - type: GettingStarted
    url: https://axiom.co/docs/get-started
  - type: Features
    data:
      - name: Log Ingestion
        description: Ingest logs from any source at massive scale with compression.
      - name: APL Query Language
        description: Query telemetry data using Axiom Processing Language (APL), inspired by KQL.
      - name: Dataset Management
        description: Organize telemetry data in datasets for granular access control and retention.
      - name: Monitors and Alerts
        description: Set up threshold-based and anomaly-detection monitors with PagerDuty/Slack integrations.
      - name: OpenTelemetry Support
        description: Native support for OpenTelemetry traces, metrics, and logs via OTLP.
      - name: Long-Term Retention
        description: Store telemetry data for extended periods at low cost with queryable archives.
      - name: Dashboards
        description: Build custom dashboards with rich visualization for monitoring application health.
  - type: UseCases
    data:
      - name: Application Logging
        description: Centralize application logs for debugging and troubleshooting.
      - name: Infrastructure Monitoring
        description: Monitor infrastructure metrics and detect anomalies.
      - name: Security Analytics
        description: Analyze security logs and audit trails for threat detection.
      - name: Distributed Tracing
        description: Trace requests across microservices with OpenTelemetry.
      - name: Business Analytics
        description: Analyze user behavior and business events stored as structured logs.
  - type: Integrations
    data:
      - name: OpenTelemetry
        description: Ingest OTLP data from any OpenTelemetry-compatible source.
      - name: Vercel
        description: Built-in Vercel log drain integration for edge function and deployment logs.
      - name: AWS CloudWatch
        description: Forward CloudWatch logs to Axiom via Lambda log forwarder.
      - name: Kubernetes
        description: Deploy Axiom Helm charts to collect Kubernetes logs and metrics.
      - name: GitHub Actions
        description: Send CI/CD pipeline logs to Axiom from GitHub Actions workflows.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
