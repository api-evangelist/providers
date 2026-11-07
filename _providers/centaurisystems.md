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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-11-06'
api_count: 4
apis:
- description: Launchpad developer portal API for Centauri Systems
  name: Launchpad API
  slug: launchpad-api
- description: The Oauth API from Centauri Systems — 1 operation(s) for oauth.
  name: Centauri Systems OAuth API
  slug: centaurisystems-oauth-api
- description: The Payments API from Centauri Systems — 1 operation(s) for payments.
  name: Centauri Systems Payments API
  slug: centaurisystems-payments-api
- description: The Users API from Centauri Systems — 1 operation(s) for users.
  name: Centauri Systems Users API
  slug: centaurisystems-users-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/centaurisystems/plans/centaurisystems-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/centaurisystems-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/centaurisystems/rules/centaurisystems-rules.yml
  title: ''
  type: Spectral
  url: rules/centaurisystems-rules.yml
- group: design
  href: https://artifacts.apis.io/centaurisystems/json-ld/centaurisystems-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/centaurisystems-context.jsonld
- group: design
  href: https://artifacts.apis.io/centaurisystems/vocabulary/centaurisystems-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/centaurisystems-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/centaurisystems/data-model/centaurisystems-data-model.yml
  title: ''
  type: DataModel
  url: data-model/centaurisystems-data-model.yml
- group: design
  href: https://artifacts.apis.io/centaurisystems/conformance/centaurisystems-conformance.yml
  title: ''
  type: Conformance
  url: conformance/centaurisystems-conformance.yml
- group: agent
  href: https://artifacts.apis.io/centaurisystems/llms/centaurisystems-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/centaurisystems-llms.txt
- group: other
  href: https://artifacts.apis.io/centaurisystems/hosts/centaurisystems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/centaurisystems-hosts.yml
- group: other
  href: https://artifacts.apis.io/centaurisystems/vendors/centaurisystems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/centaurisystems-vendors.yml
- group: build
  href: https://artifacts.apis.io/centaurisystems/packages/centaurisystems-packages.yml
  title: ''
  type: SDKs
  url: packages/centaurisystems-packages.yml
- group: build
  href: https://artifacts.apis.io/centaurisystems/packages/centaurisystems-packages.yml
  title: ''
  type: Packages
  url: packages/centaurisystems-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://centaurisystems.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://centaurisystems.io/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CentauriSystems
- group: auth
  href: https://artifacts.apis.io/centaurisystems/security/centaurisystems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/centaurisystems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://centaurisystems.io/
- group: docs
  title: ''
  type: Documentation
  url: https://centaurisystems.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://centaurisystems.io/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://centaurisystems.io/docs/quickstart
coverage:
  checked: '2026-10-16'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://centaurisystems.io/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-16'
description: Centauri Systems provides a developer portal platform and API tooling built for Apigee. Their solutions enable rapid deployment of branded developer portals, API productization, and integrated tooling such as AI‑driven page builders, pricing calculators, and multi‑org management. The company offers products like Launchpad and Aphelion, targeting enterprises seeking to accelerate API adoption on Google Cloud Marketplace.
image: https://centaurisystems.io/og-image-home.png
json_schemas:
- name: PostOauthTokenRequest
  property_count: 2
  slug: centaurisystems-post-oauth-token-request
- name: PostOauthTokenResponse
  property_count: 5
  slug: centaurisystems-post-oauth-token-response
jsonld:
- class_count: 2
  name: Centaurisystems Context
  property_count: 7
  slug: centaurisystems-context
layout: provider
modified: '2026-10-16'
name: Centauri Systems
nav: Providers
network: true
overview: 'Centauri Systems is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including OAuth API, Payments API, Users API, and 1 more. Tagged areas include Company, Developer Portal, API Tooling, Apigee, and Cloud Platform.


  The Centauri Systems catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Centauri Systems'' developer surface includes documentation, pricing, getting-started guide, and 16 more developer resources.'
plans:
- name: Centaurisystems Plans Pricing
  plan_count: 3
  slug: centaurisystems-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Centauri Systems API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: centaurisystems-rules
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 18.9
    developer_ergonomics: 17.9
    discoverability: 69.6
    operational_transparency: 2.6
  previous_composite: 33.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
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
screenshot: https://apis.io/screenshots/centaurisystems/centaurisystems-2026-11-03T123639.png
security:
- kind: domain-security
  name: Centaurisystems Domain Security
  slug: centaurisystems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: centaurisystems
tags:
- Company
- Developer Portal
- API Tooling
- Apigee
- Cloud Platform
website: https://centaurisystems.io/
---
