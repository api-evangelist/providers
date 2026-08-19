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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: true
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Avoca Agentic Access
  operation_count: 31
  slug: avoca-agentic-access
  summary_line: 31 operations
api_count: 8
apis:
- description: v1 funnel, UTM, service-area, and issue-type analytics
  name: Avoca Analytics (v1) API
  slug: avoca-analytics-v1-api
- description: Call records, transcripts, and pre-call transfers
  name: Avoca Calls API
  slug: avoca-calls-api
- description: Coach (QA) call evaluations and rubrics
  name: Avoca Coach API
  slug: avoca-coach-api
- description: Unified leads (v0) and the canonical leads feed (v1)
  name: Avoca Leads API
  slug: avoca-leads-api
- description: Campaign text and subscription-event feeds for BI ingestion
  name: Avoca Outbound Texting API
  slug: avoca-outbound-texting-api
- description: Simple Scheduler analytics — legacy flat endpoints
  name: Avoca Scheduler Analytics (v0) API
  slug: avoca-scheduler-analytics-v0-api
- description: v1 scheduling-widget sessions and completed bookings
  name: Avoca Sessions & Bookings API
  slug: avoca-sessions-bookings-api
- description: Teams accessible to the API key
  name: Avoca Teams API
  slug: avoca-teams-api
artifact_total: 22
asyncapis:
- description: ''
  name: Avoca Webhooks
  slug: avoca-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Avoca Enterprise Analytics (v1) Analytics (v1) Analytics (v1) API
  slug: open-avoca-analytics-v1-api
- collection_type: open
  name: Avoca Enterprise Analytics (v1) Analytics (v1) Calls API
  slug: open-avoca-calls-api
- collection_type: open
  name: Avoca Enterprise Analytics (v1) Analytics (v1) Coach API
  slug: open-avoca-coach-api
- collection_type: open
  name: Avoca Enterprise Analytics (v1) Analytics (v1) Leads API
  slug: open-avoca-leads-api
- collection_type: open
  name: Avoca Enterprise Analytics (v1) Analytics (v1) Outbound Texting API
  slug: open-avoca-outbound-texting-api
- collection_type: open
  name: Avoca Enterprise Analytics (v1) Analytics (v1) Scheduler Analytics (v0) API
  slug: open-avoca-scheduler-analytics-v0-api
- collection_type: open
  name: Avoca Enterprise Analytics (v1) Analytics (v1) Sessions & Bookings API
  slug: open-avoca-sessions-bookings-api
- collection_type: open
  name: Avoca Enterprise Analytics (v1) Analytics (v1) Teams API
  slug: open-avoca-teams-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/avoca-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/avoca-enterprise-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/avoca-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.avoca.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.avoca.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.avoca.ai/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.avoca.ai/api-reference/introduction
- group: auth
  title: ''
  type: Authentication
  url: authentication/avoca-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.avoca.ai/blog
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.avoca.ai/
- group: start
  title: ''
  type: Login
  url: https://dashboard.avoca.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.avoca.ai/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avoca.ai/legal/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.avoca.ai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.avoca.ai
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.avoca.ai/changelog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/avoca-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/avoca-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/avoca-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/avoca-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/avoca-domain-security.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/avoca-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Avoca is "The AI Front Office for Service Businesses" — always-on AI agents that answer inbound calls, texts, and web chats 24/7 for home-services companies (HVAC, plumbing, electrical, pest control, garage door, and construction), book jobs, run multi-channel outbound re-engagement campaigns, score and coach every call, and respond to leads instantly. The company raised a $125M Series B at a $1B valuation and serves 1,000+ service businesses. Avoca publishes an Enterprise API (bearer API-key auth over https://enterprise-api.avoca.ai) that exposes read access to calls, transcripts, leads, teams, coach/QA evaluations, sessions, bookings, outbound texting, and Simple Scheduler analytics, plus HMAC-signed event webhooks and a Speed-to-Lead intake webhook — designed for enterprise partners ingesting Avoca activity into their BI warehouses and CRMs (ServiceTitan, Dialpad, Five9, 3CX).
image: https://www.avoca.ai/og-default.webp
layout: provider
mcp_servers:
- description: ''
  name: avoca-mcp.yml
  slug: avoca-mcpyml
modified: '2026-07-18'
name: Avoca
nav: Providers
network: true
overview: 'Avoca publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Analytics (v1) API, Calls API, Coach API, and 5 more. Tagged areas include Company, AI, Voice AI, Conversational AI, and Customer Service.


  The Avoca catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Avoca''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, signup flow, changelog, and 16 more developer resources.'
random_paper: 75
score:
  band: developing
  composite: 44.4
  delta: -6.2
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 65.1
    developer_ergonomics: 35.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 31.6
  previous_composite: 50.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/avoca/refs/heads/main/screenshots/avoca-2026-07-25T202002.png
security:
- kind: authentication
  name: Avoca Authentication
  slug: avoca-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Avoca Domain Security
  slug: avoca-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: avoca
tags:
- Company
- AI
- Voice AI
- Conversational AI
- Customer Service
- Contact Center
- Home Services
- Field Service
- Scheduling
- Analytics
- Webhooks
- Enterprise API
website: https://docs.avoca.ai
---
