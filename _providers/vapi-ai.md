---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
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
    well_known_catalog: true
  schema_version: 0.2
  score: 55.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 48
  human_in_the_loop: 48
  name: Vapi Ai Agentic Access
  operation_count: 86
  slug: vapi-ai-agentic-access
  summary_line: 86 operations · 48 acting · 48 human-in-the-loop
api_count: 15
apis:
- description: Analytics endpoints.
  name: Vapi Analytics API
  slug: vapi-ai-analytics-api
- description: Assistants endpoints.
  name: Vapi Assistants API
  slug: vapi-ai-assistants-api
- description: Calls endpoints.
  name: Vapi Calls API
  slug: vapi-ai-calls-api
- description: Campaigns endpoints.
  name: Vapi Campaigns API
  slug: vapi-ai-campaigns-api
- description: Chats endpoints.
  name: Vapi Chats API
  slug: vapi-ai-chats-api
- description: Eval endpoints.
  name: Vapi Eval API
  slug: vapi-ai-eval-api
- description: Files endpoints.
  name: Vapi Files API
  slug: vapi-ai-files-api
- description: Insight endpoints.
  name: Vapi Insight API
  slug: vapi-ai-insight-api
- description: Observability/Scorecard endpoints.
  name: Vapi Observability/Scorecard API
  slug: vapi-ai-observability-scorecard-api
- description: Phone Numbers endpoints.
  name: Vapi Phone Numbers API
  slug: vapi-ai-phone-numbers-api
- description: Provider Resources endpoints.
  name: Vapi Provider Resources API
  slug: vapi-ai-provider-resources-api
- description: Sessions endpoints.
  name: Vapi Sessions API
  slug: vapi-ai-sessions-api
- description: Squads endpoints.
  name: Vapi Squads API
  slug: vapi-ai-squads-api
- description: Structured Outputs endpoints.
  name: Vapi Structured Outputs API
  slug: vapi-ai-structured-outputs-api
- description: Tools endpoints.
  name: Vapi Tools API
  slug: vapi-ai-tools-api
arazzos:
- description: Create an assistant, provision a Vapi phone number, place an outbound call, and poll until it ends.
  name: Vapi Assistant Outbound Call End to End
  slug: vapi-ai-assistant-phone-outbound-call-workflow
- description: Create two specialized assistants and assemble them into a squad that can hand calls between them.
  name: Vapi Build a Multi-Assistant Squad
  slug: vapi-ai-build-squad-workflow
- description: Place an outbound call, poll it to completion, then query call analytics for cost and duration.
  name: Vapi Outbound Call Then Cost Analytics
  slug: vapi-ai-call-then-analytics-workflow
- description: Create a voice AI assistant and read it back to confirm it was provisioned.
  name: Vapi Create and Verify Assistant
  slug: vapi-ai-create-assistant-workflow
- description: Create a custom function tool and attach it to a freshly created assistant.
  name: Vapi Create Function Tool and Attach to Assistant
  slug: vapi-ai-create-tool-attach-assistant-workflow
- description: Upload a file, build a query tool knowledge base from it, and create an assistant that uses it.
  name: Vapi File-Backed Knowledge Base Assistant
  slug: vapi-ai-file-knowledge-base-assistant-workflow
- description: Create an assistant and import an existing Twilio number that routes inbound calls to it.
  name: Vapi Import Twilio Number and Bind Assistant
  slug: vapi-ai-import-twilio-number-workflow
- description: Build a two-assistant squad, place an outbound call to it, and poll until the call ends.
  name: Vapi Squad Outbound Call
  slug: vapi-ai-squad-outbound-call-workflow
artifact_total: 121
asyncapis:
- description: 'AsyncAPI description of Vapi''s realtime surfaces: 1. The WebSocket Transport (`wss://api.vapi.ai/{callId}/transport`) used to stream binary audio and JSON control messages to and from an active call. '
  name: Vapi Realtime API (WebSocket Transport + Server URL Events)
  slug: vapi-asyncapi
collections:
- collection_type: postman
  name: Vapi Analytics API
  slug: postman-vapi-analytics-api
- collection_type: postman
  name: Vapi Assistants API
  slug: postman-vapi-assistants-api
- collection_type: postman
  name: Vapi Calls API
  slug: postman-vapi-calls-api
