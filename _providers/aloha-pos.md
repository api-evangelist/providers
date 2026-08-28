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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Aloha Pos Agentic Access
  operation_count: 14
  slug: aloha-pos-agentic-access
  summary_line: 14 operations · 8 acting
api_count: 5
apis:
- description: Aloha Cloud-specific endpoints including the In-Store API server (gRPC, default port 50051, 127.0.0.1) for local POS connectivity and the Business Services Layer (BSL) Order Service for routing online
  name: Aloha Cloud APIs
  slug: aloha-cloud-api
- description: Item and item-price management.
  name: Aloha POS Catalog API
  slug: aloha-pos-catalog-api
- description: Menu structure and details.
  name: Aloha POS Menu API
  slug: aloha-pos-menu-api
- description: Order creation and lookup.
  name: Aloha POS Order API
  slug: aloha-pos-order-api
- description: Site (location) provisioning and lookup.
  name: Aloha POS Site API
  slug: aloha-pos-site-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NCR Voyix Commerce Platform APIs (Aloha) Catalog API
  slug: open-aloha-pos-catalog-api
- collection_type: open
  name: NCR Voyix Commerce Platform APIs (Aloha) Catalog Menu API
  slug: open-aloha-pos-menu-api
- collection_type: open
  name: NCR Voyix Commerce Platform APIs (Aloha) Catalog Order API
  slug: open-aloha-pos-order-api
- collection_type: open
  name: NCR Voyix Commerce Platform APIs (Aloha) Catalog Site API
  slug: open-aloha-pos-site-api
- collection_type: open
  name: NCR Voyix Commerce Platform APIs (Aloha)
  slug: open-ncr-voyix-platform
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aloha-pos-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aloha-pos-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aloha-pos-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.ncrvoyix.com/restaurants/aloha-cloud
- group: other
  title: ''
  type: Developer
  url: https://developer.ncrvoyix.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ncrvoyix.com/restaurant/aloha-pos
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NCRVoyix-Corporation
- group: other
  title: ''
  type: APIExplorer
  url: https://developer.ncrvoyix.com/portals/dev-portal/api-explorer
- group: auth
  title: HMAC (AccessKey) Authentication
  type: Authentication
  url: https://github.com/NCRVoyix-Corporation/ncr-bsp-hmac
- group: design
  title: ''
  type: Rules
  url: rules/ncr-voyix-platform-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/aloha-pos-ncr-voyix-platform-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/aloha-pos-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aloha-pos-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aloha-pos-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/aloha-pos-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.ncrvoyix.com/resources/blog
created: '2026-05-08'
description: Aloha POS is a restaurant point-of-sale platform from NCR Voyix. The NCR Voyix Developer Experience exposes APIs for Aloha (cloud and on-premise) covering site, store, menu, order, payment, and reporting integrations as part of the broader NCR Voyix Commerce Platform.
examples:
- key_count: 4
  name: Ncr Voyix Platform Create Order Example
  slug: ncr-voyix-platform-create-order-example
- key_count: 4
  name: Ncr Voyix Platform Create Site Example
  slug: ncr-voyix-platform-create-site-example
- key_count: 5
  name: Ncr Voyix Platform Put Catalog Item Example
  slug: ncr-voyix-platform-put-catalog-item-example
- key_count: 5
  name: Ncr Voyix Platform Put Item Price Example
  slug: ncr-voyix-platform-put-item-price-example
finops:
- name: Aloha Pos Finops
  service_category: Payments & POS
  slug: aloha-pos-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aloha-pos.png
json_schemas:
- name: ItemPrice
  property_count: 6
  slug: ncr-voyix-platform-item-price
- name: Item
  property_count: 6
  slug: ncr-voyix-platform-item
- name: Order
  property_count: 5
  slug: ncr-voyix-platform-order
- name: Site
  property_count: 5
  slug: ncr-voyix-platform-site
json_structures:
- name: Ncr Voyix Platform Item Price Structure
  property_count: 6
  slug: ncr-voyix-platform-item-price-structure
- name: Ncr Voyix Platform Item Structure
  property_count: 6
  slug: ncr-voyix-platform-item-structure
- name: Ncr Voyix Platform Order Structure
  property_count: 5
  slug: ncr-voyix-platform-order-structure
- name: Ncr Voyix Platform Site Structure
  property_count: 5
  slug: ncr-voyix-platform-site-structure
jsonld:
- class_count: 4
  name: Aloha Pos Ncr Voyix Platform Context
  property_count: 33
  slug: aloha-pos-ncr-voyix-platform-context
layout: provider
modified: '2026-06-02'
name: Aloha POS
nav: Providers
network: true
overview: 'Aloha POS publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Menu API, Order API, and 1 more. Tagged areas include Point-of-Sale, Restaurant, Hospitality, and NCR.


  The Aloha POS catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Aloha POS''s developer surface includes authentication, documentation, engineering blog, and 14 more developer resources.'
plans:
- name: Aloha Pos Plans Pricing
  plan_count: 2
  slug: aloha-pos-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Aloha Pos Rate Limits
  slug: aloha-pos-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Aloha POS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: aloha-pos-jsonschema-spectral-rules
- effective_rule_count: 70
  extends:
  - spectral:oas
  name: Aloha POS API Rules
  rule_count: 29
  severity_counts:
    error: 8
    hint: 0
    info: 7
    warn: 14
  slug: ncr-voyix-platform-rules
score:
  band: emerging
  composite: 23.4
  delta: 3.1
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 28.8
    contract_quality: 22.0
    developer_ergonomics: 26.2
    discoverability: 55.6
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 20.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aloha-pos/refs/heads/main/screenshots/aloha-pos-2026-06-20T171543.png
security:
- kind: authentication
  name: Aloha Pos Authentication
  slug: aloha-pos-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aloha Pos Domain Security
  slug: aloha-pos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aloha-pos
tags:
- Point-of-Sale
- Restaurant
- Hospitality
- NCR
website: https://www.ncrvoyix.com/restaurants/aloha-cloud
---
