---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cleanslate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cleanslatecenters.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/cleanslate_stock/
coverage:
  checked: '2026-08-09'
  detail: 'CleanSlate is a 65-clinic outpatient addiction-treatment medical group (acquired by Spero Health on 2026-07-01) whose only public host is a WordPress marketing site — 6,945 archived URLs across its entire history contain no /api, /developers or /docs path, and no GitHub organization exists — so there is no software product to expose an API; the live site additionally answers every automated request, including /robots.txt, with a SiteGround `sg-captcha: challenge` interstitial (HTTP 202).'
  evidence:
  - status: 202
    url: https://www.cleanslatecenters.com/developers
  - status: 202
    url: https://www.cleanslatecenters.com/robots.txt
  - status: 200
    url: https://web.archive.org/cdx/search/cdx?url=cleanslatecenters.com&matchType=domain&fl=original&collapse=urlkey&limit=20000
  - status: 200
    url: https://api.github.com/search/users?q=cleanslate+type:org
  reason: not-a-software-company
  state: none
created: '2026-08-09'
description: 'CleanSlate (CleanSlate Centers) is a national outpatient medical group treating opioid and alcohol use disorder with physician-led, office-based medication-assisted treatment — FDA-approved medication combined with primary care and behavioral health therapy for polysubstance use and co-occurring disorders. Founded in 2009 in Massachusetts by Dr. Amanda Wilson in response to the opioid epidemic, it grew to more than 65 outpatient centers across eight states and raised roughly $79M in venture backing before being acquired by Spero Health on July 1, 2026. CleanSlate is a care-delivery organization: it operates clinics, not a software platform, and publishes no public API, SDK, developer portal or machine-readable specification.'
layout: provider
modified: '2026-08-09'
name: CleanSlate
nav: Providers
network: true
overview: CleanSlate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Behavioral Health, Addiction Treatment, and Opioid Use Disorder.
random_paper: 2
screenshot: https://raw.githubusercontent.com/api-evangelist/cleanslate/refs/heads/main/screenshots/cleanslate-2026-09-02T145103.png
security:
- kind: domain-security
  name: Cleanslate Domain Security
  slug: cleanslate-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cleanslate
tags:
- Company
- Healthcare
- Behavioral Health
- Addiction Treatment
- Opioid Use Disorder
- Medication-Assisted Treatment
- Outpatient Clinics
- United States
website: https://www.cleanslatecenters.com/
---
