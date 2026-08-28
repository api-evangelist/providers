---
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: Propertyme Agentic Access
  operation_count: 86
  slug: propertyme-agentic-access
  summary_line: 86 operations · 38 acting
api_count: 11
apis:
- description: Read the contact records in a connected PropertyMe portfolio — owners, tenants, suppliers and the agency contact itself — with change-since-timestamp polling, contact alerts by type, images, and write
  name: PropertyMe Contacts API
  slug: propertyme-contacts-api
- description: The lot (property) record in a connected PropertyMe portfolio — list all lots changed since a timestamp, or filter to rentals, active sales, vacancies and archived lots, retrieve lot detail, contact a
  name: PropertyMe Properties API
  slug: propertyme-properties-api
- description: Read-only access to the tenancies in a connected PropertyMe portfolio and to tenancy balances, including a single tenancy balance record by id. This is the lettings ledger surface that most listing-or
  name: PropertyMe Tenancies API
  slug: propertyme-tenancies-api
- description: The full routine and entry/exit inspection lifecycle — create, query, search by contact or lot, filter by status, and drive an inspection through schedule, reschedule, inspect, close and reopen transi
  name: PropertyMe Inspections API
  slug: propertyme-inspections-api
- description: Maintenance work orders, in both a v1 and a newer v2 shape. Create and update jobs, search by due date, created date and status, move a job through approve, assign, complete, reject and reopen, manage
  name: PropertyMe Job Tasks API
  slug: propertyme-job-tasks-api
- description: General property management tasks distinct from maintenance jobs — list tasks changed since a timestamp, create and update a task, find a task by id, read the assigned task manager, and attach comment
  name: PropertyMe Tasks API
  slug: propertyme-tasks-api
- description: Create a new bill in a connected PropertyMe portfolio, including the supporting document, against the trust accounting ledger. This is the only transaction-writing operation exposed in the published c
  name: PropertyMe Bills API
  slug: propertyme-bills-api
- description: Typed dashboard aggregates over a connected portfolio — activities, communications, lots and transactions, each retrieved by dashboard item type. The read model behind the PropertyMe dashboard, drawin
  name: PropertyMe Dashboards API
  slug: propertyme-dashboards-api
- description: The file surface, exposed as sub-resources rather than a standalone collection — create documents against contacts, lots, owner and tenant folios, inspections, tasks and jobs, and list images for cont
  name: PropertyMe Documents and Images API
  slug: propertyme-documents-and-images-api
- description: The agency staff directory inside a connected portfolio — list all members, and resolve the responsible member for a lot, a task, a job or an inspection. Requires the contact:read scope.
  name: PropertyMe Members API
  slug: propertyme-members-api
- description: 'The consent seam. A single DELETE /v1/portfolios/disconnect operation severs the integration''s connection to the customer''s current portfolio. Every other operation in the API is implicitly scoped to '
  name: PropertyMe Portfolio Connection API
  slug: propertyme-portfolio-connection-api
arazzos:
- description: 'PropertyMe publishes no webhooks, so an integration keeps a portfolio current by polling the six change-since collections with an int64 Timestamp cursor. This workflow seeds the mirror from Timestamp '
  name: Connect a PropertyMe portfolio and run a change-since sync
  slug: propertyme-connect-and-sync
- description: The routine and entry/exit inspection lifecycle. Requires activity:read for the reads and activity:write for every transition. The permitted transition graph is not published, so each step reads curre
  name: Schedule, conduct, report and close a PropertyMe inspection
  slug: propertyme-inspection-cycle
- description: The maintenance work-order flow, using the v2 job-task shape for create and read and the shared v1 sub-resources for quotations, transitions and attachments. Requires activity:read and activity:write,
  name: Raise, quote, approve and complete a PropertyMe maintenance job
  slug: propertyme-maintenance-job
artifact_total: 20
collections:
- collection_type: open
  name: PropertyMe
  slug: open-propertyme
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/propertyme-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/propertyme-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/propertyme-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.propertyme.com.au/
- group: company
  title: ''
  type: About
  url: https://www.propertyme.com.au/about
- group: docs
  title: ''
  type: Documentation
  url: https://app.propertyme.com/api/swagger-ui/
- group: docs
  title: ''
  type: APIReference
  url: https://app.propertyme.com/api/swagger-ui/
- group: docs
  title: ''
  type: OpenAPI
  url: https://app.propertyme.com/api/openapi.json
- group: other
  title: ''
  type: OpenIDConnect
  url: authentication/propertyme-openid-configuration.json
- group: start
  title: ''
  type: SignUp
  url: https://www.propertyme.com.au/request-a-demo
