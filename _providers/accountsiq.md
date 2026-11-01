---
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: 'The current AIQ SOAP 1.1 integration web service. 219 operations covering customers, suppliers, stock items, sales and purchase invoices, credit and debit notes, orders, deliveries, general journals, '
  name: AccountsIQ Integration API 2.0
  slug: integration-2-0
- description: The legacy AIQ SOAP 1.1 integration web service, still published and supported alongside 2.0. 217 operations over the same accounting surface, authenticated with the Login method, which returns a sess
  name: AccountsIQ Integration API 1.1
  slug: integration-1-1
artifact_total: 13
common:
- group: auth
  href: https://artifacts.apis.io/accountsiq/security/accountsiq-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/accountsiq-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.accountsiq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://accountsiq.github.io/API-Wiki/
- group: docs
  title: ''
  type: Documentation
  url: https://accountsiq.github.io/API-Wiki/
- group: docs
  title: ''
  type: APIReference
  url: https://accountsiq.github.io/API-Wiki/specifications.html
- group: start
  title: ''
  type: GettingStarted
  url: https://accountsiq.github.io/API-Wiki/integration.html
- group: build
  title: ''
  type: Postman
  url: https://accountsiq.github.io/API-Wiki/postman-collection.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/accountsIQ
- group: operate
  title: ''
  type: Support
  url: https://www.accountsiq.com/success/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.accountsiq.com/
- group: company
  title: ''
  type: Blog
  url: https://www.accountsiq.com/resource/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.accountsiq.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.accountsiq.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.accountsiq.com/legal/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.accountsiq.com/legal/privacy-statement
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.accountsiq.com/
- group: auth
  href: https://artifacts.apis.io/accountsiq/conformance/accountsiq-conformance.yml
  title: ''
  type: Compliance
  url: conformance/accountsiq-conformance.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.accountsiq.com/
- group: agent
  href: https://artifacts.apis.io/accountsiq/llms/accountsiq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/accountsiq-llms.txt
- group: build
  title: ''
  type: Examples
  url: https://uk1.accountsiq.com/system/dashboard/integration/integration_1_1.asmx
- group: design
  href: https://artifacts.apis.io/accountsiq/lifecycle/accountsiq-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/accountsiq-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/accountsiq/conformance/accountsiq-conformance.yml
  title: ''
  type: Conformance
  url: conformance/accountsiq-conformance.yml
- group: start
  href: https://artifacts.apis.io/accountsiq/sandbox/accountsiq-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/accountsiq-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/accountsiq/plans/accountsiq-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/accountsiq-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/accountsiq/rate-limits/accountsiq-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/accountsiq-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/accountsiq/packages/accountsiq-packages.yml
  title: ''
  type: Packages
  url: packages/accountsiq-packages.yml
- group: auth
  href: https://artifacts.apis.io/accountsiq/security/accountsiq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/accountsiq-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/accountsiq/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/accountsiq/mcp/accountsiq-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/accountsiq-mcp.yml
created: '2026-09-06'
description: AccountsIQ is a cloud accounting and financial management platform for mid-sized businesses and multi-entity group structures, headquartered in Dublin, Ireland. The platform covers the general ledger, accounts receivable and payable, banking and bank-feed reconciliation, budgeting, cashflow forecasting, fixed assets, stock, sales and purchase order processing, multi-currency consolidation and business intelligence. Its public integration surface is the AIQ SOAP API, published as two WSDL contracts — Integration 1.1 (session-token Login authentication) and Integration 2.0 (OAuth 2.0 client-credentials via TokenGet/TokenRefresh) — served from four regional deployments (eu1, eu2, uk1, us1) and documented in the openly published AccountsIQ API Wiki, with first-party Postman collections for every region and version.
finops:
- has_sources: true
  method: derived
  name: Accountsiq Finops
  primary_unit: subscription
  service_category: ''
  slug: accountsiq-finops
  template: false
image: https://cdn.prod.website-files.com/6789021db7b1eb2a4e86ccba/68302f995f42ad33549c88c1_open-graph.png
layout: provider
modified: '2026-09-06'
name: AccountsIQ
nav: Providers
network: true
overview: 'AccountsIQ is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Accounting, Financial Management, Cloud Accounting, and ERP.


  AccountsIQ''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Accountsiq Plans Pricing
  plan_count: 4
  slug: accountsiq-plans-pricing
- name: Accountsiq Price Estimates
  plan_count: 0
  slug: accountsiq-price-estimates
random_paper: 2
rate_limits:
- limit_count: 0
  name: Accountsiq Rate Limits
  slug: accountsiq-rate-limits
score:
  band: developing
  composite: 49.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 6.5
    developer_ergonomics: 70.8
    discoverability: 66.1
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - ireland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 47.9
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/accountsiq/accountsiq-2026-10-11T092528.png
security:
- kind: authentication
  name: Accountsiq Authentication
  slug: accountsiq-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Accountsiq Domain Security
  slug: accountsiq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Accountsiq Trust Center
  slug: accountsiq-trust-center
  summary_line: ISO 27001, GDPR
skill_count: 4
skills:
- name: accountsiq-incremental-sync
  slug: accountsiq-incremental-sync
- name: accountsiq-onboard-integration
  slug: accountsiq-onboard-integration
- name: accountsiq-post-sales-invoice
  slug: accountsiq-post-sales-invoice
- name: accountsiq-reconcile-payments
  slug: accountsiq-reconcile-payments
slug: accountsiq
tags:
- Company
- Accounting
- Financial Management
- Cloud Accounting
- ERP
- Consolidation
- General Ledger
- Business Intelligence
- SOAP
- Ireland
website: https://www.accountsiq.com/
---
