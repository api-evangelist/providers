---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Euronet Agentic Access
  operation_count: 65
  slug: euronet-agentic-access
  summary_line: 65 operations · 27 acting
api_count: 6
apis:
- description: Xe (a Euronet Money Transfer brand) Currency Data API — a REST JSON API serving real-time and historical exchange rates for 170+ currencies from 100+ global sources. Documented Swagger 2.0 with HTTP B
  name: Xe Currency Data API
  slug: xe-currency-data-api
- description: Xe Payments API — cross-border payment execution for Xe's international money-transfer platform. Documented Swagger 2.0 covering quotes, recipients, tradeable currencies, purposes of payment, transact
  name: Xe Payments API
  slug: xe-payments-api
- description: Xe Mass Payments API — batch/bulk cross-border payouts for Xe's platform. Documented Swagger 2.0 covering account, quote, invoice, payments, transaction, terms, and permissions resources for high-volu
  name: Xe Mass Payments API
  slug: xe-mass-payments-api
- description: 'Xe Currency Data Tradable Rates API — tradable (dealable) FX rates companion to the Currency Data API. Documented Swagger 2.0 exposing a tradable-rates endpoint; the published definition ships with a '
  name: Xe Currency Data Tradable Rates API
  slug: xe-currency-data-tradable-rates-api
- description: Xe XETA API — a Swagger 2.0 definition published by XE.com on SwaggerHub covering 16 operations. The spec declares host xeta-api.xe.com/v1 (not publicly reachable at review time) and a Drupal-based au
  name: XETA API
  slug: xeta-api
- description: Dandelion by Euronet — a real-time, ISO 20022-compliant cross-border payments network exposed through a single customizable API reaching 190+ countries, ~6 billion bank accounts and mobile wallets, an
  name: Dandelion Cross-Border Payments API
  slug: dandelion-cross-border-payments-api
artifact_total: 11
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/euronet-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/euronet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/euronet-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/euronet-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/euronet-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/euronet-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/euronet-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/euronet-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/euronet-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.xe.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/euronet-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/euronet-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/euronet-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/euronet-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/euronet-xe-currency-data-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/euronet-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: APIReference
  url: https://app.swaggerhub.com/apis/XE.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.xe.com/xecurrencydata/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.xe.com/legal/
- group: company
  title: ''
  type: Blog
  url: https://www.xe.com/blog/
- group: company
  title: ''
  type: Website
  url: https://www.euronet.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://public.dandelionpayments.com/
- group: docs
  title: ''
  type: Documentation
  url: https://xecdapi.xe.com/docs/v1/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.dandelionpayments.com/hc/en-gb
- group: start
  title: ''
  type: SignUp
  url: https://xecd.xe.com/account/signup.php?freetrial
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.euronet.com/legal-privacy-statement/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/euronet-worldwide
created: '2026-07-24'
description: 'Euronet Worldwide (NASDAQ: EEFT) is a US-based (Leawood, Kansas) global payments and financial technology company operating across three segments: Payments Infrastructure (EFT/ATM networks, transaction processing, merchant acquiring, and the REN payments software from Euronet Software Solutions); epay (prepaid and digital-media distribution across 60+ countries); and Money Transfer, home to its Ria, Xe, and Dandelion brands. The company processes roughly 20 billion transactions a year across 200 countries and territories. Its most API-native surface sits in the Money Transfer segment: the Xe brand publishes several developer APIs on SwaggerHub (Currency Data, Payments, Mass Payments, Tradable Rates, and XETA), and Dandelion operates a real-time, ISO 20022-compliant cross-border payments developer portal. As a US company in a market with no single payments mandate, Euronet exposes a fragmented but genuine set of self-serve (Xe Currency Data free trial) and partner-onboarded
  (Payments, Dandelion) developer surfaces rather than one unified platform API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: euronet-mcp.yml
  slug: euronet-mcpyml
modified: '2026-07-24'
name: Euronet Worldwide
nav: Providers
network: true
overview: 'Euronet Worldwide publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Xe Currency Data API, Xe Payments API, Xe Mass Payments API, and 2 more. Tagged areas include Payments, United States, Payment Processing, Cross-Border, and Money Transfer.


  Euronet Worldwide''s developer surface includes authentication, API reference, pricing, engineering blog, documentation, signup flow, and 22 more developer resources.'
random_paper: 41
rate_limits:
- limit_count: 0
  name: Euronet Rate Limits
  slug: euronet-rate-limits
score:
  band: thin
  composite: 38.2
  delta: -5.4
  facets:
    commercial_clarity: 44.7
    contract_quality: 32.3
    developer_ergonomics: 51.6
    discoverability: 72.2
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 43.6
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/euronet/refs/heads/main/screenshots/euronet-2026-07-25T213700.png
security:
- kind: authentication
  name: Euronet Authentication
  slug: euronet-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Euronet Domain Security
  slug: euronet-domain-security
  summary_line: TLSv1.3 · DMARC
slug: euronet
tags:
- Payments
- United States
- Payment Processing
- Cross-Border
- Money Transfer
- Currency Exchange
- FX
- Payouts
- Real-Time Payments
- ISO 20022
- Acquiring
website: https://www.euronet.com/
---
