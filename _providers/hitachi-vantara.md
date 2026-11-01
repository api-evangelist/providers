---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: Security
  url: https://www.hitachivantara.com/en-us/security#section-vulnerability-disclosure-policy
- group: agent
  href: https://artifacts.apis.io/hitachi-vantara/llms/hitachi-vantara-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hitachi-vantara-llms.txt
- group: auth
  href: https://artifacts.apis.io/hitachi-vantara/well-known/hitachi-vantara-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hitachi-vantara-security.txt
- group: auth
  href: https://artifacts.apis.io/hitachi-vantara/well-known/hitachi-vantara-hitachivantara-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hitachi-vantara-hitachivantara-security.txt
- group: agent
  href: https://artifacts.apis.io/hitachi-vantara/well-known/hitachi-vantara-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hitachi-vantara-well-known.yml
- group: other
  href: https://artifacts.apis.io/hitachi-vantara/hosts/hitachi-vantara-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hitachi-vantara-hosts.yml
- group: other
  href: https://artifacts.apis.io/hitachi-vantara/vendors/hitachi-vantara-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hitachi-vantara-vendors.yml
- group: auth
  href: https://artifacts.apis.io/hitachi-vantara/security/hitachi-vantara-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hitachi-vantara-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/hitachi-vantara/security/hitachi-vantara-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hitachi-vantara-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hitachivantara.com/en-us/home
- group: docs
  title: ''
  type: Documentation
  url: https://www.hitachivantara.com/en-us/home
- group: company
  title: ''
  type: Blog
  url: https://www.hitachivantara.com/en-us/blog
created: '2026-10-28'
description: Hitachi Vantara provides data infrastructure, storage platforms, hybrid cloud solutions, and AI‑ready services. It helps enterprises manage, protect, and govern data across on‑premises and cloud environments, offering integrated products such as block, file, and object storage, data management tools, and infrastructure‑as‑a‑service.
image: https://s7d9.scene7.com/is/image/hitachivantara/Default-OG:ogimage?fmt=webp
layout: provider
modified: '2026-10-28'
name: Hitachi Content Platform
nav: Providers
network: true
overview: 'Hitachi Content Platform is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Data Infrastructure, Storage, Hybrid Cloud, AI Services, and Enterprise Solutions.


  Hitachi Content Platform''s developer surface includes documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Hitachi Vantara Plans Pricing
  plan_count: 0
  slug: hitachi-vantara-plans-pricing
random_paper: 12
scopes:
- name: Hitachi Vantara Scopes
  scope_count: 0
  slug: hitachi-vantara-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Hitachi Vantara Authentication
  slug: hitachi-vantara-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Hitachi Vantara Domain Security
  slug: hitachi-vantara-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hitachi Vantara Vulnerability Disclosure
  slug: hitachi-vantara-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: hitachi-vantara
tags:
- Data Infrastructure
- Storage
- Hybrid Cloud
- AI Services
- Enterprise Solutions
website: https://www.hitachivantara.com/en-us/home
---
