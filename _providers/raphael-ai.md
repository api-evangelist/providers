---
api_count: 1
apis:
- description: Consumer AI image and video generation product. No public API is offered yet (stated as coming in the near future); the only machine-readable surface is an llms.txt product/marketing discovery index.
  name: Raphael AI
  slug: raphael-ai
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://raphael.app
- group: commercial
  title: ''
  type: Pricing
  url: https://raphael.app/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://raphael.app/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://raphael.app/tos
coverage:
  checked: '2026-09-13'
  detail: Raphael AI is a consumer AI image/video web app; its own pricing FAQ states "we don't have a public API at the moment but will be offering one in the near future," and no API host exists (api.raphael.app is NXDOMAIN). The only machine-readable surface is a marketing llms.txt.
  evidence:
  - status: 200
    url: https://raphael.app/pricing
  - status: 404
    url: https://raphael.app/openapi.json
  - status: 404
    url: https://raphael.app/mcp
  - status: 404
    url: https://raphael.app/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-09-12'
description: A free, no-signup AI image and video generator (text-to-image, image-to-image, image editing, outpaint, background removal, text-to-video, image-to-video) that aggregates multiple underlying models (Nano Banana, Seedream, GPT Image, Veo, Kling and more). Currently exposes an llms.txt product/marketing index but no public API, MCP server, or agent skills; the provider states a public API is planned for the near future.
layout: provider
modified: '2026-09-13'
name: Raphael AI
nav: Providers
network: true
overview: 'Raphael AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, image generation, text-to-image, image-to-image, and image editing.


  Raphael AI''s developer surface includes pricing and 3 more developer resources.'
plans:
- name: Raphael Ai Plans Pricing
  plan_count: 4
  slug: raphael-ai-plans-pricing
random_paper: 14
slug: raphael-ai
tags:
- AI
- image generation
- text-to-image
- image-to-image
- image editing
- video generation
- generative media
- model aggregator
website: https://raphael.app
---
