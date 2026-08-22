---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: Schema-driven GraphQL access to CMG's live and historical ECM dataset. Per CMG's published FAQ the feed lets teams "query specific fields across deals, participants, terms and activity through a singl
  name: CMG DataLab Real-Time Feed (GraphQL API)
  slug: capital-markets-gateway-datalab-real-time-feed
- description: 'REST API for the CMG XC workflow platform. Per CMG''s published FAQ it provides "systemic support of the full ECM deal lifecycle from setup through allocation and post-trade" and "integrates with CRM, '
  name: CMG XC REST API
  slug: capital-markets-gateway-xc-rest-api
- description: Real-time event notification surface for CMG XC. Per CMG's published FAQ, "real-time event notifications are delivered via EventHub, enabling STP integration with internal trade processing and OMS pla
  name: CMG XC EventHub
  slug: capital-markets-gateway-eventhub
artifact_total: 5
asyncapis:
- description: ''
  name: Capital Markets Gateway Eventhub
  slug: capital-markets-gateway-eventhub
common:
- group: company
  title: ''
  type: Website
  url: https://cmgx.io/
- group: company
  title: ''
  type: Blog
  url: https://cmgx.io/news-insights/
- group: company
  title: ''
  type: BlogRSS
  url: https://cmgx.io/feed/
- group: start
  title: ''
  type: SignUp
  url: https://cmgx.io/sign-up/
- group: operate
  title: ''
  type: Support
  url: https://cmgx.io/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cmgx.io/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cmgx.io/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/capital-markets-gateway
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cmg-capital-markets-gateway
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/cmgxio
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/capital-markets-gateway-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/capital-markets-gateway-eventhub.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/capital-markets-gateway-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/capital-markets-gateway-domain-security.yml
coverage:
  checked: '2026-08-09'
  detail: CMG names three programmatic surfaces in its own public FAQs — a DataLab Real-Time Feed (GraphQL API), a CMG XC REST API and EventHub event notifications — but its documentation host docs.cmgx.io 302s to a Document360 knowledge base behind the id.cmgecm.com customer identity gate, so no endpoint, GraphQL SDL, OpenAPI or event catalog is reachable without an active tenant.
  evidence:
  - status: 302
    url: https://docs.cmgx.io/
  - status: 404
    url: https://cmgx.io/developers/
  - status: 404
    url: https://cmgx.io/openapi.json
  - status: 200
    url: https://cmgx.io/data-insights/
  reason: customer-only-docs
  state: gated
created: '2026-08-09'
description: Capital Markets Gateway (CMG) is a New York headquartered financial technology company that connects the buy side and the sell side across the equity capital markets (ECM) offering process. Its two products are CMG XC, a workflow-management platform carrying the full ECM deal lifecycle — offering setup, termsheet publication, a consolidated and de-duplicated order book, bookbuilding, allocations, designations and trade release — and CMG DataLab, an ECM data and analytics service spanning 20+ years and 60,000+ equity transactions across 50+ regions, with 550+ deal, structure and performance metrics per deal. CMG names three programmatic surfaces in its own public FAQs — a DataLab Real-Time Feed (GraphQL API), a CMG XC REST API covering setup through allocation and post-trade, and EventHub real-time event notifications for straight-through processing into OMS and trade-processing systems — but publishes no public API reference, endpoint or machine-readable contract for any of
  them. The documentation host redirects to a customer identity login.
image: https://cmgx.io/wp-content/uploads/2024/11/CMG_URLPreview_2024-11-06-min-1-scaled.jpg
layout: provider
modified: '2026-08-09'
name: Capital Markets Gateway
nav: Providers
network: true
overview: 'Capital Markets Gateway publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Capital Markets, Equity Capital Markets, and Market Data.


  The Capital Markets Gateway catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Capital Markets Gateway''s developer surface includes engineering blog, signup flow, support, and 11 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 29.8
  delta: -1.7
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 7.1
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 31.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 31.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Capital Markets Gateway Domain Security
  slug: capital-markets-gateway-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: capital-markets-gateway
tags:
- Company
- Financial Services
- Capital Markets
- Equity Capital Markets
- Market Data
- Data Intelligence
- Workflow Management
- Investment Banking
- Fintech
website: https://cmgx.io/
---
