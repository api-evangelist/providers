---
aid: bigpanda
url: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/apis.yml
apis:
  - aid: bigpanda:bigpanda
    name: BigPanda
    tags:
      - Alerts
      - Audit
      - Changes
      - Correlation
      - Correlation Patterns
      - Enrichments
      - Environments
      - Incident Tags
      - Incidents
      - Logs
      - Maintenance
      - Maintenance Plans
      - Name
      - Patterns
      - Plans
      - Schedules
      - Topologies
      - Troubleshooting
      - Users
    humanURL: https://docs.bigpanda.io/reference/environments-api
    properties:
      - url: https://docs.bigpanda.io/reference/environments-api
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/openapi/bigpanda-openapi.yml
        type: OpenAPI
    description: Use the Environments API to define incident groups based on incident properties such as source, severity, or alert data.
name: BigPanda
tags:
  - Incidents
  - Monitoring
  - Platform
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - type: Portal
    url: https://docs.bigpanda.io
  - type: GettingStarted
    url: https://docs.bigpanda.io/docs/get-started
  - type: Documentation
    url: https://docs.bigpanda.io/reference
  - type: ChangeLog
    url: https://docs.bigpanda.io/docs/release-notes
  - type: PostmanWorkspace
    url: https://www.postman.com/bigpandaio/bigpanda-api-staging/overview
  - type: Status
    url: https://status.bigpanda.io/
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/rules/bigpanda-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/vocabulary/bigpanda-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/capabilities/incident-management.yaml
  - type: Features
    data:
      - name: AI Alert Correlation
        description: ML-powered correlation of alerts from 200+ monitoring tools into actionable incidents.
      - name: Incident Management
        description: Triage, acknowledge, and resolve correlated incidents with full audit trail.
      - name: Root Cause Analysis
        description: Automatically identify root causes by correlating alerts with change events.
      - name: Maintenance Plans
        description: Schedule maintenance windows to suppress expected alerts during planned work.
      - name: Change Correlation
        description: Ingest deployment and config changes to correlate with alert spikes.
      - name: Environments
        description: Define DSL-based environments to group incidents by source, severity, or host.
      - name: Enrichments
        description: Enrich alerts with contextual tags from CMDB and other data sources.
      - name: AIOps Automation
        description: Automate incident response workflows with AI-driven insights and routing.
  - type: UseCases
    data:
      - name: Alert Noise Reduction
        description: Reduce alert fatigue by correlating thousands of alerts into a handful of incidents.
      - name: Change Impact Analysis
        description: Automatically link deployment changes to alert spikes for faster root cause identification.
      - name: On-Call Automation
        description: Route correlated incidents to the right on-call team with full context.
      - name: Maintenance Scheduling
        description: Suppress alerts during planned maintenance to prevent false incident creation.
      - name: ITSM Integration
        description: Automatically create and update tickets in ServiceNow or Jira from correlated incidents.
  - type: Integrations
    data:
      - name: PagerDuty
        description: Route correlated incidents to PagerDuty for on-call alerting.
      - name: ServiceNow
        description: Create and update ServiceNow incidents automatically from BigPanda.
      - name: Datadog
        description: Ingest Datadog alerts into BigPanda for cross-tool correlation.
      - name: Nagios
        description: Ingest Nagios monitoring alerts via BigPanda integration.
      - name: Prometheus
        description: Correlate Prometheus/Alertmanager alerts in BigPanda.
      - name: Jira
        description: Create Jira issues from BigPanda incidents for engineering tracking.
created: '2025-01-08'
modified: '2026-04-19'
position: Consuming
description: BigPanda is a software platform that uses artificial intelligence (AI) to help IT operations teams automate incident management by correlating alerts from various systems, identifying root causes, and streamlining the incident resolution process, essentially moving from reactive to proactive incident response by providing context and insights through intelligent data analysis.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
