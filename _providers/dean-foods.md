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
artifact_total: 1
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dean-foods
- group: other
  title: ''
  type: Acquirer
  url: https://www.dfamilk.com/
- group: other
  title: ''
  type: ShutdownNotice
  url: https://www.prnewswire.com/news-releases/dean-foods-company-initiates-voluntary-reorganization-with-new-financial-support-from-existing-lenders-300956285.html
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dean-foods-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dean-foods-llms.txt
coverage:
  checked: '2026-09-05'
  detail: Dean Foods filed Chapter 11 on 2019-11-12 and its plants and brands were sold to Dairy Farmers of America in May 2020; the company has no operating surface left to profile — deanfoods.com is now registered to Dairy Farmers of America, Inc., serves no HTTPS at all (the TLS handshake to port 443 aborts with "tlsv1 alert internal error", so every https probe returns 0 rather than a status code), and over plain HTTP answers 301 to https://www.dfamilk.com/ for every path including /openapi.json, /llms.txt and all seven /.well-known/ paths, while no api., developer., docs. or portal. subdomain resolves on either deanfoods.com or dfamilk.com and no GitHub organization exists under any spelling of the name.
  evidence:
  - status: 0
    url: https://deanfoods.com/openapi.json
  - status: 0
    url: https://deanfoods.com/.well-known/agent-card.json
  - status: 301
    url: http://deanfoods.com/
  - status: 404
    url: https://www.dfamilk.com/.well-known/agent-card.json
  - status: 404
    url: https://www.dfamilk.com/zzz-soft404-control-probe
  - status: 404
    url: https://api.github.com/orgs/deanfoods
  reason: defunct
  state: none
created: '2025-01-01'
description: Dean Foods was a leading U.S. food and beverage company and one of the largest processors and direct-to-store distributors of fresh fluid milk and other dairy products. After filing for Chapter 11 bankruptcy in 2019, most of Dean Foods' assets were acquired by Dairy Farmers of America (DFA) in 2020. Dean Foods no longer operates as an independent company and does not publish a public developer API; surviving brands are now managed under DFA. This profile is retained for historical reference.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dean-foods.png
layout: provider
modified: '2026-09-05'
name: Dean Foods
nav: Providers
network: true
overview: Dean Foods is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Acquired, Beverages, Dairy, Defunct, and Food and Beverage.
press:
- date: '2026-05-25'
  title: Dean Foods
  url: https://greenamerica.org/dean-foods
- date: '2026-05-25'
  title: Dean Foods opts for internal transformation plan after ...
  url: https://www.just-food.com/news/dean-foods-opts-for-internal-transformation-plan-after-strategic-review/
- date: '2026-05-25'
  title: Dean Foods Completes Sale to DFA | Dairy News
  url: https://www.lancasterfarming.com/farming-news/dairy/dean-foods-completes-sale-to-dfa/article_cc082519-cf62-522d-8841-bb0b497557c0.html
- date: '2026-05-25'
  title: 'Dean Foods goes bust thanks to a fatal error: shying away ...'
  url: https://agfundernews.com/dean-foods-goes-bust-thanks-to-a-fatal-error-shying-away-from-alt-milk
- date: '2026-05-25'
  title: Dean Foods Company Initiates Voluntary Reorganization ...
  url: https://www.prnewswire.com/news-releases/dean-foods-company-initiates-voluntary-reorganization-with-new-financial-support-from-existing-lenders-300956285.html
random_paper: 5
screenshot: https://raw.githubusercontent.com/api-evangelist/dean-foods/refs/heads/main/screenshots/dean-foods-2026-06-20T175743.png
security:
- kind: domain-security
  name: Dean Foods Domain Security
  slug: dean-foods-domain-security
  summary_line: DNSSEC · DMARC
slug: dean-foods
tags:
- Acquired
- Beverages
- Dairy
- Defunct
- Food and Beverage
- Milk
- Fortune 500
---
