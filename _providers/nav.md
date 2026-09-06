---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.2
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: REST API for Nav partner integrations. Partners authenticate with a Bearer token API key issued during onboarding and use it to create Nav accounts for their users, fetch account state, change an acco
  name: Nav Partner API
  slug: nav-partner-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nav-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nav.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.nav.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.nav.com/docs/guides/intro
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.nav.com/docs/rest-api/partner-api
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.nav.com/docs/widgets/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.nav.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.nav.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nav.com/nav-prime/
- group: start
  title: ''
  type: SignUp
  url: https://app.nav.com/registration/
- group: start
  title: ''
  type: Login
  url: https://app.nav.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nav.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nav.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nav.com/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/nav-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nav-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/nav-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nav-packages.yml
- group: design
  title: ''
  type: Components
  url: components/nav-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nav-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nav-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nav-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/nav-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nav-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/nav-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nav-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nav-problem-types.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nav-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nav-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/nav-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nav-llms.txt
created: '2026-08-26'
description: 'Nav Technologies, Inc. is a US financial-technology company (not a bank) that gives small business owners one place to see their business and personal credit, cash-flow health and funding eligibility, then matches them to a marketplace of financing and business credit card offers. Consumer-facing products are Nav Prime (business credit building with tradelines, five bureau scores from D&B, Experian, Equifax and TransUnion, bookkeeping and a FICO SBSS score), the Nav Credit Builder Card and a mobile app. The developer surface is the Nav Partner API — a REST API at api.nav.com used by embedded-finance platforms to create Nav accounts, change plans, end a partner relationship, resolve bureau credit visibility and mint single-use SSO tokens — together with the @navinc/widget-sdk embeddable widget SDK, which renders Nav business-credit UI inside a partner''s own application as the <nav-credit-widget> custom element. Access is partner-gated: API keys are issued during onboarding
  and there is no self-serve developer signup.'
image: https://api-docs.nav.com/img/nav-logo-on-light.svg
layout: provider
modified: '2026-08-26'
name: Nav
nav: Providers
network: true
overview: 'Nav publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Business Credit, Small Business, Financial-Services, Embedded Finance, and Lending.


  Nav''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Nav Plans Pricing
  plan_count: 4
  slug: nav-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Nav Rate Limits
  slug: nav-rate-limits
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 41.7
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nav/refs/heads/main/screenshots/nav-2026-09-02T150726.png
security:
- kind: authentication
  name: Nav Authentication
  slug: nav-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Nav Domain Security
  slug: nav-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: nav
tags:
- Business Credit
- Small Business
- Financial-Services
- Embedded Finance
- Lending
- Credit Scores
- Credit Reporting
- Financing Marketplace
- Fintech
- Partner API
website: https://www.nav.com/
---
