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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cheerz-domain-security.yml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/cheerz-well-known.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cheerz-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cheerz-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cheerz-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.cheerz.com/en
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.cheerz.com/hc/fr
- group: operate
  title: ''
  type: Contact
  url: https://www.cheerz.com/en/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.cheerz.com/fr/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cheerz
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cheerz.com/en/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cheerz.com/en/privacy-policy
- group: commercial
  title: ''
  type: Legal
  url: https://www.cheerz.com/en/legal
- group: build
  title: ''
  type: CodeOfConduct
  url: https://www.cheerz.com/en/code-of-conduct
- group: other
  title: ''
  type: iOSApp
  url: https://apps.apple.com/us/app/cheerz-photo-printing/id690875126
- group: other
  title: ''
  type: AndroidApp
  url: https://play.google.com/store/apps/details?id=com.printklub.polabox
- group: other
  title: ''
  type: ParentCompany
  url: https://www.cewe-group.com/en/about-us/corporate-group/sites/paris-site-cheerz.html
- group: build
  title: ''
  type: IntegrationModel
  url: ''
- group: other
  title: ''
  type: Products
  url: ''
coverage:
  checked: '2026-08-17'
  detail: Cheerz is a consumer photo-printing retailer with no developer surface of any kind — the only HTTP 200 on any API-shaped path is www.cheerz.com/api-docs, which is the Google-OAuth sign-in screen for the internal "Cheerz Admin" back office rather than an API reference, no api. or developer. or docs. subdomain of cheerz.com resolves in DNS, the 418-URL English and 464-URL French sitemaps contain nothing but products, categories, collections, blog posts and four legal pages, robots.txt Disallows the /*/api/* private JSON backend its own SPA and mobile apps call, and no first-party client library exists on npm, PyPI, RubyGems or Packagist.
  evidence:
  - status: 404
    url: https://www.cheerz.com/openapi.json
  - status: 404
    url: https://www.cheerz.com/developers
  - status: 404
    url: https://www.cheerz.com/graphql
  - status: 200
    url: https://www.cheerz.com/api-docs
  - status: 404
    url: https://www.cheerz.com/.well-known/agent-card.json
  - status: 404
    url: https://support.cheerz.com/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2026-08-17'
description: Cheerz is a French direct-to-consumer photo-printing brand. Customers pick photos from their phone camera roll or a connected cloud gallery in the Cheerz iOS/Android app or on cheerz.com, and Cheerz prints and ships the result as photo prints, fridge magnets, photo books and albums, wall canvases, framed prints and posters, calendars including advent calendars, puzzles, greeting and invitation cards, and the branded Cheerz Box and Memory Box gift formats. Founded in Paris in 2012 under the legal entity Printklub, backed by Serena Capital and Iron Capital, and acquired by the German photo-finishing group CEWE Stiftung & Co. KGaA in February 2018 for roughly EUR 45 million; it continues to operate as CEWE's Paris site. Cheerz publishes no public API, developer portal, SDK or machine-readable contract of any kind — it is an end-user retail product, and partnership, bulk-order and affiliate enquiries are handled by a human contact channel rather than a developer programme.
image: https://avatars.githubusercontent.com/u/2437868?v=4
layout: provider
modified: '2026-08-17'
name: Cheerz
nav: Providers
network: true
overview: 'Cheerz is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Photo Printing, E-Commerce, and Personalized Gifts.


  Cheerz''s developer surface includes engineering blog, legal docs, and 15 more developer resources.'
plans:
- name: Cheerz Plans Pricing
  plan_count: 0
  slug: cheerz-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Cheerz Rate Limits
  slug: cheerz-rate-limits
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Cheerz Domain Security
  slug: cheerz-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cheerz
tags:
- Company
- Consumer
- Photo Printing
- E-Commerce
- Personalized Gifts
- Mobile Commerce
- Print On Demand
- France
website: https://www.cheerz.com/en
---
