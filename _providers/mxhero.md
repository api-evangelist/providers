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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: AI email knowledge-recovery service. Captured company email is optimized and stored in an isolated per-tenant vector database, then exposed to AI agents through an official MCP server (email_search to
  name: mxHERO Mail2Cloud Advanced (AI Email Knowledge)
  slug: mxhero-mail2cloud-advanced-ai-email-knowledge
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://mxhero.com
- group: other
  title: ''
  type: Products
  url: https://www.mxhero.com/products
- group: docs
  title: ''
  type: Documentation
  url: https://mxhero.helpjuice.com/en_US/mxhero-ai
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.mxhero.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://web-new.mxhero.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www2.mxhero.com/products-pricing.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mxhero.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mxhero.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mxaiorg
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mxhero-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/mxhero-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mxhero-authentication.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mxhero-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mxhero-domain-security.yml
created: '2026-07-17'
description: 'mxHERO Inc. is the pioneer of email-to-cloud content management, based in San Francisco and a long-time Box partner. Its Mail2Cloud platform is a bridge that intelligently captures email and attachments (in-flight or at-rest) over SMTP/S and IMAP/S and routes them, bi-directionally, into cloud content platforms such as Box, Egnyte, Microsoft OneDrive, Google Drive, and Dropbox — without retaining the content itself. Mail2Cloud Advanced adds an AI email-knowledge layer: captured email is deduplicated, metadata-preserved, and stored in an isolated per-tenant vector database that an official Model Context Protocol (MCP) server exposes to AI agents for secure email search and knowledge recovery, with a V3 REST API for dataset and S/MIME management.'
image: https://mxhero.com/wp-content/uploads/2021/03/mxhero-logo.png
layout: provider
mcp_servers:
- description: ''
  name: mxhero-mcp.yml
  slug: mxhero-mcpyml
modified: '2026-07-20'
name: mxHero
nav: Providers
network: true
overview: 'mxHero publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email, Cloud Storage, Content Management, and Email to Cloud.


  mxHero''s developer surface includes documentation, engineering blog, pricing, authentication, and 11 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 21.9
  delta: -2.6
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 36.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 24.5
  provenance:
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Mxhero Authentication
  slug: mxhero-authentication
  summary_line: token/apiKey · 2 schemes
- kind: domain-security
  name: Mxhero Domain Security
  slug: mxhero-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mxhero
tags:
- Company
- Email
- Cloud Storage
- Content Management
- Email to Cloud
- Artificial Intelligence
- MCP
- Email Search
- Compliance
- Collaboration
website: https://mxhero.com
---
