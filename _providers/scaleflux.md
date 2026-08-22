---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scaleflux-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/scaleflux-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/scaleflux-cli.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/scaleflux-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/scaleflux-llms.txt
- group: company
  title: ''
  type: Website
  url: https://scaleflux.com/
- group: other
  title: ''
  type: Products
  url: https://scaleflux.com/products/
- group: company
  title: ''
  type: Blog
  url: https://scaleflux.com/category/blog/
- group: company
  title: ''
  type: News
  url: https://scaleflux.com/about/news/
- group: other
  title: ''
  type: Resources
  url: https://scaleflux.com/resources/
- group: operate
  title: ''
  type: FAQ
  url: https://scaleflux.com/faqs/
- group: operate
  title: ''
  type: Support
  url: https://scaleflux.com/contact-us/
- group: company
  title: ''
  type: Partners
  url: https://scaleflux.com/partners/
- group: company
  title: ''
  type: Careers
  url: https://scaleflux.com/about/careers/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scaleflux.com/privacy-policy/
- group: company
  title: ''
  type: About
  url: https://scaleflux.com/about/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/scaleflux_stock/
created: '2026-08-02'
description: 'ScaleFlux is a semiconductor and systems company, founded in 2014 and headquartered in Milpitas / San Jose, California, that designs enterprise NVMe SSD controllers, computational storage drives and CXL memory products. Its FX-series SoC controllers (SFX 3016, FX 5016) embed transparent hardware compression, so drives such as the CSD 2000, CSD 3000 and CSD 5000 series present substantially more logical than physical capacity while offloading compression and data-shaping work from the host CPU. The company also ships non-compressing NSD drives and CXL memory expansion silicon aimed at AI, cloud and database infrastructure. ScaleFlux is a hardware vendor rather than a web-API provider: it publishes no public REST, GraphQL or webhook API. Its programmable surface is the NVMe standard command set plus the vendor-specific "sfx" extensions shipped as an upstream plugin in linux-nvme/nvme-cli (sfx-nvme), together with kernel driver and utility packages distributed through packagecloud.io.'
image: https://kinlane-productions2.s3.amazonaws.com/api-evangelist-site/api-evangelist-logo.png
layout: provider
modified: '2026-08-02'
name: ScaleFlux
nav: Providers
network: true
overview: 'ScaleFlux is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Storage, Hardware, Semiconductors, and Computational Storage.


  ScaleFlux''s developer surface includes CLI, engineering blog, product news, FAQ, support, and 12 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 12.9
  delta: 1.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 11.9
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Scaleflux Domain Security
  slug: scaleflux-domain-security
  summary_line: TLSv1.3 · DMARC
slug: scaleflux
tags:
- Company
- Storage
- Hardware
- Semiconductors
- Computational Storage
- NVMe
- SSD
- CXL
- Data Center
- Infrastructure
website: https://scaleflux.com/
---
