---
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://agripedia.co.jp/
- group: company
  title: ''
  type: Newsroom
  url: https://agripedia.co.jp/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agripedia.co.jp/news/detail/privacy_policy
- group: company
  title: ''
  type: Blog
  url: https://note.com/agripedia
- group: company
  title: ''
  type: BlogRSS
  url: https://note.com/agripedia/rss
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AgriPedia
- group: company
  title: ''
  type: Careers
  url: https://herp.careers/careers/companies/agripedia
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/agripedia/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agripedia-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agripedia-llms.txt
coverage:
  checked: '2026-09-13'
  detail: 'Agripedia ships software only as closed end-user applications: its corporate site is a two-route Nuxt SPA (sitemap lists exactly / and /news) with no developer, docs, portal or integration link anywhere, kanri.agripedia.co.jp (AP管理システム) answers every path with a 401 "please register or sign in" body or a 302 to /users/sign_in, and connect.agripedia.co.jp calls itself "AgriPedia 社内向けSCMシステム" — an internal supply-chain tool — in its own meta description, so there is no public API being marketed and nothing gated behind a sales form either.'
  evidence:
  - status: 200
    url: https://agripedia.co.jp/
  - status: 200
    url: https://agripedia.co.jp/sitemap-static.xml
  - status: 200
    url: https://agripedia.co.jp/.well-known/zz-control-9f3a
  - status: 404
    url: https://material-sales.agripedia.co.jp/openapi.json
  - status: 404
    url: https://material-sales.agripedia.co.jp/graphql
  - status: 404
    url: https://material-sales.agripedia.co.jp/llms.txt
  - status: 404
    url: https://material-sales.agripedia.co.jp/.well-known/agent-card.json
  - status: 404
    url: https://material-sales.agripedia.co.jp/.well-known/api-catalog
  - status: 401
    url: https://kanri.agripedia.co.jp/openapi.json
  - status: 302
    url: https://kanri.agripedia.co.jp/api-docs
  - status: 200
    url: https://connect.agripedia.co.jp/openapi.json
  - status: 404
    url: https://registry.npmjs.org/agripedia
  reason: no-developer-program
  state: none
created: '2026-09-13'
description: Agripedia (アグリぺディア株式会社) is a Tokyo agricultural technology company, founded in June 2019 and headquartered in Nishi-Gotanda, Shinagawa-ku, that connects mid- and large-scale Japanese farms and production areas with food-service and food-manufacturing buyers. It supports growers from GAP certification through to the sale of the certified produce, runs a B2B direct-sales channel for GAP-certified commercial agricultural products, sells crop-protection materials and fertilizer, and operates its own production management system for cultivation history and traceability. It holds JGAP group certification (March 2023) and is a GAP partner of Japan's Ministry of Agriculture, Forestry and Fisheries. Its software reaches farms, buyers and staff as closed, credentialed web applications; the company publishes no developer program, no public API, and no machine-readable contract on any host it operates.
image: https://storage.googleapis.com/production-os-assets/assets/b88741c2-9769-459d-8a72-ec63d33322a4
layout: provider
modified: '2026-09-13'
name: Agripedia
nav: Providers
network: true
overview: 'Agripedia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, AgTech, Farm Management, and Food Supply Chain.


  Agripedia''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 10
security:
- kind: domain-security
  name: Agripedia Domain Security
  slug: agripedia-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agripedia
tags:
- Company
- Agriculture
- AgTech
- Farm Management
- Food Supply Chain
- Traceability
- GAP Certification
- B2B Marketplace
- Japan
website: https://agripedia.co.jp/
---
