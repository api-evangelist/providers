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
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api-india-1.fieldproxy.ai
  baseurl_source: declared
  description: 'Fieldproxy API as documented publicly: 17 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: Fieldproxy API
  slug: fieldproxy-ai-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/fieldproxy-ai/rules/fieldproxy-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/fieldproxy-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/fieldproxy-ai/json-ld/fieldproxy-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fieldproxy-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/fieldproxy-ai/vocabulary/fieldproxy-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fieldproxy-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/fieldproxy-ai/data-model/fieldproxy-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fieldproxy-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/fieldproxy-ai/authentication/fieldproxy-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fieldproxy-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/fieldproxy-ai/conformance/fieldproxy-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fieldproxy-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fieldproxy-ai/llms/fieldproxy-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fieldproxy-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/fieldproxy-ai/well-known/fieldproxy-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fieldproxy-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/fieldproxy-ai/hosts/fieldproxy-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fieldproxy-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/fieldproxy-ai/vendors/fieldproxy-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fieldproxy-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fieldproxy.ai/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://support.fieldproxy.ai/report
- group: auth
  title: ''
  type: Security
  url: https://www.fieldproxy.ai/industries/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fieldproxy.ai/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fieldproxy.ai/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://www.fieldproxy.ai/guides
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.fieldproxy.ai/developers
- group: company
  title: ''
  type: Blog
  url: https://www.fieldproxy.ai/resources/blog
- group: docs
  title: ''
  type: APIReference
  url: https://www.fieldproxy.ai/developers/docs
- group: auth
  href: https://artifacts.apis.io/fieldproxy-ai/security/fieldproxy-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fieldproxy-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fieldproxy.ai
coverage:
  checked: '2026-10-27'
  detail: Developer pages are rendered via JavaScript and provide no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.fieldproxy.ai/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Fieldproxy provides AI‑powered field service software that configures around a customer’s existing workflows, integrating job dispatch, scheduling, invoicing and customer portals into a single system. The platform is aimed at field service businesses and enterprises that need to manage technicians, jobs, assets and payments, offering unlimited users with a single price and multilingual support.
image: https://www.fieldproxy.ai/og-default.png
json_schemas:
- name: PostApiDeleteRequest
  property_count: 2
  slug: fieldproxy-ai-post-api-delete-request
- name: PostApiInsertRequest
  property_count: 2
  slug: fieldproxy-ai-post-api-insert-request
- name: PostApiReadRequest
  property_count: 2
  slug: fieldproxy-ai-post-api-read-request
- name: PostApiReadResponse
  property_count: 4
  slug: fieldproxy-ai-post-api-read-response
- name: PostApiUpdateRequest
  property_count: 3
  slug: fieldproxy-ai-post-api-update-request
- name: PostAuthOrgResponse
  property_count: 4
  slug: fieldproxy-ai-post-auth-org-response
jsonld:
- class_count: 9
  name: Fieldproxy Ai Context
  property_count: 11
  slug: fieldproxy-ai-context
layout: provider
modified: '2026-10-27'
name: Fieldproxy
nav: Providers
network: true
overview: 'Fieldproxy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Field Service Software, AI, Scheduling, Dispatch, and Invoicing.


  The Fieldproxy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Fieldproxy''s developer surface includes authentication, support, pricing, documentation, engineering blog, API reference, and 15 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Fieldproxy API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: fieldproxy-ai-rules
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 26.1
    developer_ergonomics: 45.2
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
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
  name: Fieldproxy Ai Authentication
  slug: fieldproxy-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Fieldproxy Ai Domain Security
  slug: fieldproxy-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fieldproxy-ai
tags:
- Field Service Software
- AI
- Scheduling
- Dispatch
- Invoicing
- Customer Portal
- Multi‑language
website: https://fieldproxy.ai
---
