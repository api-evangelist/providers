---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.7
  scored_at: '2026-08-10'
api_count: 8
apis:
- description: Belharra's three custom post types — press-release (4 items), company-news (21 items) and multimedia-file (10 items).
  name: Belharra Therapeutics Custom Types API
  slug: belharra-therapeutics-custom-types-api
- description: Route, type, taxonomy, status and author discovery documents.
  name: Belharra Therapeutics Discovery API
  slug: belharra-therapeutics-discovery-api
- description: Media library (430 attachments at harvest time).
  name: Belharra Therapeutics Media API
  slug: belharra-therapeutics-media-api
- description: oEmbed 1.0 provider endpoint for belharratx.com URLs.
  name: Belharra Therapeutics Oembed API
  slug: belharra-therapeutics-oembed-api
- description: Corporate pages (29 published at harvest time).
  name: Belharra Therapeutics Pages API
  slug: belharra-therapeutics-pages-api
- description: Blog/news archive (10 published at harvest time), categorised as Company News or Press Releases.
  name: Belharra Therapeutics Posts API
  slug: belharra-therapeutics-posts-api
- description: Cross-content search across published objects (74 searchable records at harvest time).
  name: Belharra Therapeutics Search API
  slug: belharra-therapeutics-search-api
- description: Categories and tags. Two categories are registered (Company News, Press Releases); the post_tag taxonomy is registered but empty.
  name: Belharra Therapeutics Taxonomy API
  slug: belharra-therapeutics-taxonomy-api
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://belharratx.com/
- group: company
  title: ''
  type: About
  url: https://belharratx.com/about/
- group: other
  title: ''
  type: OurStory
  url: https://belharratx.com/about/our-story/
- group: other
  title: ''
  type: Leadership
  url: https://belharratx.com/about/our-team/leadership/
- group: other
  title: ''
  type: Platform
  url: https://belharratx.com/our-approach/platform/
- group: other
  title: ''
  type: Publications
  url: https://belharratx.com/our-approach/publications/
- group: company
  title: ''
  type: Partners
  url: https://belharratx.com/partners/
- group: company
  title: ''
  type: News
  url: https://belharratx.com/newsroom/
- group: operate
  title: ''
  type: PressReleases
  url: https://belharratx.com/press-releases/
- group: company
  title: ''
  type: BlogRSS
  url: https://belharratx.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://belharratx.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://belharratx.com/contact/
- group: other
  title: ''
  type: PatientResources
  url: https://belharratx.com/patients/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://belharratx.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://belharratx.com/terms/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/belharra-tx
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/belharra-therapeutics/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.nasdaqprivatemarket.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/belharra-therapeutics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/belharra-therapeutics-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/belharra-therapeutics-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/belharra-therapeutics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/belharra-therapeutics-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/belharra-therapeutics-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/belharra-therapeutics-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/belharra-therapeutics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/belharra-therapeutics-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-06'
description: Belharra Therapeutics is a privately held, next-generation chemoproteomics company headquartered at 3985 Sorrento Valley Boulevard, Suite C, San Diego, California, that is building small molecule therapeutics against targets the industry has long considered undruggable. Its Searchlight platform is an unbiased chemoproteomics screening system designed to illuminate novel, previously invisible binding pockets on high-value proteins across the proteome — the company states it can identify small molecule binders for any binding site, on any protein, in any conformational state, in any cell type, and reported having identified more than four thousand drug-like pocket probes by January 2024. The company was incubated and supported by Versant Ventures out of foundational chemoproteomics research at The Scripps Research Institute, with co-founders including Christopher G. Parker and Benjamin Cravatt of Scripps Research and Stuart Schreiber of the Broad Institute of MIT and Harvard.
  Jeff Jonker was hired as chief executive officer in September 2021, and the company debuted publicly in January 2023 with $130 million in hand — a $50 million Series A led by Versant Ventures plus an $80 million upfront payment from a multi-year Genentech collaboration spanning oncology, immuno-oncology, autoimmune and neurodegenerative disease. In June 2024 it announced a strategic immunology collaboration with Sanofi carrying up to $40 million in upfront and near-term milestone payments, and in January 2025 it appointed Sean Buchanan as chief scientific officer. Belharra runs no developer program and publishes no product API, developer portal, API reference, or SDK. The only machine-readable surface reachable without credentials is the WordPress REST content API behind belharratx.com, catalogued here.
image: https://belharratx.com/wp-content/uploads/2024/12/belharra-logo.png
layout: provider
modified: '2026-08-06'
name: Belharra Therapeutics
nav: Providers
network: true
overview: 'Belharra Therapeutics publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Custom Types API, Discovery API, Media API, and 5 more. Tagged areas include Company, biotechnology, pharmaceuticals, chemoproteomics, and drug-discovery.


  Belharra Therapeutics'' developer surface includes product news, authentication, and 26 more developer resources.'
random_paper: 87
score:
  band: thin
  composite: 32.3
  delta: -0.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 56.9
    developer_ergonomics: 12.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 32.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/belharra-therapeutics/refs/heads/main/screenshots/belharra-therapeutics-2026-08-07T162258.png
security:
- kind: authentication
  name: Belharra Therapeutics Authentication
  slug: belharra-therapeutics-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Belharra Therapeutics Domain Security
  slug: belharra-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: belharra-therapeutics
tags:
- Company
- biotechnology
- pharmaceuticals
- chemoproteomics
- drug-discovery
- small-molecule-therapeutics
- proteomics
- life-sciences
- oncology
- immunology
- content-api
website: https://belharratx.com/
---
