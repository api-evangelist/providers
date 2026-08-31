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
  url: security/noonswoon-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/noonswoon
- group: company
  title: ''
  type: Website
  url: https://noonswoonapp.com
created: '2026-07-17'
description: Noonswoon is an early-stage consumer mobile startup surfaced as a portfolio company of 500 Global and added to the API Evangelist network for enrichment. Its public GitHub organization (github.com/noonswoon) hosts a set of older mobile and social application projects (iOS/Android growth apps, a social-TV effort, and a web forum) dating from roughly 2012-2015. As of this enrichment pass the company publishes no developer portal, API documentation, OpenAPI, or SDKs, and its primary web property (noonswoonapp.com) returns a 502 backend error, indicating the consumer product is no longer actively operating. No public API surface was found to catalog; this profile captures the identity, domain-security posture, and source-code footprint that remain discoverable.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/noonswoon.png
layout: provider
modified: '2026-07-20'
name: Noonswoon
nav: Providers
network: true
overview: Noonswoon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Startup, Mobile, Consumer, and Social.
random_paper: 0
score:
  band: minimal
  composite: 5.3
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
    operational_transparency: 2.6
  previous_composite: 5.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/noonswoon/refs/heads/main/screenshots/noonswoon-2026-08-07T185502.png
security:
- kind: domain-security
  name: Noonswoon Domain Security
  slug: noonswoon-domain-security
  summary_line: TLSv1.2 · HSTS
slug: noonswoon
tags:
- Company
- Startup
- Mobile
- Consumer
- Social
website: https://noonswoonapp.com
---
