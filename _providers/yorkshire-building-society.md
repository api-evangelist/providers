---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 54.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Yorkshire Building Society Agentic Access
  operation_count: 78
  slug: yorkshire-building-society-agentic-access
  summary_line: 78 operations · 23 acting
api_count: 6
apis:
- description: OBIE Read/Write Account and Transaction Information (AISP) API v3.1.2 - lets FCA-authorised account information service providers retrieve account, balance, transaction, beneficiary, standing order, d
  name: Yorkshire Building Society Account Information API
  slug: ybs-account-information-api
- description: OBIE Read/Write Payment Initiation (PISP) API v3.1.2 - lets FCA-authorised payment initiation service providers set up domestic single, scheduled, standing-order and file payment consents and initiate
  name: Yorkshire Building Society Payment Initiation API
  slug: ybs-payment-initiation-api
- description: OBIE Read/Write Confirmation of Funds (CBPII) API v3.1.2 - lets FCA-authorised card-based payment instrument issuers set up a funds confirmation consent and confirm whether a specified amount is avail
  name: Yorkshire Building Society Confirmation of Funds API
  slug: ybs-confirmation-of-funds-api
- description: OBIE Read/Write Event Subscriptions API v3.1.2 - lets an onboarded TPP create, read and delete event subscriptions so it can receive aggregated-polling and real-time event notifications (for example c
  name: Yorkshire Building Society Event Subscriptions API
  slug: ybs-event-subscriptions-api
- description: OBIE Dynamic Client Registration (DCR) API v3.1 - lets an FCA-authorised TPP present its OBIE/eIDAS software statement and register a client application with the YBS and Chelsea Building Society autho
  name: Yorkshire Building Society Dynamic Client Registration API
  slug: ybs-dynamic-client-registration-api
- description: 'OBIE token endpoint (Generate Access Token API v3.1.0) - the OAuth2/OIDC token endpoint used by onboarded TPPs to exchange authorization codes and client credentials for access tokens against the YBS '
  name: Yorkshire Building Society Generate Access Token API
  slug: ybs-generate-access-token-api
artifact_total: 12
asyncapis:
- description: ''
  name: Yorkshire Building Society Events Webhooks
  slug: yorkshire-building-society-events-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/yorkshire-building-society-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yorkshire-building-society-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/yorkshire-building-society-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/yorkshire-building-society-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/yorkshire-building-society-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/yorkshire-building-society-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/yorkshire-building-society-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/yorkshire-building-society-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/yorkshire-building-society-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/yorkshire-building-society-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/yorkshire-building-society-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/yorkshire-building-society-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/yorkshire-building-society-events-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/yorkshire-building-society-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/yorkshire-building-society-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yorkshire-building-society-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/yorkshire-building-society-account-information-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/yorkshire-building-society-payment-initiation-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/yorkshire-building-society-confirmation-of-funds-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/yorkshire-building-society-event-subscriptions-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.ybs.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.ybs.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.ybs.co.uk/docs/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.ybs.co.uk/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://developers.ybs.co.uk/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.ybs.co.uk/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developers.ybs.co.uk/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yorkshire-building-society
created: '2026-07-23'
description: Yorkshire Building Society (YBS) is a UK mutual building society founded in 1864 and headquartered in Bradford, West Yorkshire. As a member-owned mutual rather than a shareholder-owned bank, it is owned by and run for the benefit of its savers and borrowers, with more than three million customers and around £66 billion in assets across the YBS Group, which trades under the Yorkshire Building Society, Chelsea Building Society (CBS), Norwich & Peterborough and Accord Mortgages brands. YBS is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the PRA as an FCA-authorised ASPSP. Although it is not one of the CMA9 banks mandated to build Open Banking, YBS is a voluntary participant in the UK Open Banking / PSD2 ecosystem and operates a public developer portal at developers.ybs.co.uk that documents its OBIE Read/Write API family - Account Information (AIS), Payment Initiation (PIS), Confirmation of Funds (CBPII), Event Subscriptions,
  Dynamic Client Registration, and token issuance - conformant to the Open Banking Implementation Entity (OBIE) Read/Write Data API Standard v3.1.2. Access to the production and sandbox surfaces (ob-ybs.api.ybs.co.uk / ob-che.api.ybs.co.uk and the matching sandbox hosts) is secured with FAPI-grade OAuth2/OIDC, PSD2 strong customer authentication, mutual-TLS transport authentication and PS256-signed JWTs, and is available to FCA-authorised third-party providers holding eIDAS/OBIE certificates.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: yorkshire-building-society-mcp.yml
  slug: yorkshire-building-society-mcpyml
modified: '2026-07-23'
name: Yorkshire Building Society
nav: Providers
network: true
overview: 'Yorkshire Building Society publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account Information API, Payment Initiation API, Confirmation of Funds API, and 1 more. Tagged areas include Financial Services, Banking, Building Society, Open Banking, and PSD2.


  The Yorkshire Building Society catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Yorkshire Building Society''s developer surface includes authentication, sandbox, documentation, getting-started guide, support, and 24 more developer resources.'
random_paper: 10
scopes:
- name: Yorkshire Building Society Scopes
  scope_count: 4
  slug: yorkshire-building-society-scopes
  summary_line: 4 scopes
score:
  band: developing
  composite: 44.1
  delta: -3.3
  facets:
    commercial_clarity: 21.1
    contract_quality: 53.7
    developer_ergonomics: 53.8
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 7.9
  previous_composite: 47.4
  provenance:
    agentic_access: derived
    conformance: first-party
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
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 60.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Yorkshire Building Society Authentication
  slug: yorkshire-building-society-authentication
  summary_line: oauth2/mutualTLS · 3 schemes
- kind: domain-security
  name: Yorkshire Building Society Domain Security
  slug: yorkshire-building-society-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: yorkshire-building-society
tags:
- Financial Services
- Banking
- Building Society
- Open Banking
- PSD2
- OBIE
- FAPI
- United Kingdom
- Payments
- Account Information
- Fintech
website: https://www.ybs.co.uk/
---
