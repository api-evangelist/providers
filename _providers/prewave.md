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
    dry_run_mode: true
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
  score: 31.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 46
  human_in_the_loop: 2
  name: Prewave Agentic Access
  operation_count: 117
  slug: prewave-agentic-access
  summary_line: 117 operations · 46 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: 🆕 NEW - Retrieve actions (tasks/work items), action types, and action statuses for supplier relationships, compliance reviews, and operational activities. Available from February 2026.
  name: Prewave Actions API
  slug: prewave-actions-api
- description: Endpoints for retrieving alert information from user feeds, disruption maps, and specific targets. Supports filtering by collections, dates, priorities, geographic regions, target identifiers, and oth
  name: Prewave Alerts API
  slug: prewave-alerts-api
- description: Public API for managing collections in Prewave's supply chain network. Collections are used to organize and group suppliers (targets) in your supply chain.
  name: Prewave Collections - Management API
  slug: prewave-collections-management-api
- description: Allows you to retrieve network information. Like tree-graph and commodity-graph.
  name: Prewave Collections - Network API
  slug: prewave-collections-network-api
- description: Public API for managing targets within collections in Prewave's supply chain network.
  name: Prewave Collections - Targets API
  slug: prewave-collections-targets-api
- description: Public API for retrieving supplier relationship graphs from tier-n enabled collections.
  name: Prewave Collections - Tier-N API
  slug: prewave-collections-tier-n-api
- description: Endpoints for retrieving alerts from the disruption map. Supports filtering by geographic region, collections, countries, and other criteria.
  name: Prewave Disruptions API
  slug: prewave-disruptions-api
- description: 🆕 NEW - Allows you to manage customer Due Diligence Statements (DDS), including creating, updating, submitting, withdrawing customer DDS, and viewing supplier DDS associated with products.
  name: Prewave EUDR - Customers - DDS API
  slug: prewave-eudr-customers-dds-api
- description: Allows you to manage customer origin requests for products, including creating, updating, closing requests, and viewing requests per product.
  name: Prewave EUDR - Customers - Origin Requests API
  slug: prewave-eudr-customers-origin-requests-api
- description: Allows you to manage customer products, including creating, updating, linking/unlinking products, and deactivating products.
  name: Prewave EUDR - Customers - Products API
  slug: prewave-eudr-customers-products-api
- description: Allows you to search for suppliers, find suppliers by IDs or references, and manage supplier connection contacts.
  name: Prewave EUDR - Customers - Suppliers API
  slug: prewave-eudr-customers-suppliers-api
- description: Shared reference data for EUDR, including countries, HS codes, and commodities. Available to both customers and suppliers.
  name: Prewave EUDR - Shared API
  slug: prewave-eudr-shared-api
- description: Allows suppliers to manage their origin requests, view their customers, and answer origin requests with supplier DDS.
  name: Prewave EUDR - Suppliers API
  slug: prewave-eudr-suppliers-api
- description: Get exposure analysis graph and targets
  name: Prewave Exposure API
  slug: prewave-exposure-api
- description: Allows you to retrieve information about infotags and groups.
  name: Prewave Infotags API
  slug: prewave-infotags-api
- description: Public API for managing enterprise export configurations and retrieving score data in Prewave's supply chain network.
  name: Prewave Scores - Enterprise Export API
  slug: prewave-scores-enterprise-export-api
- description: Upload and read custom supplier scores from your systems (e.g. SAP). Bulk upload, list event types, and view history per supplier. Available from June 2026.
  name: Prewave Scores - Externals API
  slug: prewave-scores-externals-api
- description: '⚠️ **DEPRECATED** - Target score endpoints. These endpoints are deprecated and will be removed at the end of December 2026. Use `/public/v1/enterprise-export/scores` instead. **Note**: Responses from '
  name: Prewave Scores - Target API
  slug: prewave-scores-target-api
- description: 🆕 NEW - Supplier connection contact management endpoints. Available from February 2026.
  name: Prewave Suppliers - Connection Contacts API
  slug: prewave-suppliers-connection-contacts-api
- description: Supplier management endpoints for listing, retrieving, updating supplier data, and bulk operations.
  name: Prewave Suppliers - Management API
  slug: prewave-suppliers-management-api
- description: 🆕 NEW - Supplier and site management endpoints. Available from January 2026.
  name: Prewave Suppliers - Sites API
  slug: prewave-suppliers-sites-api
- description: Allows you to create or update sites.
  name: Prewave Suppliers - Sites Upsert API
  slug: prewave-suppliers-sites-upsert-api
- description: ⚠️ **DEPRECATED** - This API is deprecated and will be removed at the end of December 2026.
  name: Prewave Suppliers - Supplier Graph API
  slug: prewave-suppliers-supplier-graph-api
- description: 🆕 NEW - API to manage users in the public network. Available from February 2026.
  name: Prewave Users API
  slug: prewave-users-api
- description: 🆕 NEW - API to manage user roles in the public network. Available from February 2026.
  name: Prewave Users - Roles API
  slug: prewave-users-roles-api
arazzos:
- description: Register an outbound product, request commodity origins, attach a DDS, and submit it.
  name: Submit an EUDR Due Diligence Statement
  slug: prewave-eudr-dds-submission
- description: Create a supplier site, run validation and screening, then read its risk alerts.
  name: Onboard and monitor a supplier
  slug: prewave-onboard-and-monitor-supplier
