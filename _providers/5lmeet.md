---
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: http://www.5lmeet.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/5lmeet-stock
- group: auth
  title: ''
  type: DomainSecurity
  url: security/5lmeet-domain-security.yml
coverage:
  checked: '2026-09-05'
  detail: '5Lmeet is a Beijing co-working and co-living property operator whose only shipped software is an end-user iPad visitor-management app for its own front desks — there is no developer portal, no API, and no machine-readable contract anywhere: all 22 discovery and /.well-known/ paths returned genuine IIS 404s on www.5lmeet.com (a negative-control path 404''d too, so the host does not echo), and api.5lmeet.com resolves to 101.201.52.28 but accepts no connection on port 80 or 443.'
  evidence:
  - status: 200
    url: http://www.5lmeet.com/
  - status: 404
    url: http://www.5lmeet.com/openapi.json
  - status: 404
    url: http://www.5lmeet.com/.well-known/security.txt
  - status: 404
    url: http://www.5lmeet.com/.well-known/agent-card.json
  - status: 404
    url: http://www.5lmeet.com/llms.txt
  - status: 404
    url: http://5lmeet.com/apis.json
  - status: 0
    url: http://api.5lmeet.com/
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: '5Lmeet (Chinese brand 共享际, operated by 优享创智 / UR Community) is a Beijing-based urban space operator founded in December 2015 by Dr. Mao Daqing, the former vice-chairman of China Vanke and founder of Ucommune. It runs an "urban renewal and spatial reconstruction" model that blends co-working, co-living, food and beverage, retail, fitness and cultural programming into single mixed-use compounds — the name stands for livable, linked, liberal, lively and landscape. Its Dongsi compound in Beijing pairs a basement co-working floor with a cafe and bakery, a gym, the Hatchery food incubator, the Unread bookstore, a 24-hour convenience store, residential units and a rooftop garden. The company raised roughly RMB 400 million in October 2016 and a USD 14.55 million Series B in early 2017 led by GIC, Singapore''s sovereign wealth fund, alongside Kaifeng Culture Tourism Investment Group, and is valued in the secondary market rather than publicly listed. 5Lmeet is a real-estate and hospitality
  operator, not a software vendor: the only software it has published is an end-user iPad visitor-management app for its own front desks, and it operates no developer program, public API, SDK or machine-readable contract of any kind.'
layout: provider
modified: '2026-09-05'
name: 5Lmeet
nav: Providers
network: true
overview: 5Lmeet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Coworking, Co-Living, and Workspace.
random_paper: 0
security:
- kind: domain-security
  name: 5Lmeet Domain Security
  slug: 5lmeet-domain-security
  summary_line: no transport/DNS hardening detected
slug: 5lmeet
tags:
- Company
- Real Estate
- Coworking
- Co-Living
- Workspace
- Property Technology
- Hospitality
- Urban Development
- China
website: http://www.5lmeet.com/
---
