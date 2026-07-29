---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: 1Worldsync Agentic Access
  operation_count: 3
  slug: 1worldsync-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 1
apis:
- description: The FetchProduct API from 1WorldSync — 3 operation(s) for fetchproduct.
  name: 1WorldSync FetchProduct API
  slug: 1worldsync-fetchproduct-api
artifact_total: 6
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/1worldsync-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/1worldsync-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://1worldsync.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.1worldsync.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.1worldsync.com/read-api-2-0-documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://content1-api.1worldsync.com/swagger/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.1worldsync.com/register
- group: start
  title: ''
  type: SignUp
  url: https://developer.1worldsync.com/register
- group: operate
  title: ''
  type: Support
  url: https://1worldsync.com/resource-center/support/contact-support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.1worldsync.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://1worldsync.com/subscription-plans/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://1worldsync.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://1worldsync.com/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/9015441/2sB3BDKBGR
- group: auth
  title: ''
  type: Compliance
  url: https://1worldsync.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: https://1worldsync.com/security/
- group: auth
  title: ''
  type: Authentication
  url: authentication/1worldsync-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/1worldsync-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/1worldsync-conventions.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/1worldsync-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/1worldsync-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/1worldsync-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/1worldsync-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/1worldsync-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/1worldsync-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/1worldsync-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/1worldsync-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/1worldsync-data-model.yml
created: '2026-07-17'
description: 1WorldSync is the leading product content network and a GS1-certified GDSN data pool, helping consumer goods brands, manufacturers, and retailers create, manage, syndicate, and verify trusted product content across the digital shelf and the physical supply chain. Its Content1 platform exposes REST APIs for product master data — the Content1 Read API (product search, fetch, count, and hierarchy retrieval), the Item Management Inbound API (add, update, delete, and link items and hierarchies), a Digital Asset Management (DAM) API for images and rich media, and a User Management API (UMA) — all authenticated with HMAC-signed requests using an app_id and a secret key. 1WorldSync serves CPG, grocery, healthcare, foodservice, and DIY sectors and is SOC 2 Type 2 and ISO/IEC 27001:2022 certified.
image: https://1worldsync.com/wp-content/uploads/2024/10/Untitled-design-49.png
layout: provider
mcp_servers:
- description: ''
  name: 1worldsync-mcp.yml
  slug: 1worldsync-mcpyml
modified: '2026-07-17'
name: 1WorldSync
nav: Providers
network: true
overview: '1WorldSync publishes 1 API on the [APIs.io](https://apis.io/) network: FetchProduct API. Tagged areas include Company, Product Content, GDSN, Data Syndication, and Master Data.


  1WorldSync''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, pricing, authentication, and 22 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 51.7
  delta: 0.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 57.6
    developer_ergonomics: 64.7
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 7.9
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/1worldsync/refs/heads/main/screenshots/1worldsync-2026-07-25T181115.png
security:
- kind: authentication
  name: 1Worldsync Authentication
  slug: 1worldsync-authentication
  summary_line: hmac · 1 scheme
- kind: domain-security
  name: 1Worldsync Domain Security
  slug: 1worldsync-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: 1Worldsync Trust Center
  slug: 1worldsync-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2022
slug: 1worldsync
tags:
- Company
- Product Content
- GDSN
- Data Syndication
- Master Data
- Digital Shelf
- Product Information Management
- PIM
- CPG
- Retail
- GS1
website: https://1worldsync.com/
---
