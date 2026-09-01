---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The only publicly documented HTTP endpoints Chatsimple (now Expertise AI) publishes. Documented on the Zapier integration page of docs.expertise.ai as four operations under the base URL https://api.ex
  name: Expertise AI Zapier / Leads API
  slug: chatsimple-zapier-leads-api
- description: 'A remote Model Context Protocol server at https://api.expertise.ai/mcp, found by direct probe of the API host root and documented nowhere on the provider''s site. It implements the MCP Streamable HTTP '
  name: Expertise AI MCP Server
  slug: chatsimple-mcp-server
artifact_total: 9
asyncapis:
- description: ''
  name: Chatsimple Webhooks
  slug: chatsimple-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.expertise.ai
- group: start
  title: ''
  type: Portal
  url: https://my.expertise.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.expertise.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.expertise.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.expertise.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://my.expertise.ai?signup=true
- group: start
  title: ''
  type: Login
  url: https://my.expertise.ai/?log_in=true
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.expertise.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.expertise.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.expertise.ai/contact-us
- group: auth
  title: ''
  type: TrustCenter
  url: security/chatsimple-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.expertise.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/chatsimple-plans.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chatsimple-domain-security.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.expertise.ai/live/integrations/zapier
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.expertise.ai/getting-started/connect
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ChatSimple
- group: operate
  title: ''
  type: Roadmap
  url: https://www.expertise.ai/roadmap
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/chatsimple-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/chatsimple-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chatsimple-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/chatsimple-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/chatsimple-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chatsimple-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chatsimple-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/chatsimple-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/chatsimple-packages.yml
- group: design
  title: ''
  type: Components
  url: components/chatsimple-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chatsimple-llms.txt
created: '2026-07-17'
description: Chatsimple (now operating as Expertise AI, expertise.ai) is an AI agent platform for revenue and go-to-market teams. It builds no-code conversational AI sales agents and chatbots that engage website visitors, qualify and capture leads, book meetings, and answer questions from a trained knowledge base, plus a Voice AI assistant and an "Expertise Assistant" library of 100+ pre-built GTM plays that automate prospecting, pipeline management, and outreach. The platform embeds on any website, integrates with CRM and communication tools such as HubSpot, Salesforce, Slack, Zapier, Marketo, and LeanData, and offers API access on its Enterprise tier. It is SOC 2 Type II, SOC 3, GDPR, and CCPA aligned with a public trust center. Originally launched as chatsimple.ai, the company rebranded to Expertise AI; chatsimple.ai now redirects to expertise.ai.
image: https://www.expertise.ai/images/og-home-page.png
layout: provider
mcp_servers:
- description: ''
  name: Chatsimple MCP Server
  slug: chatsimple-mcp-server
modified: '2026-08-13'
name: Chatsimple
nav: Providers
network: true
overview: 'Chatsimple publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Agents, Conversational AI, Chatbots, and Lead Generation.


  The Chatsimple catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Chatsimple''s developer surface includes developer portal, documentation, engineering blog, pricing, signup flow, support, API reference, and 22 more developer resources.'
plans:
- name: Chatsimple Plans
  plan_count: 9
  slug: chatsimple-plans
random_paper: 16
rate_limits:
- limit_count: 0
  name: Chatsimple Rate Limits
  slug: chatsimple-rate-limits
score:
  band: developing
  composite: 52.3
  coverage:
    artifact_dirs: 16
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 57.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 52.3
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chatsimple/refs/heads/main/screenshots/chatsimple-2026-07-25T205118.png
security:
- kind: authentication
  name: Chatsimple Authentication
  slug: chatsimple-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Chatsimple Domain Security
  slug: chatsimple-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Chatsimple Trust Center
  slug: chatsimple-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2, SOC 3, GDPR, CCPA
slug: chatsimple
tags:
- Company
- AI Agents
- Conversational AI
- Chatbots
- Lead Generation
- Sales Automation
- CRM Integration
- Voice AI
- Go-To-Market
- Customer Engagement
website: https://www.expertise.ai
---
