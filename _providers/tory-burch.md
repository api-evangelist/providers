---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 3.6
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tory-burch-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tory-burch-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/tory-burch-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tory-burch-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tory-burch-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.toryburch.com/en-us/
- group: company
  title: ''
  type: About
  url: https://www.toryburch.com/en-us/about-us/
- group: operate
  title: ''
  type: Support
  url: https://www.toryburch.com/en-us/client-services/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.toryburch.com/en-us/client-services/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.toryburch.com/en-us/customer-services/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.toryburch.com/en-us/terms-of-use/content-terms-and-conditions/
- group: other
  title: ''
  type: Locations
  url: https://www.toryburch.com/en-us/stores/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tory-burch
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/toryburch
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/toryburch
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/toryburch
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/toryburch
- group: other
  title: ''
  type: Pinterest
  url: https://pinterest.com/ToryBurch
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Tory_Burch_LLC
- group: other
  title: ''
  type: Foundation
  url: https://www.toryburchfoundation.org/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/tory-burch_stock/
coverage:
  checked: '2026-08-05'
  detail: Tory Burch is a luxury fashion retailer whose product is physical goods; the only machine-readable document it serves is a retail-content llms.txt indexing 778 storefront pages, and the Apigee gateway behind www.toryburch.com/api/ answers every probed path with an ApplicationNotFound fault because no public proxy is registered on it.
  evidence:
  - status: 200
    url: https://www.toryburch.com/llms.txt
  - status: 404
    url: https://www.toryburch.com/api/graphql
  - status: 301
    url: https://www.toryburch.com/openapi.json
  - status: 404
    url: https://www.toryburch.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/toryburch
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: 'Tory Burch LLC is an American luxury women''s fashion label founded in February 2004 by designer Tory Burch and headquartered in New York City, trading under the legal entity River Light V, L.P. The privately held company designs and sells ready-to-wear clothing, designer shoes, handbags, small leather goods, jewellery, watches, eyewear, fragrance and beauty, swimwear and home decor, together with the Tory Sport activewear line, through roughly 400 boutiques worldwide, wholesale partners and a direct-to-consumer storefront at toryburch.com serving the United States, United Kingdom, the European Union and Asia. Its affiliated Tory Burch Foundation funds and educates women entrepreneurs. Tory Burch is a fashion and retail business rather than a software vendor: it operates no developer program, publishes no API documentation, SDKs or machine-readable API contract, and holds no public GitHub organisation. Its storefront is a Next.js front end on Akamai over a Salesforce Commerce
  Cloud (Demandware) commerce platform with Adobe Scene7 media, and an Apigee API gateway fronts www.toryburch.com/api/ for first-party storefront traffic only, exposing no publicly registered proxy. The one machine-readable artifact the company does publish is a site-wide llms.txt.'
image: https://s7.toryburch.com/is/image/ToryBurch/medallion-navy@2x.1200x1200.jpg
layout: provider
modified: '2026-08-05'
name: Tory Burch
nav: Providers
network: true
overview: 'Tory Burch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fashion, Luxury Goods, Apparel, and Footwear.


  Tory Burch''s developer surface includes support, YouTube channel, and 19 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 13.4
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 0.0
  provenance:
    conformance: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: domain-security
  name: Tory Burch Domain Security
  slug: tory-burch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tory-burch
tags:
- Company
- Fashion
- Luxury Goods
- Apparel
- Footwear
- Handbags and Accessories
- Retail
- Ecommerce
- Direct to Consumer
- Consumer Brands
- United States
website: https://www.toryburch.com/en-us/
---
