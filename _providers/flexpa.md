---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Flexpa Agentic Access
  operation_count: 15
  slug: flexpa-agentic-access
  summary_line: 15 operations · 2 acting
api_count: 4
apis:
- description: The Access Tokens API from Flexpa — 1 operation(s) for access tokens.
  name: Flexpa Access Tokens API
  slug: flexpa-access-tokens-api
- description: The Claims Data API from Flexpa — 5 operation(s) for claims data.
  name: Flexpa Claims Data API
  slug: flexpa-claims-data-api
- description: The FHIR API from Flexpa — 8 operation(s) for fhir.
  name: Flexpa FHIR API
  slug: flexpa-fhir-api
- description: The Link API from Flexpa — 1 operation(s) for link.
  name: Flexpa Link API
  slug: flexpa-link-api
artifact_total: 11
collections:
- collection_type: open
  name: Flexpa API
  slug: open-flexpa
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flexpa-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flexpa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flexpa-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flexpa
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flexpa
- group: company
  title: ''
  type: Website
  url: https://www.flexpa.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.flexpa.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/flexpa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flexpa-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/flexpa-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.flexpa.com/blog
created: '2026-06-21'
description: Flexpa is a patient-access platform that lets applications connect a patient to their health insurance plan and retrieve claims and clinical data as normalized FHIR R4 resources. Patients authorize access through Flexpa Link / OAuth 2.0 PKCE, and applications read ExplanationOfBenefit, Coverage, Patient, and other resources from a single FHIR API at https://api.flexpa.com.
finops:
- name: Flexpa Finops
  service_category: Healthcare
  slug: flexpa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flexpa.png
layout: provider
modified: '2026-06-21'
name: Flexpa
nav: Providers
network: true
overview: 'Flexpa publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Access Tokens API, Claims Data API, FHIR API, and 1 more. Tagged areas include Healthcare, FHIR, Patient Access, Claims Data, and Health Insurance.


  Flexpa''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Flexpa Plans Pricing
  plan_count: 5
  slug: flexpa-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 4
  name: Flexpa Rate Limits
  slug: flexpa-rate-limits
score:
  band: thin
  composite: 34.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/screenshots/flexpa-2026-07-25T214752.png
security:
- kind: authentication
  name: Flexpa Authentication
  slug: flexpa-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Flexpa Domain Security
  slug: flexpa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flexpa
tags:
- Healthcare
- FHIR
- Patient Access
- Claims Data
- Health Insurance
website: https://www.flexpa.com
---
