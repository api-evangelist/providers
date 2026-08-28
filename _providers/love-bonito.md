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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/love-bonito-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lovebonito.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.lovebonito.com/intl/faq
- group: operate
  title: ''
  type: Support
  url: https://www.lovebonito.com/intl/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lovebonito.com/intl/pages/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lovebonito.com/intl/pages/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/love-bonito
- group: commercial
  title: ''
  type: Plans
  url: plans/love-bonito-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/love-bonito-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/love-bonito-llms.txt
coverage:
  checked: '2026-08-25'
  detail: Love, Bonito is a direct-to-consumer womenswear retailer whose product is clothing, not software; the only API host it runs, the Kong gateway at api.lovebonito.com, is undocumented private plumbing for its own storefront and mobile apps and returns 401 Unauthorized on every path including /.well-known/*, while no developers./docs. host resolves and its 2,472-URL sitemap contains no developer page.
  evidence:
  - status: 401
    url: https://api.lovebonito.com/
  - status: 401
    url: https://api.lovebonito.com/rest/all/schema
  - status: 401
    url: https://api.lovebonito.com/graphql
  - status: 0
    url: https://developers.lovebonito.com/
  - status: 404
    url: https://www.lovebonito.com/.well-known/api-catalog
  - status: 404
    url: https://www.lovebonito.com/.well-known/agent-card.json
  - status: 200
    url: https://www.lovebonito.com/media/sitemaps/sg_sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-25'
description: Love, Bonito is a Singapore-headquartered direct-to-consumer womenswear brand, founded in 2010 out of the BonitoChico blogshop and now one of Southeast Asia's largest vertically integrated fashion labels. It designs, manufactures and retails women's apparel — Signatures, Staples and Capsule collections spanning tops, dresses, bottoms, matching sets, petites and maternity — through its own e-commerce storefront, iOS/Android shopping apps and physical stores across Singapore, Malaysia, Indonesia, Hong Kong, Cambodia and the Philippines. The commerce stack is a Next.js storefront on a Magento-derived backend with Storyblok for content, fronted by Cloudflare, with an internal Kong API gateway at api.lovebonito.com serving its own first-party apps. Love, Bonito publishes no public developer program, API reference, or machine-readable contract; its partner surface is an affiliate program run through third-party networks (Impact, FlexOffers), not a first-party API.
image: https://www.lovebonito.com/resources/favicons/192.png?v=3
layout: provider
modified: '2026-08-25'
name: Love Bonito
nav: Providers
network: true
overview: 'Love Bonito is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Fashion, and Apparel.


  Love Bonito''s developer surface includes support and 9 more developer resources.'
plans:
- name: Love Bonito Plans Pricing
  plan_count: 0
  slug: love-bonito-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Love Bonito Rate Limits
  slug: love-bonito-rate-limits
score:
  band: minimal
  composite: 5.3
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: domain-security
  name: Love Bonito Domain Security
  slug: love-bonito-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: love-bonito
tags:
- Company
- Retail
- E-Commerce
- Fashion
- Apparel
- Direct to Consumer
- Singapore
- Southeast Asia
website: https://www.lovebonito.com/
---
