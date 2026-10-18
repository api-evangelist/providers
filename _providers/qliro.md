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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/qliro/refs/heads/main/llms/qliro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/qliro-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qliro/refs/heads/main/well-known/qliro-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/qliro-status-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qliro/refs/heads/main/well-known/qliro-se-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/qliro-se-support-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/qliro/refs/heads/main/well-known/qliro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/qliro-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliro/refs/heads/main/hosts/qliro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qliro-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qliro/refs/heads/main/vendors/qliro-vendors.yml
  title: ''
  type: Vendors
  url: vendors/qliro-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qliro.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://qliro.com/composable-payouts/price-list-for-currency-conversion-and-currencies
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Qliro
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.qliro.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qliro/refs/heads/main/security/qliro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qliro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://qliro.com/
- group: docs
  title: ''
  type: Documentation
  url: https://qliro.com/for-merchants
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://qliro.com/hubfs/New%20website%20-%20Privacy%20policy/Privacy%20Policy%20-%20Qliro.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://qliro.com/sv/for-shoppare-villkor
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://qliro.com/mcp
  - status: 403
    url: https://assets.qliro.com/mcp
  - status: 200
    url: https://qliro.com/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: Qliro provides flexible payment solutions for online and in‑store shoppers and merchants across Scandinavia. It offers “Buy now, pay later”, installment plans, and a consumer‑focused app, supporting multiple languages and currencies. The platform emphasizes secure, fast checkout experiences and integrates with e‑commerce merchants to boost conversion.
image: https://qliro.com/hubfs/Feature_B2CHomepage.png
layout: provider
modified: '2026-10-15'
name: Qliro
nav: Providers
network: true
overview: 'Qliro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Fintech, BuyNowPayLater, and E-Commerce.


  Qliro''s developer surface includes pricing, documentation, and 13 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 55.4
    operational_transparency: 21.1
  provenance:
    mcp: derived
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
  name: Qliro Domain Security
  slug: qliro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qliro
tags:
- Company
- Payments
- Fintech
- BuyNowPayLater
- E-Commerce
website: https://qliro.com/
---