- collection_type: postman
  name: Vapi Campaigns API
  slug: postman-vapi-campaigns-api
- collection_type: postman
  name: Vapi Chats API
  slug: postman-vapi-chats-api
- collection_type: postman
  name: Vapi Eval API
  slug: postman-vapi-eval-api
- collection_type: postman
  name: Vapi Files API
  slug: postman-vapi-files-api
- collection_type: postman
  name: Vapi Insight API
  slug: postman-vapi-insight-api
- collection_type: postman
  name: Vapi Observability/Scorecard API
  slug: postman-vapi-observability-api
- collection_type: postman
  name: Vapi Phone Numbers API
  slug: postman-vapi-phone-numbers-api
- collection_type: postman
  name: Vapi Provider Resources API
  slug: postman-vapi-provider-resources-api
- collection_type: postman
  name: Vapi Sessions API
  slug: postman-vapi-sessions-api
- collection_type: postman
  name: Vapi Squads API
  slug: postman-vapi-squads-api
- collection_type: postman
  name: Vapi Structured Outputs API
  slug: postman-vapi-structured-outputs-api
- collection_type: postman
  name: Vapi Tools API
  slug: postman-vapi-tools-api
- collection_type: open
  name: Vapi Analytics API
  slug: open-vapi-analytics-api
- collection_type: open
  name: Vapi Assistants API
  slug: open-vapi-assistants-api
- collection_type: open
  name: Vapi Calls API
  slug: open-vapi-calls-api
- collection_type: open
  name: Vapi Campaigns API
  slug: open-vapi-campaigns-api
- collection_type: open
  name: Vapi Chats API
  slug: open-vapi-chats-api
- collection_type: open
  name: Vapi Eval API
  slug: open-vapi-eval-api
- collection_type: open
  name: Vapi Files API
  slug: open-vapi-files-api
- collection_type: open
  name: Vapi Insight API
  slug: open-vapi-insight-api
- collection_type: open
  name: Vapi Observability/Scorecard API
  slug: open-vapi-observability-api
- collection_type: open
  name: Vapi Phone Numbers API
  slug: open-vapi-phone-numbers-api
- collection_type: open
  name: Vapi Provider Resources API
  slug: open-vapi-provider-resources-api
- collection_type: open
  name: Vapi Sessions API
  slug: open-vapi-sessions-api
- collection_type: open
  name: Vapi Squads API
  slug: open-vapi-squads-api
- collection_type: open
  name: Vapi Structured Outputs API
  slug: open-vapi-structured-outputs-api
- collection_type: open
  name: Vapi Tools API
  slug: open-vapi-tools-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vapi-ai-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/vapi-ai-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vapi-ai-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vapi-ai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vapi-ai-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/vapi-ai-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vapi-ai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vapi-ai-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vapi-ai-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/vapi-ai-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/vapi-ai-cli.yml
- group: design
  title: ''
  type: Components
  url: components/vapi-ai-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vapi-ai-data-model.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/vapi-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vapi-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vapi-ai-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/vapi/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vapi-ai-assistant-phone-outbound-call-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vapi-ai-build-squad-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vapi-ai-call-then-analytics-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vapi-ai-create-assistant-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vapi-ai-create-tool-attach-assistant-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vapi-ai-file-knowledge-base-assistant-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vapi-ai-import-twilio-number-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vapi-ai-squad-outbound-call-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://vapi.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vapi.ai
- group: docs
  title: ''
  type: Documentation
  url: https://api.vapi.ai/api
- group: docs
  title: ''
  type: OpenAPI
  url: https://api.vapi.ai/api-json
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.vapi.ai/quickstart
- group: start
  title: ''
  type: Signup
  url: https://dashboard.vapi.ai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vapi.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://vapi.ai/pricing
- group: operate
  title: ''
  type: Forums
  url: https://discord.gg/pUFNcf2WmH
- group: company
  title: ''
  type: Blog
  url: https://vapi.ai/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://vapi.ai/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VapiAI
- group: build
  title: ''
  type: SDKs
  url: https://github.com/VapiAI/server-sdk-typescript
- group: build
  title: ''
  type: SDKs
  url: https://github.com/VapiAI/server-sdk-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/VapiAI/server-sdk-csharp
- group: build
  title: ''
  type: SDKs
  url: https://github.com/VapiAI/server-sdk-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/VapiAI/server-sdk-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/VapiAI/client-sdk-web
