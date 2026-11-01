---
agent_readiness:
  band: agent-ready
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.feathr.co
  baseurl_source: declared
  description: 'Feathr API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: Feathr API
  slug: feathr-api
artifact_total: 11
asyncapis:
- description: ''
  name: Feathr Webhooks
  slug: feathr-webhooks
common:
- group: design
  href: https://artifacts.apis.io/feathr/rules/feathr-rules.yml
  title: ''
  type: Spectral
  url: rules/feathr-rules.yml
- group: design
  href: https://artifacts.apis.io/feathr/json-ld/feathr-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/feathr-context.jsonld
- group: design
  href: https://artifacts.apis.io/feathr/vocabulary/feathr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/feathr-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/feathr/asyncapi/feathr-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/feathr-webhooks.yml
- group: design
  href: https://artifacts.apis.io/feathr/data-model/feathr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/feathr-data-model.yml
- group: design
  href: https://artifacts.apis.io/feathr/conventions/feathr-conventions.yml
  title: ''
  type: Conventions
  url: conventions/feathr-conventions.yml
- group: auth
  href: https://artifacts.apis.io/feathr/authentication/feathr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/feathr-authentication.yml
- group: design
  href: https://artifacts.apis.io/feathr/conformance/feathr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/feathr-conformance.yml
- group: agent
  href: https://artifacts.apis.io/feathr/llms/feathr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/feathr-llms.txt
- group: other
  href: https://artifacts.apis.io/feathr/hosts/feathr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/feathr-hosts.yml
- group: other
  href: https://artifacts.apis.io/feathr/vendors/feathr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/feathr-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.feathr.co/terms
- group: operate
  title: ''
  type: Support
  url: https://help.feathr.co/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.feathr.co/privacy-policy?hsLang=en
- group: commercial
  title: ''
  type: Pricing
  url: https://www.feathr.co/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.feathr.co/resources/newsroom
- group: company
  title: ''
  type: Blog
  url: https://www.feathr.co/resources/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.feathr.co/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://dev.feathr.co/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Feathr
- group: auth
  href: https://artifacts.apis.io/feathr/security/feathr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/feathr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://feathr.co/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.feathr.co/openapi.json
  - status: 401
    url: https://developers.feathr.co/mcp
  - status: 200
    url: https://feathr.co/
  reason: partner-login
  state: gated
created: '2026-10-27'
description: Feathr provides a unified digital marketing platform that helps arts & culture organizations, associations, nonprofits, and mission‑driven partners engage audiences, automate email, run digital advertising, and track conversions. Their AI‑driven audience building tools simplify fundraising and event promotion, offering personalized pricing plans for organizations of any size.
image: https://www.feathr.co/hubfs/Feathr_Featured_logo-1200x600-show-up-where-it-matters.png
json_schemas:
- name: GetMeResponse
  property_count: 3
  slug: feathr-get-me-response
- name: GetPersonsIdResponse
  property_count: 26
  slug: feathr-get-persons-id-response
- name: GetPersonsResponse
  property_count: 4
  slug: feathr-get-persons-response
- name: PostWebhooksIdRotateSecretResponse
  property_count: 1
  slug: feathr-post-webhooks-id-rotate-secret-response
- name: PostWebhooksRequest
  property_count: 3
  slug: feathr-post-webhooks-request
jsonld:
- class_count: 5
  name: Feathr Context
  property_count: 35
  slug: feathr-context
layout: provider
modified: '2026-10-27'
name: Feathr
nav: Providers
network: true
overview: 'Feathr is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Marketing, AI, Nonprofit, and Event Promotion.


  The Feathr catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Feathr''s developer surface includes authentication, support, pricing, engineering blog, getting-started guide, documentation, and 16 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Feathr API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: feathr-rules
score:
  band: thin
  composite: 35.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 33.9
    developer_ergonomics: 40.5
    discoverability: 67.9
    operational_transparency: 13.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
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
  name: Feathr Authentication
  slug: feathr-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Feathr Domain Security
  slug: feathr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: feathr
tags:
- Company
- Digital Marketing
- AI
- Nonprofit
- Event Promotion
website: https://feathr.co/
---
