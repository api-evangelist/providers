---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'Atlas is Duplo''s global payments API for African and emerging-market businesses: collect payments (checkout, payment links, virtual accounts), disburse funds (single and bulk bank payouts, internation'
  name: Atlas Payments API
  slug: atlas-payments-api
artifact_total: 4
asyncapis:
- description: ''
  name: Duplo Atlas Webhooks
  slug: duplo-atlas-webhooks
common:
- group: auth
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
  title: ''
  type: Compliance
  url: conformance/duplo-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/duplo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/duplo-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/duplo-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/duplo-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/duplo-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/duplo-atlas-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/duplo-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/duplo-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/duplo-problem-types.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/duplo-llms.txt
created: '2026-07-17'
description: 'Duplo is a fintech company building the financial operating system for African and emerging-market businesses, headquartered in Lagos, Nigeria with operations in South Africa. Its platform unifies B2B payments and spend management: automated expense tracking with approval workflows, local and international (cross-border) payments, multi-currency global business accounts, NRS-compliant e-invoicing, direct debit, tax management, auto reconciliation, bulk payments to up to 500 recipients, and real-time financial reporting. For developers, Duplo exposes Atlas, a global payments API (base host atlas.tryduplo.com) covering collections/checkout, disbursements and bulk payouts, virtual accounts, payment links, exchange rates and FX swaps, wallet management, and e-invoicing, authenticated with Bearer API keys and delivering event notifications via webhooks. Duplo maintains PCI DSS, ISO 27001 and ISO 22301 certifications, is NDPR compliant, and operates under Central Bank of Nigeria
  oversight as a licensed Payment Service Solution Provider (PSSP).'
image: https://tryduplo.com/wp-content/uploads/2026/04/Dashboard-1-01-scaled.webp
layout: provider
modified: '2026-07-18'
name: Duplo
nav: Providers
network: true
overview: 'Duplo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, B2B Payments, and Cross-Border Payments.


  The Duplo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Duplo''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 21 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 53.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
  previous_composite: 53.4
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 59.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/duplo/refs/heads/main/screenshots/duplo-2026-07-25T212511.png
security:
- kind: authentication
  name: Duplo Authentication
  slug: duplo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Duplo Domain Security
  slug: duplo-domain-security
  summary_line: TLSv1.3 · DMARC
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
