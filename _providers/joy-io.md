---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-17'
  detail: Joy ships software only as an end-user product — a manager web/mobile app plus a hosted booking widget — and publishes no developer portal, API reference, OpenAPI, webhook catalogue or SDK; the private backend its own app calls, manager-api.privateaser.com (read from https://app.joy.io/config.js), returns HTTP 404 on /openapi.json and every other spec path and is gated by an AWS Cognito user pool, and the 90-article help-center index at faq.joy.io/llms.txt never uses the word "api".
  evidence:
  - status: 404
    url: https://manager-api.privateaser.com/openapi.json
  - status: 200
    url: https://joy.io/sitemap.xml
  - status: 200
    url: https://faq.joy.io/llms.txt
  - status: 200
    url: https://api.github.com/orgs/Privateaser-Joy/repos?per_page=100
  reason: no-developer-program
  state: none
created: '2026-08-17'
description: 'Joy is a French SaaS platform for bars, restaurants and venues that turns group and event enquiries into confirmed bookings. Founded in 2014 as Privateaser, the company now runs a two-sided business: privateaser.com, the group-venue marketplace that captures demand, and Joy, the manager-facing application (web plus iOS/Android) where an establishment centralises requests from Google, Instagram, its own website, WhatsApp and Privateaser, then works them through a unified calendar and messaging inbox, an SEO/GEO-optimised event showcase page, a virtual phone assistant, quotes, French-compliant invoicing, and Stripe-backed deposits and prepayments. Joy reports more than 3,000 partner establishments and over EUR100M in bookings managed in 2025. It publishes no public API, SDK, webhook catalogue or developer portal; the only integration surfaces it documents for customers are an embeddable iframe booking form, Reserve-with-Google, and a one-click reservation copy into Zenchef.'
image: https://joy.io/og-image.png
layout: provider
modified: '2026-08-17'
name: Joy (ex-Privateaser)
nav: Providers
network: true
random_paper: 3
slug: joy-io
tags:
- Company
- Marketplace
- Reservations
- Bookings
- Restaurants
- Hospitality
- Events
- SaaS
- France
---
