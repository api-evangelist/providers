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
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: Single GraphQL gateway at api.island.is wrapping internal REST microservices that power island.is applications. The gateway is authentication-gated (island.is identity server / IdS scopes) and returns
  name: island.is GraphQL Gateway
  slug: graphql
- description: 'Iceland''s X-Road data-exchange layer (Straumurinn). Government-to-government REST services that publish OpenAPI 3.0 descriptions are auto-imported into the X-Road API Catalogue, providing a governed, '
  name: X-Road (Straumurinn) API Catalogue
  slug: xroad
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/island-is-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://island.is
- group: docs
  title: ''
  type: Documentation
  url: https://docs.devland.is/
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-23'
description: island.is (Stafrænt Ísland / Digital Iceland) is Iceland's national digital-services and government API platform, operated by the Ministry of Finance and Economic Affairs / Digital Iceland. It provides a GraphQL gateway at api.island.is (authentication-gated) that fronts internal REST microservices, with business/government-to-government REST services described using OpenAPI 3.0 and registered in the X-Road "Straumurinn" API Catalogue. The developer handbook is published at docs.devland.is. Iceland's former CKAN open-data portal (opingogn.is) has been decommissioned and now redirects to island.is.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/island-is.png
layout: provider
modified: '2026-06-23'
name: island.is (Digital Iceland)
nav: Providers
network: true
overview: 'island.is (Digital Iceland) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Digital Government, GraphQL, OpenAPI, X-Road, and API Platform.


  island.is (Digital Iceland)''s developer surface includes documentation and 3 more developer resources.'
random_paper: 60
score:
  band: minimal
  composite: 9.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/island-is/refs/heads/main/screenshots/island-is-2026-07-25T222951.png
security:
- kind: domain-security
  name: Island Is Domain Security
  slug: island-is-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: island-is
tags:
- Digital Government
- GraphQL
- OpenAPI
- X-Road
- API Platform
- Government Data
- National Government
- Iceland
- Europe
website: https://island.is
---
