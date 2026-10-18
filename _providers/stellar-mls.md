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
api_count: 1
apis:
- description: Stellar MLS listing data delivery program (API, IDX and custom options). The Web API is not served from a Stellar MLS host; it is distributed through MLS Grid and Bridge API (distribution vendors, not
  name: Stellar MLS Data Delivery
  slug: stellar-mls-data-delivery
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/stellar-mls/refs/heads/main/llms/stellar-mls-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stellar-mls-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/stellar-mls/refs/heads/main/well-known/stellar-mls-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/stellar-mls-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/stellar-mls/refs/heads/main/hosts/stellar-mls-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stellar-mls-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/stellar-mls/refs/heads/main/vendors/stellar-mls-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stellar-mls-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stellarmls.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.stellarmls.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stellarmls.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.stellarmls.com/news
- group: other
  title: ''
  type: Leadership
  url: https://www.stellarmls.com/about/team
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.stellarmls.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/StellarMLS
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stellar-mls/refs/heads/main/security/stellar-mls-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stellar-mls-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stellarmls.com
- group: docs
  title: ''
  type: Documentation
  url: https://doc.stellarmls.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://www.stellarmls.com/mcp
  - status: 403
    url: https://bod.stellarmls.com/mcp
  - status: 200
    url: https://www.stellarmls.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: 'Stellar MLS is a Florida-based multiple listing service. It does not host its own public developer API: listing data is delivered to brokers and vendors through the RESO Web API services of two distribution vendors, MLS Grid and Bridge API, under a three-party data license agreement, plus IDX and custom (non-IDX) feed options.'
image: https://irp.cdn-website.com/3d0f9886/dms3rep/multi/opt/Stellar+MLS+Open+Graph-1920w.png
layout: provider
modified: '2026-10-14'
name: Stellar MLS
nav: Providers
network: true
overview: 'Stellar MLS is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, MLS, RESO, and IDX.


  Stellar MLS''s developer surface includes support, documentation, and 12 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 67.9
    operational_transparency: 5.3
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
  name: Stellar Mls Domain Security
  slug: stellar-mls-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stellar-mls
tags:
- Company
- Real Estate
- MLS
- RESO
- IDX
website: https://www.stellarmls.com
---
