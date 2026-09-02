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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Maison Safqa Holdings Limited Agentic Access
  operation_count: 6
  slug: maison-safqa-holdings-limited-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 1
apis:
- description: Update inventory quantities for product variants. Changes are stored locally and periodically synced to Shopify.
  name: Maison Safqa Holdings Limited Inventory API
  slug: maison-safqa-holdings-limited-inventory-api
- description: Create, retrieve, and update products. Products are created in draft status and synced to Shopify when activated.
  name: Maison Safqa Holdings Limited Products API
  slug: maison-safqa-holdings-limited-products-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Maison Safqa Brand Developer Inventory API
  slug: open-maison-safqa-holdings-limited-inventory-api
- collection_type: open
  name: Maison Safqa Brand Developer Inventory Products API
  slug: open-maison-safqa-holdings-limited-products-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/maison-safqa-holdings-limited-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/maison-safqa-holdings-limited-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.maisonsafqa.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.maisonsafqa.com
- group: operate
  title: ''
  type: Support
  url: mailto:itsupport@maisonsafqa.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.maisonsafqa.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://maisonsafqa.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/maison-safqa-holdings-limited-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/maison-safqa-holdings-limited-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/maison-safqa-holdings-limited-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/maison-safqa-holdings-limited-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/maison-safqa-holdings-limited-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/maison-safqa-holdings-limited-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/maison-safqa-holdings-limited-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/maison-safqa-holdings-limited-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/maison-safqa-holdings-limited-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/maison-safqa-holdings-limited-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/maison-safqa-holdings-limited-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/maison-safqa-holdings-limited-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maison-safqa-holdings-limited-domain-security.yml
created: '2026-07-17'
description: Maison Safqa Holdings Limited operates Maison Safqa, a members-only luxury flash-sale marketplace (built on Shopify) offering exclusive time-limited sales on high-end brands. For its partner brands it publishes the Maison Safqa Brand Developer API — an API-key-authenticated REST interface for creating products (single and bulk) and updating inventory levels, which the platform then syncs into Shopify with brand data taking precedence on conflict and prices converted to SAR on ingestion. Surfaced originally as a 500 Global portfolio lead and enriched from the provider's public developer portal.
image: https://cdn.shopify.com/s/files/1/0865/0224/4663/files/logo-ms.svg?v=1763809309
layout: provider
mcp_servers:
- description: Candidate MCP tool surface derived one-to-one from the Maison Safqa Brand Developer API operations. No official hosted/remote MCP server was found for this provider; this is a governance starting poin
  name: Maison Safqa Holdings Limited MCP Server
  slug: maison-safqa-holdings-limited-mcp-server
modified: '2026-07-20'
name: Maison Safqa Holdings Limited
nav: Providers
network: true
overview: 'Maison Safqa Holdings Limited publishes 2 APIs on the [APIs.io](https://apis.io/) network: Inventory API and Products API. Tagged areas include Company, Retail, E-Commerce, Luxury, and Marketplace.


  Maison Safqa Holdings Limited''s developer surface includes documentation, support, authentication, sandbox, and 17 more developer resources.'
random_paper: 8
rate_limits:
- limit_count: 2
  name: Maison Safqa Holdings Limited Rate Limits
  slug: maison-safqa-holdings-limited-rate-limits
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 19
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 53.7
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 21.1
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maison-safqa-holdings-limited/refs/heads/main/screenshots/maison-safqa-holdings-limited-2026-07-25T225926.png
security:
- kind: authentication
  name: Maison Safqa Holdings Limited Authentication
  slug: maison-safqa-holdings-limited-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Maison Safqa Holdings Limited Domain Security
  slug: maison-safqa-holdings-limited-domain-security
  summary_line: TLSv1.3 · DMARC
slug: maison-safqa-holdings-limited
tags:
- Company
- Retail
- E-Commerce
- Luxury
- Marketplace
- Product Catalog
- Inventory Management
- Shopify
website: https://maisonsafqa.com
---
