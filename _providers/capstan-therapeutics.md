---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://capstantx.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.abbvie.com/capstan-therapeutics.html — a different registrable domain (capstantx.com -> abbvie.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://capstantx.com/
coverage:
  checked: '2026-08-09'
  detail: 'Capstan''s own site is gone: capstantx.com 301s to www.abbvie.com/capstan-therapeutics.html and its nameservers are now ns1-4.abbviedns.com, following AbbVie''s completed acquisition on 19 August 2025 — the company was a clinical-stage biotech that never operated a developer program, GitHub org, or public API.'
  evidence:
  - status: 301
    url: https://capstantx.com/
  - status: 301
    url: https://www.capstantx.com/
  - status: 403
    url: https://capstantx.com/.well-known/agent-card.json
  - status: 403
    url: https://capstantx.com/openapi.json
  - status: 404
    url: https://api.github.com/orgs/capstantx
  reason: defunct
  state: none
created: '2026-08-09'
description: Capstan Therapeutics was a clinical-stage biotechnology company based in San Diego, California, developing in vivo cell engineering medicines built on a proprietary targeted lipid nanoparticle (tLNP) platform that delivers mRNA and other RNA payloads to specific cell types inside the body. Its lead candidate CPTX2309 is an anti-CD19 in vivo CAR-T therapy in Phase 1 for B cell-mediated autoimmune disease, intended to achieve deep B cell depletion without lymphodepleting chemotherapy. AbbVie completed its acquisition of Capstan on 19 August 2025 for up to $2.1 billion. The company's own domain now redirects to AbbVie and its DNS is served by AbbVie nameservers; it operates no developer program, public API, SDK, or machine-readable specification.
layout: provider
modified: '2026-08-09'
name: Capstan Therapeutics
nav: Providers
network: true
overview: Capstan Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Cell Therapy, and Immunology.
random_paper: 9
screenshot: https://raw.githubusercontent.com/api-evangelist/capstan-therapeutics/refs/heads/main/screenshots/capstan-therapeutics-2026-09-02T145011.png
slug: capstan-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Cell Therapy
- Immunology
- Life Sciences
- Acquired
website: https://capstantx.com/
---
