---
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wooden-street-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wooden-street-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/wooden-street-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wooden-street-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://www.woodenstreet.com/
- group: company
  title: ''
  type: Blog
  url: https://www.woodenstreet.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.woodenstreet.com/grievance-redressal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.woodenstreet.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.woodenstreet.com/privacy-policy
coverage:
  checked: '2026-09-04'
  detail: 'Wooden Street is a physical-goods retailer — an Indian direct-to-consumer furniture brand that manufactures and sells solid-wood furniture through woodenstreet.com and 100+ company-owned experience stores — so there is no product to expose as an API and no developer program to find: its own robots.txt disallows /api/, its 345-URL information sitemap contains no developer, API, partner or integration page, no public package registry, Postman workspace or GitHub organization carries a first-party client, and the one first-party backend host that does resolve (api.woodenstreet.com, behind Cloudflare) answers every discovery path with its private JSON envelope {"status":"error","message":"Route not found"}.'
  evidence:
  - status: 200
    url: https://www.woodenstreet.com/
  - status: 404
    url: https://www.woodenstreet.com/openapi.json
  - status: 404
    url: https://www.woodenstreet.com/.well-known/agent-card.json
  - status: 404
    url: https://api.woodenstreet.com/openapi.json
  - status: 404
    url: https://api.woodenstreet.com/graphql
  - status: 404
    url: https://api.woodenstreet.com/.well-known/agent-card.json
  - status: 404
    url: https://www.woodenstreet.com/developers
  reason: not-a-software-company
  state: none
created: '2026-09-04'
description: 'Wooden Street (operated by Ufurnish Technology Pvt. Ltd.) is an Indian direct-to-consumer furniture and home-furnishing brand founded in 2015 in Jaipur, Rajasthan by Lokendra Ranawat, Virendra Ranawat, Dinesh Pratap Singh and Vikas Baheti. It sells solid-wood and custom-made furniture, mattresses, home decor, modular kitchens and wardrobes through woodenstreet.com and a company-owned, company-operated network of experience stores across more than 100 Indian cities, backed by its own manufacturing and warehousing. The company is venture-backed (Indian Angel Network and Rajasthan Venture Capital Funds, then WestBridge Capital in 2022 and a Series C led by Premji Invest) and appears in the API Evangelist network via the secondary-market harvest, where it is listed on EquityZen and Nasdaq Private Market. As of this enrichment pass Wooden Street publishes no public developer program: there is no developer portal, API reference, OpenAPI/GraphQL/AsyncAPI definition, SDK, Postman collection,
  MCP server or agent card anywhere on its public surface, and its robots.txt explicitly disallows /api/. A first-party backend host, api.woodenstreet.com, is reachable and answers with a JSON envelope, but it is the undocumented private backend for the retail storefront and mobile apps rather than a published API product.'
image: https://www.woodenstreet.com/apple-touch-icon.png
layout: provider
modified: '2026-09-04'
name: Wooden Street
nav: Providers
network: true
overview: 'Wooden Street is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Furniture, Home Furnishing, Ecommerce, and Retail.


  Wooden Street''s developer surface includes engineering blog, support, and 7 more developer resources.'
plans:
- name: Wooden Street Plans Pricing
  plan_count: 0
  slug: wooden-street-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Wooden Street Rate Limits
  slug: wooden-street-rate-limits
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 10.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Wooden Street Domain Security
  slug: wooden-street-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wooden-street
tags:
- Company
- Furniture
- Home Furnishing
- Ecommerce
- Retail
- Direct To Consumer
- Interior Design
- India
website: https://www.woodenstreet.com/
---
