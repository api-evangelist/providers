---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-06'
  detail: 'Beautylish runs a first-party beauty storefront with no developer surface at all: developer.beautylish.com and developers.beautylish.com do not resolve, every /.well-known/ path and /llms.txt on www.beautylish.com return 404, and the only public JSON on the domain is /rest/interview-product/list, a static fixture of fake "Acme/Hooli" products served for their software-engineering hiring exercise rather than a product API.'
  evidence:
  - status: 404
    url: https://www.beautylish.com/llms.txt
  - status: 404
    url: https://www.beautylish.com/.well-known/agent-card.json
  - status: 404
    url: https://www.beautylish.com/.well-known/security.txt
  - status: 200
    url: https://www.beautylish.com/rest/interview-product/list
  - status: 200
    url: https://www.beautylish.com/help
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: 'Beautylish is a San Francisco based online beauty retailer and community, founded in 2010 by Nils Johnson, Vu Nguyen and Sameer Iyengar. It began as a community where beauty enthusiasts shared tutorials, reviews and product knowledge, and launched its own e-commerce storefront in 2012. Beautylish curates makeup, skincare, hair, fragrance, nails, bath and body, wellness and tool brands from around the world, pairs them with editorial content and makeup-artist guidance, and operates its own fulfillment, rewards (Beautylish Rewards), flexible payments and Zero Day Delivery programs. The company runs a first-party storefront rather than a developer platform: as of this profile it publishes no developer portal, no public API reference, no OpenAPI or other machine-readable contract, and no SDKs. Its public partner surface is a ShareASale/Awin affiliate program rather than an API.'
layout: provider
modified: '2026-08-06'
name: Beautylish
nav: Providers
network: true
random_paper: 65
slug: beautylish
tags:
- Company
- E-Commerce
- Retail
- Beauty
- Cosmetics
- Consumer
- Marketplace
- Direct to Consumer
---
