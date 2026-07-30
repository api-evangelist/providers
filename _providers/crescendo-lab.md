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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: documented
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 60.6
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: Bulk (1-to-many) SMS. Small batches dispatch inline; >30 recipients queue asynchronously.
  name: Crescendo Lab Broadcast API
  slug: crescendo-lab-broadcast-api
- description: Address book with NCC-consent tracking.
  name: Crescendo Lab Contacts API
  slug: crescendo-lab-contacts-api
- description: Transactional (1-to-1) SMS send + status.
  name: Crescendo Lab SMS API
  slug: crescendo-lab-sms-api
- description: Cost-attribution teams. Tag sends with a team to see which team sent/spent how much (shared wallet — reporting only, not a wallet split).
  name: Crescendo Lab Teams API
  slug: crescendo-lab-teams-api
artifact_total: 8
asyncapis:
- description: ''
  name: Crescendo Lab Maacgo Webhooks
  slug: crescendo-lab-maacgo-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://cresclab.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sms.cresclab.com/developers.html
- group: docs
  title: ''
  type: Documentation
  url: https://sms.cresclab.com/developers.html#api
- group: company
  title: ''
  type: Blog
  url: https://blog.cresclab.com/zh-tw
- group: operate
  title: ''
  type: HelpCenter
  url: https://crescendolab.zendesk.com/hc/zh-tw
- group: commercial
  title: ''
  type: Pricing
  url: https://cresclab.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://sms.cresclab.com/app.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sms.cresclab.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sms.cresclab.com/privacy.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Crescendo-Lab
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crescendo-lab-llms.txt
- group: build
  title: ''
  type: SDKs
  url: packages/crescendo-lab-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/crescendo-lab-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/crescendo-lab-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/crescendo-lab-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/crescendo-lab-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/crescendo-lab-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/crescendo-lab-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crescendo-lab-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/crescendo-lab-well-known.yml
created: '2026-07-17'
description: Crescendo Lab is a Taiwan-based, Asia-leading AI omnichannel customer communication software company (cresclab.com) serving 800+ global brands, and a LINE Biz-Solutions Gold Partner. Its platform spans MAAC (AI marketing automation), CAAC (conversational applications), and DAAC (data intelligence) across LINE, WhatsApp, SMS, email, and social channels. Its developer-facing surface is MAAC Go (sms.cresclab.com) — a self-serve, NCC-compliant Taiwan SMS API with a published OpenAPI spec, first-party Node/Python SDKs, a CLI, an official MCP server, and delivery webhooks. Surfaced as a 500 Global portfolio company and enriched into the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crescendo-lab.png
layout: provider
mcp_servers:
- description: ''
  name: crescendo-lab-mcp.yml
  slug: crescendo-lab-mcpyml
modified: '2026-07-18'
name: Crescendo Lab
nav: Providers
network: true
overview: 'Crescendo Lab publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Broadcast API, Contacts API, SMS API, and 1 more. Tagged areas include Company, SMS, Messaging, Marketing Automation, and Customer Engagement.


  The Crescendo Lab catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Crescendo Lab''s developer surface includes documentation, engineering blog, pricing, signup flow, CLI, authentication, and 15 more developer resources.'
random_paper: 68
score:
  band: developing
  composite: 44.8
  delta: -3.6
  facets:
    commercial_clarity: 44.7
    contract_quality: 63.7
    developer_ergonomics: 58.2
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 48.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 27.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crescendo-lab/refs/heads/main/screenshots/crescendo-lab-2026-07-25T210727.png
security:
- kind: authentication
  name: Crescendo Lab Authentication
  slug: crescendo-lab-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Crescendo Lab Domain Security
  slug: crescendo-lab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crescendo-lab
tags:
- Company
- SMS
- Messaging
- Marketing Automation
- Customer Engagement
- Taiwan
- Omnichannel
- MCP
website: https://cresclab.com
---
