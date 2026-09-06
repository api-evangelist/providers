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
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Quotapath Agentic Access
  operation_count: 18
  slug: quotapath-agentic-access
  summary_line: 18 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.quotapath.com/v1
  baseurl_source: declared
  description: The data API from QuotaPath — 1 operation(s) for data.
  name: QuotaPath data API
  slug: quotapath-data-api
- baseURL: https://api.quotapath.com/v1
  baseurl_source: declared
  description: The deal API from QuotaPath — 3 operation(s) for deal.
  name: QuotaPath deal API
  slug: quotapath-deal-api
- baseURL: https://api.quotapath.com/v1
  baseurl_source: declared
  description: The path API from QuotaPath — 2 operation(s) for path.
  name: QuotaPath path API
  slug: quotapath-path-api
- baseURL: https://api.quotapath.com/v1
  baseurl_source: declared
  description: The payout API from QuotaPath — 3 operation(s) for payout.
  name: QuotaPath payout API
  slug: quotapath-payout-api
- baseURL: https://api.quotapath.com/v1
  baseurl_source: declared
  description: The plan API from QuotaPath — 1 operation(s) for plan.
  name: QuotaPath plan API
  slug: quotapath-plan-api
- baseURL: https://api.quotapath.com/v1
  baseurl_source: declared
  description: The team API from QuotaPath — 1 operation(s) for team.
  name: QuotaPath team API
  slug: quotapath-team-api
- baseURL: https://api.quotapath.com/v1
  baseurl_source: declared
  description: The user API from QuotaPath — 1 operation(s) for user.
  name: QuotaPath user API
  slug: quotapath-user-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: QuotaPath data API
  slug: open-quotapath-data-api
- collection_type: open
  name: QuotaPath data deal API
  slug: open-quotapath-deal-api
- collection_type: open
  name: QuotaPath data path API
  slug: open-quotapath-path-api
- collection_type: open
  name: QuotaPath data payout API
  slug: open-quotapath-payout-api
- collection_type: open
  name: QuotaPath data plan API
  slug: open-quotapath-plan-api
- collection_type: open
  name: QuotaPath data team API
  slug: open-quotapath-team-api
- collection_type: open
  name: QuotaPath data user API
  slug: open-quotapath-user-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/quotapath-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/quotapath-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quotapath-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/quotapath-authentication.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/quotapath-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/quotapath-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/quotapath-openapi-overlay.yaml
- group: design
  title: ''
  type: Conventions
  url: conventions/quotapath-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/quotapath-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/quotapath-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/quotapath-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.quotapath.com/
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.quotapath.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.quotapath.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.quotapath.com/docs/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.quotapath.com/docs/
- group: operate
  title: ''
  type: Support
  url: https://help.quotapath.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.quotapath.com/
- group: company
  title: ''
  type: Blog
  url: https://www.quotapath.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/quotapath
- group: commercial
  title: ''
  type: Pricing
  url: https://www.quotapath.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.quotapath.com/trial-start/
- group: start
  title: ''
  type: Login
  url: https://app.quotapath.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.quotapath.com/site-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.quotapath.com/privacy/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.quotapath.com/en/articles/8097859-api-documentation
- group: build
  title: ''
  type: Packages
  url: packages/quotapath-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/quotapath-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/quotapath-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/quotapath-problem-types.yml
created: '2026-07-17'
description: QuotaPath is a sales commission tracking and compensation management platform that helps revenue, finance, and sales operations teams design, automate, and audit variable-pay programs. It sits as a system of record between a company's CRM, finance stack, and payroll — pulling deals from HubSpot and Salesforce, applying commission plans, quotas, and ASC 606 ledger logic, and syncing payouts to accounting and HRIS systems like QuickBooks, NetSuite, and Rippling. QuotaPath exposes a REST API (available on the Premium tier) for pushing deals, reading payouts, managing quota assignments, and building custom CRM and payroll integrations. The API uses token-based API-key authentication over https://api.quotapath.com/v1 with limit/offset pagination.
image: https://storage.googleapis.com/quotapath-prod-app/qp_logos/logo_primary.png
layout: provider
modified: '2026-08-14'
name: QuotaPath
nav: Providers
network: true
overview: 'QuotaPath publishes 7 APIs on the [APIs.io](https://apis.io/) network, including data API, deal API, path API, and 4 more. Tagged areas include Company, Sales Commissions, Compensation Management, Sales Operations, and Revenue Operations.


  QuotaPath''s developer surface includes authentication, documentation, API reference, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Quotapath Plans Pricing
  plan_count: 3
  slug: quotapath-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Quotapath Rate Limits
  slug: quotapath-rate-limits
score:
  band: developing
  composite: 52.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 47.0
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 52.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quotapath/refs/heads/main/screenshots/quotapath-2026-08-17T081433.png
security:
- kind: authentication
  name: Quotapath Authentication
  slug: quotapath-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Quotapath Domain Security
  slug: quotapath-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Quotapath Trust Center
  slug: quotapath-trust-center
  summary_line: SOC 2, ISO 27001
slug: quotapath
tags:
- Company
- Sales Commissions
- Compensation Management
- Sales Operations
- Revenue Operations
- Finance
- Payouts
- CRM Integration
- Payroll
website: https://www.quotapath.com/
---
