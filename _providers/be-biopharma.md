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
  url: security/be-biopharma-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/be-biopharma-llms.txt
- group: company
  title: ''
  type: Website
  url: https://be.bio/
- group: other
  title: ''
  type: Archive
  url: https://web.archive.org/web/20260513184102/https://be.bio/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/be-biopharma-inc
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/be-biopharma_stock/
coverage:
  checked: '2026-08-06'
  detail: Be Biopharma's own domain be.bio no longer resolves — its authoritative nameservers (ns1.g02.cfdns.net) return SOA only for both the apex and www, so there is no host left to probe; the site was last archived 2026-05-13, the company terminated its lead BeCoMe-9 hemophilia B trial in June 2026, and LinkedIn now lists a single employee.
  evidence:
  - status: 0
    url: https://be.bio/
  - status: 404
    url: https://www.be.bio/.well-known/security.txt
  - status: 404
    url: https://www.be.bio/.well-known/openid-configuration
  - status: 404
    url: https://www.be.bio/.well-known/ai-plugin.json
  - status: 200
    url: https://web.archive.org/web/20260513184102/https://be.bio/
  - status: 200
    url: https://api.github.com/search/users?q=bebiopharma+OR+be-biopharma
  reason: defunct
  state: none
created: '2026-08-06'
description: 'Be Biopharma (Be Bio) is a Cambridge, Massachusetts clinical-stage biotechnology company founded in October 2020 by Longwood Fund together with B cell engineering researchers David Rawlings, M.D. and Richard James, Ph.D. of Seattle Children''s Research Institute. The company develops engineered B Cell Medicines (BCMs) — a patient''s own B cells engineered to produce a therapeutic protein — for genetic disease, cancer and other serious conditions. Its lead candidate, BE-101, inserted a functional Factor IX gene into primary human B cells for hemophilia B and held FDA Orphan Drug and Fast Track designations; a second program, BE-102, targeted hypophosphatasia. The company raised $82M in October 2024 and $92M in a January 2025 Series C, dosed the first participant in the Phase 1/2 BeCoMe-9 trial in July 2025, and terminated that trial in June 2026 for stated strategic business reasons. Be Biopharma is a therapeutics developer, not a software company: it has never published a developer
  program, API, SDK or machine-readable contract.'
layout: provider
modified: '2026-08-06'
name: Be Biopharma
nav: Providers
network: true
overview: Be Biopharma is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Cell Therapy, and Gene Therapy.
random_paper: 15
security:
- kind: domain-security
  name: Be Biopharma Domain Security
  slug: be-biopharma-domain-security
  summary_line: no transport/DNS hardening detected
slug: be-biopharma
tags:
- Company
- Biotechnology
- Life Sciences
- Cell Therapy
- Gene Therapy
- Pharmaceuticals
- Healthcare
- Clinical Trials
- Rare Disease
website: https://be.bio/
---
