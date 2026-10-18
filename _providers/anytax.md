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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/anytax/refs/heads/main/well-known/anytax-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anytax-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anytax/refs/heads/main/hosts/anytax-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anytax-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anytax/refs/heads/main/vendors/anytax-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anytax-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anytax/refs/heads/main/security/anytax-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anytax-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anytax.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.anytax.io/
- group: company
  title: ''
  type: About
  url: https://www.anytax.io/about
- group: other
  title: ''
  type: Product
  url: https://www.anytax.io/product
- group: operate
  title: ''
  type: FAQ
  url: https://www.anytax.io/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anytax.io/legal-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anytax.io/legal-data
coverage:
  checked: '2026-10-15'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was discovered at the API host.
  evidence:
  - status: 404
    url: https://api.anytax.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: AnyTax provides API‑driven tax solutions, offering tax filing, estimation, and planning services through a white‑label integration. Their platform enables banks, financial advisors, and fintechs to embed tax calculations via REST APIs or SDKs, supporting individuals, freelancers, and small businesses. The service focuses on seamless data connectivity, compliance, and customizable tax products, aiming to make tax processes accessible and automated for any financial platform.
layout: provider
modified: '2026-10-15'
name: AnyTax
nav: Providers
network: true
overview: 'AnyTax is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Tax, and Integration.


  AnyTax''s developer surface includes documentation, FAQ, and 9 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 35.7
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Anytax Domain Security
  slug: anytax-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: anytax
tags:
- Company
- Fintech
- Tax
- Integration
website: https://anytax.io/
---
