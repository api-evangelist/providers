---
agent_readiness:
  band: agent-native
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
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 84
  human_in_the_loop: 4
  name: Customers Bank Agentic Access
  operation_count: 211
  slug: customers-bank-agentic-access
  summary_line: 211 operations · 84 acting · 4 human-in-the-loop
api_count: 10
apis:
- description: The AccountAccess API from Customers Bank — 8 operation(s) for accountaccess.
  name: Customers Bank Account Access API
  slug: customers-bank-accountaccess-api
- description: Allows for querying and managing of the Control Type (Dual or Single) on various accounts within the system
  name: Customers Bank Account Control Type API
  slug: customers-bank-accountcontroltype-api
- description: The AccountEntitlements API from Customers Bank — 2 operation(s) for accountentitlements.
  name: Customers Bank Account Entitlements API
  slug: customers-bank-accountentitlements-api
- description: The Accounts API from Customers Bank — 5 operation(s) for accounts.
  name: Customers Bank Accounts API
  slug: customers-bank-accounts-api
- description: The AddressBook API from Customers Bank — 15 operation(s) for addressbook.
  name: Customers Bank Address Book API
  slug: customers-bank-addressbook-api
- description: Provides endpoints to enable authentication to the Cubi api's
  name: Customers Bank Authenticate API
  slug: customers-bank-authenticate-api
- description: The Banks API from Customers Bank — 6 operation(s) for banks.
  name: Customers Bank Banks API
  slug: customers-bank-banks-api
- description: The BookTransfers API from Customers Bank — 6 operation(s) for booktransfers.
  name: Customers Bank Book Transfers API
  slug: customers-bank-booktransfers-api
- description: The BookTransferSearch API from Customers Bank — 2 operation(s) for booktransfersearch.
  name: Customers Bank Book Transfer Search API
  slug: customers-bank-booktransfersearch-api
- description: The ClientCredentials API from Customers Bank — 5 operation(s) for clientcredentials.
  name: Customers Bank Client Credentials API
  slug: customers-bank-clientcredentials-api
- description: The CorrespondentInstructions API from Customers Bank — 2 operation(s) for correspondentinstructions.
  name: Customers Bank Correspondent Instructions API
  slug: customers-bank-correspondentinstructions-api
- description: The Customers API from Customers Bank — 2 operation(s) for customers.
  name: Customers Bank Customers API
  slug: customers-bank-customers-api
- description: The EventHistory API from Customers Bank — 4 operation(s) for eventhistory.
  name: Customers Bank Event History API
  slug: customers-bank-eventhistory-api
- description: The EventTypes API from Customers Bank — 2 operation(s) for eventtypes.
  name: Customers Bank Event Types API
  slug: customers-bank-eventtypes-api
- description: The HomeRealmDiscovery API from Customers Bank — 2 operation(s) for homerealmdiscovery.
  name: Customers Bank Home Realm Discovery API
  slug: customers-bank-homerealmdiscovery-api
- description: Allow for querying and management of incoming ACH payments
  name: Customers Bank Incoming Ach API
  slug: customers-bank-incomingach-api
- description: The IncomingPayments API from Customers Bank — 8 operation(s) for incomingpayments.
  name: Customers Bank Incoming Payments API
  slug: customers-bank-incomingpayments-api
- description: The IncomingWiresV API from Customers Bank — 3 operation(s) for incomingwiresv.
  name: Customers Bank Incoming Wires V API
  slug: customers-bank-incomingwiresv-api
- description: The InterestPayments API from Customers Bank — 2 operation(s) for interestpayments.
  name: Customers Bank Interest Payments API
  slug: customers-bank-interestpayments-api
- description: The Loan API from Customers Bank — 6 operation(s) for loan.
  name: Customers Bank Loan API
  slug: customers-bank-loan-api
- description: The LoanApplication API from Customers Bank — 2 operation(s) for loanapplication.
  name: Customers Bank Loan Application API
  slug: customers-bank-loanapplication-api
