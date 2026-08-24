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
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Propelplm Agentic Access
  operation_count: 33
  slug: propelplm-agentic-access
  summary_line: 33 operations · 9 acting
api_count: 15
apis:
- description: The Assembly API from Propel Software (Propel PLM) — 1 operation(s) for assembly.
  name: Propel Software (Propel PLM) Assembly API
  slug: propelplm-assembly-api
- description: The assets API from Propel Software (Propel PLM) — 1 operation(s) for assets.
  name: Propel Software (Propel PLM) assets API
  slug: propelplm-assets-api
- description: The Attachment API from Propel Software (Propel PLM) — 2 operation(s) for attachment.
  name: Propel Software (Propel PLM) Attachment API
  slug: propelplm-attachment-api
- description: The Bill of Material API from Propel Software (Propel PLM) — 1 operation(s) for bill of material.
  name: Propel Software (Propel PLM) Bill of Material API
  slug: propelplm-bill-of-material-api
- description: The BOM API from Propel Software (Propel PLM) — 2 operation(s) for bom.
  name: Propel Software (Propel PLM) BOM API
  slug: propelplm-bom-api
- description: The categories API from Propel Software (Propel PLM) — 3 operation(s) for categories.
  name: Propel Software (Propel PLM) categories API
  slug: propelplm-categories-api
- description: The change API from Propel Software (Propel PLM) — 3 operation(s) for change.
  name: Propel Software (Propel PLM) change API
  slug: propelplm-change-api
- description: The channels API from Propel Software (Propel PLM) — 3 operation(s) for channels.
  name: Propel Software (Propel PLM) channels API
  slug: propelplm-channels-api
- description: The Configuration API from Propel Software (Propel PLM) — 1 operation(s) for configuration.
  name: Propel Software (Propel PLM) Configuration API
  slug: propelplm-configuration-api
- description: The Item API from Propel Software (Propel PLM) — 2 operation(s) for item.
  name: Propel Software (Propel PLM) Item API
  slug: propelplm-item-api
- description: The ManufacturerItem API from Propel Software (Propel PLM) — 1 operation(s) for manufactureritem.
  name: Propel Software (Propel PLM) ManufacturerItem API
  slug: propelplm-manufactureritem-api
- description: The ManufacturerPart API from Propel Software (Propel PLM) — 2 operation(s) for manufacturerpart.
  name: Propel Software (Propel PLM) ManufacturerPart API
  slug: propelplm-manufacturerpart-api
- description: The markup API from Propel Software (Propel PLM) — 1 operation(s) for markup.
  name: Propel Software (Propel PLM) markup API
  slug: propelplm-markup-api
- description: The products API from Propel Software (Propel PLM) — 5 operation(s) for products.
  name: Propel Software (Propel PLM) products API
  slug: propelplm-products-api
- description: The variants API from Propel Software (Propel PLM) — 4 operation(s) for variants.
  name: Propel Software (Propel PLM) variants API
  slug: propelplm-variants-api
artifact_total: 38
asyncapis:
- description: ''
  name: Propelplm Events
  slug: propelplm-events
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Get Bom Assembly API
  slug: open-propelplm-assembly-api
- collection_type: open
  name: Get Bom Assembly assets API
  slug: open-propelplm-assets-api
- collection_type: open
  name: Get Bom Assembly Attachment API
  slug: open-propelplm-attachment-api
- collection_type: open
  name: Get Bom Assembly Bill of Material API
  slug: open-propelplm-bill-of-material-api
- collection_type: open
  name: Get Assembly BOM API
  slug: open-propelplm-bom-api
- collection_type: open
  name: Get Bom Assembly categories API
  slug: open-propelplm-categories-api
- collection_type: open
  name: Get Bom Assembly change API
  slug: open-propelplm-change-api
- collection_type: open
  name: Get Bom Assembly channels API
  slug: open-propelplm-channels-api
