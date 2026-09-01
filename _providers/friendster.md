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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/friendster-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://friendster.com
created: '2026-07-17'
description: Friendster is a mobile-first social network for real-life friends, operating at friendster.com with a native iOS app and a web experience. The service positions itself around privacy and intentional design — no ads, no algorithms, no spam, and an explicit promise never to sell user data — and centers on connecting people with the friends they actually know in real life. It was surfaced as a portfolio company of Battery Ventures and added to the API Evangelist network as a stub. As of this enrichment pass Friendster publishes a consumer marketing site and a native iOS app, but exposes no public developer program, API, OpenAPI, or documentation surface — so there are no API artifacts to harvest, only company identity and live domain-security posture.
image: https://friendster.com/img/OGimg.png
layout: provider
modified: '2026-07-19'
name: Friendster
nav: Providers
network: true
overview: Friendster is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social Network, Social-Media, Consumer, and Mobile.
random_paper: 7
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
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/friendster/refs/heads/main/screenshots/friendster-2026-07-25T215219.png
security:
- kind: domain-security
  name: Friendster Domain Security
  slug: friendster-domain-security
  summary_line: TLSv1.3 · DMARC
slug: friendster
tags:
- Company
- Social Network
- Social-Media
- Consumer
- Mobile
- Privacy
website: https://friendster.com
---
