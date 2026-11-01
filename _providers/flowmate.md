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
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'FlowMate API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: FlowMate API
  slug: flowmate-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/flowmate/plans/flowmate-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flowmate-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/flowmate/rules/flowmate-rules.yml
  title: ''
  type: Spectral
  url: rules/flowmate-rules.yml
- group: design
  href: https://artifacts.apis.io/flowmate/json-ld/flowmate-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/flowmate-context.jsonld
- group: design
  href: https://artifacts.apis.io/flowmate/vocabulary/flowmate-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/flowmate-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/flowmate/data-model/flowmate-data-model.yml
  title: ''
  type: DataModel
  url: data-model/flowmate-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.flowmate.io/trust
- group: auth
  href: https://artifacts.apis.io/flowmate/authentication/flowmate-authentication.yml
  title: ''
  type: Authentication
  url: authentication/flowmate-authentication.yml
- group: design
  href: https://artifacts.apis.io/flowmate/conformance/flowmate-conformance.yml
  title: ''
  type: Conformance
  url: conformance/flowmate-conformance.yml
- group: agent
  href: https://artifacts.apis.io/flowmate/llms/flowmate-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flowmate-llms.txt
- group: other
  href: https://artifacts.apis.io/flowmate/hosts/flowmate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flowmate-hosts.yml
- group: other
  href: https://artifacts.apis.io/flowmate/vendors/flowmate-vendors.yml
  title: ''
  type: Vendors
  url: vendors/flowmate-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FlowMate
- group: auth
  href: https://artifacts.apis.io/flowmate/security/flowmate-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/flowmate-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/flowmate/security/flowmate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flowmate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flowmate.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.flowmate.io/
- group: docs
  title: ''
  type: Documentation
  url: https://flowmate.gitbook.io/flowmate-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://api.flowmate.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.flowmate.io/signup
- group: company
  title: ''
  type: Blog
  url: https://www.flowmate.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.flowmate.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flowmate.io/general-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flowmate.io/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/flowmate/workspace
coverage:
  checked: '2026-10-20'
  detail: API documentation is provided as markdown pages without an OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://api.flowmate.io/llms.txt
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: FlowMate provides an automation layer that integrates large language model platforms such as Claude, ChatGPT, and Gemini into enterprise workflows. By allowing users to describe workflows in plain language, FlowMate builds and runs them across AI platforms, offering a unified execution engine. The service includes features like lead capture, real‑time automation, and a pricing model for SaaS and AI platforms, with documentation and support available through its website.
image: https://cdn.prod.website-files.com/6a5663cc904a71cc06198535/6a919fc4e835a7629e923dc4_og-home.png
json_schemas:
- name: DeleteFlowsIdResponse
  property_count: 4
  slug: flowmate-delete-flows-id-response
- name: GetUsersIdResponse
  property_count: 10
  slug: flowmate-get-users-id-response
- name: GetUsersResponse
  property_count: 10
  slug: flowmate-get-users-response
- name: GetUsersResponse2
  property_count: 10
  slug: flowmate-get-users-response2
- name: PostUsersRequest
  property_count: 10
  slug: flowmate-post-users-request
- name: PostUsersResponse
  property_count: 10
  slug: flowmate-post-users-response
jsonld:
- class_count: 14
  name: Flowmate Context
  property_count: 22
  slug: flowmate-context
layout: provider
modified: '2026-10-20'
name: FlowMate
nav: Providers
network: true
overview: 'FlowMate is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automation, Artificial Intelligence, Integration, and Workflows.


  The FlowMate catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FlowMate''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 18 more developer resources.'
plans:
- name: Flowmate Plans Pricing
  plan_count: 4
  slug: flowmate-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: FlowMate API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: flowmate-rules
score:
  band: developing
  composite: 44.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 24.1
    developer_ergonomics: 57.1
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Flowmate Authentication
  slug: flowmate-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Flowmate Domain Security
  slug: flowmate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Flowmate Trust Center
  slug: flowmate-trust-center
  summary_line: SOC 2, GDPR
slug: flowmate
tags:
- Company
- Automation
- Artificial Intelligence
- Integration
- Workflows
website: https://flowmate.io/
---