- collection_type: open
  name: Get Bom Assembly Configuration API
  slug: open-propelplm-configuration-api
- collection_type: open
  name: Get Bom Assembly Item API
  slug: open-propelplm-item-api
- collection_type: open
  name: Get Bom Assembly ManufacturerItem API
  slug: open-propelplm-manufactureritem-api
- collection_type: open
  name: Get Bom Assembly ManufacturerPart API
  slug: open-propelplm-manufacturerpart-api
- collection_type: open
  name: Get Bom Assembly markup API
  slug: open-propelplm-markup-api
- collection_type: open
  name: Get Bom Assembly products API
  slug: open-propelplm-products-api
- collection_type: open
  name: Get Bom Assembly variants API
  slug: open-propelplm-variants-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/propelplm-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/propelplm-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.propelsoftware.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.propelplm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.propelplm.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.propelplm.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.propelplm.com/docs/available-apis/
- group: auth
  title: ''
  type: Authentication
  url: authentication/propelplm-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/propelplm-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://converged.propelsoftware.com/
- group: operate
  title: ''
  type: Support
  url: https://propelplm.my.site.com/helpcenter/s/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.propelsoftware.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.propelsoftware.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.propelsoftware.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/propelplm
- group: operate
  title: ''
  type: StatusPage
  url: https://status.propelsoftware.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.propelsoftware.com/trust
- group: build
  title: ''
  type: Postman
  url: https://api-docs.propelplm.com/
- group: build
  title: ''
  type: Packages
  url: packages/propelplm-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/propelplm-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/propelplm-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/propelplm-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/propelplm-core-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/propelplm-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/propelplm-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/propelplm-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/propelplm-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/propelplm-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/propelplm-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/propelplm-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/propelplm-events.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/propelplm-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Propel Software is an AI-powered product data platform for manufacturers and product companies, unifying Product Lifecycle Management (PLM), Quality Management (QMS), and Product Information Management (PIM) on a single system of record built natively on the Salesforce Platform. Propel exposes a resource-based REST API (Salesforce Apex REST) for the core PLM objects — Items, Bills of Material, Changes/ECOs, and Attachments — plus a bulk Import API and a read-oriented PIM API for syndicating product, variant, category, channel, and digital-asset data to commerce and marketing channels. All API access is authenticated with Salesforce OAuth 2.0 bearer tokens and executes within the requesting user's permission scope. Propel is backed by Norwest Venture Partners.
image: https://www.propelsoftware.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Propel Software (Propel PLM) MCP Server
  slug: propel-software-propel-plm-mcp-server
modified: '2026-07-20'
name: Propel Software (Propel PLM)
nav: Providers
network: true
overview: 'Propel Software (Propel PLM) publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Assembly API, assets API, Attachment API, and 12 more. Tagged areas include Company, Product Lifecycle Management, PLM, Quality Management, and QMS.


  The Propel Software (Propel PLM) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Propel Software (Propel PLM)''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, pricing, and 26 more developer resources.'
random_paper: 0
scopes:
- name: Propelplm Scopes
  scope_count: 4
  slug: propelplm-scopes
  summary_line: 4 scopes · implicit/authorizationCode
score:
  band: strong
  composite: 54.4
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 30.3
    contract_quality: 53.9
    developer_ergonomics: 70.8
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 42.1
  previous_composite: 54.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/propelplm/refs/heads/main/screenshots/propelplm-2026-08-17T081348.png
security:
- kind: authentication
  name: Propelplm Authentication
  slug: propelplm-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Propelplm Domain Security
  slug: propelplm-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Propelplm Trust Center
  slug: propelplm-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR
slug: propelplm
tags:
- Company
- Product Lifecycle Management
- PLM
- Quality Management
- QMS
- Product Information Management
- PIM
- Manufacturing
- Salesforce
- Bill of Materials
- Change Management
website: https://www.propelsoftware.com
---
