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
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.contio.ai
  baseurl_source: declared
  description: 'Contio API as documented publicly: 76 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Contio API
  slug: contio-ai-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/contio-ai/plans/contio-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/contio-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/contio-ai/rules/contio-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/contio-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/contio-ai/json-ld/contio-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/contio-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/contio-ai/vocabulary/contio-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/contio-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/contio-ai/data-model/contio-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/contio-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/contio-ai/conventions/contio-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/contio-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/contio-ai/conventions/contio-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/contio-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/contio-ai/security/contio-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/contio-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/contio-ai/authentication/contio-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/contio-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/contio-ai/conformance/contio-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/contio-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/contio-ai/llms/contio-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contio-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/contio-ai/mcp/contio-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/contio-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/contio-ai/well-known/contio-ai-helpcenter-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/contio-ai-helpcenter-security.txt
- group: agent
  href: https://artifacts.apis.io/contio-ai/well-known/contio-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contio-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/contio-ai/hosts/contio-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contio-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/contio-ai/vendors/contio-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contio-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://contio.ai/tos
- group: operate
  title: ''
  type: StatusPage
  url: https://status.contio.ai/
- group: start
  title: ''
  type: SignUp
  url: https://contio.ai/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://contio.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://contio.ai/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://contio.ai/whats-new
- group: company
  title: ''
  type: Blog
  url: https://contio.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.contio.ai/user-api/guides/hosted-mcp/#connect-your-mcp-client
- group: docs
  title: ''
  type: Documentation
  url: https://docs.contio.ai/
- group: auth
  href: https://artifacts.apis.io/contio-ai/security/contio-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/contio-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/contio-ai/security/contio-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contio-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contio.ai/
coverage:
  checked: '2026-11-04'
  detail: Homepage loads a JavaScript‑rendered Astro site, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://contio.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: Contio provides an AI‑powered operating system for meetings that transforms spoken conversations into actionable tasks, drafts, and follow‑ups. The platform serves teams across industries – from general collaboration to benefits brokers and wealth managers – offering features like meeting planning, real‑time insights, privacy‑focused security, and integrations with existing tools. It aims to boost productivity by turning what gets said into what gets done, with a focus on AI‑driven automation and secure data handling.
image: https://contio.ai/og.png
json_schemas:
- name: GetV1MeetingTemplatesResponse
  property_count: 4
  slug: contio-ai-get-v1-meeting-templates-response
- name: PostMcpRequest
  property_count: 4
  slug: contio-ai-post-mcp-request
- name: PostV1CanvasesResponse
  property_count: 5
  slug: contio-ai-post-v1-canvases-response
- name: PostV1OauthRegisterRequest
  property_count: 6
  slug: contio-ai-post-v1-oauth-register-request
- name: PostV1OauthRegisterResponse
  property_count: 10
  slug: contio-ai-post-v1-oauth-register-response
- name: PutV1CanvasesIdContentResponse
  property_count: 3
  slug: contio-ai-put-v1-canvases-id-content-response
jsonld:
- class_count: 13
  name: Contio Ai Context
  property_count: 27
  slug: contio-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.contio.ai.
  name: Contio MCP Server
  slug: contio-ai-mcp-yml
modified: '2026-11-04'
name: Contio
nav: Providers
network: true
overview: 'Contio is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Productivity, Meetings, Software-as-a-Service, and Collaboration.


  The Contio catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Contio''s developer surface includes authentication, signup flow, pricing, changelog, engineering blog, getting-started guide, documentation, and 21 more developer resources.'
plans:
- name: Contio Ai Plans Pricing
  plan_count: 4
  slug: contio-ai-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: Contio API Rules
  rule_count: 45
  severity_counts:
    error: 38
    hint: 0
    info: 4
    warn: 3
  slug: contio-ai-rules
score:
  band: developing
  composite: 47.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 26.3
    developer_ergonomics: 35.7
    discoverability: 65.0
    operational_transparency: 42.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Contio Ai Authentication
  slug: contio-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Contio Ai Domain Security
  slug: contio-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Contio Ai Vulnerability Disclosure
  slug: contio-ai-vulnerability-disclosure
  summary_line: no policy recorded
slug: contio-ai
tags:
- Artificial Intelligence
- Productivity
- Meetings
- Software-as-a-Service
- Collaboration
website: https://contio.ai/
---
