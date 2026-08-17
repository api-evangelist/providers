---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-08-17'
api_count: 8
apis:
- description: Job openings custom post type.
  name: Ascend Advanced Therapies Careers API
  slug: ascend-advanced-therapies-careers-api
- description: Site, content-type, and taxonomy metadata.
  name: Ascend Advanced Therapies Discovery API
  slug: ascend-advanced-therapies-discovery-api
- description: Media library attachments.
  name: Ascend Advanced Therapies Media API
  slug: ascend-advanced-therapies-media-api
- description: oEmbed discovery for site URLs.
  name: Ascend Advanced Therapies oEmbed API
  slug: ascend-advanced-therapies-oembed-api
- description: Static site pages.
  name: Ascend Advanced Therapies Pages API
  slug: ascend-advanced-therapies-pages-api
- description: News & Insights articles, blogs, and webinar entries.
  name: Ascend Advanced Therapies Posts API
  slug: ascend-advanced-therapies-posts-api
- description: Cross-content site search.
  name: Ascend Advanced Therapies Search API
  slug: ascend-advanced-therapies-search-api
- description: Categories and tags.
  name: Ascend Advanced Therapies Taxonomy API
  slug: ascend-advanced-therapies-taxonomy-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ascend Advanced Therapies Content API (WordPress REST) Careers API
  slug: open-ascend-advanced-therapies-careers-api
- collection_type: open
  name: Ascend Advanced Therapies Content API (WordPress REST) Careers Discovery API
  slug: open-ascend-advanced-therapies-discovery-api
- collection_type: open
  name: Ascend Advanced Therapies Content API (WordPress REST) Careers Media API
  slug: open-ascend-advanced-therapies-media-api
- collection_type: open
  name: Ascend Advanced Therapies Content API (WordPress REST) Careers oEmbed API
  slug: open-ascend-advanced-therapies-oembed-api
- collection_type: open
  name: Ascend Advanced Therapies Content API (WordPress REST) Careers Pages API
  slug: open-ascend-advanced-therapies-pages-api
- collection_type: open
  name: Ascend Advanced Therapies Content API (WordPress REST) Careers Posts API
  slug: open-ascend-advanced-therapies-posts-api
- collection_type: open
  name: Ascend Advanced Therapies Content API (WordPress REST) Careers Search API
  slug: open-ascend-advanced-therapies-search-api
- collection_type: open
  name: Ascend Advanced Therapies Content API (WordPress REST) Careers Taxonomy API
  slug: open-ascend-advanced-therapies-taxonomy-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/ascend-advanced-therapies-monitor-news-insights.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ascend-advanced-therapies-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ascend-advanced-therapies-wp-rest-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.ascend-adv.com/
- group: company
  title: ''
  type: About
  url: https://www.ascend-adv.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://www.ascend-adv.com/news-insights/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.ascend-adv.com/feed/
- group: operate
  title: ''
  type: Contact
  url: https://www.ascend-adv.com/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://www.ascend-adv.com/careers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ascend-adv.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ascend-adv.com/privacy-policy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.ascend-adv.com/cookie-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ascend-advanced-therapies/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ascend-advanced-therapies-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ascend-advanced-therapies-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ascend-advanced-therapies-llms.txt
created: '2026-07-17'
description: Ascend Advanced Therapies is a gene-to-GMP contract development and manufacturing organization (CDMO) for advanced therapies, specializing in adeno-associated virus (AAV) vector development and manufacture for gene therapies, immunotherapies, oncolytics, and vaccines. Formed in 2023 when expert teams merged behind more than $130M of funding, and aligned with ABL, Inc. since late 2024, Ascend operates GMP manufacturing, aseptic fill-finish, and analytical facilities in Rockville, Maryland and Alachua, Florida alongside European capacity. Services span process development, gene therapy formulation, scalable manufacturing, in-house fill-finish, GMP QC testing, long-read NGS for viral vectors, and potency assay development, built on its EpyQ production system and proprietary AAV yield enhancers. Ascend is a life-science manufacturer rather than a software vendor and publishes no commercial product API; the only machine-readable interface it exposes is the WordPress REST content
  API behind its corporate website, captured here for discovery.
image: https://www.ascend-adv.com/wp-content/uploads/2025/02/cropped-favicon-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: ascend-advanced-therapies-mcp.yml
  slug: ascend-advanced-therapies-mcpyml
modified: '2026-07-19'
name: Ascend Advanced Therapies
nav: Providers
network: true
overview: 'Ascend Advanced Therapies publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Careers API, Discovery API, Media API, and 5 more. Tagged areas include Company, Biotechnology, Gene Therapy, Cell Therapy, and Contract Manufacturing.


  Ascend Advanced Therapies'' developer surface includes engineering blog and 15 more developer resources.'
random_paper: 115
score:
  band: emerging
  composite: 27.3
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 56.2
    developer_ergonomics: 6.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 27.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ascend-advanced-therapies/refs/heads/main/screenshots/ascend-advanced-therapies-2026-07-25T201402.png
security:
- kind: authentication
  name: Ascend Advanced Therapies Authentication
  slug: ascend-advanced-therapies-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ascend Advanced Therapies Domain Security
  slug: ascend-advanced-therapies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ascend-advanced-therapies
tags:
- Company
- Biotechnology
- Gene Therapy
- Cell Therapy
- Contract Manufacturing
- Life Sciences
- Pharmaceuticals
- CDMO
- AAV
website: https://www.ascend-adv.com/
---
