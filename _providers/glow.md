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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/glow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://glow.fm
created: '2026-07-17'
description: 'Glow (glow.fm) was a podcast subscription and membership monetization platform that let podcasters run paid, listener-supported premium feeds. The standalone product has since been folded into Libsyn: as of this enrichment pass the glow.fm domain issues a 301 redirect to Libsyn''s podcast-monetization offering, its TLS certificate has expired, and no active developer portal, API, documentation, or SDK surface remains under the Glow brand. It was surfaced in the API Evangelist network as a venture-portfolio lead (a16z, Norwest Venture Partners, Union Square Ventures) and has no live API to enrich.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/glow.png
layout: provider
modified: '2026-07-19'
name: Glow
nav: Providers
network: true
overview: Glow is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Podcasting, Media, Monetization, and Subscription.
random_paper: 0
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
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/glow/refs/heads/main/screenshots/glow-2026-07-25T215929.png
security:
- kind: domain-security
  name: Glow Domain Security
  slug: glow-domain-security
  summary_line: no transport/DNS hardening detected
slug: glow
tags:
- Company
- Podcasting
- Media
- Monetization
- Subscription
- Defunct
website: https://glow.fm
---
