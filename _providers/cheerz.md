---
api_count: 0
artifact_total: 0
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
random_paper: 45
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
---
