---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 22
  human_in_the_loop: 2
  name: Kaiv Ai Agentic Access
  operation_count: 31
  slug: kaiv-ai-agentic-access
  summary_line: 31 operations · 22 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.kaiv.ai/api/bridge/v1
  baseurl_source: declared
  description: Who the key belongs to, and signing out.
  name: kaiv-ai Account API
  slug: kaiv-ai-account-api
- baseURL: https://api.kaiv.ai/api/bridge/v1
  baseurl_source: declared
  description: Tool-call records and usage figures.
  name: kaiv-ai Activity API
  slug: kaiv-ai-activity-api
- baseURL: https://api.kaiv.ai/api/bridge/v1
  baseurl_source: declared
  description: Tool changes found when a source is read again, held until they are accepted.
  name: kaiv-ai Changes API
  slug: kaiv-ai-changes-api
- baseURL: https://api.kaiv.ai/api/bridge/v1
  baseurl_source: declared
  description: The credential Bridge sends to your API or MCP server. Stored encrypted, never shown to an AI client.
  name: kaiv-ai Credentials API
  slug: kaiv-ai-credentials-api
- baseURL: https://api.kaiv.ai/api/bridge/v1
  baseurl_source: declared
  description: A server that makes uploaded documents searchable.
  name: kaiv-ai Documents API
  slug: kaiv-ai-documents-api
- baseURL: https://api.kaiv.ai/api/bridge/v1
  baseurl_source: declared
  description: Gateway keys for AI clients that use a key instead of signing in.
  name: kaiv-ai Keys API
  slug: kaiv-ai-keys-api
- baseURL: https://api.kaiv.ai/api/bridge/v1
  baseurl_source: declared
  description: A trial MCP server from a public spec, with no account.
  name: kaiv-ai No account API
  slug: kaiv-ai-no-account-api
- baseURL: https://api.kaiv.ai/api/bridge/v1
  baseurl_source: declared
  description: Rules for which tools a key may call.
  name: kaiv-ai Policies API
  slug: kaiv-ai-policies-api
- baseURL: https://api.kaiv.ai/api/bridge/v1
  baseurl_source: declared
  description: Create a managed MCP server from a source, choose its tools and publish it.
  name: kaiv-ai Servers API
  slug: kaiv-ai-servers-api
artifact_total: 24
common:
- group: agent
  href: https://artifacts.apis.io/kaiv-ai/agentic-access/kaiv-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kaiv-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/kaiv-ai/rules/kaiv-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/kaiv-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/kaiv-ai/json-ld/kaiv-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kaiv-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/kaiv-ai/vocabulary/kaiv-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kaiv-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/kaiv-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/kaiv-ai/data-model/kaiv-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kaiv-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/kaiv-ai/errors/kaiv-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kaiv-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/kaiv-ai/conformance/kaiv-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kaiv-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/kaiv-ai/llms/kaiv-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kaiv-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/kaiv-ai/well-known/kaiv-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kaiv-ai-security.txt
- group: auth
  href: https://artifacts.apis.io/kaiv-ai/well-known/kaiv-ai-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kaiv-ai-api-security.txt
- group: agent
  href: https://artifacts.apis.io/kaiv-ai/well-known/kaiv-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kaiv-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/kaiv-ai/hosts/kaiv-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kaiv-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/kaiv-ai/vendors/kaiv-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kaiv-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://kaiv.ai/bridge/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://kaiv.ai/bridge/changelog
- group: auth
  href: https://artifacts.apis.io/kaiv-ai/security/kaiv-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kaiv-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/kaiv-ai/security/kaiv-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kaiv-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kaiv.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://kaiv.ai/bridge
- group: docs
  title: ''
  type: Documentation
  url: https://kaiv.ai/bridge/docs
- group: docs
  title: ''
  type: APIReference
  url: https://kaiv.ai/bridge/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://kaiv.ai/bridge/docs/connect-a-client
- group: operate
  title: ''
  type: Support
  url: https://kaiv.ai/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://kaiv.ai/bridge/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.kaiv.ai/bridge/auth?mode=signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kaiv.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kaiv.ai/privacy
created: '2026-10-29'
description: 'Kaiva is an AI infrastructure company. We build the foundation that connects agents to the tools and data people already depend on. Bridge is our lead product: a managed MCP platform you can start using today. Our background in enterprise transformation informs the problems we choose to solve. We focus on making infrastructure for useful AI accessible to every builder, supporting developers, startups, and teams extending AI into existing business systems.'
image: https://kaiv.ai/animations/kaiva-ai-infra-poster.webp
json_schemas:
- name: Credential
  property_count: 0
  slug: kaiv-ai-credential
- name: Server
  property_count: 5
  slug: kaiv-ai-server
- name: Tool
  property_count: 6
  slug: kaiv-ai-tool
jsonld:
- class_count: 3
  name: Kaiv Ai Context
  property_count: 11
  slug: kaiv-ai-context
layout: provider
modified: '2026-10-29'
name: kaiv-ai
nav: Providers
network: true
overview: 'kaiv-ai publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Activity API, Changes API, and 6 more. Tagged areas include Artificial Intelligence, Infrastructure, MCP, Bridge, and Enterprise.


  The kaiv-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  kaiv-ai''s developer surface includes changelog, documentation, API reference, getting-started guide, support, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Kaiv Ai Plans Pricing
  plan_count: 0
  slug: kaiv-ai-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Kaiv Ai Rate Limits
  slug: kaiv-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: kaiv-ai API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 2
  slug: kaiv-ai-rules
scopes:
- name: Kaiv Ai Scopes
  scope_count: 0
  slug: kaiv-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 30
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.0
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 60.1
    developer_ergonomics: 27.9
    discoverability: 73.2
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 49.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/kaiv-ai/kaiv-ai-2026-11-03T134259.png
security:
- kind: authentication
  name: Kaiv Ai Authentication
  slug: kaiv-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Kaiv Ai Domain Security
  slug: kaiv-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kaiv Ai Vulnerability Disclosure
  slug: kaiv-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: create-server
  slug: kaiv-ai-create-server
- name: invoke-tool
  slug: kaiv-ai-invoke-tool
- name: publish-server
  slug: kaiv-ai-publish-server
slug: kaiv-ai
tags:
- Artificial Intelligence
- Infrastructure
- MCP
- Bridge
- Enterprise
- Developer Tools
website: https://kaiv.ai/
---