- group: build
  title: ''
  type: SDKs
  url: https://github.com/VapiAI/client-sdk-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/VapiAI/client-sdk-react-native
- group: build
  title: ''
  type: SDKs
  url: https://github.com/VapiAI/client-sdk-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/VapiAI/client-sdk-html-script-tag
- group: build
  title: ''
  type: Tools
  url: https://github.com/VapiAI/mcp-server
- group: build
  title: ''
  type: Tools
  url: https://github.com/VapiAI/skills
- group: build
  title: ''
  type: Tools
  url: https://github.com/VapiAI/gitops
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/VapiAI/docs
- group: design
  title: ''
  type: Webhooks
  url: https://docs.vapi.ai/server-url
- group: design
  title: ''
  type: Webhooks
  url: https://docs.vapi.ai/server-url/events
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/vapi-asyncapi.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.vapi.ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vapi.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vapi.ai/terms-of-service
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vapi.ai/aup
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Vapi_AI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vapi-ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.ycombinator.com/companies/vapi
- group: commercial
  title: ''
  type: Plans
  url: plans/vapi-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vapi-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vapi-ai-finops.yml
created: '2026-05-24T00:00:00.000Z'
description: Vapi is a San Francisco-based voice AI platform that lets developers build real-time, low-latency voice agents over phone, web, and SIP. It orchestrates three modular components — a transcriber (STT), an LLM, and a voice (TTS) — into a sub-700ms voice-to-voice pipeline, with first-class support for tools/function calling, multi-agent squads, outbound campaigns, persistent sessions, structured outputs, recording artifacts, evaluation scorecards, and a full REST API plus official SDKs in TypeScript, Python, C#, Ruby, PHP, and client SDKs for Web, React Native, iOS, and Python. Vapi is a Y Combinator company.
examples:
- key_count: 8
  name: Vapi Assistant Example
  slug: vapi-assistant-example
- key_count: 8
  name: Vapi Call Example
  slug: vapi-call-example
- key_count: 8
  name: Vapi Campaign Example
  slug: vapi-campaign-example
- key_count: 8
  name: Vapi Chat Example
  slug: vapi-chat-example
- key_count: 8
  name: Vapi Eval Example
  slug: vapi-eval-example
- key_count: 8
  name: Vapi File Example
  slug: vapi-file-example
- key_count: 7
  name: Vapi Insight Example
  slug: vapi-insight-example
- key_count: 8
  name: Vapi Phone Number Example
  slug: vapi-phone-number-example
- key_count: 8
  name: Vapi Scorecard Example
  slug: vapi-scorecard-example
- key_count: 8
  name: Vapi Session Example
  slug: vapi-session-example
- key_count: 7
  name: Vapi Squad Example
  slug: vapi-squad-example
- key_count: 8
  name: Vapi Structured Output Example
  slug: vapi-structured-output-example
- key_count: 8
  name: Vapi Tool Example
  slug: vapi-tool-example
