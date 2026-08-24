---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 38.8
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 60
  human_in_the_loop: 0
  name: Bell Canada Agentic Access
  operation_count: 74
  slug: bell-canada-agentic-access
  summary_line: 74 operations · 60 acting
api_count: 4
apis:
- description: Bell's implementation of the TM Forum TMF621 Trouble Ticket Open API (Bell version v2.5, TMF621 v4.1.1), letting an enterprise or wholesale partner create, patch, retrieve and list trouble tickets aga
  name: Bell Canada Trouble Ticket API
  slug: bell-canada-trouble-ticket-api
- description: Bell's implementation of the TM Forum TMF641 Service Ordering Management Open API (Bell version v1.4, TMF641 v4.6), used by partners to place, amend, cancel and track service requests with Bell over a
  name: Bell Canada Service Order API
  slug: bell-canada-service-order-api
- description: 'Bell''s implementation of the TM Forum TMF639 Resource Inventory Management Open API (Bell version v1.6, TMF639 v4.1), exposing logical, physical and generic resource records so partners can query and '
  name: Bell Canada Resource Inventory Management API
  slug: bell-canada-resource-inventory-api
- description: 'Bell''s implementation of the TM Forum TMF655 Change Management Open API (Bell version v1.1, TMF655 v4.2), letting a partner raise, update, retrieve and list change requests against Bell services with '
  name: Bell Canada Change Management API
  slug: bell-canada-change-management-api
artifact_total: 13
asyncapis:
- description: ''
  name: Bell Canada Webhooks
  slug: bell-canada-webhooks
collections:
- collection_type: open
  name: API ChangeManagement
  slug: open-bell-canada-change-management-api
- collection_type: open
  name: Resource Inventory Management
  slug: open-bell-canada-resource-inventory-api
- collection_type: open
  name: API ServiceOrdering
  slug: open-bell-canada-service-order-api
- collection_type: open
  name: Trouble Ticket
  slug: open-bell-canada-trouble-ticket-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bell-canada-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bell-canada-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bell-canada-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bell-canada-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bell-canada-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bell-canada-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bell-canada-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bell-canada-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bell-canada-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bell-canada-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/bell-canada-examples.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bell-canada-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bell-canada-llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.bell.ca/faq/apis
- group: operate
  title: ''
  type: Support
  url: https://developer.bell.ca/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bellcanada
- group: company
  title: ''
  type: Website
  url: https://www.bell.ca
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bell.ca
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bell.ca/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developer.bell.ca/servicemanagement
- group: start
  title: ''
  type: SignUp
  url: https://developer.bell.ca/register
- group: operate
  title: ''
  type: Contact
  url: https://developer.bell.ca/contact
- group: company
  title: ''
  type: Partners
  url: https://developer.bell.ca/partners
- group: company
  title: ''
  type: Blog
  url: https://developer.bell.ca/article
- group: other
  title: ''
  type: Products
  url: https://developer.bell.ca/product
- group: commercial
  title: ''
  type: Privacy
  url: https://aliant.bell.ca/Security_and_privacy/Commitment_to_privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aliant.bell.ca/Legal_and_terms
- group: auth
  title: ''
  type: Security
  url: https://support.bell.ca/Billing-and-Accounts/Security_and_privacy
- group: other
  title: ''
  type: Company
  url: https://www.bce.ca
created: '2026-07-25'
description: 'Bell Canada is Canada''s largest communications company and the principal operating subsidiary of BCE Inc., providing wireless, wireline, internet, television and enterprise network services across Canada, and operating Bell Media as the country''s largest broadcaster. As a facilities-based mobile network operator and broadband carrier it sits at the connectivity layer of the telecom value chain, and its public API posture reflects that: Bell runs a real developer portal at developer.bell.ca whose only published API suite is a set of four TM Forum Open API aligned B2B service management interfaces — Trouble Ticket (TMF621), Service Order (TMF641), Resource Inventory (TMF639) and Change Management (TMF655) — for enterprise and wholesale partners integrating their ITSM systems with Bell. The Swagger 2.0 definitions and PDF specifications are downloadable without a login, but access to the sandbox and to any live endpoint requires a business registration form and manual approval;
  no base URL, no credential scheme and no self-serve key issuance is published, and the documented request examples redact the credential as a literal SECURITY_CREDENTIALS placeholder. Bell publishes no first-party CAMARA network APIs and runs no Open Gateway portal of its own. Its network APIs reach developers indirectly, through EnStream LP — the identity and fraud-signal joint venture Bell Mobility owns with Rogers and TELUS — which announced a partnership with Aduna, the Ericsson-and-carrier joint venture, on 27 February 2025 to distribute Canadian Number Verification and SIM Swap signals through Aduna''s CAMARA-aligned global channel. Bell is therefore an aggregator-mediated carrier: partner-gated on its own surface, reachable by developers only through a third party.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Bell Canada MCP Server
  slug: bell-canada-mcp-server
modified: '2026-07-25'
name: Bell Canada
nav: Providers
network: true
overview: 'Bell Canada publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Trouble Ticket API, Service Order API, Resource Inventory Management API, and 1 more. Tagged areas include Telecommunications, Canada, Mobile Network Operator, Broadband, and 5G.


  The Bell Canada catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bell Canada''s developer surface includes authentication, sandbox, code examples, getting-started guide, support, documentation, API reference, and 23 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 49.4
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 56.9
    developer_ergonomics: 66.1
    discoverability: 83.3
    governance: 16.7
    operational_transparency: 21.1
  previous_composite: 49.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 43.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bell-canada/refs/heads/main/screenshots/bell-canada-2026-08-07T162303.png
security:
- kind: authentication
  name: Bell Canada Authentication
  slug: bell-canada-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Bell Canada Domain Security
  slug: bell-canada-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bell-canada
tags:
- Telecommunications
- Canada
- Mobile Network Operator
- Broadband
- 5G
- IoT
- TM Forum
- BSS
- OSS
- Network APIs
- CAMARA
- Open Gateway
- Identity Verification
- SIM Swap
- Enterprise
website: https://www.bell.ca
---
