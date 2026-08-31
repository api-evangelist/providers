---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 34.7
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 36
  human_in_the_loop: 0
  name: Goodlord Agentic Access
  operation_count: 65
  slug: goodlord-agentic-access
  summary_line: 65 operations · 36 acting
api_count: 3
apis:
- description: Resource 'Agent' operations.
  name: Goodlord Agent API
  slug: goodlord-agent-api
- description: An application contains rental information and all of the applicants/guarantors which are applying for a tenancy.
  name: Goodlord Application API
  slug: goodlord-application-api
- description: Authentication operations
  name: Goodlord Authentication API
  slug: goodlord-authentication-api
- description: Resource 'Company' operations.
  name: Goodlord Company API
  slug: goodlord-company-api
- description: Resource 'File' operations.
  name: Goodlord File API
  slug: goodlord-file-api
- description: Resource 'InsuranceClaim' operations.
  name: Goodlord Insurance Claim API
  slug: goodlord-insuranceclaim-api
- description: Operations which are concerned around retrieving files
  name: Goodlord Media API
  slug: goodlord-media-api
- description: Resource 'Payment' operations.
  name: Goodlord Payment API
  slug: goodlord-payment-api
- description: Resource 'RentSchedule' operations.
  name: Goodlord Rent Schedule API
  slug: goodlord-rentschedule-api
- description: Resource 'RentScheduleRow' operations.
  name: Goodlord Rent Schedule Row API
  slug: goodlord-rentschedulerow-api
- description: Resource 'RentScheduleRowPostDto' operations.
  name: Goodlord Rent Schedule Row Post Dto API
  slug: goodlord-rentschedulerowpostdto-api
- description: Resource 'RentScheduleRowUpdate' operations.
  name: Goodlord Rent Schedule Row Update API
  slug: goodlord-rentschedulerowupdate-api
- description: Resource 'Role' operations.
  name: Goodlord Role API
  slug: goodlord-role-api
- description: Resource 'RoleGroup' operations.
  name: Goodlord Role Group API
  slug: goodlord-rolegroup-api
- description: A person who exists on an application.
  name: Goodlord Subject API
  slug: goodlord-subject-api
artifact_total: 25
asyncapis:
- description: ''
  name: Goodlord Referencing Webhooks
  slug: goodlord-referencing-webhooks
collections:
- collection_type: open
  name: Insurance App
  slug: open-goodlord-insurance-app-api
- collection_type: open
  name: Referencing API
  slug: open-goodlord-referencing-api-sandbox
- collection_type: open
  name: Referencing API
  slug: open-goodlord-referencing-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/goodlord-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/goodlord-referencing-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/goodlord-referencing-api-sandbox-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/goodlord-insurance-app-api-overlay.yaml
- group: design
  title: ''
  type: Conventions
  url: conventions/goodlord-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/goodlord-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/goodlord-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/goodlord-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://goodlord.statuspal.io/
- group: design
  title: ''
  type: Conformance
  url: conformance/goodlord-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.goodlord.com/
- group: start
  title: ''
  type: Sandbox
  url: sandbox/goodlord-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/goodlord-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/goodlord-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/goodlord-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/goodlord-referencing-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: APIReference
  url: https://portal.goodlord.co/portal/catalogue-products/referencing-product-1/dHlrL3Byb2QtcmVmZXJlbmNpbmctYXBp/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://portal.goodlord.co/blog/2024/8/22/getting-started-with-goodlords-referencing-api
- group: operate
  title: ''
  type: Support
  url: https://www.goodlord.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://agenthelp.goodlord.co/s/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.goodlord.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.goodlord.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/goodlord-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goodlord-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/goodlord-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/goodlord-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/goodlord-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.goodlord.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.goodlord.co/
- group: docs
  title: ''
  type: Documentation
  url: https://portal.goodlord.co/portal/catalogue-products
- group: company
  title: ''
  type: Blog
  url: https://www.goodlord.com/newsagent
- group: company
  title: ''
  type: Blog
  url: https://portal.goodlord.co/blog
- group: auth
  title: ''
  type: Authentication
  url: https://portal.goodlord.co/portal/catalogue-products/referencing-product-1
- group: other
  title: ''
  type: OpenIDConnectDiscovery
  url: https://login.goodlord.co/7ddbafdc-ee33-46fb-968a-3011e2a0a825/B2C_1A_2_SIGNUPORSIGNIN/v2.0/.well-known/openid-configuration
- group: start
  title: ''
  type: Login
  url: https://app.goodlord.co/
- group: company
  title: ''
  type: Partners
  url: https://www.goodlord.com/about/our-partners
- group: commercial
  title: ''
  type: Pricing
  url: https://www.goodlord.com/platform
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/goodlord
- group: operate
  title: ''
  type: Contact
  url: https://www.goodlord.com/contact-us
created: '2026-07-26'
description: 'Goodlord (Oh Goodlord Limited, London) is a United Kingdom PropTech platform that digitises the pre-tenancy and tenancy lifecycle for residential letting agents, landlords and tenants — tenant referencing, e-signed tenancy contracts, rent and deposit payments, rent protection insurance, guarantors, PEPs and sanctions checks, inventories, utility switching and end-of-tenancy. It sits in the middle of the UK rental value chain, between the agency CRM (Reapit, Alto, Street, Qube) and the regulated deposit schemes, insurers and utility suppliers, rather than on the listings side controlled by the Rightmove/Zoopla portal duopoly. Its API posture is unusually open for the UK sector but is honestly split in two — the documentation is genuinely public and the machine-readable contracts are downloadable without a login from a Tyk-powered developer portal at portal.goodlord.co, yet credentials are not self-serve: the portal''s own registration page returns "Registration is not allowed"
  and requires an invite code, and Goodlord''s own getting-started guide instructs developers to obtain sandbox and production access through a Goodlord sales manager or account manager. Public contract, partner-gated keys. There is no RESO reference of any kind — RESO is a US NAR/MLS construct with no United Kingdom counterpart — and Goodlord publishes no open data.'
image: https://www.goodlord.com/hubfs/goodlord-logo-1.jpg
layout: provider
mcp_servers:
- description: ''
  name: Goodlord MCP Server
  slug: goodlord-mcp-server
modified: '2026-07-26'
name: Goodlord
nav: Providers
network: true
overview: 'Goodlord publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Agent API, Application API, Authentication API, and 12 more. Tagged areas include Real-Estate, United Kingdom, PropTech, Property Management, and Rentals.


  The Goodlord catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Goodlord''s developer surface includes sandbox, API reference, getting-started guide, support, authentication, documentation, engineering blog, and 33 more developer resources.'
random_paper: 18
scopes:
- name: Goodlord Scopes
  scope_count: 2
  slug: goodlord-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: strong
  composite: 58.4
  coverage:
    artifact_dirs: 21
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 67.0
    developer_ergonomics: 66.1
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 58.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 71.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/goodlord/refs/heads/main/screenshots/goodlord-2026-08-07T165804.png
security:
- kind: authentication
  name: Goodlord Authentication
  slug: goodlord-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Goodlord Domain Security
  slug: goodlord-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Goodlord Trust Center
  slug: goodlord-trust-center
  summary_line: ISO 27001, GDPR
slug: goodlord
tags:
- Real-Estate
- United Kingdom
- PropTech
- Property Management
- Rentals
- Lettings
- Tenant Referencing
- Tenancy Management
- Insurance
- Payments
website: https://www.goodlord.com/
---
