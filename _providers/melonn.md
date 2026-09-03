---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 4.3
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: REST API to connect any external platform to Melonn's logistics operations — order management, inventory queries, shipment tracking, and returns — with real-time webhooks for order and inventory statu
  name: Melonn REST API
  slug: melonn-rest-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/melonn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.melonn.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.melonn.com/integraciones/melonn-api/
- group: company
  title: ''
  type: Blog
  url: https://www.melonn.com/blog/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.melonn.com/faq/
- group: start
  title: ''
  type: SignUp
  url: https://www.melonn.com/colombia/solicitar-asesoria/
created: '2026-07-17'
description: Melonn is a third-party logistics (3PL) and multichannel fulfillment operator for e-commerce businesses across Colombia and Mexico. Through its proprietary Órbita platform it centralizes inventory, processes and packs orders, manages returns, and offers same/next-day delivery, unifying multiple sales channels into a single operation. Melonn connects to platforms such as Shopify, VTEX, WooCommerce, Magento, PrestaShop, MercadoLibre, Amazon, Walmart, Rappi, TikTok Shop, Liverpool, and Coppel, and exposes a REST API with real-time webhooks so any external platform can drive order management, inventory queries, shipment tracking, and returns. Melonn was surfaced as a portfolio company of QED Investors. Public developer documentation and a sandbox are provided on request via the Melonn advisory/contact form rather than an open developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/melonn.png
layout: provider
modified: '2026-07-20'
name: Melonn
nav: Providers
network: true
overview: 'Melonn publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fulfillment, Logistics, E-Commerce, and Supply Chain.


  Melonn''s developer surface includes documentation, engineering blog, signup flow, and 3 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 3
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 13.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/melonn/refs/heads/main/screenshots/melonn-2026-08-07T172453.png
security:
- kind: domain-security
  name: Melonn Domain Security
  slug: melonn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: melonn
tags:
- Company
- Fulfillment
- Logistics
- E-Commerce
- Supply Chain
- Shipping
- Latin America
- 3PL
website: https://www.melonn.com
---
