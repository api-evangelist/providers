---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/halopsa/hosts/halopsa-hosts.yml
  title: ''
  type: Hosts
  url: hosts/halopsa-hosts.yml
- group: other
  href: https://artifacts.apis.io/halopsa/vendors/halopsa-vendors.yml
  title: ''
  type: Vendors
  url: vendors/halopsa-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usehalo.com/terms-conditions
- group: auth
  title: ''
  type: Security
  url: https://www.usehalo.com/security
- group: operate
  title: ''
  type: Roadmap
  url: https://www.usehalo.com/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usehalo.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.usehalo.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.usehalo.com/news/halo-orbit-2023
- group: docs
  title: ''
  type: Documentation
  url: https://www.usehalo.com/guides/
- group: docs
  title: ''
  type: APIReference
  url: https://www.usehalo.com/swagger
- group: start
  title: ''
  type: GettingStarted
  url: https://www.usehalo.com/onboarding-process
- group: auth
  href: https://artifacts.apis.io/halopsa/security/halopsa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/halopsa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usehalo.com/
coverage:
  checked: '2026-10-27'
  detail: No public developer documentation or API specifications were found on the provider's website.
  evidence:
  - status: 200
    url: https://www.usehalo.com/
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: Halo (formerly HaloPSA) provides a unified workflow automation platform for enterprises, offering modules for IT Service Management (ITSM), Customer Service Management (CSM), Enterprise Service Management (ESM), CRM, and Professional Services Automation (PSA). The solution integrates AI-driven automation, extensive third‑party integrations, and a low‑code portal for building custom workflows, targeting mid‑size to large organizations across multiple industries.
layout: provider
modified: '2026-10-26'
name: HaloPSA
nav: Providers
network: true
overview: 'HaloPSA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Workflow Automation, ITSM, Customer Service Management, and Enterprise Service Management.


  HaloPSA''s developer surface includes pricing, documentation, API reference, getting-started guide, and 9 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 45.5
    operational_transparency: 7.9
  previous_composite: 18.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/halopsa/halopsa-2026-11-03T133334.png
security:
- kind: domain-security
  name: Halopsa Domain Security
  slug: halopsa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: halopsa
tags:
- Company
- Workflow Automation
- ITSM
- Customer Service Management
- Enterprise Service Management
website: https://usehalo.com/
---
