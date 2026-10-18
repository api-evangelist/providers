---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
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
  score: 6.5
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Calaxy provides a decentralized social platform API for creators and communities.
  name: Calaxy API
  slug: calaxy-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/calaxy/refs/heads/main/well-known/calaxy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/calaxy-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/calaxy/refs/heads/main/hosts/calaxy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calaxy-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/calaxy/refs/heads/main/vendors/calaxy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/calaxy-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/calaxy/refs/heads/main/security/calaxy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calaxy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://calaxy.com
- group: docs
  title: ''
  type: Documentation
  url: https://calaxy.com/blog
- group: company
  title: ''
  type: Blog
  url: https://calaxy.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://calaxy.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calaxy.com/privacy-policy
coverage:
  checked: '2026-10-06'
  detail: The provider's documentation is HTML without any OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://calaxy.com/blog
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Calaxy is a decentralized social platform that empowers creators, communities, and brands to build and own their own Worlds—standalone social apps. Launched in 2025, it offers tools for audience engagement, content monetization, and cross‑network interoperability, aiming to free the internet one World at a time.
image: https://framerusercontent.com/assets/MQZ7bXN5YT9U4COx2lOJTALokI.png
layout: provider
modified: '2026-10-06'
name: Calaxy
nav: Providers
network: true
overview: 'Calaxy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Decentralized, Social, Platform, CreatorEconomy, and Community.


  Calaxy''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Calaxy Domain Security
  slug: calaxy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: calaxy
tags:
- Decentralized
- Social
- Platform
- CreatorEconomy
- Community
website: https://calaxy.com
---
