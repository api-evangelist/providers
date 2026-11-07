---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/betrend-im/llms/betrend-im-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/betrend-im-llms.txt
- group: other
  href: https://artifacts.apis.io/betrend-im/hosts/betrend-im-hosts.yml
  title: ''
  type: Hosts
  url: hosts/betrend-im-hosts.yml
- group: other
  href: https://artifacts.apis.io/betrend-im/vendors/betrend-im-vendors.yml
  title: ''
  type: Vendors
  url: vendors/betrend-im-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://betrend.im/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://betrend.im/en/privacy
- group: start
  title: ''
  type: Login
  url: https://betrend.im/en/login
- group: auth
  href: https://artifacts.apis.io/betrend-im/security/betrend-im-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/betrend-im-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://betrend.im/
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's hosts.
  evidence:
  - status: 200
    url: https://betrend.im/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: betrend provides live scores, odds, racing and lottery results for the United Kingdom. The platform offers real‑time updates on football matches, horse racing, and lottery draws, with detailed statistics, betting odds, and match commentary. Users can browse upcoming fixtures, view past results, and access comprehensive sports data across multiple languages.
examples:
- key_count: 3
  name: Betrend Im Mcp
  slug: betrend-im-mcp
image: https://betrend.im/icons/og-default.png
layout: provider
modified: '2026-11-02'
name: betrend - Live Scores, Odds, Racing and Lottery Results
nav: Providers
network: true
overview: betrend - Live Scores, Odds, Racing and Lottery Results is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sports, Live Scores, Betting, and Lottery.
random_paper: 15
scopes:
- name: Betrend Im Scopes
  scope_count: 0
  slug: betrend-im-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Betrend Im Authentication
  slug: betrend-im-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Betrend Im Domain Security
  slug: betrend-im-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: betrend-im
tags:
- Company
- Sports
- Live Scores
- Betting
- Lottery
- United Kingdom
website: https://betrend.im/
---
