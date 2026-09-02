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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 65
  human_in_the_loop: 10
  name: Remberg Agentic Access
  operation_count: 115
  slug: remberg-agentic-access
  summary_line: 115 operations · 65 acting · 10 human-in-the-loop
api_count: 12
apis:
- description: The ai-chat API from Remberg — 2 operation(s) for ai-chat.
  name: Remberg ai-chat API
  slug: remberg-ai-chat-api
- description: The asset-status-signals API from Remberg — 5 operation(s) for asset-status-signals.
  name: Remberg asset-status-signals API
  slug: remberg-asset-status-signals-api
- description: The asset-types API from Remberg — 3 operation(s) for asset-types.
  name: Remberg asset-types API
  slug: remberg-asset-types-api
- description: The assets API from Remberg — 5 operation(s) for assets.
  name: Remberg assets API
  slug: remberg-assets-api
- description: The contacts API from Remberg — 2 operation(s) for contacts.
  name: Remberg contacts API
  slug: remberg-contacts-api
- description: The failure-types API from Remberg — 2 operation(s) for failure-types.
  name: Remberg failure-types API
  slug: remberg-failure-types-api
- description: The files API from Remberg — 6 operation(s) for files.
  name: Remberg files API
  slug: remberg-files-api
- description: The forms API from Remberg — 2 operation(s) for forms.
  name: Remberg forms API
  slug: remberg-forms-api
- description: The inventories API from Remberg — 4 operation(s) for inventories.
  name: Remberg inventories API
  slug: remberg-inventories-api
- description: The organizations API from Remberg — 4 operation(s) for organizations.
  name: Remberg organizations API
  slug: remberg-organizations-api
- description: The part-stock-changes API from Remberg — 2 operation(s) for part-stock-changes.
  name: Remberg part-stock-changes API
  slug: remberg-part-stock-changes-api
- description: The parts API from Remberg — 3 operation(s) for parts.
  name: Remberg parts API
  slug: remberg-parts-api
- description: The procedure-templates API from Remberg — 1 operation(s) for procedure-templates.
  name: Remberg procedure-templates API
  slug: remberg-procedure-templates-api
- description: The tickets API from Remberg — 4 operation(s) for tickets.
  name: Remberg tickets API
  slug: remberg-tickets-api
- description: The user-groups API from Remberg — 1 operation(s) for user-groups.
  name: Remberg user-groups API
  slug: remberg-user-groups-api
- description: The user-roles API from Remberg — 1 operation(s) for user-roles.
  name: Remberg user-roles API
  slug: remberg-user-roles-api
- description: The users API from Remberg — 3 operation(s) for users.
  name: Remberg users API
  slug: remberg-users-api
- description: The work-orders API from Remberg — 12 operation(s) for work-orders.
  name: Remberg work-orders API
  slug: remberg-work-orders-api
- description: The work-requests API from Remberg — 7 operation(s) for work-requests.
  name: Remberg work-requests API
  slug: remberg-work-requests-api
artifact_total: 46
asyncapis:
- description: ''
  name: Remberg Events Webhooks
  slug: remberg-events-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AI ai-chat API
  slug: open-remberg-ai-chat-api
- collection_type: open
  name: AI ai-chat asset-status-signals API
  slug: open-remberg-asset-status-signals-api
- collection_type: open
  name: AI ai-chat asset-types API
  slug: open-remberg-asset-types-api
- collection_type: open
  name: AI ai-chat assets API
  slug: open-remberg-assets-api
- collection_type: open
  name: AI ai-chat contacts API
  slug: open-remberg-contacts-api
- collection_type: open
  name: AI ai-chat failure-types API
  slug: open-remberg-failure-types-api
- collection_type: open
  name: AI ai-chat files API
  slug: open-remberg-files-api
- collection_type: open
  name: AI ai-chat forms API
  slug: open-remberg-forms-api
- collection_type: open
  name: AI ai-chat inventories API
  slug: open-remberg-inventories-api
- collection_type: open
  name: AI ai-chat organizations API
  slug: open-remberg-organizations-api
