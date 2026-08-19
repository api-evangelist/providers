---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Spot By Netapp Agentic Access
  operation_count: 36
  slug: spot-by-netapp-agentic-access
  summary_line: 36 operations · 18 acting
api_count: 10
apis:
- description: The Audit Service API from Spot by NetApp — 3 operation(s) for audit service.
  name: Spot by NetApp Audit Service API
  slug: spot-by-netapp-audit-service-api
- description: The Create an API Token API from Spot by NetApp — 1 operation(s) for create an api token.
  name: Spot by NetApp Create an API Token API
  slug: spot-by-netapp-create-an-api-token-api
- description: The Elastigroup AWS API from Spot by NetApp — 6 operation(s) for elastigroup aws.
  name: Spot by NetApp Elastigroup AWS API
  slug: spot-by-netapp-elastigroup-aws-api
- description: The Elastigroup Azure Spot VMs API from Spot by NetApp — 2 operation(s) for elastigroup azure spot vms.
  name: Spot by NetApp Elastigroup Azure Spot VMs API
  slug: spot-by-netapp-elastigroup-azure-spot-vms-api
- description: The Elastigroup GCP API from Spot by NetApp — 2 operation(s) for elastigroup gcp.
  name: Spot by NetApp Elastigroup GCP API
  slug: spot-by-netapp-elastigroup-gcp-api
- description: The Health Check Service API from Spot by NetApp — 1 operation(s) for health check service.
  name: Spot by NetApp Health Check Service API
  slug: spot-by-netapp-health-check-service-api
- description: The Insights Service API from Spot by NetApp — 1 operation(s) for insights service.
  name: Spot by NetApp Insights Service API
  slug: spot-by-netapp-insights-service-api
- description: The Notification Subscription Service API from Spot by NetApp — 1 operation(s) for notification subscription service.
  name: Spot by NetApp Notification Subscription Service API
  slug: spot-by-netapp-notification-subscription-service-api
- description: The Ocean Automatic Rightsizing API from Spot by NetApp — 1 operation(s) for ocean automatic rightsizing.
  name: Spot by NetApp Ocean Automatic Rightsizing API
  slug: spot-by-netapp-ocean-automatic-rightsizing-api
- description: The Ocean AWS API from Spot by NetApp — 3 operation(s) for ocean aws.
  name: Spot by NetApp Ocean AWS API
  slug: spot-by-netapp-ocean-aws-api
artifact_total: 46
collections:
- collection_type: postman
  name: Spot by NetApp Audit Service API
  slug: postman-spot-by-netapp-audit-service-api
- collection_type: postman
  name: Spot by NetApp Audit Service Create an API Token API
  slug: postman-spot-by-netapp-create-an-api-token-api
- collection_type: postman
  name: Spot by NetApp Audit Service Elastigroup AWS API
  slug: postman-spot-by-netapp-elastigroup-aws-api
- collection_type: postman
  name: Spot by NetApp Audit Service Elastigroup Azure Spot VMs API
  slug: postman-spot-by-netapp-elastigroup-azure-spot-vms-api
- collection_type: postman
  name: Spot by NetApp Audit Service Elastigroup GCP API
  slug: postman-spot-by-netapp-elastigroup-gcp-api
- collection_type: postman
  name: Spot by NetApp Audit Service Health Check Service API
  slug: postman-spot-by-netapp-health-check-service-api
- collection_type: postman
  name: Spot by NetApp Audit Service Insights Service API
  slug: postman-spot-by-netapp-insights-service-api
- collection_type: postman
  name: Spot by NetApp Audit Service Notification Subscription Service API
  slug: postman-spot-by-netapp-notification-subscription-service-api
- collection_type: postman
  name: Spot by NetApp Audit Service Ocean Automatic Rightsizing API
  slug: postman-spot-by-netapp-ocean-automatic-rightsizing-api
- collection_type: postman
  name: Spot by NetApp Audit Service Ocean AWS API
  slug: postman-spot-by-netapp-ocean-aws-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Spot by NetApp Audit Service API
  slug: open-spot-by-netapp-audit-service-api
- collection_type: open
  name: Spot by NetApp Audit Service Create an API Token API
  slug: open-spot-by-netapp-create-an-api-token-api
- collection_type: open
  name: Spot by NetApp Audit Service Elastigroup AWS API
  slug: open-spot-by-netapp-elastigroup-aws-api
- collection_type: open
  name: Spot by NetApp Audit Service Elastigroup Azure Spot VMs API
  slug: open-spot-by-netapp-elastigroup-azure-spot-vms-api
- collection_type: open
  name: Spot by NetApp Audit Service Elastigroup GCP API
  slug: open-spot-by-netapp-elastigroup-gcp-api
- collection_type: open
  name: Spot by NetApp Audit Service Health Check Service API
  slug: open-spot-by-netapp-health-check-service-api
