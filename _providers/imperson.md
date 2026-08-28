---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 8.8
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.imperson.com/
- group: company
  title: ''
  type: Blog
  url: https://www.imperson.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.imperson.com/blog-feed.xml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.imperson.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.imperson.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://toolbox.imperson.com
- group: design
  title: ''
  type: Components
  url: components/imperson-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/imperson-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/imperson-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/imperson-domain-security.yml
coverage:
  checked: '2026-08-14'
  detail: Imperson runs a real product API at api.imperson.com — it backs the company's own Toolbox app — but every path on it answers HTTP 401 behind an HTTP Basic challenge (realm "messaging.api"), there is no developer portal (/developers 404), docs.imperson.com 302s into a Google Workspace Drive, and the only route to the API on the whole nine-page marketing site is a "CONTACT SALES" form.
  evidence:
  - status: 401
    url: https://api.imperson.com/
  - status: 404
    url: https://www.imperson.com/developers
  - status: 302
    url: https://docs.imperson.com/
  - status: 400
    url: https://www.imperson.com/.well-known/agent-card.json
  reason: sales-gate
  state: gated
created: '2026-07-17'
description: Imperson is an enterprise conversational-AI company and creative studio that builds turnkey, premium chatbots to automate the customer journey through natural, two-way dialogue. Its platform spans lead generation, customer support, sales and e-commerce, and engagement/entertainment, with a conversation engine, dashboard analytics, and a knowledgebase, activating across channels including Facebook Messenger, Amazon Alexa, websites, SMS, Google Assistant, native apps, and phone. Imperson operates an enterprise-sales model (no public self-serve developer API is published) and has produced chatbot experiences for brands such as Disney, Microsoft, Amazon, National Geographic, and Universal. The company was surfaced as a Techstars portfolio company and profiled into the API Evangelist network.
image: https://static.wixstatic.com/media/dfeb02_6b88203b659746a59986fab720eb18e7~mv2.png/v1/fill/w_1000,h_1000,al_c/dfeb02_6b88203b659746a59986fab720eb18e7~mv2.png
layout: provider
mcp_servers:
- description: ''
  name: Imperson Wix Site MCP
  slug: imperson-wix-site-mcp
modified: '2026-08-14'
name: Imperson
nav: Providers
network: true
overview: 'Imperson is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Conversational AI, Chatbots, Customer-Support, and Lead Generation.


  Imperson''s developer surface includes engineering blog, signup flow, and 8 more developer resources.'
plans:
- name: Imperson Plans Pricing
  plan_count: 0
  slug: imperson-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Imperson Rate Limits
  slug: imperson-rate-limits
score:
  band: emerging
  composite: 14.2
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.2
  provenance:
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/imperson/refs/heads/main/screenshots/imperson-2026-07-25T222152.png
security:
- kind: authentication
  name: Imperson Authentication
  slug: imperson-authentication
  summary_line: http-basic/oauth2 · 2 schemes
- kind: domain-security
  name: Imperson Domain Security
  slug: imperson-domain-security
  summary_line: TLSv1.3 · HSTS
slug: imperson
tags:
- Company
- Conversational AI
- Chatbots
- Customer-Support
- Lead Generation
- Sales Automation
- Enterprise
- MCP
website: https://www.imperson.com/
---
