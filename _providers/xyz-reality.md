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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://www.xyzreality.com/security-policy
- group: auth
  href: https://artifacts.apis.io/xyz-reality/well-known/xyz-reality-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/xyz-reality-security.txt
- group: agent
  href: https://artifacts.apis.io/xyz-reality/well-known/xyz-reality-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/xyz-reality-well-known.yml
- group: other
  href: https://artifacts.apis.io/xyz-reality/hosts/xyz-reality-hosts.yml
  title: ''
  type: Hosts
  url: hosts/xyz-reality-hosts.yml
- group: other
  href: https://artifacts.apis.io/xyz-reality/vendors/xyz-reality-vendors.yml
  title: ''
  type: Vendors
  url: vendors/xyz-reality-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.xyzreality.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.xyzreality.com/resource-type/newsroom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/XYZReality
- group: auth
  href: https://artifacts.apis.io/xyz-reality/security/xyz-reality-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/xyz-reality-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/xyz-reality/security/xyz-reality-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xyz-reality-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.xyzreality.com
coverage:
  checked: '2026-10-25'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found at the API host.
  evidence:
  - status: 0
    url: https://api.xyzreality.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: XYZ Reality provides a construction delivery platform that integrates data, BIM, and augmented reality to improve project controls, quality, and progress tracking. Their solutions serve owners, general contractors, and specialty contractors across sectors like data centers, airports, pharmaceuticals, hydrogen plants, and oil & gas, offering tools such as engineering‑grade AR, 360° validation, and on‑site deployment to reduce rework and accelerate delivery.
image: https://xyz-reality.transforms.svdcdn.com/production/assets/Page-Images/Onsite-deployment/Ontime-delivery-3.jpg?w=1200&h=630&q=82&auto=format&fit=crop&dm=1738945418&s=9a14dac00700f9b0f5a72140d5d5c816
layout: provider
modified: '2026-10-25'
name: XYZ Reality
nav: Providers
network: true
overview: XYZ Reality is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Augmented Reality, Virtual Reality, and PropTech.
random_paper: 18
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.4
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 7.9
  previous_composite: 9.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/xyz-reality/xyz-reality-2026-11-03T150319.png
security:
- kind: domain-security
  name: Xyz Reality Domain Security
  slug: xyz-reality-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Xyz Reality Vulnerability Disclosure
  slug: xyz-reality-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: xyz-reality
tags:
- Company
- Real Estate
- Augmented Reality
- Virtual Reality
- PropTech
- Platform
website: https://www.xyzreality.com
---
