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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://vali.health/security
- group: agent
  href: https://artifacts.apis.io/vali/llms/vali-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vali-llms.txt
- group: other
  href: https://artifacts.apis.io/vali/hosts/vali-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vali-hosts.yml
- group: other
  href: https://artifacts.apis.io/vali/vendors/vali-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vali-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://vali.health/security
- group: auth
  href: https://artifacts.apis.io/vali/security/vali-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/vali-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/vali/security/vali-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vali-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vali.health
- group: docs
  title: ''
  type: Documentation
  url: https://vali.health/about-us
- group: commercial
  title: ''
  type: Pricing
  url: https://vali.health/pricing
- group: company
  title: ''
  type: Blog
  url: https://vali.health/blog/stop-losing-revenue-unstaffed-home-care-shifts
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vali.health/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vali.health/privacy-policy
created: '2026-10-25'
description: Vali provides an AI‑powered workforce platform for home‑care agencies, automating caregiver scheduling, shift fulfillment, and operational oversight. Founded after personal experiences with gaps in in‑home care, Vali’s mission is to strengthen the operational backbone of agencies, ensuring reliable care delivery and reducing caregiver turnover. The platform combines intelligent matching, real‑time coordination, and human oversight to improve efficiency and patient outcomes across the US and Canada.
image: https://cdn.prod.website-files.com/69bc0e97791e8fa883cb21ef/69d9dd7e67dfb880dfa04b95_Open%20graph.png
layout: provider
modified: '2026-10-25'
name: Vali
nav: Providers
network: true
overview: 'Vali is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, HomeCare, Healthcare, and Workforce.


  Vali''s developer surface includes documentation, pricing, engineering blog, and 10 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Vali Domain Security
  slug: vali-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Vali Trust Center
  slug: vali-trust-center
  summary_line: SOC 2, HIPAA
slug: vali
tags:
- Company
- AI
- HomeCare
- Healthcare
- Workforce
website: https://vali.health
---
