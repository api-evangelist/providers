---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 43
  human_in_the_loop: 0
  name: Pexa Agentic Access
  operation_count: 87
  slug: pexa-agentic-access
  summary_line: 87 operations · 43 acting
api_count: 7
apis:
- description: The PEXA Exchange API covers key facets of PEXA Exchange e-conveyancing functionality — creating and updating workspaces, invitations, participants, land title references, documents, conversations, fi
  name: PEXA Exchange API
  slug: pexa-exchange-api
- description: The Billing API from PEXA — 1 operation(s) for billing.
  name: PEXA Billing API
  slug: pexa-billing-api
- description: The Conversation API from PEXA — 8 operation(s) for conversation.
  name: PEXA Conversation API
  slug: pexa-conversation-api
- description: The Document API from PEXA — 4 operation(s) for document.
  name: PEXA Document API
  slug: pexa-document-api
- description: The HealthCheck API from PEXA — 2 operation(s) for healthcheck.
  name: PEXA Health Check API
  slug: pexa-healthcheck-api
- description: The Invitation API from PEXA — 6 operation(s) for invitation.
  name: PEXA Invitation API
  slug: pexa-invitation-api
- description: The Landtitle API from PEXA — 2 operation(s) for landtitle.
  name: PEXA Landtitle API
  slug: pexa-landtitle-api
- description: The Notification API from PEXA — 1 operation(s) for notification.
  name: PEXA Notification API
  slug: pexa-notification-api
- description: The Notification Service [$] API from PEXA — 0 operation(s) for notification service [$].
  name: PEXA Notification Service [$] API
  slug: pexa-notification-service-api
- description: Registration related endpoints
  name: PEXA Notification Registration API
  slug: pexa-notificationregistration-api
- description: The Project API from PEXA — 4 operation(s) for project.
  name: PEXA Project API
  slug: pexa-project-api
- description: The Settlement API from PEXA — 8 operation(s) for settlement.
  name: PEXA Settlement API
  slug: pexa-settlement-api
- description: The Standalone Discharge Experience API from PEXA — 1 operation(s) for standalone discharge experience.
  name: PEXA Standalone Discharge Experience API
  slug: pexa-standalone-discharge-experience-api
- description: The Subscriber API from PEXA — 6 operation(s) for subscriber.
  name: PEXA Subscriber API
  slug: pexa-subscriber-api
- description: The TitleSearch API from PEXA — 3 operation(s) for titlesearch.
  name: PEXA Title Search API
  slug: pexa-titlesearch-api
- description: The User API from PEXA — 2 operation(s) for user.
  name: PEXA User API
  slug: pexa-user-api
- description: The Workspace API from PEXA — 9 operation(s) for workspace.
  name: PEXA Workspace API
  slug: pexa-workspace-api
- description: The Workspaces API from PEXA — 6 operation(s) for workspaces.
  name: PEXA Workspaces API
  slug: pexa-workspaces-api
artifact_total: 32
asyncapis:
- description: ''
  name: Pexa Notification Webhooks
  slug: pexa-notification-webhooks
collections:
- collection_type: postman
  name: Notification Service [$]
  slug: postman-pexa-notification-service
- collection_type: postman
  name: PEXA Plus Marketplace B2B API
  slug: postman-pexa-plus-marketplace-b2b-api-oas300
- collection_type: postman
  name: PEXA Plus Marketplace B2B API
  slug: postman-pexa-plus-marketplace-b2b-api
- collection_type: postman
  name: Projects API
  slug: postman-pexa-projects-api-v4
- collection_type: postman
  name: Standalone Discharge Experience API
  slug: postman-pexa-standalone-discharge-experience-api
- collection_type: open
  name: PEXA Exchange API
  slug: open-pexa-exchange-api-legacy-swagger
- collection_type: open
  name: PEXA Exchange API
  slug: open-pexa-exchange-api-swagger
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/pexa-capability-edges.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/pexa-discharge-a-mortgage.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/pexa-order-a-title-search.md
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/pexa/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pexa-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pexa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pexa-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pexa-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pexa-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.pexa.com.au/
- group: start
  title: ''
  type: Portal
  url: https://developer.pexa.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.pexa.com.au/
- group: start
  title: ''
  type: SignUp
  url: https://www.pexa.com.au/pexa-apis/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pexa.com.au/api-pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pexa.com.au/staticly-media/2024/10/PEXA_Integration_Principles-sm-1728949058.pdf
