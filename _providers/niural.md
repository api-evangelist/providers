---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Niural Agentic Access
  operation_count: 15
  slug: niural-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api-live.niural.com
  baseurl_source: declared
  description: The Authentication API from Niural — 1 operation(s) for authentication.
  name: Niural Authentication API
  slug: niural-authentication-api
- baseURL: https://api-live.niural.com
  baseurl_source: declared
  description: The Contracts API from Niural — 4 operation(s) for contracts.
  name: Niural Contracts API
  slug: niural-contracts-api
- baseURL: https://api-live.niural.com
  baseurl_source: declared
  description: The Invoices API from Niural — 2 operation(s) for invoices.
  name: Niural Invoices API
  slug: niural-invoices-api
- baseURL: https://api-live.niural.com
  baseurl_source: declared
  description: The Transactions API from Niural — 4 operation(s) for transactions.
  name: Niural Transactions API
  slug: niural-transactions-api
artifact_total: 22
asyncapis:
- description: ''
  name: Niural Webhooks
  slug: niural-webhooks
collections:
- collection_type: open
  name: Niural Public Authentication API
  slug: open-niural-authentication-api
- collection_type: open
  name: Niural Public Contracts API
  slug: open-niural-contracts-api
- collection_type: open
  name: Niural Public Invoices API
  slug: open-niural-invoices-api
- collection_type: open
  name: Niural Public Transactions API
  slug: open-niural-transactions-api
common:
- group: other
  href: https://artifacts.apis.io/niural/capabilities/niural-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/niural-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.niural.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.niural.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.niural.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.niural.com/reference/post_authenticate
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.niural.com/docs/get-started
- group: operate
  title: ''
  type: Support
  url: https://help.niural.com/
- group: company
  title: ''
  type: Blog
  url: https://www.niural.com/blogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Niural
- group: commercial
  title: ''
  type: Pricing
  url: https://www.niural.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.niural.com/auth/employer/register
- group: start
  title: ''
  type: Login
  url: https://app.niural.com/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.niural.com/legal/customer-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.niural.com/legal/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://trust.niural.com/
- group: auth
  href: https://artifacts.apis.io/niural/security/niural-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/niural-trust-center.yml
- group: docs
  href: https://artifacts.apis.io/niural/openapi/_original/niural-public-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/niural-public-api-openapi.yml
- group: other
  href: https://artifacts.apis.io/niural/overlays/niural-public-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/niural-public-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/niural/llms/niural-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/niural-llms.txt
- group: auth
  href: https://artifacts.apis.io/niural/authentication/niural-authentication.yml
  title: ''
  type: Authentication
  url: authentication/niural-authentication.yml
- group: design
  href: https://artifacts.apis.io/niural/conventions/niural-conventions.yml
  title: ''
  type: Conventions
  url: conventions/niural-conventions.yml
- group: design
  href: https://artifacts.apis.io/niural/errors/niural-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/niural-problem-types.yml
- group: design
  href: https://artifacts.apis.io/niural/lifecycle/niural-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/niural-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/niural/changelog/niural-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/niural-changelog.yml
- group: design
  href: https://artifacts.apis.io/niural/data-model/niural-data-model.yml
  title: ''
  type: DataModel
  url: data-model/niural-data-model.yml
- group: design
  href: https://artifacts.apis.io/niural/conformance/niural-conformance.yml
  title: ''
  type: Conformance
  url: conformance/niural-conformance.yml
- group: operate
  href: https://artifacts.apis.io/niural/rate-limits/niural-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/niural-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/niural/plans/niural-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/niural-plans-pricing.yml
- group: start
  href: https://artifacts.apis.io/niural/sandbox/niural-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/niural-sandbox.yml
- group: design
  href: https://artifacts.apis.io/niural/asyncapi/niural-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/niural-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/niural/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/niural/mcp/niural-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/niural-mcp.yml
- group: build
  href: https://artifacts.apis.io/niural/packages/niural-packages.yml
  title: ''
  type: Packages
  url: packages/niural-packages.yml
- group: auth
  href: https://artifacts.apis.io/niural/security/niural-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/niural-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/niural/security/niural-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/niural-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/niural/agentic-access/niural-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/niural-agentic-access.yml
created: '2026-08-04'
description: 'Niural is a US-headquartered global workforce platform that unifies US payroll, PEO, employer of record (EOR), agent of record (AOR), contractor management and cross-border contractor payments in 150+ countries inside a single system, with an AI layer (EMMA) that orchestrates payroll, compliance and expense approvals. Its public developer surface — the Niural Public API, documented on ReadMe at docs.niural.com — is narrower than the product: an OpenAPI 3.0.3 contract of 15 operations across four resources (authentication, pay-on-demand contractor contracts, invoices and transactions), served from separate sandbox and live hosts, authenticated with a client-credential exchange that returns a bearer JWT, with cursor pagination, a 25 requests/second rate limit, and three HMAC-SHA256-signed webhook events. Payroll, PEO, EOR and benefits are not exposed on the public API.'
finops:
- has_sources: true
  method: derived
  name: Niural Finops
  primary_unit: employee
  service_category: ''
  slug: niural-finops
  template: false
image: https://www.niural.com/favicon.ico
layout: provider
modified: '2026-08-04'
name: Niural
nav: Providers
network: true
overview: 'Niural publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Contracts API, Invoices API, and 1 more. Tagged areas include Company, Payroll, Human Resources, Employer of Record, and Contractor Management.


  The Niural catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Niural''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 29 more developer resources.'
plans:
- name: Niural Plans Pricing
  plan_count: 8
  slug: niural-plans-pricing
- name: Niural Price Estimates
  plan_count: 0
  slug: niural-price-estimates
random_paper: 3
rate_limits:
- limit_count: 1
  name: Niural Rate Limits
  slug: niural-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Niural API Rules
  rule_count: 51
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 1
  slug: niural-rules
score:
  band: strong
  composite: 62.2
  coverage:
    artifact_dirs: 30
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.0
  facets:
    access_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 55.1
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 57.9
  previous_composite: 57.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/niural/niural-2026-08-07T185346.png
security:
- kind: authentication
  name: Niural Authentication
  slug: niural-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Niural Domain Security
  slug: niural-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Niural Vulnerability Disclosure
  slug: niural-vulnerability-disclosure
  summary_line: Hackerone · security.txt
- kind: trust-center
  name: Niural Trust Center
  slug: niural-trust-center
  summary_line: SOC 2 Type II
skill_count: 3
skills:
- name: Invoice a contract and settle it with a transaction
  slug: niural-invoice-and-pay-contractor
- name: Onboard a contractor onto a pay-on-demand contract
  slug: niural-onboard-contractor
- name: Reconcile webhook events against the REST API
  slug: niural-reconcile-webhook-events
slug: niural
tags:
- Company
- Payroll
- Human Resources
- Employer of Record
- Contractor Management
- Global Payments
- Invoicing
- Compliance
- Fintech
website: https://www.niural.com/
---
