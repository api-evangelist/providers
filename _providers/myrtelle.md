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
  url: security/myrtelle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://myrtellegtx.com/
coverage:
  checked: '2026-08-26'
  detail: Myrtelle is a clinical-stage gene therapy developer (lead program MYR-101 / rAAV-Olig001-ASPA for Canavan disease) with no developer program of any kind — its reachable property canavantreatment.com 404s on every OpenAPI, GraphQL, llms.txt, agent-card and /.well-known/ path and exposes only stock WordPress core routes at /wp-json, no GitHub organization exists (api.github.com/orgs/myrtelle returns 404), and no first-party package is published to npm or PyPI.
  evidence:
  - status: 404
    url: https://canavantreatment.com/openapi.json
  - status: 404
    url: https://canavantreatment.com/.well-known/agent-card.json
  - status: 404
    url: https://canavantreatment.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/myrtelle
  - status: 404
    url: https://pypi.org/pypi/myrtelle/json
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Myrtelle, Inc. is a clinical-stage biotechnology company headquartered in Wakefield, Massachusetts, developing gene therapies for myelin-based disorders of the central nervous system. Its lead program, MYR-101 (rAAV-Olig001-ASPA), is a first-in-class oligotrophic recombinant adeno-associated virus gene therapy for Canavan disease, a rare and fatal childhood genetic brain disease caused by mutations in the ASPA gene. The program is licensed exclusively worldwide from Pfizer Inc., holds Orphan Drug, Fast Track and Rare Pediatric Disease designations in the US with similar designations in Europe, and has reported Phase 1/2 interim results in Nature Medicine. Myrtelle is a therapeutics developer, not a software company: it publishes no developer program, API, SDK or machine-readable API contract, and is profiled here for network completeness only.'
layout: provider
modified: '2026-08-26'
name: Myrtelle
nav: Providers
network: true
overview: Myrtelle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Gene Therapy, Life Sciences, and Pharmaceuticals.
random_paper: 17
screenshot: https://raw.githubusercontent.com/api-evangelist/myrtelle/refs/heads/main/screenshots/myrtelle-2026-09-02T150708.png
security:
- kind: domain-security
  name: Myrtelle Domain Security
  slug: myrtelle-domain-security
  summary_line: TLSv1.3 · DMARC
slug: myrtelle
tags:
- Company
- Biotechnology
- Gene Therapy
- Life Sciences
- Pharmaceuticals
- Clinical Trials
- Rare Disease
- Healthcare
website: https://myrtellegtx.com/
---