- description: The Messages API from Customers Bank — 2 operation(s) for messages.
  name: Customers Bank Messages API
  slug: customers-bank-messages-api
- description: The NonAdmin API from Customers Bank — 4 operation(s) for nonadmin.
  name: Customers Bank Non Admin API
  slug: customers-bank-nonadmin-api
- description: The NotificationEmail API from Customers Bank — 3 operation(s) for notificationemail.
  name: Customers Bank Notification Email API
  slug: customers-bank-notificationemail-api
- description: Allows for querying and management of outgoing ACH payments
  name: Customers Bank Outgoing Ach API
  slug: customers-bank-outgoingach-api
- description: The OutgoingPayments API from Customers Bank — 15 operation(s) for outgoingpayments.
  name: Customers Bank Outgoing Payments API
  slug: customers-bank-outgoingpayments-api
- description: The OutgoingWiresV API from Customers Bank — 7 operation(s) for outgoingwiresv.
  name: Customers Bank Outgoing Wires V API
  slug: customers-bank-outgoingwiresv-api
- description: Allows for the querying of ACH partner programs available for use within the system. Partner programs are used when sending a payment in order to specify pre-built configurations under which the payme
  name: Customers Bank Partner Program API
  slug: customers-bank-partnerprogram-api
- description: The Partners API from Customers Bank — 4 operation(s) for partners.
  name: Customers Bank Partners API
  slug: customers-bank-partners-api
- description: Returns accounts related codes and definitions
  name: Customers Bank Reference Data API
  slug: customers-bank-referencedata-api
- description: The SearchIncomingWiresV API from Customers Bank — 1 operation(s) for searchincomingwiresv.
  name: Customers Bank Search Incoming Wires V API
  slug: customers-bank-searchincomingwiresv-api
- description: The SearchOutgoingWiresV API from Customers Bank — 1 operation(s) for searchoutgoingwiresv.
  name: Customers Bank Search Outgoing Wires V API
  slug: customers-bank-searchoutgoingwiresv-api
- description: The Subaccounts API from Customers Bank — 5 operation(s) for subaccounts.
  name: Customers Bank Subaccounts API
  slug: customers-bank-subaccounts-api
- description: The Tags API from Customers Bank — 2 operation(s) for tags.
  name: Customers Bank Tags API
  slug: customers-bank-tags-api
- description: The Users API from Customers Bank — 6 operation(s) for users.
  name: Customers Bank Users API
  slug: customers-bank-users-api
- description: The UserSettings API from Customers Bank — 1 operation(s) for usersettings.
  name: Customers Bank User Settings API
  slug: customers-bank-usersettings-api
- description: The Webhooks API from Customers Bank — 8 operation(s) for webhooks.
  name: Customers Bank Webhooks API
  slug: customers-bank-webhooks-api
- description: The WebPubSub API from Customers Bank — 1 operation(s) for webpubsub.
  name: Customers Bank Web Pub Sub API
  slug: customers-bank-webpubsub-api
artifact_total: 54
asyncapis:
- description: ''
  name: Customers Bank Webhooks
  slug: customers-bank-webhooks
collections:
- collection_type: open
  name: Accounts
  slug: open-customers-bank-accounts
- collection_type: open
  name: ACH
  slug: open-customers-bank-ach
- collection_type: open
  name: ConsumerLending
  slug: open-customers-bank-consumerlending
- collection_type: open
  name: InstantPayments
  slug: open-customers-bank-instantpayments
- collection_type: open
  name: IT Operations
  slug: open-customers-bank-itoperations
- collection_type: open
  name: Partners
  slug: open-customers-bank-partners
- collection_type: open
  name: Security
  slug: open-customers-bank-security
- collection_type: open
  name: Transfers
  slug: open-customers-bank-transfers
- collection_type: open
  name: Webhooks
  slug: open-customers-bank-webhooks
