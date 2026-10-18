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
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 1.8
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/newsguard/refs/heads/main/well-known/newsguard-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/newsguard-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/newsguard/refs/heads/main/hosts/newsguard-hosts.yml
  title: ''
  type: Hosts
  url: hosts/newsguard-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/newsguard/refs/heads/main/vendors/newsguard-vendors.yml
  title: ''
  type: Vendors
  url: vendors/newsguard-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/newsguard/refs/heads/main/security/newsguard-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/newsguard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://newsguardtech.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://newsguardtech.com/
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: NewsGuard provides transparent reliability ratings for news and information sources, helping users identify trustworthy content and avoid misinformation. Their platform offers AI‑driven tools, false‑claim fingerprints, and comprehensive dashboards for media outlets, advertisers, and researchers. By combining human expertise with automated analysis, NewsGuard aims to improve media literacy and combat disinformation across digital platforms.
layout: provider
modified: '2026-10-12'
name: NewsGuard
nav: Providers
network: true
overview: NewsGuard is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Fact Checking, Artificial Intelligence, and Disinformation.
random_paper: 8
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Newsguard Domain Security
  slug: newsguard-domain-security
  summary_line: DMARC
slug: newsguard
tags:
- Company
- Media
- Fact Checking
- Artificial Intelligence
- Disinformation
website: https://newsguardtech.com/
---
