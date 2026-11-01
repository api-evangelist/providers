---
agent_readiness:
  band: agent-aware
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
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/dynadot/llms/dynadot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dynadot-llms.txt
- group: other
  href: https://artifacts.apis.io/dynadot/hosts/dynadot-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dynadot-hosts.yml
- group: other
  href: https://artifacts.apis.io/dynadot/vendors/dynadot-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dynadot-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.dynadot.com/support
- group: auth
  title: ''
  type: Security
  url: https://www.dynadot.com/domain/security
- group: company
  title: ''
  type: Blog
  url: https://www.dynadot.com/blog
- group: auth
  href: https://artifacts.apis.io/dynadot/security/dynadot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dynadot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dynadot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.dynadot.com/domain/api-commands
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dynadot.com/help/pricing-payment
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dynadot.com/terms-of-use
coverage:
  checked: '2026-10-27'
  detail: The API documentation page is a JavaScript‑rendered SPA with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://www.dynadot.com/domain/api-commands
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Dynadot is a domain registrar and marketplace offering domain registration, transfer, aftermarket auctions, bulk search, and related services. It provides tools for domain management, DNS configuration, SSL certificates, and website building, serving over a million customers worldwide.
layout: provider
modified: '2026-10-27'
name: Dynadot
nav: Providers
network: true
overview: 'Dynadot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Domain Registrar, Marketplace, DNS Management, and SSL.


  Dynadot''s developer surface includes support, engineering blog, documentation, pricing, and 7 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 44.6
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dynadot Domain Security
  slug: dynadot-domain-security
  summary_line: TLSv1.2 · DMARC
slug: dynadot
tags:
- Company
- Domain Registrar
- Marketplace
- DNS Management
- SSL
website: https://dynadot.com/
---
