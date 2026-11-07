---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 19.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Accoil provides product engagement analytics for B2B SaaS, with documentation covering getting started, connections, configuration, accounts, workspaces, features, activation, segments, dashboards, fe
  name: Accoil API
  slug: accoil-api-2
- baseURL: https://in.accoil.com
  baseurl_source: declared
  description: 'Accoil API as documented publicly: 17 operations. Contract generated from the documentation by API Evangelist (2026-10-26); not the provider''s own document.'
  name: Accoil API
  slug: accoil-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/accoil/plans/accoil-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/accoil-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/accoil/rules/accoil-rules.yml
  title: ''
  type: Spectral
  url: rules/accoil-rules.yml
- group: design
  href: https://artifacts.apis.io/accoil/json-ld/accoil-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/accoil-context.jsonld
- group: design
  href: https://artifacts.apis.io/accoil/vocabulary/accoil-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/accoil-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/accoil/data-model/accoil-data-model.yml
  title: ''
  type: DataModel
  url: data-model/accoil-data-model.yml
- group: design
  href: https://artifacts.apis.io/accoil/conventions/accoil-conventions.yml
  title: ''
  type: Conventions
  url: conventions/accoil-conventions.yml
- group: auth
  href: https://artifacts.apis.io/accoil/authentication/accoil-authentication.yml
  title: ''
  type: Authentication
  url: authentication/accoil-authentication.yml
- group: design
  href: https://artifacts.apis.io/accoil/conformance/accoil-conformance.yml
  title: ''
  type: Conformance
  url: conformance/accoil-conformance.yml
- group: agent
  href: https://artifacts.apis.io/accoil/llms/accoil-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/accoil-llms.txt
- group: other
  href: https://artifacts.apis.io/accoil/hosts/accoil-hosts.yml
  title: ''
  type: Hosts
  url: hosts/accoil-hosts.yml
- group: other
  href: https://artifacts.apis.io/accoil/vendors/accoil-vendors.yml
  title: ''
  type: Vendors
  url: vendors/accoil-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.accoil.com/terms
- group: operate
  title: ''
  type: Support
  url: https://www.accoil.com/solutions/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.accoil.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.accoil.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.accoil.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://developer.accoil.com/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.accoil.com/docs/quick-start/rest-api
- group: docs
  title: ''
  type: Documentation
  url: https://developer.accoil.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Accoil
- group: auth
  href: https://artifacts.apis.io/accoil/security/accoil-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/accoil-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.accoil.com/
coverage:
  checked: '2026-10-26'
  detail: Documentation is HTML only and provides no OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://docs.accoil.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Accoil builds AI‑enabled onboarding, customer‑success, and account‑management solutions for B2B software companies, helping teams grow revenue from existing customers. The consultancy offers tailored consulting, tooling, and services to expand retention and expansion.
image: https://www.accoil.com/images/og-home-services.png
json_schemas:
- name: GetV1AccountsResponse
  property_count: 4
  slug: accoil-get-v1-accounts-response
- name: GetV2AccountsResponse
  property_count: 4
  slug: accoil-get-v2-accounts-response
- name: GetV2SegmentsIdMembersResponse
  property_count: 4
  slug: accoil-get-v2-segments-id-members-response
- name: GetV2SegmentsResponse
  property_count: 4
  slug: accoil-get-v2-segments-response
- name: GetV2UsersResponse
  property_count: 4
  slug: accoil-get-v2-users-response
- name: GetV2WorkspacesResponse
  property_count: 4
  slug: accoil-get-v2-workspaces-response
jsonld:
- class_count: 13
  name: Accoil Context
  property_count: 11
  slug: accoil-context
layout: provider
modified: '2026-10-26'
name: Accoil
nav: Providers
network: true
overview: 'Accoil is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Retention, Expansion, Customer Success, Playbooks, and Analytics.


  The Accoil catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Accoil''s developer surface includes authentication, support, pricing, engineering blog, API reference, getting-started guide, documentation, and 15 more developer resources.'
plans:
- name: Accoil Plans Pricing
  plan_count: 3
  slug: accoil-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Accoil API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: accoil-rules
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 69.0
    catalog_earned_first_party: 12.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 47.4
    contract_governance: 19.7
    contract_quality: 26.0
    developer_ergonomics: 29.8
    discoverability: 64.3
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 38.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/accoil/accoil-2026-11-03T120151.png
security:
- kind: authentication
  name: Accoil Authentication
  slug: accoil-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Accoil Domain Security
  slug: accoil-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: accoil
tags:
- Retention
- Expansion
- Customer Success
- Playbooks
- Analytics
website: https://www.accoil.com/
---
