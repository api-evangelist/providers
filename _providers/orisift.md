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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The Lookup API from Orisift — 1 operation(s) for lookup.
  name: Orisift Lookup API
  slug: orisift-lookup-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Blog
  url: https://orisift.com/blog/reserved-and-fictional-phone-ranges
- group: commercial
  href: https://artifacts.apis.io/orisift/plans/orisift-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/orisift-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/orisift/rules/orisift-rules.yml
  title: ''
  type: Spectral
  url: rules/orisift-rules.yml
- group: design
  href: https://artifacts.apis.io/orisift/json-ld/orisift-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/orisift-context.jsonld
- group: design
  href: https://artifacts.apis.io/orisift/vocabulary/orisift-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/orisift-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/orisift/data-model/orisift-data-model.yml
  title: ''
  type: DataModel
  url: data-model/orisift-data-model.yml
- group: design
  href: https://artifacts.apis.io/orisift/conformance/orisift-conformance.yml
  title: ''
  type: Conformance
  url: conformance/orisift-conformance.yml
- group: other
  href: https://artifacts.apis.io/orisift/hosts/orisift-hosts.yml
  title: ''
  type: Hosts
  url: hosts/orisift-hosts.yml
- group: other
  href: https://artifacts.apis.io/orisift/vendors/orisift-vendors.yml
  title: ''
  type: Vendors
  url: vendors/orisift-vendors.yml
- group: build
  href: https://artifacts.apis.io/orisift/packages/orisift-packages.yml
  title: ''
  type: SDKs
  url: packages/orisift-packages.yml
- group: build
  href: https://artifacts.apis.io/orisift/packages/orisift-packages.yml
  title: ''
  type: Packages
  url: packages/orisift-packages.yml
- group: auth
  href: https://artifacts.apis.io/orisift/security/orisift-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/orisift-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://orisift.com/
- group: docs
  title: ''
  type: Documentation
  url: https://orisift.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://orisift.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://orisift.com/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/orisift
- group: commercial
  title: ''
  type: Pricing
  url: https://orisift.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://orisift.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://orisift.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://orisift.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/orisift/workspace
coverage:
  checked: '2026-09-28'
  detail: Documentation at https://orisift.com/docs is a JavaScript‑rendered single‑page app with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://orisift.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: Orisift provides a unified validation API for phone numbers, email addresses, IP addresses, and domain information. The service offers format checking, numbering plan verification, reserved and fictional range detection for phone numbers, as well as MX, Null MX, SPF, and DMARC checks for email domains. It returns detailed evidence and risk signals, supporting agencies and developers in data quality and compliance workflows. The platform delivers a single endpoint with credit‑based usage, allowing free trial credits and paid plans for higher volume.
image: https://orisift.com/opengraph-image?0bbf128a9b71721e
json_schemas:
- name: PostV1LookupRequest
  property_count: 1
  slug: orisift-post-v1-lookup-request
- name: PostV1LookupResponse
  property_count: 13
  slug: orisift-post-v1-lookup-response
jsonld:
- class_count: 2
  name: Orisift Context
  property_count: 14
  slug: orisift-context
layout: provider
modified: '2026-09-28'
name: Orisift
nav: Providers
network: true
overview: 'Orisift is listed with 1 API on the [APIs.io](https://apis.io/) network: Lookup API. Tagged areas include Company, Validation, Phone, Email, and IP.


  The Orisift catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Orisift''s developer surface includes engineering blog, documentation, API reference, getting-started guide, pricing, signup flow, and 16 more developer resources.'
plans:
- name: Orisift Plans Pricing
  plan_count: 4
  slug: orisift-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Orisift API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: orisift-rules
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.0
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 22.1
    developer_ergonomics: 25.0
    discoverability: 57.1
    operational_transparency: 2.6
  previous_composite: 38.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/orisift/orisift-2026-10-11T112208.png
security:
- kind: domain-security
  name: Orisift Domain Security
  slug: orisift-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: orisift
tags:
- Company
- Validation
- Phone
- Email
- IP
- Domain
website: https://orisift.com/
---
