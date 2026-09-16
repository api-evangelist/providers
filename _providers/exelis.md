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
  href: https://raw.githubusercontent.com/api-evangelist/exelis/refs/heads/main/security/exelis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/exelis-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/exelis
- group: company
  title: ''
  type: Website
  url: https://www.l3harris.com
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Exelis_Inc.
coverage:
  checked: '2026-09-07'
  detail: Exelis Inc. ceased to exist as a company when Harris Corporation acquired it in 2015 and folded it into L3Harris in 2019; exelis.com now answers only an unconfigured OVHcloud "Site not installed" 404 page that L3Harris does not operate, exelisvis.com no longer resolves at all, and exelisinc.com resolves but refuses connections, so there is no Exelis-brand host left on which an API could be published.
  evidence:
  - status: 404
    url: https://exelis.com/
  - status: 404
    url: https://exelis.com/.well-known/security.txt
  - status: 404
    url: https://exelis.com/apis.json
  - status: 404
    url: https://www.l3harris.com/.well-known/api-catalog
  reason: defunct
  state: none
created: '2026-03-24'
description: Exelis Inc. was an American global aerospace, defense, information, and services company that produced communications systems, electronic warfare products, geospatial systems, integrated structures, and night vision equipment. Headquartered in McLean, Virginia, Exelis was acquired by Harris Corporation in 2015. Harris and L3 Technologies then merged in 2019 to form L3Harris Technologies. No public APIs are published under the Exelis brand; developer resources, if any, are tracked under L3Harris.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/exelis.png
layout: provider
modified: '2026-09-15'
name: Exelis
nav: Providers
network: true
overview: Exelis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Aerospace, Defense, Acquired, L3Harris, and Electronic Warfare.
press:
- date: '2026-05-25'
  title: Generative Artificial Intelligence in the DoD Acquisition ...
  url: https://acqirc.org/events/generative-artificial-intelligence-in-the-dod-acquisition-lifecycle/
- date: '2026-05-25'
  title: News & Announcements
  url: https://saalex.com/news-announcements/
- date: '2026-05-25'
  title: SparkCognition Government Systems Appoints Lieutenant ...
  url: https://www.prnewswire.com/news-releases/sparkcognition-government-systems-appoints-lieutenant-general-ken-hunzeker-ret-to-board-of-directors-301518687.html
- date: '2026-05-25'
  title: Harris completes $4.75 billion acquisition of Exelis
  url: https://rbj.net/2015/05/29/harris-completes-4-75-billion-acquisition-of-exelis/
- date: '2026-05-25'
  title: SAIC
  url: https://www.govconwire.com/s/company/saic/page/770
random_paper: 20
screenshot: https://raw.githubusercontent.com/api-evangelist/exelis/refs/heads/main/screenshots/exelis-2026-06-20T180930.png
security:
- kind: domain-security
  name: Exelis Domain Security
  slug: exelis-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: exelis
tags:
- Aerospace
- Defense
- Acquired
- L3Harris
- Electronic Warfare
- Geospatial
- Night Vision
- Government
- Defunct
website: https://www.l3harris.com
---
