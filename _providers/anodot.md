---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Anodot Agentic Access
  operation_count: 34
  slug: anodot-agentic-access
  summary_line: 34 operations · 11 acting
api_count: 9
apis:
- description: The Anodot Cloud Cost Management API provides programmatic access to cloud cost data, anomaly detection for cost spikes, cost allocation, budget management, and optimization recommendations across AWS
  name: Anodot Cloud Cost Management API
  slug: anodot-cloud-cost-api
- baseURL: https://app.anodot.com
  baseurl_source: declared
  description: The Access Token API from Anodot — 1 operation(s) for access token.
  name: Anodot Access Token API
  slug: anodot-access-token-api
- baseURL: https://app.anodot.com
  baseurl_source: declared
  description: The Alert Actions API from Anodot — 6 operation(s) for alert actions.
  name: Anodot Alert Actions API
  slug: anodot-alert-actions-api
- baseURL: https://app.anodot.com
  baseurl_source: declared
  description: The Alerts API from Anodot — 5 operation(s) for alerts.
  name: Anodot Alerts API
  slug: anodot-alerts-api
- baseURL: https://app.anodot.com
  baseurl_source: declared
  description: The Anomalies API from Anodot — 5 operation(s) for anomalies.
  name: Anodot Anomalies API
  slug: anodot-anomalies-api
- baseURL: https://app.anodot.com
  baseurl_source: declared
  description: The Customers API from Anodot — 1 operation(s) for customers.
  name: Anodot Customers API
  slug: anodot-customers-api
- baseURL: https://app.anodot.com
  baseurl_source: declared
  description: The Forecast API from Anodot — 9 operation(s) for forecast.
  name: Anodot Forecast API
  slug: anodot-forecast-api
- baseURL: https://app.anodot.com
  baseurl_source: declared
  description: The Groups API from Anodot — 1 operation(s) for groups.
  name: Anodot Groups API
  slug: anodot-groups-api
- baseURL: https://app.anodot.com
  baseurl_source: declared
  description: The Users API from Anodot — 1 operation(s) for users.
  name: Anodot Users API
  slug: anodot-users-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Anodot Business Monitoring Access Token API
  slug: open-anodot-access-token-api
- collection_type: open
  name: Anodot Business Monitoring Access Token Alert Actions API
  slug: open-anodot-alert-actions-api
- collection_type: open
  name: Anodot Business Monitoring Access Token Alerts API
  slug: open-anodot-alerts-api
- collection_type: open
  name: Anodot Business Monitoring Access Token Anomalies API
  slug: open-anodot-anomalies-api
- collection_type: open
  name: Anodot Business Monitoring Access Token Customers API
  slug: open-anodot-customers-api
- collection_type: open
  name: Anodot Business Monitoring Access Token Forecast API
  slug: open-anodot-forecast-api
- collection_type: open
  name: Anodot Business Monitoring Access Token Groups API
  slug: open-anodot-groups-api
- collection_type: open
  name: Anodot Business Monitoring Access Token Users API
  slug: open-anodot-users-api
- collection_type: open
  name: Anodot Business Monitoring API
  slug: open-anodot
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/anodot-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anodot-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/anodot
- group: company
  title: ''
  type: Website
  url: https://www.anodot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anodot.com/
- group: start
  title: ''
  type: Portal
  url: https://cloudcost.anodot.com/
- group: other
  title: ''
  type: Resources
  url: https://www.anodot.com/resources/
- group: company
  title: ''
  type: Blog
  url: https://www.anodot.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anodot.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anodot.com/terms-of-service/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anodot
created: '2026-03-27'
description: Anodot is an AI-powered business monitoring and cloud cost management platform providing autonomous anomaly detection, cost optimization, and real-time alerts for cloud infrastructure, business metrics, and FinOps workflows.
finops:
- name: Anodot Finops
  service_category: API
  slug: anodot-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/anodot.png
layout: provider
modified: '2026-05-19'
name: Anodot
nav: Providers
network: true
overview: 'Anodot publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Access Token API, Alert Actions API, Alerts API, and 5 more. Tagged areas include Artificial Intelligence, Anomaly Detection, Business Monitoring, Cloud Cost Management, and FinOps.


  Anodot''s developer surface includes documentation, developer portal, engineering blog, and 8 more developer resources.'
plans:
- name: Anodot Plans Pricing
  plan_count: 3
  slug: anodot-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Anodot Rate Limits
  slug: anodot-rate-limits
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 9
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 42.2
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 33.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anodot/refs/heads/main/screenshots/anodot-2026-06-20T172012.png
security:
- kind: domain-security
  name: Anodot Domain Security
  slug: anodot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: anodot
tags:
- Artificial Intelligence
- Anomaly Detection
- Business Monitoring
- Cloud Cost Management
- FinOps
- Machine-Learning
- Observability
website: https://www.anodot.com/
---
