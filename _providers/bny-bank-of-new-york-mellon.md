---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bny Bank Of New York Mellon Agentic Access
  operation_count: 4
  slug: bny-bank-of-new-york-mellon-agentic-access
  summary_line: 4 operations
api_count: 4
apis:
- description: 'BNY Data On-Chain publishes BNY-attested data on-chain so on-chain consumers can read it directly from smart contracts. The product ships a Solidity consumer interface (IBNYDataConsumerV2) with typed '
  name: BNY Data On-Chain
  slug: data-on-chain
- description: Custody, fund accounting, middle-office, and transfer agency operations.
  name: BNY (Bank of New York Mellon) Asset Servicing API
  slug: bny-bank-of-new-york-mellon-asset-servicing-api
- description: FX, securities finance, fixed income, and equities surface.
  name: BNY (Bank of New York Mellon) Markets API
  slug: bny-bank-of-new-york-mellon-markets-api
- description: Pershing clearing, custody, NetX360+, and Wove platform surface.
  name: BNY (Bank of New York Mellon) Pershing API
  slug: bny-bank-of-new-york-mellon-pershing-api
- description: Payments, liquidity, cash management, trade finance, and FX.
  name: BNY (Bank of New York Mellon) Treasury Services API
  slug: bny-bank-of-new-york-mellon-treasury-services-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BNY Asset Servicing API
  slug: open-bny-asset-servicing-api
- collection_type: open
  name: BNY Asset Servicing API
  slug: open-bny-bank-of-new-york-mellon-asset-servicing-api
- collection_type: open
  name: BNY Asset Servicing Markets API
  slug: open-bny-bank-of-new-york-mellon-markets-api
- collection_type: open
  name: BNY Asset Servicing Pershing API
  slug: open-bny-bank-of-new-york-mellon-pershing-api
- collection_type: open
  name: BNY Asset Servicing Treasury Services API
  slug: open-bny-bank-of-new-york-mellon-treasury-services-api
- collection_type: open
  name: BNY Markets API
  slug: open-bny-markets-api
- collection_type: open
  name: BNY Pershing API
  slug: open-bny-pershing-api
- collection_type: open
  name: BNY Treasury Services API
  slug: open-bny-treasury-services-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/bnymellon/bny-data-on-chain/issues
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/BNYMellon/bny-data-on-chain/blob/main/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bny-bank-of-new-york-mellon-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bny-bank-of-new-york-mellon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bny-bank-of-new-york-mellon-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.bny.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bny.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bnymellon
- group: company
  title: ''
  type: About
  url: https://www.bny.com/corporate/global/en/about-us.html
- group: company
  title: ''
  type: Newsroom
  url: https://www.bny.com/corporate/global/en/newsroom.html
- group: other
  title: ''
  type: Insights
  url: https://www.bny.com/corporate/global/en/insights/all-insights.html
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.bny.com/investor-relations.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-bank-of-new-york-mellon-corporation
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/BNY
- group: commercial
  title: ''
  type: Plans
  url: plans/bny-bank-of-new-york-mellon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bny-bank-of-new-york-mellon-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bny-bank-of-new-york-mellon-finops.yml
created: '2026-05-23'
description: BNY (rebranded from BNY Mellon in 2024, NYSE ticker changed from BK to BNY in May 2026) is the world's largest custodian bank, overseeing approximately $59.4 trillion in assets under custody and/or administration and $2.1 trillion in assets under management as of Q1 2026. BNY operates across Securities Services, Market & Wealth Services, and Investment & Wealth Management, with brand families including Pershing (clearing and custody for wealth managers, parent of NetX360+ and the Wove platform), Eagle Investment Systems (investment data management), Albridge (wealth data aggregation), BNY Markets (FX, securities finance, capital markets), and BNY Investments. BNY publishes APIs through the BNY Developer Marketplace at developer.bny.com (formerly marketplace.bnymellon.com), covering Asset Servicing, Treasury Services, Payments, Pershing, Markets, and the BNY Data On-Chain product, with registration and API reference gated behind a Nexen single sign-on.
finops:
- name: Bny Bank Of New York Mellon Finops
  service_category: Banking / Asset Servicing / Payments
  slug: bny-bank-of-new-york-mellon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bny-bank-of-new-york-mellon.png
layout: provider
modified: '2026-05-23'
name: BNY (Bank of New York Mellon)
nav: Providers
network: true
overview: 'BNY (Bank of New York Mellon) publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Asset Servicing API, Markets API, Pershing API, and 1 more. Tagged areas include Banking, Custody, Asset Servicing, Treasury Services, and Payments.


  BNY (Bank of New York Mellon)''s developer surface includes authentication and 16 more developer resources.'
plans:
- name: Bny Bank Of New York Mellon Plans Pricing
  plan_count: 1
  slug: bny-bank-of-new-york-mellon-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Bny Bank Of New York Mellon Rate Limits
  slug: bny-bank-of-new-york-mellon-rate-limits
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 9
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -1.4
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 57.1
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  open_source:
    applies: true
    score: 25.0
  previous_composite: 37.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bny-bank-of-new-york-mellon/refs/heads/main/screenshots/bny-bank-of-new-york-mellon-2026-06-20T173546.png
security:
- kind: authentication
  name: Bny Bank Of New York Mellon Authentication
  slug: bny-bank-of-new-york-mellon-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bny Bank Of New York Mellon Domain Security
  slug: bny-bank-of-new-york-mellon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bny-bank-of-new-york-mellon
tags:
- Banking
- Custody
- Asset Servicing
- Treasury Services
- Payments
- Wealth Management
- Clearing
- Capital Markets
- Digital Assets
- Financial-Services
website: https://www.bny.com
---
