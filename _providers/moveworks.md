---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Moveworks Agentic Access
  operation_count: 46
  slug: moveworks-agentic-access
  summary_line: 46 operations · 15 acting
api_count: 9
apis:
- baseURL: https://api.moveworks.ai
  baseurl_source: declared
  description: The authentication API from Moveworks — 2 operation(s) for authentication.
  name: Moveworks Authentication API
  slug: moveworks-authentication-api
- baseURL: https://api.moveworks.ai
  baseurl_source: declared
  description: The conversations API from Moveworks — 3 operation(s) for conversations.
  name: Moveworks Conversations API
  slug: moveworks-conversations-api
- baseURL: https://api.moveworks.ai
  baseurl_source: declared
  description: The deprecated API from Moveworks — 1 operation(s) for deprecated.
  name: Moveworks Deprecated API
  slug: moveworks-deprecated-api
- baseURL: https://api.moveworks.ai
  baseurl_source: declared
  description: The events API from Moveworks — 1 operation(s) for events.
  name: Moveworks Events API
  slug: moveworks-events-api
- baseURL: https://api.moveworks.ai
  baseurl_source: declared
  description: The messages API from Moveworks — 3 operation(s) for messages.
  name: Moveworks Messages API
  slug: moveworks-messages-api
- baseURL: https://api.moveworks.ai
  baseurl_source: declared
  description: The responses API from Moveworks — 3 operation(s) for responses.
  name: Moveworks Responses API
  slug: moveworks-responses-api
- baseURL: https://api.moveworks.ai
  baseurl_source: declared
  description: The smartForms API from Moveworks — 3 operation(s) for smartforms.
  name: Moveworks Smart Forms API
  slug: moveworks-smartforms-api
- baseURL: https://api.moveworks.ai
  baseurl_source: declared
  description: The webhooks API from Moveworks — 1 operation(s) for webhooks.
  name: Moveworks Webhooks API
  slug: moveworks-webhooks-api
- baseURL: https://api.moveworks.ai
  baseurl_source: declared
  description: The Articles API from Moveworks — 1 operation(s) for articles.
  name: Moveworks Articles API
  slug: moveworks-articles-api
- baseURL: https://api.moveworks.ai
  baseurl_source: declared
  description: The Files API from Moveworks — 5 operation(s) for files.
  name: Moveworks Files API
  slug: moveworks-files-api
- baseURL: https://api.moveworks.ai
  baseurl_source: declared
  description: The Groups API from Moveworks — 2 operation(s) for groups.
  name: Moveworks Groups API
  slug: moveworks-groups-api
- baseURL: https://api.moveworks.ai
  baseurl_source: declared
  description: The Interactions API from Moveworks — 1 operation(s) for interactions.
  name: Moveworks Interactions API
  slug: moveworks-interactions-api
- baseURL: https://api.moveworks.ai
  baseurl_source: declared
  description: The Plugin Calls API from Moveworks — 1 operation(s) for plugin calls.
  name: Moveworks Plugin Calls API
  slug: moveworks-plugin-calls-api
- baseURL: https://api.moveworks.ai
  baseurl_source: declared
  description: The Plugin Resources API from Moveworks — 1 operation(s) for plugin resources.
  name: Moveworks Plugin Resources API
  slug: moveworks-plugin-resources-api
- baseURL: https://api.moveworks.ai
  baseurl_source: declared
  description: Exported AI Assistant interaction records
  name: Moveworks Records API
  slug: moveworks-records-api
- baseURL: https://api.moveworks.ai
  baseurl_source: declared
  description: The Users API from Moveworks — 2 operation(s) for users.
  name: Moveworks Users API
  slug: moveworks-users-api
arazzos:
- description: Create a conversation, request a response, then list the resulting messages.
  name: Moveworks — start an AI Assistant conversation and read the reply
  slug: moveworks-conversation
- description: Mint an OAuth client-credentials token, verify it, then send an event-triggered message to employees.
  name: Moveworks — authenticate and notify employees for an event
  slug: moveworks-notify-employees
artifact_total: 39
asyncapis:
- description: ''
  name: Moveworks Webhooks
  slug: moveworks-webhooks
collections:
- collection_type: open
  name: (Beta) Conversations authentication API
  slug: open-moveworks-authentication-api
- collection_type: open
  name: (Beta) authentication conversations API
  slug: open-moveworks-conversations-api
- collection_type: open
  name: (Beta) Conversations authentication  API
  slug: open-moveworks-default-api
