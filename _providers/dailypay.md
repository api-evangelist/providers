---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Dailypay Agentic Access
  operation_count: 18
  slug: dailypay-agentic-access
  summary_line: 18 operations · 6 acting
api_count: 1
apis:
- description: Embed DailyPay and On Demand Pay features into your application. A json:api-compliant REST API covering jobs, accounts, transfers, paychecks, organizations, people and debit-card tokenization, secured
  name: DailyPay Rest API
  slug: dailypay-rest-api
artifact_total: 8
common:
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
  name: dailypay-mcp.yml
  slug: dailypay-mcpyml
modified: '2026-08-01'
name: DailyPay
nav: Providers
network: true
overview: 'DailyPay publishes 1 API on the [APIs.io](https://apis.io/) network: Rest API. Tagged areas include Company, Payments, Payroll, Human Resources, and Earned Wage Access.


  DailyPay''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, signup flow, and 33 more developer resources.'
random_paper: 70
scopes:
- name: Dailypay Scopes
  scope_count: 5
  slug: dailypay-scopes
  summary_line: 5 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 58.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 61.4
    developer_ergonomics: 75.5
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 31.6
  previous_composite: 58.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 71.9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
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
- Financial Services
- Fintech
- Money Transfer
- Benefits
website: https://www.dailypay.com/
---
