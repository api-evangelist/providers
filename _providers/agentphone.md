---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Agentphone Agentic Access
  operation_count: 67
  slug: agentphone-agentic-access
  summary_line: 67 operations · 32 acting
api_count: 2
apis:
- baseURL: https://api.agentphone.ai
  baseurl_source: declared
  description: The agent-webhooks API from AgentPhone — 3 operation(s) for agent-webhooks.
  name: AgentPhone Agent Webhooks API
  slug: agentphone-agent-webhooks-api
- baseURL: https://api.agentphone.ai
  baseurl_source: declared
  description: The agents API from AgentPhone — 7 operation(s) for agents.
  name: AgentPhone Agents API
  slug: agentphone-agents-api
- baseURL: https://api.agentphone.ai
  baseurl_source: declared
  description: The calls API from AgentPhone — 8 operation(s) for calls.
  name: AgentPhone Calls API
  slug: agentphone-calls-api
- baseURL: https://api.agentphone.ai
  baseurl_source: declared
  description: The contacts API from AgentPhone — 3 operation(s) for contacts.
  name: AgentPhone Contacts API
  slug: agentphone-contacts-api
- baseURL: https://api.agentphone.ai
  baseurl_source: declared
  description: The conversations API from AgentPhone — 5 operation(s) for conversations.
  name: AgentPhone Conversations API
  slug: agentphone-conversations-api
- baseURL: https://api.agentphone.ai
  baseurl_source: declared
  description: The location API from AgentPhone — 2 operation(s) for location.
  name: AgentPhone Location API
  slug: agentphone-location-api
- baseURL: https://api.agentphone.ai
  baseurl_source: declared
  description: The messages API from AgentPhone — 2 operation(s) for messages.
  name: AgentPhone Messages API
  slug: agentphone-messages-api
- baseURL: https://api.agentphone.ai
  baseurl_source: declared
  description: The numbers API from AgentPhone — 3 operation(s) for numbers.
  name: AgentPhone Numbers API
  slug: agentphone-numbers-api
- baseURL: https://api.agentphone.ai
  baseurl_source: declared
  description: The registration API from AgentPhone — 2 operation(s) for registration.
  name: AgentPhone Registration API
  slug: agentphone-registration-api
- baseURL: https://api.agentphone.ai
  baseurl_source: declared
  description: The usage API from AgentPhone — 5 operation(s) for usage.
  name: AgentPhone Usage API
  slug: agentphone-usage-api
- baseURL: https://api.agentphone.ai
  baseurl_source: declared
  description: The webhooks API from AgentPhone — 5 operation(s) for webhooks.
  name: AgentPhone Webhooks API
  slug: agentphone-webhooks-api
- baseURL: https://api.agentphone.ai
  baseurl_source: declared
  description: The agent-signup API from AgentPhone — 2 operation(s) for agent-signup.
  name: AgentPhone Agent Signup API
  slug: agentphone-agent-signup-api
- baseURL: https://api.agentphone.ai
  baseurl_source: declared
  description: The contact cards API from AgentPhone — 1 operation(s) for contact cards.
  name: AgentPhone contact cards API
  slug: agentphone-contact-cards-api
- baseURL: https://api.agentphone.ai
  baseurl_source: declared
  description: The feedback API from AgentPhone — 1 operation(s) for feedback.
  name: AgentPhone Feedback API
  slug: agentphone-feedback-api
- baseURL: https://api.agentphone.ai
  baseurl_source: declared
  description: The integrations API from AgentPhone — 4 operation(s) for integrations.
  name: AgentPhone Integrations API
  slug: agentphone-integrations-api
- baseURL: https://api.agentphone.ai
  baseurl_source: declared
  description: The sip-trunks API from AgentPhone — 2 operation(s) for sip-trunks.
  name: AgentPhone Sip Trunks API
  slug: agentphone-sip-trunks-api
