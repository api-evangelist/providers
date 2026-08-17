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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bivacor-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bivacor-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bivacor-llms.txt
- group: company
  title: ''
  type: Website
  url: https://bivacor.com/
- group: company
  title: ''
  type: Blog
  url: https://bivacor.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://bivacor.com/feed/
- group: company
  title: ''
  type: Press
  url: https://bivacor.com/media-coverage/
- group: other
  title: ''
  type: Publications
  url: https://bivacor.com/publications/
- group: company
  title: ''
  type: Careers
  url: https://jobs.ashbyhq.com/bivacor-inc
- group: operate
  title: ''
  type: Contact
  url: https://bivacor.com/#contact
- group: operate
  title: ''
  type: Support
  url: mailto:admin@bivacor.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bivacor-pty-ltd
- group: company
  title: ''
  type: Twitter
  url: https://x.com/bivacor
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.nasdaqprivatemarket.com/
coverage:
  checked: '2026-08-07'
  detail: BiVACOR is a clinical-stage medical device manufacturer whose product is an implantable titanium total artificial heart, not software; bivacor.com is a single-page WordPress marketing site whose 15-URL sitemap contains no developer, API or documentation path, and api./developer./docs./portal./status.bivacor.com have no DNS record at all - the only 200 on any contract-discovery path is /wp-json/, the stock WordPress REST API that ships enabled by default and is not a product API.
  evidence:
  - status: 404
    url: https://bivacor.com/openapi.json
  - status: 404
    url: https://bivacor.com/.well-known/agent-card.json
  - status: 404
    url: https://bivacor.com/.well-known/security.txt
  - status: 404
    url: https://bivacor.com/llms.txt
  - status: 200
    url: https://bivacor.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-07'
description: BiVACOR, Inc. is a privately held, clinical-stage medical device company with corporate operations in Huntington Beach, California, clinical operations in Houston, Texas, and engineering operations on the Gold Coast, Queensland, Australia. It develops the BiVACOR Total Artificial Heart (TAH), a titanium biventricular rotary blood pump built around a single magnetically levitated rotor with a dual-sided impeller that replaces both ventricles of a failing heart, with no valves, flexing diaphragms or mechanical bearings, and flows above 12 L/min. Founded by Chief Technical Officer Daniel Timms, PhD, and led by CEO Jim Dillon with Chief Medical Officer William E. Cohn, MD, the company completed the first-in-human implantation at The Texas Heart Institute in July 2024 under an FDA Early Feasibility Study, received FDA Breakthrough Device Designation in May 2025, and was accepted into the FDA Total Product Life Cycle Advisory Program in August 2025. The TAH is an investigational device,
  limited by federal law to investigational use, and is not approved for commercial sale. BiVACOR is a medical hardware and clinical-research business - it publishes no developer program, public API, SDK, or machine-readable API contract.
image: https://bivacor.com/wp-content/uploads/2024/02/BIVACOR_Logo-300x64.jpg
layout: provider
modified: '2026-08-07'
name: BiVACOR
nav: Providers
network: true
overview: 'BiVACOR is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Health Care, Cardiology, and Heart Failure.


  BiVACOR''s developer surface includes engineering blog, support, and 12 more developer resources.'
random_paper: 146
score:
  band: minimal
  composite: 8.1
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bivacor/refs/heads/main/screenshots/bivacor-2026-08-07T162559.png
security:
- kind: domain-security
  name: Bivacor Domain Security
  slug: bivacor-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bivacor
tags:
- Company
- Medical Devices
- Health Care
- Cardiology
- Heart Failure
- Total Artificial Heart
- Mechanical Circulatory Support
- Medical Technology
- Clinical Trials
website: https://bivacor.com/
---