artifact_total: 58
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Public Prewave Actions API
  slug: open-prewave-actions-api
- collection_type: open
  name: Public Prewave Actions Alerts API
  slug: open-prewave-alerts-api
- collection_type: open
  name: Public Prewave Actions Collections - Management API
  slug: open-prewave-collections-management-api
- collection_type: open
  name: Public Prewave Actions Collections - Network API
  slug: open-prewave-collections-network-api
- collection_type: open
  name: Public Prewave Actions Collections - Targets API
  slug: open-prewave-collections-targets-api
- collection_type: open
  name: Public Prewave Actions Collections - Tier-N API
  slug: open-prewave-collections-tier-n-api
- collection_type: open
  name: Public Prewave Actions Disruptions API
  slug: open-prewave-disruptions-api
- collection_type: open
  name: Public Prewave Actions EUDR - Customers - DDS API
  slug: open-prewave-eudr-customers-dds-api
- collection_type: open
  name: Public Prewave Actions EUDR - Customers - Origin Requests API
  slug: open-prewave-eudr-customers-origin-requests-api
- collection_type: open
  name: Public Prewave Actions EUDR - Customers - Products API
  slug: open-prewave-eudr-customers-products-api
- collection_type: open
  name: Public Prewave Actions EUDR - Customers - Suppliers API
  slug: open-prewave-eudr-customers-suppliers-api
- collection_type: open
  name: Public Prewave Actions EUDR - Shared API
  slug: open-prewave-eudr-shared-api
- collection_type: open
  name: Public Prewave Actions EUDR - Suppliers API
  slug: open-prewave-eudr-suppliers-api
- collection_type: open
  name: Public Prewave Actions Exposure API
  slug: open-prewave-exposure-api
- collection_type: open
  name: Public Prewave Actions Infotags API
  slug: open-prewave-infotags-api
- collection_type: open
  name: Public Prewave Actions Scores - Enterprise Export API
  slug: open-prewave-scores-enterprise-export-api
- collection_type: open
  name: Public Prewave Actions Scores - Externals API
  slug: open-prewave-scores-externals-api
- collection_type: open
  name: Public Prewave Actions Scores - Target API
  slug: open-prewave-scores-target-api
- collection_type: open
  name: Public Prewave Actions Suppliers - Connection Contacts API
  slug: open-prewave-suppliers-connection-contacts-api
- collection_type: open
  name: Public Prewave Actions Suppliers - Management API
  slug: open-prewave-suppliers-management-api
- collection_type: open
  name: Public Prewave Actions Suppliers - Sites API
  slug: open-prewave-suppliers-sites-api
- collection_type: open
  name: Public Prewave Actions Suppliers - Sites Upsert API
  slug: open-prewave-suppliers-sites-upsert-api
- collection_type: open
  name: Public Prewave Actions Suppliers - Supplier Graph API
  slug: open-prewave-suppliers-supplier-graph-api
- collection_type: open
  name: Public Prewave Actions Users API
  slug: open-prewave-users-api
- collection_type: open
  name: Public Prewave Actions Users - Roles API
  slug: open-prewave-users-roles-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/prewave-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/prewave-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.prewave.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.prewave.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.prewave.com/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.prewave.com
- group: company
  title: ''
  type: Blog
  url: https://www.prewave.com/resources/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.prewave.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.prewave.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/prewave
- group: operate
  title: ''
  type: StatusPage
  url: https://status.prewave.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.prewave.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/prewave-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/prewave-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/prewave-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/prewave-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/prewave-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/prewave-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/prewave-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/prewave-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/prewave-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prewave-onboard-and-monitor-supplier.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prewave-eudr-dds-submission.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prewave-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/prewave-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prewave-domain-security.yml
created: '2026-07-17'
description: Prewave is a Vienna-based AI-powered supply-chain risk intelligence platform that monitors millions of risk events across languages and networks to give enterprises proactive resilience, multi-tier supplier transparency, and sustainability-compliance automation (EU Deforestation Regulation, LkSG, and CSDDD). The Public Prewave API is a REST API at api.prewave.com covering suppliers and sites, collections and the Tier-N supplier graph, alerts and the risk feed, disruptions, risk scores (target, external, and enterprise export), exposure graphs, EUDR products / origin requests / Due Diligence Statements, actions, and user and role management. It authenticates with an X-Auth-Token API key.
image: https://www.prewave.com/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: Prewave MCP Server
  slug: prewave-mcp-server
modified: '2026-07-20'
name: Prewave
nav: Providers
network: true
overview: 'Prewave publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Alerts API, Collections - Management API, and 22 more. Tagged areas include Company, Saas, Supply Chain, Risk Intelligence, and Sustainability.


  Prewave''s developer surface includes documentation, API reference, engineering blog, changelog, authentication, and 22 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 40.4
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 58.5
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 41.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prewave/refs/heads/main/screenshots/prewave-2026-08-17T081335.png
security:
- kind: authentication
  name: Prewave Authentication
  slug: prewave-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Prewave Domain Security
  slug: prewave-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: trust-center
  name: Prewave Trust Center
  slug: prewave-trust-center
  summary_line: trust center published
slug: prewave
tags:
- Company
- Saas
- Supply Chain
- Risk Intelligence
- Sustainability
- Compliance
- EUDR
- Supplier Management
website: https://www.prewave.com/
---
