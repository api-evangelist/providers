---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hippo-harvest-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hippoharvest.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hippoharvest.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hippoharvest.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.hippoharvest.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Hippo-Harvest
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hippo-harvest-llms.txt
coverage:
  checked: '2026-08-22'
  detail: Hippo Harvest sells packaged organic salad greens grown in its own robotic greenhouses; its only web property is a Squarespace marketing site whose sitemap lists thirteen consumer pages (products, where-to-buy, a butter-lettuce sample request) and no developer surface at all, and every OpenAPI, GraphQL, MCP and /.well-known/ path on that host returns the site's 404.
  evidence:
  - status: 404
    url: https://www.hippoharvest.com/openapi.json
  - status: 404
    url: https://www.hippoharvest.com/llms.txt
  - status: 404
    url: https://www.hippoharvest.com/.well-known/agent-card.json
  - status: 200
    url: https://www.hippoharvest.com/sitemap.xml
  - status: 200
    url: https://api.github.com/orgs/hippo-harvest
  reason: not-a-software-company
  state: none
created: '2026-08-22'
description: 'Hippo Harvest is a controlled-environment agriculture company based in Pescadero, California, founded in 2019, that grows USDA-certified-organic leafy greens in modular greenhouses run by custom autonomous mobile robots and machine learning. Its closed-loop, direct-to-root watering and nutrient system is published by the company as using 92% less water, 55% less fertilizer and 94% less land than conventional field agriculture, while pricing to compete with field-grown product. Hippo Harvest sells packaged salad greens (spring mix, spinach, 50/50 blend, butter lettuce) into grocery retail rather than selling software: the robotics, computer vision and growing-control stack is internal operating infrastructure, not a product. It raised a $21M Series B led by Standard Investments in February 2024 and a $30M Series C led by Cox Farms in July 2026, and is permitting a 30-acre facility in Hollister, California. No public API, developer portal, SDK or machine-readable contract of
  any kind was found on any host the company controls.'
image: https://images.squarespace-cdn.com/content/635abb7ce3040e40049edb8f/2f8cd1c2-69e2-47d9-961d-7f8df305f83e/Hippo-Logo.png?content-type=image%2Fpng
layout: provider
modified: '2026-08-22'
name: Hippo Harvest
nav: Providers
network: true
overview: 'Hippo Harvest is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Controlled Environment Agriculture, Robotics, and Food and Beverage.


  Hippo Harvest''s developer surface includes support and 6 more developer resources.'
random_paper: 10
screenshot: https://raw.githubusercontent.com/api-evangelist/hippo-harvest/refs/heads/main/screenshots/hippo-harvest-2026-09-02T145734.png
security:
- kind: domain-security
  name: Hippo Harvest Domain Security
  slug: hippo-harvest-domain-security
  summary_line: TLSv1.3 · HSTS
slug: hippo-harvest
tags:
- Company
- Agriculture
- Controlled Environment Agriculture
- Robotics
- Food and Beverage
- Sustainability
- Consumer Packaged Goods
website: https://www.hippoharvest.com/
---
