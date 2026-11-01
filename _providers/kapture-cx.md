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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Kapture’s APIs are organized around REST with predictable resource-oriented URLs, accept form-encoded request bodies, return JSON responses, and use standard HTTP.
  name: Kapture API
  slug: kapture-api
- description: 'Kapture CX API as documented publicly: 12 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Kapture CX API
  slug: kapture-cx-api
artifact_total: 15
common:
- group: other
  href: https://artifacts.apis.io/kapture-cx/vendors/kapture-cx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kapture-cx-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/kapture-cx/plans/kapture-cx-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kapture-cx-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/kapture-cx/rules/kapture-cx-rules.yml
  title: ''
  type: Spectral
  url: rules/kapture-cx-rules.yml
- group: design
  href: https://artifacts.apis.io/kapture-cx/json-ld/kapture-cx-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kapture-cx-context.jsonld
- group: design
  href: https://artifacts.apis.io/kapture-cx/vocabulary/kapture-cx-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kapture-cx-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/kapture-cx/data-model/kapture-cx-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kapture-cx-data-model.yml
- group: auth
  href: https://artifacts.apis.io/kapture-cx/authentication/kapture-cx-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kapture-cx-authentication.yml
- group: design
  href: https://artifacts.apis.io/kapture-cx/errors/kapture-cx-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kapture-cx-problem-types.yml
- group: design
  href: https://artifacts.apis.io/kapture-cx/conformance/kapture-cx-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kapture-cx-conformance.yml
- group: agent
  href: https://artifacts.apis.io/kapture-cx/llms/kapture-cx-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kapture-cx-llms.txt
- group: agent
  href: https://artifacts.apis.io/kapture-cx/well-known/kapture-cx-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kapture-cx-well-known.yml
- group: other
  href: https://artifacts.apis.io/kapture-cx/hosts/kapture-cx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kapture-cx-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.kapture.cx/trust-center/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kapture.cx/terms-and-conditions/
- group: company
  title: ''
  type: Newsroom
  url: https://www.kapture.cx/newsroom/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.kapture.cx/kapture-api
- group: docs
  title: ''
  type: Documentation
  url: https://dev.kapture.cx/
- group: auth
  href: https://artifacts.apis.io/kapture-cx/security/kapture-cx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kapture-cx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kapture.cx/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kapture.cx/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.kapture.cx/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.kapture.cx/demo/
- group: operate
  title: ''
  type: Support
  url: https://www.kapture.cx/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kapture.cx/privacy-policy/
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract is published; standard discovery paths on api.kapture.cx returned 404.
  evidence:
  - status: 404
    url: https://api.kapture.cx/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Kapture CX provides an AI‑powered customer experience platform that enables businesses to build, test, and deploy conversational agents across voice, chat, email, and social channels. The platform includes AgentOS with modules such as VITOS for agent building and COMMAND for human‑in‑the‑loop workflows, offering web and mobile interfaces for contact‑center operations.
image: https://www.kapture.cx/wp-content/uploads/2023/12/Kapture-Old-Logo.svg
json_schemas:
- name: PostEmployeeViewTaskDetailHtmlResponse
  property_count: 9
  slug: kapture-cx-post-employee-view-task-detail-html-response
- name: PostGetFaqContentsHtmlRequest
  property_count: 6
  slug: kapture-cx-post-get-faq-contents-html-request
- name: PostMsCustomerCustomerApiV1AddUpdateRequest
  property_count: 3
  slug: kapture-cx-post-ms-customer-customer-api-v1-add-update-request
- name: PostMsCustomerOrderApiV1AddUpdateRequest
  property_count: 4
  slug: kapture-cx-post-ms-customer-order-api-v1-add-update-request
- name: PostSearchTicketByTicketIdHtmlV20Request
  property_count: 10
  slug: kapture-cx-post-search-ticket-by-ticket-id-html-v20-request
- name: PostSelectCustomerBetweenStartAndEndDatesHtmlResponse
  property_count: 2
  slug: kapture-cx-post-select-customer-between-start-and-end-dates-html-response
jsonld:
- class_count: 8
  name: Kapture Cx Context
  property_count: 33
  slug: kapture-cx-context
layout: provider
modified: '2026-10-28'
name: Kapture CX
nav: Providers
network: true
overview: 'Kapture CX is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Customer Experience, CRM, AI, Automation, and Contact Center.


  The Kapture CX catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Kapture CX''s developer surface includes authentication, documentation, pricing, engineering blog, getting-started guide, support, and 18 more developer resources.'
plans:
- name: Kapture Cx Plans Pricing
  plan_count: 0
  slug: kapture-cx-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Kapture Cx Rate Limits
  slug: kapture-cx-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Kapture CX API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: kapture-cx-rules
scopes:
- name: Kapture Cx Scopes
  scope_count: 0
  slug: kapture-cx-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 57.0
    catalog_earned_first_party: 0.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 39.5
    contract_governance: 33.3
    contract_quality: 24.8
    developer_ergonomics: 50.0
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 10
      marker_coverage: 100.0
      total: 10
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Kapture Cx Authentication
  slug: kapture-cx-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Kapture Cx Domain Security
  slug: kapture-cx-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kapture-cx
tags:
- Customer Experience
- CRM
- AI
- Automation
- Contact Center
website: https://kapture.cx/
---
