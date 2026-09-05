---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.3
  scored_at: '2026-09-04'
api_count: 9
apis:
- baseURL: https://api-test.seel.com/v1
  baseurl_source: declared
  description: The Bill API from Seel — 3 operation(s) for bill.
  name: Seel Bill API
  slug: seel-bill-api
- baseURL: https://api-test.seel.com/v1
  baseurl_source: declared
  description: The Claim API from Seel — 2 operation(s) for claim.
  name: Seel Claim API
  slug: seel-claim-api
- baseURL: https://api-test.seel.com/v1
  baseurl_source: declared
  description: The Contract API from Seel — 2 operation(s) for contract.
  name: Seel Contract API
  slug: seel-contract-api
- baseURL: https://api-test.seel.com/v1
  baseurl_source: declared
  description: The Event API from Seel — 1 operation(s) for event.
  name: Seel Event API
  slug: seel-event-api
- baseURL: https://api-test.seel.com/v1
  baseurl_source: declared
  description: The Fulfillment API from Seel — 3 operation(s) for fulfillment.
  name: Seel Fulfillment API
  slug: seel-fulfillment-api
- baseURL: https://api-test.seel.com/v1
  baseurl_source: declared
  description: The Merchant API from Seel — 2 operation(s) for merchant.
  name: Seel Merchant API
  slug: seel-merchant-api
- baseURL: https://api-test.seel.com/v1
  baseurl_source: declared
  description: The Order API from Seel — 4 operation(s) for order.
  name: Seel Order API
  slug: seel-order-api
- baseURL: https://api-test.seel.com/v1
  baseurl_source: declared
  description: The Product API from Seel — 4 operation(s) for product.
  name: Seel Product API
  slug: seel-product-api
- baseURL: https://api-test.seel.com/v1
  baseurl_source: declared
  description: The Quote API from Seel — 2 operation(s) for quote.
  name: Seel Quote API
  slug: seel-quote-api
artifact_total: 22
asyncapis:
- description: Seel delivers webhook notifications to a merchant-configured HTTPS endpoint when protection contract and claim lifecycle events occur. Each notification is a Notification object with id, created_ts, t
  name: Seel Webhooks
  slug: seel-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Seel Commerce Protection Bill API
  slug: open-seel-bill-api
- collection_type: open
  name: Seel Commerce Protection Bill Claim API
  slug: open-seel-claim-api
- collection_type: open
  name: Seel Commerce Protection Bill Contract API
  slug: open-seel-contract-api
- collection_type: open
  name: Seel Commerce Protection Bill Event API
  slug: open-seel-event-api
- collection_type: open
  name: Seel Commerce Protection Bill Fulfillment API
  slug: open-seel-fulfillment-api
- collection_type: open
  name: Seel Commerce Protection Bill Merchant API
  slug: open-seel-merchant-api
- collection_type: open
  name: Seel Commerce Protection Bill Order API
  slug: open-seel-order-api
- collection_type: open
  name: Seel Commerce Protection Bill Product API
  slug: open-seel-product-api
- collection_type: open
  name: Seel Commerce Protection Bill Quote API
  slug: open-seel-quote-api
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/seel-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/seel-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://seel.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.seel.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.seel.com/docs/welcome-to-seel
- group: docs
  title: ''
  type: APIReference
  url: https://developer.seel.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.seel.com/docs/wfp-getting-started
- group: company
  title: ''
  type: Blog
  url: https://seel.com/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://kover2618.zendesk.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.seel.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.seel.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/seel-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/seel-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seel-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Seel is a post-purchase protection and e-commerce insurance platform that helps online merchants offer Worry-Free Purchase coverage, Extended Warranty, and return, fulfillment, and price-drop protection to their shoppers. Its API lets merchants request protection Quotes for a cart, bind coverage to Orders (creating Contracts), manage Products, Fulfillments, Claims, and Bills, and emit Events, with contract and claim lifecycle changes delivered via webhooks. Seel serves 5,000+ merchants and has protected 24M+ orders. Backed by Lightspeed Venture Partners and Techstars.
image: https://seel.com/favicon.ico
layout: provider
modified: '2026-07-21'
name: Seel
nav: Providers
network: true
overview: 'Seel publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Bill API, Claim API, Contract API, and 6 more. Tagged areas include Company, E-Commerce, Insurance, Post-Purchase, and Returns.


  The Seel catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Seel''s developer surface includes documentation, API reference, getting-started guide, engineering blog, and 11 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 9.3
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 30.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/seel/refs/heads/main/screenshots/seel-2026-09-02T154753.png
security:
- kind: authentication
  name: Seel Authentication
  slug: seel-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Seel Domain Security
  slug: seel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: seel
tags:
- Company
- E-Commerce
- Insurance
- Post-Purchase
- Returns
- Extended Warranty
- Fraud
- Payments
website: https://seel.com/
---
