---
agent_readiness:
  band: agent-ready
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
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'mellow-world API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: mellow-world API
  slug: mellow-world-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/mellow-world/plans/mellow-world-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mellow-world-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/mellow-world/rules/mellow-world-rules.yml
  title: ''
  type: Spectral
  url: rules/mellow-world-rules.yml
- group: design
  href: https://artifacts.apis.io/mellow-world/json-ld/mellow-world-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mellow-world-context.jsonld
- group: design
  href: https://artifacts.apis.io/mellow-world/vocabulary/mellow-world-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mellow-world-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/mellow-world/data-model/mellow-world-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mellow-world-data-model.yml
- group: design
  href: https://artifacts.apis.io/mellow-world/conventions/mellow-world-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/mellow-world-conventions.yml
- group: design
  href: https://artifacts.apis.io/mellow-world/conventions/mellow-world-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mellow-world-conventions.yml
- group: auth
  href: https://artifacts.apis.io/mellow-world/security/mellow-world-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/mellow-world-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mellow-world/authentication/mellow-world-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mellow-world-authentication.yml
- group: design
  href: https://artifacts.apis.io/mellow-world/conformance/mellow-world-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mellow-world-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mellow-world/llms/mellow-world-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mellow-world-llms.txt
- group: auth
  href: https://artifacts.apis.io/mellow-world/well-known/mellow-world-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mellow-world-security.txt
- group: auth
  href: https://artifacts.apis.io/mellow-world/well-known/mellow-world-mellow-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mellow-world-mellow-security.txt
- group: agent
  href: https://artifacts.apis.io/mellow-world/well-known/mellow-world-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mellow-world-well-known.yml
- group: other
  href: https://artifacts.apis.io/mellow-world/hosts/mellow-world-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mellow-world-hosts.yml
- group: other
  href: https://artifacts.apis.io/mellow-world/vendors/mellow-world-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mellow-world-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mellow.world/hub/prompts/chatgpt-dots-setup-checklist
- group: auth
  href: https://artifacts.apis.io/mellow-world/security/mellow-world-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mellow-world-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mellow-world/security/mellow-world-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mellow-world-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mellow.world/
- group: docs
  title: ''
  type: Documentation
  url: https://www.mellow.world/guides
- group: start
  title: ''
  type: Login
  url: https://www.mellow.world/hub/signin?return_to=%2Fhub%2Foverview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mellow.world/hub/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mellow.world/privacy
- group: start
  title: ''
  type: SignUp
  url: https://www.mellow.world/hub/signin?mode=signup&return_to=%2Fhub%2Foverview
- group: operate
  title: ''
  type: Support
  url: https://www.mellow.world/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mellow.world/terms
coverage:
  checked: '2026-10-31'
  detail: Documentation pages are HTML without machine‑readable OpenAPI or other contract files.
  evidence:
  - status: 200
    url: https://www.mellow.world/guides
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Mellow World provides a suite of social media management tools focused on Instagram, enabling users to schedule posts, create content calendars, and cross‑post to platforms like Threads. The service offers a free tier with basic scheduling and paid plans for higher volume, analytics, and team collaboration. Documentation includes guides, pricing details, support resources, and a privacy policy, all hosted at www.mellow.world.
image: https://www.mellow.world/og-hub-en.png
json_schemas:
- name: PostApiHubV1PostsRequest
  property_count: 5
  slug: mellow-world-post-api-hub-v1-posts-request
- name: PostApiHubV1PostsResponse
  property_count: 2
  slug: mellow-world-post-api-hub-v1-posts-response
- name: PostApiHubV1ValidateRequest
  property_count: 5
  slug: mellow-world-post-api-hub-v1-validate-request
- name: PostApiHubV1ValidateResponse
  property_count: 3
  slug: mellow-world-post-api-hub-v1-validate-response
jsonld:
- class_count: 4
  name: Mellow World Context
  property_count: 10
  slug: mellow-world-context
layout: provider
modified: '2026-10-30'
name: mellow-world
nav: Providers
network: true
overview: 'mellow-world is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social Media, Marketing, Scheduling, and Content Creation.


  The mellow-world catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  mellow-world''s developer surface includes authentication, getting-started guide, documentation, pricing, signup flow, support, and 21 more developer resources.'
plans:
- name: Mellow World Plans Pricing
  plan_count: 3
  slug: mellow-world-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: mellow-world API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: mellow-world-rules
score:
  band: developing
  composite: 40.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 22.1
    developer_ergonomics: 38.1
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Mellow World Authentication
  slug: mellow-world-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mellow World Domain Security
  slug: mellow-world-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mellow World Vulnerability Disclosure
  slug: mellow-world-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mellow-world
tags:
- Company
- Social Media
- Marketing
- Scheduling
- Content Creation
- SaaS
website: https://mellow.world/
---
