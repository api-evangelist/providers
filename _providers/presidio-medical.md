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
  url: security/presidio-medical-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/presidio-medical-llms.txt
- group: company
  title: ''
  type: Website
  url: https://presidiomedical.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/presidio-medical-inc
- group: company
  title: ''
  type: Investors
  url: https://forgeglobal.com/presidio-medical_stock/
coverage:
  checked: '2026-08-05'
  detail: Presidio Medical manufactures an implantable ultra-low-frequency spinal cord stimulator and has never run a developer program; on top of that its corporate WordPress site went offline sometime after the Internet Archive's last 200 capture on 2026-06-07 and now returns a WP Engine "Site Not Configured" HTTP 404 on every path including the root and a control path, while no api/developer/docs/portal subdomain resolves at all.
  evidence:
  - status: 404
    url: https://presidiomedical.com/
  - status: 404
    url: https://presidiomedical.com/openapi.json
  - status: 404
    url: https://presidiomedical.com/.well-known/agent-card.json
  - status: 404
    url: https://presidiomedical.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: Presidio Medical is a privately held, clinical-stage medical device company headquartered in South San Francisco, California, founded in 2017 by Kenneth Wu and led by CEO and Chairman Michael Onuscheck. It is developing an implantable Ultra Low Frequency (ULF) neuromodulation platform intended to treat diseases of undesired neural activity, with a first indication in chronic nociceptive low back pain. The therapy delivers ultra low frequency current through an epidural spinal cord stimulation (SCS) lead to reversibly inhibit pain-signaling neurons via sodium channel inactivation, positioned as a non-opioid alternative to conventional SCS. The company raised a $72M Series C in 2023 led by Deerfield Management with Invus Opportunities, Action Potential Venture Capital and ShangBay Capital, and received FDA IDE approval for the global pivotal FULFILL randomized controlled trial in the United States and Australia. Presidio Medical sells an implantable medical device, not software;
  it has never operated a developer program, public API, SDK or machine-readable API contract. As of 2026-08-05 its corporate WordPress site at presidiomedical.com is offline, returning a WP Engine "Site Not Configured" HTTP 404 on every path including the root.
layout: provider
modified: '2026-08-05'
name: Presidio Medical
nav: Providers
network: true
overview: Presidio Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Neuromodulation, Neurotechnology, and Spinal Cord Stimulation.
random_paper: 10
security:
- kind: domain-security
  name: Presidio Medical Domain Security
  slug: presidio-medical-domain-security
  summary_line: TLSv1.3 · DMARC
slug: presidio-medical
tags:
- Company
- Medical Devices
- Neuromodulation
- Neurotechnology
- Spinal Cord Stimulation
- Chronic Pain
- Implantable Devices
- Clinical Stage
- Healthcare
- Life Sciences
website: https://presidiomedical.com/
---
