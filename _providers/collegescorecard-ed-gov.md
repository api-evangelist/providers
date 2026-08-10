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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Data on higher education institutions in the United States
  name: CollegeScoreCard.ed.gov
  slug: collegescorecardedgov
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/collegescorecard-ed-gov-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://collegescorecard.ed.gov/data/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Data on higher education institutions in the United States
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/collegescorecard-ed-gov.png
layout: provider
modified: '2026-05-28'
name: CollegeScoreCard.ed.gov
nav: Providers
network: true
overview: CollegeScoreCard.ed.gov publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data and Public APIs.
random_paper: 100
score:
  band: minimal
  composite: 6.5
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/collegescorecard-ed-gov/refs/heads/main/screenshots/collegescorecard-ed-gov-2026-07-25T210054.png
security:
- kind: domain-security
  name: Collegescorecard Ed Gov Domain Security
  slug: collegescorecard-ed-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: collegescorecard-ed-gov
tags:
- Open Data
- Public APIs
website: https://collegescorecard.ed.gov/data/
---
