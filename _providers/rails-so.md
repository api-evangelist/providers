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
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public HTTP envelope for admitted agent apps.
  name: Rails Agent API
  slug: rails-agent-api
- baseURL: https://rails.so
  baseurl_source: declared
  description: Public HTTP envelope for admitted agent apps. OAuth issuer is rails.so; each MCP resource has its own audience. Tool names and schemas are release-bound and come from authenticated tools/list, not thi
  name: Agent Rails public MCP and OAuth HTTP API API
  slug: agent-rails-public-mcp-and-oauth-http-api-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/rails-so/rules/rails-so-rules.yml
  title: ''
  type: Spectral
  url: rules/rails-so-rules.yml
- group: design
  href: https://artifacts.apis.io/rails-so/json-ld/rails-so-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/rails-so-context.jsonld
- group: design
  href: https://artifacts.apis.io/rails-so/vocabulary/rails-so-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/rails-so-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/rails-so/conformance/rails-so-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rails-so-conformance.yml
- group: agent
  href: https://artifacts.apis.io/rails-so/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/rails-so/data-model/rails-so-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rails-so-data-model.yml
- group: design
  href: https://artifacts.apis.io/rails-so/errors/rails-so-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rails-so-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/rails-so/llms/rails-so-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rails-so-llms.txt
- group: agent
  href: https://artifacts.apis.io/rails-so/well-known/rails-so-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rails-so-well-known.yml
- group: other
  href: https://artifacts.apis.io/rails-so/hosts/rails-so-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rails-so-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://rails.so/sign-in
- group: auth
  href: https://artifacts.apis.io/rails-so/security/rails-so-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rails-so-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rails.so/
- group: docs
  title: ''
  type: Documentation
  url: https://rails.so/learn
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rails.so/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rails.so/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.rails.so/openapi.json
  - status: null
    url: https://rails.so/openapi.json
  - status: null
    url: https://app.rails.so/openapi.json
  - status: 401
    url: https://rails.so/mcp
  - status: 401
    url: https://app.rails.so/mcp
  - status: 401
    url: https://jobbot.rails.so/mcp
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Rails.so provides AI-powered agents that integrate directly into ChatGPT and Claude, enabling teams to automate workflows, manage communications, and access data across tools like Gmail and Google Calendar. The platform offers a suite of specialized agents such as Rolodex, Invoice Chaser, and custom agents for sales, research, and scheduling, all operating within the AI interface while keeping company data private. Early access is available via sign‑up, and the service emphasizes privacy, data security, and seamless AI collaboration.
image: https://rails.so/consumer/static/og/rails-og-d-rail-poster-1200x630.png
json_schemas:
- name: AuthorizationServerMetadata
  property_count: 5
  slug: rails-so-authorization-server-metadata
- name: RegistrationRequest
  property_count: 6
  slug: rails-so-registration-request
- name: RegistrationResponse
  property_count: 5
  slug: rails-so-registration-response
- name: TokenResponse
  property_count: 5
  slug: rails-so-token-response
jsonld:
- class_count: 10
  name: Rails So Context
  property_count: 36
  slug: rails-so-context
layout: provider
modified: '2026-10-29'
name: rails-so
nav: Providers
network: true
overview: 'rails-so publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Rails public MCP and OAuth HTTP API API, and 1 more. Tagged areas include Artificial Intelligence, Automation, Productivity, Collaboration, and ChatGPT.


  The rails-so catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  rails-so''s developer surface includes documentation and 15 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: rails-so API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: rails-so-rules
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 52.8
    developer_ergonomics: 11.2
    discoverability: 73.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 34.4
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Rails So Domain Security
  slug: rails-so-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rails-so
tags:
- Artificial Intelligence
- Automation
- Productivity
- Collaboration
- ChatGPT
- Claude
- Company
website: https://rails.so/
---