- collection_type: open
  name: (Beta) Conversations authentication deprecated API
  slug: open-moveworks-deprecated-api
- collection_type: open
  name: (Beta) Conversations authentication events API
  slug: open-moveworks-events-api
- collection_type: open
  name: (Beta) Conversations authentication messages API
  slug: open-moveworks-messages-api
- collection_type: open
  name: (Beta) Conversations authentication responses API
  slug: open-moveworks-responses-api
- collection_type: open
  name: (Beta) Conversations authentication smartForms API
  slug: open-moveworks-smartforms-api
- collection_type: open
  name: (Beta) Conversations authentication webhooks API
  slug: open-moveworks-webhooks-api
common:
- group: commercial
  href: https://artifacts.apis.io/moveworks/plans/moveworks-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/moveworks-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.moveworks.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.moveworks.com/us/en/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.moveworks.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.moveworks.com/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.moveworks.com/agent-studio/quickstart-guide
- group: operate
  title: ''
  type: Support
  url: https://help.moveworks.com/docs/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.moveworks.com
- group: operate
  title: ''
  type: Community
  url: https://community.moveworks.com
- group: company
  title: ''
  type: Blog
  url: https://www.moveworks.com/us/en/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moveworks
- group: commercial
  title: ''
  type: Pricing
  url: https://www.moveworks.com/us/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.moveworks.com/us/en/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.moveworks.com/us/en/legal/privacy-policy
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.moveworks.com/ai-assistant/getting-started/roadmap-release-notes/release-notes-2026
- group: docs
  href: https://artifacts.apis.io/moveworks/openapi/_original/moveworks-content-gateway-openapi.yaml
  title: ''
  type: OpenAPI
  url: openapi/_original/moveworks-content-gateway-openapi.yaml
- group: docs
  href: https://artifacts.apis.io/moveworks/openapi/_original/moveworks-identity-gateway-openapi.yaml
  title: ''
  type: OpenAPI
  url: openapi/_original/moveworks-identity-gateway-openapi.yaml
- group: docs
  href: https://artifacts.apis.io/moveworks/openapi/_original/moveworks-knowledge-gateway-openapi.yaml
  title: ''
  type: OpenAPI
  url: openapi/_original/moveworks-knowledge-gateway-openapi.yaml
- group: docs
  href: https://artifacts.apis.io/moveworks/openapi/_original/moveworks-forms-gateway-openapi.yaml
  title: ''
  type: OpenAPI
  url: openapi/_original/moveworks-forms-gateway-openapi.yaml
- group: other
  href: https://artifacts.apis.io/moveworks/overlays/moveworks-content-gateway-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moveworks-content-gateway-overlay.yaml
- group: other
  href: https://artifacts.apis.io/moveworks/overlays/moveworks-identity-gateway-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moveworks-identity-gateway-overlay.yaml
- group: other
  href: https://artifacts.apis.io/moveworks/overlays/moveworks-knowledge-gateway-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moveworks-knowledge-gateway-overlay.yaml
- group: other
  href: https://artifacts.apis.io/moveworks/overlays/moveworks-forms-gateway-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moveworks-forms-gateway-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/moveworks/well-known/moveworks-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/moveworks-well-known.yml
- group: other
  href: https://artifacts.apis.io/moveworks/well-known/moveworks-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/moveworks-api-catalog.json
- group: agent
  href: https://artifacts.apis.io/moveworks/mcp/moveworks-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/moveworks-mcp.yml
- group: agent
  href: https://artifacts.apis.io/moveworks/llms/moveworks-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/moveworks-llms.txt
- group: build
  href: https://artifacts.apis.io/moveworks/packages/moveworks-packages.yml
  title: ''
  type: Packages
  url: packages/moveworks-packages.yml
- group: auth
  href: https://artifacts.apis.io/moveworks/authentication/moveworks-authentication.yml
  title: ''
  type: Authentication
  url: authentication/moveworks-authentication.yml
- group: agent
  href: https://artifacts.apis.io/moveworks/agentic-access/moveworks-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/moveworks-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/moveworks/conformance/moveworks-conformance.yml
  title: ''
  type: Conformance
  url: conformance/moveworks-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.moveworks.com/us/en/platform/security
- group: design
  href: https://artifacts.apis.io/moveworks/errors/moveworks-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/moveworks-error-codes.yml
