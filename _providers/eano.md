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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Eano API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: Eano API
  slug: eano-api
artifact_total: 11
asyncapis:
- description: ''
  name: Eano Webhooks
  slug: eano-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/eano/plans/eano-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/eano-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/eano/rules/eano-rules.yml
  title: ''
  type: Spectral
  url: rules/eano-rules.yml
- group: design
  href: https://artifacts.apis.io/eano/json-ld/eano-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/eano-context.jsonld
- group: design
  href: https://artifacts.apis.io/eano/vocabulary/eano-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/eano-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/eano/asyncapi/eano-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/eano-webhooks.yml
- group: design
  href: https://artifacts.apis.io/eano/data-model/eano-data-model.yml
  title: ''
  type: DataModel
  url: data-model/eano-data-model.yml
- group: auth
  href: https://artifacts.apis.io/eano/authentication/eano-authentication.yml
  title: ''
  type: Authentication
  url: authentication/eano-authentication.yml
- group: design
  href: https://artifacts.apis.io/eano/conformance/eano-conformance.yml
  title: ''
  type: Conformance
  url: conformance/eano-conformance.yml
- group: agent
  href: https://artifacts.apis.io/eano/llms/eano-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/eano-llms.txt
- group: auth
  href: https://artifacts.apis.io/eano/well-known/eano-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/eano-help-security.txt
- group: agent
  href: https://artifacts.apis.io/eano/well-known/eano-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/eano-well-known.yml
- group: other
  href: https://artifacts.apis.io/eano/hosts/eano-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eano-hosts.yml
- group: other
  href: https://artifacts.apis.io/eano/vendors/eano-vendors.yml
  title: ''
  type: Vendors
  url: vendors/eano-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eano.com/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://help.eano.com/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eano.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.eano.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.eano.com/pro/login
- group: company
  title: ''
  type: Blog
  url: https://www.eano.com/resources/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.eano.com/en/articles/16040854-project-templates-bundling-your-scope-milestones-and-tasks-into-one-reusable-setup
- group: docs
  title: ''
  type: Documentation
  url: https://developer.eano.com/
- group: auth
  href: https://artifacts.apis.io/eano/security/eano-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eano-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eano.com/
coverage:
  checked: '2026-10-24'
  detail: Provider documentation pages are HTML without any published OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://developer.eano.com/docs/getting-started/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-24'
description: Eano provides an all‑in‑one residential construction project management platform that combines AI‑driven estimating, sales, project tracking, and financial tools. The SaaS solution helps general contractors, remodelers, and home‑builders manage estimates, proposals, change orders, vendor management, and client communication in a single cloud‑based system. Features include AI‑assisted takeoffs, video estimations, CRM, budgeting, integrations with QuickBooks, and a client dashboard for real‑time project visibility.
image: https://cdn.prod.website-files.com/670d5a126bda66dca6cdabeb/672174e1cad37880075a2860_webclip.jpg
json_schemas:
- name: GetApiV1ExternalBidsResponse
  property_count: 13
  slug: eano-get-api-v1-external-bids-response
- name: GetApiV1ExternalProjectsIdResponse
  property_count: 3
  slug: eano-get-api-v1-external-projects-id-response
- name: PostApiV1ExternalProjectsRequest
  property_count: 5
  slug: eano-post-api-v1-external-projects-request
- name: PostApiV1ExternalProjectsResponse
  property_count: 3
  slug: eano-post-api-v1-external-projects-response
jsonld:
- class_count: 4
  name: Eano Context
  property_count: 10
  slug: eano-context
layout: provider
modified: '2026-10-24'
name: Eano
nav: Providers
network: true
overview: 'Eano is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Construction, SaaS, Project Management, AI, and Residential.


  The Eano catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Eano''s developer surface includes authentication, support, pricing, engineering blog, getting-started guide, documentation, and 17 more developer resources.'
plans:
- name: Eano Plans Pricing
  plan_count: 9
  slug: eano-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Eano API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: eano-rules
score:
  band: developing
  composite: 42.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 29.9
    developer_ergonomics: 40.5
    discoverability: 57.1
    operational_transparency: 18.4
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
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Eano Authentication
  slug: eano-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Eano Domain Security
  slug: eano-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: eano
tags:
- Construction
- SaaS
- Project Management
- AI
- Residential
website: https://www.eano.com/
---
