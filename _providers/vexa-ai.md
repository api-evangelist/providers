---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Meeting, calendar, settings, and webhook APIs for Vexa AI.
  name: Vexa AI Meetings API
  slug: vexa-ai-meetings-api
- baseURL: https://api.cloud.vexa.ai
  baseurl_source: declared
  description: 'vexa-ai API as documented publicly: 101 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: vexa-ai API
  slug: vexa-ai-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/vexa-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/vexa-ai/rate-limits/vexa-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/vexa-ai-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/vexa-ai/rules/vexa-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/vexa-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/vexa-ai/json-ld/vexa-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/vexa-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/vexa-ai/vocabulary/vexa-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/vexa-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/vexa-ai/data-model/vexa-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vexa-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/vexa-ai/changelog/vexa-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/vexa-ai-changelog.yml
- group: auth
  href: https://artifacts.apis.io/vexa-ai/authentication/vexa-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vexa-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/vexa-ai/scopes/vexa-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/vexa-ai-scopes.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://docs.vexa.ai/roadmap/status.md
- group: design
  href: https://artifacts.apis.io/vexa-ai/lifecycle/vexa-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/vexa-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/vexa-ai/errors/vexa-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/vexa-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/vexa-ai/conformance/vexa-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vexa-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/vexa-ai/llms/vexa-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vexa-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/vexa-ai/a2a/vexa-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/vexa-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/vexa-ai/mcp/vexa-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/vexa-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/vexa-ai/well-known/vexa-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/vexa-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/vexa-ai/well-known/vexa-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vexa-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/vexa-ai/hosts/vexa-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vexa-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/vexa-ai/vendors/vexa-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vexa-ai-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://vexa.ai/integrations/webhooks
- group: auth
  title: ''
  type: Security
  url: https://vexa.ai/legal/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.vexa.ai/changelog
- group: start
  title: ''
  type: Login
  url: https://vexa.ai/signin
- group: auth
  href: https://artifacts.apis.io/vexa-ai/security/vexa-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/vexa-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/vexa-ai/security/vexa-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vexa-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vexa.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.vexa.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vexa.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.vexa.ai/api/meetings
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.vexa.ai/quickstart
- group: operate
  title: ''
  type: Support
  url: https://vexa.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://vexa.ai/feed.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Vexa-ai
- group: operate
  title: ''
  type: Roadmap
  url: https://vexa.ai/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://vexa.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vexa.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vexa.ai/
coverage:
  checked: '2026-10-31'
  detail: Docs provide API details but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://docs.vexa.ai/api/meetings.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Vexa AI provides an open-source meeting bot platform that records, transcribes, and processes Google Meet, Microsoft Teams, and Zoom calls in real time. Users can self‑host the service on their own servers, integrate with their own LLMs, and choose cloud or on‑premise deployment, offering flexible pricing from $0.30 per hour.
image: https://vexa.ai/logodark.svg
json_schemas:
- name: GetMeetingsPlatformNativemeetingidParticipantsResponse
  property_count: 6
  slug: vexa-ai-get-meetings-platform-nativemeetingid-participants-response
- name: GetUserModelsResponse
  property_count: 6
  slug: vexa-ai-get-user-models-response
- name: GetUserWebhookDeliveriesResponse
  property_count: 9
  slug: vexa-ai-get-user-webhook-deliveries-response
- name: PostAgentChatResponse
  property_count: 7
  slug: vexa-ai-post-agent-chat-response
- name: PostApiChatResponse
  property_count: 7
  slug: vexa-ai-post-api-chat-response
- name: PutUserModelsRequest
  property_count: 5
  slug: vexa-ai-put-user-models-request
jsonld:
- class_count: 99
  name: Vexa Ai Context
  property_count: 117
  slug: vexa-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.vexa.ai.
  name: vexa-ai MCP Server
  slug: vexa-ai-mcp-yml
modified: '2026-10-31'
name: vexa-ai
nav: Providers
network: true
overview: 'vexa-ai is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, MeetingBot, Transcription, and Open Source.


  The vexa-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  vexa-ai''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 31 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 2
  name: Vexa Ai Rate Limits
  slug: vexa-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: vexa-ai API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: vexa-ai-rules
scopes:
- name: Vexa Ai Scopes
  scope_count: 3
  slug: vexa-ai-scopes
  summary_line: 3 scopes
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 70.0
    catalog_earned_first_party: 8.0
    catalog_gap: 45.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -13.4
  facets:
    access_clarity: 22.4
    contract_governance: 19.7
    contract_quality: 25.9
    developer_ergonomics: 41.0
    discoverability: 65.0
    operational_transparency: 51.3
  previous_composite: 50.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
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
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Vexa Ai Authentication
  slug: vexa-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Vexa Ai Domain Security
  slug: vexa-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Vexa Ai Vulnerability Disclosure
  slug: vexa-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: vexa-ai
tags:
- Company
- Artificial Intelligence
- MeetingBot
- Transcription
- Open Source
- Self-Hosted
website: https://vexa.ai/
---
