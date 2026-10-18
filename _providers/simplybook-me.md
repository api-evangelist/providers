---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: API documentation for SimplyBook.me
  name: SimplyBook.me API
  slug: simplybook-me-api-2
- description: The Admin API from SimplyBook.me — 2 operation(s) for admin.
  name: SimplyBook.me Admin API
  slug: simplybook-me-admin-api
artifact_total: 8
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/simplybook-me/refs/heads/main/plans/simplybook-me-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/simplybook-me-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/simplybook-me/refs/heads/main/rules/simplybook-me-rules.yml
  title: ''
  type: Spectral
  url: rules/simplybook-me-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/simplybook-me/refs/heads/main/json-ld/simplybook-me-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/simplybook-me-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/simplybook-me/refs/heads/main/vocabulary/simplybook-me-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/simplybook-me-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/simplybook-me/refs/heads/main/data-model/simplybook-me-data-model.yml
  title: ''
  type: DataModel
  url: data-model/simplybook-me-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/simplybook-me/refs/heads/main/conformance/simplybook-me-conformance.yml
  title: ''
  type: Conformance
  url: conformance/simplybook-me-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/simplybook-me/refs/heads/main/llms/simplybook-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/simplybook-me-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/simplybook-me/refs/heads/main/well-known/simplybook-me-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/simplybook-me-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/simplybook-me/refs/heads/main/hosts/simplybook-me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/simplybook-me-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/simplybook-me/refs/heads/main/vendors/simplybook-me-vendors.yml
  title: ''
  type: Vendors
  url: vendors/simplybook-me-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://simplybook.me/en/terms-and-conditions
- group: auth
  title: ''
  type: Security
  url: https://simplybook.me/en/legal/security
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/
- group: company
  title: ''
  type: Blog
  url: https://simplybook.me/en/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.simplybook.me/wiki/Getting_started
- group: docs
  title: ''
  type: Documentation
  url: https://help.simplybook.me/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/simplybook-me/refs/heads/main/security/simplybook-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/simplybook-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://simplybook.me
- group: start
  title: ''
  type: DeveloperPortal
  url: https://simplybook.me/en/developers
- group: docs
  title: ''
  type: APIReference
  url: https://simplybook.me/en/api/developer-api/tab/guide_api
- group: commercial
  title: ''
  type: Pricing
  url: https://simplybook.me/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://simplybook.me/en/default/registration
coverage:
  checked: '2026-10-13'
  detail: Help center API page provides HTML documentation but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://help.simplybook.me/wiki/API
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: SimplyBook.me provides an online appointment booking system for businesses of all sizes, offering features such as calendar synchronization, payment processing, AI voice booking, and extensive integrations with tools like Zapier, Facebook, and Instagram. The platform serves industries ranging from beauty and wellness to education, medical services, and fitness, delivering customizable booking pages, automated reminders, and analytics to help businesses streamline client scheduling and improve operational efficiency.
json_schemas:
- name: PostAdminWebhooksRequest
  property_count: 2
  slug: simplybook-me-post-admin-webhooks-request
- name: PostAdminWebhooksResponse
  property_count: 5
  slug: simplybook-me-post-admin-webhooks-response
jsonld:
- class_count: 2
  name: Simplybook Me Context
  property_count: 5
  slug: simplybook-me-context
layout: provider
modified: '2026-10-13'
name: SimplyBook.me
nav: Providers
network: true
overview: 'SimplyBook.me is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Admin API, and 1 more. Tagged areas include Scheduling, Software-as-a-Service, Booking, Integration, and Automation.


  The SimplyBook.me catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SimplyBook.me''s developer surface includes engineering blog, getting-started guide, documentation, API reference, pricing, signup flow, and 16 more developer resources.'
plans:
- name: Simplybook Me Plans Pricing
  plan_count: 5
  slug: simplybook-me-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: SimplyBook.me API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: simplybook-me-rules
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 61.8
    catalog_earned_first_party: 12.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 19.9
    developer_ergonomics: 45.2
    discoverability: 60.7
    operational_transparency: 10.5
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
    score: 20.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Simplybook Me Domain Security
  slug: simplybook-me-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: simplybook-me
tags:
- Scheduling
- Software-as-a-Service
- Booking
- Integration
- Automation
website: https://simplybook.me
---
