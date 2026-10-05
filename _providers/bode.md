---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bode/refs/heads/main/llms/bode-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bode-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bode/refs/heads/main/well-known/bode-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bode-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bode/refs/heads/main/hosts/bode-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bode-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bode/refs/heads/main/vendors/bode-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bode-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bode.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bode.com/policies/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bode/refs/heads/main/security/bode-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bode-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bode.com
coverage:
  checked: '2026-10-02'
  detail: GraphQL endpoint returned a schema unrelated to Bode, indicating no owned machine‑readable contract.
  evidence:
  - status: 200
    url: https://bode.com/api/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-02'
description: Bode is a fashion and lifestyle brand offering clothing, accessories, and home goods. The company operates an e‑commerce site at https://bode.com, but no public API documentation or endpoints were discovered during profiling. This entry remains a stub pending any future API availability.
image: http://bode.com/cdn/shop/files/Bode_Logo_1200x628_01.jpg?v=1674142983
layout: provider
modified: '2026-10-02'
name: Bode
nav: Providers
network: true
overview: Bode is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fashion, E-Commerce, Clothing, and Accessories.
random_paper: 14
score:
  band: minimal
  composite: 9.5
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
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bode Domain Security
  slug: bode-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bode
tags:
- Company
- Fashion
- E-Commerce
- Clothing
- Accessories
- Home Goods
website: https://bode.com
---
