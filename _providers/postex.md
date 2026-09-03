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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://api.postex.pk/services/integration/api/order
  baseurl_source: declared
  description: Booking, tracking, and listing shipment orders
  name: PostEx Orders API
  slug: postex-orders-api
- baseURL: https://api.postex.pk/services/integration/api/order
  baseurl_source: declared
  description: Operational cities and merchant address reference data
  name: PostEx Reference API
  slug: postex-reference-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PostEx Merchant Order Integration Orders API
  slug: open-postex-orders-api
- collection_type: open
  name: PostEx Merchant Order Integration Orders Reference API
  slug: open-postex-reference-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/postex-order-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/postex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://postex.pk
- group: agent
  title: ''
  type: MCPServer
  url: mcp/postex-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/postex-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/postex-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/postex-authentication.yml
created: '2026-07-17'
description: PostEx is a Pakistani e-commerce logistics, courier, and fintech platform that provides cash-on-delivery parcel fulfilment with instant upfront payments to online merchants, alongside a business suite for expense management, working- capital financing, and the XPay payment gateway. Merchants and order- management systems integrate with PostEx through its merchant Order Integration API (https://api.postex.pk) to book shipments, look up operational cities and pickup addresses, track parcels, and reconcile orders. This profile was enriched by API Evangelist by live-probing the production API host, which confirmed a real merchant integration surface authenticated with a token request header. PostEx is backed by 500 Global.
image: https://postex.pk/favicon.ico
layout: provider
mcp_servers:
- description: Candidate MCP server for the PostEx merchant Order Integration API. No official hosted or remote MCP server was found for PostEx; this tool list is derived one-tool-per-operation from the OpenAPI defi
  name: PostEx MCP Server
  slug: postex-mcp-server
modified: '2026-07-20'
name: PostEx
nav: Providers
network: true
overview: 'PostEx publishes 2 APIs on the [APIs.io](https://apis.io/) network: Orders API and Reference API. Tagged areas include Company, Logistics, Couriers, Shipping, and E-Commerce.


  PostEx''s developer surface includes authentication and 7 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 55.8
    developer_ergonomics: 13.7
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 23.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/postex/refs/heads/main/screenshots/postex-2026-09-02T151830.png
security:
- kind: authentication
  name: Postex Authentication
  slug: postex-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Postex Domain Security
  slug: postex-domain-security
  summary_line: TLSv1.3 · DMARC
slug: postex
tags:
- Company
- Logistics
- Couriers
- Shipping
- E-Commerce
- Fulfillment
- Cash on Delivery
- Payments
- Fintech
- Pakistan
website: https://postex.pk
---
