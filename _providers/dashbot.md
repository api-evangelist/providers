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
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 46.5
  scored_at: '2026-08-24'
api_count: 3
apis:
- description: Read API for enriched conversational data. GET /export returns a zipFile handle for all dimension data across a set of bot IDs over a date range, optionally filtered to named prompts; GET /index is th
  name: Dashbot Export API
  slug: dashbot-export-api
- description: Write/ingest API for unstructured customer conversations. POST one message object per call to /track (realtime, timestamp within 24 hours) or /trackhistorical (older data), with platform, version, dir
  name: Dashbot Universal Tracker API
  slug: dashbot-universal-tracker-api
- description: Model Context Protocol endpoint served from the Dimension Labs documentation host. Answers JSON-RPC 2.0; tools/list is authorization-gated for anonymous clients, so the tool set is not publicly enumer
  name: Dimension Labs Documentation MCP
  slug: dashbot-mcp
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Export API
  slug: open-dashbot-export-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.dimensionlabs.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.dimensionlabs.io/docs/dimension-product-guide
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dimensionlabs.io/docs/dimension-product-guide
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dimensionlabs.io/reference/using-the-integration-guides
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dimensionlabs.io/reference/generating-dashbot-api-key
- group: auth
  title: ''
  type: Authentication
  url: authentication/dashbot-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dashbot-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/dashbot-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dashbot-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dashbot-problem-types.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dashbot-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dashbot-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/dashbot-tool-crosswalk.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dashbot-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dashbot-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dashbot-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dashbot-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.dimensionlabs.io/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/dashbot-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dashbot-rate-limits.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/dashbot-export-api-overlay.yaml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/actionably
- group: company
  title: ''
  type: Blog
  url: https://www.dimensionlabs.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dimensionlabs.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dimensionlabs.io/terms-of-service-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dimensionlabs.io/privacy-policy-policy
- group: start
  title: ''
  type: SignUp
  url: https://tally.so/r/pb5Zjb
- group: start
  title: ''
  type: Login
  url: https://next.dimensionlabs.io/
- group: operate
  title: ''
  type: Support
  url: https://docs.dimensionlabs.io/docs/troubleshoting
created: '2026-07-17'
description: Dashbot is a conversational-data analytics platform (now operating as Dimension Labs) that ingests chatbot, voice-assistant, live-chat, call, survey and other unstructured customer conversations and enriches them into structured "dimensions" for causal intelligence and reporting. Data is sent in through a Universal REST tracker and dozens of one-click integrations (Twilio, Slack, Intercom, Zendesk, Salesforce, Amazon Lex/Connect, Google Dialogflow, Genesys, Cognigy, Kore.ai, Rasa, and more), then explored through dashboards, data explorer, flows and an analytics Agent. A REST Export API (api.dimensionlabs.io) and first-party JavaScript, Python and Ruby SDKs let teams pull enriched data back out programmatically. Dashbot was surfaced as a portfolio company of bessemer-venture-partners; the company rebranded to Dimension Labs while the API and SDKs retain the Dashbot name (api.dashbot.io still responds).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dashbot.png
layout: provider
mcp_servers:
- description: Dimension Labs serves a Model Context Protocol endpoint from its own documentation host, https://docs.dimensionlabs.io/mcp. It is the MCP server that ships with their ReadMe documentation hub (the res
  name: Dashbot MCP Server
  slug: dashbot-mcp-server
modified: '2026-08-14'
name: Dashbot
nav: Providers
network: true
overview: 'Dashbot publishes 1 API on the [APIs.io](https://apis.io/) network: Export API. Tagged areas include Company, Ai Ml, Conversational Analytics, Chatbots, and Voice Assistants.


  Dashbot''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, pricing, signup flow, and 23 more developer resources.'
plans:
- name: Dashbot Plans Pricing
  plan_count: 5
  slug: dashbot-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Dashbot Rate Limits
  slug: dashbot-rate-limits
score:
  band: developing
  composite: 51.5
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 30.3
    contract_quality: 41.3
    developer_ergonomics: 55.4
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 2.6
  previous_composite: 51.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dashbot/refs/heads/main/screenshots/dashbot-2026-07-25T211226.png
security:
- kind: authentication
  name: Dashbot Authentication
  slug: dashbot-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Dashbot Domain Security
  slug: dashbot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dashbot
tags:
- Company
- Ai Ml
- Conversational Analytics
- Chatbots
- Voice Assistants
- Customer Experience
- Data Enrichment
- Analytics
- Contact Center
website: https://www.dimensionlabs.io/
---
