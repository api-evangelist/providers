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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The Merit Systems Protection Board protects federal merit systems and safeguards the rights of federal employees against prohibited personnel practices under 5 U.S.C. 2301(b).
  name: Merit Systems Protection Board
  slug: merit-systems-protection-board
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/merit-systems-protection-board-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/merit-systems-protection-board-domain-security.yml
created: '2024-12-03'
description: The Merit Systems Protection Board (MSPB) is an independent quasi-judicial agency that protects federal merit systems against partisan political and other prohibited personnel practices. It safeguards the rights of federal employees and adjudicates employee appeals.
finops:
- name: Merit Systems Protection Board Finops
  service_category: API
  slug: merit-systems-protection-board-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/merit-systems-protection-board.png
layout: provider
modified: '2026-04-28'
name: Merit Systems Protection Board
nav: Providers
network: true
overview: Merit Systems Protection Board publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Civil Service, Employment, Federal-Government, and Government.
plans:
- name: Merit Systems Protection Board Plans Pricing
  plan_count: 3
  slug: merit-systems-protection-board-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Merit Systems Protection Board Rate Limits
  slug: merit-systems-protection-board-rate-limits
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 5
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 9.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/merit-systems-protection-board/refs/heads/main/screenshots/merit-systems-protection-board-2026-06-20T185222.png
security:
- kind: domain-security
  name: Merit Systems Protection Board Domain Security
  slug: merit-systems-protection-board-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Merit Systems Protection Board Vulnerability Disclosure
  slug: merit-systems-protection-board-vulnerability-disclosure
  summary_line: disclosure policy published
slug: merit-systems-protection-board
tags:
- Civil Service
- Employment
- Federal-Government
- Government
---
