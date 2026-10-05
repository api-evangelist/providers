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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: Bobw developer documentation and API reference
  name: Bobw API
  slug: bobw-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bobw/refs/heads/main/plans/bobw-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bobw-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bobw/refs/heads/main/llms/bobw-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bobw-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bobw/refs/heads/main/well-known/bobw-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bobw-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bobw/refs/heads/main/well-known/bobw-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bobw-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bobw/refs/heads/main/hosts/bobw-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bobw-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bobw/refs/heads/main/vendors/bobw-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bobw-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.bobw.co/en/
- group: company
  title: ''
  type: Newsroom
  url: https://bobw.co/press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bobw/refs/heads/main/security/bobw-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bobw-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bobw.co
- group: docs
  title: ''
  type: Documentation
  url: https://help.bobw.co
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bobw.co/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bobw.co/privacy-policy
- group: company
  title: ''
  type: About
  url: https://bobw.co/about-bob-w
coverage:
  checked: '2026-10-02'
  detail: Documentation at https://help.bobw.co/en/ is rendered via JavaScript and provides no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://help.bobw.co/en/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-02'
description: Bob W is a hospitality brand offering short‑stay, fully equipped apartments across Europe. It combines hotel‑level service with local design, sustainable practices and tech‑enabled check‑in. The company offsets all guest emissions, sources local furniture, and aims for net‑zero hospitality by 2050. With over 60 properties in 21+ cities, Bob W delivers flexible stays for business and leisure travelers, emphasizing sustainability and community integration.
layout: provider
modified: '2026-10-02'
name: Bobw
nav: Providers
network: true
overview: 'Bobw publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Hospitality, Accommodation, Sustainability, Europe, and Short-Stay.


  Bobw''s developer surface includes support, documentation, and 12 more developer resources.'
plans:
- name: Bobw Plans Pricing
  plan_count: 1
  slug: bobw-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 38.0
    catalog_earned_first_party: 8.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 62.5
    operational_transparency: 0.0
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
  name: Bobw Domain Security
  slug: bobw-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bobw
tags:
- Hospitality
- Accommodation
- Sustainability
- Europe
- Short-Stay
website: https://bobw.co
---
