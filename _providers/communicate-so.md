---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 55.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 186
  human_in_the_loop: 10
  name: Communicate So Agentic Access
  operation_count: 270
  slug: communicate-so-agentic-access
  summary_line: 270 operations · 186 acting · 10 human-in-the-loop
api_count: 1
apis:
- baseURL: https://app.communicate.so/api/v1
  baseurl_source: declared
  description: The Account credentials API from communicate-so — 4 operation(s) for account credentials.
  name: communicate-so Account credentials API
  slug: communicate-so-account-credentials-api
- baseURL: https://app.communicate.so/api/v1
  baseurl_source: declared
  description: The Account preferences API from communicate-so — 1 operation(s) for account preferences.
  name: communicate-so Account preferences API
  slug: communicate-so-account-preferences-api
- baseURL: https://app.communicate.so/api/v1
  baseurl_source: declared
  description: The Agents API from communicate-so — 73 operation(s) for agents.
  name: communicate-so Agents API
  slug: communicate-so-agents-api
- baseURL: https://app.communicate.so/api/v1
  baseurl_source: declared
  description: The Authentication API from communicate-so — 1 operation(s) for authentication.
  name: communicate-so Authentication API
  slug: communicate-so-authentication-api
- baseURL: https://app.communicate.so/api/v1
  baseurl_source: declared
  description: The Chat API from communicate-so — 1 operation(s) for chat.
  name: communicate-so Chat API
  slug: communicate-so-chat-api
- baseURL: https://app.communicate.so/api/v1
  baseurl_source: declared
  description: The Discovery API from communicate-so — 1 operation(s) for discovery.
  name: communicate-so Discovery API
  slug: communicate-so-discovery-api
- baseURL: https://app.communicate.so/api/v1
  baseurl_source: declared
  description: The Grill API from communicate-so — 8 operation(s) for grill.
  name: communicate-so Grill API
  slug: communicate-so-grill-api
- baseURL: https://app.communicate.so/api/v1
  baseurl_source: declared
  description: The Inbox API from communicate-so — 16 operation(s) for inbox.
  name: communicate-so Inbox API
  slug: communicate-so-inbox-api
- baseURL: https://app.communicate.so/api/v1
  baseurl_source: declared
  description: The Learnings API from communicate-so — 3 operation(s) for learnings.
  name: communicate-so Learnings API
  slug: communicate-so-learnings-api
- baseURL: https://app.communicate.so/api/v1
  baseurl_source: declared
  description: The Notifications API from communicate-so — 9 operation(s) for notifications.
  name: communicate-so Notifications API
  slug: communicate-so-notifications-api
- baseURL: https://app.communicate.so/api/v1
  baseurl_source: declared
  description: The Sources API from communicate-so — 11 operation(s) for sources.
  name: communicate-so Sources API
  slug: communicate-so-sources-api
- baseURL: https://app.communicate.so/api/v1
  baseurl_source: declared
  description: The Teams API from communicate-so — 4 operation(s) for teams.
  name: communicate-so Teams API
  slug: communicate-so-teams-api
- baseURL: https://app.communicate.so/api/v1
  baseurl_source: declared
  description: The Workspace members API from communicate-so — 6 operation(s) for workspace members.
  name: communicate-so Workspace members API
  slug: communicate-so-workspace-members-api
- baseURL: https://app.communicate.so/api/v1
  baseurl_source: declared
  description: The Workspaces API from communicate-so — 79 operation(s) for workspaces.
  name: communicate-so Workspaces API
  slug: communicate-so-workspaces-api
artifact_total: 32
common:
- group: agent
  href: https://artifacts.apis.io/communicate-so/agentic-access/communicate-so-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/communicate-so-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/communicate-so/rate-limits/communicate-so-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/communicate-so-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/communicate-so/plans/communicate-so-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/communicate-so-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/communicate-so/rules/communicate-so-rules.yml
  title: ''
  type: Spectral
  url: rules/communicate-so-rules.yml
- group: design
  href: https://artifacts.apis.io/communicate-so/json-ld/communicate-so-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/communicate-so-context.jsonld
- group: design
  href: https://artifacts.apis.io/communicate-so/vocabulary/communicate-so-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/communicate-so-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/communicate-so/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/communicate-so/data-model/communicate-so-data-model.yml
  title: ''
  type: DataModel
  url: data-model/communicate-so-data-model.yml
- group: operate
  href: https://artifacts.apis.io/communicate-so/changelog/communicate-so-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/communicate-so-changelog.yml
- group: design
  href: https://artifacts.apis.io/communicate-so/conventions/communicate-so-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/communicate-so-conventions.yml
- group: design
  href: https://artifacts.apis.io/communicate-so/conventions/communicate-so-conventions.yml
  title: ''
  type: Conventions
  url: conventions/communicate-so-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://communicate.so/security
- group: auth
  href: https://artifacts.apis.io/communicate-so/authentication/communicate-so-authentication.yml
  title: ''
  type: Authentication
  url: authentication/communicate-so-authentication.yml
- group: auth
  href: https://artifacts.apis.io/communicate-so/scopes/communicate-so-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/communicate-so-scopes.yml
- group: design
  href: https://artifacts.apis.io/communicate-so/errors/communicate-so-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/communicate-so-problem-types.yml
