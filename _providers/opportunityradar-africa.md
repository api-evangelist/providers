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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Read‑only public feed of opportunities across East Africa.
  name: OpportunityRadar API
  slug: opportunityradar-api
- baseURL: https://api.opportunityradar.africa
  baseurl_source: declared
  description: 'opportunityradar-africa API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: opportunityradar-africa API
  slug: opportunityradar-africa-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/opportunityradar-africa/rules/opportunityradar-africa-rules.yml
  title: ''
  type: Spectral
  url: rules/opportunityradar-africa-rules.yml
- group: design
  href: https://artifacts.apis.io/opportunityradar-africa/json-ld/opportunityradar-africa-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/opportunityradar-africa-context.jsonld
- group: design
  href: https://artifacts.apis.io/opportunityradar-africa/vocabulary/opportunityradar-africa-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/opportunityradar-africa-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/opportunityradar-africa/data-model/opportunityradar-africa-data-model.yml
  title: ''
  type: DataModel
  url: data-model/opportunityradar-africa-data-model.yml
- group: design
  href: https://artifacts.apis.io/opportunityradar-africa/conventions/opportunityradar-africa-conventions.yml
  title: ''
  type: Conventions
  url: conventions/opportunityradar-africa-conventions.yml
- group: auth
  href: https://artifacts.apis.io/opportunityradar-africa/authentication/opportunityradar-africa-authentication.yml
  title: ''
  type: Authentication
  url: authentication/opportunityradar-africa-authentication.yml
- group: design
  href: https://artifacts.apis.io/opportunityradar-africa/conformance/opportunityradar-africa-conformance.yml
  title: ''
  type: Conformance
  url: conformance/opportunityradar-africa-conformance.yml
- group: other
  href: https://artifacts.apis.io/opportunityradar-africa/hosts/opportunityradar-africa-hosts.yml
  title: ''
  type: Hosts
  url: hosts/opportunityradar-africa-hosts.yml
- group: company
  title: ''
  type: Blog
  url: https://opportunityradar.africa/blog/
- group: auth
  href: https://artifacts.apis.io/opportunityradar-africa/security/opportunityradar-africa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opportunityradar-africa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opportunityradar.africa/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://opportunityradar.africa/developers.html
- group: docs
  title: ''
  type: Documentation
  url: https://opportunityradar.africa/developers.html
- group: docs
  title: ''
  type: APIReference
  url: https://opportunityradar.africa/developers.html
- group: start
  title: ''
  type: GettingStarted
  url: https://opportunityradar.africa/developers.html
- group: operate
  title: ''
  type: Support
  url: https://opportunityradar.africa/contact.html
- group: commercial
  title: ''
  type: Pricing
  url: https://opportunityradar.africa/pricing.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://opportunityradar.africa/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://opportunityradar.africa/privacy.html
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI or other machine‑readable contract found at standard locations despite public API documentation.
  evidence:
  - status: 404
    url: https://api.opportunityradar.africa/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: OpportunityRadar is an East African platform that aggregates and makes accessible jobs, tenders, grants, scholarships and other opportunities across Uganda, Kenya, Tanzania, Rwanda and Ethiopia. It provides a free daily Telegram alert service, keyword search, and a cover‑letter helper, aiming to democratize access to opportunities for users with limited internet connectivity.
json_schemas:
- name: GetApiOpportunitiesResponse
  property_count: 7
  slug: opportunityradar-africa-get-api-opportunities-response
jsonld:
- class_count: 1
  name: Opportunityradar Africa Context
  property_count: 6
  slug: opportunityradar-africa-context
layout: provider
modified: '2026-10-29'
name: opportunityradar-africa
nav: Providers
network: true
overview: 'opportunityradar-africa is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Opportunity, Africa, Jobs, and Tenders.


  The opportunityradar-africa catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  opportunityradar-africa''s developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, support, pricing, and 12 more developer resources.'
plans:
- name: Opportunityradar Africa Plans Pricing
  plan_count: 0
  slug: opportunityradar-africa-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Opportunityradar Africa Rate Limits
  slug: opportunityradar-africa-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: opportunityradar-africa API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: opportunityradar-africa-rules
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 51.2
    catalog_earned_first_party: 0.0
    catalog_gap: 63.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 19.0
    developer_ergonomics: 57.1
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Opportunityradar Africa Authentication
  slug: opportunityradar-africa-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Opportunityradar Africa Domain Security
  slug: opportunityradar-africa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: opportunityradar-africa
tags:
- Company
- Opportunity
- Africa
- Jobs
- Tenders
- Grants
- Technology
website: https://opportunityradar.africa/
---
