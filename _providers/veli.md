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
  trial: false
  try_now: true
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Veli Agentic Access
  operation_count: 9
  slug: veli-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 5
apis:
- description: Buy/sell order execution signals
  name: Veli Orders API
  slug: veli-orders-api
- description: Portfolio performance and returns
  name: Veli Performance API
  slug: veli-performance-api
- description: User portfolio creation and management
  name: Veli Portfolios API
  slug: veli-portfolios-api
- description: Portfolio holdings and allocations
  name: Veli Positions API
  slug: veli-positions-api
- description: Investment strategy catalog and configuration
  name: Veli Strategies API
  slug: veli-strategies-api
artifact_total: 53
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Veli Orders API
  slug: open-veli-orders-api
- collection_type: open
  name: Veli Orders Performance API
  slug: open-veli-performance-api
- collection_type: open
  name: Veli Orders Portfolios API
  slug: open-veli-portfolios-api
- collection_type: open
  name: Veli Orders Positions API
  slug: open-veli-positions-api
- collection_type: open
  name: Veli Orders Strategies API
  slug: open-veli-strategies-api
- collection_type: open
  name: Veli API
  slug: open-veli
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/veli-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/veli-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/veli-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://veli.io/
- group: start
  title: ''
  type: Portal
  url: https://veli.io/
- group: docs
  title: ''
  type: Documentation
  url: https://veli.io/
- group: design
  title: Veli API Spectral Rules
  type: SpectralRules
  url: rules/veli-spectral-rules.yml
- group: design
  title: Veli Vocabulary
  type: Vocabulary
  url: vocabulary/veli-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://veli.io/feed/
created: '2026-03-16'
description: Veli provides crypto investment strategies via API, enabling platforms to offer smart investment solutions while handling running investment strategies, buying, selling, rebalancing, and fee collection behind the scenes. Partners retain custody and execution while Veli manages the strategy logic.
examples:
- key_count: 3
  name: Veli Asset Allocation Example
  slug: veli-asset-allocation-example
- key_count: 4
  name: Veli Create Portfolio Request Example
  slug: veli-create-portfolio-request-example
- key_count: 4
  name: Veli Order Example
  slug: veli-order-example
- key_count: 7
  name: Veli Performance Response Example
  slug: veli-performance-response-example
- key_count: 8
  name: Veli Portfolio Example
  slug: veli-portfolio-example
- key_count: 7
  name: Veli Position Example
  slug: veli-position-example
- key_count: 10
  name: Veli Strategy Example
  slug: veli-strategy-example
features:
- description: Deploy pre-built or custom crypto investment strategies including index tracking, theme portfolios, and algorithmic rebalancing.
  name: Automated Investment Strategies
- description: Automatic portfolio rebalancing to maintain target allocations as market prices shift, with configurable rebalancing thresholds.
  name: Portfolio Rebalancing
- description: Partners retain full custody and execution of assets while Veli provides the strategy logic, signals, and portfolio management.
  name: Partner Custody
- description: Built-in fee management for partner platforms to charge management fees on invested assets with automated collection workflows.
  name: Fee Collection
- description: Portfolio performance metrics, returns, allocation breakdowns, and transaction history for investor reporting and dashboards.
  name: Performance Reporting
finops:
- name: Veli Finops
  service_category: API
  slug: veli-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/veli.png
integrations:
- description: Integrate with major crypto exchanges for execution of buy/sell orders triggered by Veli strategy signals.
  name: Crypto Exchanges
- description: Connect portfolio data to tracking apps and dashboards via Veli performance and allocation APIs.
  name: Portfolio Trackers
- description: Integrate identity verification and compliance checks with Veli user management for regulated investment products.
  name: KYC/AML Providers
json_schemas:
- name: AssetAllocation
  property_count: 3
  slug: veli-asset-allocation
- name: CreatePortfolioRequest
  property_count: 4
  slug: veli-create-portfolio-request
- name: Order
  property_count: 4
  slug: veli-order
- name: PerformanceResponse
  property_count: 7
  slug: veli-performance-response
- name: Portfolio
  property_count: 8
  slug: veli-portfolio
- name: Position
  property_count: 7
  slug: veli-position
- name: Strategy
  property_count: 10
  slug: veli-strategy
json_structures:
- name: Veli Asset Allocation Structure
  property_count: 3
  slug: veli-asset-allocation-structure
- name: Veli Create Portfolio Request Structure
  property_count: 4
  slug: veli-create-portfolio-request-structure
- name: Veli Order Structure
  property_count: 4
  slug: veli-order-structure
- name: Veli Performance Response Structure
  property_count: 7
  slug: veli-performance-response-structure
- name: Veli Portfolio Structure
  property_count: 8
  slug: veli-portfolio-structure
- name: Veli Position Structure
  property_count: 7
  slug: veli-position-structure
- name: Veli Strategy Structure
  property_count: 10
  slug: veli-strategy-structure
layout: provider
modified: '2026-05-19'
name: Veli
nav: Providers
network: true
overview: 'Veli publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Orders API, Performance API, Portfolios API, and 2 more. Tagged areas include Crypto, DeFi, Finance, Investment, and Portfolio-Management.


  The Veli catalog on APIs.io includes 2 Spectral governance rulesets.


  Veli''s developer surface includes authentication, developer portal, documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Veli Plans Pricing
  plan_count: 3
  slug: veli-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Veli Rate Limits
  slug: veli-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Veli API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: veli-jsonschema-spectral-rules
- effective_rule_count: 77
  extends:
  - spectral:oas
  name: Veli API Rules
  rule_count: 36
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 22
  slug: veli-spectral-rules
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 15
    catalog_gap: 51.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 23.7
    developer_ergonomics: 33.3
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 26.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/veli/refs/heads/main/screenshots/veli-2026-06-20T200905.png
security:
- kind: authentication
  name: Veli Authentication
  slug: veli-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Veli Domain Security
  slug: veli-domain-security
  summary_line: TLSv1.2 · DMARC
slug: veli
tags:
- Crypto
- DeFi
- Finance
- Investment
- Portfolio-Management
use_cases:
- description: Exchanges integrate Veli to offer automated investment portfolios (crypto index funds, theme portfolios) to their retail user base.
  name: Crypto Exchange Investment Products
- description: Neobanks and fintech apps add crypto investment strategy features powered by Veli while maintaining regulatory compliance and custody.
  name: Neobank Wealth Features
- description: Build automated crypto wealth management products with goal-based portfolio construction, risk profiling, and rebalancing automation.
  name: Robo-Advisor for Crypto
- description: Launch branded crypto investment products using Veli's strategy engine without building portfolio management infrastructure.
  name: White-Label Investment Platform
website: https://veli.io/
---
