---
api_count: 0
artifact_total: 1
common:
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/acutus-medical_stock/
- group: other
  title: ''
  type: SECFilings
  url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001522860&type=&dateb=&owner=include&count=40
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acutus-medical-inc-
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acutus-medical-domain-security.yml
coverage:
  checked: '2026-09-06'
  detail: Acutus Medical exited the electrophysiology mapping and ablation business in December 2024, was delisted from Nasdaq in May 2024 and went dark with a Form 15-15D in January 2025, and has since withdrawn its entire web presence — acutus.com and acutusmedical.com answer NOERROR with zero A records, www.acutus.com, www.acutusmedical.com and the ir.acutusmedical.com investor site named in its own press releases all answer NXDOMAIN, and Certificate Transparency for acutusmedical.com holds only a wildcard and the apex, so no api./docs./developer. host was ever certified and none was left unprobed; both zones still carry Microsoft 365 MX and SPF records, so mail routes while there is no longer any host on which an API contract could be served.
  evidence:
  - status: 0
    url: https://acutus.com/
  - status: 0
    url: https://www.acutusmedical.com/
  - status: 0
    url: https://ir.acutusmedical.com/
  - status: 0
    url: https://acutus.com/openapi.json
  - status: 0
    url: https://www.acutusmedical.com/llms.txt
  - status: 0
    url: https://acutusmedical.com/.well-known/agent-card.json
  - status: 0
    url: https://acutusmedical.com/.well-known/security.txt
  - status: 404
    url: https://api.github.com/orgs/acutusmedical
  - status: 404
    url: https://pypi.org/pypi/acutus/json
  - status: 200
    url: https://api.certspotter.com/v1/issuances?domain=acutusmedical.com&include_subdomains=true&expand=dns_names
  - status: 200
    url: https://data.sec.gov/submissions/CIK0001522860.json
  - status: 200
    url: https://www.linkedin.com/company/acutus-medical-inc-
  reason: defunct
  state: none
created: '2026-09-06'
description: Acutus Medical, Inc. is a Carlsbad, California arrhythmia-management medical device company (SEC CIK 0001522860, SIC 3841 Surgical & Medical Instruments) that built the AcQMap non-contact ultrasound-based cardiac imaging and mapping system, the AcQBlate FORCE sensing ablation catheter, and the AcQCross and AcQGuide left-heart access family for electrophysiologists treating complex cardiac arrhythmias. The company sold its left-heart access portfolio to Medtronic beginning in 2022, restructured in November 2023 to solely manufacture and distribute that portfolio for Medtronic, and in December 2024 announced an operational downsizing that exited the electrophysiology mapping and ablation business and cut roughly 70% of its workforce. Its common stock was suspended and delisted from Nasdaq in May 2024, and it filed a Form 15-15D on 24 January 2025 to suspend its reporting obligations and go dark. Acutus was a device manufacturer rather than a software or platform business and never
  operated a developer program or published an API; as of September 2026 its entire public web presence — acutus.com, acutusmedical.com and the ir.acutusmedical.com investor site its own press releases link to — no longer resolves in DNS, leaving no host on which a contract could be published.
layout: provider
modified: '2026-09-06'
name: Acutus Medical, Inc.
nav: Providers
network: true
overview: Acutus Medical, Inc. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Cardiology, and Electrophysiology.
random_paper: 18
security:
- kind: domain-security
  name: Acutus Medical Domain Security
  slug: acutus-medical-domain-security
  summary_line: no transport/DNS hardening detected
slug: acutus-medical
tags:
- Company
- Medical Devices
- Healthcare
- Cardiology
- Electrophysiology
- Cardiac Ablation
- Cardiac Mapping
- Contract Manufacturing
---
