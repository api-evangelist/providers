---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Provides programmatic access to Landmark Global shipping, tracking, customs and fulfillment services as described on the integrations page.
  name: Landmark Global API
  slug: landmark-global-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/landmark-global/hosts/landmark-global-hosts.yml
  title: ''
  type: Hosts
  url: hosts/landmark-global-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/landmarkglobal
- group: auth
  href: https://artifacts.apis.io/landmark-global/security/landmark-global-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/landmark-global-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://landmarkglobal.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://landmarkglobal.com/eu/en/
- group: docs
  title: ''
  type: Documentation
  url: https://landmarkglobal.com/eu/en/integrations-technology/
- group: docs
  title: ''
  type: APIReference
  url: https://mercury.landmarkglobal.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://landmarkglobal.com/eu/en/about-us/
- group: operate
  title: ''
  type: Support
  url: https://landmarkglobal.com/eu/en/customer-support/
- group: company
  title: ''
  type: Blog
  url: https://landmarkglobal.com/eu/en/news-insights/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://landmarkglobal.com/eu/en/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://landmarkglobal.com/eu/en/privacy-policy/
coverage:
  checked: '2026-10-28'
  detail: Documentation describes API capabilities but provides no machine‑readable OpenAPI, GraphQL or other contract.
  evidence:
  - status: 404
    url: https://api.landmarkglobal.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Landmark Global provides cross‑border e‑commerce logistics, offering parcel delivery, customs clearance, fulfillment, and returns solutions across Europe, Asia, the US and Canada. Their platform integrates with merchants via APIs and a technology suite called Mercury, helping businesses expand globally with streamlined shipping and tracking services.
image: https://landmarkglobal.com/uploads/_1200x630_crop_center-center_82_none_ns/LandmarkGlobal_010_LogoFiltre.jpg?mtime=1782391230
layout: provider
modified: '2026-10-27'
name: Landmark Global
nav: Providers
network: true
overview: 'Landmark Global is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, E-commerce, Shipping, and API.


  Landmark Global''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 7 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Landmark Global Domain Security
  slug: landmark-global-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: landmark-global
tags:
- Company
- Logistics
- E-commerce
- Shipping
- API
website: https://landmarkglobal.com/
---
