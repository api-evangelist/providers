---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://alzheon.com/wp-json
  baseurl_source: declared
  description: Comments (the site publishes none).
  name: Alzheon Comments API
  slug: alzheon-comments-api
- baseURL: https://alzheon.com/wp-json
  baseurl_source: declared
  description: The route index / discovery document.
  name: Alzheon Discovery API
  slug: alzheon-discovery-api
- baseURL: https://alzheon.com/wp-json
  baseurl_source: declared
  description: Avada FAQ custom post type.
  name: Alzheon FAQ API
  slug: alzheon-faq-api
- baseURL: https://alzheon.com/wp-json
  baseurl_source: declared
  description: 'The media library: images, posters, publication PDFs.'
  name: Alzheon Media API
  slug: alzheon-media-api
- baseURL: https://alzheon.com/wp-json
  baseurl_source: declared
  description: Registered types, taxonomies and statuses.
  name: Alzheon Metadata API
  slug: alzheon-metadata-api
- baseURL: https://alzheon.com/wp-json
  baseurl_source: declared
  description: oEmbed representations of alzheon.com URLs.
  name: Alzheon O Embed API
  slug: alzheon-oembed-api
- baseURL: https://alzheon.com/wp-json
  baseurl_source: declared
  description: 'Static site pages: science, pipeline, people, patients, careers.'
  name: Alzheon Pages API
  slug: alzheon-pages-api
- baseURL: https://alzheon.com/wp-json
  baseurl_source: declared
  description: Avada portfolio custom post type.
  name: Alzheon Portfolio API
  slug: alzheon-portfolio-api
- baseURL: https://alzheon.com/wp-json
  baseurl_source: declared
  description: Press releases and in-the-news items published by Alzheon.
  name: Alzheon Posts API
  slug: alzheon-posts-api
- baseURL: https://alzheon.com/wp-json
  baseurl_source: declared
  description: Cross-content-type search.
  name: Alzheon Search API
  slug: alzheon-search-api
- baseURL: https://alzheon.com/wp-json
  baseurl_source: declared
  description: Categories and tags used to classify content.
  name: Alzheon Taxonomy API
  slug: alzheon-taxonomy-api
- baseURL: https://alzheon.com/wp-json
  baseurl_source: declared
  description: Publicly listed content authors.
  name: Alzheon Users API
  slug: alzheon-users-api
artifact_total: 15
collections:
- collection_type: open
  name: Alzheon Content API (WordPress REST)
  slug: open-alzheon-content
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/alzheon-content-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://alzheon.com/
- group: company
  title: ''
  type: Blog
  url: https://alzheon.com/media/press-releases/
- group: company
  title: ''
  type: BlogRSS
  url: https://alzheon.com/feed/
- group: company
  title: ''
  type: News
  url: https://alzheon.com/media/in-the-news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alzheon.com/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://alzheon.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://alzheon.com/careers/
- group: company
  title: ''
  type: About
  url: https://alzheon.com/people/about-us/
- group: other
  title: ''
  type: Pipeline
  url: https://alzheon.com/science/pipeline/
- group: other
  title: ''
  type: Publications
  url: https://alzheon.com/science/publications/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alzheon
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Alzheon
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/alzheon_stock/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alzheon-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alzheon-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alzheon-llms.txt
created: '2026-07-31'
description: Alzheon, Inc. is a privately held clinical-stage biopharmaceutical company founded in 2013 and headquartered at 111 Speen Street, Framingham, Massachusetts, developing oral small-molecule therapeutics and diagnostics for Alzheimer's disease and other neurodegenerative disorders. Its lead candidate, valiltramiprosate (ALZ-801) — a valine-conjugated prodrug of tramiprosate that blocks the formation of neurotoxic soluble beta-amyloid oligomers — has FDA Fast Track designation and completed the pivotal APOLLOE4 Phase 3 trial in APOE4/4 homozygotes with early Alzheimer's disease. Alzheon operates no product or developer API and publishes no developer portal, SDKs or API documentation; its corporate site does serve the standard WordPress REST API anonymously, which makes its press releases, science pages and media library machine-readable.
image: https://alzheon.com/wp-content/uploads/2016/03/alzheon-logo2.svg
layout: provider
modified: '2026-07-31'
name: Alzheon
nav: Providers
network: true
overview: 'Alzheon publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Discovery API, FAQ API, and 9 more. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Clinical Trials.


  Alzheon''s developer surface includes engineering blog, product news, and 16 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 13.7
    developer_ergonomics: 16.1
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 17.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alzheon/refs/heads/main/screenshots/alzheon-2026-08-07T161303.png
security:
- kind: authentication
  name: Alzheon Authentication
  slug: alzheon-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Alzheon Domain Security
  slug: alzheon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alzheon
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Clinical Trials
- Alzheimers Disease
- Neurology
- Drug Development
- Healthcare
- Private Company
website: https://alzheon.com/
---
