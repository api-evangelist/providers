---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Simple CRM for B2B Sales Teams
  name: Anvil CRM API
  slug: anvil-crm-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/anvilcrm-com/llms/anvilcrm-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anvilcrm-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/anvilcrm-com/well-known/anvilcrm-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anvilcrm-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/anvilcrm-com/hosts/anvilcrm-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anvilcrm-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/anvilcrm-com/vendors/anvilcrm-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anvilcrm-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://anvilcrm.com/security
- group: auth
  href: https://artifacts.apis.io/anvilcrm-com/security/anvilcrm-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anvilcrm-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anvilcrm.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anvilcrm.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anvilcrm.com/privacy
coverage:
  checked: '2026-11-01'
  detail: API documentation pages redirect to a login page, requiring authentication to access.
  evidence:
  - status: 307
    url: https://app.anvilcrm.com/docs
  reason: auth-required
  state: gated
created: '2026-11-01'
description: Anvil CRM provides a simple, affordable CRM solution for small and medium B2B sales teams, offering deal management, pipeline tracking, contact organization, and MCP-compatible AI assistant integration. It helps teams streamline sales processes, improve customer relationships, and boost productivity with an intuitive interface and robust API access.
image: https://anvilcrm.com/images/anvil-logo/Anvil_Logo-04.png
layout: provider
modified: '2026-11-01'
name: Anvil CRM
nav: Providers
network: true
overview: Anvil CRM is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CRM, B2B, Sales, MCP, and Artificial Intelligence.
plans:
- name: Anvilcrm Com Plans Pricing
  plan_count: 0
  slug: anvilcrm-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Anvilcrm Com Rate Limits
  slug: anvilcrm-com-rate-limits
scopes:
- name: Anvilcrm Com Scopes
  scope_count: 0
  slug: anvilcrm-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 5.3
  previous_composite: 13.1
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Anvilcrm Com Authentication
  slug: anvilcrm-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Anvilcrm Com Domain Security
  slug: anvilcrm-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: anvilcrm-com
tags:
- CRM
- B2B
- Sales
- MCP
- Artificial Intelligence
- Software-as-a-Service
website: https://anvilcrm.com/
---
