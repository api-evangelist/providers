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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clever-real-estate/refs/heads/main/hosts/clever-real-estate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clever-real-estate-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cleverrealtors.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cleverrealtors.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://cleverrealtors.com/category/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clever-real-estate/refs/heads/main/security/clever-real-estate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clever-real-estate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cleverrealtors.com
coverage:
  checked: '2026-10-09'
  detail: The provider's website does not offer a developer program or public API documentation.
  evidence:
  - status: 200
    url: https://cleverrealtors.com
  reason: no-developer-program
  state: none
created: '2026-10-08'
description: Clever Real Estate operates a real‑estate brokerage platform based in Dallas, Texas, offering a low‑commission model for buying, selling, and renting properties. The site provides tools for agents, listings, community information, and a streamlined process for clients, emphasizing customer service and transparency. It includes a public API for accessing property data, agent details, and transaction services, supporting integration with third‑party real‑estate applications.
image: https://cleverrealtors.com/wp-content/uploads/2026/07/output1-11.webp
layout: provider
modified: '2026-10-08'
name: Clever Real Estate
nav: Providers
network: true
overview: 'Clever Real Estate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Brokerage, Dallas, and Low Commission.


  Clever Real Estate''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 13.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clever Real Estate Domain Security
  slug: clever-real-estate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clever-real-estate
tags:
- Real Estate
- Brokerage
- Dallas
- Low Commission
website: https://cleverrealtors.com
---
