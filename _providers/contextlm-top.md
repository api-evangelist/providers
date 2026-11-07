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
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'ContextLM API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: ContextLM API
  slug: contextlm-top-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/contextlm-top/plans/contextlm-top-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/contextlm-top-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/contextlm-top/rules/contextlm-top-rules.yml
  title: ''
  type: Spectral
  url: rules/contextlm-top-rules.yml
- group: design
  href: https://artifacts.apis.io/contextlm-top/json-ld/contextlm-top-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/contextlm-top-context.jsonld
- group: design
  href: https://artifacts.apis.io/contextlm-top/vocabulary/contextlm-top-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/contextlm-top-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/contextlm-top/data-model/contextlm-top-data-model.yml
  title: ''
  type: DataModel
  url: data-model/contextlm-top-data-model.yml
- group: operate
  href: https://artifacts.apis.io/contextlm-top/changelog/contextlm-top-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/contextlm-top-changelog.yml
- group: auth
  href: https://artifacts.apis.io/contextlm-top/authentication/contextlm-top-authentication.yml
  title: ''
  type: Authentication
  url: authentication/contextlm-top-authentication.yml
- group: design
  href: https://artifacts.apis.io/contextlm-top/conformance/contextlm-top-conformance.yml
  title: ''
  type: Conformance
  url: conformance/contextlm-top-conformance.yml
- group: agent
  href: https://artifacts.apis.io/contextlm-top/llms/contextlm-top-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contextlm-top-llms.txt
- group: agent
  href: https://artifacts.apis.io/contextlm-top/well-known/contextlm-top-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contextlm-top-well-known.yml
- group: other
  href: https://artifacts.apis.io/contextlm-top/hosts/contextlm-top-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contextlm-top-hosts.yml
- group: other
  href: https://artifacts.apis.io/contextlm-top/vendors/contextlm-top-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contextlm-top-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://api.contextlm.top/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://api.contextlm.top/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://api.contextlm.top/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://api.contextlm.top/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/xingchuan0105
- group: operate
  title: ''
  type: ChangeLog
  url: https://api.contextlm.top/help/release-notes
- group: start
  title: ''
  type: GettingStarted
  url: https://app.contextlm.top/help/getting-started/overview
- group: auth
  href: https://artifacts.apis.io/contextlm-top/security/contextlm-top-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contextlm-top-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contextlm.top/
- group: company
  title: ''
  type: Blog
  url: https://blog.contextlm.top
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.contextlm.top
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found despite probing known endpoints and documentation pages.
  evidence:
  - status: 404
    url: https://api.contextlm.top/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: ContextLM provides AI‑enhanced knowledge bases that let individuals and small teams import private documents and query them with AI, delivering answers that include precise source citations. Their flagship product, Context OS, is a self‑hosted personal AI knowledge repository, and they also offer a creator space for developers. The platform aims to augment public knowledge creation without replacing human contributors.
image: https://contextlm.top/og.png
json_schemas:
- name: PostApiAuthAgentTokenRequest
  property_count: 1
  slug: contextlm-top-post-api-auth-agent-token-request
- name: PostApiAuthAgentTokenResponse
  property_count: 2
  slug: contextlm-top-post-api-auth-agent-token-response
- name: PostApiV1ChatRequest
  property_count: 3
  slug: contextlm-top-post-api-v1-chat-request
- name: PostApiV1WorkspacesWorkspaceidApiKeysResponse
  property_count: 2
  slug: contextlm-top-post-api-v1-workspaces-workspaceid-api-keys-response
- name: PostApiV1WorkspacesWorkspaceidDocumentsResponse
  property_count: 2
  slug: contextlm-top-post-api-v1-workspaces-workspaceid-documents-response
jsonld:
- class_count: 5
  name: lm Top Context
  property_count: 9
  slug: contextlm-top-context
layout: provider
modified: '2026-11-04'
name: ContextLM
nav: Providers
network: true
overview: 'ContextLM is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Knowledge Base, PrivateDocuments, ContextOS, and CreatorSpace.


  The ContextLM catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ContextLM''s developer surface includes changelog, authentication, support, pricing, getting-started guide, engineering blog, and 17 more developer resources.'
plans:
- name: Contextlm Top Plans Pricing
  plan_count: 3
  slug: contextlm-top-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: ContextLM API Rules
  rule_count: 40
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 1
  slug: contextlm-top-rules
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 22.6
    developer_ergonomics: 40.5
    discoverability: 57.1
    operational_transparency: 21.1
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
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Contextlm Top Authentication
  slug: contextlm-top-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Contextlm Top Domain Security
  slug: contextlm-top-domain-security
  summary_line: TLSv1.3
slug: contextlm-top
tags:
- Artificial Intelligence
- Knowledge Base
- PrivateDocuments
- ContextOS
- CreatorSpace
website: https://contextlm.top/
---
