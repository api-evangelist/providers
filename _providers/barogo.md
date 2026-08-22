---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Barogo Agentic Access
  operation_count: 21
  slug: barogo-agentic-access
  summary_line: 21 operations · 14 acting
api_count: 5
apis:
- description: 상점 배달 권역 / 불가 구역 / 할증 구역 조회
  name: Barogo Areas API
  slug: barogo-areas-api
- description: 배달대행사 배달 수행 상태 조회
  name: Barogo Delivery API
  slug: barogo-delivery-api
- description: 상점 예치금(Cash, Money) 잔액 조회
  name: Barogo Deposits API
  slug: barogo-deposits-api
- description: 주문 접수 / 조회 / 수정 / 취소 및 배달 가능 여부·요금 조회
  name: Barogo Orders API
  slug: barogo-orders-api
- description: 상점 조회 및 주문 제휴사 ↔ 고릴라 상점 매핑
  name: Barogo Stores API
  slug: barogo-stores-api
artifact_total: 17
asyncapis:
- description: ''
  name: Barogo Gorela Webhooks
  slug: barogo-gorela-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Barogo Gorela Order Agency Areas API
  slug: open-barogo-areas-api
- collection_type: open
  name: Barogo Gorela Order Agency Delivery API
  slug: open-barogo-delivery-api
- collection_type: open
  name: Barogo Gorela Order Agency Deposits API
  slug: open-barogo-deposits-api
- collection_type: open
  name: Barogo Gorela Callback (Webhook) API
  slug: open-barogo-gorela-callbacks
- collection_type: open
  name: Barogo Gorela Order Agency Orders API
  slug: open-barogo-orders-api
- collection_type: open
  name: Barogo Gorela Order Agency Stores API
  slug: open-barogo-stores-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/barogo-gorela-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.barogo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.gorelas.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.gorelas.com/api-doc/request
- group: docs
  title: ''
  type: APIReference
  url: https://developer.gorelas.com/api-docs-md/index.md
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.gorelas.com/api-docs-md/index.md#연동-가이드
- group: start
  title: ''
  type: SignUp
  url: https://developer.gorelas.com/linkage
- group: operate
  title: ''
  type: Support
  url: mailto:tech_poc@barogo.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BarogoDevelopers
- group: company
  title: ''
  type: Blog
  url: https://m.blog.naver.com/PostList.nhn?blogId=barogo_info
- group: company
  title: ''
  type: News
  url: https://www.barogo.com/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.barogo.com/policy/delivery
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.barogo.com/policy/privacy
- group: commercial
  title: ''
  type: LocationBasedServicesTerms
  url: https://www.barogo.com/policy/locationbased
- group: start
  title: ''
  type: Console
  url: https://admin.gorelas.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/barogo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/barogo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/barogo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/barogo-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/barogo-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/barogo-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/barogo-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/barogo-gorela-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/barogo-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/barogo-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/barogo-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/barogo-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/barogo-well-known.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/barogo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/barogo-domain-security.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/barogo-stock
created: '2026-08-06'
description: Barogo (바로고) is a South Korean last-mile delivery platform founded in 2014 and headquartered in Gangnam-gu, Seoul. It operates a nationwide two-wheeler dispatch network for food and goods, with rider, merchant and hub-manager apps and a store POS program, and counts McDonald's, Burger King, KFC, Krispy Kreme, Baskin Robbins and Dunkin among its clients. Its developer-facing product is Gorela (고릴라), a delivery-brokerage platform that sits between an "order agency" — a POS, marketplace or commerce platform that takes the customer's order — and the delivery agencies that assign riders. The Gorela API covers fare quoting and serviceability, order intake in fixed-fare and flexible-fare modes, order read/amend/cancel, store mapping, prepaid store balances, delivery-agency status and delivery zones, plus twenty callbacks pushed back to the partner as an order fans out into its child deliveries.
image: https://www.barogo.com/images/common/logo.png
layout: provider
mcp_servers:
- description: ''
  name: barogo-mcp.yml
  slug: barogo-mcpyml
modified: '2026-08-06'
name: Barogo
nav: Providers
network: true
overview: 'Barogo publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Areas API, Delivery API, Deposits API, and 2 more. Tagged areas include Company, Delivery, Logistics, Last Mile Delivery, and Food Delivery.


  The Barogo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Barogo''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, product news, and 25 more developer resources.'
random_paper: 4
score:
  band: developing
  composite: 42.2
  delta: -9.3
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 69.3
    developer_ergonomics: 39.9
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 83.3
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/barogo/refs/heads/main/screenshots/barogo-2026-08-07T162156.png
security:
- kind: authentication
  name: Barogo Authentication
  slug: barogo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Barogo Domain Security
  slug: barogo-domain-security
  summary_line: TLSv1.3
slug: barogo
tags:
- Company
- Delivery
- Logistics
- Last Mile Delivery
- Food Delivery
- Courier
- Fulfillment
- Orders
- Webhooks
- South Korea
- Transportation
- Marketplace
website: https://www.barogo.com/
---