- collection_type: open
  name: Spot by NetApp Audit Service Insights Service API
  slug: open-spot-by-netapp-insights-service-api
- collection_type: open
  name: Spot by NetApp Audit Service Notification Subscription Service API
  slug: open-spot-by-netapp-notification-subscription-service-api
- collection_type: open
  name: Spot by NetApp Audit Service Ocean Automatic Rightsizing API
  slug: open-spot-by-netapp-ocean-automatic-rightsizing-api
- collection_type: open
  name: Spot by NetApp Audit Service Ocean AWS API
  slug: open-spot-by-netapp-ocean-aws-api
- collection_type: open
  name: Spot by NetApp API
  slug: open-spot-by-netapp
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/spot-by-netapp/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spot-by-netapp-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spot-by-netapp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spot-by-netapp-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spothq
- group: company
  title: ''
  type: Website
  url: https://spot.io/
- group: start
  title: ''
  type: Portal
  url: https://docs.spot.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spot.io/
- group: docs
  title: ''
  type: Reference
  url: https://docs.spot.io/api/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/spotinst
- group: build
  title: ''
  type: SDKs
  url: https://github.com/spotinst/spotinst-sdk-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/spotinst/spotinst-sdk-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/spotinst/spotinst-sdk-nodejs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/spotinst/spotinst-sdk-python
- group: other
  title: ''
  type: Terraform
  url: https://github.com/spotinst/terraform-provider-spotinst
- group: other
  title: ''
  type: Helm
  url: https://github.com/spotinst/spotinst-kubernetes-helm-charts
- group: build
  title: ''
  type: CLI
  url: https://github.com/spotinst/spotctl
- group: start
  title: ''
  type: Console
  url: https://console.spotinst.com/
- group: start
  title: ''
  type: Login
  url: https://console.spotinst.com/
- group: company
  title: ''
  type: Blog
  url: https://www.flexera.com/blog/finops/feed/
created: '2026-03-27'
description: Spot by NetApp (formerly Spot by Flexera, originally Spotinst) is a cloud infrastructure optimization platform providing automated cost optimization, scaling, and intelligent management for cloud workloads across AWS, Azure, and GCP. The Spot platform includes Elastigroup for intelligent auto-scaling using Spot instances, Ocean for Kubernetes and container cost optimization, Stateful Nodes for stateful workloads, EMR Scaler for Hadoop workloads, and Ocean CD for progressive delivery. The platform delivers FinOps capabilities including rightsizing recommendations, cost analysis, and cloud spend visibility.
examples:
- key_count: 4
  name: Spot Create Elastigroup Example
  slug: spot-create-elastigroup-example
- key_count: 4
  name: Spot Get Cost Summary Example
  slug: spot-get-cost-summary-example
finops:
- name: Spot By Netapp Finops
  service_category: API
  slug: spot-by-netapp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spot-by-netapp.png
json_schemas:
- name: Spot Elastigroup
  property_count: 9
  slug: spot-elastigroup
- name: Spot Ocean Cluster
  property_count: 10
  slug: spot-ocean-cluster
json_structures:
- name: Spot By Netapp Structure
  property_count: 0
  slug: spot-by-netapp-structure
jsonld:
- class_count: 39
  name: Spot By Netapp Context
  property_count: 3
  slug: spot-by-netapp-context
layout: provider
modified: '2026-05-19'
name: Spot by NetApp
nav: Providers
network: true
overview: 'Spot by NetApp publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Audit Service API, Create an API Token API, Elastigroup AWS API, and 7 more. Tagged areas include Cloud Optimization, FinOps, Kubernetes, Azure, and GCP.


  The Spot by NetApp catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Spot by NetApp''s developer surface includes authentication, developer portal, documentation, GitHub presence, CLI, developer console, engineering blog, and 13 more developer resources.'
plans:
- name: Spot By Netapp Plans Pricing
  plan_count: 3
  slug: spot-by-netapp-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 5
  name: Spot By Netapp Rate Limits
  slug: spot-by-netapp-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Spot by NetApp API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: spot-by-netapp-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Spot by NetApp API Rules
  rule_count: 11
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 5
  slug: spot-by-netapp-rules
score:
  band: developing
  composite: 43.2
  delta: -8.7
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 63.6
    developer_ergonomics: 69.0
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 13.2
  previous_composite: 51.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/spot-by-netapp/refs/heads/main/screenshots/spot-by-netapp-2026-06-20T194351.png
security:
- kind: authentication
  name: Spot By Netapp Authentication
  slug: spot-by-netapp-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Spot By Netapp Domain Security
  slug: spot-by-netapp-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: spot-by-netapp
tags:
- Cloud Optimization
- FinOps
- Kubernetes
- Azure
- GCP
- Cost Optimization
- Auto Scaling
website: https://spot.io/
---
