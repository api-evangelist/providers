---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.2
  scored_at: '2026-11-06'
api_count: 4
apis:
- description: API reference for Celesto AI cloud CLI
  name: Celesto AI API
  slug: celesto-ai-api
- description: 'Celesto AI agentor API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Celesto AI agentor API
  slug: agentor-api
- description: 'Celesto AI celesto API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Celesto AI celesto API
  slug: celesto-api
- description: 'Celesto AI core API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Celesto AI core API
  slug: core-api
artifact_total: 19
common:
- group: commercial
  href: https://artifacts.apis.io/celesto-ai/plans/celesto-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/celesto-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/celesto-ai/rules/celesto-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/celesto-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/celesto-ai/json-ld/celesto-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/celesto-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/celesto-ai/vocabulary/celesto-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/celesto-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/celesto-ai/data-model/celesto-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/celesto-ai-data-model.yml
- group: build
  href: https://artifacts.apis.io/celesto-ai/cli/celesto-ai-cli.yml
  title: ''
  type: CLI
  url: cli/celesto-ai-cli.yml
- group: auth
  href: https://artifacts.apis.io/celesto-ai/authentication/celesto-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/celesto-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/celesto-ai/conformance/celesto-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/celesto-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/celesto-ai/llms/celesto-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/celesto-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/celesto-ai/a2a/celesto-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/celesto-ai-a2a.yml
- group: auth
  href: https://artifacts.apis.io/celesto-ai/well-known/celesto-ai-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/celesto-ai-status-security.txt
- group: agent
  href: https://artifacts.apis.io/celesto-ai/well-known/celesto-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/celesto-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/celesto-ai/hosts/celesto-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/celesto-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/celesto-ai/vendors/celesto-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/celesto-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://celesto.ai/legal/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.celesto.ai/
- group: start
  title: ''
  type: SignUp
  url: https://celesto.ai/sign-up
- group: auth
  title: ''
  type: Security
  url: https://celesto.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://celesto.ai/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://celesto.ai/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/celestoai
- group: company
  title: ''
  type: Blog
  url: https://celesto.ai/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://celesto.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.celesto.ai/
- group: auth
  href: https://artifacts.apis.io/celesto-ai/security/celesto-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/celesto-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://celesto.ai/
coverage:
  checked: '2026-11-04'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 301
    url: https://docs.celesto.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: 'celesto-ai is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://ik.imagekit.io/gradsflow/celestoai/meta-seo/cute-metatag_HcjF7UuBs.jpg
json_schemas:
- name: GetChatResponse
  property_count: 1
  slug: celesto-ai-get-chat-response
- name: GetResponse
  property_count: 2
  slug: celesto-ai-get-response
- name: GetSandboxesIdDesktopResponse
  property_count: 4
  slug: celesto-ai-get-sandboxes-id-desktop-response
- name: PostChatRequest
  property_count: 1
  slug: celesto-ai-post-chat-request
- name: PostComputersIdTerminalsResponse
  property_count: 5
  slug: celesto-ai-post-computers-id-terminals-response
- name: PostRequest
  property_count: 4
  slug: celesto-ai-post-request
- name: PostSandboxesIdExecRequest
  property_count: 3
  slug: celesto-ai-post-sandboxes-id-exec-request
- name: PostSandboxesIdExecResponse
  property_count: 3
  slug: celesto-ai-post-sandboxes-id-exec-response
- name: PostSandboxesRequest
  property_count: 3
  slug: celesto-ai-post-sandboxes-request
- name: PostSandboxesResponse
  property_count: 2
  slug: celesto-ai-post-sandboxes-response
jsonld:
- class_count: 10
  name: Celesto Ai Context
  property_count: 24
  slug: celesto-ai-context
layout: provider
modified: '2026-11-04'
name: Celesto AI
nav: Providers
network: true
overview: 'Celesto AI is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including agentor API, celesto API, core API, and 1 more. Tagged areas include Artificial Intelligence, CI, Runners, Cloud, and Automation.


  The Celesto AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Celesto AI''s developer surface includes CLI, authentication, signup flow, pricing, engineering blog, getting-started guide, documentation, and 19 more developer resources.'
plans:
- name: Celesto Ai Plans Pricing
  plan_count: 6
  slug: celesto-ai-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Celesto AI API Rules
  rule_count: 43
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 2
  slug: celesto-ai-rules
score:
  band: thin
  composite: 33.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 67.8
    catalog_earned_first_party: 12.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 24.4
    developer_ergonomics: 25.0
    discoverability: 53.6
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Celesto Ai Authentication
  slug: celesto-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Celesto Ai Domain Security
  slug: celesto-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: celesto-ai
tags:
- Artificial Intelligence
- CI
- Runners
- Cloud
- Automation
- Company
website: https://celesto.ai/
---
