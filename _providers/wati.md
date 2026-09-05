---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.7
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Wati Agentic Access
  operation_count: 4
  slug: wati-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- description: 'Tenant-scoped REST API for sending WhatsApp template and session messages, managing contacts, assigning operators, and orchestrating chatbot flows. Uses Bearer token authentication with per-workspace '
  name: WATI WhatsApp Business API
  slug: whatsapp-api
- baseURL: https://live-mt-server.wati.io
  baseurl_source: declared
  description: Manage WhatsApp contacts in the WATI workspace.
  name: WATI Contacts API
  slug: wati-contacts-api
- baseURL: https://live-mt-server.wati.io
  baseurl_source: declared
  description: Retrieve and send WhatsApp messages.
  name: WATI Messages API
  slug: wati-messages-api
- baseURL: https://live-mt-server.wati.io
  baseurl_source: declared
  description: Send WhatsApp template messages.
  name: WATI Templates API
  slug: wati-templates-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WATI WhatsApp Business Contacts API
  slug: open-wati-contacts-api
- collection_type: open
  name: WATI WhatsApp Business Contacts Messages API
  slug: open-wati-messages-api
- collection_type: open
  name: WATI WhatsApp Business Contacts Templates API
  slug: open-wati-templates-api
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
overview: 'WATI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Contacts API, Messages API, and Templates API. Tagged areas include WhatsApp, Messaging, Customer Engagement, Chatbots, and Business Communication.


  WATI''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 8 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 54.4
    developer_ergonomics: 22.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 32.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Chatbots
- Business Communication
- CRM
website: https://www.wati.io
---
