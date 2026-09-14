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
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/siemens/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dresser-rand-group-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dresser-rand-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.siemens-energy.com/
- group: other
  title: ''
  type: Successor
  url: https://www.siemens-energy.com/global/en/home.html
coverage:
  checked: '2026-09-06'
  detail: Dresser-Rand's own domain still resolves but answers every path — root, /robots.txt and every /.well-known/ path alike — with one blanket 301 into a Siemens Energy marketing page that is itself a 404, and HTTPS on the host does not answer at all; the brand was absorbed by Siemens in 2015 and even its LinkedIn company page is now gone.
  evidence:
  - status: 301
    url: http://dresser-rand.com/.well-known/security.txt
  - status: 404
    url: https://www.siemens-energy.com/global/en/offerings/industrial-applications.html
  - status: 404
    url: https://www.linkedin.com/company/dresser-rand
  reason: defunct
  state: none
created: '2026-03-24'
description: Dresser-Rand Group was a global supplier of rotating equipment solutions to the worldwide oil, gas, petrochemical, and process industries. It was acquired by Siemens in 2015 and now operates as part of Siemens Energy.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dresser-rand-group.png
layout: provider
modified: '2026-09-06'
name: Dresser-Rand Group
nav: Providers
network: true
overview: Dresser-Rand Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Industrial, Oil and Gas, Rotating Equipment, and Energy.
press:
- date: '2026-05-25'
  title: Siemens Gets Greenlight on $7.8 Billion Buyout of Dresser ...
  url: https://www.oilandgas360.com/siemens-gets-greenlight-on-7-8-billion-buyout-of-dresser-rand/
- date: '2026-05-25'
  title: Dresser-Rand to Acquire Turbo Machines Field Services ...
  url: https://www.prnewswire.com/news-releases/dresser-rand-to-acquire-turbo-machines-field-services-pty-ltd-92217034.html
- date: '2026-05-25'
  title: Siemens buyout of Dresser-Rand set to face Feb. 13 review ...
  url: https://www.mlex.com/mlex/articles/2080153/siemens-buyout-of-dresser-rand-set-to-face-feb-13-review-deadline-in-eu
- date: '2026-05-25'
  title: How Will Siemens' Acquisition of Dresser-Rand Change ...
  url: https://www.ien.eu/article/how-will-siemens-acquisition-of-dresser-rand-change-the-competitive-landscape/?a=enquire
- date: '2026-05-25'
  title: Siemens in agreed $7.6 billion deal to buy Dresser-Rand
  url: https://www.reuters.com/article/technology/siemens-in-agreed-76-billion-deal-to-buy-dresser-rand-idUSKCN0HH0CM/
random_paper: 1
screenshot: https://raw.githubusercontent.com/api-evangelist/dresser-rand-group/refs/heads/main/screenshots/dresser-rand-group-2026-06-20T180225.png
security:
- kind: domain-security
  name: Dresser Rand Group Domain Security
  slug: dresser-rand-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dresser Rand Group Vulnerability Disclosure
  slug: dresser-rand-group-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dresser-rand-group
tags:
- Industrial
- Oil and Gas
- Rotating Equipment
- Energy
website: https://www.siemens-energy.com/
---
