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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The Activity Log API from Fund That Flip — 2 operation(s) for activity log.
  name: Fund That Flip Activity Log API
  slug: fund-that-flip-activity-log-api
- description: The Attachment Upload API from Fund That Flip — 1 operation(s) for attachment upload.
  name: Fund That Flip Attachment Upload API
  slug: fund-that-flip-attachment-upload-api
- description: The Company API from Fund That Flip — 4 operation(s) for company.
  name: Fund That Flip Company API
  slug: fund-that-flip-company-api
- description: 'The Company: Categories API from Fund That Flip — 3 operation(s) for company: categories.'
  name: 'Fund That Flip Company: Categories API'
  slug: fund-that-flip-company-categories-api
- description: The Expense Accounts API from Fund That Flip — 3 operation(s) for expense accounts.
  name: Fund That Flip Expense Accounts API
  slug: fund-that-flip-expense-accounts-api
- description: The Project API from Fund That Flip — 3 operation(s) for project.
  name: Fund That Flip Project API
  slug: fund-that-flip-project-api
- description: 'The Project Expenses: Categories API from Fund That Flip — 1 operation(s) for project expenses: categories.'
  name: 'Fund That Flip Project Expenses: Categories API'
  slug: fund-that-flip-project-expenses-categories-api
- description: 'The Project Expenses: Line Items API from Fund That Flip — 2 operation(s) for project expenses: line items.'
  name: 'Fund That Flip Project Expenses: Line Items API'
  slug: fund-that-flip-project-expenses-line-items-api
- description: 'The Project Expenses: Transactions API from Fund That Flip — 3 operation(s) for project expenses: transactions.'
  name: 'Fund That Flip Project Expenses: Transactions API'
  slug: fund-that-flip-project-expenses-transactions-api
- description: The Project Income API from Fund That Flip — 3 operation(s) for project income.
  name: Fund That Flip Project Income API
  slug: fund-that-flip-project-income-api
- description: 'The Project Photo Log: Photos API from Fund That Flip — 3 operation(s) for project photo log: photos.'
  name: 'Fund That Flip Project Photo Log: Photos API'
  slug: fund-that-flip-project-photo-log-photos-api
- description: The Project Receipts API from Fund That Flip — 3 operation(s) for project receipts.
  name: Fund That Flip Project Receipts API
  slug: fund-that-flip-project-receipts-api
- description: The Project Updates API from Fund That Flip — 3 operation(s) for project updates.
  name: Fund That Flip Project Updates API
  slug: fund-that-flip-project-updates-api
- description: 'The Project Updates: Photos API from Fund That Flip — 2 operation(s) for project updates: photos.'
  name: 'Fund That Flip Project Updates: Photos API'
  slug: fund-that-flip-project-updates-photos-api
- description: The User API from Fund That Flip — 1 operation(s) for user.
  name: Fund That Flip User API
  slug: fund-that-flip-user-api
artifact_total: 19
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/fund-that-flip-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/fund-that-flip-flipperforce-public-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fund-that-flip-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fund-that-flip-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.upright.us/
- group: start
  title: ''
  type: Portal
  url: https://www.flipperforce.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.flipperforce.com/en/
- group: docs
  title: ''
  type: APIReference
  url: https://tools.flipperforce.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.flipperforce.com/house-flipping-blog/new-public-api
- group: operate
  title: ''
  type: Support
  url: https://help.flipperforce.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.upright.us/en
- group: company
  title: ''
  type: Blog
  url: https://learn.upright.us/real-estate-investing-blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FundThatFlip
- group: commercial
  title: ''
  type: Pricing
  url: https://flipperforce.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://tools.flipperforce.com/register
- group: start
  title: ''
  type: Login
  url: https://tools.flipperforce.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flipperforce.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.upright.us/legal
- group: build
  title: ''
  type: Packages
  url: packages/fund-that-flip-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fund-that-flip-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/fund-that-flip-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fund-that-flip-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fund-that-flip-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fund-that-flip-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fund-that-flip-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fund-that-flip-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/fund-that-flip-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fund-that-flip-rate-limits.yml
created: '2026-08-16'
description: Fund That Flip is a Cleveland- and New York-based real estate fintech founded in 2014 that lends to residential redevelopers and offers passive income opportunities to accredited investors, having originated more than $2.6B in short-term hard money, fix-and-flip, new construction and DSCR loans. In 2022 it acquired FlipperForce, a web-based project management, deal analysis, rehab estimating and job-costing platform for house flippers and builders, and in September 2023 the combined lending and software business rebranded as Upright (upright.us). The company's developer surface is the FlipperForce Public API — an OpenAPI 3.1 documented REST API at tools.flipperforce.com/api/v1 covering projects, expenses, income, receipts, photo logs, project updates, companies, expense accounts and the workspace activity log.
image: https://cdn.prod.website-files.com/64b99dfa2be98253c176ca3b/64fa2106537c70e46a8afb34_apple-touch-icon.png
layout: provider
modified: '2026-08-16'
name: Fund That Flip
nav: Providers
network: true
overview: 'Fund That Flip publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Activity Log API, Attachment Upload API, Company API, and 12 more. Tagged areas include Company, Real-Estate, Lending, Construction, and Project Management.


  Fund That Flip''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, support, engineering blog, and 22 more developer resources.'
plans:
- name: Fund That Flip Plans Pricing
  plan_count: 7
  slug: fund-that-flip-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Fund That Flip Rate Limits
  slug: fund-that-flip-rate-limits
score:
  band: developing
  composite: 51.4
  coverage:
    artifact_dirs: 20
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 55.3
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 51.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fund-that-flip/refs/heads/main/screenshots/fund-that-flip-2026-08-17T080937.png
security:
- kind: authentication
  name: Fund That Flip Authentication
  slug: fund-that-flip-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fund That Flip Domain Security
  slug: fund-that-flip-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fund-that-flip
tags:
- Company
- Real-Estate
- Lending
- Construction
- Project Management
- Financial-Services
- Investing
- Fintech
- Property Technology
- Accounting
website: https://www.upright.us/
---