features:
- Sub-700ms voice-to-voice latency orchestration layer
- Transcriber + LLM + voice (TTS) modular pipeline with multi-provider choice
- Bring your own provider keys to pay providers at cost
- Assistants, Squads (multi-agent handoff), Sessions (persistent state)
- Inbound and outbound calling over Twilio, Telnyx, Vonage, vapi.phoneNumber, and SIP
- Campaigns for batched outbound calling with concurrency/retry
- Tools (function, transfer-call, end-call, DTMF, hangup, voicemail, MCP, query, Make, Zapier, GHL, KB)
- Server URL webhooks for real-time call events and function execution
- Per-call mono/stereo/customer/assistant/video recordings, PCAP packet captures, call logs
- Analytics, Insights, Observability Scorecards, and Evals for production monitoring and regression testing
- Structured Outputs for JSON-schema-constrained extraction from calls
- Chats API (text channel) and OpenAI-compatible /chat/responses
- Official SDKs - server (TS, Python, C#, Ruby, PHP) and client (Web, Python, React Native, iOS, HTML)
- Vapi MCP Server for Model Context Protocol integration
- HIPAA and Zero Data Retention add-ons; SOC2 and PCI on Scale plan
- $0.05/min Vapi orchestration fee on Build plan; model and voice costs passed at cost
finops:
- name: Vapi Ai Finops
  service_category: AI and Machine Learning
  slug: vapi-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vapi-ai.png
json_schemas:
- name: Vapi Assistant
  property_count: 30
  slug: vapi-assistant
- name: Vapi Call
  property_count: 30
  slug: vapi-call
- name: Vapi Campaign
  property_count: 20
  slug: vapi-campaign
- name: Vapi Chat
  property_count: 18
  slug: vapi-chat
- name: Vapi Eval
  property_count: 8
  slug: vapi-eval
- name: Vapi File
  property_count: 18
  slug: vapi-file
- name: Vapi Insight
  property_count: 7
  slug: vapi-insight
- name: Vapi ByoPhoneNumber
  property_count: 16
  slug: vapi-phone-number
- name: Vapi Scorecard
  property_count: 8
  slug: vapi-scorecard
- name: Vapi Session
  property_count: 20
  slug: vapi-session
- name: Vapi Squad
  property_count: 7
  slug: vapi-squad
- name: Vapi StructuredOutput
  property_count: 13
  slug: vapi-structured-output
- name: Vapi FunctionTool
  property_count: 12
  slug: vapi-tool
json_structures:
- name: Vapi Assistant Structure
  property_count: 30
  slug: vapi-assistant-structure
- name: Vapi Call Structure
  property_count: 30
  slug: vapi-call-structure
- name: Vapi Campaign Structure
  property_count: 20
  slug: vapi-campaign-structure
- name: Vapi Chat Structure
  property_count: 18
  slug: vapi-chat-structure
- name: Vapi Eval Structure
  property_count: 8
  slug: vapi-eval-structure
- name: Vapi File Structure
  property_count: 18
  slug: vapi-file-structure
- name: Vapi Insight Structure
  property_count: 7
  slug: vapi-insight-structure
- name: Vapi Phone Number Structure
  property_count: 16
  slug: vapi-phone-number-structure
- name: Vapi Scorecard Structure
  property_count: 8
  slug: vapi-scorecard-structure
- name: Vapi Session Structure
  property_count: 20
  slug: vapi-session-structure
- name: Vapi Squad Structure
  property_count: 7
  slug: vapi-squad-structure
- name: Vapi Structured Output Structure
  property_count: 13
  slug: vapi-structured-output-structure
- name: Vapi Tool Structure
  property_count: 12
  slug: vapi-tool-structure
jsonld:
- class_count: 0
  name: Vapi Ai Context
  property_count: 12
  slug: vapi-ai-context
layout: provider
mcp_servers:
- description: ''
  name: vapi-ai-mcp.yml
  slug: vapi-ai-mcpyml
modified: '2026-06-20'
name: Vapi
nav: Providers
network: true
overview: 'Vapi publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Assistants API, Calls API, and 12 more. Tagged areas include AI, Voice AI, Voice Agents, Conversational AI, and Telephony.


  The Vapi catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Vapi''s developer surface includes changelog, CLI, authentication, developer portal, documentation, getting-started guide, signup flow, and 57 more developer resources.'
plans:
- name: Vapi Ai Plans Pricing
  plan_count: 4
  slug: vapi-ai-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 4
  name: Vapi Ai Rate Limits
  slug: vapi-ai-rate-limits
rules:
- name: Vapi API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: vapi-ai-asyncapi-spectral-rules
- name: Vapi API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: vapi-ai-jsonschema-spectral-rules
- name: Vapi API Rules
  rule_count: 17
  severity_counts:
    error: 11
    hint: 0
    info: 0
    warn: 6
  slug: vapi-ai-rules
score:
  band: exemplar
  composite: 74.8
  delta: -0.6
  facets:
    commercial_clarity: 78.9
    contract_quality: 76.0
    developer_ergonomics: 76.1
    discoverability: 77.8
    governance: 59.4
    operational_transparency: 76.3
  previous_composite: 75.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vapi-ai/refs/heads/main/screenshots/vapi-ai-2026-06-20T200922.png
security:
- kind: authentication
  name: Vapi Ai Authentication
  slug: vapi-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vapi Ai Domain Security
  slug: vapi-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Vapi Ai Trust Center
  slug: vapi-ai-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
slug: vapi-ai
tags:
- AI
- Voice AI
- Voice Agents
- Conversational AI
- Telephony
- Real-Time
- Transcription
- Text-to-Speech
- LLM
- Agents
- MCP
website: https://vapi.ai
---
