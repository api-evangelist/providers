---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-06'
  detail: Before Brands was absorbed into Nestle Health Science — beforebrands.com now delegates to nestle.com nameservers, resolves to the sitedetour.com parking host and returns 404, while spoonfulone.com 301s to nestlehealthscience.com whose SpoonfulOne brand page itself 301s to a generic brand index, so there is no company surface left to profile.
  evidence:
  - status: 404
    url: http://beforebrands.com/
  - status: 301
    url: https://spoonfulone.com/
  - status: 301
    url: https://www.nestlehealthscience.com/brands/spoonfulone
  - status: 404
    url: http://beforebrands.com/openapi.json
  - status: 404
    url: http://beforebrands.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/beforebrands
  reason: defunct
  state: none
created: '2026-08-06'
description: 'Before Brands, Inc. was a Menlo Park, California science-based food and nutrition company founded on Stanford allergy research by Dr. Kari Nadeau, best known for SpoonfulOne — a consumer early-allergen-introduction product line that blended sixteen commonly allergenic proteins into daily servings for infants and toddlers. Nestle Health Science took a minority stake plus ex-US licensing rights in 2019 and later absorbed the business outright. It was a consumer packaged goods company, not a software company: it never operated a developer program, published no API, SDK or webhook surface, and its own domain is now controlled by Nestle and no longer serves a site.'
layout: provider
modified: '2026-08-06'
name: Before Brands
nav: Providers
network: true
random_paper: 63
slug: before-brands
tags:
- Company
- Food and Beverage
- Consumer Packaged Goods
- Nutrition
- Health
- Allergy
- Infant Nutrition
- Acquired
---
