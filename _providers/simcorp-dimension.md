---
access_model:
  confidence: high
  label: Enterprise · Credentials issued by SimCorp
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans
  - probe
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
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: Web API providing HTTP-based interfaces for accessing and manipulating SimCorp Dimension data in real time, supporting stateless RESTful operations across the investment management lifecycle. Named by
  name: SimCorp Dimension Web API
  slug: simcorp-dimension-web-api
- description: API for distributing and sharing investment data across integrated systems, supporting event streaming channels and direct data access from SimCorp Dimension. Named by SimCorp on the Data Model Portal
  name: SimCorp Dimension Data Distribution API
  slug: simcorp-dimension-data-distribution-api
- description: Real-time streaming API for delivering live investment data, market updates and event-driven notifications from SimCorp Dimension. Named by SimCorp on the Data Model Portal home page. No AsyncAPI or e
  name: SimCorp Dimension Streaming API
  slug: simcorp-dimension-streaming-api
artifact_total: 26
common:
- group: company
  title: ''
  type: Website
  url: https://www.simcorp.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simcorp-dimension-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/simcorp-dimension-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/simcorp-dimension-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/simcorp-dimension-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/simcorp-dimension-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/simcorp-dimension-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/simcorp-dimension-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SimCorp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/simcorp-dimension
- group: start
  title: ''
  type: Portal
  url: https://thesim.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://thesim.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://thesim.dev/gettingstarted/
- group: company
  title: ''
  type: Blog
  url: https://www.simcorp.com/insights
- group: operate
  title: ''
  type: Support
  url: https://www.simcorp.com/about-us/contact
- group: operate
  title: ''
  type: Community
  url: https://www.dimensionalcommunity.com/insights
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.simcorp.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.simcorp.com/legal/privacy-policy
- group: other
  title: ''
  type: Portfolio Management
  url: https://www.simcorp.com/solutions/simcorp-one/portfolio-management
- group: auth
  title: ''
  type: Trading and Compliance
  url: https://www.simcorp.com/solutions/simcorp-one/trading-and-compliance
- group: other
  title: ''
  type: Risk and Performance
  url: https://www.simcorp.com/solutions/simcorp-one/risk-and-performance
- group: other
  title: ''
  type: Operations
  url: https://www.simcorp.com/solutions/simcorp-one/operations
- group: other
  title: ''
  type: Accounting
  url: https://www.simcorp.com/solutions/simcorp-one/accounting
- group: other
  title: ''
  type: Data Management
  url: https://www.simcorp.com/solutions/simcorp-one/data-management
- group: other
  title: ''
  type: Reporting
  url: https://www.simcorp.com/solutions/simcorp-one/reporting
- group: build
  title: ''
  type: Client Communications
  url: https://www.simcorp.com/solutions/simcorp-one/Client-Communications-and-Regulatory-Reporting
- group: company
  title: ''
  type: Partners
  url: https://www.simcorp.com/partners/open-platform-partners
- group: other
  title: ''
  type: Resources
  url: https://en.wikipedia.org/wiki/SimCorp
- group: other
  title: ''
  type: Resources
  url: https://www.simcorp.com/about-us/news/2024/simcorp-introduces-new-flagship-platform-simcorp-one
- group: design
  title: ''
  type: JSONLD
  url: json-ld/simcorp-dimension-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/simcorp-dimension-portfolio-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/simcorp-dimension-instrument-schema.json
coverage:
  checked: '2026-08-29'
  detail: SimCorp's own Data Model Portal at thesim.dev carries the Web API, Data Distribution API and Streaming API reference plus the Swagger documentation, and /gettingstarted/ resolves to a sign-in wall offering corporate SSO for SimCorp employees and a SimCorp-issued username and password for clients, vendors and partners — there is no registration path at all, so the contract is unreadable without an existing SimCorp relationship.
  evidence:
  - status: 200
    url: https://thesim.dev/gettingstarted/
  - status: 404
    url: https://thesim.dev/openapi.json
  - status: 0
    url: https://developer.simcorp.com/dimension/data-api
  - status: 0
    url: https://api.simcorp.com/dimension/v1/openapi.json
  reason: customer-only-docs
  state: gated
