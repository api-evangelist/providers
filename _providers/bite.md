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
api_count: 1
apis:
- description: Bite provides AI‑native trade compliance APIs as described on their developer portal.
  name: Bite API
  slug: bite-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bite/refs/heads/main/plans/bite-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bite-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bite/refs/heads/main/changelog/bite-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bite-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bite/refs/heads/main/llms/bite-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bite-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bite/refs/heads/main/hosts/bite-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bite-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bite/refs/heads/main/vendors/bite-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bite-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://bitedata.io/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://bitedata.io/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://bitedata.io/wiki/getting-started
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bite/refs/heads/main/security/bite-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bite-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bitedata.io/
- group: docs
  title: ''
  type: Documentation
  url: https://bitedata.io/resources
- group: company
  title: ''
  type: Blog
  url: https://bitedata.io/blog
- group: operate
  title: ''
  type: Support
  url: https://bitedata.io/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://bitedata.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bitedata.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bitedata.io/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.bitedata.io
coverage:
  checked: '2026-09-28'
  detail: Developer portal requires login via Keycloak, returning only an HTML login page.
  evidence:
  - status: 200
    url: https://app.bitedata.io/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: Bite provides AI‑native trade compliance and HTS classification software that automates tariff lookups, screening, and post‑entry audits. It integrates with ERP, EDI, and supplier systems to monitor, analyze, and manage risk across the global trade lifecycle, offering scalable plans from single checks to enterprise workflows.
image: https://bitedata.io/og-default.jpg
layout: provider
modified: '2026-09-28'
name: Bite
nav: Providers
network: true
overview: 'Bite publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Trade, Compliance, Artificial Intelligence, Software-as-a-Service, and HTS.


  Bite''s developer surface includes changelog, getting-started guide, documentation, engineering blog, support, pricing, and 11 more developer resources.'
plans:
- name: Bite Plans Pricing
  plan_count: 4
  slug: bite-plans-pricing
random_paper: 2
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bite Domain Security
  slug: bite-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bite
tags:
- Trade
- Compliance
- Artificial Intelligence
- Software-as-a-Service
- HTS
website: https://bitedata.io/
---
