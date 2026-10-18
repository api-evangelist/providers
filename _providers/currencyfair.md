---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.3
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: CurrencyFair API for international money transfers
  name: CurrencyFair API
  slug: currencyfair-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/currencyfair/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/currencyfair/refs/heads/main/conformance/currencyfair-conformance.yml
  title: ''
  type: Conformance
  url: conformance/currencyfair-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/currencyfair/refs/heads/main/well-known/currencyfair-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/currencyfair-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/currencyfair/refs/heads/main/hosts/currencyfair-hosts.yml
  title: ''
  type: Hosts
  url: hosts/currencyfair-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/currencyfair/refs/heads/main/vendors/currencyfair-vendors.yml
  title: ''
  type: Vendors
  url: vendors/currencyfair-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.currencyfair.com/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.currencyfair.com/en-us/trust/terms-and-conditions
- group: auth
  title: ''
  type: Security
  url: https://blog.currencyfair.com/consumer/tag/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.currencyfair.com/trust/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.currencyfair.com/login/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/currencyfair/refs/heads/main/security/currencyfair-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/currencyfair-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.currencyfair.com
- group: company
  title: ''
  type: Blog
  url: https://blog.currencyfair.com/consumer
- group: operate
  title: ''
  type: Support
  url: https://support.currencyfair.com/s/?language=en_US
- group: docs
  title: ''
  type: Documentation
  url: https://support.currencyfair.com/s/?language=en_US
created: '2026-10-12'
description: Currencyfair is a fintech platform that enables individuals and businesses to send money internationally with lower fees and competitive exchange rates. Founded in 2009, it offers multi‑currency accounts, rate alerts, and integrations such as Xero, facilitating cross‑border payments, tuition fees, property purchases, and payroll. The service operates in over 150 countries, supporting more than 20 currencies, and is authorised as a payment institution.
layout: provider
modified: '2026-10-12'
name: Currencyfair
nav: Providers
network: true
overview: 'Currencyfair is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Money Transfer, International Payments, and Foreign Exchange.


  Currencyfair''s developer surface includes engineering blog, support, documentation, and 12 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 22.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 23.1
    discoverability: 62.5
    operational_transparency: 10.5
  provenance:
    conformance: derived
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Currencyfair Domain Security
  slug: currencyfair-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: currencyfair
tags:
- Company
- Fintech
- Money Transfer
- International Payments
- Foreign Exchange
website: https://www.currencyfair.com
---
