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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
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
  score: 29.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.dcal.ai
  baseurl_source: declared
  description: 'Dapta API as documented publicly: 35 operations. Contract generated from the documentation by API Evangelist (2026-10-25); not the provider''s own document.'
  name: Dapta API
  slug: daptatech-com-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/daptatech-com/plans/daptatech-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/daptatech-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/daptatech-com/rules/daptatech-com-rules.yml
  title: ''
  type: Spectral
  url: rules/daptatech-com-rules.yml
- group: design
  href: https://artifacts.apis.io/daptatech-com/json-ld/daptatech-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/daptatech-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/daptatech-com/vocabulary/daptatech-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/daptatech-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/daptatech-com/data-model/daptatech-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/daptatech-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/daptatech-com/conventions/daptatech-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/daptatech-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/daptatech-com/conventions/daptatech-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/daptatech-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/daptatech-com/authentication/daptatech-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/daptatech-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/daptatech-com/conformance/daptatech-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/daptatech-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/daptatech-com/llms/daptatech-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/daptatech-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/daptatech-com/well-known/daptatech-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/daptatech-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/daptatech-com/hosts/daptatech-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/daptatech-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/daptatech-com/vendors/daptatech-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/daptatech-com-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://auth.dapta.ai/sign-up
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dapta.ai/quick-setup
- group: auth
  href: https://artifacts.apis.io/daptatech-com/security/daptatech-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/daptatech-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://daptatech.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dapta.ai
- group: company
  title: ''
  type: Blog
  url: https://dapta.ai/blog-posts
- group: commercial
  title: ''
  type: Pricing
  url: https://dapta.ai/pricing
- group: operate
  title: ''
  type: Support
  url: https://dapta.ai/contact-us
created: '2026-10-25'
description: Dapta AI provides AI-powered voice and text agents designed to automate sales and customer engagement for small and medium businesses. Their platform offers AI voice agents that answer calls, qualify leads, and book meetings, as well as AI text agents for SMS and web chat, WhatsApp, and other channels. With tools like AI notetaker, smart forms, and workflow automation, Dapta aims to boost sales efficiency by up to 70% and streamline business operations across various industries.
image: https://dapta.ai/wp-content/uploads/2025/02/og-tag.jpg?wsr
json_schemas:
- name: GetDcalBookingsConfirmOrDeclineMdResponse
  property_count: 1
  slug: daptatech-com-get-dcal-bookings-confirm-or-decline-md-response
- name: GetDformsDesignClientLogosMdResponse
  property_count: 1
  slug: daptatech-com-get-dforms-design-client-logos-md-response
- name: GetV1PublicPagesAccountcodeResponse
  property_count: 5
  slug: daptatech-com-get-v1-public-pages-accountcode-response
- name: PostV1PublicFormsAccountcodeSlugEventsRequest
  property_count: 4
  slug: daptatech-com-post-v1-public-forms-accountcode-slug-events-request
- name: PostV1PublicFormsAccountcodeSlugSubmissionsRequest
  property_count: 6
  slug: daptatech-com-post-v1-public-forms-accountcode-slug-submissions-request
- name: PostV1PublicFormsAccountcodeSlugUploadsRequest
  property_count: 5
  slug: daptatech-com-post-v1-public-forms-accountcode-slug-uploads-request
jsonld:
- class_count: 7
  name: Daptatech Com Context
  property_count: 20
  slug: daptatech-com-context
layout: provider
modified: '2026-10-25'
name: Dapta
nav: Providers
network: true
overview: 'Dapta is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, SalesAutomation, VoiceAgents, and TextAgents.


  The Dapta catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dapta''s developer surface includes authentication, signup flow, getting-started guide, documentation, engineering blog, pricing, support, and 14 more developer resources.'
plans:
- name: Daptatech Com Plans Pricing
  plan_count: 5
  slug: daptatech-com-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Dapta API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: daptatech-com-rules
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 26.0
    developer_ergonomics: 40.5
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 13
      marker_coverage: 100.0
      total: 13
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Daptatech Com Authentication
  slug: daptatech-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Daptatech Com Domain Security
  slug: daptatech-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: daptatech-com
tags:
- Company
- AI
- SalesAutomation
- VoiceAgents
- TextAgents
website: https://daptatech.com
---