- group: commercial
  title: ''
  type: Pricing
  url: https://www.propertyme.com.au/pricing
- group: auth
  title: ''
  type: Security
  url: https://www.propertyme.com.au/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.propertyme.com.au/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.propertyme.com.au/privacy
- group: operate
  title: ''
  type: Support
  url: https://support.propertyme.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.propertyme.com/
- group: company
  title: ''
  type: Blog
  url: https://www.propertyme.com.au/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.propertyme.com.au/feed
- group: company
  title: ''
  type: Partners
  url: https://www.propertyme.com.au/partner-directory
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PropertyMe
- group: build
  title: ''
  type: SampleCode
  url: https://github.com/PropertyMe/HelloPropertyMe.NET
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/propertyme
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UC99HN1NFPAYyXvyKyRhHkJQ
- group: operate
  title: ''
  type: Contact
  url: https://www.propertyme.com.au/contact
- group: agent
  title: ''
  type: WellKnown
  url: well-known/propertyme-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/propertyme-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/propertyme-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/propertyme-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/propertyme-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/propertyme-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/propertyme-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/propertyme-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/propertyme-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/propertyme-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/propertyme-openapi-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/propertyme-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/propertyme-connect-and-sync.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/propertyme-maintenance-job.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/propertyme-inspection-cycle.yml
created: '2026-07-26'
description: PropertyMe is an Australian cloud property management and trust accounting platform for residential real estate agencies, founded in 2013 and operated by MePay Holdings Pty Ltd (AFCA member ID 81095, AFS licence no. 528836), with roughly 1.7 million properties under management across Australia and New Zealand. In the Australian property value chain it sits on the PROPERTY MANAGEMENT rail rather than the listing or settlement rails — it does not operate a portal like REA Group's realestate.com.au or Domain, and it is not a PEXA conveyancing participant; it is the system of record for the rental portfolio, holding lots, tenancies, owners, tenants, suppliers, trust transactions, inspections, maintenance jobs and documents, plus its own MePay payments product and the Grow CRM and AiMe assistant products. Its API posture is unusually honest for this sector — the machine-readable contract is genuinely open while the credentials are not. A Swagger 2.0 document describing 75 paths,
  86 operations and 296 definitions is served anonymously with no login at https://app.propertyme.com/api/openapi.json, rendered by a public Swagger UI at https://app.propertyme.com/api/swagger-ui/, and the OpenID Connect discovery document at https://login.propertyme.com is also served anonymously and advertises the full scope list. But no self-serve developer signup, app registration route or public client-credential issuance path exists anywhere on propertyme.com.au, app.propertyme.com or any developer/developers/docs/api subdomain (none of which resolve); a developer must approach PropertyMe to be issued an OAuth client_id and client_secret, and every call is additionally scoped to one customer's portfolio that the agency itself connects and can disconnect. RESO is absent — PropertyMe does not appear in the RESO certification directory, there is no OData service, no $metadata document and no Universal Property Identifier, which is the expected Australian answer because RESO is a North
  American NAR/MLS construct with no Australian counterpart. PropertyMe publishes no open data.
image: https://www.propertyme.com.au/wp-content/themes/PropertyMe/assets/dist/favicons/android-icon-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: PropertyMe MCP Server
  slug: propertyme-mcp-server
modified: '2026-07-26'
name: PropertyMe
nav: Providers
network: true
overview: 'PropertyMe publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Contacts API, Properties API, Tenancies API, and 8 more. Tagged areas include Real-Estate, Australia, Property Management, Rentals, and PropTech.


  PropertyMe''s developer surface includes authentication, documentation, API reference, signup flow, pricing, support, engineering blog, and 33 more developer resources.'
random_paper: 19
scopes:
- name: Propertyme Scopes
  scope_count: 20
  slug: propertyme-scopes
  summary_line: 20 scopes · authorizationCode/clientCredentials/deviceCode/ciba
score:
  band: developing
  composite: 41.4
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 16.7
    contract_quality: 30.7
    developer_ergonomics: 37.5
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 28.9
  previous_composite: 41.4
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/propertyme/refs/heads/main/screenshots/propertyme-2026-07-27T125353.png
security:
- kind: authentication
  name: Propertyme Authentication
  slug: propertyme-authentication
  summary_line: openIdConnect/oauth2/http · 2 schemes
- kind: domain-security
  name: Propertyme Domain Security
  slug: propertyme-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: propertyme
tags:
- Real-Estate
- Australia
- Property Management
- Rentals
- PropTech
- Tenancy
- Trust Accounting
- Inspections
- Maintenance
- Documents
- Payments
- New Zealand
website: https://www.propertyme.com.au/
---
