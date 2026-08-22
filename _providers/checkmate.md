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
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.2
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: The Health API from Checkmate — 1 operation(s) for health.
  name: Checkmate Health API
  slug: checkmate-health-api
- description: The Merchants API from Checkmate — 2 operation(s) for merchants.
  name: Checkmate Merchants API
  slug: checkmate-merchants-api
- description: The Shoppers API from Checkmate — 1 operation(s) for shoppers.
  name: Checkmate Shoppers API
  slug: checkmate-shoppers-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenStock Health API
  slug: open-checkmate-health-api
- collection_type: open
  name: OpenStock Health Merchants API
  slug: open-checkmate-merchants-api
- collection_type: open
  name: OpenStock Health Shoppers API
  slug: open-checkmate-shoppers-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/checkmate-openstock-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://joincheckmate.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://openstock.sh
- group: docs
  title: ''
  type: Documentation
  url: https://api.openstock.sh/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.openstock.sh/docs
- group: company
  title: ''
  type: Blog
  url: https://joincheckmate.com/blog
- group: operate
  title: ''
  type: Support
  url: mailto:support@joincheckmate.com
- group: start
  title: ''
  type: SignUp
  url: https://joincheckmate.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://joincheckmate.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://joincheckmate.com/terms-conditions
- group: auth
  title: ''
  type: Security
  url: https://joincheckmate.com/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/checkmate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/checkmate-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/checkmate-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/checkmate-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/checkmate-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/checkmate-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/checkmate-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/checkmate-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/checkmate-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/checkmate-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/checkmate-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/checkmate-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/checkmate-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Checkmate is a shopping intelligence and data company whose network powers three products: Checkmate for consumers (a browser extension and mobile app that automatically finds the best price and applies working discount codes across 284,000+ merchants for 5M+ monthly shoppers), Mate for brands (AI-powered revenue intelligence), and OpenStock for publishers and agents. OpenStock is a commerce API and Model Context Protocol (MCP) server that exposes the entire Checkmate network through a single endpoint — letting AI agents, shopping copilots, and applications discover merchants, pull live catalogues and offers, generate real merchant-backed discount codes, check availability, and attribute orders. Backed by GV (Google Ventures).'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/checkmate.png
layout: provider
mcp_servers:
- description: ''
  name: checkmate-mcp.yml
  slug: checkmate-mcpyml
modified: '2026-07-18'
name: Checkmate
nav: Providers
network: true
overview: 'Checkmate publishes 3 APIs on the [APIs.io](https://apis.io/) network: Health API, Merchants API, and Shoppers API. Tagged areas include Company, Consumer, Commerce, Ecommerce, and Shopping.


  Checkmate''s developer surface includes documentation, API reference, engineering blog, support, signup flow, authentication, and 19 more developer resources.'
random_paper: 9
score:
  band: developing
  composite: 43.8
  delta: 0.7
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 50.1
    developer_ergonomics: 47.0
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 43.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/checkmate/refs/heads/main/screenshots/checkmate-2026-07-25T205130.png
security:
- kind: authentication
  name: Checkmate Authentication
  slug: checkmate-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Checkmate Domain Security
  slug: checkmate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Checkmate Vulnerability Disclosure
  slug: checkmate-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: checkmate
tags:
- Company
- Consumer
- Commerce
- Ecommerce
- Shopping
- Discount Codes
- Coupons
- Merchants
- MCP
- Agentic Commerce
- Retail
- API
website: https://joincheckmate.com
---
