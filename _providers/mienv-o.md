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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST API for comparing carrier rates, creating shipments and shipping labels, and tracking parcels across Latin American carriers. Live, authenticated host at api.mienvio.mx/v2.
  name: Mienvío Shipping API
  slug: mienvío-shipping-api
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://mienvio.mx
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mienvio.mx/api
- group: docs
  title: ''
  type: Documentation
  url: https://mienvio.mx/api
- group: company
  title: ''
  type: Blog
  url: https://mienvio.mx/blog-mienvio
- group: start
  title: ''
  type: SignUp
  url: https://mienvio.mx/signup
- group: start
  title: ''
  type: Login
  url: https://app2.mienvio.mx/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mienvio.mx/terminos-y-condiciones-mienvio
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mienv-o-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mienv-o-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mienv-o-llms.txt
created: '2026-07-17'
description: Mienvío is a Mexican logistics control-tower platform that unifies multiple parcel carriers behind a single multi-carrier shipping API and dashboard for e-commerce, retail, marketplace, and fintech shippers across Latin America. It compares carrier rates, automates routing by cost, SLA, and coverage zone, generates shipping labels, and provides real-time tracking, delivery-incident management, and post-purchase customer notifications. Merchants integrate through the REST API (api.mienvio.mx/v2) or prebuilt Shopify and WooCommerce connectors, shipping nationally, internationally, and locally across Mexico, Colombia, Chile, Costa Rica, Peru, Guatemala, and El Salvador.
image: https://cdn.prod.website-files.com/65b146ad7d71aced5d8ce108/66215bcd108d7fa4e58d0d3b_icono-256.jpg
layout: provider
modified: '2026-07-20'
name: Mienvío
nav: Providers
network: true
overview: 'Mienvío publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Shipping, Logistics, Multi-Carrier, and E-Commerce.


  Mienvío''s developer surface includes documentation, engineering blog, signup flow, and 7 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 12.5
  coverage:
    artifact_dirs: 5
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 13.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mienv-o/refs/heads/main/screenshots/mienv-o-2026-08-07T172857.png
security:
- kind: domain-security
  name: Mienv O Domain Security
  slug: mienv-o-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mienv-o
tags:
- Company
- Shipping
- Logistics
- Multi-Carrier
- E-Commerce
- Fulfillment
- Package Tracking
- Mexico
- Latin America
website: https://mienvio.mx
---
