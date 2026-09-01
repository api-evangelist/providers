---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-01'
api_count: 7
apis:
- description: WordPress REST API discovery documents.
  name: Emulate Discovery API
  slug: emulate-discovery-api
- description: Gated content request forms.
  name: Emulate Forms API
  slug: emulate-forms-api
- description: Careers / job listings.
  name: Emulate Jobs API
  slug: emulate-jobs-api
- description: Press coverage and newsroom items.
  name: Emulate News API
  slug: emulate-news-api
- description: Emulate blog posts.
  name: Emulate Posts API
  slug: emulate-posts-api
- description: Resource library items and their taxonomies.
  name: Emulate Resources API
  slug: emulate-resources-api
- description: Organ-Chip protocols, user guides and data-analysis content.
  name: Emulate Support API
  slug: emulate-support-api
artifact_total: 11
collections:
- collection_type: open
  name: Emulate Content REST API (derived)
  slug: open-emulate-content-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/emulate-content-api-overlay.yaml
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
  name: Emulate MCP Server
  slug: emulate-mcp-server
modified: '2026-08-01'
name: Emulate
nav: Providers
network: true
overview: 'Emulate publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, Forms API, Jobs API, and 4 more. Tagged areas include Company, Biotechnology, Life Sciences, Organ-on-a-Chip, and Drug Discovery.


  Emulate''s developer surface includes engineering blog, support, documentation, legal docs, product news, and 18 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 30.8
  coverage:
    artifact_dirs: 16
    catalog_gap: 60.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 4.5
    contract_quality: 12.4
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  previous_composite: 30.8
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
    score: 31.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
website: https://emulatebio.com/
---
