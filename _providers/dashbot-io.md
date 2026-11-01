---
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Conversational analytics API providing endpoints for exporting data, intents, events, and tracker information.
  name: Dashbot API
  slug: dashbot-api
- baseURL: https://api.dimensionlabs.io
  baseurl_source: declared
  description: 'Dashbot API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-10-25); not the provider''s own document.'
  name: Dashbot API
  slug: dashbot-io-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/dashbot-io/plans/dashbot-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dashbot-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dashbot-io/rules/dashbot-io-rules.yml
  title: ''
  type: Spectral
  url: rules/dashbot-io-rules.yml
- group: design
  href: https://artifacts.apis.io/dashbot-io/json-ld/dashbot-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dashbot-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/dashbot-io/vocabulary/dashbot-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dashbot-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dashbot-io/data-model/dashbot-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dashbot-io-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.dimensionlabs.io/
- group: design
  href: https://artifacts.apis.io/dashbot-io/conformance/dashbot-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dashbot-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dashbot-io/llms/dashbot-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dashbot-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/dashbot-io/well-known/dashbot-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dashbot-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/dashbot-io/hosts/dashbot-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dashbot-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/dashbot-io/vendors/dashbot-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dashbot-io-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.dimensionlabs.io/security
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dimensionlabs.io/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.dimensionlabs.io/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dimensionlabs.io/get-started/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dashbot.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ada.cx/reference/data-export/overview
- group: auth
  href: https://artifacts.apis.io/dashbot-io/security/dashbot-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dashbot-io-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/dashbot-io/security/dashbot-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dashbot-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dashbot.io/
coverage:
  checked: '2026-10-25'
  detail: Documentation provides markdown pages but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://docs.dimensionlabs.io/api.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: Dashbot provides AI-powered conversational analytics, turning chat logs, voice transcripts, and survey data into structured insights. Their platform helps businesses understand customer sentiment, identify churn drivers, and improve agent performance through real-time dashboards and automated reporting. Founded with backing from Bessemer Venture Partners, Dashbot serves enterprises across contact centers, SaaS, and e‑commerce, offering integrations with popular messaging and voice platforms.
image: https://www.dimensionlabs.io/og/default.jpg?v=2026-10-12b
json_schemas:
- name: GetExportResponse
  property_count: 1
  slug: dashbot-io-get-export-response
- name: PostLandingRequest
  property_count: 7
  slug: dashbot-io-post-landing-request
- name: PostRequest
  property_count: 4
  slug: dashbot-io-post-request
- name: PostTrackRequest
  property_count: 8
  slug: dashbot-io-post-track-request
- name: PostTrackResponse
  property_count: 8
  slug: dashbot-io-post-track-response
- name: PostTrackhistoricalRequest
  property_count: 6
  slug: dashbot-io-post-trackhistorical-request
jsonld:
- class_count: 7
  name: Dashbot Io Context
  property_count: 17
  slug: dashbot-io-context
layout: provider
modified: '2026-10-25'
name: Dashbot
nav: Providers
network: true
overview: 'Dashbot is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI analytics, Customer conversation analytics, Voice of Customer, Revenue intelligence, and Contact center analytics.


  The Dashbot catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dashbot''s developer surface includes pricing, changelog, getting-started guide, documentation, API reference, and 15 more developer resources.'
plans:
- name: Dashbot Io Plans Pricing
  plan_count: 5
  slug: dashbot-io-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Dashbot API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 1
  slug: dashbot-io-rules
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 57.9
    contract_governance: 35.6
    contract_quality: 25.9
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 26.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dashbot Io Domain Security
  slug: dashbot-io-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Dashbot Io Trust Center
  slug: dashbot-io-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: dashbot-io
tags:
- AI analytics
- Customer conversation analytics
- Voice of Customer
- Revenue intelligence
- Contact center analytics
- SaaS
website: https://www.dashbot.io/
---
