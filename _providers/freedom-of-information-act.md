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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Freedom Of Information Act Agentic Access
  operation_count: 5
  slug: freedom-of-information-act-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 3
apis:
- description: Agencies and their FOIA components.
  name: Freedom of Information Act Agency Components API
  slug: freedom-of-information-act-agency-components-api
- description: Portal-to-agency request submission API (implemented by participating agencies at foia-api.agency.gov).
  name: Freedom of Information Act Agency Submission API
  slug: freedom-of-information-act-agency-submission-api
- description: Agency annual FOIA reports as XML.
  name: Freedom of Information Act Annual Reports API
  slug: freedom-of-information-act-annual-reports-api
artifact_total: 10
collections:
- collection_type: open
  name: Freedom of Information Act (FOIA) API
  slug: open-freedom-of-information-act
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/freedom-of-information-act-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freedom-of-information-act-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/freedom-of-information-act-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.foia.gov/developer/
- group: company
  title: ''
  type: Website
  url: https://www.foia.gov/
created: '2024-01-01'
description: The Freedom of Information Act (FOIA) API provides access to FOIA request data and related information from federal agencies.
finops:
- name: Freedom Of Information Act Finops
  service_category: API
  slug: freedom-of-information-act-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/freedom-of-information-act.png
layout: provider
modified: '2026-05-19'
name: Freedom of Information Act
nav: Providers
network: true
overview: 'Freedom of Information Act publishes 3 APIs on the [APIs.io](https://apis.io/) network: Agency Components API, Agency Submission API, and Annual Reports API. Tagged areas include Federal Government, FOIA, and Transparency.


  Freedom of Information Act''s developer surface includes authentication, developer portal, and 3 more developer resources.'
plans:
- name: Freedom Of Information Act Plans Pricing
  plan_count: 3
  slug: freedom-of-information-act-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 5
  name: Freedom Of Information Act Rate Limits
  slug: freedom-of-information-act-rate-limits
score:
  band: emerging
  composite: 27.5
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 59.2
    developer_ergonomics: 19.6
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 27.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freedom-of-information-act/refs/heads/main/screenshots/freedom-of-information-act-2026-06-20T181524.png
security:
- kind: authentication
  name: Freedom Of Information Act Authentication
  slug: freedom-of-information-act-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Freedom Of Information Act Domain Security
  slug: freedom-of-information-act-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: freedom-of-information-act
tags:
- Federal Government
- FOIA
- Transparency
website: https://www.foia.gov/
---
