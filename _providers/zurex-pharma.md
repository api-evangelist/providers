---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zurex-pharma-domain-security.yml
coverage:
  checked: '2026-09-05'
  detail: 'Zurex Pharma sells regulated physical antiseptics (ZuraPrep, ZuraGard, ZurAsept, ZuraLac), not software, and it has no readable web surface either: its own domain zurexpharma.com is pointed at Wix with no site connected, so the origin answers the "ConnectYourDomain Error | Wix.com" HTML page with HTTP 404 for every path including the root, /openapi.json, /llms.txt and every /.well-known/ path, while its LinkedIn company page at /company/zurex-pharma also 404s.'
  evidence:
  - status: 404
    url: https://www.zurexpharma.com/
  - status: 404
    url: https://www.zurexpharma.com/openapi.json
  - status: 404
    url: https://www.zurexpharma.com/llms.txt
  - status: 404
    url: https://zurexpharma.com/.well-known/agent-card.json
  - status: 404
    url: https://www.linkedin.com/company/zurex-pharma
  reason: not-a-software-company
  state: none
created: '2026-09-05'
description: 'Zurex Pharma, Inc. is a privately held specialty pharmaceutical and medical technology company founded in 2008 and headquartered in Middleton, Wisconsin, developing a portfolio of patented antimicrobial formulations intended to prevent healthcare-acquired infections. Its products are physical, regulated goods rather than software: ZuraPrep, a single-use pre-surgical skin antiseptic submitted to the FDA as NDA 210872 in June 2018; ZuraGard for peri-operative and catheter exit-site antisepsis; ZurAsept, a catheter lock solution; and ZuraLac, a teat sanitizer for dairy cattle. Backed by Baird Venture Partners, the State of Wisconsin Investment Board, Peak Ridge Capital and Wisconsin Investment Partners. The company publishes no developer program, no API and no machine-readable API artifacts of any kind, and as of this pass its own domain serves no website.'
layout: provider
modified: '2026-09-05'
name: Zurex Pharma
nav: Providers
network: true
overview: Zurex Pharma is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Medical Devices, Healthcare, and Antimicrobials.
random_paper: 13
security:
- kind: domain-security
  name: Zurex Pharma Domain Security
  slug: zurex-pharma-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zurex-pharma
tags:
- Company
- Pharmaceuticals
- Medical Devices
- Healthcare
- Antimicrobials
- Infection Prevention
- Life Sciences
- Wisconsin
---
