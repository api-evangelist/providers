---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/zornade-com/plans/zornade-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zornade-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/zornade-com/security/zornade-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/zornade-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/zornade-com/authentication/zornade-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zornade-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/zornade-com/llms/zornade-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zornade-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/zornade-com/well-known/zornade-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/zornade-com-security.txt
- group: agent
  href: https://artifacts.apis.io/zornade-com/well-known/zornade-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zornade-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/zornade-com/hosts/zornade-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zornade-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/zornade-com/vendors/zornade-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zornade-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zornade.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zornade.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://zornade.com/pricing
- group: build
  title: ''
  type: Postman
  url: https://god.gw.postman.com/run-collection/58736891-302076e4-847a-4e05-a332-497dda6836a6?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D58736891-302076e4-847a-4e05-a332-497dda6836a6%26entityType%3Dcollection%26workspaceId%3D4c1afaac-145d-4c8e-871d-31b3b8646862
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zornade
- group: docs
  title: ''
  type: Documentation
  url: https://zornade.com/documentation
- group: company
  title: ''
  type: Blog
  url: https://zornade.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://app.zornade.com/api/?utm_source=zornade.com&utm_medium=internal_nav&utm_campaign=footer_developer&utm_content=api_reference&ref=footer_developer-api_reference
- group: auth
  href: https://artifacts.apis.io/zornade-com/security/zornade-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/zornade-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/zornade-com/security/zornade-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zornade-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zornade.com/
created: '2026-10-31'
description: Zornade is an Italian provider of territorial data, offering access to cadastral information and a suite of 19 data blocks sourced from over 15 official registries. Through its APIs and ready-to-use maps, it serves approximately 85 million parcels, enabling developers to integrate comprehensive land and property data into applications for analytics, visualization, and services across Italy.
image: https://zornade.com/ogimage.jpg
layout: provider
modified: '2026-10-31'
name: zornade-com
nav: Providers
network: true
overview: 'zornade-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, GIS, Italy, and Land Registry.


  zornade-com''s developer surface includes authentication, pricing, documentation, engineering blog, API reference, and 14 more developer resources.'
plans:
- name: Zornade Com Plans Pricing
  plan_count: 4
  slug: zornade-com-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 21.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.4
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 48.2
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - italy
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - italy-southern-europe
  previous_composite: 28.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Zornade Com Authentication
  slug: zornade-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Zornade Com Domain Security
  slug: zornade-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zornade Com Vulnerability Disclosure
  slug: zornade-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zornade-com
tags:
- Company
- Data
- GIS
- Italy
- Land Registry
website: https://zornade.com/
---
