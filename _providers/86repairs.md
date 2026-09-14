---
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/86repairs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.86repairs.com/
- group: build
  title: ''
  type: Packages
  url: packages/86repairs-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/86repairs-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/86repairs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/86repairs-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.86repairs.com/
- group: operate
  title: ''
  type: Support
  url: https://www.86repairs.com/customer-support
- group: operate
  title: ''
  type: HelpCenter
  url: https://intercom.help/86-repairs-customer-service/en/
- group: start
  title: ''
  type: Login
  url: https://portal.86repairs.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.86repairs.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.86repairs.com/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/86repairs
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@86Repairs
coverage:
  checked: '2026-09-05'
  detail: 86 Repairs ships its repair-management product only as an end-user web portal and mobile apps — no developer subdomain resolves (docs., developer., developers.86repairs.com all fail DNS), the sitemap lists no API, developer or integrations page, and the private portal backend at eightysix-api.86repairs.com returns a real JSON 404 for /openapi.json, /swagger.json, /graphql and every .well-known path while serving only /health.
  evidence:
  - status: 404
    url: https://eightysix-api.86repairs.com/openapi.json
  - status: 404
    url: https://eightysix-api.86repairs.com/graphql
  - status: 200
    url: https://eightysix-api.86repairs.com/health
  - status: 0
    url: https://docs.86repairs.com/
  - status: 0
    url: https://developer.86repairs.com/
  - status: 403
    url: https://api.86repairs.com/
  - status: 200
    url: https://www.86repairs.com/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: '86 Repairs is a restaurant equipment repair and maintenance (R&M) management platform founded in 2018 in Chicago by Daniel Estrada and Joe Gallagher. It manages the repair lifecycle for restaurant operators — 24/7 intake and troubleshooting, warranty verification, dispatch to a vetted service provider network, preventative maintenance scheduling, equipment and asset inventory, invoice assurance and R&M spend analytics — and is used by operators and franchisees of brands including McDonald''s, Wendy''s, Taco Bell, Jersey Mike''s, Five Guys and Wingstop. The product is delivered as an end-user web portal (portal.86repairs.com) and iOS/Android mobile apps, backed by a private NestJS service at eightysix-api.86repairs.com; it is not offered as a developer platform. Parts Town, the Addison, Illinois OEM foodservice parts distributor, acquired 86 Repairs in June 2026 to connect parts availability with repair and service workflows. As of this profile 86 Repairs publishes no public
  API: no developer portal, no API reference, no OpenAPI/AsyncAPI/GraphQL contract, no SDK or package on any public registry, no webhook catalog, no MCP server and no A2A agent card were found on any host it controls.'
image: https://www.86repairs.com/hubfs/86%20Repairs%20for%20Facilities%20Managers%20%281200%20x%20630%20px%29%20%281%29.png
layout: provider
modified: '2026-09-05'
name: 86 Repairs
nav: Providers
network: true
overview: '86 Repairs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Restaurants, Foodservice, Facilities Management, Maintenance, and Field Service Management.


  86 Repairs'' developer surface includes engineering blog, support, YouTube channel, and 11 more developer resources.'
plans:
- name: 86Repairs Plans Pricing
  plan_count: 0
  slug: 86repairs-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: 86Repairs Rate Limits
  slug: 86repairs-rate-limits
security:
- kind: domain-security
  name: 86Repairs Domain Security
  slug: 86repairs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 86repairs
tags:
- Restaurants
- Foodservice
- Facilities Management
- Maintenance
- Field Service Management
- Equipment
- Asset Management
- Hospitality
- Vendor Management
- No Developer Program
website: https://www.86repairs.com/
---
