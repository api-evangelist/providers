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
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Wati Agentic Access
  operation_count: 4
  slug: wati-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 4
apis:
- description: 'Tenant-scoped REST API for sending WhatsApp template and session messages, managing contacts, assigning operators, and orchestrating chatbot flows. Uses Bearer token authentication with per-workspace '
  name: WATI WhatsApp Business API
  slug: whatsapp-api
- description: Manage WhatsApp contacts in the WATI workspace.
  name: WATI Contacts API
  slug: wati-contacts-api
- description: Retrieve and send WhatsApp messages.
  name: WATI Messages API
  slug: wati-messages-api
- description: Send WhatsApp template messages.
  name: WATI Templates API
  slug: wati-templates-api
artifact_total: 10
collections:
- collection_type: open
  name: WATI WhatsApp Business API
  slug: open-wati
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wati-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/wati-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wati-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wati-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/watiglobal
- group: company
  title: ''
  type: Website
  url: https://www.wati.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wati.io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wati.io/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.wati.io/register
- group: operate
  title: ''
  type: Support
  url: https://support.wati.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wati-io
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/wati-io/wati-mcp-server
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.wati.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.wati.io/feed/
created: '2026-05-11'
description: WATI is an official WhatsApp Business Platform that provides a shared team inbox, no-code chatbot builder, broadcast campaigns, and CRM integrations for businesses communicating with customers over WhatsApp. The platform offers a tenant-scoped REST API for sending template and session messages, managing contacts, and integrating with external systems. WATI APIs use Bearer token authentication tied to each customer's WATI workspace.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wati.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: WATI
nav: Providers
network: true
overview: 'WATI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Contacts API, Messages API, and Templates API. Tagged areas include WhatsApp, Messaging, Customer Engagement, Chatbot, and Business Communication.


  WATI''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 8 more developer resources.'
random_paper: 32
score:
  band: thin
  composite: 31.9
  delta: -3.6
  facets:
    commercial_clarity: 18.4
    contract_quality: 58.5
    developer_ergonomics: 34.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 35.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wati/refs/heads/main/screenshots/wati-2026-06-20T201254.png
security:
- kind: authentication
  name: Wati Authentication
  slug: wati-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Wati Domain Security
  slug: wati-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Wati Trust Center
  slug: wati-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: wati
tags:
- WhatsApp
- Messaging
- Customer Engagement
- Chatbot
- Business Communication
- CRM
website: https://www.wati.io
---
