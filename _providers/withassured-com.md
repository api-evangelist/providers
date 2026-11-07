---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    dynamic_client_registration: true
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
  score: 18.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Assured platform providing credentialing and enrollment operations.
  name: Assured Platform API
  slug: assured-platform-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/withassured-com/conformance/withassured-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/withassured-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/withassured-com/llms/withassured-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/withassured-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/withassured-com/well-known/withassured-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/withassured-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/withassured-com/hosts/withassured-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/withassured-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/withassured-com/vendors/withassured-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/withassured-com-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.withassured.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.withassured.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/withassured-com/authentication/withassured-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/withassured-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/withassured-com/security/withassured-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/withassured-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://withassured.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.withassured.com/
- group: company
  title: ''
  type: Blog
  url: https://www.withassured.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.withassured.com/terms-and-condition
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.withassured.com/privacy-policy
created: '2026-10-25'
description: Assured provides an AI‑powered platform that streamlines provider credentialing, payer enrollment, and network management for health systems, digital‑health companies, and multi‑specialty groups. The solution automates credentialing committee readiness, reduces enrollment time to under 48 hours, and offers tools such as NPI and PECOS lookup, licensing, and roster management. Backed by Kindred Ventures, Assured aims to simplify compliance and accelerate onboarding across the healthcare ecosystem.
image: https://cdn.prod.website-files.com/69a36525d6ee68c8fc548c9d/6a85fcb309a6e237c1a8ebc2_c7d7693cf2e8eb12c9f4fb40fbaaff72_OpenGraph.jpg
layout: provider
modified: '2026-10-25'
name: Assured
nav: Providers
network: true
overview: 'Assured is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Credentialing, Artificial Intelligence, and Platform.


  Assured''s developer surface includes API reference, authentication, documentation, engineering blog, and 10 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 73.2
    operational_transparency: 0.0
  previous_composite: 21.1
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/withassured-com/withassured-com-2026-11-03T150206.png
security:
- kind: authentication
  name: Withassured Com Authentication
  slug: withassured-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Withassured Com Domain Security
  slug: withassured-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: withassured-com
tags:
- Company
- Healthcare
- Credentialing
- Artificial Intelligence
- Platform
website: https://withassured.com/
---
