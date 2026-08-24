---
access_model:
  confidence: high
  label: Enterprise · Approval required
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - https://www.sensestreet.com/contact
  - https://docs.sensestreet.com/implementation-data-requirements
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: The enterprise REST API. Callers upload files of broker conversations for asynchronous processing and retrieve the extracted RFQs once parsing completes, or call the prediction operations synchronousl
  name: Sense Street Batch API
  slug: sense-street-batch-api
- description: Real-time streaming access to quotes and market activity extracted from broker conversations across multiple commodities. Customers subscribe to feeds such as oil, carbon, EMEA gas and US gas to recei
  name: Sense Street WebSocket API
  slug: sense-street-websocket-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://sensestreet.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sensestreet.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sensestreet.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sensestreet.com/batch-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sensestreet.com/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sensestreet
- group: operate
  title: ''
  type: Support
  url: https://sensestreet.com/contact
- group: company
  title: ''
  type: Blog
  url: https://sensestreet.com/resources
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sensestreet.com/security-compliance/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://sensestreet.com/security-compliance/certifications
- group: auth
  title: ''
  type: TrustCenter
  url: security/sense-street-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sense-street-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sense-street-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/sense-street-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sense-street-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sense-street-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sense-street-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sense-street-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sense-street-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sense-street-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sense-street-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sense-street-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sense-street-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sense-street-llms.txt
created: '2026-07-17'
description: 'Sense Street provides production-grade AI workflow automation for capital markets, structuring unstructured OTC trading conversations in real time. Its platform connects to trading communication channels such as Bloomberg, Symphony, ICE and Eikon and extracts RFQs, orders, quotes and market sentiment from broker chat, delivering them to the desk through an AI-Enhanced Blotter and a Quotebook that feeds structured market data to algo models and alerts. The product supports multiple asset classes (Fixed Income, Commodities) and languages with claimed 95%+ precision. Sense Street ships a real REST API — a batch processing API under /api/v1 plus a WebSocket streaming API for commodity quote feeds — and publishes a first-party, actively maintained Python client to PyPI. The API contract itself is not public: the OpenAPI exists but is issued to customers, the documentation pages are listed publicly while their bodies require sign-in, and access requires a per-tenant host, VPN connectivity,
  allowlisted static IPs and a registered RSA key pair. Sense Street Limited is registered in London with an engineering office in Kraków, and is a portfolio company of Seedcamp and Speedinvest.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sense-street.png
layout: provider
mcp_servers:
- description: ''
  name: Sense Street MCP Server
  slug: sense-street-mcp-server
modified: '2026-08-14'
name: Sense Street
nav: Providers
network: true
overview: 'Sense Street publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Capital Markets, Trading, Artificial Intelligence, and Fintech.


  Sense Street''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 18 more developer resources.'
plans:
- name: Sense Street Plans Pricing
  plan_count: 0
  slug: sense-street-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Sense Street Rate Limits
  slug: sense-street-rate-limits
score:
  band: thin
  composite: 32.1
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 32.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 53.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Sense Street Authentication
  slug: sense-street-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Sense Street Domain Security
  slug: sense-street-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: trust-center
  name: Sense Street Trust Center
  slug: sense-street-trust-center
  summary_line: SOC 2 Type II, ISO 27001, Data Protection Registration Certificate
slug: sense-street
tags:
- Company
- Capital Markets
- Trading
- Artificial Intelligence
- Fintech
- Conversation Intelligence
- OTC
- Market Data
- Natural Language Processing
- Commodities
- Fixed Income
website: https://sensestreet.com
---
