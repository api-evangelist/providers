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
  url: security/neye-systems-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/neye-systems-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/neye-systems-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.neye.ai/
- group: company
  title: ''
  type: About
  url: https://www.neye.ai/about-us
- group: company
  title: ''
  type: Press
  url: https://www.neye.ai/press-release
- group: company
  title: ''
  type: Investors
  url: https://www.neye.ai/our-investors
- group: company
  title: ''
  type: Careers
  url: https://www.neye.ai/join-us
- group: operate
  title: ''
  type: Contact
  url: https://www.neye.ai/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.neye.ai/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.neye.ai/privacy-policy
coverage:
  checked: '2026-08-26'
  detail: nEye ships an optical circuit switch ASIC, not software — its entire public surface is an eight-page Webflow marketing site (www.neye.ai) whose sitemap lists only home, about, investors, careers, contact, press and legal pages, with no developer, docs or API route anywhere, and every /openapi.json, /graphql, /llms.txt and /.well-known/* probe returning a real 404.
  evidence:
  - status: 200
    url: https://www.neye.ai/sitemap.xml
  - status: 404
    url: https://www.neye.ai/openapi.json
  - status: 404
    url: https://www.neye.ai/.well-known/agent-card.json
  - status: 200
    url: https://www.neyesystems.com/zzz-does-not-exist-9182
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'nEye (nEye.ai, formerly nEye Systems) is a silicon photonics company in Santa Clara and Emeryville, California building an optical circuit switch on a chip — a programmable photonic integrated circuit that combines silicon photonics, MEMS and CMOS to switch light directly between GPUs, CPUs and memory inside AI and high-performance computing data centers, marketed as the SuperSwitch. The company was spun out of University of California, Berkeley research by co-founder and chief scientist Ming C. Wu and is led by CEO Ashish Vengsarkar. It raised an $80M Series C led by Sutter Hill Ventures in April 2026, bringing total funding to $152M with participation from CapitalG, M12 and Socratic Partners, and it participates in the Open Compute Project Open OCS effort alongside Google, NVIDIA and Microsoft. nEye is a semiconductor and optical hardware company: as of this profile it publishes no developer program, API, SDK, webhook surface or machine-readable contract of any kind, and
  its entire public surface is a seven-page marketing site.'
image: https://cdn.prod.website-files.com/68e49740aa56011f2ac8b755/68ea44cf079b8a74058011bf_neye.png
layout: provider
modified: '2026-08-26'
name: nEye Systems
nav: Providers
network: true
overview: nEye Systems is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Silicon Photonics, Optical Networking, and Data Center Infrastructure.
random_paper: 10
screenshot: https://raw.githubusercontent.com/api-evangelist/neye-systems/refs/heads/main/screenshots/neye-systems-2026-09-02T150752.png
security:
- kind: domain-security
  name: Neye Systems Domain Security
  slug: neye-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: neye-systems
tags:
- Company
- Semiconductors
- Silicon Photonics
- Optical Networking
- Data Center Infrastructure
- Artificial Intelligence
- Networking Hardware
- Interconnect
website: https://www.neye.ai/
---
