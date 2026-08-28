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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hitwise-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.hitwise.com/
created: '2026-07-17'
description: Hitwise was an online competitive-intelligence and audience-measurement company that tracked website traffic, clickstream behavior, and search-term data to help marketers benchmark share of visits, referral sources, and competitor performance across industry verticals. Originally an Australian firm, it was later owned by Experian and then Connexity. The Hitwise brand has since been retired -- as of this enrichment pass the hitwise.com domain no longer serves a live product (it returns a lapsed-host "Site is not available" page with a mismatched TLS certificate) and exposes no public developer portal, documentation, or API. This profile was surfaced as a portfolio-company lead of insight-partners; enrichment found no active API surface to catalog.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hitwise.png
layout: provider
modified: '2026-07-19'
name: Hitwise
nav: Providers
network: true
overview: Hitwise is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Web Analytics, Competitive Intelligence, and Audience Measurement.
random_paper: 9
score:
  band: minimal
  composite: 5.0
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
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Hitwise Domain Security
  slug: hitwise-domain-security
  summary_line: no transport/DNS hardening detected
slug: hitwise
tags:
- Company
- Analytics
- Web Analytics
- Competitive Intelligence
- Audience Measurement
- Marketing
- Data
- Defunct
website: http://www.hitwise.com/
---
