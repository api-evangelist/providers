---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: 'Anonymous, read-only REST surface behind emulatebio.com. Emulate runs WordPress and exposes the WordPress REST API publicly, with six first-party custom namespaces registered alongside the core wp/v2 '
  name: Emulate Content REST API
  slug: content-api
artifact_total: 4
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/emulate-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/emulate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://forgeglobal.com/emulate_stock/
- group: company
  title: ''
  type: Website
  url: https://emulatebio.com/
- group: company
  title: ''
  type: Blog
  url: https://emulatebio.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://emulatebio.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://emulatebio.com/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://emulatebio.com/contact-support/
- group: docs
  title: ''
  type: Documentation
  url: https://emulatebio.com/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/emulatebio
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://emulatebio.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://emulatebio.com/emulate-inc-terms-of-use/
- group: commercial
  title: ''
  type: Legal
  url: https://emulatebio.com/legal/
- group: company
  title: ''
  type: Careers
  url: https://emulatebio.com/careers/
- group: other
  title: ''
  type: Events
  url: https://emulatebio.com/events/
- group: other
  title: ''
  type: Publications
  url: https://emulatebio.com/publications/
- group: other
  title: ''
  type: Products
  url: https://emulatebio.com/products/
- group: other
  title: ''
  type: Software
  url: https://emulatebio.com/products/software/
- group: company
  title: ''
  type: News
  url: https://emulatebio.com/in-the-news/
- group: design
  title: ''
  type: Conformance
  url: conformance/emulate-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/emulate-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/emulate-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-01'
description: Emulate, Inc. is a Boston, Massachusetts biotechnology company, spun out of Harvard's Wyss Institute in 2014, that commercialized Organ-on-a-Chip technology for human-relevant preclinical research. Its Human Emulation System pairs the Ava Emulation System and Zoe-CM2 Culture Module instruments with Chip-S1, Chip-R1, Chip-A1 and Chip-Array consumables and validated Organ-Chip models for Brain, Liver, Kidney, Lung, Duodenum Intestine, Bone Marrow, Lymphoid and Vagina, applied across toxicology, oncology, cell and gene therapy, immunology, infectious disease, microbiome and neuroscience. Emulate publishes no developer portal, API reference or SDKs; its software products are downloadable desktop analysis calculators and a firmware Utility Hub. Enrichment probing did find a real, anonymous, read-only WordPress REST API behind emulatebio.com carrying six first-party emulate-* namespaces for news, blog posts, jobs, forms, the resource library and Organ-Chip support protocols.
image: https://emulatebio.com/wp-content/uploads/2024/02/emulate-logo.png
layout: provider
mcp_servers:
- description: ''
  name: emulate-mcp.yml
  slug: emulate-mcpyml
modified: '2026-08-01'
name: Emulate
nav: Providers
network: true
overview: 'Emulate publishes 1 API on the [APIs.io](https://apis.io/) network: Content REST API. Tagged areas include Company, Biotechnology, Life Sciences, Organ-on-a-Chip, and Drug Discovery.


  Emulate''s developer surface includes engineering blog, support, documentation, legal docs, product news, and 18 more developer resources.'
random_paper: 29
score:
  band: emerging
  composite: 21.5
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 13.6
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 21.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/emulate/refs/heads/main/screenshots/emulate-2026-08-07T164847.png
security:
- kind: authentication
  name: Emulate Authentication
  slug: emulate-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Emulate Domain Security
  slug: emulate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: emulate
tags:
- Company
- Biotechnology
- Life Sciences
- Organ-on-a-Chip
- Drug Discovery
- Preclinical Research
- Toxicology
- Laboratory Instruments
- In Vitro Models
- Scientific Software
website: https://forgeglobal.com/emulate_stock/
---
