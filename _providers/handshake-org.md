---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/handshake-org/hosts/handshake-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/handshake-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/handshake-org/vendors/handshake-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/handshake-org-vendors.yml
- group: auth
  href: https://artifacts.apis.io/handshake-org/security/handshake-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/handshake-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://handshake.org/
- group: docs
  title: ''
  type: Documentation
  url: https://handshake-org.github.io/
- group: operate
  title: ''
  type: Community
  url: https://handshake.org/community
- group: operate
  title: ''
  type: FAQ
  url: https://handshake.org/faq
- group: other
  title: ''
  type: Download
  url: https://handshake.org/download
coverage:
  checked: '2026-10-26'
  detail: Documentation redirects to a non‑existent spec URL, providing no machine‑readable contract.
  evidence:
  - status: 301
    url: https://handshake-org.github.io/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Handshake is a decentralized, permissionless naming protocol that enables the registration and management of top-level domain names on a blockchain. It provides a secure, censorship-resistant alternative to traditional DNS, allowing users to own and control their internet identities without reliance on centralized authorities. The project is backed by notable investors such as Greylock, Pantera Capital, and Sequoia Capital, and aims to foster an open, user-owned internet ecosystem.
image: https://www.handshake.org/images/landing/logo-dark.svg
layout: provider
modified: '2026-10-25'
name: Handshake
nav: Providers
network: true
overview: 'Handshake is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Decentralized, Naming, Blockchain, and DNS.


  Handshake''s developer surface includes documentation, FAQ, and 6 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 4.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/handshake-org/handshake-org-2026-11-03T133141.png
security:
- kind: domain-security
  name: Handshake Org Domain Security
  slug: handshake-org-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: handshake-org
tags:
- Company
- Decentralized
- Naming
- Blockchain
- DNS
website: https://handshake.org/
---
