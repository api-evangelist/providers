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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Arqit provides quantum‑resistant encryption and key management APIs as described in their resource reference pages.
  name: Arqit API
  slug: arqit-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arqit-limited/refs/heads/main/hosts/arqit-limited-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arqit-limited-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arqit-limited/refs/heads/main/vendors/arqit-limited-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arqit-limited-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arqitgroup.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://arqitgroup.com/news
- group: other
  title: ''
  type: Leadership
  url: https://arqitgroup.com/leadership/nicola-barbiero
- group: company
  title: ''
  type: Blog
  url: https://arqitgroup.com/resources/blog
- group: docs
  title: ''
  type: APIReference
  url: https://arqitgroup.com/resources/tag/reference
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arqit-limited/refs/heads/main/security/arqit-limited-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arqit-limited-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arqitgroup.com
coverage:
  checked: 2026-09-26
  detail: Reference pages render via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://arqitgroup.com/resources/tag/reference
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Arqit provides enterprise‑grade quantum security solutions that safeguard data against future quantum threats. Their platform enables secure communications at scale, offering quantum‑resistant encryption, key management, and cryptographic services for enterprises seeking to protect information from emerging quantum attacks. Arqit’s technology is built on quantum‑ready protocols and integrates with existing security infrastructures to future‑proof data protection.
layout: provider
modified: '2026-09-26'
name: Arqit
nav: Providers
network: true
overview: 'Arqit publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Quantum Security, Encryption, Enterprise, and Crypto.


  Arqit''s developer surface includes engineering blog, API reference, and 7 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arqit Limited Domain Security
  slug: arqit-limited-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arqit-limited
tags:
- Company
- Quantum Security
- Encryption
- Enterprise
- Crypto
website: https://arqitgroup.com
---
