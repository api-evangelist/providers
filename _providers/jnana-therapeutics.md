---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://www.jnanatx.com/wp-json
  baseurl_source: declared
  description: Comment collection. Registered and reachable, but empty — no post carries comments.
  name: Jnana Therapeutics Comments API
  slug: jnana-therapeutics-comments-api
- baseURL: https://www.jnanatx.com/wp-json
  baseurl_source: declared
  description: Route, type, taxonomy and status discovery documents.
  name: Jnana Therapeutics Discovery API
  slug: jnana-therapeutics-discovery-api
- baseURL: https://www.jnanatx.com/wp-json
  baseurl_source: declared
  description: Media library (376 attachments at harvest time).
  name: Jnana Therapeutics Media API
  slug: jnana-therapeutics-media-api
- baseURL: https://www.jnanatx.com/wp-json
  baseurl_source: declared
  description: oEmbed 1.0 provider endpoint for www.jnanatx.com URLs.
  name: Jnana Therapeutics Oembed API
  slug: jnana-therapeutics-oembed-api
- baseURL: https://www.jnanatx.com/wp-json
  baseurl_source: declared
  description: Corporate pages — home, RAPID platform, programs, team, join us, news, contact, privacy policy, terms of use (9 published at harvest time).
  name: Jnana Therapeutics Pages API
  slug: jnana-therapeutics-pages-api
- baseURL: https://www.jnanatx.com/wp-json
  baseurl_source: declared
  description: News archive — press releases, in-the-news coverage, presentations and insights (62 published at harvest time).
  name: Jnana Therapeutics Posts API
  slug: jnana-therapeutics-posts-api
- baseURL: https://www.jnanatx.com/wp-json
  baseurl_source: declared
  description: Cross-content search across published objects (73 indexed at harvest time).
  name: Jnana Therapeutics Search API
  slug: jnana-therapeutics-search-api
- baseURL: https://www.jnanatx.com/wp-json
  baseurl_source: declared
  description: Yoast SEO head-metadata document for a given site URL.
  name: Jnana Therapeutics Seo API
  slug: jnana-therapeutics-seo-api
- baseURL: https://www.jnanatx.com/wp-json
  baseurl_source: declared
  description: 'Post categories (7 registered — press-releases 43, in-the-news 16, presentations 3, insights 2, publications 0, blogs 0, videos 0) and team departments (4 registered). The core `post_tag` taxonomy is '
  name: Jnana Therapeutics Taxonomy API
  slug: jnana-therapeutics-taxonomy-api
- baseURL: https://www.jnanatx.com/wp-json
  baseurl_source: declared
  description: '`team` custom post type — leadership, board and scientific advisory profiles (9 published at harvest time).'
  name: Jnana Therapeutics Team API
  slug: jnana-therapeutics-team-api
- baseURL: https://www.jnanatx.com/wp-json
  baseurl_source: declared
  description: Genesis theme reading-settings and breadcrumb documents.
  name: Jnana Therapeutics Theme API
  slug: jnana-therapeutics-theme-api
- baseURL: https://www.jnanatx.com/wp-json
  baseurl_source: declared
  description: Author collection (4 records). Anonymously readable, exposing WordPress author display names and slugs. Flagged in conventions/ as an exposure worth reviewing, not a documented product.
  name: Jnana Therapeutics Users API
  slug: jnana-therapeutics-users-api
artifact_total: 16
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jnana-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jnanatx.com/
- group: other
  title: ''
  type: Platform
  url: https://www.jnanatx.com/rapid-platform/
- group: other
  title: ''
  type: Programs
  url: https://www.jnanatx.com/programs/
- group: other
  title: ''
  type: Team
  url: https://www.jnanatx.com/team/
- group: company
  title: ''
  type: News
  url: https://www.jnanatx.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.jnanatx.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://www.jnanatx.com/join-us/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.jnanatx.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jnanatx.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jnanatx.com/terms-of-use/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jnana-therapeutics/
- group: other
  title: ''
  type: X
  url: https://x.com/jnanatx
- group: other
  title: ''
  type: ParentCompany
  url: https://www.otsuka.co.jp/en/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/jnana-therapeutics_stock/
- group: auth
  title: ''
  type: Authentication
  url: authentication/jnana-therapeutics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jnana-therapeutics-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jnana-therapeutics-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/jnana-therapeutics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jnana-therapeutics-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/jnana-therapeutics-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/jnana-therapeutics-content-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/jnana-therapeutics-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jnana-therapeutics-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/jnana-therapeutics-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jnana-therapeutics-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-23'
description: 'Jnana Therapeutics Inc. is a biotechnology company headquartered at One Design Center Place, Suite 19-400, Boston, Massachusetts, that built RAPID — Reactive Affinity Probe Interaction Discovery — a next-generation chemoproteomics platform for discovering small-molecule medicines against target classes that conventional screening has struggled to drug, including SLC transporters, transcription factors, signaling scaffold proteins, phosphatases, GPCRs and helicases. RAPID runs in living cells: a proprietary Reactive Affinity Probe library covalently labels druggable pockets on a validated target, and a proprietary detection technology then screens large drug-like compound libraries for binders that displace the probe, yielding allosteric inhibitors, localization modulators and molecular glues without iterative structural biology. Its internal pipeline focuses on phenylketonuria (PKU) — where JNT-517, an oral inhibitor acting at a cryptic allosteric site on the SLC6A19 transporter,
  reached Phase 1b/2 — and on immune-mediated diseases including targets such as interferon regulatory factor 3 (IRF3), alongside biopharma collaborations that include Roche. Otsuka Pharmaceutical Co., Ltd. completed its acquisition of Jnana on 23 September 2024 for $800 million plus up to $325 million in development and regulatory milestones, making Jnana a direct subsidiary of Otsuka America, Inc.; Otsuka initiated a global Phase 3 trial of repinatrabit in PKU in December 2025. Jnana Therapeutics runs no developer program and publishes no product API, developer portal, API reference or SDK. The only machine-readable surface reachable without credentials is the WordPress REST content API behind www.jnanatx.com, catalogued here.'
image: https://www.jnanatx.com/wp-content/uploads/2022/09/cropped-android-chrome-512x512-1.png
layout: provider
modified: '2026-08-23'
name: Jnana Therapeutics
nav: Providers
network: true
overview: 'Jnana Therapeutics publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Discovery API, Media API, and 9 more. Tagged areas include Company, Biotechnology, Pharmaceuticals, Drug Discovery, and chemoproteomics.


  Jnana Therapeutics'' developer surface includes product news, authentication, and 25 more developer resources.'
plans:
- name: Jnana Therapeutics Plans Pricing
  plan_count: 0
  slug: jnana-therapeutics-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Jnana Therapeutics Rate Limits
  slug: jnana-therapeutics-rate-limits
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 18
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
    contract_quality: 49.5
    developer_ergonomics: 13.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 29.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jnana-therapeutics/refs/heads/main/screenshots/jnana-therapeutics-2026-09-02T145947.png
security:
- kind: authentication
  name: Jnana Therapeutics Authentication
  slug: jnana-therapeutics-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Jnana Therapeutics Domain Security
  slug: jnana-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jnana-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Drug Discovery
- chemoproteomics
- Rare Disease
- Immunology
- Life Sciences
- Clinical Trials
- content-api
website: https://www.jnanatx.com/
---