- group: design
  href: https://artifacts.apis.io/communicate-so/conformance/communicate-so-conformance.yml
  title: ''
  type: Conformance
  url: conformance/communicate-so-conformance.yml
- group: agent
  href: https://artifacts.apis.io/communicate-so/llms/communicate-so-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/communicate-so-llms.txt
- group: other
  href: https://artifacts.apis.io/communicate-so/a2a/communicate-so-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/communicate-so-a2a.yml
- group: build
  href: https://artifacts.apis.io/communicate-so/mcp/communicate-so-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/communicate-so-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/communicate-so/mcp/communicate-so-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/communicate-so-mcp.yml
- group: agent
  href: https://artifacts.apis.io/communicate-so/well-known/communicate-so-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/communicate-so-well-known.yml
- group: other
  href: https://artifacts.apis.io/communicate-so/hosts/communicate-so-hosts.yml
  title: ''
  type: Hosts
  url: hosts/communicate-so-hosts.yml
- group: other
  href: https://artifacts.apis.io/communicate-so/vendors/communicate-so-vendors.yml
  title: ''
  type: Vendors
  url: vendors/communicate-so-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://communicate.so/security
- group: start
  title: ''
  type: Login
  url: https://app.communicate.so/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://communicate.so/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.communicate.so/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/communicate-so/security/communicate-so-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/communicate-so-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/communicate-so/security/communicate-so-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/communicate-so-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/communicate-so/security/communicate-so-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/communicate-so-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://communicate.so/
- group: docs
  title: ''
  type: Documentation
  url: https://communicate.so/developers
- group: docs
  title: ''
  type: APIReference
  url: https://communicate.so/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://communicate.so/pricing
- group: operate
  title: ''
  type: Support
  url: https://communicate.so/contact
- group: company
  title: ''
  type: Blog
  url: https://communicate.so/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/communicateso
- group: commercial
  title: ''
  type: TermsOfService
  url: https://communicate.so/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://communicate.so/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://communicate.so/openapi.json
  - status: null
    url: https://communicate.so/mcp
  - status: null
    url: https://developer.communicate.so/mcp
  - status: 401
    url: https://app.communicate.so/mcp
  - status: 200
    url: https://communicate.so/
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Communicate provides an AI-powered customer support platform that answers queries instantly in the brand’s voice across all channels. It transforms help center articles, tickets, and product documentation into a conversational agent, offering grounded answers, seamless handoff to human agents, and robust data privacy controls. Teams benefit from higher resolution rates, reduced deflection, and flexible pricing with a $1 activation and credit‑based usage.
image: https://communicate.so/og/home
json_schemas:
- name: createAgentResponse
  property_count: 26
  slug: communicate-so-create-agent-response
- name: duplicateAgentResponse
  property_count: 26
  slug: communicate-so-duplicate-agent-response
- name: fetchAgentLogoResponse
  property_count: 26
  slug: communicate-so-fetch-agent-logo-response
- name: listWorkspaceAgentsResponse
  property_count: 0
  slug: communicate-so-list-workspace-agents-response
- name: readAgentResponse
  property_count: 26
  slug: communicate-so-read-agent-response
- name: readInboxConversationResponse
  property_count: 10
  slug: communicate-so-read-inbox-conversation-response
jsonld:
- class_count: 120
  name: Communicate So Context
  property_count: 175
  slug: communicate-so-context
layout: provider
mcp_servers:
- description: Remote MCP server at communicate.so.
  name: communicate-so MCP Server
  slug: communicate-so-mcp-yml
modified: '2026-10-29'
name: communicate-so
nav: Providers
network: true
overview: 'communicate-so publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account credentials API, Account preferences API, Agents API, and 11 more. Tagged areas include Artificial Intelligence, Customer Service, Chatbots, Software-as-a-Service, and Automation.


  The communicate-so catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  communicate-so''s developer surface includes changelog, authentication, getting-started guide, documentation, API reference, pricing, support, and 32 more developer resources.'
plans:
- name: Communicate So Plans Pricing
  plan_count: 2
  slug: communicate-so-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Communicate So Rate Limits
  slug: communicate-so-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: communicate-so API Rules
  rule_count: 63
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 12
  slug: communicate-so-rules
scopes:
- name: Communicate So Scopes
  scope_count: 2
  slug: communicate-so-scopes
  summary_line: 2 scopes
score:
  band: developing
  composite: 53.3
  coverage:
    artifact_dirs: 34
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.8
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 67.0
    developer_ergonomics: 36.2
    discoverability: 75.0
    operational_transparency: 47.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 65.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: unknown
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
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/communicate-so/communicate-so-2026-11-03T124945.png
security:
- kind: authentication
  name: Communicate So Authentication
  slug: communicate-so-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Communicate So Domain Security
  slug: communicate-so-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Communicate So Vulnerability Disclosure
  slug: communicate-so-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Communicate So Trust Center
  slug: communicate-so-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
skill_count: 1
skills:
- name: bootstrap-account-credential
  slug: communicate-so-bootstrap-account-credential
slug: communicate-so
tags:
- Artificial Intelligence
- Customer Service
- Chatbots
- Software-as-a-Service
- Automation
website: https://communicate.so/
---