- baseURL: https://api.agentphone.ai
  baseurl_source: declared
  description: The verification API from AgentPhone — 2 operation(s) for verification.
  name: AgentPhone Verification API
  slug: agentphone-verification-api
- baseURL: https://api.agentphone.ai
  baseurl_source: declared
  description: The whatsapp API from AgentPhone — 6 operation(s) for whatsapp.
  name: AgentPhone WhatsApp API
  slug: agentphone-whatsapp-api
- baseURL: https://api.agentphone.ai
  baseurl_source: declared
  description: The Subaccounts API from AgentPhone — 2 operation(s) for subaccounts.
  name: AgentPhone Subaccounts API
  slug: agentphone-subaccounts-api
artifact_total: 44
asyncapis:
- description: Event surface AgentPhone delivers to a project-level or per-agent webhook URL. Generated by the API Evangelist enrichment pipeline from the published webhook documentation (https://docs.agentphone.ai/
  name: AgentPhone Webhooks
  slug: agentphone-webhooks-asyncapi
collections:
- collection_type: open
  name: API Reference agent-webhooks API
  slug: open-agentphone-agent-webhooks-api
- collection_type: open
  name: API Reference agent-webhooks agents API
  slug: open-agentphone-agents-api
- collection_type: open
  name: API Reference agent-webhooks calls API
  slug: open-agentphone-calls-api
- collection_type: open
  name: API Reference agent-webhooks contactCards API
  slug: open-agentphone-contactcards-api
- collection_type: open
  name: API Reference agent-webhooks contacts API
  slug: open-agentphone-contacts-api
- collection_type: open
  name: API Reference agent-webhooks conversations API
  slug: open-agentphone-conversations-api
- collection_type: open
  name: API Reference agent-webhooks location API
  slug: open-agentphone-location-api
- collection_type: open
  name: API Reference agent-webhooks messages API
  slug: open-agentphone-messages-api
- collection_type: open
  name: API Reference agent-webhooks numbers API
  slug: open-agentphone-numbers-api
- collection_type: open
  name: API Reference agent-webhooks registration API
  slug: open-agentphone-registration-api
- collection_type: open
  name: API Reference agent-webhooks sub-accounts API
  slug: open-agentphone-sub-accounts-api
- collection_type: open
  name: API Reference agent-webhooks usage API
  slug: open-agentphone-usage-api
- collection_type: open
  name: API Reference agent webhooks API
  slug: open-agentphone-webhooks-api
common:
- group: company
  title: ''
  type: Blog
  url: https://www.agentphone.ai/blog
- group: commercial
  href: https://artifacts.apis.io/agentphone/plans/agentphone-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentphone-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.agentphone.ai/
- group: other
  href: https://artifacts.apis.io/agentphone/capabilities/agentphone-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/agentphone-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/agentphone/overlays/agentphone-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/agentphone-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/agentphone/security/agentphone-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentphone-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/agentphone/agentic-access/agentphone-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentphone-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/agentphone/authentication/agentphone-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentphone-authentication.yml
- group: build
  href: https://artifacts.apis.io/agentphone/packages/agentphone-packages.yml
  title: ''
  type: Packages
  url: packages/agentphone-packages.yml
- group: build
  href: https://artifacts.apis.io/agentphone/packages/agentphone-packages.yml
  title: ''
  type: SDKs
  url: packages/agentphone-packages.yml
- group: agent
  href: https://artifacts.apis.io/agentphone/well-known/agentphone-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentphone-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentphone/well-known/agentphone-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/agentphone-api-catalog.json
- group: agent
  href: https://artifacts.apis.io/agentphone/mcp/agentphone-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentphone-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentphone/llms/agentphone-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentphone-llms.txt
- group: design
  href: https://artifacts.apis.io/agentphone/conformance/agentphone-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentphone-conformance.yml
- group: design
  href: https://artifacts.apis.io/agentphone/errors/agentphone-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentphone-error-codes.yml
- group: design
  href: https://artifacts.apis.io/agentphone/lifecycle/agentphone-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agentphone-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/agentphone/conventions/agentphone-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentphone-conventions.yml
- group: design
  href: https://artifacts.apis.io/agentphone/conventions/agentphone-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agentphone-conventions.yml
- group: operate
  href: https://artifacts.apis.io/agentphone/rate-limits/agentphone-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agentphone-rate-limits.yml
- group: start
  href: https://artifacts.apis.io/agentphone/sandbox/agentphone-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/agentphone-sandbox.yml
- group: design
  href: https://artifacts.apis.io/agentphone/data-model/agentphone-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentphone-data-model.yml
- group: docs
  href: https://artifacts.apis.io/agentphone/asyncapi/agentphone-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/agentphone-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/agentphone/asyncapi/agentphone-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/agentphone-webhooks-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/agentphone/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.agentphone.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agentphone.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.agentphone.ai/welcome
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AgentPhone-AI
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/sbNJDZbYmn
- group: commercial
  title: ''
  type: Pricing
  url: https://agentphone.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://agentphone.ai/signup
- group: start
  title: ''
  type: Login
  url: https://agentphone.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentphone.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentphone.ai/privacy
created: '2026-07-17'
description: AgentPhone is the telephony infrastructure layer for AI agents. A single REST API provisions real US/Canada phone numbers for agents with voice calling, SMS, MMS, and iMessage built in, plus unified webhooks, automatic conversation threading, real-time call transcription, hosted-LLM or webhook voice modes, and 10DLC/A2P compliance handled for you. Official Python and TypeScript SDKs and a published MCP server let agents buy numbers, place calls, and send messages through natural language. Founded 2026 (Y Combinator), used by teams at Google ADK, Replit, LangChain, Sim AI, and Alchemy.
finops:
- has_sources: true
  method: derived
  name: Agentphone Finops
  primary_unit: ''
  service_category: ''
  slug: agentphone-finops
  template: true
image: https://agentphone.ai/favicon.png?v=3
layout: provider
mcp_servers:
- description: Local (stdio) MCP server; 26 tools listed.
  name: AgentPhone MCP Server
  slug: agentphone
modified: '2026-10-06'
name: AgentPhone
nav: Providers
network: true
overview: 'AgentPhone publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Webhooks API, Agents API, Calls API, and 16 more. Tagged areas include Company, Telephony, Phone Numbers, SMS, and Voice.


  The AgentPhone catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  AgentPhone''s developer surface includes engineering blog, authentication, sandbox, documentation, getting-started guide, support, pricing, and 28 more developer resources.'
plans:
- name: Agentphone Plans Pricing
  plan_count: 0
  slug: agentphone-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Agentphone Rate Limits
  slug: agentphone-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: AgentPhone API Rules
  rule_count: 50
  severity_counts:
    error: 40
    hint: 0
    info: 3
    warn: 7
  slug: agentphone-rules
score:
  band: developing
  composite: 54.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.2
  facets:
    access_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 57.1
    developer_ergonomics: 78.6
    discoverability: 73.2
    operational_transparency: 10.5
  previous_composite: 46.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 43.3
      derived: 0
      marker_coverage: 0.0
      total: 32
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 20.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/agentphone/agentphone-2026-07-25T195242.png
security:
- kind: authentication
  name: Agentphone Authentication
  slug: agentphone-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Agentphone Domain Security
  slug: agentphone-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Place an outbound call and read the transcript
  slug: agentphone-place-call-and-get-transcript
- name: Provision a number and send an SMS
  slug: agentphone-provision-and-text
- name: agentphone
  slug: agentphone-published-skill
slug: agentphone
tags:
- Company
- Telephony
- Phone Numbers
- SMS
- Voice
- AI Agents
- Messaging
- Communications
- Webhook
- MCP
- iMessage
website: https://www.agentphone.ai/
---
