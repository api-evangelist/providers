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
api_count: 1
apis:
- description: Integration for ClickBid platform to earn money via games.
  name: ClickBid API
  slug: clickbid-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/clickbid/llms/clickbid-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clickbid-llms.txt
- group: other
  href: https://artifacts.apis.io/clickbid/hosts/clickbid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clickbid-hosts.yml
- group: other
  href: https://artifacts.apis.io/clickbid/vendors/clickbid-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clickbid-vendors.yml
- group: auth
  href: https://artifacts.apis.io/clickbid/security/clickbid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clickbid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clickbid.io/
- group: docs
  title: ''
  type: Documentation
  url: https://clickbid.io/guides/earn-money-playing-games
- group: operate
  title: ''
  type: Support
  url: https://clickbid.io/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clickbid.io/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clickbid.io/privacy
coverage:
  checked: '2026-10-27'
  detail: Documentation pages are static HTML with no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL files discovered.
  evidence:
  - status: 200
    url: https://clickbid.io/guides/earn-money-playing-games
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: ClickBid lives in your phone's wallet. Play featured games, hit in-game goals, and earn real money delivered straight to your pass — no app install. The platform enables users to engage with games, achieve milestones, and receive payouts directly to their digital wallet, all without needing a separate app installation.
image: https://clickbid.io/public/icon-192.png
layout: provider
modified: '2026-10-27'
name: ClickBid
nav: Providers
network: true
overview: 'ClickBid is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobile, Gaming, Payments, and Wallets.


  ClickBid''s developer surface includes documentation, support, and 7 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 64.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 8.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/clickbid/clickbid-2026-11-03T124410.png
security:
- kind: domain-security
  name: Clickbid Domain Security
  slug: clickbid-domain-security
  summary_line: TLSv1.3 · DMARC
slug: clickbid
tags:
- Company
- Mobile
- Gaming
- Payments
- Wallets
website: https://clickbid.io/
---
