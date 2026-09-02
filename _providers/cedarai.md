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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-01'
api_count: 8
apis:
- description: The ChargeService API from Cedarai — 3 operation(s) for chargeservice.
  name: Cedarai ChargeService API
  slug: cedarai-chargeservice-api
- description: The Equipment History API from Cedarai — 1 operation(s) for equipment history.
  name: Cedarai Equipment History API
  slug: cedarai-equipment-history-api
- description: The Ims API from Cedarai — 16 operation(s) for ims.
  name: Cedarai Ims API
  slug: cedarai-ims-api
- description: The InvoicesService API from Cedarai — 3 operation(s) for invoicesservice.
  name: Cedarai InvoicesService API
  slug: cedarai-invoicesservice-api
- description: The LindaService API from Cedarai — 9 operation(s) for lindaservice.
  name: Cedarai LindaService API
  slug: cedarai-lindaservice-api
- description: The NetworkStructureService API from Cedarai — 1 operation(s) for networkstructureservice.
  name: Cedarai NetworkStructureService API
  slug: cedarai-networkstructureservice-api
- description: The QuotesService API from Cedarai — 3 operation(s) for quotesservice.
  name: Cedarai QuotesService API
  slug: cedarai-quotesservice-api
- description: The TruckLoadTenderService API from Cedarai — 5 operation(s) for truckloadtenderservice.
  name: Cedarai TruckLoadTenderService API
  slug: cedarai-truckloadtenderservice-api
- description: The WorkOrderService API from Cedarai — 10 operation(s) for workorderservice.
  name: Cedarai WorkOrderService API
  slug: cedarai-workorderservice-api
artifact_total: 23
asyncapis:
- description: ''
  name: Cedarai Webhooks
  slug: cedarai-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: protobuf/arms/charge.proto ChargeService API
  slug: open-cedarai-chargeservice-api
- collection_type: open
  name: protobuf/arms/charge.proto ChargeService Equipment History API
  slug: open-cedarai-equipment-history-api
- collection_type: open
  name: protobuf/arms/charge.proto ChargeService Ims API
  slug: open-cedarai-ims-api
- collection_type: open
  name: protobuf/arms/charge.proto ChargeService InvoicesService API
  slug: open-cedarai-invoicesservice-api
- collection_type: open
  name: protobuf/arms/charge.proto ChargeService LindaService API
  slug: open-cedarai-lindaservice-api
- collection_type: open
  name: protobuf/arms/charge.proto ChargeService NetworkStructureService API
  slug: open-cedarai-networkstructureservice-api
- collection_type: open
  name: protobuf/arms/charge.proto ChargeService QuotesService API
  slug: open-cedarai-quotesservice-api
- collection_type: open
  name: protobuf/arms/charge.proto ChargeService TruckLoadTenderService API
  slug: open-cedarai-truckloadtenderservice-api
- collection_type: open
  name: protobuf/arms/charge.proto ChargeService WorkOrderService API
  slug: open-cedarai-workorderservice-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cedarai-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cedarai-external-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://cedarai.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cedarai.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cedarai.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cedarai.com/user-docs/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cedarai.com/user-docs/admin/getting-started
- group: start
  title: ''
  type: Login
  url: https://arms.cedarai.com/
- group: company
  title: ''
  type: Blog
  url: https://cedarai.com/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cedarai.com/privacy-policy/
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://www.cedarai.com/aup/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cedarai.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/cedarai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cedarai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cedarai-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cedarai-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cedarai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cedarai-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cedarai-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cedarai-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cedarai-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cedarai-domain-security.yml
created: '2026-07-17'
description: Cedar AI builds ARMS (Automated Rail Management System), a cloud-native, AI-powered transportation management platform for railroads, industrial shippers, transload and intermodal terminals, and fleet/car owners. The ARMS External API exposes REST and gRPC services for railcar inventory and history, waybills and bills of lading, work orders and train movements, switching and class lists, charges, shipper invoices and quotes, truck load tenders, network structure, and threaded notes (Linda) with AI summaries — plus Ed25519-signed webhooks for real-time operational events, across US (cedarai.com) and EU (cedarai.se) regions. Backed by Felicis.
image: https://arms.cedarai.com/cedar-icon.svg
layout: provider
mcp_servers:
- description: ''
  name: Cedarai MCP Server
  slug: cedarai-mcp-server
modified: '2026-07-18'
name: Cedarai
nav: Providers
network: true
overview: 'Cedarai publishes 9 APIs on the [APIs.io](https://apis.io/) network, including ChargeService API, Equipment History API, Ims API, and 6 more. Tagged areas include Company, Rail, Transportation, Logistics, and Freight.


  The Cedarai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cedarai''s developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, and 18 more developer resources.'
random_paper: 20
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 18
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 4.5
    contract_quality: 63.6
    developer_ergonomics: 54.2
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 40.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cedarai/refs/heads/main/screenshots/cedarai-2026-07-25T204839.png
security:
- kind: authentication
  name: Cedarai Authentication
  slug: cedarai-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Cedarai Domain Security
  slug: cedarai-domain-security
  summary_line: TLSv1.2 · DMARC
slug: cedarai
tags:
- Company
- Rail
- Transportation
- Logistics
- Freight
- Supply Chain
- Railcar Management
- Transportation Management System
- Fleet Management
- Artificial Intelligence
website: https://cedarai.com
---