- collection_type: open
  name: Wires
  slug: open-customers-bank-wires
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/customers-bank-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/customers-bank-accounts-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/customers-bank-ach-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/customers-bank-consumerlending-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/customers-bank-instantpayments-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/customers-bank-itoperations-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/customers-bank-partners-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/customers-bank-security-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/customers-bank-transfers-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/customers-bank-webhooks-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/customers-bank-wires-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/customers-bank-authenticate-and-list-accounts.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/customers-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/customers-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.customersbank.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cubiapi.readme.io
- group: docs
  title: ''
  type: Documentation
  url: https://cubiapi.readme.io/docs/getting-started
- group: agent
  title: ''
  type: MCPServer
  url: https://cubiapi.readme.io/mcp
- group: agent
  title: ''
  type: MCPServer
  url: mcp/customers-bank-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/customers-bank-tool-crosswalk.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CustomersBank
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/customers-bank
- group: start
  title: ''
  type: GettingStarted
  url: https://cubiapi.readme.io/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://cubiapi.readme.io/reference
- group: auth
  title: ''
  type: Authentication
  url: authentication/customers-bank-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/customers-bank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/customers-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/customers-bank-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/customers-bank-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/customers-bank-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/customers-bank-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/customers-bank-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/customers-bank-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/customers-bank-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/customers-bank-llms.txt
- group: agent
  title: ''
  type: AgentSkills
  url: skills/_index.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.customersbank.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.customersbank.com/terms-of-use/
created: '2026-07-23'
description: Customers Bank is a Pennsylvania state-chartered, FDIC-insured full-service commercial bank and the principal subsidiary of Customers Bancorp, Inc. (NYSE CUBI), a super-regional bank holding company with roughly $22 billion in assets headquartered in West Reading, Pennsylvania. Beyond traditional commercial and consumer banking it operates a national embedded-banking / Banking-as-a-Service platform, exposing a first-party, OAuth2-secured REST API surface (accounts, ACH, wires, instant payments, book transfers, consumer lending, plus partner, IT-operations and webhook management) to fintech and corporate partners through a public ReadMe developer portal at cubiapi.readme.io, complete with a hosted Model Context Protocol (MCP) server for AI agents. This is proprietary, partner-gated integration infrastructure rather than an FDX or CFPB Section 1033 consumer-permissioned data-sharing API; no FDX-conformant or Section 1033 data-access endpoint is publicly documented, and the surface
  is a sandbox-first partner API secured by OAuth2 client-credentials with HMAC-signed webhooks.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Customers Bank MCP Server
  slug: customers-bank-mcp-server
- description: Customers Bank hosts a remote Model Context Protocol server (the ReadMe generic MCP) that lets AI editors (Cursor, Windsurf, Claude Desktop) browse the API/documentation and execute requests against t
  name: Customers Bank MCP Server
  slug: customers-bank-mcp-server-2
modified: '2026-07-23'
name: Customers Bank
nav: Providers
network: true
overview: 'Customers Bank publishes 38 APIs on the [APIs.io](https://apis.io/) network, including Account Access API, Account Control Type API, Account Entitlements API, and 35 more. Tagged areas include Financial-Services, Banking, United States, Banking as a Service, and Embedded Finance.


  The Customers Bank catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Customers Bank''s developer surface includes documentation, getting-started guide, API reference, authentication, changelog, sandbox, and 32 more developer resources.'
random_paper: 5
score:
  band: developing
  composite: 41.6
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 2.2
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 60.4
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 38
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 49.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/customers-bank/refs/heads/main/screenshots/customers-bank-2026-07-25T211012.png
security:
- kind: authentication
  name: Customers Bank Authentication
  slug: customers-bank-authentication
  summary_line: oauth2/http-bearer/hmac · 3 schemes
- kind: domain-security
  name: Customers Bank Domain Security
  slug: customers-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: customers-bank
tags:
- Financial-Services
- Banking
- United States
- Banking as a Service
- Embedded Finance
- Payments
- Commercial Banking
website: https://www.customersbank.com
---
