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
  url: security/elion-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eliontx.com/
- group: other
  title: ''
  type: Company
  url: https://forgeglobal.com/elion-therapeutics_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/elion-therapeutics-llms.txt
coverage:
  checked: '2026-08-12'
  detail: Elion Therapeutics is a clinical-stage antifungal drug developer whose only web property is a WordPress marketing site — the origin answers HTTP 404 to every /.well-known/ path and to /llms.txt, and there is no developer portal, GitHub organization, or API of any kind to profile.
  evidence:
  - status: 404
    url: https://eliontx.com/.well-known/api-catalog
  - status: 404
    url: https://eliontx.com/llms.txt
  - status: 200
    url: https://eliontx.com/robots.txt
  - status: 404
    url: https://github.com/eliontx
  reason: not-a-software-company
  state: none
created: '2026-08-12'
description: 'Elion Therapeutics is a privately held, clinical-stage biotechnology company developing treatments for life-threatening invasive fungal infections (IFIs). Formerly known as Sfunga Therapeutics, the company was founded on the belief that mechanistic insight into natural products enables targeted optimization of them. Its lead candidate, SF001, is a next-generation polyene antifungal — a rationally designed analog of amphotericin B intended to retain broad fungicidal activity while mitigating the systemic toxicity that limits the parent molecule. SF001 received FDA Qualified Infectious Disease Product (QIDP) and Fast Track designations in 2023 and has advanced from a first-in-human single-ascending-dose study into multiple-ascending-dose evaluation. Elion closed an $81 million Series B in June 2024 led by Deerfield Management and the AMR Action Fund, with participation from Illinois Ventures. Elion is a therapeutics developer, not a software vendor: it publishes no developer
  program, public API, or machine-readable API contract, and this profile records that absence rather than any API surface.'
layout: provider
modified: '2026-08-12'
name: Elion Therapeutics
nav: Providers
network: true
overview: Elion Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Therapeutics, and Life Sciences.
random_paper: 8
security:
- kind: domain-security
  name: Elion Therapeutics Domain Security
  slug: elion-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: elion-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Therapeutics
- Life Sciences
- Anti-Infectives
- Drug Development
- Clinical Stage
- Healthcare
website: https://eliontx.com/
---
