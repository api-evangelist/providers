---
access_model:
  confidence: medium
  label: Paid · Partner/sales onboarding (API keys via developer portal)
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - documentation
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: Data Access is MX's open-finance API platform for sharing an institution's financial data and accessing other institutions' data using FDX and OAuth standards, with tokenized, consumer-permissioned ac
  name: MX Data Access
  slug: mx-data-access
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The Accounts endpoints represent a user's checking, savings, mortgage, 401(k), or other types of accounts held by a financial institution. An account belongs to a `member`, which represents the user's
  name: MX Accounts API
  slug: mx-accounts-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: 'The features documented here are in a beta state, and this documentation is considered draft material subject to frequent change. Using our Platform API, you can securely submit ACH Returns to reduce '
  name: MX ach return API
  slug: mx-ach-return-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: Use these endpoints to create and manage budgets for your end users. You can create a budget for a specific category or autogenerate a budget for several categories based on existing transactions. Eac
  name: MX Budgets API
  slug: mx-budgets-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: A `transaction` can have its `category` set to one of MX’s default categories or a custom category for a specific `user`. See [Default Categories and Subcategories](docs.mx.com/api-reference/platform-
  name: MX Categories API
  slug: mx-categories-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: Consent Management
  name: MX Consent Management API
  slug: mx-consent-management-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: Use these endpoints to create and manage goals for a `user`. You can also reposition goals to adjust their priority levels. Every goal has a track type and a meta type. The [track type](docs.mx.com/ap
  name: MX Goals API
  slug: mx-goals-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: Use these endpoints to build customizable user experiences in UIs powered by our Financial Insights data. With Financial Insights, your users will receive personalized insights based on their transact
  name: MX Insights API
  slug: mx-insights-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: Institutions represent a financial institution. A single real-world financial institution may have several `institution` objects on the MX platform. For example, the mortgage division of a financial i
  name: MX Institutions API
  slug: mx-institutions-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: Investment Data Enhancement lets you connect to an end user's financial institution and retrieve cleansed and enhanced investment data. By combining investment data with retail banking information, yo
  name: MX investment holdings API
  slug: mx-investment-holdings-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The jobs API from MX — 1 operation(s) for jobs.
  name: MX Jobs API
  slug: mx-jobs-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The managed data [deprecated] API from MX — 7 operation(s) for managed data [deprecated].
  name: MX managed data [deprecated] API
  slug: mx-managed-data-deprecated-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: Members represent the connection between an end user and a financial institution. This institution may represent your institution or another one from which MX is aggregating data. For more info, see [
  name: MX Members API
  slug: mx-members-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: Merchants are representations of a transaction’s origin. For example, if you buy a coffee at Starbucks, the transaction merchant will be `Starbucks`. Use the `merchant_guid` and a `merchant_location_g
  name: MX Merchants API
  slug: mx-merchants-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: Microdeposits is an additional verification method that allows you to verify account details and navigate the process of using microdeposits and the automated clearing house (ACH) system. Make two, sm
  name: MX Microdeposits API
  slug: mx-microdeposits-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The monthly cash flow profile API from MX — 1 operation(s) for monthly cash flow profile.
  name: MX monthly cash flow profile API
  slug: mx-monthly-cash-flow-profile-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: 'You can only use notifications endpoints if you’re using the MX mobile application. All notifications created through the API will be of notification type `API_NOTIFICATION`, channel `PUSH`, and will '
  name: MX Notifications API
  slug: mx-notifications-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The processor token API from MX — 6 operation(s) for processor token.
  name: MX processor token API
  slug: mx-processor-token-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The rewards API from MX — 4 operation(s) for rewards.
  name: MX Rewards API
  slug: mx-rewards-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: Use the Spending Plan endpoints to create your own version of our [Spending Plan Widget](docs.mx.com/products/experience/pfm/legacy-widget-overviews/spending-plan), which helps end users track their s
  name: MX spending plan API
  slug: mx-spending-plan-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: With Statements, you can retrieve a user's monthly account statements in PDF format. This data can be used for solutions like personal financial management or risk analysis.
  name: MX Statements API
  slug: mx-statements-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: Tags and taggings are two resources in the MX Platform API that, when used together, give end users more control over organizing their transactions. A tag is a custom label that can be applied to a tr
  name: MX Taggings API
  slug: mx-taggings-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: Tags and taggings are two resources in the MX Platform API that, when used together, give end users more control over organizing their transactions. A tag is a custom label that can be applied to a tr
  name: MX Tags API
  slug: mx-tags-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: Transaction Rules allow users to automatically recategorize or rename all similar transactions according to their preferences. This only applies to future transactions. When recategorizing or renaming
  name: MX transaction rules API
  slug: mx-transaction-rules-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: Transactions represent any instance in which money moves into or out of an account. This could be a purchase at a business, a payroll deposit, a transfer from one account to another, an ATM withdrawal
  name: MX Transactions API
  slug: mx-transactions-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: Users represent an end user using the Platform API through your web or mobile app. Users are created by MX clients and belong to a specific [client](docs.mx.com/products/connectivity/overview/data-arc
  name: MX Users API
  slug: mx-users-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: MX provides Verifiable Credential endpoints that comply with web5 standards. For more info, see [Verifiable Credentials Overview](docs.mx.com/api-reference/reference/verifiable-credentials).
  name: MX verifiable credentials API
  slug: mx-verifiable-credentials-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: Use the [Request Widget URL](docs.mx.com/api-reference/platform-api/reference/request-widget-url) endpoint to generate a URL that loads one of our widgets. Many request body parameters only work for s
  name: MX Widgets API
  slug: mx-widgets-api
artifact_total: 39
asyncapis:
- description: ''
  name: Mx Webhooks
  slug: mx-webhooks
collections:
- collection_type: postman
  name: Consent Management V4 API
  slug: postman-mx-consent-management
- collection_type: postman
  name: MX Platform API
  slug: postman-mx-platform-api
- collection_type: open
  name: Consent Management V4 API
  slug: open-mx-consent-management
- collection_type: open
  name: MX Platform API
  slug: open-mx-platform-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/mx-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mx-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/mx-platform-api-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/mx/overview
- group: auth
  title: ''
  type: TrustCenter
  url: security/mx-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mx-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mx-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mx-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.mx.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.mx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mx.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mxenabled
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/425337
- group: company
  title: ''
  type: Blog
  url: https://www.mx.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mx.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mx.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://support.mx.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mx.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.mx.com/api-reference/platform-api/overview/versioning
- group: auth
  title: ''
  type: Security
  url: https://mx.com/security-policy/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/mx-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mx-well-known.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.mx.com/trust/
- group: build
  title: ''
  type: Packages
  url: packages/mx-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mx-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mx-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/mx-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mx-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mx-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mx-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mx-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/mx-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/mx-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mx-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mx-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mx-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.mx.com/sign_up
created: '2026-07-23'
description: MX Technologies is a privately held financial data platform headquartered in Lehi, Utah, operating as a B2B data aggregator and open-finance infrastructure provider rather than a chartered bank or credit union. MX connects consumer and business accounts across tens of thousands of financial institutions and fintechs, then cleanses, categorizes, and enhances the resulting transaction data so banks and fintechs can build verification, aggregation, and personal-finance experiences. Unlike most US banks, MX runs a real, self-documented developer surface — the MX Platform API (HTTP Basic auth over https://api.mx.com), a Consent Management API, and a Data Access product that shares and consumes institution data using FDX and OAuth standards — with downloadable OpenAPI 3.0 specifications published at docs.mx.com. MX is one of the major US open-finance aggregators (alongside Plaid, Finicity, and Akoya) and positions Data Access as FDX-conformant, consumer-permissioned, tokenized data
  sharing.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: MX MCP Server
  slug: mx-mcp-server
modified: '2026-07-23'
name: MX
nav: Providers
network: true
overview: 'MX publishes 27 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, ach return API, Budgets API, and 24 more. Tagged areas include Financial-Services, Banking, United States, Open Finance, and Data Aggregation.


  The MX catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MX''s developer surface includes authentication, documentation, engineering blog, support, changelog, sandbox, signup flow, and 31 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 4
  name: Mx Rate Limits
  slug: mx-rate-limits
score:
  band: strong
  composite: 62.6
  coverage:
    artifact_dirs: 25
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 64.0
    developer_ergonomics: 56.5
    discoverability: 61.1
    governance: 18.2
    operational_transparency: 92.1
  previous_composite: 62.6
  provenance:
    conformance: first-party
    contracts:
      callable: 96.3
      derived: 0
      marker_coverage: 0.0
      total: 27
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 64.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mx/refs/heads/main/screenshots/mx-2026-08-07T184503.png
security:
- kind: authentication
  name: Mx Authentication
  slug: mx-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Mx Domain Security
  slug: mx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mx Vulnerability Disclosure
  slug: mx-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Mx Trust Center
  slug: mx-trust-center
  summary_line: SOC 2, PCI DSS
slug: mx
tags:
- Financial-Services
- Banking
- United States
- Open Finance
- Data Aggregation
- FDX
- Fintech
- Financial Data
website: https://www.mx.com/
---
