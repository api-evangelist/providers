---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
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
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Dailypay Agentic Access
  operation_count: 18
  slug: dailypay-agentic-access
  summary_line: 18 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.dailypay.com/rest
  baseurl_source: declared
  description: The _accounts_ endpoint provides comprehensive information about money accounts. You can retrieve account details, including the account's unique ID, a link to the account holder, type, subtype, verif
  name: DailyPay Accounts API
  slug: dailypay-accounts-api
- baseURL: https://api.dailypay.com/rest
  baseurl_source: declared
  description: Securely tokenize personal cards for use in the accounts API.
  name: DailyPay Card Tokenization API
  slug: dailypay-card-tokenization-api
- baseURL: https://api.dailypay.com/rest
  baseurl_source: declared
  description: The _health_ endpoint provides a simple health check for the API. **Functionality:** Check the status of the API to ensure it is functioning correctly.
  name: DailyPay Health API
  slug: dailypay-health-api
- baseURL: https://api.dailypay.com/rest
  baseurl_source: declared
  description: The _jobs_ endpoint provides access to comprehensive information about a person's employment. It enables you to retrieve details about individual jobs, including information about the organization the
  name: DailyPay Jobs API
  slug: dailypay-jobs-api
- baseURL: https://api.dailypay.com/rest
  baseurl_source: declared
  description: The _organizations_ endpoint provides details about a business entity, such as an employer, or a group of people, such as a division. The response includes the organization name and ID which can be us
  name: DailyPay Organizations API
  slug: dailypay-organizations-api
- baseURL: https://api.dailypay.com/rest
  baseurl_source: declared
  description: The _paychecks_ endpoint provides detailed information about paychecks. You can retrieve individual paycheck details, including the person and job associated with the paycheck, its status, pay period,
  name: DailyPay Paychecks API
  slug: dailypay-paychecks-api
- baseURL: https://api.dailypay.com/rest
  baseurl_source: declared
  description: The _people_ endpoint allows you to see information related to who owns resources such as jobs and accounts. **Functionality:** Retrieve limited details about a person, including their name, global st
  name: DailyPay People API
  slug: dailypay-people-api
- baseURL: https://api.dailypay.com/rest
  baseurl_source: declared
  description: The _transfers_ endpoint allows you to initiate and track money movement. You can access transfer details, including the transfer's unique ID, amount, currency, status, schedule, submission and resolu
  name: DailyPay Transfers API
  slug: dailypay-transfers-api
artifact_total: 15
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/dailypay-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/dailypay-rest-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.dailypay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.dailypay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.dailypay.com/products/rest
- group: docs
  title: ''
  type: APIReference
  url: https://developer.dailypay.com/products/rest/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.dailypay.com/products/rest/guides/auth
- group: auth
  title: ''
  type: Authentication
  url: authentication/dailypay-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/dailypay-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://auth.dailypay.com/.well-known/openid-configuration
- group: operate
  title: ''
  type: Support
  url: https://www.dailypay.com/contact/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.dailypay.com/help/
- group: company
  title: ''
  type: Blog
  url: https://www.dailypay.com/resource-center/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.dailypay.com/resource-center/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dailypay
- group: start
  title: ''
  type: SignUp
  url: https://dailypay.app.link/vYyj0iSlyTb
- group: start
  title: ''
  type: Login
  url: https://account.dailypay.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dailypay.com/en-us/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dailypay.com/en-us/legal/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.dailypay.com/en-us/legal/compliance/
- group: auth
  title: ''
  type: TrustCenter
  url: security/dailypay-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.dailypay.com/security/vulnerability-disclosure-program/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dailypay-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dailypay-domain-security.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dailypay.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dailypay-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/dailypay-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dailypay-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dailypay-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/dailypay-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dailypay-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/dailypay-decline-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dailypay-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dailypay-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dailypay-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/dailypay-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dailypay-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dailypay-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/dailypay-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dailypay-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dailypay-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-01'
description: DailyPay is an on-demand pay (earned wage access) platform that lets employees access wages they have already earned before the scheduled payday. The company sells to employers across healthcare, retail, restaurants, manufacturing, hospitality and the public sector, and integrates with 180+ HCM, payroll and time-management systems. Its developer surface — the DailyPay REST API — is a json:api-shaped OAuth 2.0 / OpenID Connect API covering people, jobs, organizations, paychecks, accounts (including the EARNINGS_BALANCE account that carries available earnings), transfers and PCI-scoped debit-card tokenization, complemented by DailyPay Elements, a set of hosted drop-in iframe components for embedding on-demand pay into partner applications.
image: https://developer.dailypay.com/static/svgs/dp_text.svg
layout: provider
mcp_servers:
- description: ''
  name: DailyPay MCP Server
  slug: dailypay-mcp-server
modified: '2026-08-01'
name: DailyPay
nav: Providers
network: true
overview: 'DailyPay publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Card Tokenization API, Health API, and 5 more. Tagged areas include Company, Payments, Payroll, Human Resources, and Earned Wage Access.


  DailyPay''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, signup flow, and 35 more developer resources.'
random_paper: 0
scopes:
- name: Dailypay Scopes
  scope_count: 5
  slug: dailypay-scopes
  summary_line: 5 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 58.0
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 55.5
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 58.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 71.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dailypay/refs/heads/main/screenshots/dailypay-2026-08-07T164026.png
security:
- kind: authentication
  name: Dailypay Authentication
  slug: dailypay-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Dailypay Domain Security
  slug: dailypay-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dailypay Vulnerability Disclosure
  slug: dailypay-vulnerability-disclosure
  summary_line: Hackerone · security.txt
- kind: trust-center
  name: Dailypay Trust Center
  slug: dailypay-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: dailypay
tags:
- Company
- Payments
- Payroll
- Human Resources
- Earned Wage Access
- On-Demand Pay
- Financial-Services
- Fintech
- Money Transfer
- Benefits
website: https://www.dailypay.com/
---
