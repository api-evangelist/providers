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
artifact_total: 3
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/energy-transfer
- group: other
  title: ''
  type: Successor
  url: https://www.energytransfer.com
- group: start
  title: ''
  type: Successor Developer Portal
  url: https://dev.messenger.energytransfer.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/energy-transfer-equity-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/energy-transfer-equity-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/energy-transfer-equity-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/energy-transfer-equity-rate-limits.yml
coverage:
  checked: '2026-09-06'
  detail: Energy Transfer Equity, L.P. was dissolved into Energy Transfer LP in October 2018 and serves no host of its own; its legacy corporate domain energytransferequity.com now answers from GoDaddy NameFind parking nameservers with a 114-byte for-sale lander on every path, including a negative-control path that cannot exist.
  evidence:
  - status: 200
    url: https://energytransferequity.com/.well-known/ete-negative-control-7f3ab91c.json
  - status: 200
    url: https://energytransferequity.com/llms.txt
  - status: 404
    url: https://dev.messenger.energytransfer.com/openapi.json
  - status: 403
    url: https://www.energytransfer.com/.well-known/agent-card.json
  reason: defunct
  state: none
created: '2026-03-24'
description: 'Energy Transfer Equity, L.P. (ETE) was a master limited partnership that owned and operated a diverse portfolio of midstream energy assets. In October 2018, ETE merged with its operating subsidiary Energy Transfer Partners (ETP) to form a single publicly traded partnership, Energy Transfer LP (NYSE: ET). All developer resources, including the Messenger+ API for pipeline messaging and gas scheduling, are now provided under the Energy Transfer LP brand.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/energy-transfer-equity.png
layout: provider
modified: '2026-09-06'
name: Energy Transfer Equity
nav: Providers
network: true
overview: Energy Transfer Equity is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Pipelines, Midstream, Defunct Entity, and Fortune 100.
plans:
- name: Energy Transfer Equity Plans Pricing
  plan_count: 0
  slug: energy-transfer-equity-plans-pricing
press:
- date: '2026-05-25'
  title: WILLIAMS RIDES AI GAS BOOM America's race to build artificial ...
  url: https://www.facebook.com/tribunephl/posts/williams-rides-ai-gas-boomamericas-race-to-build-artificial-intelligence-is-now-/1388683783308038/
- date: '2026-05-25'
  title: Energy Transfer details vast midstream network in 10-K
  url: https://www.stocktitan.net/sec-filings/ET/10-k-energy-transfer-lp-files-annual-report-92d1558c35ce.html
- date: '2026-05-25'
  title: Energy Transfer LP Common Units (ET) Stock Price, Quote ...
  url: https://seekingalpha.com/symbol/ET
- date: '2026-05-25'
  title: Energy Transfer Equity LP files to offer up to $1 billion of ...
  url: https://www.reuters.com/article/idUSFWN1FT10C/
- date: '2026-05-25'
  title: Power demand is skyrocketing from AI, electrification and ...
  url: https://www.facebook.com/WilliamsEnergyCo/posts/power-demand-is-skyrocketing-from-ai-electrification-and-industrial-reshoring-bu/904918505241219/
random_paper: 14
rate_limits:
- limit_count: 0
  name: Energy Transfer Equity Rate Limits
  slug: energy-transfer-equity-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/energy-transfer-equity/refs/heads/main/screenshots/energy-transfer-equity-2026-06-20T180709.png
security:
- kind: domain-security
  name: Energy Transfer Equity Domain Security
  slug: energy-transfer-equity-domain-security
  summary_line: TLSv1.3
slug: energy-transfer-equity
tags:
- Energy
- Pipelines
- Midstream
- Defunct Entity
- Fortune 100
---
