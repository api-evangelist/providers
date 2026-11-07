---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/opendocs-cloud/plans/opendocs-cloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/opendocs-cloud-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/opendocs-cloud/llms/opendocs-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/opendocs-cloud-llms.txt
- group: agent
  href: https://artifacts.apis.io/opendocs-cloud/well-known/opendocs-cloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/opendocs-cloud-well-known.yml
- group: other
  href: https://artifacts.apis.io/opendocs-cloud/hosts/opendocs-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/opendocs-cloud-hosts.yml
- group: other
  href: https://artifacts.apis.io/opendocs-cloud/vendors/opendocs-cloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/opendocs-cloud-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.opendocs.cloud/Identity/Account/Login
- group: auth
  href: https://artifacts.apis.io/opendocs-cloud/security/opendocs-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opendocs-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendocs.cloud/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.opendocs.cloud/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://opendocs.cloud/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://opendocs.cloud/docs
- group: operate
  title: ''
  type: Support
  url: https://opendocs.cloud/help-center
- group: company
  title: ''
  type: Blog
  url: https://opendocs.cloud/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://opendocs.cloud/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://opendocs.cloud/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://opendocs.cloud/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/opendocs-cloud/workspace
coverage:
  checked: '2026-10-31'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://app.opendocs.cloud/developers/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: opendocs-cloud provides a cloud-based platform for creating, sharing, and collaborating on API documentation. It enables developers to host interactive API docs, generate client SDKs, and manage versioning with ease. The service integrates with popular API design tools, supports OpenAPI and AsyncAPI specifications, and offers customizable theming and access controls for teams of any size. By centralizing documentation workflows, opendocs-cloud helps organizations improve API discoverability, reduce onboarding time, and maintain up-to-date reference material for internal and external consumers.
image: https://opendocs.cloud/og-image.png
layout: provider
modified: '2026-10-30'
name: opendocs-cloud
nav: Providers
network: true
overview: 'opendocs-cloud is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API Documentation, Cloud Platform, Developer Tools, and Collaboration.


  opendocs-cloud''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Opendocs Cloud Plans Pricing
  plan_count: 4
  slug: opendocs-cloud-plans-pricing
random_paper: 23
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.3
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 29.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/opendocs-cloud/opendocs-cloud-2026-11-03T140636.png
security:
- kind: domain-security
  name: Opendocs Cloud Domain Security
  slug: opendocs-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: opendocs-cloud
tags:
- Company
- API Documentation
- Cloud Platform
- Developer Tools
- Collaboration
website: https://opendocs.cloud/
---
