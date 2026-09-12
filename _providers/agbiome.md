---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-09-12'
  detail: AgBiome wound down across 2023-2024 — all 123 staff on a WARN notice, Howler and Theia sold to Certis Biologicals in March 2024 and the microbial platform sold to Ginkgo Bioworks in April 2024 — and agbiome.com now answers from a Nexcess shared-hosting placeholder under a mismatched CN=nxcli.net certificate, returning a bare Apache 403 on every /.well-known/ path and 404 on /openapi.json, /llms.txt, /robots.txt and /apis.json, while api., docs., developer., app. and status.agbiome.com are all NXDOMAIN and a Wayback sweep of every archived agbiome.com path from 2014 to 2026 finds no developer or specification URL.
  evidence:
  - status: 200
    url: https://agbiome.com/
  - status: 404
    url: https://agbiome.com/openapi.json
  - status: 404
    url: https://agbiome.com/llms.txt
  - status: 403
    url: https://agbiome.com/.well-known/agent-card.json
  - status: 403
    url: https://agbiome.com/.well-known/agent.json
  - status: 403
    url: https://agbiome.com/.well-known/security.txt
  - status: 404
    url: https://agbiome.com/apis.json
  - status: 525
    url: https://portal.agbiome.com/
  - status: 403
    url: https://blog.agbiome.com/
  - status: 200
    url: https://api.github.com/orgs/agbiome
  reason: defunct
  state: none
created: '2026-09-12'
description: 'AgBiome was an agricultural biotechnology company headquartered in Research Triangle Park, Durham, North Carolina. Founded in 2012 by Scott Uknes, Eric Ward, Jeff Dangl, John Ryals and Paul Schulze-Lefert, it built the proprietary GENESIS discovery platform — a collection of more than 100,000 fully sequenced, isolated plant-associated microbial strains and hundreds of millions of gene sequences, screened with high-throughput assays for insect, disease and nematode control — and turned it into crop-protection biologicals. It commercialized the Howler and Theia biofungicides and had a third, Esendo, before the EPA, and it spun out the genome-editing venture LifeEDIT Therapeutics in October 2020 (acquired by ElevateBio in October 2021). Backed by Syngenta, Novozymes, Monsanto, ARCH Venture Partners, Polaris, the Bill & Melinda Gates Foundation, Pontifax and UTIMCO, the company nonetheless failed to raise further capital: it filed a North Carolina WARN notice in late 2023 covering
  its entire staff of 123, sold Howler and Theia to Certis Biologicals (a Mitsui & Co. subsidiary) in March 2024, and sold its platform assets to Ginkgo Bioworks in April 2024 for roughly $18.2 million in stock. AgBiome never published a developer program, public API, SDK, or machine-readable specification, and agbiome.com no longer serves the company site — it answers from a Nexcess shared-hosting placeholder under a certificate issued to CN=nxcli.net. This profile is retained as a historical record; there is no API surface to enrich.'
layout: provider
modified: '2026-09-12'
name: AgBiome
nav: Providers
network: true
random_paper: 10
slug: agbiome
tags:
- Company
- Defunct
- Agriculture
- AgTech
- Biotechnology
- Microbiology
- Crop Protection
- Biologicals
- Life Sciences
- Research
---
