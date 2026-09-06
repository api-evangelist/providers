---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://www.ascend-adv.com/wp-json
  baseurl_source: declared
  description: Job openings custom post type.
  name: Ascend Advanced Therapies Careers API
  slug: ascend-advanced-therapies-careers-api
- baseURL: https://www.ascend-adv.com/wp-json
  baseurl_source: declared
  description: Site, content-type, and taxonomy metadata.
  name: Ascend Advanced Therapies Discovery API
  slug: ascend-advanced-therapies-discovery-api
- baseURL: https://www.ascend-adv.com/wp-json
  baseurl_source: declared
  description: Media library attachments.
  name: Ascend Advanced Therapies Media API
  slug: ascend-advanced-therapies-media-api
- baseURL: https://www.ascend-adv.com/wp-json
  baseurl_source: declared
  description: oEmbed discovery for site URLs.
  name: Ascend Advanced Therapies oEmbed API
  slug: ascend-advanced-therapies-oembed-api
- baseURL: https://www.ascend-adv.com/wp-json
  baseurl_source: declared
  description: Static site pages.
  name: Ascend Advanced Therapies Pages API
  slug: ascend-advanced-therapies-pages-api
- baseURL: https://www.ascend-adv.com/wp-json
  baseurl_source: declared
  description: News & Insights articles, blogs, and webinar entries.
  name: Ascend Advanced Therapies Posts API
  slug: ascend-advanced-therapies-posts-api
- baseURL: https://www.ascend-adv.com/wp-json
  baseurl_source: declared
  description: Cross-content site search.
  name: Ascend Advanced Therapies Search API
  slug: ascend-advanced-therapies-search-api
- baseURL: https://www.ascend-adv.com/wp-json
  baseurl_source: declared
  description: Categories and tags.
  name: Ascend Advanced Therapies Taxonomy API
  slug: ascend-advanced-therapies-taxonomy-api
artifact_total: 19
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/ascend-advanced-therapies-capability-edges.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/ascend-advanced-therapies-monitor-news-insights.md
- group: agent
  title: ''
  type: X-MCPServerCandidate
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
modified: '2026-07-19'
name: Ascend Advanced Therapies
nav: Providers
network: true
overview: 'Ascend Advanced Therapies publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Careers API, Discovery API, Media API, and 5 more. Tagged areas include Company, Biotechnology, Gene Therapy, Cell Therapy, and Contract Manufacturing.


  Ascend Advanced Therapies'' developer surface includes engineering blog and 16 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 51.2
    developer_ergonomics: 16.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 31.2
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
    score: 37.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
