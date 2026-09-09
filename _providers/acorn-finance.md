---
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-08'
api_count: 1
apis:
- description: The Acorn Finance partner REST API. Basic-authenticated JSON endpoints on api.acornfinance.com let point-of-sale and contractor-software partners create companies and company users, retrieve loan appl
  name: Acorn Finance Partner API
  slug: acorn-finance-partner-api
artifact_total: 6
asyncapis:
- description: ''
  name: Acorn Finance Postback Webhooks
  slug: acorn-finance-postback-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.acornfinance.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.acornfinance.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.acornfinance.com/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.acornfinance.com/api-applications
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.acornfinance.com/api-sign-up
- group: start
  title: ''
  type: SignUp
  url: https://sign-up.acornfinance.com/
- group: start
  title: ''
  type: Login
  url: https://my.acornfinance.com/
- group: operate
  title: ''
  type: Support
  url: https://www.acornfinance.com/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.acornfinance.com/faq/
- group: company
  title: ''
  type: Blog
  url: https://www.acornfinance.com/blogpost_category/news/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.acornfinance.com/contractors/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acornfinance.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acornfinance.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/headwaysales
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acorn-finance-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/acorn-finance-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/acorn-finance-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/acorn-finance-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/acorn-finance-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/acorn-finance-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/acorn-finance-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/acorn-finance-postback-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/acorn-finance-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/acorn-finance-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/acorn-finance-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/acorn-finance-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/acorn-finance-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acorn-finance-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acorn-finance-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/acorn-finance-mcp.yml
created: '2026-09-06'
description: Acorn Finance, operated by Headway Sales Inc. (NMLS ID# 1817022) of Sacramento, California, runs an embedded lending marketplace for home improvement and business financing. Consumers pre-qualify for personal loans of $1,000 to $100,000 through a soft credit pull and compare offers from a network of lending partners, while contractors, dealers and point-of-sale software vendors embed those offers into estimates, invoices, quotes, carts and PDFs. Acorn Finance publishes a public partner developer program at docs.acornfinance.com covering a Basic-authenticated REST API on api.acornfinance.com (company and user provisioning, loan application retrieval, API key rotation and lowest-payment-amount quoting), a partner postback webhook, and a family of embeddable JavaScript widgets served from widgets-cdn.acornfinance.com.
image: https://www.acornfinance.com/wp-content/uploads/2022/02/acorn-finance-logo-compressed.svg
layout: provider
modified: '2026-09-06'
name: Acorn Finance
nav: Providers
network: true
overview: 'Acorn Finance publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Lending, Loans, and Home Improvement.


  The Acorn Finance catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Acorn Finance''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, pricing, and 23 more developer resources.'
plans:
- name: Acorn Finance Plans Pricing
  plan_count: 1
  slug: acorn-finance-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Acorn Finance Rate Limits
  slug: acorn-finance-rate-limits
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 67.1
    commercial_clarity: 67.1
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 37.3
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Acorn Finance Authentication
  slug: acorn-finance-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Acorn Finance Domain Security
  slug: acorn-finance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: acorn-finance
tags:
- Company
- Financial Services
- Lending
- Loans
- Home Improvement
- Embedded Finance
- Point of Sale
- Consumer Finance
- Fintech
- Webhooks
website: https://www.acornfinance.com/
---
