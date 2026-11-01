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
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.consensus.app
  baseurl_source: declared
  description: 'Consensus API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: Consensus API
  slug: consensus-app-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/consensus-app/plans/consensus-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/consensus-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/consensus-app/rules/consensus-app-rules.yml
  title: ''
  type: Spectral
  url: rules/consensus-app-rules.yml
- group: design
  href: https://artifacts.apis.io/consensus-app/json-ld/consensus-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/consensus-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/consensus-app/vocabulary/consensus-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/consensus-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/consensus-app/data-model/consensus-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/consensus-app-data-model.yml
- group: operate
  href: https://artifacts.apis.io/consensus-app/changelog/consensus-app-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/consensus-app-changelog.yml
- group: design
  href: https://artifacts.apis.io/consensus-app/conventions/consensus-app-conventions.yml
  title: ''
  type: Conventions
  url: conventions/consensus-app-conventions.yml
- group: auth
  href: https://artifacts.apis.io/consensus-app/authentication/consensus-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/consensus-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/consensus-app/conformance/consensus-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/consensus-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/consensus-app/llms/consensus-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/consensus-app-llms.txt
- group: other
  href: https://artifacts.apis.io/consensus-app/a2a/consensus-app-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/consensus-app-a2a.yml
- group: auth
  href: https://artifacts.apis.io/consensus-app/well-known/consensus-app-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/consensus-app-help-security.txt
- group: agent
  href: https://artifacts.apis.io/consensus-app/well-known/consensus-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/consensus-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/consensus-app/hosts/consensus-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/consensus-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/consensus-app/vendors/consensus-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/consensus-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://consensus.app/home/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://help.consensus.app
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://consensus.app/home/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://consensus.app/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://consensus.app/home/contact/media/
- group: other
  title: ''
  type: Leadership
  url: https://consensus.app/questions/leadership/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Consensus-NLP
- group: company
  title: ''
  type: Blog
  url: https://consensus.app/home/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.consensus.app/api-quickstart-search
- group: docs
  title: ''
  type: Documentation
  url: https://docs.consensus.app/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.consensus.app/llms.txt
- group: auth
  href: https://artifacts.apis.io/consensus-app/security/consensus-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/consensus-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://consensus.app
created: '2026-10-24'
description: 'Consensus is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by union-square-ventures) and added to the network as a stub for full-pipeline profiling.'
image: https://consensus.app/images/og-default.png
json_schemas:
- name: GetV1SearchResponse
  property_count: 5
  slug: consensus-app-get-v1-search-response
- name: GetV1ThreadsResponse
  property_count: 2
  slug: consensus-app-get-v1-threads-response
- name: PostV1ThreadsRequest
  property_count: 5
  slug: consensus-app-post-v1-threads-request
- name: PostV1ThreadsResponse
  property_count: 2
  slug: consensus-app-post-v1-threads-response
- name: PostV1ThreadsThreadidInteractionsRequest
  property_count: 5
  slug: consensus-app-post-v1-threads-threadid-interactions-request
- name: PostV1ThreadsThreadidInteractionsResponse
  property_count: 9
  slug: consensus-app-post-v1-threads-threadid-interactions-response
jsonld:
- class_count: 7
  name: Consensus App Context
  property_count: 20
  slug: consensus-app-context
layout: provider
modified: '2026-10-24'
name: Consensus
nav: Providers
network: true
overview: 'Consensus is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI and EducationalApplication.


  The Consensus catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Consensus'' developer surface includes changelog, authentication, support, pricing, engineering blog, getting-started guide, documentation, and 21 more developer resources.'
plans:
- name: Consensus App Plans Pricing
  plan_count: 5
  slug: consensus-app-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Consensus API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: consensus-app-rules
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 64.8
    catalog_earned_first_party: 12.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 35.6
    contract_quality: 26.2
    developer_ergonomics: 47.6
    discoverability: 51.8
    operational_transparency: 31.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
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
  name: Consensus App Authentication
  slug: consensus-app-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Consensus App Domain Security
  slug: consensus-app-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: consensus-app
tags:
- AI
- EducationalApplication
website: https://consensus.app
---
