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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/starion-group/well-known/starion-group-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/starion-group-well-known.yml
- group: other
  href: https://artifacts.apis.io/starion-group/hosts/starion-group-hosts.yml
  title: ''
  type: Hosts
  url: hosts/starion-group-hosts.yml
- group: build
  href: https://artifacts.apis.io/starion-group/packages/starion-group-packages.yml
  title: ''
  type: SDKs
  url: packages/starion-group-packages.yml
- group: build
  href: https://artifacts.apis.io/starion-group/packages/starion-group-packages.yml
  title: ''
  type: Packages
  url: packages/starion-group-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stariongroup.eu/legal-notice/
- group: operate
  title: ''
  type: Support
  url: https://support.stariongroup.eu/support/home
- group: auth
  title: ''
  type: Security
  url: https://www.stariongroup.eu/category/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stariongroup.eu/privacy-notice/
- group: company
  title: ''
  type: Newsroom
  url: https://www.stariongroup.eu/news/
- group: company
  title: ''
  type: Blog
  url: https://www.stariongroup.eu/category/media-updates/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/STARIONGROUP
- group: auth
  href: https://artifacts.apis.io/starion-group/security/starion-group-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/starion-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stariongroup.eu/
- group: other
  title: ''
  type: x-coverage
  url: https://api.stariongroup.eu/openapi.json
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://support.stariongroup.eu/mcp
  - status: 200
    url: https://www.stariongroup.eu/
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: Starion Group provides system engineering services for space, defence, and critical infrastructures. Based in Europe, they offer expertise in satellite lifecycle, space systems engineering, security, ground segment operations, data engineering, MBSE, AI, and quantum technologies, serving both public and private sector clients.
image: https://www.stariongroup.eu/wp-content/uploads/2023/01/starion-logo.png
layout: provider
modified: '2026-10-26'
name: Starion Group
nav: Providers
network: true
overview: 'Starion Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Space, Defence, Engineering, and Critical Infrastructure.


  Starion Group''s developer surface includes support, engineering blog, and 12 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 49.1
    operational_transparency: 7.9
  previous_composite: 14.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/starion-group/starion-group-2026-11-03T143739.png
security:
- kind: domain-security
  name: Starion Group Domain Security
  slug: starion-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: starion-group
tags:
- Company
- Space
- Defence
- Engineering
- Critical Infrastructure
website: https://www.stariongroup.eu/
---