- group: auth
  title: ''
  type: Authentication
  url: https://auth.pexa.com.au/.well-known/openid-configuration
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pexa.com.au/
- group: operate
  title: ''
  type: Support
  url: https://www.pexa.com.au/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.pexa-group.com/content-hub/news/
- group: company
  title: ''
  type: About
  url: https://www.pexa-group.com/about/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.pexa-group.com/investor-centre/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pexa-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/pexa-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.pexa.com.au/security/
- group: design
  title: ''
  type: Conventions
  url: conventions/pexa-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/pexa-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pexa-error-codes.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/pexa-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pexa-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pexa-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.pexa.com.au/Exchange/docs/changelog/
- group: start
  title: ''
  type: Sandbox
  url: sandbox/pexa-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pexa-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://compliance.pexa.com.au/
- group: design
  title: ''
  type: DataModel
  url: data-model/pexa-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/pexa-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/pexa-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pexa-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pexa-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/pexa-notification-webhooks.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/pexa-exchange-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/pexa-exchange-legacy-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/pexa-projects-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/pexa-notification-service-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/pexa-standalone-discharge-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/pexa-plus-marketplace-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/pexa-plus-marketplace-oas300-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.pexa.com.au/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.pexa.com.au/Exchange/api/apireference/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.pexa.com.au/pexa-apis/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.pexa.com.au/s/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pexa.com.au/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pexa.com.au/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PEXA-AU
created: '2026-07-26'
description: 'PEXA (Property Exchange Australia) operates Australia''s dominant Electronic Lodgement Network (ELN), the digital rail on which property is settled and title dealings are lodged with the state land registries. Where the Australian real estate value chain splits into a listings duopoly (REA Group and Domain) sitting over progressively privatised state land registries, PEXA occupies the transaction layer underneath both — electronic conveyancing, settlement funds movement, digital signing and lodgement — and e-conveyancing is now effectively mandated for most dealings in most Australian jurisdictions, making PEXA the closest thing in the property sector to a required, national, machine-readable rail. Its API posture is correspondingly unusual: PEXA publishes a genuine developer portal at developer.pexa.com.au with Swagger UI reference documentation and machine-readable OpenAPI/Swagger contracts for the Exchange, Projects, Notification (webhooks), Standalone Discharge and PEXA
  Plus Marketplace APIs, and the ARNECC Model Operating Requirements oblige it to offer API access to third parties on an equivalent basis. But that surface is not self-serve: PEXA states plainly that access to the Developer Portal and to test or production credentials is contingent on having signed PEXA''s API Agreement, so a developer registers via a form, is validated and approved, signs an agreement, and is then issued OAuth 2.0 client credentials (or mutual TLS). RESO is absent — it is a North American MLS standard with no bearing on Australian e-conveyancing — so there is no RESO Web API or Data Dictionary certification here, and none should be expected. This is a well-documented, regulated, licensed-access API estate rather than an open one.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pexa.png
layout: provider
mcp_servers:
- description: ''
  name: Candidate MCP tool surface derived from PEXA operations
  slug: candidate-mcp-tool-surface-derived-from-pexa-operations
modified: '2026-07-26'
name: PEXA
nav: Providers
network: true
overview: 'PEXA publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Exchange API, Billing API, Conversation API, and 15 more. Tagged areas include Real-Estate, Australia, Conveyancing, Property Settlement, and Land Registry.


  The PEXA catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PEXA''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, support, engineering blog, and 48 more developer resources.'
random_paper: 10
scopes:
- name: Pexa Scopes
  scope_count: 11
  slug: pexa-scopes
  summary_line: 11 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 51.2
  coverage:
    artifact_dirs: 25
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 58.9
    developer_ergonomics: 54.2
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 51.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 28.6
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pexa/refs/heads/main/screenshots/pexa-2026-07-27T125357.png
security:
- kind: authentication
  name: Pexa Authentication
  slug: pexa-authentication
  summary_line: oauth2/mutualTLS · 3 schemes
- kind: domain-security
  name: Pexa Domain Security
  slug: pexa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Pexa Vulnerability Disclosure
  slug: pexa-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: pexa
tags:
- Real-Estate
- Australia
- Conveyancing
- Property Settlement
- Land Registry
- Title
- PropTech
- Mortgage
- Digital Signing
- Webhook
website: https://www.pexa.com.au/
---
