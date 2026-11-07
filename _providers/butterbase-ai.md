---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Data API provides programmatic access to Butterbase's unified record and rulebook for CRM, client intake, support, invoicing, and more.
  name: Data API
  slug: data-api
- baseURL: https://api.butterbase.ai
  baseurl_source: declared
  description: 'Butterbase API as documented publicly: 48 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Butterbase API
  slug: butterbase-ai-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/butterbase-ai/plans/butterbase-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/butterbase-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/butterbase-ai/rules/butterbase-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/butterbase-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/butterbase-ai/json-ld/butterbase-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/butterbase-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/butterbase-ai/vocabulary/butterbase-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/butterbase-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/butterbase-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/butterbase-ai/data-model/butterbase-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/butterbase-ai-data-model.yml
- group: build
  href: https://artifacts.apis.io/butterbase-ai/cli/butterbase-ai-cli.yml
  title: ''
  type: CLI
  url: cli/butterbase-ai-cli.yml
- group: operate
  href: https://artifacts.apis.io/butterbase-ai/changelog/butterbase-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/butterbase-ai-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://butterbase.ai/trust
- group: auth
  href: https://artifacts.apis.io/butterbase-ai/authentication/butterbase-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/butterbase-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/butterbase-ai/conformance/butterbase-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/butterbase-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/butterbase-ai/llms/butterbase-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/butterbase-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/butterbase-ai/well-known/butterbase-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/butterbase-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/butterbase-ai/hosts/butterbase-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/butterbase-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/butterbase-ai/vendors/butterbase-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/butterbase-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/butterbase-ai/packages/butterbase-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/butterbase-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/butterbase-ai/packages/butterbase-ai-packages.yml
  title: ''
  type: Packages
  url: packages/butterbase-ai-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.butterbase.ai/changelog
- group: auth
  href: https://artifacts.apis.io/butterbase-ai/security/butterbase-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/butterbase-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/butterbase-ai/security/butterbase-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/butterbase-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://butterbase.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.butterbase.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.butterbase.ai/api-reference/data-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.butterbase.ai/getting-started/introduction/
- group: commercial
  title: ''
  type: Pricing
  url: https://butterbase.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://butterbase.ai/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://butterbase.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://butterbase.ai/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/tpxgTmExhF
- group: company
  title: ''
  type: Blog
  url: https://butterbase.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/butterbase-ai
coverage:
  checked: '2026-11-03'
  detail: Documentation pages are rendered via JavaScript and do not expose a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.butterbase.ai/api-reference/data-api/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: Butterbase provides an agent‑native backend platform that lets AI assistants such as Claude, Codex, and Cursor run business‑critical workflows. It offers a unified record and rulebook with backend‑enforced policies for CRM, client intake, support, invoicing, and more. The service includes a data API, integrations, and a developer portal, and is backed by South Park Commons. It aims to simplify building and operating AI‑driven businesses with a single shared data model and policy engine.
image: https://butterbase.ai/favicon-192x192.png
json_schemas:
- name: GetV1AppidImagesCompletionsJobidResponse
  property_count: 9
  slug: butterbase-ai-get-v1-appid-images-completions-jobid-response
- name: PostV1AiMeetingsRequest
  property_count: 4
  slug: butterbase-ai-post-v1-ai-meetings-request
- name: PostV1AiMeetingsResponse
  property_count: 6
  slug: butterbase-ai-post-v1-ai-meetings-response
- name: PostV1AppidImagesCompletionsRequest
  property_count: 10
  slug: butterbase-ai-post-v1-appid-images-completions-request
- name: PostV1AppidRagCollectionsNameQueryRequest
  property_count: 6
  slug: butterbase-ai-post-v1-appid-rag-collections-name-query-request
- name: PostV1AppidRagCollectionsRequest
  property_count: 5
  slug: butterbase-ai-post-v1-appid-rag-collections-request
jsonld:
- class_count: 51
  name: Butterbase Ai Context
  property_count: 86
  slug: butterbase-ai-context
layout: provider
modified: '2026-11-03'
name: Butterbase
nav: Providers
network: true
overview: 'Butterbase is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Backend, Business, Agent-Native, and Platform.


  The Butterbase catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Butterbase''s developer surface includes CLI, changelog, authentication, documentation, API reference, getting-started guide, pricing, and 24 more developer resources.'
plans:
- name: Butterbase Ai Plans Pricing
  plan_count: 3
  slug: butterbase-ai-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Butterbase API Rules
  rule_count: 44
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 3
  slug: butterbase-ai-rules
score:
  band: developing
  composite: 40.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 50.5
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Butterbase Ai Authentication
  slug: butterbase-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Butterbase Ai Domain Security
  slug: butterbase-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Butterbase Ai Trust Center
  slug: butterbase-ai-trust-center
  summary_line: SOC 2, GDPR
slug: butterbase-ai
tags:
- Artificial Intelligence
- Backend
- Business
- Agent-Native
- Platform
website: https://butterbase.ai/
---
