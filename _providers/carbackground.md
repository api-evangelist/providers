---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
    dynamic_client_registration: true
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
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: CarBackground.ai provides vehicle background data via a private API; documentation is only available by email.
  name: CarBackground API
  slug: carbackground-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/carbackground/plans/carbackground-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/carbackground-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://carbackground.ai/trust
- group: design
  href: https://artifacts.apis.io/carbackground/conformance/carbackground-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carbackground-conformance.yml
- group: agent
  href: https://artifacts.apis.io/carbackground/llms/carbackground-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carbackground-llms.txt
- group: auth
  href: https://artifacts.apis.io/carbackground/well-known/carbackground-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/carbackground-security.txt
- group: agent
  href: https://artifacts.apis.io/carbackground/well-known/carbackground-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carbackground-well-known.yml
- group: other
  href: https://artifacts.apis.io/carbackground/hosts/carbackground-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carbackground-hosts.yml
- group: other
  href: https://artifacts.apis.io/carbackground/vendors/carbackground-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carbackground-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://carbackground.ai/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carbackground.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carbackground.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://carbackground.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://carbackground.ai/blog
- group: auth
  href: https://artifacts.apis.io/carbackground/security/carbackground-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/carbackground-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/carbackground/security/carbackground-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carbackground-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carbackground.ai/
coverage:
  checked: '2026-11-03'
  detail: Documentation is only provided by email and no machine‑readable OpenAPI, GraphQL, AsyncAPI or other contract is publicly accessible.
  evidence:
  - status: 200
    url: https://app.carbackground.ai/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Car Background AI offers an AI‑powered car photo editor that removes or replaces vehicle backgrounds, enhances lighting and detail, and provides bulk processing and dealership branding tools. The service is aimed at car dealers, photographers, private sellers, online marketplaces, and dealer‑management systems that need consistent, marketplace‑ready images at scale.
image: https://carbackground.ai/a/3hxVSBkC7Dw7Cd5d65r527/carbg-social-preview.webp
layout: provider
modified: '2026-11-03'
name: Car Background AI
nav: Providers
network: true
overview: 'Car Background AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Car Photo Editing, Bulk Editing, Dealership Branding, Automotive Marketplace, and License Plate Blur.


  Car Background AI''s developer surface includes pricing, engineering blog, and 14 more developer resources.'
plans:
- name: Carbackground Plans Pricing
  plan_count: 4
  slug: carbackground-plans-pricing
random_paper: 22
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 51.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carbackground Domain Security
  slug: carbackground-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Carbackground Vulnerability Disclosure
  slug: carbackground-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: carbackground
tags:
- Car Photo Editing
- Bulk Editing
- Dealership Branding
- Automotive Marketplace
- License Plate Blur
- Background Generation
website: https://carbackground.ai/
---
