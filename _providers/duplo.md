---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: true
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Atlas is Duplo''s global payments API for African and emerging-market businesses: collect payments (checkout, payment links, virtual accounts), disburse funds (single and bulk bank payouts, internation'
  name: Atlas Payments API
  slug: atlas-payments-api
artifact_total: 12
asyncapis:
- description: ''
  name: Duplo Atlas Webhooks
  slug: duplo-atlas-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/duplo/plans/duplo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/duplo-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://tryduplo.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://tryduplo.com/feed/
- group: auth
  href: https://artifacts.apis.io/duplo/security/duplo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/duplo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tryduplo.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tryduplo.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tryduplo.com/en/atlas
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tryduplo.com/en/atlas/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tryduplo.com/en/atlas/guides
- group: company
  title: ''
  type: Blog
  url: https://tryduplo.com/blog
- group: operate
  title: ''
  type: Support
  url: https://duplo.zohodesk.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tryduplo.com
- group: commercial
  title: ''
  type: Pricing
  url: https://tryduplo.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.tryduplo.com
- group: start
  title: ''
  type: Login
  url: https://dashboard.tryduplo.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tryduplo.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tryduplo.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tryduplo
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.tryduplo.com/en/atlas/changelogs
- group: auth
  href: https://artifacts.apis.io/duplo/conformance/duplo-conformance.yml
  title: ''
  type: Compliance
  url: conformance/duplo-conformance.yml
- group: auth
  href: https://artifacts.apis.io/duplo/authentication/duplo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/duplo-authentication.yml
- group: design
  href: https://artifacts.apis.io/duplo/conventions/duplo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/duplo-conventions.yml
- group: start
  href: https://artifacts.apis.io/duplo/sandbox/duplo-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/duplo-sandbox.yml
- group: design
  href: https://artifacts.apis.io/duplo/lifecycle/duplo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/duplo-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/duplo/conformance/duplo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/duplo-conformance.yml
- group: design
  href: https://artifacts.apis.io/duplo/asyncapi/duplo-atlas-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/duplo-atlas-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/duplo/mcp/duplo-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/duplo-mcp.yml
- group: agent
  href: https://artifacts.apis.io/duplo/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/duplo/data-model/duplo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/duplo-data-model.yml
- group: design
  href: https://artifacts.apis.io/duplo/errors/duplo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/duplo-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/duplo/llms/duplo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/duplo-llms.txt
created: '2026-07-17'
description: 'Duplo is a fintech company building the financial operating system for African and emerging-market businesses, headquartered in Lagos, Nigeria with operations in South Africa. Its platform unifies B2B payments and spend management: automated expense tracking with approval workflows, local and international (cross-border) payments, multi-currency global business accounts, NRS-compliant e-invoicing, direct debit, tax management, auto reconciliation, bulk payments to up to 500 recipients, and real-time financial reporting. For developers, Duplo exposes Atlas, a global payments API (base host atlas.tryduplo.com) covering collections/checkout, disbursements and bulk payouts, virtual accounts, payment links, exchange rates and FX swaps, wallet management, and e-invoicing, authenticated with Bearer API keys and delivering event notifications via webhooks. Duplo maintains PCI DSS, ISO 27001 and ISO 22301 certifications, is NDPR compliant, and operates under Central Bank of Nigeria
  oversight as a licensed Payment Service Solution Provider (PSSP).'
finops:
- has_sources: true
  method: derived
  name: Duplo Finops
  primary_unit: transaction
  service_category: ''
  slug: duplo-finops
  template: false
image: https://tryduplo.com/wp-content/uploads/2026/04/Dashboard-1-01-scaled.webp
layout: provider
modified: '2026-10-06'
name: Duplo
nav: Providers
network: true
overview: 'Duplo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, B2B Payments, and Cross-Border Payments.


  The Duplo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Duplo''s developer surface includes engineering blog, documentation, API reference, getting-started guide, support, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Duplo Plans Pricing
  plan_count: 10
  slug: duplo-plans-pricing
- name: Duplo Price Estimates
  plan_count: 0
  slug: duplo-price-estimates
random_paper: 20
score:
  band: strong
  composite: 58.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 42.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - nigeria
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
  previous_composite: 58.5
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 33.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/duplo/duplo-2026-07-25T212511.png
security:
- kind: authentication
  name: Duplo Authentication
  slug: duplo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Duplo Domain Security
  slug: duplo-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 5
skills:
- name: Send a bank payout
  slug: duplo-bank-payout
- name: Collect a payment with Atlas Checkout
  slug: duplo-collect-payment-checkout
- name: Issue an NRS-compliant e-invoice
  slug: duplo-einvoice
- name: Swap between currency pairs
  slug: duplo-fx-swap
- name: Create a customer with a virtual account and reconcile inflows
  slug: duplo-virtual-account-collection
slug: duplo
tags:
- Company
- Fintech
- Payments
- B2B Payments
- Cross-Border Payments
- Expense Management
- Virtual Accounts
- E-Invoicing
- Foreign Exchange
- Africa
- Nigeria
website: https://tryduplo.com
---
