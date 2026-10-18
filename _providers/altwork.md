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
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Altwork API providing GraphQL endpoint and MCP services.
  name: Altwork API
  slug: altwork-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/altwork/refs/heads/main/llms/altwork-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/altwork-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/altwork/refs/heads/main/well-known/altwork-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/altwork-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/altwork/refs/heads/main/hosts/altwork-hosts.yml
  title: ''
  type: Hosts
  url: hosts/altwork-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/altwork/refs/heads/main/vendors/altwork-vendors.yml
  title: ''
  type: Vendors
  url: vendors/altwork-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://altwork.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://altwork.com/policies/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://altwork.com/pages/press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/altwork/refs/heads/main/security/altwork-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/altwork-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://altwork.com
created: '2026-09-24'
description: Altwork designs and sells high-end ergonomic workstations and accessories aimed at bio‑performance. Their flagship Signature Station integrates multiple monitors, laptop mounts, and accessories to promote comfort and productivity for professionals. The company emphasizes engineering precision, offering customizable setups and support from in‑house experts. Altwork’s website showcases product lines, technology insights, a blog, and comprehensive support resources.
image: http://altwork.com/cdn/shop/files/AW_Success_In_Zero_Gravity_X2_ce9434a2-8fa4-40d5-bbb0-d572274f7fc9.png?v=1782503280&width=2048
layout: provider
modified: '2026-09-24'
name: Altwork
nav: Providers
network: true
overview: Altwork is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ergonomics, Workstations, BioPerformance, and E-Commerce.
random_paper: 2
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 11.2
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 75.0
    operational_transparency: 0.0
  previous_composite: 0.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Altwork Domain Security
  slug: altwork-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: altwork
tags:
- Company
- Ergonomics
- Workstations
- BioPerformance
- E-Commerce
website: https://altwork.com
---
