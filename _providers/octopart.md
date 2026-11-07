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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Octopart API v4 GraphQL endpoint for electronic part data (search, pricing, availability, specs). Anonymous introspection at https://octopart.com/api/v4/endpoint returns {"errors":[{"message":"no toke
  name: Octopart
  slug: octopart
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/octopart/hosts/octopart-hosts.yml
  title: ''
  type: Hosts
  url: hosts/octopart-hosts.yml
- group: other
  href: https://artifacts.apis.io/octopart/vendors/octopart-vendors.yml
  title: ''
  type: Vendors
  url: vendors/octopart-vendors.yml
- group: build
  href: https://artifacts.apis.io/octopart/packages/octopart-packages.yml
  title: ''
  type: SDKs
  url: packages/octopart-packages.yml
- group: build
  href: https://artifacts.apis.io/octopart/packages/octopart-packages.yml
  title: ''
  type: Packages
  url: packages/octopart-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/octopart
- group: auth
  href: https://artifacts.apis.io/octopart/security/octopart-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/octopart-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://octopart.com/api/v4/reference
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Electronic part data for manufacturing, design, and sourcing
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/octopart.png
layout: provider
modified: '2026-10-19'
name: Octopart
nav: Providers
network: true
overview: Octopart is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Shopping and Public APIs.
random_paper: 12
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 55.4
    operational_transparency: 2.6
  previous_composite: 8.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/octopart/octopart-2026-08-07T185945.png
security:
- kind: domain-security
  name: Octopart Domain Security
  slug: octopart-domain-security
  summary_line: TLSv1.3 · DMARC
slug: octopart
tags:
- Shopping
- Public APIs
website: https://octopart.com/api/v4/reference
---
