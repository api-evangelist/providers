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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Kanmon Agentic Access
  operation_count: 35
  slug: kanmon-agentic-access
  summary_line: 35 operations · 14 acting · 1 human-in-the-loop
api_count: 14
apis:
- description: The Bank Accounts API from Kanmon — 2 operation(s) for bank accounts.
  name: Kanmon Bank Accounts API
  slug: kanmon-bank-accounts-api
- description: The Businesses API from Kanmon — 3 operation(s) for businesses.
  name: Kanmon Businesses API
  slug: kanmon-businesses-api
- description: The Connect Tokens API from Kanmon — 1 operation(s) for connect tokens.
  name: Kanmon Connect Tokens API
  slug: kanmon-connect-tokens-api
- description: The Documents API from Kanmon — 1 operation(s) for documents.
  name: Kanmon Documents API
  slug: kanmon-documents-api
- description: The Draw Requests API from Kanmon — 2 operation(s) for draw requests.
  name: Kanmon Draw Requests API
  slug: kanmon-draw-requests-api
- description: The Embedded Sessions API from Kanmon — 1 operation(s) for embedded sessions.
  name: Kanmon Embedded Sessions API
  slug: kanmon-embedded-sessions-api
- description: The Integrated MCA API from Kanmon — 2 operation(s) for integrated mca.
  name: Kanmon Integrated MCA API
  slug: kanmon-integrated-mca-api
- description: The Invoices API from Kanmon — 3 operation(s) for invoices.
  name: Kanmon Invoices API
  slug: kanmon-invoices-api
- description: The Issued Products API from Kanmon — 2 operation(s) for issued products.
  name: Kanmon Issued Products API
  slug: kanmon-issued-products-api
- description: The Offers API from Kanmon — 2 operation(s) for offers.
  name: Kanmon Offers API
  slug: kanmon-offers-api
- description: The Payments API from Kanmon — 3 operation(s) for payments.
  name: Kanmon Payments API
  slug: kanmon-payments-api
- description: The Prequalifications API from Kanmon — 1 operation(s) for prequalifications.
  name: Kanmon Prequalifications API
  slug: kanmon-prequalifications-api
- description: The Sandbox Utilities API from Kanmon — 2 operation(s) for sandbox utilities.
  name: Kanmon Sandbox Utilities API
  slug: kanmon-sandbox-utilities-api
- description: The Users API from Kanmon — 3 operation(s) for users.
  name: Kanmon Users API
  slug: kanmon-users-api
artifact_total: 34
asyncapis:
- description: ''
  name: Kanmon Webhooks
  slug: kanmon-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kanmon Public V2 Bank Accounts API
  slug: open-kanmon-bank-accounts-api
- collection_type: open
  name: Kanmon Public V2 Bank Accounts Businesses API
  slug: open-kanmon-businesses-api
- collection_type: open
  name: Kanmon Public V2 Bank Accounts Connect Tokens API
  slug: open-kanmon-connect-tokens-api
- collection_type: open
  name: Kanmon Public V2 Bank Accounts Documents API
  slug: open-kanmon-documents-api
- collection_type: open
  name: Kanmon Public V2 Bank Accounts Draw Requests API
  slug: open-kanmon-draw-requests-api
- collection_type: open
  name: Kanmon Public V2 Bank Accounts Embedded Sessions API
  slug: open-kanmon-embedded-sessions-api
- collection_type: open
  name: Kanmon Public V2 Bank Accounts Integrated MCA API
  slug: open-kanmon-integrated-mca-api
- collection_type: open
  name: Kanmon Public V2 Bank Accounts Invoices API
  slug: open-kanmon-invoices-api
- collection_type: open
  name: Kanmon Public V2 Bank Accounts Issued Products API
  slug: open-kanmon-issued-products-api
- collection_type: open
  name: Kanmon Public V2 Bank Accounts Offers API
  slug: open-kanmon-offers-api
- collection_type: open
  name: Kanmon Public V2 Bank Accounts Payments API
  slug: open-kanmon-payments-api
- collection_type: open
  name: Kanmon Public V2 Bank Accounts Prequalifications API
  slug: open-kanmon-prequalifications-api
- collection_type: open
  name: Kanmon Public V2 Bank Accounts Sandbox Utilities API
  slug: open-kanmon-sandbox-utilities-api
- collection_type: open
  name: Kanmon Public V2 Bank Accounts Users API
  slug: open-kanmon-users-api
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/kanmon-openapi-original.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/kanmon-openapi-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kanmon-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kanmon-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kanmon-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/kanmon-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kanmon-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kanmon-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kanmon-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/kanmon-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kanmon-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kanmon-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kanmon-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kanmon-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kanmon-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/kanmon-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kanmon-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://kanmon.dev
- group: docs
  title: ''
  type: Documentation
  url: https://kanmon.dev
- group: docs
  title: ''
  type: APIReference
  url: https://kanmon.dev
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kanmon
- group: company
  title: ''
  type: Blog
  url: https://www.kanmon.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.kanmon.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kanmon.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kanmon.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.kanmon.com
created: '2026-07-17'
description: Kanmon is an embedded-lending platform that lets vertical SaaS and business-management software offer working capital to their customers without becoming a lender themselves. Through the Kanmon Public V2 REST API and the embeddable Kanmon Connect UI, platforms can originate term loans, lines of credit, invoice financing, Accounts Payable financing, and integrated merchant cash advances. Kanmon is the licensed lender and owns underwriting, compliance, and credit risk, while partners integrate financing directly into their existing product with API keys, official SDKs, prebuilt borrower UI components, and outbound webhooks.
image: https://files.readme.io/c09d869-small-kanmon_logoicon_bw_black.png
layout: provider
mcp_servers:
- description: ''
  name: kanmon-mcp.yml
  slug: kanmon-mcpyml
modified: '2026-07-19'
name: Kanmon
nav: Providers
network: true
overview: 'Kanmon publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Bank Accounts API, Businesses API, Connect Tokens API, and 11 more. Tagged areas include Company, Fintech, Embedded Finance, Embedded Lending, and Lending.


  The Kanmon catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kanmon''s developer surface includes authentication, sandbox, documentation, API reference, engineering blog, support, and 21 more developer resources.'
random_paper: 48
score:
  band: developing
  composite: 40.8
  delta: -2.2
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 61.5
    developer_ergonomics: 48.2
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 43.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kanmon/refs/heads/main/screenshots/kanmon-2026-07-25T223455.png
security:
- kind: authentication
  name: Kanmon Authentication
  slug: kanmon-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Kanmon Domain Security
  slug: kanmon-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kanmon
tags:
- Company
- Fintech
- Embedded Finance
- Embedded Lending
- Lending
- Working Capital
- Invoice Financing
- API
website: https://www.kanmon.com
---
