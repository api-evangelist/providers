---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Watermark and detect images, PDFs and videos synchronously or asynchronously.
  name: Etchv API
  slug: etchv-api
artifact_total: 6
asyncapis:
- description: ''
  name: Etchv Webhooks
  slug: etchv-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/etchv/plans/etchv-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/etchv-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/etchv/asyncapi/etchv-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/etchv-webhooks.yml
- group: design
  href: https://artifacts.apis.io/etchv/conventions/etchv-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/etchv-conventions.yml
- group: design
  href: https://artifacts.apis.io/etchv/conventions/etchv-conventions.yml
  title: ''
  type: Conventions
  url: conventions/etchv-conventions.yml
- group: auth
  href: https://artifacts.apis.io/etchv/authentication/etchv-authentication.yml
  title: ''
  type: Authentication
  url: authentication/etchv-authentication.yml
- group: design
  href: https://artifacts.apis.io/etchv/conformance/etchv-conformance.yml
  title: ''
  type: Conformance
  url: conformance/etchv-conformance.yml
- group: auth
  href: https://artifacts.apis.io/etchv/well-known/etchv-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/etchv-security.txt
- group: agent
  href: https://artifacts.apis.io/etchv/well-known/etchv-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/etchv-well-known.yml
- group: other
  href: https://artifacts.apis.io/etchv/hosts/etchv-hosts.yml
  title: ''
  type: Hosts
  url: hosts/etchv-hosts.yml
- group: other
  href: https://artifacts.apis.io/etchv/vendors/etchv-vendors.yml
  title: ''
  type: Vendors
  url: vendors/etchv-vendors.yml
- group: build
  href: https://artifacts.apis.io/etchv/packages/etchv-packages.yml
  title: ''
  type: SDKs
  url: packages/etchv-packages.yml
- group: build
  href: https://artifacts.apis.io/etchv/packages/etchv-packages.yml
  title: ''
  type: Packages
  url: packages/etchv-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://etchv.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.etchv.com/
- group: auth
  title: ''
  type: Security
  url: https://etchv.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://etchv.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://etchv.com/pricing
- group: start
  title: ''
  type: Login
  url: https://etchv.com/login
- group: company
  title: ''
  type: Blog
  url: https://etchv.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://etchv.com/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/etchv/security/etchv-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/etchv-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/etchv/security/etchv-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/etchv-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://etchv.com
- group: docs
  title: ''
  type: Documentation
  url: https://etchv.com/docs
created: '2026-10-20'
description: Etchv provides an invisible forensic watermarking API that embeds unique, traceable watermarks into images, PDFs, and video files. The service offers real-time API calls without signup, supporting formats like MP4 and MOV, and includes SDKs for multiple languages. It targets developers needing content security, provenance, and anti-piracy solutions, with detailed documentation, quickstart guides, and pricing information publicly available.
image: https://etchv.com/opengraph-image?3957397a121aa923
layout: provider
modified: '2026-10-20'
name: etchv
nav: Providers
network: true
overview: 'etchv is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Watermarking, Media, Security, and Developer Tools.


  The etchv catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  etchv''s developer surface includes authentication, pricing, engineering blog, getting-started guide, documentation, and 19 more developer resources.'
plans:
- name: Etchv Plans Pricing
  plan_count: 4
  slug: etchv-plans-pricing
random_paper: 10
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 47.5
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/etchv/etchv-2026-11-03T131628.png
security:
- kind: authentication
  name: Etchv Authentication
  slug: etchv-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Etchv Domain Security
  slug: etchv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Etchv Vulnerability Disclosure
  slug: etchv-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: etchv
tags:
- Company
- Watermarking
- Media
- Security
- Developer Tools
website: https://etchv.com
---
