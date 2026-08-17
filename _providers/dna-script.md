---
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The GraphQL API behind DNA Script's SYNTAX Console Software — the fleet-management layer customers use to design plate templates, upload oligo sequence files, schedule and start synthesis runs, monito
  name: DNA Script SYNTAX Console GraphQL API
  slug: syntax-console
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dna-script-domain-security.yml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/dna-script-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dna-script-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.dnascript.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/dna-script-stock
- group: other
  title: ''
  type: Products
  url: https://www.dnascript.com/products/
- group: other
  title: ''
  type: KnowledgeHub
  url: https://www.dnascript.com/resources/
- group: operate
  title: ''
  type: FAQ
  url: https://www.dnascript.com/resources/faq/
- group: operate
  title: ''
  type: Support
  url: https://www.dnascript.com/resources/support/
- group: company
  title: ''
  type: Blog
  url: https://www.dnascript.com/blog/
- group: company
  title: ''
  type: News
  url: https://www.dnascript.com/company/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dnascript.com/wp-content/uploads/2021/03/DNA-SCRIPT-PRIVACY-POLICY.pdf
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.dnascript.com/wp-content/uploads/2021/03/DNA-SCRIPT-COOKIES-POLICY.pdf
- group: other
  title: ''
  type: QualityPolicy
  url: https://www.dnascript.com/resources/quality-policy/
- group: other
  title: ''
  type: Patents
  url: https://www.dnascript.com/products/patents/
- group: start
  title: ''
  type: Login
  url: https://syntax.dnascript.com/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.dnascript.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://www.dnascript.com/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dna-script/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/dnascript
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCxFbsx6YvSeqMM9oFzwaXQg
created: '2026-08-04'
description: DNA Script is a synthetic-biology company founded in 2014 in Paris, France, with US operations in South San Francisco, that pioneered Enzymatic DNA Synthesis (EDS) — a water-based, template-free, lower-carbon alternative to phosphoramidite chemistry. Its flagship product, the SYNTAX System, is a benchtop DNA printer that synthesizes, desalts, quantifies and normalizes up to 96 custom oligonucleotides in parallel (up to 120 nt on-instrument, up to 500 nt via ordered EDS oligos), giving laboratories same-day, on-premise production of custom DNA. The instrument is paired with SYNTAX System Software on the instrument touchscreen and a separate Console Software layer — offered cloud-hosted or on-premises — through which customers upload sequence files, design plate templates, schedule and monitor synthesis runs across a fleet of instruments, track reagent and consumable levels, and review run reports. The company also markets the ENCODEX DNA biomanufacturing platform for larger-scale
  enzymatic DNA production. DNA Script publishes no public developer portal, no OpenAPI and no documented API program; the Console Software is reached through a customer-authenticated GraphQL endpoint at syntax.dnascript.com.
image: https://www.dnascript.com/wp-content/uploads/2025/01/DNA_Script_Logo_RedWhite.png
layout: provider
modified: '2026-08-04'
name: DNA Script
nav: Providers
network: true
overview: 'DNA Script publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Synthetic Biology, Life Sciences, and DNA Synthesis.


  DNA Script''s developer surface includes FAQ, support, engineering blog, product news, YouTube channel, and 16 more developer resources.'
random_paper: 119
score:
  band: emerging
  composite: 23.9
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 43.2
    developer_ergonomics: 6.5
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 23.9
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dna-script/refs/heads/main/screenshots/dna-script-2026-08-07T164437.png
security:
- kind: authentication
  name: Dna Script Authentication
  slug: dna-script-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Dna Script Domain Security
  slug: dna-script-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dna-script
tags:
- Company
- Biotechnology
- Synthetic Biology
- Life Sciences
- DNA Synthesis
- Laboratory Instruments
- Genomics
- Scientific Computing
- GraphQL
website: https://www.dnascript.com/
---
