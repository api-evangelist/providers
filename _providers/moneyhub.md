---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 42.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 36
  human_in_the_loop: 0
  name: Moneyhub Agentic Access
  operation_count: 77
  slug: moneyhub-agentic-access
  summary_line: 77 operations · 36 acting
api_count: 1
apis:
- description: Moneyhub's Open Banking Payments API initiates account-to-account payments (Payment Initiation Service) over the UK Faster Payments rails as a cheaper, near-instant alternative to cards, direct debits
  name: Moneyhub Open Banking Payments API
  slug: moneyhub-open-banking-payments-api
- description: The accounts API from Moneyhub — 6 operation(s) for accounts.
  name: Moneyhub Accounts API
  slug: moneyhub-accounts-api
- description: The affordability API from Moneyhub — 5 operation(s) for affordability.
  name: Moneyhub Affordability API
  slug: moneyhub-affordability-api
- description: The beneficiaries API from Moneyhub — 2 operation(s) for beneficiaries.
  name: Moneyhub Beneficiaries API
  slug: moneyhub-beneficiaries-api
- description: The categories API from Moneyhub — 3 operation(s) for categories.
  name: Moneyhub Categories API
  slug: moneyhub-categories-api
- description: The categorise transactions API from Moneyhub — 1 operation(s) for categorise transactions.
  name: Moneyhub categorise transactions API
  slug: moneyhub-categorise-transactions-api
- description: The counterparties API from Moneyhub — 2 operation(s) for counterparties.
  name: Moneyhub Counterparties API
  slug: moneyhub-counterparties-api
- description: The holdings API from Moneyhub — 3 operation(s) for holdings.
  name: Moneyhub Holdings API
  slug: moneyhub-holdings-api
- description: The notification thresholds API from Moneyhub — 2 operation(s) for notification thresholds.
  name: Moneyhub notification thresholds API
  slug: moneyhub-notification-thresholds-api
- description: The projects API from Moneyhub — 2 operation(s) for projects.
  name: Moneyhub Projects API
  slug: moneyhub-projects-api
- description: The regular transactions API from Moneyhub — 2 operation(s) for regular transactions.
  name: Moneyhub regular transactions API
  slug: moneyhub-regular-transactions-api
- description: The rental records API from Moneyhub — 2 operation(s) for rental records.
  name: Moneyhub rental records API
  slug: moneyhub-rental-records-api
- description: The savings goals API from Moneyhub — 2 operation(s) for savings goals.
  name: Moneyhub savings goals API
  slug: moneyhub-savings-goals-api
- description: The spending analysis API from Moneyhub — 1 operation(s) for spending analysis.
  name: Moneyhub spending analysis API
  slug: moneyhub-spending-analysis-api
- description: The spending goals API from Moneyhub — 2 operation(s) for spending goals.
  name: Moneyhub spending goals API
  slug: moneyhub-spending-goals-api
- description: The standard-financial-statements API from Moneyhub — 2 operation(s) for standard-financial-statements.
  name: Moneyhub Standard Financial Statements API
  slug: moneyhub-standard-financial-statements-api
- description: The standing orders API from Moneyhub — 1 operation(s) for standing orders.
  name: Moneyhub standing orders API
  slug: moneyhub-standing-orders-api
- description: The statements API from Moneyhub — 1 operation(s) for statements.
  name: Moneyhub Statements API
  slug: moneyhub-statements-api
- description: The sync API from Moneyhub — 1 operation(s) for sync.
  name: Moneyhub Sync API
  slug: moneyhub-sync-api
- description: The tax API from Moneyhub — 1 operation(s) for tax.
  name: Moneyhub Tax API
  slug: moneyhub-tax-api
- description: The transactions API from Moneyhub — 9 operation(s) for transactions.
  name: Moneyhub Transactions API
  slug: moneyhub-transactions-api
artifact_total: 31
asyncapis:
- description: ''
  name: Moneyhub Webhooks
  slug: moneyhub-webhooks
collections:
- collection_type: postman
  name: Moneyhub Data API
  slug: postman-moneyhub-data-api-swagger
