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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/chefhero/refs/heads/main/plans/chefhero-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chefhero-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chefhero/refs/heads/main/hosts/chefhero-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chefhero-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chefhero/refs/heads/main/vendors/chefhero-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chefhero-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.notch.financial/company/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.notch.financial/company/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.notch.financial/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.notch.financial/resources/news
- group: docs
  title: ''
  type: Documentation
  url: https://www.notch.financial/resources/guides
- group: company
  title: ''
  type: Blog
  url: https://www.notch.financial/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chefhero/refs/heads/main/security/chefhero-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chefhero-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.notch.financial
created: '2026-10-08'
description: Chefhero, now operating as Notch, provides a cloud‑based platform that automates accounts receivable, invoice management and payment processing for food‑service businesses and other SMBs. The Toronto‑based company rebranded in 2021 to focus on digitizing the wholesale food‑service supply chain, offering tools for customers, distributors and finance teams to streamline billing, collections and reconciliation.
layout: provider
modified: '2026-10-08'
name: Chefhero
nav: Providers
network: true
overview: 'Chefhero is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Food Tech, and Software-as-a-Service.


  Chefhero''s developer surface includes pricing, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Chefhero Plans Pricing
  plan_count: 2
  slug: chefhero-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 16.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 33.0
    catalog_earned_first_party: 8.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 12.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chefhero Domain Security
  slug: chefhero-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: chefhero
tags:
- Company
- Fintech
- Payments
- Food Tech
- Software-as-a-Service
- B2B
website: https://www.notch.financial
---
