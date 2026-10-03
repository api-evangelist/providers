---
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/billee/refs/heads/main/llms/billee-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/billee-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/billee/refs/heads/main/hosts/billee-hosts.yml
  title: ''
  type: Hosts
  url: hosts/billee-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/billee/refs/heads/main/vendors/billee-vendors.yml
  title: ''
  type: Vendors
  url: vendors/billee-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.billee.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.billee.ai/privacy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billee/refs/heads/main/security/billee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/billee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://billee.ai/
coverage:
  checked: '2026-09-28'
  detail: OpenAPI spec endpoints on api.billee.ai return 404, and no documentation host provides a machine‑readable contract.
  evidence:
  - status: 404
    url: https://api.billee.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Billee is a full-service utility management platform for multifamily owners and operators. It combines white‑glove service with AI‑powered automation to handle billing, vacant cost recovery, vendor management, meter monitoring, ESG reporting, and more, delivering accurate utility billing, cost reduction, and operational efficiency across property portfolios.
image: https://cdn.prod.website-files.com/69439062b357b63debfb5fcf/6965e9da07c5e6dd797871c1_Billee-OG_2026.jpg
layout: provider
modified: '2026-09-28'
name: Billee
nav: Providers
network: true
overview: Billee is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Utility, Billing, Artificial Intelligence, and Multifamily.
random_paper: 5
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 10.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Billee Domain Security
  slug: billee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: billee
tags:
- Company
- Utility
- Billing
- Artificial Intelligence
- Multifamily
website: https://billee.ai/
---
