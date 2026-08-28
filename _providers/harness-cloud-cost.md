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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Harness Cloud Cost Agentic Access
  operation_count: 17
  slug: harness-cloud-cost-agentic-access
  summary_line: 17 operations · 7 acting
api_count: 6
apis:
- description: Detect and review unusual cost patterns and anomalies.
  name: Harness Cloud Cost Management Anomalies API
  slug: harness-cloud-cost-anomalies-api
- description: Define and monitor cloud spending budgets with alerts.
  name: Harness Cloud Cost Management Budgets API
  slug: harness-cloud-cost-budgets-api
- description: Manage cloud provider and Kubernetes connectors for cost ingestion.
  name: Harness Cloud Cost Management Connectors API
  slug: harness-cloud-cost-connectors-api
- description: Allocate and chargeback cloud costs by business units.
  name: Harness Cloud Cost Management Cost Categories API
  slug: harness-cloud-cost-cost-categories-api
- description: Group and analyze cloud cost data through customizable views.
  name: Harness Cloud Cost Management Perspectives API
  slug: harness-cloud-cost-perspectives-api
- description: AI-driven recommendations for cloud cost optimization.
  name: Harness Cloud Cost Management Recommendations API
  slug: harness-cloud-cost-recommendations-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Harness Cloud Cost Management Anomalies API
  slug: open-harness-cloud-cost-anomalies-api
- collection_type: open
  name: Harness Cloud Cost Management Anomalies Budgets API
  slug: open-harness-cloud-cost-budgets-api
- collection_type: open
  name: Harness Cloud Cost Management Anomalies Connectors API
  slug: open-harness-cloud-cost-connectors-api
- collection_type: open
  name: Harness Cloud Cost Management Anomalies Cost Categories API
  slug: open-harness-cloud-cost-cost-categories-api
- collection_type: open
  name: Harness Cloud Cost Management Anomalies Perspectives API
  slug: open-harness-cloud-cost-perspectives-api
- collection_type: open
  name: Harness Cloud Cost Management Anomalies Recommendations API
  slug: open-harness-cloud-cost-recommendations-api
- collection_type: open
  name: Harness Cloud Cost Management API
  slug: open-harness-cloud-cost
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/harness-cloud-cost-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/harness-cloud-cost-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/harness-cloud-cost-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harness-cloud-cost-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/harness-cloud-cost-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/harness
- group: company
  title: ''
  type: Website
  url: https://www.harness.io/products/cloud-cost
- group: docs
  title: ''
  type: Documentation
  url: https://developer.harness.io/docs/cloud-cost-management
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.harness.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.harness.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.harness.io
- group: agent
  title: ''
  type: LlmsText
  url: https://apidocs.harness.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.harness.io/blog/rss.xml
created: '2026-03-27'
description: Harness Cloud Cost Management (CCM) provides intelligent cloud cost optimization with AI-driven recommendations, customizable cost perspectives, budgets, anomaly detection, and chargeback / showback through cost categories. CCM ingests cost data from AWS, Azure, GCP, and Kubernetes clusters and exposes a REST API on the Harness platform for FinOps automation.
finops:
- name: Harness Cloud Cost Finops
  service_category: API
  slug: harness-cloud-cost-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/harness-cloud-cost.png
layout: provider
modified: '2026-05-19'
name: Harness Cloud Cost Management
nav: Providers
network: true
overview: 'Harness Cloud Cost Management publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Anomalies API, Budgets API, Connectors API, and 3 more. Tagged areas include Anomaly Detection, Budgets, Cloud Cost Management, FinOps, and Kubernetes.


  The Harness Cloud Cost Management catalog on APIs.io includes 1 Spectral governance ruleset.


  Harness Cloud Cost Management''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Harness Cloud Cost Plans Pricing
  plan_count: 3
  slug: harness-cloud-cost-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Harness Cloud Cost Rate Limits
  slug: harness-cloud-cost-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Harness Cloud Cost Management API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: harness-cloud-cost-rules
score:
  band: developing
  composite: 40.3
  delta: 2.4
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 42.9
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/harness-cloud-cost/refs/heads/main/screenshots/harness-cloud-cost-2026-06-20T182521.png
security:
- kind: authentication
  name: Harness Cloud Cost Authentication
  slug: harness-cloud-cost-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Harness Cloud Cost Domain Security
  slug: harness-cloud-cost-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Harness Cloud Cost Vulnerability Disclosure
  slug: harness-cloud-cost-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Harness Cloud Cost Trust Center
  slug: harness-cloud-cost-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, GDPR, CSA STAR
slug: harness-cloud-cost
tags:
- Anomaly Detection
- Budgets
- Cloud Cost Management
- FinOps
- Kubernetes
- Recommendations
website: https://www.harness.io/products/cloud-cost
---
