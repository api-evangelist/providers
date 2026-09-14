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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hertz-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hertz-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hertz
- group: company
  title: ''
  type: Website
  url: https://www.hertz.com
- group: operate
  title: ''
  type: Support
  url: https://www.hertz.com/supporthub/
- group: company
  title: ''
  type: Blog
  url: https://www.hertz.com/us/en/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hertz.com/rentacar/navigation/templates/legalView.jsp
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hertz.com/rentacar/privacypolicy/index.jsp?targetPage=privacyPolicyView.jsp
coverage:
  checked: '2026-09-13'
  detail: Hertz's own Travel Agent "GDS Tools" page hands integrators quick-reference guides for Amadeus, Galileo by Travelport, SABRE Travel Network and Worldspan instead of publishing an API reference, and the only developer-shaped hostname, developers.hertz.com, is a dangling Akamai CNAME whose certificate does not match the name.
  evidence:
  - status: 200
    url: https://www.hertz.com/rentacar/misc/index.jsp?targetPage=GDSindex_TA.jsp
  - status: 0
    url: https://developers.hertz.com/
  - status: 404
    url: https://api.hertz.com/openapi.json
  - status: 403
    url: https://api.hertz.io/openapi.json
  - status: 404
    url: https://www.hertz.com/.well-known/api-catalog
  reason: marketplace-only
  state: gated
created: '2026-03-21'
description: 'The Hertz Corporation is a global vehicle rental company operating the Hertz, Dollar and Thrifty brands from airport and neighbourhood locations in roughly 160 countries, renting cars, vans and trucks to leisure, corporate, government and rideshare customers and running the Hertz Gold Plus Rewards loyalty programme. Hertz publishes no public developer programme: probing on 2026-09-13 found no developer portal, no OpenAPI or other machine-readable contract, no SDKs, no first-party MCP server and no /.well-known/ discovery documents on any Hertz host. Third-party integrators reach Hertz rates and availability through the global distribution systems — Amadeus, Sabre and Travelport — which Hertz''s own Travel Agent GDS Tools page directs them to, rather than through a first-party API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hertz.png
layout: provider
modified: '2026-09-13'
name: Hertz
nav: Providers
network: true
overview: 'Hertz is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Car Rental, Vehicle Rental, Travel, and Mobility.


  Hertz''s developer surface includes support, engineering blog, and 6 more developer resources.'
random_paper: 11
security:
- kind: domain-security
  name: Hertz Domain Security
  slug: hertz-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hertz
tags:
- Fortune 500
- Car Rental
- Vehicle Rental
- Travel
- Mobility
- Transportation
- Fleet Management
website: https://www.hertz.com
---
