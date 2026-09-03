---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://tapsense.com
coverage:
  checked: '2026-08-12'
  detail: TapSense is dead and its domain has been resold - tapsense.com now answers from Trellian's parking netblock with a 995-byte "This domain may be for sale" page on a wildcard record, so api. and developer. return that same holding page rather than any surface and docs.tapsense.com fails TLS on an expired certificate.
  evidence:
  - status: 200
    url: https://tapsense.com/
  - status: 200
    url: https://api.tapsense.com/
  - status: 200
    url: https://developer.tapsense.com/
  - status: 0
    url: https://docs.tapsense.com/
  - status: 404
    url: https://tapsense.com/openapi.json
  - status: 404
    url: https://tapsense.com/.well-known/agent-card.json
  reason: defunct
  state: none
created: '2026-07-17'
description: TapSense was a mobile advertising and real-time-bidding exchange founded in 2011 in San Francisco, connecting app publishers to brand advertisers through a private mobile RTB marketplace, an advertiser API and publisher SDKs. It was surfaced as a portfolio company of a16z and added to the API Evangelist network as a stub for enrichment. The company is defunct and the 2026-08-12 re-verification confirms it - the tapsense.com zone is now a parked domain held by Trellian Pty. Limited, serving a 995-byte "This domain may be for sale" holding page from a wildcard A record, so www, api and developer subdomains all return that same page and docs.tapsense.com fails TLS on an expired certificate. No OpenAPI, GraphQL, AsyncAPI, MCP, agent card, webhook or well-known document exists on any host, and no first-party package survives on npm, PyPI, RubyGems, Maven Central, CocoaPods or crates.io. The advertiser API and mobile SDKs the company once marketed went offline with it, so there is
  nothing to enrich beyond this identity record.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tapsense.png
layout: provider
modified: '2026-08-12'
name: Tapsense
nav: Providers
network: true
overview: Tapsense is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobile Advertising, AdTech, Real-Time Bidding, and Monetization.
random_paper: 6
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tapsense/refs/heads/main/screenshots/tapsense-2026-09-02T162533.png
slug: tapsense
tags:
- Company
- Mobile Advertising
- AdTech
- Real-Time Bidding
- Monetization
website: https://tapsense.com
---
