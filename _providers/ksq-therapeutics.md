---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.0
  scored_at: '2026-08-24'
api_count: 8
apis:
- description: The press_release custom post type behind ksqtx.com — the company news archive. 39 items were returned anonymously on 2026-08-23 (X-WP-Total), spanning the Takeda and Ono collaborations, the CRISPR Th
  name: KSQ Therapeutics Press Releases API
  slug: ksq-therapeutics-press-releases-api
- description: WordPress page collection behind ksqtx.com — Home, About, Platform, Pipeline, Partners, News, Press Releases, Careers and the Expanded Access Policy. 9 items on 2026-08-23. Bodies are Divi page-builde
  name: KSQ Therapeutics Pages API
  slug: ksq-therapeutics-pages-api
- description: WordPress media library — 235 attachments on 2026-08-23, including leadership and board headshots, pipeline and platform graphics, poster PDFs and the homepage background video.
  name: KSQ Therapeutics Media API
  slug: ksq-therapeutics-media-api
- description: Cross-type WordPress search over every REST-exposed post type. 48 results anonymously on 2026-08-23. Returns lightweight {id, title, url, type, subtype} records.
  name: KSQ Therapeutics Search API
  slug: ksq-therapeutics-search-api
- description: The WordPress REST route index, namespace index, registered post types, taxonomies and statuses. 349 routes across 9 namespaces on 2026-08-23. This is the only machine-readable contract KSQ Therapeuti
  name: KSQ Therapeutics Discovery API
  slug: ksq-therapeutics-discovery-api
- description: Category and post_tag term collections. Registered and anonymously reachable; one category term ("Uncategorized", 5 posts) and zero tags on 2026-08-23.
  name: KSQ Therapeutics Taxonomy API
  slug: ksq-therapeutics-taxonomy-api
- description: The core WordPress post collection. Registered and anonymously reachable, but empty on this deployment (X-WP-Total 0 on 2026-08-23) — KSQ publishes news through press_release instead.
  name: KSQ Therapeutics Posts API
  slug: ksq-therapeutics-posts-api
- description: oEmbed 1.0 discovery for ksqtx.com URLs. Verified live anonymously on 2026-08-23 — provider_name "KSQ Therapeutics", provider_url https://ksqtx.com.
  name: KSQ Therapeutics oEmbed API
  slug: ksq-therapeutics-oembed-api
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://ksqtx.com/
- group: company
  title: ''
  type: About
  url: https://ksqtx.com/about/
- group: other
  title: ''
  type: Platform
  url: https://ksqtx.com/platform/
- group: other
  title: ''
  type: Pipeline
  url: https://ksqtx.com/pipeline/
- group: company
  title: ''
  type: Partners
  url: https://ksqtx.com/partners/
- group: company
  title: ''
  type: Blog
  url: https://ksqtx.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://ksqtx.com/feed/
- group: company
  title: ''
  type: News
  url: https://ksqtx.com/press-releases/
- group: company
  title: ''
  type: Careers
  url: https://ksqtx.com/careers/
- group: operate
  title: ''
  type: Support
  url: https://ksqtx.com/contact-us/
- group: other
  title: ''
  type: PatientResources
  url: https://ksqtx.com/eap/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ksqtx
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ksqtx/TRACE
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/10414448/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/KSQ_TX
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/ksq-therapeutics_stock/
- group: auth
  title: ''
  type: Authentication
  url: authentication/ksq-therapeutics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ksq-therapeutics-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ksq-therapeutics-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ksq-therapeutics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ksq-therapeutics-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ksq-therapeutics-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ksq-therapeutics-content-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ksq-therapeutics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ksq-therapeutics-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/ksq-therapeutics-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/ksq-therapeutics-cli.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ksq-therapeutics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ksq-therapeutics-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-23'
description: 'KSQ Therapeutics is a clinical-stage biotechnology company headquartered at 4 Maguire Road in Lexington, Massachusetts, founded in 2015 by pioneers of CRISPR screening and functional genomics. Its proprietary CRISPRomics platform runs genome-scale CRISPR/Cas9 functional genomic screens across cancer models and immune cell types to identify therapeutic targets that directly correlate genomic function to disease. The company applies those targets in two directions: CRISPR/Cas9-engineered tumor-infiltrating lymphocyte (eTIL) cell therapies, where a single gene is inactivated to increase the tumor-killing capacity of a patient''s own T cells — KSQ-001EX (SOCS1 inactivated) and KSQ-004EX (SOCS1 and Regnase-1 inactivated) — and small molecules such as KSQ-4279, a first-in-class USP1 inhibitor for advanced solid tumors. KSQ has run broad discovery collaborations with Takeda, licensed cell-therapy technology with CRISPR Therapeutics, partnered manufacturing with CTMC, and sold multiple
  research-stage oncology programs to Ono Pharmaceutical. Investors include Flagship Pioneering, ARCH Venture Partners, Polaris Partners, Alexandria, Alpha Wave Global, Baillie Gifford, Invus, LG and Lilly Asia Ventures. KSQ Therapeutics runs no developer program and publishes no product API, developer portal, OpenAPI or API reference. The only machine-readable surfaces reachable without credentials are the WordPress REST content API behind ksqtx.com, an All in One SEO generated /llms.txt, and the open-source bioinformatics code in its public GitHub organization — all catalogued here.'
image: https://ksqtx.com/wp-content/uploads/2024/02/KSQ-logo-color-RegTM.png
layout: provider
modified: '2026-08-23'
name: KSQ Therapeutics
nav: Providers
network: true
overview: 'KSQ Therapeutics publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Press Releases API, Pages API, Media API, and 5 more. Tagged areas include Company, Biotechnology, Life Sciences, Therapeutics, and Oncology.


  KSQ Therapeutics'' developer surface includes engineering blog, product news, support, authentication, CLI, and 25 more developer resources.'
plans:
- name: Ksq Therapeutics Plans Pricing
  plan_count: 0
  slug: ksq-therapeutics-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Ksq Therapeutics Rate Limits
  slug: ksq-therapeutics-rate-limits
score:
  band: thin
  composite: 32.1
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 30.3
    contract_quality: 50.3
    developer_ergonomics: 33.3
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: authentication
  name: Ksq Therapeutics Authentication
  slug: ksq-therapeutics-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Ksq Therapeutics Domain Security
  slug: ksq-therapeutics-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: ksq-therapeutics
tags:
- Company
- Biotechnology
- Life Sciences
- Therapeutics
- Oncology
- Genomics
- CRISPR
- Gene Editing
- Cell Therapy
- Clinical Stage
- Functional Genomics
- content-api
website: https://ksqtx.com/
---
