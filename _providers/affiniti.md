---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-09-12'
  detail: 'Affiniti — trading today as Extu after the OneAffiniti / Incentive Solutions merger — sells a through-channel marketing and incentive SaaS platform as an end-user product and a managed service, and publishes no developer program of any kind: its own llms.txt indexes 661 pages and its three XML sitemaps every public URL, and neither names a developer portal, API reference, SDK, webhook or specification, while every OpenAPI/GraphQL/MCP/agent-card path probed on extu.com, oneaffiniti.com, app.extu.com and the cms-api.extu.com backend the Partner Experience app actually calls returns 404 (a Laravel "route could not be found" JSON body on cms-api, including for a random control path). The only machine-readable documents any Extu host serves are the OpenID Connect discovery documents for the two Auth0 tenants behind its CMS and partner logins, which are sign-in metadata for humans, not an API contract.'
  evidence:
  - status: 200
    url: https://extu.com/llms.txt
  - status: 200
    url: https://extu.com/sitemap_index.xml
  - status: 200
    url: https://extu.com/robots.txt
  - status: 404
    url: https://cms-api.extu.com/openapi.json
  - status: 404
    url: https://cms-api.extu.com/swagger.json
  - status: 404
    url: https://cms-api.extu.com/api-docs
  - status: 404
    url: https://cms-api.extu.com/api/v1
  - status: 404
    url: https://extu.com/.well-known/agent-card.json
  - status: 404
    url: https://extu.com/.well-known/agent.json
  - status: 404
    url: https://extu.com/.well-known/api-catalog
  - status: 404
    url: https://extu.com/.well-known/security.txt
  - status: 404
    url: https://oneaffiniti.com/apis.json
  - status: 200
    url: https://cms-login.extu.com/.well-known/openid-configuration
  - status: 200
    url: https://pexp-login.extu.com/.well-known/openid-configuration
  - status: 404
    url: https://extu.com/.well-known/affiniti-negative-control-7f3ab91c.json
  reason: no-developer-program
  state: none
created: '2026-09-12'
description: 'Affiniti is the channel-marketing software company founded in Sydney, Australia by Joel Montgomery and listed under that name on the EquityZen secondary market; it traded for most of its life as OneAffiniti and, after Capstreet-backed Incentive Solutions acquired it in April 2021, the combined business rebranded to Extu in September 2023, the brand its product and every live web property carry today. It sells a through-channel marketing automation and channel incentive platform that suppliers and distributors use to run co-branded campaigns, content syndication, rewards, rebates, SPIFFs and attribution for their reseller partners in technology, building, automotive, energy, insurance and medical channels. It is a SaaS product and managed service: its own llms.txt and full XML sitemap list no developer portal, API reference, SDK or machine-readable contract of any kind.'
image: https://extu.com/wp-content/uploads/2023/05/Extu_Logo_FullColor.png
layout: provider
modified: '2026-09-12'
name: Affiniti
nav: Providers
network: true
random_paper: 2
slug: affiniti
tags:
- Company
- Channel Marketing
- Marketing Automation
- Through-Channel Marketing
- Partner Marketing
- Incentives
- Loyalty
- Rebates
- Rewards
- B2B SaaS
---
