---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Read-only REST API providing access to U.S. Congressional data including bills and resolutions, roll call votes, member profiles, committee information, cosponsorship records, and congressional roles.
  name: GovTrack REST API
  slug: govtrack-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/govtrack-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.govtrack.us
- group: docs
  title: ''
  type: Documentation
  url: https://www.govtrack.us/developers/api
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/govtrack
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/govtrack
- group: company
  title: ''
  type: Blog
  url: https://www.govtrack.us/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.govtrack.us/about
- group: other
  title: ''
  type: X
  url: https://x.com/govtrack
- group: commercial
  title: ''
  type: Plans
  url: plans/govtrack-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/govtrack-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/govtrack-finops.yml
created: '2026-06-13'
description: GovTrack is a free, open-access platform for tracking the United States Congress, providing legislative data since 2004. It offers a REST API for accessing bill status, voting records, Congressional member information, committee data, and cosponsorship records — all without authentication or API keys. Operated by Civic Impulse, LLC, GovTrack serves millions of users annually including journalists, legislative professionals, educators, and the general public.
finops:
- name: Govtrack Finops
  service_category: ''
  slug: govtrack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/govtrack.png
layout: provider
modified: '2026-06-13'
name: GovTrack
nav: Providers
network: true
overview: 'GovTrack publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Government, Legislative, Congress, Bills, and Voting Records.


  GovTrack''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Govtrack Plans Pricing
  plan_count: 2
  slug: govtrack-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 1
  name: Govtrack Rate Limits
  slug: govtrack-rate-limits
score:
  band: emerging
  composite: 25.8
  delta: -3.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 32.3
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 29.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/govtrack/refs/heads/main/screenshots/govtrack-2026-06-20T182304.png
security:
- kind: domain-security
  name: Govtrack Domain Security
  slug: govtrack-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: govtrack
tags:
- Government
- Legislative
- Congress
- Bills
- Voting Records
- Political Data
- Open Government
- United States
website: https://www.govtrack.us
---
