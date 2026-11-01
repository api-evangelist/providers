---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://transaction-tax.api.in.commenda.io
  baseurl_source: declared
  description: 'Commenda API as documented publicly: 53 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: Commenda API
  slug: commenda-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/commenda/rules/commenda-rules.yml
  title: ''
  type: Spectral
  url: rules/commenda-rules.yml
- group: design
  href: https://artifacts.apis.io/commenda/json-ld/commenda-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/commenda-context.jsonld
- group: design
  href: https://artifacts.apis.io/commenda/vocabulary/commenda-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/commenda-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/commenda/data-model/commenda-data-model.yml
  title: ''
  type: DataModel
  url: data-model/commenda-data-model.yml
- group: design
  href: https://artifacts.apis.io/commenda/conformance/commenda-conformance.yml
  title: ''
  type: Conformance
  url: conformance/commenda-conformance.yml
- group: agent
  href: https://artifacts.apis.io/commenda/llms/commenda-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/commenda-llms.txt
- group: other
  href: https://artifacts.apis.io/commenda/a2a/commenda-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/commenda-a2a.yml
- group: agent
  href: https://artifacts.apis.io/commenda/well-known/commenda-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/commenda-well-known.yml
- group: other
  href: https://artifacts.apis.io/commenda/hosts/commenda-hosts.yml
  title: ''
  type: Hosts
  url: hosts/commenda-hosts.yml
- group: other
  href: https://artifacts.apis.io/commenda/vendors/commenda-vendors.yml
  title: ''
  type: Vendors
  url: vendors/commenda-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.commenda.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.commenda.io/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.commenda.io/auth/signin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/commenda-eng
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.commenda.io/introduction/quickstart
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.commenda.io/changelog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.commenda.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.commenda.io/llms.txt
- group: auth
  href: https://artifacts.apis.io/commenda/security/commenda-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/commenda-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.commenda.io/
- group: company
  title: ''
  type: Blog
  url: https://www.commenda.io/blog
coverage:
  checked: '2026-10-20'
  detail: The documentation site loads content via JavaScript and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.commenda.io
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-20'
description: Commenda provides an AI‑native global compliance platform that helps businesses manage entity formation, local director services, registered address, compliance calendars, indirect tax, transfer pricing and accounting across 70+ countries. The platform integrates AI to automate data collection, reporting and regulatory filing, offering tools for startups, mid‑market and enterprise customers to stay compliant worldwide.
image: https://assets.commenda.io/website/og/commenda-opengraph-default-v2.webp
json_schemas:
- name: GetApiV1RegistrationsRegistrationidResponse
  property_count: 23
  slug: commenda-get-api-v1-registrations-registrationid-response
- name: GetApiV1RegistrationsV27C9E6679742540De944BE07Fc1F90Ae7Respo
  property_count: 1
  slug: commenda-get-api-v1-registrations-v27-c9-e6679742540-de944-be07-fc1-f90-ae7-respo
- name: PostApiV1RegistrationsListResponse
  property_count: 2
  slug: commenda-post-api-v1-registrations-list-response
- name: PostApiV1RegistrationsRequest
  property_count: 6
  slug: commenda-post-api-v1-registrations-request
- name: PostApiV1RegistrationsV2ListResponse
  property_count: 1
  slug: commenda-post-api-v1-registrations-v2-list-response
- name: PostWebhooksRequest
  property_count: 6
  slug: commenda-post-webhooks-request
jsonld:
- class_count: 21
  name: Commenda Context
  property_count: 37
  slug: commenda-context
layout: provider
modified: '2026-10-20'
name: Commenda
nav: Providers
network: true
overview: 'Commenda is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Compliance, Global, and Tax.


  The Commenda catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Commenda''s developer surface includes getting-started guide, changelog, documentation, API reference, engineering blog, and 16 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Commenda API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: commenda-rules
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: unknown
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
- kind: domain-security
  name: Commenda Domain Security
  slug: commenda-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: commenda
tags:
- Company
- AI
- Compliance
- Global
- Tax
website: https://www.commenda.io/
---
