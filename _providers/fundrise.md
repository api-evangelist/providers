---
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
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Fundrise Agentic Access
  operation_count: 17
  slug: fundrise-agentic-access
  summary_line: 17 operations · 7 acting
api_count: 2
apis:
- description: The Acknowledgments API provides acknowledgments needed to place Investments and Liquidations.
  name: Fundrise Acknowledgments API
  slug: fundrise-acknowledgments-api
- description: '### Getting access To get started, please contact the support team via <a href="mailto:connect@fundrise.com" target="_blank">connect@fundrise.com</a>. ### Terminology - <strong>Client</strong>: This r'
  name: Fundrise Authentication API
  slug: fundrise-authentication-api
- description: The Clients API provides operations for creating new Clients and updating fields for existing Clients. The Client represents an End-User of the platform. Newly created Clients will have exactly one ac
  name: Fundrise Clients API
  slug: fundrise-clients-api
- description: The Holdings API contains up-to-date information about the status and performance of a Client's holdings in Fundrise. This endpoint may be used to fetch holding information after a Client's initial Tr
  name: Fundrise Holdings API
  slug: fundrise-holdings-api
- description: The Investment APIs provide operations for placing and cancelling Investments in various Offerings on behalf of an authenticated Client.
  name: Fundrise Investments API
  slug: fundrise-investments-api
- description: The Liquidations APIs provide operations for a Client to place a Liquidation request. A Liquidation request results in selling shares in exchange for dollars.
  name: Fundrise Liquidations API
  slug: fundrise-liquidations-api
- description: The Offerings API contains information about all Offerings available via Fundrise Connect and documents associated with those offerings. Each Offering has a status indicating whether or not they are a
  name: Fundrise Offerings API
  slug: fundrise-offerings-api
- description: The Tax Form API provides operations for fetching tax document information for a given tax year.
  name: Fundrise Tax Forms API
  slug: fundrise-tax-forms-api
- description: The Transactions API provides operations for fetching Transactions (individual or bulk) on behalf of authenticated Clients.
  name: Fundrise Transactions API
  slug: fundrise-transactions-api
arazzos:
- description: 'The primary Fundrise Connect flow, modelled from the sequence Fundrise publishes under the "Workflow Example" tag of its own OpenAPI: create a Client, exchange the issued refresh token for a Client ac'
  name: Fundrise Connect — onboard a Client and place an Investment
  slug: fundrise-onboard-client-and-invest
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fundrise Connect (External API) Acknowledgments API
  slug: open-fundrise-acknowledgments-api
- collection_type: open
  name: Fundrise Connect (External API) Authentication API
  slug: open-fundrise-authentication-api
- collection_type: open
  name: Fundrise Connect (External API) Clients API
  slug: open-fundrise-clients-api
- collection_type: open
  name: Fundrise Connect (External API) Holdings API
  slug: open-fundrise-holdings-api
- collection_type: open
  name: Fundrise Connect (External API) Investments API
  slug: open-fundrise-investments-api
- collection_type: open
  name: Fundrise Connect (External API) Liquidations API
  slug: open-fundrise-liquidations-api
- collection_type: open
  name: Fundrise Connect (External API) Offerings API
  slug: open-fundrise-offerings-api
- collection_type: open
  name: Fundrise Connect (External API) Tax Forms API
  slug: open-fundrise-tax-forms-api
- collection_type: open
  name: Fundrise Connect (External API) Transactions API
  slug: open-fundrise-transactions-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/fundrise-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fundrise-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/fundrise-connect-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://fundrise.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fundrise.com/connect-api
- group: docs
  title: ''
  type: Documentation
  url: https://connect.fundrise.com/
- group: docs
  title: ''
  type: APIReference
  url: https://connect.fundrise.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://connect.fundrise.com/#tag/Authentication
- group: start
  title: ''
  type: SignUp
  url: https://fundrise.com/checkout-start
- group: start
  title: ''
  type: Login
  url: https://fundrise.com/login
- group: operate
  title: ''
  type: Support
  url: https://fundrise.com/help
- group: operate
  title: ''
  type: HelpCenter
  url: https://fundrise.com/help
- group: company
  title: ''
  type: Blog
  url: https://fundrise.com/education
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fundrise
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fundrise.com/website-documents/Terms%20of%20Service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fundrise.com/privacy-policy.html
- group: auth
  title: ''
  type: Security
  url: https://fundrise.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/fundrise-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fundrise-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fundrise-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fundrise-domain-security.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/fundrise-openid-configuration.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fundrise-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: 'Fundrise is a Washington, DC based financial technology company that gives individual investors direct access to private-market alternative assets — private real estate, private credit, and venture capital — through a family of non-traded funds it sponsors and manages. Founded in 2012 and an early user of the SEC''s Regulation A+ exemption, Fundrise packages institutional-grade private investments into low-minimum vehicles bought and held entirely online. Its developer-facing surface is Fundrise Connect, a REST API that lets banks, brokerages, investment apps and other financial platforms natively onboard their own end users (\"Clients\") into Fundrise offerings: create and update Clients, retrieve open Offerings and their historical daily NAV, fetch the offering documents and acknowledgments a Client must sign, place and cancel investments, request and cancel share liquidations, and read back holdings, transactions and tax forms. Access is gated — partners request credentials
  from the Fundrise Connect team — and the API is documented publicly with an OpenAPI 3.1 definition.'
image: https://fundrise.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Fundrise MCP Server
  slug: fundrise-mcp-server
modified: '2026-08-04'
name: Fundrise
nav: Providers
network: true
overview: 'Fundrise publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Acknowledgments API, Authentication API, Clients API, and 6 more. Tagged areas include Company, Financial-Services, Investing, Real-Estate, and Private Credit.


  Fundrise''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 18 more developer resources.'
random_paper: 3
rate_limits:
- limit_count: 0
  name: Fundrise Rate Limits
  slug: fundrise-rate-limits
scopes:
- name: Fundrise Scopes
  scope_count: 2
  slug: fundrise-scopes
  summary_line: 2 scopes
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 22
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 4.5
    contract_quality: 58.3
    developer_ergonomics: 51.8
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fundrise/refs/heads/main/screenshots/fundrise-2026-08-17T123444.png
security:
- kind: authentication
  name: Fundrise Authentication
  slug: fundrise-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Fundrise Domain Security
  slug: fundrise-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Fundrise Vulnerability Disclosure
  slug: fundrise-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: fundrise
tags:
- Company
- Financial-Services
- Investing
- Real-Estate
- Private Credit
- Venture Capital
- Alternative Assets
- Wealth Management
- Fintech
- Embedded Investing
website: https://fundrise.com/
---
