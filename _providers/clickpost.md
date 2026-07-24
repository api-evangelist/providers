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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Clickpost Agentic Access
  operation_count: 10
  slug: clickpost-agentic-access
  summary_line: 10 operations · 7 acting
api_count: 7
apis:
- description: Shipment cancellation.
  name: ClickPost Cancellation API
  slug: clickpost-cancellation-api
- description: Shipping labels.
  name: ClickPost Label API
  slug: clickpost-label-api
- description: Order creation and lookup.
  name: ClickPost Order API
  slug: clickpost-order-api
- description: Pickup scheduling.
  name: ClickPost Pickup API
  slug: clickpost-pickup-api
- description: Carrier recommendation operations.
  name: ClickPost Recommendation API
  slug: clickpost-recommendation-api
- description: Pincode and zone serviceability.
  name: ClickPost Serviceability API
  slug: clickpost-serviceability-api
- description: Shipment tracking.
  name: ClickPost Tracking API
  slug: clickpost-tracking-api
artifact_total: 17
collections:
- collection_type: open
  name: ClickPost API
  slug: open-clickpost
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clickpost-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/clickpost-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clickpost-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clickpost-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Clickpost
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clickpost1
- group: company
  title: ''
  type: Website
  url: https://www.clickpost.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.clickpost.ai/
- group: build
  title: ''
  type: Carrier Integrations
  url: https://www.clickpost.ai/carrier-integration
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clickpost.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clickpost.ai/terms-and-conditions
- group: design
  title: ''
  type: JSONLD
  url: json-ld/clickpost-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/clickpost-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.clickpost.ai/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.clickpost.ai/blog
created: '2025-03-01'
description: ClickPost is a logistics and supply chain platform that aggregates 500+ carrier integrations, multi-channel customer notifications, and 50+ storefront/OMS/WMS connectors behind a unified REST API. The platform covers carrier recommendation, order creation (single and multi-piece), serviceability, manifesting, pickups, real-time tracking with webhooks, proof of delivery, NDR (non-delivery report) management, returns, and expected delivery date forecasting for both Indian domestic and international shipments.
finops:
- name: Clickpost Finops
  service_category: API
  slug: clickpost-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clickpost.png
jsonld:
- class_count: 0
  name: Clickpost Context
  property_count: 6
  slug: clickpost-context
layout: provider
modified: '2026-05-19'
name: ClickPost
nav: Providers
network: true
overview: 'ClickPost publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Cancellation API, Label API, Order API, and 4 more. Tagged areas include Carriers, Delivery, E-Commerce Logistics, Logistics, and Returns.


  The ClickPost catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ClickPost''s developer surface includes authentication, documentation, engineering blog, and 12 more developer resources.'
plans:
- name: Clickpost Plans Pricing
  plan_count: 3
  slug: clickpost-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Clickpost Rate Limits
  slug: clickpost-rate-limits
rules:
- name: ClickPost API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 4
  slug: clickpost-rules
score:
  band: developing
  composite: 46.4
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 61.1
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 26.3
    operational_transparency: 36.8
  previous_composite: 46.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clickpost/refs/heads/main/screenshots/clickpost-2026-06-20T174515.png
security:
- kind: authentication
  name: Clickpost Authentication
  slug: clickpost-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Clickpost Domain Security
  slug: clickpost-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Clickpost Vulnerability Disclosure
  slug: clickpost-vulnerability-disclosure
  summary_line: disclosure policy published
slug: clickpost
tags:
- Carriers
- Delivery
- E-Commerce Logistics
- Logistics
- Returns
- Shipping
- Supply Chain
- Tracking
website: https://www.clickpost.ai
---
