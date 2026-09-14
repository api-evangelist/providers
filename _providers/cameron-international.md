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
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cameron-international-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cameron-international-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cameron
- group: company
  title: ''
  type: Website
  url: https://www.slb.com/legacy-companies/cameron-products
- group: other
  title: ''
  type: ParentCompany
  url: https://www.slb.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.delfi.slb.com/
- group: other
  title: ''
  type: DELFI
  url: https://www.software.slb.com/delfi/what-is-delfi
- group: company
  title: ''
  type: News
  url: https://www.slb.com/news
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cameron-international-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cameron-international-security.txt
- group: auth
  title: ''
  type: Security
  url: security/cameron-international-vulnerability-disclosure.yml
coverage:
  checked: '2026-09-05'
  detail: Cameron International no longer exists as an operating company — its own domain www.c-a-m.com and the cameron.slb.com subdomain both 301 to SLB's /legacy-companies/cameron-products page, and STEP 0b contract discovery (openapi/swagger/api-docs, GraphQL, MCP tools/list, agent-card and OGC probes) returned clean 404s on every Cameron and SLB host including the DELFI developer portal, which serves only an Angular single-page shell.
  evidence:
  - status: 301
    url: https://www.c-a-m.com/
  - status: 301
    url: https://cameron.slb.com/
  - status: 404
    url: https://www.slb.com/products-and-services/delivering-domain-expertise/surface/cameron-surface
  - status: 404
    url: https://developer.delfi.slb.com/openapi.json
  - status: 404
    url: https://www.slb.com/.well-known/api-catalog
  - status: 200
    url: https://www.slb.com/.well-known/security.txt
  reason: defunct
  state: none
created: '2026-03-23'
description: Cameron International (formerly Cooper Cameron Corporation) was a leading provider of flow equipment products, systems, and services to the worldwide oil, gas, and process industries. In 2016 the business was acquired by Schlumberger (now SLB) and its pressure-control, drilling, subsea, valves, measurement, and compression product lines were integrated into SLB's digital oilfield portfolio. Cameron-branded capabilities are now delivered and integrated through the SLB DELFI digital platform and its developer APIs rather than through a standalone Cameron developer program.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cameron-international.png
layout: provider
modified: '2026-09-05'
name: Cameron International
nav: Providers
network: true
overview: 'Cameron International is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Oil and Gas, Energy, Flow Equipment, Schlumberger, and Industrial.


  Cameron International''s developer surface includes product news and 10 more developer resources.'
press:
- date: '2026-05-25'
  title: 'Forbes Earnings Preview: Cameron International'
  url: https://www.forbes.com/sites/narrativescience/2014/01/28/forbes-earnings-preview-cameron-international-6/
- date: '2026-05-25'
  title: Schlumberger to buy oilfield gear maker Cameron in $14.8 ...
  url: https://www.reuters.com/article/business/schlumberger-to-buy-oilfield-gear-maker-cameron-in-148-billion-deal-idUSKCN0QV11T/
- date: '2026-05-25'
  title: Schlumberger Completes Merger with Cameron
  url: https://www.slb.com/newsroom/press-release/2016/pr-2016-0401-cameron-merger-complete
- date: '2026-05-25'
  title: 'Not Your Granddaddy''s OFS Provider: Schlumberger and ...'
  url: https://www.oilandgas360.com/not-your-granddaddys-ofs-provider-schlumberger-and-cameron-are-primed-to-change-how-its-done-at-the-wellhead/
- date: '2026-05-25'
  title: Cameron International 2026 Company Profile
  url: https://pitchbook.com/profiles/company/41282-47
random_paper: 2
screenshot: https://raw.githubusercontent.com/api-evangelist/cameron-international/refs/heads/main/screenshots/cameron-international-2026-06-20T173912.png
security:
- kind: domain-security
  name: Cameron International Domain Security
  slug: cameron-international-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cameron International Vulnerability Disclosure
  slug: cameron-international-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cameron-international
tags:
- Oil and Gas
- Energy
- Flow Equipment
- Schlumberger
- Industrial
- Fortune 500
website: https://www.slb.com/legacy-companies/cameron-products
---
