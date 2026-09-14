---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acelyrin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://acelyrin.com/
coverage:
  checked: '2026-09-06'
  detail: ACELYRIN was absorbed into Alumis, Inc. on 2025-05-21 as a wholly owned subsidiary and its corporate domain acelyrin.com now 301-redirects to www.alumis.com, so the only surviving surface belongs to the acquirer; the company was a clinical-stage drug developer that never published a developer portal, API, or GitHub organization.
  evidence:
  - status: 301
    url: https://acelyrin.com/
  - status: 200
    url: https://www.alumis.com/
  - status: 404
    url: https://acelyrin.com/.well-known/api-catalog
  - status: 404
    url: https://acelyrin.com/openapi.json
  - status: 404
    url: https://api.github.com/orgs/acelyrin
  reason: defunct
  state: none
created: '2026-09-06'
description: 'ACELYRIN, Inc. (Nasdaq: SLRN) was a late-stage clinical biopharmaceutical company headquartered in Agoura Hills, California, focused on accelerating the development and commercialization of medicines in immunology. Its lead candidates were izokibep, an anti-IL-17A small protein therapeutic, and lonigutamab, a humanized IgG1 monoclonal antibody against IGF-1R. It completed a $540M IPO in May 2023, and on May 21, 2025 it merged with a subsidiary of Alumis, Inc. and survives as a wholly owned Alumis subsidiary. Its corporate domain acelyrin.com now 301-redirects to alumis.com. The company is a drug developer, not a software vendor: it published no developer program, public API, SDK, webhook surface, or machine-readable specification, and no GitHub organization exists under the ACELYRIN name.'
layout: provider
modified: '2026-09-06'
name: ACELYRIN, Inc.
nav: Providers
network: true
overview: ACELYRIN, Inc. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biopharmaceutical, Biotechnology, Pharmaceuticals, and Immunology.
random_paper: 15
security:
- kind: domain-security
  name: Acelyrin Domain Security
  slug: acelyrin-domain-security
  summary_line: TLSv1.3 · DMARC
slug: acelyrin
tags:
- Company
- Biopharmaceutical
- Biotechnology
- Pharmaceuticals
- Immunology
- Clinical Trials
- Healthcare
- Acquired
website: https://acelyrin.com/
---