created: '2024-01-01'
description: 'SimCorp Dimension is the investment management system at the core of SimCorp One, the front-to-back platform SimCorp A/S (Copenhagen; part of Deutsche Boerse Group) sells to asset managers, insurers, pension funds, sovereign wealth funds and central banks. Its integration surface is the SimCorp Integration Model (SIM), which SimCorp presents as three API families — Web APIs for synchronous HTTP access, Data Distribution APIs for bulk and channel-based data sharing, and Streaming APIs for real-time, event-driven delivery — spanning portfolio management, trading and compliance, risk and performance, accounting, operations, data management and regulatory reporting. The reference documentation, Swagger documentation, example code and standardized Message Format Models are published on the SimCorp Data Model Portal at thesim.dev, which is credential-gated: SimCorp employees sign in with corporate SSO, and clients, vendors and partners sign in with a portal account SimCorp issues.
  No OpenAPI, AsyncAPI, GraphQL SDL or WSDL is reachable anonymously, and there is no self-service sign-up, trial or published pricing — API access follows from a SimCorp One licence.'
features:
- Front-to-back investment management
- Real-time portfolio data and analytics
- Event-driven streaming data distribution
- Risk and performance measurement
- Accounting and operations management
- Trading and compliance monitoring
- Client communications and regulatory reporting
- Open platform integration model
finops:
- name: Simcorp Dimension Finops
  service_category: API
  slug: simcorp-dimension-finops
image: https://avatars.githubusercontent.com/u/62388281?v=4
json_schemas:
- name: SimCorp Dimension Instrument
  property_count: 23
  slug: simcorp-dimension-instrument
- name: SimCorp Dimension Portfolio
  property_count: 24
  slug: simcorp-dimension-portfolio
jsonld:
- class_count: 0
  name: Simcorp Dimension Context
  property_count: 8
  slug: simcorp-dimension-context
layout: provider
modified: '2026-08-29'
name: SimCorp Dimension
nav: Providers
network: true
overview: 'SimCorp Dimension publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Accounting, Asset Management, Compliance, Data Distribution, and Enterprise Software.


  The SimCorp Dimension catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SimCorp Dimension''s developer surface includes developer portal, documentation, getting-started guide, engineering blog, support, and 27 more developer resources.'
plans:
- name: Simcorp Dimension Plans Pricing
  plan_count: 0
  slug: simcorp-dimension-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Simcorp Dimension Rate Limits
  slug: simcorp-dimension-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SimCorp Dimension API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: simcorp-dimension-jsonschema-spectral-rules
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 15
    catalog_gap: 68.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 28.0
    contract_quality: 6.7
    developer_ergonomics: 38.1
    discoverability: 79.6
    governance: 28.0
    operational_transparency: 2.6
  previous_composite: 32.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 50.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/simcorp-dimension/refs/heads/main/screenshots/simcorp-dimension-2026-06-20T193926.png
security:
- kind: domain-security
  name: Simcorp Dimension Domain Security
  slug: simcorp-dimension-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Simcorp Dimension Trust Center
  slug: simcorp-dimension-trust-center
  summary_line: SOC 2 Type 2
slug: simcorp-dimension
tags:
- Accounting
- Asset Management
- Compliance
- Data Distribution
- Enterprise Software
- Financial Data
- Financial Technology
- Investment Management
- Portfolio-Management
- Risk Management
- SimCorp One
- Streaming
- Trading
use_cases:
- Portfolio management and analysis
- Investment data integration and distribution
- Risk and performance reporting
- Regulatory compliance and reporting
- Real-time market data streaming
- Multi-asset investment operations
website: https://www.simcorp.com/
---
