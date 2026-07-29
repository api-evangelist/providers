---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Even Financial Agentic Access
  operation_count: 22
  slug: even-financial-agentic-access
  summary_line: 22 operations · 5 acting
api_count: 6
apis:
- description: '### Introduction Welcome to Engine by MoneyLion''s Integration Guide for our Supply Analytics data product, which provides funnel, payout and client tag data on specific leads and lead segments to bett'
  name: Even Financial Analytics API
  slug: even-financial-analytics-api
- description: Approval probability reports contains data about the likelihood that a user with specified attributes will be approved for particular product offers. The user attributes are passed in the request's `P
  name: Even Financial Approval Probability API
  slug: even-financial-approval-probability-api
- description: A lead combines information about a user with search criteria for financial products, and is submitted in exchange for a rate table. A rate table is a list of financial offers that match a submitted l
  name: Even Financial Lead API
  slug: even-financial-lead-api
- description: 'Preview offers are matched based upon a simple set of anonymous criteria and as a result are not personalized. This is useful if you''d like to display offers without requesting personalized data. For '
  name: Even Financial Offer Preview API
  slug: even-financial-offer-preview-api
- description: The Prefill API from Even Financial — 2 operation(s) for prefill.
  name: Even Financial Prefill API
  slug: even-financial-prefill-api
- description: A collection of endpoints that can be used to improve a search experience.
  name: Even Financial UI Utils API
  slug: even-financial-ui-utils-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Submit a consumer lead to Engine by MoneyLion and read back the resulting rate table of offers.
  name: Submit a lead and retrieve its rate table
  slug: even-financial-submit-lead-rate-table
artifact_total: 13
asyncapis:
- description: ''
  name: Even Financial Webhooks
  slug: even-financial-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://even-financial.gitbook.io/developer-center
- group: docs
  title: ''
  type: Documentation
  url: https://engine.tech/docs
- group: docs
  title: ''
  type: APIReference
  url: https://engine.tech/docs/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://even-financial.gitbook.io/developer-center/native-api-integrations/credit-cards-marketplace/getting-started
- group: company
  title: ''
  type: Blog
  url: https://engine.tech/blog
- group: operate
  title: ''
  type: Support
  url: https://engine.tech/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EVENFinancial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://engine.tech/about/legal#terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://engine.tech/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.engine.tech
- group: auth
  title: ''
  type: Authentication
  url: authentication/even-financial-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/even-financial-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/even-financial-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/even-financial-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/even-financial-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/even-financial-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/even-financial-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/even-financial-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/even-financial-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/even-financial-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/even-financial-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/even-financial-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/even-financial-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/even-financial-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/even-financial-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/even-financial-submit-lead-rate-table.yml
created: '2026-07-17'
description: Engine by MoneyLion (formerly Even Financial) operates an embedded-finance search, comparison and recommendation engine for financial services. Its API matches consumers to personalized financial products — personal loans, credit cards, savings and deposit accounts, auto refinancing, HELOC and insurance — by submitting a lead (a user plus product search criteria) in exchange for a rate table of offers. The platform pairs the native API with embeddable marketplaces, calculators, widgets and mobile SDKs, plus approval-probability reports and channel-partner analytics. Even Financial was founded in 2015, backed by Canaan Partners, and rebranded to Engine by MoneyLion in 2023 following MoneyLion's acquisition.
image: https://cdn.prod.website-files.com/65c76d4633ca994639a589c7/65e2220541631373794b6e17_opengraph.png
layout: provider
mcp_servers:
- description: ''
  name: even-financial-mcp.yml
  slug: even-financial-mcpyml
modified: '2026-07-19'
name: Even Financial
nav: Providers
network: true
overview: 'Even Financial publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Approval Probability API, Lead API, and 3 more. Tagged areas include Company, Financial Services, Embedded Finance, Fintech, and Lending.


  The Even Financial catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Even Financial''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, changelog, and 20 more developer resources.'
random_paper: 31
score:
  band: developing
  composite: 50.9
  delta: -1.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 70.9
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 52.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/even-financial/refs/heads/main/screenshots/even-financial-2026-07-25T213723.png
security:
- kind: authentication
  name: Even Financial Authentication
  slug: even-financial-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Even Financial Domain Security
  slug: even-financial-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: even-financial
tags:
- Company
- Financial Services
- Embedded Finance
- Fintech
- Lending
- Personal Loans
- Credit Cards
- Marketplace
- Recommendation Engine
- Lead Generation
website: https://even-financial.gitbook.io/developer-center
---
