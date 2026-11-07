---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Bud Ecosystem provides an Enterprise AI Operating System with APIs documented at https://docs.budecosystem.com/.
  name: Bud Ecosystem API
  slug: bud-ecosystem-api
- baseURL: https://gateway.bud.studio
  baseurl_source: declared
  description: 'Bud Ecosystem API as documented publicly: 31 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: Bud Ecosystem API
  slug: budecosystem-api
artifact_total: 13
asyncapis:
- description: ''
  name: Budecosystem Webhooks
  slug: budecosystem-webhooks
common:
- group: design
  href: https://artifacts.apis.io/budecosystem/rules/budecosystem-rules.yml
  title: ''
  type: Spectral
  url: rules/budecosystem-rules.yml
- group: design
  href: https://artifacts.apis.io/budecosystem/json-ld/budecosystem-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/budecosystem-context.jsonld
- group: design
  href: https://artifacts.apis.io/budecosystem/vocabulary/budecosystem-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/budecosystem-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/budecosystem/asyncapi/budecosystem-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/budecosystem-webhooks.yml
- group: design
  href: https://artifacts.apis.io/budecosystem/data-model/budecosystem-data-model.yml
  title: ''
  type: DataModel
  url: data-model/budecosystem-data-model.yml
- group: operate
  href: https://artifacts.apis.io/budecosystem/changelog/budecosystem-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/budecosystem-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.budecosystem.com/trust
- group: design
  href: https://artifacts.apis.io/budecosystem/conformance/budecosystem-conformance.yml
  title: ''
  type: Conformance
  url: conformance/budecosystem-conformance.yml
- group: agent
  href: https://artifacts.apis.io/budecosystem/llms/budecosystem-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/budecosystem-llms.txt
- group: other
  href: https://artifacts.apis.io/budecosystem/a2a/budecosystem-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/budecosystem-a2a.yml
- group: agent
  href: https://artifacts.apis.io/budecosystem/well-known/budecosystem-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/budecosystem-well-known.yml
- group: other
  href: https://artifacts.apis.io/budecosystem/hosts/budecosystem-hosts.yml
  title: ''
  type: Hosts
  url: hosts/budecosystem-hosts.yml
- group: other
  href: https://artifacts.apis.io/budecosystem/vendors/budecosystem-vendors.yml
  title: ''
  type: Vendors
  url: vendors/budecosystem-vendors.yml
- group: build
  href: https://artifacts.apis.io/budecosystem/packages/budecosystem-packages.yml
  title: ''
  type: SDKs
  url: packages/budecosystem-packages.yml
- group: build
  href: https://artifacts.apis.io/budecosystem/packages/budecosystem-packages.yml
  title: ''
  type: Packages
  url: packages/budecosystem-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://budecosystem.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://budecosystem.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://budecosystem.com/news
- group: other
  title: ''
  type: Leadership
  url: https://budecosystem.com/leadership
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.budecosystem.com/getting-started/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.budecosystem.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BudEcosystem
- group: auth
  href: https://artifacts.apis.io/budecosystem/security/budecosystem-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/budecosystem-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/budecosystem/security/budecosystem-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/budecosystem-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://budecosystem.com/
- group: company
  title: ''
  type: Blog
  url: https://budecosystem.com/blog
coverage:
  checked: '2026-10-19'
  detail: Documentation pages are rendered via JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.budecosystem.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-19'
description: Bud Ecosystem provides an Enterprise AI Operating System that unifies silicon, agents, training, inference, routing, guardrails, and governance on a sovereign platform. It offers Bud Novaria for datacenter and cloud, and Bud Gaia for personal AI, delivering integrated AI stack across tools and layers to accelerate enterprise AI value.
image: https://budecosystem.com/assets/social/og-default.png
json_schemas:
- name: GetV1BatchesBatchAbc123Response
  property_count: 20
  slug: budecosystem-get-v1-batches-batch-abc123-response
- name: GetV1FilesFileAbc123Response
  property_count: 8
  slug: budecosystem-get-v1-files-file-abc123-response
- name: GetV1FilesResponse
  property_count: 8
  slug: budecosystem-get-v1-files-response
- name: PostV1BatchesBatchAbc123CancelResponse
  property_count: 20
  slug: budecosystem-post-v1-batches-batch-abc123-cancel-response
- name: PostV1ChatCompletionsResponse
  property_count: 6
  slug: budecosystem-post-v1-chat-completions-response
- name: PutRoutersIdRequest
  property_count: 10
  slug: budecosystem-put-routers-id-request
jsonld:
- class_count: 12
  name: Budecosystem Context
  property_count: 42
  slug: budecosystem-context
layout: provider
modified: '2026-10-19'
name: Bud Ecosystem
nav: Providers
network: true
overview: 'Bud Ecosystem is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Enterprise, Platform, and Operating System.


  The Bud Ecosystem catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Bud Ecosystem''s developer surface includes changelog, getting-started guide, documentation, engineering blog, and 22 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Bud Ecosystem API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: budecosystem-rules
score:
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 34.5
    developer_ergonomics: 19.0
    discoverability: 66.1
    operational_transparency: 26.3
  previous_composite: 36.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/budecosystem/budecosystem-2026-11-03T122726.png
security:
- kind: domain-security
  name: Budecosystem Domain Security
  slug: budecosystem-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Budecosystem Trust Center
  slug: budecosystem-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, FedRAMP
slug: budecosystem
tags:
- Company
- Artificial Intelligence
- Enterprise
- Platform
- Operating System
website: https://budecosystem.com/
---
