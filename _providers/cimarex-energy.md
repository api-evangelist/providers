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
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cimarex-energy/refs/heads/main/security/cimarex-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cimarex-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coterra.com/
- group: company
  title: ''
  type: SuccessorWebsite
  url: https://www.coterra.com/
- group: company
  title: ''
  type: News
  url: https://www.prnewswire.com/news-releases/cabot-oil--gas-and-cimarex-energy-complete-combination-forming-coterra-energy-301389768.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coterra.com/legal-notice/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cimarex-energy/refs/heads/main/llms/cimarex-energy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cimarex-energy-llms.txt
coverage:
  checked: '2026-09-05'
  detail: Cimarex Energy was fully absorbed into Coterra Energy in October 2021 and its own domain is now broken — cimarex.com still resolves through Cloudflare but the origin presents no valid certificate, so every path including the site root answers HTTP 526 rather than redirecting anywhere; no developer/api/docs/data subdomain of cimarex.com resolves in DNS, there is no cimarex GitHub organization, and no first-party package exists on npm or PyPI.
  evidence:
  - status: 526
    url: https://cimarex.com/
  - status: 526
    url: https://cimarex.com/.well-known/api-catalog
  - status: 404
    url: https://www.coterra.com/openapi.json
  - status: 403
    url: https://www.coterra.com/.well-known/security.txt
  - status: 404
    url: https://www.coterra.com/privacy-policy/
  reason: defunct
  state: none
created: '2025-02-21'
description: 'Cimarex Energy was an independent oil and gas exploration and production company headquartered in Denver, Colorado, with operations focused in the Permian Basin and the Mid-Continent. In October 2021 Cimarex Energy combined with Cabot Oil & Gas Corporation to form Coterra Energy (NYSE: CTRA). No public Cimarex-branded developer APIs exist; all current digital channels and any future API offerings are part of Coterra Energy.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cimarex-energy.png
layout: provider
modified: '2026-09-15'
name: Cimarex Energy
nav: Providers
network: true
overview: 'Cimarex Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Defunct, Energy, Merger, Oil and Gas, and Permian Basin.


  Cimarex Energy''s developer surface includes product news and 5 more developer resources.'
press:
- date: '2026-05-25'
  title: Cimarex Energy Co. News and Press Releases
  url: https://www.prnewswire.com/news/cimarex-energy-co./?page=2
- date: '2026-05-25'
  title: 'Devon Energy: An Oil Company With An AI Obsession'
  url: https://seekingalpha.com/article/4856912-devon-energy-an-oil-company-with-an-ai-obsession
- date: '2026-05-25'
  title: Cabot Oil & Gas Corporation and Cimarex Energy have ...
  url: https://www.linkedin.com/posts/coterra-energy_cabot-oil-gas-corporation-and-cimarex-energy-activity-6849697849010077696-IA6p
- date: '2026-05-25'
  title: Kimmeridge Calls for Overhaul at Coterra, Says 2021 ...
  url: https://energynow.com/2025/11/kimmeridge-calls-for-overhaul-at-coterra-says-2021-merger-a-failure/
- date: '2026-05-25'
  title: OAG Analytics Announces Strategic Partnership with Cimarex ...
  url: https://www.prnewswire.com/news-releases/oag-analytics-announces-strategic-partnership-with-cimarex-energy-300890540.html
random_paper: 10
screenshot: https://raw.githubusercontent.com/api-evangelist/cimarex-energy/refs/heads/main/screenshots/cimarex-energy-2026-06-20T174342.png
security:
- kind: domain-security
  name: Cimarex Energy Domain Security
  slug: cimarex-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cimarex-energy
tags:
- Defunct
- Energy
- Merger
- Oil and Gas
- Permian Basin
- Fortune 1000
website: https://www.coterra.com/
---
