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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shopzilla-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shopzilla-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.shopzilla.com
coverage:
  checked: '2026-08-13'
  detail: Shopzilla ships only a consumer comparison-shopping website — developer.shopzilla.com, api.shopzilla.com and docs.shopzilla.com do not resolve at all, and the publisher API program a reader might expect to find here is published under the Connexity brand at api.cnnx.link (page title "Connexity Monetization API", contact info@connexity.com), so it belongs to a Connexity profile rather than to this one.
  evidence:
  - status: 200
    url: https://api.cnnx.link/
  - status: 403
    url: https://www.shopzilla.com/.well-known/security.txt
  - status: 404
    url: https://catalog.bizrate.com/openapi.json
  - status: 400
    url: https://catalog.bizrate.com/services/catalog/v1/us/product
  - status: 200
    url: https://registry.npmjs.org/-/v1/search?text=shopzilla
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'Shopzilla is a comparison-shopping brand that lets consumers search across thousands of merchants to compare products, prices, and merchant ratings. Originally launched as BizRate and later Shopzilla, Inc., the business rebranded its corporate entity to Connexity in 2014 and is today operated by Connexity, a Taboola company, alongside sibling properties such as Bizrate, Beso, and PriceGrabber. Shopzilla itself publishes no API: no Shopzilla-branded developer host resolves in DNS (developer.shopzilla.com, api.shopzilla.com and docs.shopzilla.com are all NXDOMAIN), and www.shopzilla.com sits behind an AWS CloudFront WAF that bot-challenges the root and returns HTTP 403 on every other path, including all /.well-known/ locations. The publisher/affiliate API program that was historically marketed as the Shopzilla Publisher Program is today published under the CONNEXITY brand, on Connexity-owned hosts, and is deliberately not catalogued here: the docs are titled "Connexity Monetization
  API", list info@connexity.com as the contact, and are served from api.cnnx.link and publisher-api.connexity.com. The legacy Catalog API host catalog.bizrate.com does still answer, but returns bare Tomcat errors and publishes no specification. This profile was surfaced as a portfolio company of Norwest Venture Partners; the 2026-08-13 enrichment pass probed 18 paths across three hosts, swept five package registries, and found no Shopzilla developer surface of any kind.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shopzilla.png
layout: provider
modified: '2026-08-13'
name: Shopzilla
nav: Providers
network: true
overview: Shopzilla is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Comparison Shopping, Retail, E-Commerce, and Affiliate Marketing.
random_paper: 16
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Shopzilla Domain Security
  slug: shopzilla-domain-security
  summary_line: TLSv1.3 · DMARC
slug: shopzilla
tags:
- Company
- Comparison Shopping
- Retail
- E-Commerce
- Affiliate Marketing
- Price Comparison
- Product Discovery
website: https://www.shopzilla.com
---
