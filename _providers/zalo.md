---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-10-17'
api_count: 3
apis:
- description: Send and manage messages, followers and content for a Zalo Official Account.
  name: Zalo Official Account API
  slug: official-account-api
- description: Send template-based transactional notification messages to Zalo users by phone number.
  name: Zalo Notification Service (ZNS) API
  slug: zns-api
- description: User login and profile access via OAuth v4 user access tokens.
  name: Zalo Social API
  slug: social-api
artifact_total: 4
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zalo/refs/heads/main/hosts/zalo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zalo-hosts.yml
- group: company
  title: ''
  type: Blog
  url: https://zalo.me/vi/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zalo/refs/heads/main/security/zalo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zalo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zalo.me
- group: docs
  title: ''
  type: Documentation
  url: https://developers.zalo.me/docs
- group: start
  title: ''
  type: Portal
  url: https://developers.zalo.me/
- group: auth
  title: ''
  type: Authentication
  url: https://developers.zalo.me/docs/social-api/tham-khao/user-access-token-v4
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://zalo.me
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Zalo is a Vietnamese messaging platform (VNG Corporation). Zalo For Developers documents the Official Account API, the Zalo Notification Service (ZNS) API for template-based transactional messages, the Social API with OAuth v4 user access tokens, and Zalo Mini App.
image: https://h5.zdn.vn/static/zalo-site/thumb.jpg
layout: provider
modified: '2026-10-13'
name: Zalo
nav: Providers
network: true
overview: 'Zalo is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Messaging, CPaaS, Vietnam, and Notification.


  Zalo''s developer surface includes engineering blog, documentation, developer portal, authentication, and 3 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 71.4
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 10.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Zalo Domain Security
  slug: zalo-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: zalo
tags:
- Company
- Messaging
- CPaaS
- Vietnam
- Notification
website: https://zalo.me
---
