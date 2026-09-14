---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  - '{''url'': ''https://epicsciences.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.stylekitchennashville.com/ — a different registrable domain (epicsciences.com -> stylekitchennashville.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/epic-sciences-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://epicsciences.com
coverage:
  checked: '2026-08-12'
  detail: epicsciences.com — the site every third-party record still lists as the company website — serves a blanket HTTP 301 to an unrelated third-party domain (awaji-musicisland.com) on every path including /robots.txt and every /.well-known/ location, and the domain publishes no MX, SPF, DMARC, CAA or DNSSEC records, so there is no live Epic Sciences web presence left to profile, let alone a developer surface.
  evidence:
  - status: 301
    url: https://www.epicsciences.com/
  - status: 301
    url: https://www.epicsciences.com/.well-known/agent-card.json
  - status: 301
    url: https://www.epicsciences.com/openapi.json
  - status: 404
    url: https://api.github.com/orgs/epic-sciences
  reason: defunct
  state: none
created: '2026-08-12'
description: Epic Sciences is a San Diego, California clinical diagnostics company founded in 2008 that develops blood-based "liquid biopsy" tests for oncology. Its platform, licensed from the Peter Kuhn laboratory at Scripps Research, isolates and characterizes rare circulating tumor cells (CTCs) from whole blood using specialized assays and digital pathology algorithms, and is paired with circulating tumor DNA (ctDNA) sequencing to inform treatment selection and track how a tumor evolves. Its lead product, DefineMBC, is a comprehensive blood biopsy for metastatic breast cancer whose 56-gene ctDNA panel received Medicare coverage in April 2023. The company also runs its platform as a service for pharmaceutical partners measuring outcomes in clinical trials, and in 2020 partnered with Predicine to combine CTC and ctDNA analysis in a single offering. Epic Sciences is privately held and has raised roughly $204M across seven rounds through a Series G in April 2023. It is a laboratory diagnostics
  provider, not a software vendor, and publishes no public API, developer program, SDK or machine-readable specification.
layout: provider
modified: '2026-08-12'
name: Epic Sciences
nav: Providers
network: true
overview: Epic Sciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Diagnostics, Oncology, and Life Sciences.
random_paper: 5
screenshot: https://raw.githubusercontent.com/api-evangelist/epic-sciences/refs/heads/main/screenshots/epic-sciences-2026-09-02T145413.png
security:
- kind: domain-security
  name: Epic Sciences Domain Security
  slug: epic-sciences-domain-security
  summary_line: TLSv1.3
slug: epic-sciences
tags:
- Company
- Healthcare
- Diagnostics
- Oncology
- Life Sciences
- Biotechnology
- Laboratory
- Precision Medicine
website: https://epicsciences.com
---
