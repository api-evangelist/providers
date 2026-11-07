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
  band: agent-aware
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
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Single GraphQL gateway at api.island.is wrapping internal REST microservices that power island.is applications. The gateway is authentication-gated (island.is identity server / IdS scopes) and returns
  name: island.is GraphQL Gateway
  slug: graphql
- description: 'Iceland''s X-Road data-exchange layer (Straumurinn). Government-to-government REST services that publish OpenAPI 3.0 descriptions are auto-imported into the X-Road API Catalogue, providing a governed, '
  name: X-Road (Straumurinn) API Catalogue
  slug: xroad
artifact_total: 4
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://island.is/rss.xml
- group: auth
  href: https://artifacts.apis.io/island-is/security/island-is-domain-security.yml
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
  href: https://artifacts.apis.io/island-is/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-23'
description: island.is (Stafrænt Ísland / Digital Iceland) is Iceland's national digital-services and government API platform, operated by the Ministry of Finance and Economic Affairs / Digital Iceland. It provides a GraphQL gateway at api.island.is (authentication-gated) that fronts internal REST microservices, with business/government-to-government REST services described using OpenAPI 3.0 and registered in the X-Road "Straumurinn" API Catalogue. The developer handbook is published at docs.devland.is. Iceland's former CKAN open-data portal (opingogn.is) has been decommissioned and now redirects to island.is.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/island-is.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.devland.is over HTTP; 3 tools listed.
  name: island.is (Digital Iceland) MCP Server
  slug: island-is
modified: '2026-10-06'
name: island.is (Digital Iceland)
nav: Providers
network: true
overview: 'island.is (Digital Iceland) is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Digital Government, GraphQL, OpenAPI, X-Road, and API Platform.


  island.is (Digital Iceland)''s developer surface includes documentation and 4 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 68.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - iceland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 7.6
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/island-is/island-is-2026-07-25T222951.png
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
