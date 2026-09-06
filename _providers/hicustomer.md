---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://hicustomer.jp
coverage:
  checked: '2026-08-13'
  detail: hicustomer.jp is a registered .jp domain delegated to AWS Route 53 with a completely empty zone — no A, CNAME or MX answer for the apex or for any api/docs/app subdomain — so every probe fails at DNS, and the company's last remaining product, the "Arch by HiCustomer" digital sales room, was sold to Geniee, Inc. on 2024-09-13 and now ships as Geniee DSR.
  evidence:
  - status: 0
    url: https://hicustomer.jp/
  - status: 0
    url: https://api.hicustomer.jp/
  - status: 0
    url: https://hicustomer.jp/openapi.json
  - status: 0
    url: https://hicustomer.jp/.well-known/agent-card.json
  - status: 200
    url: https://web.archive.org/web/20240523185505id_/https://hicustomer.jp/.well-known/openid-configuration
  - status: 200
    url: https://geniee.co.jp/news/20240913/
  reason: defunct
  state: none
created: '2026-07-17'
description: HiCustomer (ハイカスタマー) was a Japanese Customer Success Management (CSM) SaaS built specifically for SaaS companies. Its platform aggregated customer data scattered across BI tools, CRMs, and chat tools to visualize product usage, communication history, revenue, and contract information in one place. Teams used configurable health-score rules to monitor account health across the customer lifecycle, and custom alerts to surface churn and upsell signals at the right moment, with time-series analysis to make customer-success outreach repeatable. The company also offered customer-success consulting, and later pivoted to a digital sales room product, "Arch by HiCustomer". On 2024-09-13 HiCustomer Inc. sold the Arch business to the Tokyo-listed adtech company Geniee, Inc. (TSE 6562), which absorbed it into GENIEE SFA/CRM and rebranded it Geniee DSR. As of this enrichment pass the hicustomer.jp domain no longer resolves to a live site (its authoritative AWS Route 53 zone is delegated
  but empty) and the product is discontinued; the last archived homepage (Oct 2024) is a STUDIO-built single-page "About the company" placeholder. No public developer API, documentation, SDK, or developer portal was ever published — the Wayback record for hicustomer.jp contains no /api, /docs, /developers, /pricing or /status path at any point in its history.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hicustomer.png
layout: provider
modified: '2026-08-13'
name: HiCustomer
nav: Providers
network: true
overview: HiCustomer is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customer Success, Customer Success Management, Software-as-a-Service, and Health Score.
random_paper: 20
slug: hicustomer
tags:
- Company
- Customer Success
- Customer Success Management
- Software-as-a-Service
- Health Score
- Churn Prediction
- Customer Data Platform
- Analytics
- Japan
- B2B SaaS
- Digital Sales Room
website: https://hicustomer.jp
---
