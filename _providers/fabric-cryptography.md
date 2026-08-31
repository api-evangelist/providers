---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.fabriccryptography.com/
- group: company
  title: ''
  type: Blog
  url: https://www.fabriccryptography.com/blog
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fabric-cryptography-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fabric-cryptography-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/fabric-cryptography-plans-pricing.yml
coverage:
  checked: '2026-08-12'
  detail: Fabric Cryptography's entire public site is seven Webflow pages (home, blog index and four posts) with no developer, docs, API or SDK section, and every access path it does advertise is dead — the Co-Design, Pre-Order and Contact Typeforms all redirect to Typeform's generic "incorrect URL" page and the Lever careers board 404s; its two GitHub organizations (f16y, FabricCryptography) exist but hold zero public repositories.
  evidence:
  - status: 200
    url: https://www.fabriccryptography.com/sitemap.xml
  - status: 404
    url: https://www.fabriccryptography.com/openapi.json
  - status: 404
    url: https://www.fabriccryptography.com/.well-known/agent-card.json
  - status: 404
    url: https://jobs.lever.co/f16y
  - status: 301
    url: https://f16y.typeform.com/sales
  - status: 200
    url: https://api.github.com/orgs/f16y/repos
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: 'Fabric Cryptography (legal entity Fabric of Truth, Inc.) is a Santa Clara, California semiconductor company founded in 2022 that builds the Verifiable Processing Unit (VPU) — a custom silicon chip whose instruction set is designed exclusively for the mathematical building blocks of modern cryptography. The VPU combines the programmability of a GPU with the performance of an ASIC: hundreds of number-theory units for 32-bit to 384-bit modular arithmetic, custom hash instructions, software-controlled scratchpad memory, a non-blocking network-on-chip, and an on-chip multi-core RISC-V processor for native witness generation. Products announced are the FC 1000 chip, the VPU 8060 card (three FC 1000 chips, ~1 TB/s memory bandwidth to 30 GB) and the "Byte Smasher" server (up to eight VPU 8060 cards). Software is an LLVM-based compiler plus a reconfigurable library of primitives targeting plonky2, plonky3, GKR, halo2, Jolt/Lasso, Nova and TFHE, with a stated future cloud offering. The
  company raised $33M in 2024 from Blockchain Capital, 1kx, Inflection and Protocol Labs, and has announced collaborations with Polygon Labs (AggLayer) and RISC Zero (Boundless). As of this pass Fabric publishes no developer program, API, SDK registry package or machine-readable specification of any kind.'
image: https://cdn.prod.website-files.com/66b7d416d16b3b093afcdc6e/66c1b60dbffcf3768deabd5d_fabric_256x256.png
layout: provider
modified: '2026-08-12'
name: Fabric Cryptography
nav: Providers
network: true
overview: 'Fabric Cryptography is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptography, Hardware, Semiconductors, and Zero Knowledge Proofs.


  Fabric Cryptography''s developer surface includes engineering blog and 4 more developer resources.'
plans:
- name: Fabric Cryptography Plans Pricing
  plan_count: 0
  slug: fabric-cryptography-plans-pricing
random_paper: 10
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Fabric Cryptography Domain Security
  slug: fabric-cryptography-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fabric-cryptography
tags:
- Company
- Cryptography
- Hardware
- Semiconductors
- Zero Knowledge Proofs
- Fully Homomorphic Encryption
- Privacy
- Accelerated Computing
- Blockchain
website: https://www.fabriccryptography.com/
---
