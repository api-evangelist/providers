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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 46.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Docsbot Ai Agentic Access
  operation_count: 20
  slug: docsbot-ai-agentic-access
  summary_line: 20 operations · 13 acting
api_count: 1
apis:
- baseURL: https://api.docsbot.ai
  baseurl_source: declared
  description: The DocsBot Chat API API from docsbot-ai — 1 operation(s) for docsbot chat api.
  name: docsbot-ai DocsBot Chat API
  slug: docsbot-ai-docsbot-chat-api-api
- baseURL: https://api.docsbot.ai
  baseurl_source: declared
  description: The Libraries API from docsbot-ai — 1 operation(s) for libraries.
  name: docsbot-ai Libraries API
  slug: docsbot-ai-libraries-api
- baseURL: https://api.docsbot.ai
  baseurl_source: declared
  description: The Teams API from docsbot-ai — 16 operation(s) for teams.
  name: docsbot-ai Teams API
  slug: docsbot-ai-teams-api
artifact_total: 20
common:
- group: auth
  href: https://artifacts.apis.io/docsbot-ai/well-known/docsbot-ai-blog-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/docsbot-ai-blog-security.txt
- group: agent
  href: https://artifacts.apis.io/docsbot-ai/agentic-access/docsbot-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/docsbot-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/docsbot-ai/plans/docsbot-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/docsbot-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/docsbot-ai/rules/docsbot-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/docsbot-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/docsbot-ai/json-ld/docsbot-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/docsbot-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/docsbot-ai/vocabulary/docsbot-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/docsbot-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/docsbot-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/docsbot-ai/data-model/docsbot-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/docsbot-ai-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.docsbot.ai/
- group: auth
  title: ''
  type: Security
  url: https://docsbot.ai/legal/vdp
- group: auth
  href: https://artifacts.apis.io/docsbot-ai/authentication/docsbot-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/docsbot-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/docsbot-ai/errors/docsbot-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/docsbot-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/docsbot-ai/conformance/docsbot-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/docsbot-ai-conformance.yml
- group: auth
  href: https://artifacts.apis.io/docsbot-ai/well-known/docsbot-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/docsbot-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/docsbot-ai/well-known/docsbot-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/docsbot-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/docsbot-ai/hosts/docsbot-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docsbot-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/docsbot-ai/vendors/docsbot-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/docsbot-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docsbot.ai/legal/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://docsbot.ai/tools/support/ai-savings-calculator
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docsbot.ai/legal/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://docsbot.ai/press
- group: start
  title: ''
  type: Login
  url: https://docsbot.ai/login
- group: company
  title: ''
  type: Blog
  url: https://blog.docsbot.ai/
- group: auth
  href: https://artifacts.apis.io/docsbot-ai/security/docsbot-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/docsbot-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/docsbot-ai/security/docsbot-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/docsbot-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/docsbot-ai/security/docsbot-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docsbot-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docsbot.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docsbot.ai/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://api.docsbot.ai/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://docsbot.ai/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uglyrobot/
created: '2026-10-30'
description: DocsBot provides AI agents that integrate trusted knowledge bases with real-time actions, enabling businesses to automate customer support, internal knowledge retrieval, and workflow automation. Users can create, train, test, and launch agents that ingest content from over 37 sources, including documentation, websites, and cloud services. The platform offers a free tier and paid plans with AI credits, supports multiple AI models, and integrates with tools like Zapier and Make. DocsBot’s API allows programmatic access to its AI capabilities, and its documentation details usage, pricing, and security.
image: https://docsbot.ai/images/og/main.jpeg
json_schemas:
- name: AgentAsk
  property_count: 29
  slug: docsbot-ai-agent-ask
- name: AskResponse
  property_count: 5
  slug: docsbot-ai-ask-response
- name: Ask
  property_count: 8
  slug: docsbot-ai-ask
- name: Query
  property_count: 9
  slug: docsbot-ai-query
- name: ResearchContinueRequest
  property_count: 6
  slug: docsbot-ai-research-continue-request
- name: ResearchStartRequest
  property_count: 9
  slug: docsbot-ai-research-start-request
jsonld:
- class_count: 20
  name: Docsbot Ai Context
  property_count: 70
  slug: docsbot-ai-context
layout: provider
modified: '2026-10-30'
name: docsbot-ai
nav: Providers
network: true
overview: 'docsbot-ai publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: DocsBot Chat API, Libraries API, and Teams API. Tagged areas include Company, Artificial Intelligence, Chatbots, Automation, and Customer Service.


  The docsbot-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  docsbot-ai''s developer surface includes authentication, support, engineering blog, documentation, API reference, pricing, and 25 more developer resources.'
plans:
- name: Docsbot Ai Plans Pricing
  plan_count: 5
  slug: docsbot-ai-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Docsbot Ai Rate Limits
  slug: docsbot-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: docsbot-ai API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: docsbot-ai-rules
scopes:
- name: Docsbot Ai Scopes
  scope_count: 0
  slug: docsbot-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.5
  coverage:
    artifact_dirs: 33
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.7
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 48.7
    developer_ergonomics: 25.6
    discoverability: 67.0
    operational_transparency: 7.9
  previous_composite: 53.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 35.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/docsbot-ai/docsbot-ai-2026-11-03T130853.png
security:
- kind: authentication
  name: Docsbot Ai Authentication
  slug: docsbot-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Docsbot Ai Domain Security
  slug: docsbot-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Docsbot Ai Vulnerability Disclosure
  slug: docsbot-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Docsbot Ai Trust Center
  slug: docsbot-ai-trust-center
  summary_line: SOC 2, GDPR
skill_count: 1
skills:
- name: chat
  slug: docsbot-ai-chat-skill
slug: docsbot-ai
tags:
- Company
- Artificial Intelligence
- Chatbots
- Automation
- Customer Service
website: https://docsbot.ai/
---
