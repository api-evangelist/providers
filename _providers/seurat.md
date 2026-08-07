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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.seurat.com/
- group: company
  title: ''
  type: Blog
  url: https://www.seurat.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.seurat.com/blog-feed.xml
- group: company
  title: ''
  type: News
  url: https://www.seurat.com/news-updates
- group: operate
  title: ''
  type: PressReleases
  url: https://www.seurat.com/blog/categories/seurat-press-releases
- group: other
  title: ''
  type: WhitePapers
  url: https://www.seurat.com/white-papers
- group: operate
  title: ''
  type: FAQ
  url: https://www.seurat.com/seurat-faq
- group: operate
  title: ''
  type: Contact
  url: https://www.seurat.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.seurat.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.seurat.com/privacy-policy
- group: other
  title: ''
  type: BrandAssets
  url: https://www.seurat.com/brand-assets
- group: company
  title: ''
  type: Investors
  url: https://www.seurat.com/for-investors
- group: company
  title: ''
  type: Jobs
  url: https://boards.greenhouse.io/seurat
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/seurat-technologies/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCeIqe1rqv7GzkfdZHoltL-A
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/seurat-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/seurat-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seurat-domain-security.yml
coverage:
  checked: '2026-08-05'
  detail: Seurat Technologies sells 3D-printed metal parts, not software — the entire customer motion is an "upload your part for a quote" form, and the only machine-readable surface on www.seurat.com is the /llms.txt and /_api/mcp site MCP that Wix auto-generates for every site it hosts.
  evidence:
  - status: 200
    url: https://www.seurat.com/llms.txt
  - status: 200
    url: https://www.seurat.com/_api/mcp
  - status: 400
    url: https://www.seurat.com/.well-known/agent-card.json
  - note: Full page inventory (32 URLs) — no developer, docs, API-reference or portal page; and api./docs./developer./portal./app.seurat.com do not resolve in DNS.
    status: 200
    url: https://www.seurat.com/pages-sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: Seurat Technologies is a Wilmington, Massachusetts contract manufacturer that produces high-volume metal parts using its proprietary Area Printing technology, a Laser Powderbed Fusion (LPBF) additive process that decouples print speed from resolution and is positioned as roughly 10x more productive than conventional LPBF. Seurat does not sell 3D printers; it sells parts, qualifying customer designs through its Area Printing Production (APP) qualification program and then mass-producing them at localized factories for consumer electronics, automotive, energy, aerospace and defense OEMs. The company markets its process on reshoring, supply-chain resilience, tariff resistance and decarbonization, and engages customers through a quote / upload-your-part motion rather than any developer-facing product.
image: https://static.wixstatic.com/media/953c5a_7e5f56c496714d66967a49d669bbef21~mv2.jpg/v1/fill/w_2500,h_1598,al_c/953c5a_7e5f56c496714d66967a49d669bbef21~mv2.jpg
layout: provider
mcp_servers:
- description: ''
  name: seurat-mcp.yml
  slug: seurat-mcpyml
modified: '2026-08-05'
name: Seurat Technologies
nav: Providers
network: true
overview: 'Seurat Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Additive Manufacturing, 3D Printing, Metal Manufacturing, and Contract Manufacturing.


  Seurat Technologies'' developer surface includes engineering blog, product news, FAQ, YouTube channel, and 14 more developer resources.'
random_paper: 95
score:
  band: emerging
  composite: 13.3
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.3
  provenance:
    mcp: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: domain-security
  name: Seurat Domain Security
  slug: seurat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: seurat
tags:
- Company
- Additive Manufacturing
- 3D Printing
- Metal Manufacturing
- Contract Manufacturing
- Industrial
- Aerospace
- Automotive
- Defense
- Reshoring
website: https://www.seurat.com/
---
