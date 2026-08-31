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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Interpol Agentic Access
  operation_count: 9
  slug: interpol-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- description: The Notices API from Interpol — 9 operation(s) for notices.
  name: Interpol Notices API
  slug: interpol-notices-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Interpol Notices API
  slug: open-interpol-notices-api
- collection_type: open
  name: Interpol Notices API
  slug: open-interpol
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/interpol-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/interpol-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/interpol-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/interpol
- group: company
  title: ''
  type: Website
  url: https://www.interpol.int/
- group: other
  title: ''
  type: Source
  url: https://github.com/bundesAPI/interpol-api
created: '2024-12-03'
description: INTERPOL (International Criminal Police Organization) is an inter-governmental organization with 196 member countries that helps police worldwide work together to make the world a safer place. INTERPOL exposes a public Notices web service that returns Red, Yellow, and UN Notices data. An OpenAPI description of that service is published by the bundesAPI community and mirrored in this repository.
finops:
- name: Interpol Finops
  service_category: API
  slug: interpol-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/interpol.png
layout: provider
modified: '2026-05-19'
name: Interpol
nav: Providers
network: true
overview: 'Interpol publishes 1 API on the [APIs.io](https://apis.io/) network: Notices API. Tagged areas include Federal-Government, International, Law Enforcement, Notices, and Police.


  The Interpol catalog on APIs.io includes 1 Spectral governance ruleset.'
plans:
- name: Interpol Plans Pricing
  plan_count: 3
  slug: interpol-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Interpol Rate Limits
  slug: interpol-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Interpol API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: interpol-rules
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 10
    catalog_gap: 60.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 43.5
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 19.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/interpol/refs/heads/main/screenshots/interpol-2026-06-20T183505.png
security:
- kind: domain-security
  name: Interpol Domain Security
  slug: interpol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: interpol
tags:
- Federal-Government
- International
- Law Enforcement
- Notices
- Police
website: https://www.interpol.int/
---