- collection_type: open
  name: Moneyhub Data API
  slug: open-moneyhub-data-api-swagger
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/moneyhub-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/moneyhub/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/moneyhub-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/moneyhub-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://moneyhub.com/policies/security-and-trust-at-moneyhub/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/moneyhub-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://moneyhub.com/policies/security-and-trust-at-moneyhub/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moneyhub-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/moneyhub-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/moneyhub-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/moneyhub-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moneyhub-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/moneyhub-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/moneyhub-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/moneyhub-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://docs.moneyhubenterprise.com/docs/system-availability-and-performance-metrics
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.moneyhubenterprise.com/docs/versioning
- group: design
  title: ''
  type: Conformance
  url: conformance/moneyhub-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/moneyhub-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/moneyhub-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/moneyhub-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/moneyhub-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/moneyhub-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/moneyhub-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/moneyhub-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/moneyhub-webhooks.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/moneyhub-data-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.moneyhub.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.moneyhubenterprise.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.moneyhubenterprise.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://moneyhub.github.io/api-docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.moneyhubenterprise.com/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://identity.moneyhub.co.uk/oidc/.well-known/openid-configuration
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moneyhub
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/moneyhub
- group: company
  title: ''
  type: Blog
  url: https://www.moneyhub.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.moneyhub.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://moneyhub.com/policies/global-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.moneyhub.com/privacy-policy/
created: '2026-07-24'
description: 'Moneyhub is a UK open banking and open finance platform, headquartered in London with offices in Bristol and Ljubljana, that lets banks, pension providers, wealth managers, insurers and fintechs embed account aggregation, transaction data enrichment, financial insight and account-to-account payment initiation into their own products. Regulated by the FCA as an Account Information Service Provider (AISP), Payment Initiation Service Provider (PISP) and Credit Information Services Provider (CISP), Moneyhub ships a genuinely API-first surface: a RESTful, Swagger/OpenAPI-documented Data & Intelligence API for AIS aggregation, enrichment and affordability, and an Open Banking Payments API that initiates instant Faster Payments over the UK''s Open Banking rails as a cheaper alternative to cards and direct debits. Authentication and payment consent run entirely through an OpenID Connect / OAuth2 identity layer at identity.moneyhub.co.uk, with client-credentials, authorization-code
  and jwt-bearer grants and fine-grained scopes for data and payment initiation.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Moneyhub MCP Server
  slug: moneyhub-mcp-server
modified: '2026-07-24'
name: Moneyhub
nav: Providers
network: true
overview: 'Moneyhub publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Affordability API, Beneficiaries API, and 17 more. Tagged areas include Payments, United Kingdom, Open Banking, Open Finance, and Account-to-Account.


  The Moneyhub catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Moneyhub''s developer surface includes authentication, sandbox, changelog, documentation, API reference, getting-started guide, engineering blog, and 32 more developer resources.'
random_paper: 10
scopes:
- name: Moneyhub Scopes
  scope_count: 108
  slug: moneyhub-scopes
  summary_line: 108 scopes
score:
  band: strong
  composite: 60.7
  coverage:
    artifact_dirs: 24
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 57.7
    developer_ergonomics: 60.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 48.7
  previous_composite: 60.7
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: psd2
    - jurisdiction: UK
      standard: uk-open-banking
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 84.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moneyhub/refs/heads/main/screenshots/moneyhub-2026-08-07T184155.png
security:
- kind: authentication
  name: Moneyhub Authentication
  slug: moneyhub-authentication
  summary_line: oauth2/openIdConnect/http · 3 schemes
- kind: domain-security
  name: Moneyhub Domain Security
  slug: moneyhub-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Moneyhub Vulnerability Disclosure
  slug: moneyhub-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Moneyhub Trust Center
  slug: moneyhub-trust-center
  summary_line: ISO 27001
slug: moneyhub
tags:
- Payments
- United Kingdom
- Open Banking
- Open Finance
- Account-to-Account
- Payment Initiation
- Data Aggregation
- AISP
- PISP
- Fintech
website: https://www.moneyhub.com/
---
