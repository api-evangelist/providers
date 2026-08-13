---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Zus Agentic Access
  operation_count: 15
  slug: zus-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 5
apis:
- description: OAuth2 token issuance and exchange.
  name: Zus Health Auth API
  slug: zus-auth-api
- description: DocumentReference and Binary resources.
  name: Zus Health Documents API
  slug: zus-documents-api
- description: General FHIR R4 resources.
  name: Zus Health FHIR API
  slug: zus-fhir-api
- description: FHIR R4 Patient resources.
  name: Zus Health Patient API
  slug: zus-patient-api
- description: Jobs that retrieve external data into the Zus Aggregated Profile.
  name: Zus Health Patient History API
  slug: zus-patient-history-api
artifact_total: 12
collections:
- collection_type: open
  name: Zus Health API
  slug: open-zus
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zus-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zus-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zus-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zushealth
- group: company
  title: ''
  type: Website
  url: https://zushealth.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zushealth.com
- group: commercial
  title: ''
  type: Plans
  url: plans/zus-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zus-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zus-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://zushealth.com/feed/
created: '2026-06-21'
description: Zus Health is a shared health-data platform that aggregates a patient's clinical history from external networks into the Zus Aggregated Profile (ZAP). It exposes a FHIR R4 (v4.0.1) REST API secured with OAuth2 Bearer tokens, Patient History APIs, document ingestion and retrieval, Zushooks webhooks, a GraphQL FHIR Query Service, and embeddable open-source React components.
finops:
- name: Zus Finops
  service_category: Healthcare
  slug: zus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zus.png
layout: provider
modified: '2026-06-21'
name: Zus Health
nav: Providers
network: true
overview: 'Zus Health publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Documents API, FHIR API, and 2 more. Tagged areas include Health, FHIR, Interoperability, Patient Data, and Healthcare.


  Zus Health''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Zus Plans Pricing
  plan_count: 2
  slug: zus-plans-pricing
random_paper: 114
rate_limits:
- limit_count: 4
  name: Zus Rate Limits
  slug: zus-rate-limits
score:
  band: thin
  composite: 32.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 56.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 32.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Zus Authentication
  slug: zus-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zus Domain Security
  slug: zus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zus
tags:
- Health
- FHIR
- Interoperability
- Patient Data
- Healthcare
website: https://zushealth.com
---
