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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.6
  scored_at: '2026-08-19'
api_count: 6
apis:
- description: The Catalog API from ZenAdmin — 3 operation(s) for catalog.
  name: ZenAdmin Catalog API
  slug: zenadmin-catalog-api
- description: The Context API from ZenAdmin — 1 operation(s) for context.
  name: ZenAdmin Context API
  slug: zenadmin-context-api
- description: The Devices API from ZenAdmin — 2 operation(s) for devices.
  name: ZenAdmin Devices API
  slug: zenadmin-devices-api
- description: The Employees API from ZenAdmin — 2 operation(s) for employees.
  name: ZenAdmin Employees API
  slug: zenadmin-employees-api
- description: The Orders API from ZenAdmin — 3 operation(s) for orders.
  name: ZenAdmin Orders API
  slug: zenadmin-orders-api
- description: The Webhooks API from ZenAdmin — 4 operation(s) for webhooks.
  name: ZenAdmin Webhooks API
  slug: zenadmin-webhooks-api
artifact_total: 17
asyncapis:
- description: ''
  name: Zenadmin Webhooks
  slug: zenadmin-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ZenAdmin External Catalog API
  slug: open-zenadmin-catalog-api
- collection_type: open
  name: ZenAdmin External Catalog Context API
  slug: open-zenadmin-context-api
- collection_type: open
  name: ZenAdmin External Catalog Devices API
  slug: open-zenadmin-devices-api
- collection_type: open
  name: ZenAdmin External Catalog Employees API
  slug: open-zenadmin-employees-api
- collection_type: open
  name: ZenAdmin External Catalog Orders API
  slug: open-zenadmin-orders-api
- collection_type: open
  name: ZenAdmin External Catalog Webhooks API
  slug: open-zenadmin-webhooks-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/zenadmin-inventory-devices-employees.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zenadmin-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/zenadmin-external-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://zenadmin.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.zenadmin.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zenadmin.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zenadmin.ai
- group: start
  title: ''
  type: Login
  url: https://console.zenadmin.ai
- group: company
  title: ''
  type: Blog
  url: https://www.zenadmin.ai/blogs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zenadmin.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zenadmin.ai/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zenadmin-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zenadmin-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zenadmin-well-known.yml
created: '2026-07-17'
description: 'ZenAdmin is an all-in-one IT management platform for global teams, covering the full device and employee lifecycle: IT procurement, device lifecycle management, asset and inventory tracking, mobile device management (MDM), identity and access management, SaaS/app management, IT helpdesk, and 24/7 IT support across 150+ countries. ZenAdmin publishes an External API v1 (documented at docs.zenadmin.ai) for programmatic access to devices, hardware orders, a hardware catalog, employees, and outbound webhooks. Authentication is a per-key API key sent via the x-api-key header. This profile was originally surfaced as a 500 Global portfolio company and has been enriched from the live developer documentation.'
image: https://www.zenadmin.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: zenadmin-mcp.yml
  slug: zenadmin-mcpyml
modified: '2026-07-21'
name: ZenAdmin
nav: Providers
network: true
overview: 'ZenAdmin publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Context API, Devices API, and 3 more. Tagged areas include Company, IT Management, Device Management, Mobile Device Management, and IT Asset Management.


  The ZenAdmin catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ZenAdmin''s developer surface includes documentation, API reference, engineering blog, and 11 more developer resources.'
random_paper: 109
score:
  band: thin
  composite: 28.2
  delta: -0.1
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 16.7
    contract_quality: 25.9
    developer_ergonomics: 30.4
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 28.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Zenadmin Authentication
  slug: zenadmin-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Zenadmin Domain Security
  slug: zenadmin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zenadmin
tags:
- Company
- IT Management
- Device Management
- Mobile Device Management
- IT Asset Management
- SaaS Management
- Identity and Access Management
- IT Procurement
- Employee Lifecycle
- Webhooks
website: https://zenadmin.ai
---
