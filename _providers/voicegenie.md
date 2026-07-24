---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 71.2
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Voicegenie Agentic Access
  operation_count: 7
  slug: voicegenie-agentic-access
  summary_line: 7 operations · 7 acting
api_count: 2
apis:
- description: Place and track voice calls.
  name: VoiceGenie Calls API
  slug: voicegenie-calls-api
- description: Manage outbound/inbound campaigns and their contacts.
  name: VoiceGenie Campaigns API
  slug: voicegenie-campaigns-api
artifact_total: 7
asyncapis:
- description: ''
  name: Voicegenie Webhooks
  slug: voicegenie-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://voicegenie.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://voicegenie.gitbook.io/voicegenie-ai
- group: docs
  title: ''
  type: Documentation
  url: https://voicegenie.gitbook.io/voicegenie-ai/developer-documentation-1.0
- group: docs
  title: ''
  type: APIReference
  url: https://voicegenie.gitbook.io/voicegenie-ai/integrations/public-api-integration
- group: start
  title: ''
  type: GettingStarted
  url: https://voicegenie.gitbook.io/voicegenie-ai/welcome-to-voicegenie-ai
- group: company
  title: ''
  type: Blog
  url: https://blogs.voicegenie.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://voicegenie.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.voicegenie.ai/
- group: start
  title: ''
  type: Login
  url: https://app.voicegenie.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://voicegenie.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://voicegenie.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:support@voicegenie.ai
- group: start
  title: ''
  type: Demo
  url: https://cal.com/voicegenie/demo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/voicegenie
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/voicegenie_ai
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@VoiceGenieAI
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/voicegenie.ai/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/voicegenie-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/voicegenie-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/voicegenie-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/voicegenie-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/voicegenie-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/voicegenie-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/voicegenie-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voicegenie-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/voicegenie-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/voicegenie-webhooks.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/voicegenie-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: VoiceGenie (Ori Labs Ltd.) is a conversational voice AI platform for sales automation that lets teams deploy AI voice agents to run outbound and inbound phone calls end to end. Businesses build assistants (voice bots) with a chosen voice, language, script and knowledge base, attach a phone number (via Twilio or Plivo), upload contact lists, and launch campaigns that qualify leads, book meetings, send SMS, run surveys, chase payment reminders, and hand off to human agents when needed. VoiceGenie exposes a Public REST API on core-saas.voicegenie.ai for placing calls, adding calls to recurring campaigns, pausing/resuming campaigns, fetching call analysis and status, retrieving inbound-call updates, checking transfer status, and removing customers from campaigns, plus a post-call analysis webhook, so voice workflows can be automated from n8n, Zapier, Zoho Flow, HubSpot, HighLevel, Cal.com and custom applications.
image: https://voicegenie.ai/images/vg_logo_name.svg
layout: provider
mcp_servers:
- description: ''
  name: voicegenie-mcp.yml
  slug: voicegenie-mcpyml
modified: '2026-07-21'
name: VoiceGenie
nav: Providers
network: true
overview: 'VoiceGenie publishes 2 APIs on the [APIs.io](https://apis.io/) network: Calls API and Campaigns API. Tagged areas include Company, Voice AI, Conversational AI, Sales Automation, and Voice Agents.


  The VoiceGenie catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  VoiceGenie''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 22 more developer resources.'
random_paper: 34
score:
  band: developing
  composite: 49.3
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 66.4
    developer_ergonomics: 67.4
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 49.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Voicegenie Authentication
  slug: voicegenie-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Voicegenie Domain Security
  slug: voicegenie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: voicegenie
tags:
- Company
- Voice AI
- Conversational AI
- Sales Automation
- Voice Agents
- Telephony
- Call Center
- Customer Support
- Lead Generation
- Webhooks
website: https://voicegenie.ai
---
