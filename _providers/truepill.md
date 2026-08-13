---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Truepill Agentic Access
  operation_count: 15
  slug: truepill-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 5
apis:
- description: Insurance objects, copay requests, and claim adjudication.
  name: Truepill Insurance API
  slug: truepill-insurance-api
- description: Patient records and demographics.
  name: Truepill Patients API
  slug: truepill-patients-api
- description: Prescription details and routing.
  name: Truepill Prescriptions API
  slug: truepill-prescriptions-api
- description: Pharmacy-to-pharmacy prescription transfers.
  name: Truepill Transfers API
  slug: truepill-transfers-api
- description: Asynchronous event retrieval.
  name: Truepill Webhooks API
  slug: truepill-webhooks-api
artifact_total: 12
collections:
- collection_type: open
  name: Truepill (FuzeRx) API
  slug: open-truepill
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/truepill-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/truepill-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/truepill-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/truepill
- group: company
  title: ''
  type: Website
  url: https://www.truepill.com
- group: docs
  title: ''
  type: Documentation
  url: https://rxdocs.fuzehealth.com
- group: commercial
  title: ''
  type: Plans
  url: plans/truepill-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/truepill-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/truepill-finops.yml
created: '2026-06-21'
description: Truepill is a pharmacy and healthcare-infrastructure company providing API-driven prescription fulfillment, pharmacy dispensing, insurance/copay adjudication, telehealth, and at-home diagnostics. Following LetsGetChecked's 2024 acquisition of Truepill, the combined company rebranded as Fuze Health in May 2025, and the developer platform now ships as FuzeRx. The REST API exposes JSON endpoints for patients, prescriptions, transfers, insurance/copay, and webhook events under https://rxapi.fuzehealth.com/v1.
finops:
- name: Truepill Finops
  service_category: Healthcare and Pharmacy
  slug: truepill-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/truepill.png
layout: provider
modified: '2026-06-21'
name: Truepill
nav: Providers
network: true
overview: 'Truepill publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Insurance API, Patients API, Prescriptions API, and 2 more. Tagged areas include Pharmacy, Healthcare, Prescription Fulfillment, Telehealth, and Diagnostics.


  Truepill''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Truepill Plans Pricing
  plan_count: 1
  slug: truepill-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 3
  name: Truepill Rate Limits
  slug: truepill-rate-limits
score:
  band: thin
  composite: 31.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 54.6
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 31.9
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
  name: Truepill Authentication
  slug: truepill-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Truepill Domain Security
  slug: truepill-domain-security
  summary_line: TLSv1.3 · DMARC
slug: truepill
tags:
- Pharmacy
- Healthcare
- Prescription Fulfillment
- Telehealth
- Diagnostics
- Insurance
website: https://www.truepill.com
---
