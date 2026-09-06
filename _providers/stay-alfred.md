---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-29'
  detail: Stay Alfred Inc. permanently closed on 20 May 2020 and the stayalfred.com host is no longer controlled by the company — every path, including /openapi.json and every /.well-known/ path, returns a Cloudflare 301 into a rotating set of unrelated third-party domains, while api./developer./docs./app.stayalfred.com are all NXDOMAIN and no GitHub organization or package-registry namespace ever existed.
  evidence:
  - status: 301
    url: https://www.stayalfred.com/
  - status: 301
    url: https://www.stayalfred.com/openapi.json
  - status: 301
    url: https://www.stayalfred.com/.well-known/agent-card.json
  - status: 301
    url: https://www.stayalfred.com/.well-known/security.txt
  - status: 200
    url: https://www.stayalfred.com/robots.txt
  - status: 404
    url: https://api.github.com/orgs/stayalfred
  - status: 404
    url: https://registry.npmjs.org/stayalfred
  - status: 403
    url: https://forgeglobal.com/stay-alfred_stock/
  reason: defunct
  state: none
created: '2026-08-29'
description: 'Stay Alfred Inc. was a Spokane, Washington short-term-rental and hospitality operator that pioneered the "travel apartment" — full apartments in walkable downtown cores, leased in bulk from multifamily building owners and operated with hotel-style consistency, cleaning and guest support. Founded in 2011 by Jordan Allen, who was named EY Entrepreneur Of The Year for the Pacific Northwest in 2019, the company grew to roughly 2,000-2,500 units across 28 to 33 U.S. markets including Denver, San Diego, Miami, New Orleans and Nashville, hosted around half a million guests, and employed more than 230 people. It raised approximately $62M in total venture funding, headlined by a $47M Series B in October 2018 led by Chicago real-estate technology fund Nine Four Ventures. Distribution ran through its own consumer booking site and the major online travel agencies, so Stay Alfred was an API CONSUMER rather than an API publisher; it never operated a developer program, public API, SDK, webhook
  catalog or machine-readable specification. COVID-19 ended it: the company closed every property nationwide from 1 April 2020, a rescue funding round was withdrawn at the last minute, and on 20 May 2020 Stay Alfred announced it would close permanently, winding down through mid-2020 while it had been on track for roughly $100M in revenue that year. The stayalfred.com domain is still on its original 2013 registration but is no longer controlled by the company: it is privacy-shielded, Cloudflare-hosted, and every path now 301-redirects into a rotating chain of unrelated third-party sites. This profile is retained as a historical record; there is no API surface to enrich.'
layout: provider
modified: '2026-08-29'
name: Stay Alfred
nav: Providers
network: true
overview: Stay Alfred is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Travel, Hospitality, and Lodging.
random_paper: 3
slug: stay-alfred
tags:
- Company
- Defunct
- Travel
- Hospitality
- Lodging
- Short-Term Rental
- Vacation Rental
- Corporate Housing
- Accommodations
- Real-Estate
- Consumer
---
