---
access_model:
  confidence: high
  label: Public, self-service with a free trial
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://kudosity.com/pricing
  - https://kudosity.com/trial
  - https://developers.kudosity.com/docs/getting-started
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 42
  human_in_the_loop: 0
  name: Kudosity Agentic Access
  operation_count: 57
  slug: kudosity-agentic-access
  summary_line: 57 operations · 42 acting
api_count: 2
apis:
- description: Current v2 REST API covering SMS, MMS, WhatsApp and RCS, plus API-managed webhooks with event-type filtering and sender registration with phone verification. 22 operations across 15 paths, OpenAPI 3.0
  name: Transmit Message API
  slug: transmit-message-api
- description: 'Classic v1 REST API — fully supported, not deprecated. SMS sending with single-request multi-recipient batches and custom tracked-link domains, plus everything v2 does not carry: contacts, lists and c'
  name: Transmit SMS API
  slug: transmit-sms-api
artifact_total: 13
asyncapis:
- description: ''
  name: Kudosity Webhooks
  slug: kudosity-webhooks
collections:
- collection_type: postman
  name: Transmit Message API
  slug: postman-kudosity-transmit-message-openapi-original
- collection_type: postman
  name: Transmit SMS API
  slug: postman-kudosity-transmit-sms-openapi-original
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/kudosity/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.kudosity.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.kudosity.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.kudosity.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.kudosity.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.kudosity.com/s/
- group: company
  title: ''
  type: Blog
  url: https://kudosity.com/resources/articles
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kudosity
- group: commercial
  title: ''
  type: Pricing
  url: https://kudosity.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://kudosity.com/trial
- group: start
  title: ''
  type: Login
  url: https://app.transmitsms.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kudosity.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kudosity.com/legal/privacy-policy
- group: operate
  title: ''
  type: SLA
  url: https://kudosity.com/legal/service-level-agreement
- group: auth
  title: ''
  type: Compliance
  url: https://trust.kudosity.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/kudosity-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://trust.kudosity.com/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kudosity-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kudosity-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kudosity-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kudosity-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kudosity-mcp.yml
- group: agent
  title: ''
  type: MCP
  url: https://developers.kudosity.com/mcp
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/kudosity-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kudosity-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kudosity-website-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kudosity-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kudosity-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/kudosity-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kudosity-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kudosity-conventions.yml
- group: build
  title: ''
  type: Examples
  url: examples/kudosity-examples.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kudosity-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kudosity-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kudosity-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.kudosity.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kudosity-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kudosity-plans.yml
- group: build
  title: ''
  type: Packages
  url: packages/kudosity-packages.yml
- group: build
  title: ''
  type: Postman
  url: https://developers.kudosity.com/reference/postman
- group: agent
  title: ''
  type: AgentSkills
  url: https://developers.kudosity.com/docs/claude-plugin
- group: agent
  title: ''
  type: AgentSkills
  url: https://developers.kudosity.com/docs/copilot-extension
- group: agent
  title: ''
  type: AgentSkills
  url: https://developers.kudosity.com/docs/gemini-extension
- group: agent
  title: ''
  type: AgentSkills
  url: https://developers.kudosity.com/docs/openclaw-plugin
- group: agent
  title: ''
  type: AgentSkills
  url: https://developers.kudosity.com/docs/sms-action
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/kudosity/ai-agent-examples
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/kudosity/mcp
created: '2026-07-11'
description: 'Kudosity is an Australian business messaging platform — formerly Burst SMS / TransmitSMS — running two live public REST APIs on two hosts. The Transmit Message API (v2) covers SMS, MMS, WhatsApp and RCS with API-managed webhooks and sender registration; the Transmit SMS API (v1) carries contacts, lists, dedicated virtual numbers, keywords, email-to-SMS and all reporting. Both share one account, one set of senders and one bill. Both ship public OpenAPI documents. What makes Kudosity unusual for its size is the agent-native surface layered on top: a hosted MCP server whose tools/list answers without credentials, llms.txt on both the docs and marketing hosts with per-section fan-out, and five published agent integrations — a Claude Code plugin, a GitHub Copilot extension, a Gemini CLI extension, an OpenClaw channel plugin and an SMS GitHub Action — all open source in a public GitHub organization. RCS is in beta; there is no voice product, no sandbox and no idempotency key.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kudosity.png
layout: provider
mcp_servers:
- description: ''
  name: kudosity-mcp.yml
  slug: kudosity-mcpyml
modified: '2026-07-27'
name: Kudosity
nav: Providers
network: true
overview: 'Kudosity publishes 2 APIs on the [APIs.io](https://apis.io/) network: Transmit Message API and Transmit SMS API. Tagged areas include Messaging, SMS, MMS, RCS, and WhatsApp.


  The Kudosity catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kudosity''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 41 more developer resources.'
plans:
- name: Kudosity Plans
  plan_count: 4
  slug: kudosity-plans
random_paper: 45
rate_limits:
- limit_count: 0
  name: Kudosity Rate Limits
  slug: kudosity-rate-limits
score:
  band: strong
  composite: 57.6
  delta: -4.6
  facets:
    commercial_clarity: 92.1
    contract_quality: 51.6
    developer_ergonomics: 66.8
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 39.5
  previous_composite: 62.2
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 50.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kudosity/refs/heads/main/screenshots/kudosity-2026-07-27T062805.png
security:
- kind: authentication
  name: Kudosity Authentication
  slug: kudosity-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Kudosity Domain Security
  slug: kudosity-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kudosity Vulnerability Disclosure
  slug: kudosity-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Kudosity Trust Center
  slug: kudosity-trust-center
  summary_line: SOC 2, ISO 27001
slug: kudosity
tags:
- Messaging
- SMS
- MMS
- RCS
- WhatsApp
- Communications
- CPaaS
- Webhooks
- MCP
- Agent-native
- Australia
- Notifications
- Two-Way Messaging
- Contact Management
website: https://developers.kudosity.com
---
