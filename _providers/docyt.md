---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/docyt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.docyt.com/
- group: company
  title: ''
  type: Blog
  url: https://www.docyt.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.docyt.com/feed/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.docyt.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.docyt.com/sign_in
- group: operate
  title: ''
  type: Support
  url: https://www.docyt.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.docyt.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.docyt.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/docyt
- group: operate
  title: ''
  type: StatusPage
  url: https://docyt.statuspage.io/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/docyt/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@docytinc
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/docyt-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/docyt-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/docyt-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.docyt.com/security/
- group: build
  title: ''
  type: Packages
  url: packages/docyt-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/docyt-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/docyt-rate-limits.yml
coverage:
  checked: '2026-08-12'
  detail: Docyt sells end-user accounting software only — /developers, /developer, /api, /api-docs and /docs all 404 on www.docyt.com, its GitHub org publishes zero public repositories, and the /api/v1 surface visible in the app.docyt.com JavaScript bundle is a private backend for Docyt's own web and mobile clients that returns the SPA HTML shell, not JSON, to any unauthenticated caller.
  evidence:
  - status: 404
    url: https://www.docyt.com/developers
  - status: 404
    url: https://www.docyt.com/api-docs
  - status: 200
    url: https://app.docyt.com/openapi.json
  - status: 200
    url: https://app.docyt.com/api/v1/business_users
  - status: 200
    url: https://api.github.com/orgs/docyt/repos
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: 'Docyt is a Silicon Valley accounting-automation company that sells AI-driven bookkeeping software to small and mid-sized businesses, accounting firms, and multi-property hospitality and franchise operators. The platform digitizes source documents, categorizes and matches transactions, runs continuous bank and merchant reconciliation, handles bill pay and expense management, and closes the books against a real-time general ledger that syncs with QuickBooks, NetSuite, Sage, Xero and Zoho. Products include the HpAI (High Precision Accounting Intelligence) engine, Accountant Copilot for firms, ClosingFlow for month-end close, and ProfitBooks for self-serve small-business bookkeeping. Docyt publishes no public developer program: there is no developer portal, no API reference, and no machine-readable specification. Its application backend at app.docyt.com exposes a private /api/v1 surface consumed only by its own web and mobile clients, and the customer knowledge base redirects to
  a tenant sign-in.'
image: https://www.docyt.com/wp-content/uploads/2023/07/social-image-financial-insights.jpeg
layout: provider
modified: '2026-08-12'
name: Docyt
nav: Providers
network: true
overview: 'Docyt is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Accounting, Bookkeeping, Financial Operations, and Accounts Payable.


  Docyt''s developer surface includes engineering blog, pricing, support, YouTube channel, and 16 more developer resources.'
plans:
- name: Docyt Plans Pricing
  plan_count: 2
  slug: docyt-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Docyt Rate Limits
  slug: docyt-rate-limits
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 67.1
    commercial_clarity: 67.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 25.2
  provenance:
    conformance: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/docyt/refs/heads/main/screenshots/docyt-2026-09-02T145305.png
security:
- kind: domain-security
  name: Docyt Domain Security
  slug: docyt-domain-security
  summary_line: TLSv1.3 · DMARC
slug: docyt
tags:
- Company
- Accounting
- Bookkeeping
- Financial Operations
- Accounts Payable
- Expense Management
- Reconciliation
- Hospitality
- Artificial Intelligence
- Software-as-a-Service
website: https://www.docyt.com/
---
