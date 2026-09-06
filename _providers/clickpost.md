---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Clickpost Agentic Access
  operation_count: 10
  slug: clickpost-agentic-access
  summary_line: 10 operations · 7 acting
api_count: 7
apis:
- baseURL: https://www.clickpost.in/api/v1
  baseurl_source: spec
  description: Shipment cancellation.
  name: ClickPost Cancellation API
  slug: clickpost-cancellation-api
- baseURL: https://www.clickpost.in/api/v1
  baseurl_source: spec
  description: Shipping labels.
  name: ClickPost Label API
  slug: clickpost-label-api
- baseURL: https://www.clickpost.in/api/v1
  baseurl_source: spec
  description: Order creation and lookup.
  name: ClickPost Order API
  slug: clickpost-order-api
- baseURL: https://www.clickpost.in/api/v1
  baseurl_source: spec
  description: Pickup scheduling.
  name: ClickPost Pickup API
  slug: clickpost-pickup-api
- baseURL: https://www.clickpost.in/api/v1
  baseurl_source: spec
  description: Carrier recommendation operations.
  name: ClickPost Recommendation API
  slug: clickpost-recommendation-api
- baseURL: https://www.clickpost.in/api/v1
  baseurl_source: spec
  description: Pincode and zone serviceability.
  name: ClickPost Serviceability API
  slug: clickpost-serviceability-api
- baseURL: https://www.clickpost.in/api/v1
  baseurl_source: spec
  description: Shipment tracking.
  name: ClickPost Tracking API
  slug: clickpost-tracking-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ClickPost Cancellation API
  slug: open-clickpost-cancellation-api
- collection_type: open
  name: ClickPost Cancellation Label API
  slug: open-clickpost-label-api
- collection_type: open
  name: ClickPost Cancellation Order API
  slug: open-clickpost-order-api
- collection_type: open
  name: ClickPost Cancellation Pickup API
  slug: open-clickpost-pickup-api
- collection_type: open
  name: ClickPost Cancellation Recommendation API
  slug: open-clickpost-recommendation-api
- collection_type: open
  name: ClickPost Cancellation Serviceability API
  slug: open-clickpost-serviceability-api
- collection_type: open
  name: ClickPost Cancellation Tracking API
  slug: open-clickpost-tracking-api
- collection_type: open
  name: ClickPost API
  slug: open-clickpost
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/clickpost-capability-edges.yml
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
overview: 'ClickPost publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Cancellation API, Label API, Order API, and 4 more. Tagged areas include Carriers, Delivery, E-commerce Logistics, Logistics, and Returns.


  The ClickPost catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ClickPost''s developer surface includes authentication, documentation, engineering blog, and 13 more developer resources.'
plans:
- name: Clickpost Plans Pricing
  plan_count: 3
  slug: clickpost-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Clickpost Rate Limits
  slug: clickpost-rate-limits
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: ClickPost API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 4
  slug: clickpost-rules
score:
  band: developing
  composite: 43.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 45.5
    contract_quality: 55.8
    developer_ergonomics: 28.6
    discoverability: 72.2
    governance: 45.5
    operational_transparency: 10.5
  previous_composite: 43.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 43.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- E-commerce Logistics
- Logistics
- Returns
- Shipping
- Supply Chain
- Tracking
website: https://www.clickpost.ai
---