- collection_type: open
  name: AI ai-chat part-stock-changes API
  slug: open-remberg-part-stock-changes-api
- collection_type: open
  name: AI ai-chat parts API
  slug: open-remberg-parts-api
- collection_type: open
  name: AI ai-chat procedure-templates API
  slug: open-remberg-procedure-templates-api
- collection_type: open
  name: AI ai-chat tickets API
  slug: open-remberg-tickets-api
- collection_type: open
  name: AI ai-chat user-groups API
  slug: open-remberg-user-groups-api
- collection_type: open
  name: AI ai-chat user-roles API
  slug: open-remberg-user-roles-api
- collection_type: open
  name: AI ai-chat users API
  slug: open-remberg-users-api
- collection_type: open
  name: AI ai-chat work-orders API
  slug: open-remberg-work-orders-api
- collection_type: open
  name: AI ai-chat work-requests API
  slug: open-remberg-work-requests-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/remberg-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/remberg-ai-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.remberg.de/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.remberg.de/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.remberg.de/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.remberg.de/docs/getting-started
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.remberg.de/en/
- group: company
  title: ''
  type: Blog
  url: https://remberg.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://remberg.com/pricing
- group: company
  title: ''
  type: Website
  url: https://remberg.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/remberg-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: https://developers.remberg.de/openapi
- group: design
  title: ''
  type: Conventions
  url: conventions/remberg-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/remberg-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/remberg-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/remberg-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.remberg.de
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/remberg-events-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/remberg-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/remberg-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://remberg.com/trust
- group: auth
  title: ''
  type: TrustCenter
  url: security/remberg-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/remberg-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/remberg-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/remberg-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/remberg-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/remberg-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/remberg-manage-assets.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/remberg-manage-work-orders.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/remberg-sync-organizations-contacts.md
created: '2026-07-17'
description: remberg is a Munich-based B2B SaaS provider of an Intelligent Asset Platform for maintenance, operations, and service — CMMS/EAM/CAFM software used by industrial companies (Vaillant, Remondis, Liqui Moly, SCHUNK, EDEKA, OSRAM) to manage assets, work orders, spare parts, tickets, forms, and preventive maintenance, with an AI Copilot and a lightweight execution layer alongside SAP. remberg exposes a public REST API (api.remberg.de) across Assets, Work Orders, Work Requests, Tickets, Parts, Organizations, Contacts, Users, Files, Forms, Procedures, and AI, with API-key auth, Svix-based webhooks, documented rate limits, and ISO 27001 certification.
image: https://cdn.prod.website-files.com/673f38dcff99b6e3a5b731cb/67b82bff96b78efd5092c4e4_main-hero-16-9-de-2-1024x576.png
layout: provider
mcp_servers:
- description: ''
  name: Remberg MCP Server
  slug: remberg-mcp-server
modified: '2026-07-21'
name: Remberg
nav: Providers
network: true
overview: 'Remberg publishes 19 APIs on the [APIs.io](https://apis.io/) network, including ai-chat API, asset-status-signals API, asset-types API, and 16 more. Tagged areas include Maintenance, Asset Management, CMMS, EAM, and Field Service.


  The Remberg catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Remberg''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, authentication, and 24 more developer resources.'
random_paper: 5
rate_limits:
- limit_count: 2
  name: Remberg Rate Limits
  slug: remberg-rate-limits
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 21
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 4.5
    contract_quality: 64.7
    developer_ergonomics: 39.9
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 28.9
  previous_composite: 42.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/remberg/refs/heads/main/screenshots/remberg-2026-08-17T081515.png
security:
- kind: authentication
  name: Remberg Authentication
  slug: remberg-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Remberg Domain Security
  slug: remberg-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Remberg Trust Center
  slug: remberg-trust-center
  summary_line: ISO/IEC 27001, GDPR
slug: remberg
tags:
- Maintenance
- Asset Management
- CMMS
- EAM
- Field Service
- Work Orders
- Industrial
- Software-as-a-Service
- Germany
website: https://remberg.com
---
