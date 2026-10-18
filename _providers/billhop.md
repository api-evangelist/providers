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
api_count: 1
apis:
- description: API for Billhop platform
  name: Billhop API
  slug: billhop-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/billhop/refs/heads/main/vendors/billhop-vendors.yml
  title: ''
  type: Vendors
  url: vendors/billhop-vendors.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/billhop/refs/heads/main/llms/billhop-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/billhop-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/billhop/refs/heads/main/hosts/billhop-hosts.yml
  title: ''
  type: Hosts
  url: hosts/billhop-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.billhop.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Billhop
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billhop/refs/heads/main/security/billhop-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/billhop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://billhop.com/
- group: operate
  title: ''
  type: Support
  url: https://billhop.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://billhop.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://billhop.com/working-capital-solution
- group: start
  title: ''
  type: SignUp
  url: https://billhop.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://billhop.com/legal-information
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://billhop.com/legal-information/privacy-policy
coverage:
  checked: '2026-10-15'
  detail: Docs site renders via JavaScript and provides no machine‑readable spec.
  evidence:
  - status: 200
    url: https://docs.billhop.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-15'
description: Billhop provides a platform to supercharge corporate card programs, enabling businesses to pay suppliers with credit cards, extend payment terms, and improve cash flow. The solution offers working capital optimization, tail‑spend management, international payments, and automated reconciliation, all SOC 2 Type II compliant. Billhop was recently acquired by Ramp, expanding its reach in the European market.
image: https://billhop.com/api/og?slug=home
layout: provider
modified: '2026-10-15'
name: Billhop
nav: Providers
network: true
overview: 'Billhop is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Payments, Working Capital, Supplier Management, and Corporate Cards.


  Billhop''s developer surface includes documentation, support, engineering blog, pricing, signup flow, and 8 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 64.3
    operational_transparency: 5.3
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
  name: Billhop Domain Security
  slug: billhop-domain-security
  summary_line: TLSv1.3 · DMARC
slug: billhop
tags:
- Fintech
- Payments
- Working Capital
- Supplier Management
- Corporate Cards
website: https://billhop.com/
---
