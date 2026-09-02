---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: true
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
  score: 2.2
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tiff-s-treats-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cookiedelivery.com/
- group: company
  title: ''
  type: About
  url: https://www.cookiedelivery.com/company/about/our-story.aspx
- group: operate
  title: ''
  type: FAQ
  url: https://www.cookiedelivery.com/company/about/faq.aspx
- group: operate
  title: ''
  type: Support
  url: https://www.cookiedelivery.com/company/contact-us.aspx
- group: company
  title: ''
  type: Blog
  url: https://www.cookiedelivery.com/blog
- group: company
  title: ''
  type: Careers
  url: https://www.cookiedelivery.com/company/careers.aspx
- group: start
  title: ''
  type: Login
  url: https://www.cookiedelivery.com/OnlineOrdering/ProfileHome
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cookiedelivery.com/footer-nav/terms-of-use.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cookiedelivery.com/footer-nav/privacy-policy.aspx
- group: other
  title: ''
  type: iOSApp
  url: https://apps.apple.com/us/app/tiffs-treats/id1092458498
- group: other
  title: ''
  type: AndroidApp
  url: https://play.google.com/store/apps/details?id=com.tiffstreats.cookiedelivery
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tiff's-treats-cookie-delivery
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/tiffstreats
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/tiffstreats
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/tiffstreats/
- group: other
  title: ''
  type: ContentSignal
  url: well-known/tiff-s-treats-content-signals.yml
coverage:
  checked: '2026-08-05'
  detail: Tiff's Treats is a bakery-storefront and same-day cookie-delivery operator, not a software vendor; cookiedelivery.com answers HTTP 200 with the same 1457-byte SPA shell for every unmatched path (openapi.json, llms.txt, every /.well-known/ document), and api.cookiedelivery.com resolves but returns a bare IIS 404 everywhere, so there is no developer program to gate or document.
  evidence:
  - status: 200
    url: https://www.cookiedelivery.com/openapi.json
  - status: 200
    url: https://www.cookiedelivery.com/zzz-no-such-path-9f8a7b
  - status: 404
    url: https://api.cookiedelivery.com/openapi.json
  - status: 404
    url: https://developer.cookiedelivery.com/
  - status: 200
    url: https://www.cookiedelivery.com/.well-known/agent-card.json
  - status: 200
    url: https://www.cookiedelivery.com/robots.txt
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: 'Tiff''s Treats is an Austin, Texas cookie company founded in 1999 by University of Texas students Tiffany Taylor and Leon Chen, built around warm, baked-to-order cookies delivered same-day. The company operates roughly 90 bakery-storefronts across Texas and the southern and western United States, combining walk-in retail with an owned delivery fleet, an online ordering platform at cookiedelivery.com, and iOS and Android ordering apps. Alongside consumer delivery it runs a substantial corporate gifting, catering, e-gift-card and special-events business, plus an "Elites" subscription membership and a rewards program. Tiff''s Treats has raised more than $50 million in outside investment, including a $25 million round led by Morgan Stanley Expansion Capital, and counts Andy Roddick, Brooklyn Decker, Kendra Scott and Dirk Nowitzki among its investors. It is a direct-to-consumer food and delivery operator, not a software vendor: it publishes no developer portal, no public API, and
  no machine-readable API contract.'
image: https://www.cookiedelivery.com/CookieDelivery/media/img/logo_header.svg
layout: provider
modified: '2026-08-05'
name: Tiff's Treats
nav: Providers
network: true
overview: 'Tiff''s Treats is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food and Beverage, Restaurant, Delivery, and E-Commerce.


  Tiff''s Treats'' developer surface includes FAQ, support, engineering blog, and 14 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Tiff S Treats Domain Security
  slug: tiff-s-treats-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tiff-s-treats
tags:
- Company
- Food and Beverage
- Restaurant
- Delivery
- E-Commerce
- Retail
- Gifting
- Consumer
- Subscription
- Loyalty
- Austin
- Texas
website: https://www.cookiedelivery.com/
---
