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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: 1Worldsync Agentic Access
  operation_count: 3
  slug: 1worldsync-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 1
apis:
- baseURL: https://content1-api.1worldsync.com
  baseurl_source: declared
  description: The FetchProduct API from 1WorldSync — 3 operation(s) for fetchproduct.
  name: 1WorldSync FetchProduct API
  slug: 1worldsync-fetchproduct-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: 1WorldSync Content1 FetchProduct API
  slug: open-1worldsync-fetchproduct-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/1worldsync-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/1worldsync-content1-overlay.yaml
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
  name: 1WorldSync MCP Server
  slug: 1worldsync-mcp-server
modified: '2026-07-17'
name: 1WorldSync
nav: Providers
network: true
overview: '1WorldSync publishes 1 API on the [APIs.io](https://apis.io/) network: FetchProduct API. Tagged areas include Company, Product Content, GDSN, Data Syndication, and Master Data.


  1WorldSync''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, pricing, authentication, and 24 more developer resources.'
random_paper: 17
score:
  band: developing
  composite: 50.6
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 55.8
    developer_ergonomics: 68.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 50.6
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
