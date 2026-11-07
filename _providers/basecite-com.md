---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 55.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Basecite Com Agentic Access
  operation_count: 21
  slug: basecite-com-agentic-access
  summary_line: 21 operations · 11 acting
api_count: 1
apis:
- baseURL: https://api.basecite.com
  baseurl_source: declared
  description: The Admin API from BaseCite — 2 operation(s) for admin.
  name: BaseCite Admin API
  slug: basecite-com-admin-api
- baseURL: https://api.basecite.com
  baseurl_source: declared
  description: The Ai API from BaseCite — 2 operation(s) for ai.
  name: BaseCite AI API
  slug: basecite-com-ai-api
- baseURL: https://api.basecite.com
  baseurl_source: declared
  description: The Oauth API from BaseCite — 1 operation(s) for oauth.
  name: BaseCite OAuth API
  slug: basecite-com-oauth-api
- baseURL: https://api.basecite.com
  baseurl_source: declared
  description: The Organizations API from BaseCite — 10 operation(s) for organizations.
  name: BaseCite Organizations API
  slug: basecite-com-organizations-api
- baseURL: https://api.basecite.com
  baseurl_source: declared
  description: The Portal API from BaseCite — 1 operation(s) for portal.
  name: BaseCite Portal API
  slug: basecite-com-portal-api
- baseURL: https://api.basecite.com
  baseurl_source: declared
  description: The Sandbox API from BaseCite — 4 operation(s) for sandbox.
  name: BaseCite Sandbox API
  slug: basecite-com-sandbox-api
artifact_total: 23
asyncapis:
- description: ''
  name: Basecite Com Webhooks
  slug: basecite-com-webhooks
common:
- group: auth
  title: ''
  type: Security
  url: https://basecite.com/security
- group: agent
  href: https://artifacts.apis.io/basecite-com/agentic-access/basecite-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/basecite-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/basecite-com/rules/basecite-com-rules.yml
  title: ''
  type: Spectral
  url: rules/basecite-com-rules.yml
- group: design
  href: https://artifacts.apis.io/basecite-com/json-ld/basecite-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/basecite-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/basecite-com/vocabulary/basecite-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/basecite-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/basecite-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/basecite-com/asyncapi/basecite-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/basecite-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/basecite-com/data-model/basecite-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/basecite-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/basecite-com/cli/basecite-com-cli.yml
  title: ''
  type: CLI
  url: cli/basecite-com-cli.yml
- group: design
  href: https://artifacts.apis.io/basecite-com/conventions/basecite-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/basecite-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/basecite-com/conventions/basecite-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/basecite-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/basecite-com/authentication/basecite-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/basecite-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/basecite-com/errors/basecite-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/basecite-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/basecite-com/conformance/basecite-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/basecite-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/basecite-com/llms/basecite-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/basecite-com-llms.txt
- group: other
  href: https://artifacts.apis.io/basecite-com/a2a/basecite-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/basecite-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/basecite-com/mcp/basecite-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/basecite-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/basecite-com/well-known/basecite-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/basecite-com-security.txt
- group: agent
  href: https://artifacts.apis.io/basecite-com/well-known/basecite-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/basecite-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/basecite-com/hosts/basecite-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/basecite-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/basecite-com/vendors/basecite-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/basecite-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://basecite.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://basecite.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://basecite.com/pricing.md
- group: docs
  title: ''
  type: Documentation
  url: https://basecite.com/docs
- group: start
  title: ''
  type: SignUp
  url: https://basecite.com/signup
- group: docs
  title: ''
  type: APIReference
  url: https://basecite.com/developers
- group: auth
  href: https://artifacts.apis.io/basecite-com/scopes/basecite-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/basecite-com-scopes.yml
- group: auth
  href: https://artifacts.apis.io/basecite-com/security/basecite-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/basecite-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/basecite-com/security/basecite-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/basecite-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://basecite.com/
created: '2026-11-02'
description: BaseCite provides an evidence‑context infrastructure for organizations that need to keep customer‑submitted materials private while allowing authorized AI systems to access bounded context. The platform records consent, provenance, and integrity metadata, and offers controlled publication rules for AI‑readable context. Public pages describe capabilities, API contracts, and MCP metadata, while private uploads remain secure. BaseCite does not verify truth, legal authority, or endorse any supplier, focusing solely on secure, scoped evidence delivery for AI applications.
image: https://basecite.com/basecite-social-card.jpg
json_schemas:
- name: getAiCapabilitiesResponse
  property_count: 3
  slug: basecite-com-get-ai-capabilities-response
- name: getPartnerUploadStatusResponse
  property_count: 3
  slug: basecite-com-get-partner-upload-status-response
- name: getSandboxInfoResponse
  property_count: 3
  slug: basecite-com-get-sandbox-info-response
- name: getSandboxKeyInfoResponse
  property_count: 3
  slug: basecite-com-get-sandbox-key-info-response
- name: issueSandboxCredentialResponse
  property_count: 3
  slug: basecite-com-issue-sandbox-credential-response
- name: sandboxEchoResponse
  property_count: 3
  slug: basecite-com-sandbox-echo-response
jsonld:
- class_count: 3
  name: Basecite Com Context
  property_count: 10
  slug: basecite-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.basecite.com.
  name: BaseCite MCP Server
  slug: basecite-com-mcp-yml
modified: '2026-11-02'
name: BaseCite
nav: Providers
network: true
overview: 'BaseCite publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, AI API, OAuth API, and 3 more. Tagged areas include Company, Artificial Intelligence, Evidence, Platform, and Privacy.


  The BaseCite catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  BaseCite''s developer surface includes CLI, authentication, pricing, documentation, signup flow, API reference, and 25 more developer resources.'
plans:
- name: Basecite Com Plans Pricing
  plan_count: 0
  slug: basecite-com-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: BaseCite API Rules
  rule_count: 48
  severity_counts:
    error: 42
    hint: 0
    info: 2
    warn: 4
  slug: basecite-com-rules
scopes:
- name: Basecite Com Scopes
  scope_count: 7
  slug: basecite-com-scopes
  summary_line: 7 scopes · clientCredentials
score:
  band: developing
  composite: 39.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 63.4
    developer_ergonomics: 29.2
    discoverability: 65.0
    operational_transparency: 13.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Basecite Com Authentication
  slug: basecite-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Basecite Com Domain Security
  slug: basecite-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Basecite Com Vulnerability Disclosure
  slug: basecite-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: basecite-com-partner-upload
  slug: basecite-com-partner-upload
slug: basecite-com
tags:
- Company
- Artificial Intelligence
- Evidence
- Platform
- Privacy
website: https://basecite.com/
---
