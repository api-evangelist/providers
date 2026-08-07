---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-07'
  detail: Bloom & Wild runs its own commerce platform but ships no developer product at all — no portal, no docs, no spec, and corporate/bulk gifting is quoted through a contact form and an account manager rather than an API; the live application backend at api.bloomandwild.com answers a JSON error envelope on every discovery path, including /openapi.json.
  evidence:
  - status: 404
    url: https://api.bloomandwild.com/openapi.json
  - status: 404
    url: https://api.bloomandwild.com/graphql
  - status: 404
    url: https://www.bloomandwild.com/.well-known/agent-card.json
  - status: 404
    url: https://www.bloomandwild.com/.well-known/api-catalog
  - status: 200
    url: https://www.bloomandwild.com/llms.txt
  - status: 200
    url: https://www.bloomandwild.com/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2026-08-07'
description: 'Bloom & Wild is a British direct-to-consumer online florist and gifting brand founded in 2013 by Aron Gelbard and Ben Stanway, best known for pioneering letterbox flowers — bouquets packed flat so they fit through a UK letterbox — alongside hand-tied bouquets, plants, gift sets, gift cards and recurring flower subscriptions. Bloom & Wild Group trades as Bloom & Wild in the United Kingdom, Ireland, Germany and Austria, and operates the sister brands bloomon (Netherlands, Belgium, Denmark) and Bergamotte (France) on separate storefronts. The group is a certified B Corp and runs its own commerce platform — a Ruby on Rails backend fronted by Kong, an Angular multi-brand web app and native iOS and Android clients, on AWS and GCP. Bloom & Wild publishes NO public developer portal, no API documentation, no OpenAPI or other machine-readable API description, and no partner or corporate-gifting API: business and bulk gifting is transacted through a contact form, an account manager and
  invoicing, not through a programmatic surface. The application backends at api.bloomandwild.com and capi.bloomandwild.com are live but private to the brand''s own clients and undocumented. What the group does publish for machines is narrow but real: an llms.txt on the UK and German storefronts that routes assistants to the correct market by delivery destination and even ships an optional agent widget specification, and an RFC 9116 security.txt served across every group storefront.'
image: https://www.bloomandwild.com/assets/branded-icons/favicons/favicon-192x192.png
layout: provider
modified: '2026-08-07'
name: Bloom & Wild
nav: Providers
network: true
random_paper: 42
slug: bloom--wild
tags:
- Company
- E-commerce
- Retail
- Flowers
- Gifting
- Direct to Consumer
- Subscriptions
- Consumer Goods
- Logistics
- United Kingdom
- B Corp
---