- group: design
  href: https://artifacts.apis.io/moveworks/lifecycle/moveworks-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/moveworks-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.moveworks.com
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.moveworks.com/api-reference/legacy-deprecated-ap-is
- group: design
  href: https://artifacts.apis.io/moveworks/conventions/moveworks-conventions.yml
  title: ''
  type: Conventions
  url: conventions/moveworks-conventions.yml
- group: operate
  href: https://artifacts.apis.io/moveworks/changelog/moveworks-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/moveworks-changelog.yml
- group: design
  href: https://artifacts.apis.io/moveworks/data-model/moveworks-data-model.yml
  title: ''
  type: DataModel
  url: data-model/moveworks-data-model.yml
- group: design
  href: https://artifacts.apis.io/moveworks/asyncapi/moveworks-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/moveworks-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/moveworks/security/moveworks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/moveworks-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/moveworks/security/moveworks-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/moveworks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.moveworks.com/us/en/platform/security
- group: auth
  href: https://artifacts.apis.io/moveworks/security/moveworks-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/moveworks-trust-center.yml
- group: agent
  href: https://artifacts.apis.io/moveworks/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/moveworks/arazzo/moveworks-notify-employees.yml
  title: ''
  type: Arazzo
  url: arazzo/moveworks-notify-employees.yml
- group: design
  href: https://artifacts.apis.io/moveworks/arazzo/moveworks-conversation.yml
  title: ''
  type: Arazzo
  url: arazzo/moveworks-conversation.yml
created: '2026-07-17'
description: Moveworks is an enterprise agentic AI assistant platform that lets employees search and act across 100+ business applications (Slack, ServiceNow, Workday, Jira, Salesforce, SAP, Microsoft) through conversational AI agents. Its "Build with Moveworks" developer platform and Agent Studio expose REST APIs to send events and proactive messages, drive AI Assistant conversations (including streaming), export analytics data, and receive inbound webhooks, plus a set of customer-hosted gateways (Content, Identity, Knowledge, Forms) that feed enterprise data to the AI. All APIs use HTTP Bearer authentication with OAuth 2.0 Client Credentials issuing short-lived access tokens, are published as OpenAPI 3.1 with a discoverable /.well-known/api-catalog, and are deployed across US, EU, Canada, GovCloud (FedRAMP), Japan and UK regions.
finops:
- has_sources: true
  method: derived
  name: Moveworks Finops
  primary_unit: ''
  service_category: ''
  slug: moveworks-finops
  template: true
image: https://www.moveworks.com/content/dam/images/internal/open-graph/moveworks-open-graph-homepage-v2.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at help.moveworks.com.
  name: Moveworks MCP Server
  slug: moveworks-mcp-yml
modified: '2026-07-20'
name: Moveworks
nav: Providers
network: true
overview: 'Moveworks publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Conversations API, Deprecated API, and 13 more. Tagged areas include Company, Artificial Intelligence, AI Agents, AI Assistant, and Enterprise Automation.


  The Moveworks catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Moveworks'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 40 more developer resources.'
plans:
- name: Moveworks Plans Pricing
  plan_count: 0
  slug: moveworks-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Moveworks API Rules
  rule_count: 59
  severity_counts:
    error: 37
    hint: 0
    info: 7
    warn: 15
  slug: moveworks-rules
score:
  band: strong
  composite: 59.3
  coverage:
    artifact_dirs: 28
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 47.4
    contract_governance: 31.8
    contract_quality: 60.2
    developer_ergonomics: 58.9
    discoverability: 80.0
    operational_transparency: 65.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 58.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 85.7
      derived: 1
      marker_coverage: 100.0
      total: 16
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: fedramp
    jurisdictions_satisfied: 2
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 40.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/moveworks/moveworks-2026-08-07T184356.png
security:
- kind: authentication
  name: Moveworks Authentication
  slug: moveworks-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Moveworks Domain Security
  slug: moveworks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Moveworks Vulnerability Disclosure
  slug: moveworks-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Moveworks Trust Center
  slug: moveworks-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, ISO 27017, ISO 27018, ISO 27701, ISO 42001, CSA STAR Level 2, FedRAMP, GDPR, CCPA
skill_count: 2
skills:
- name: Drive an AI Assistant conversation
  slug: moveworks-drive-conversation
- name: Notify employees for an event
  slug: moveworks-notify-employees
slug: moveworks
tags:
- Company
- Artificial Intelligence
- AI Agents
- AI Assistant
- Enterprise Automation
- Conversational AI
- Employee Experience
- ITSM
- Enterprise Search
website: https://www.moveworks.com
---
