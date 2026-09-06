---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://www.flaretx.com/wp-json
  baseurl_source: declared
  description: Comment collection. Registered and reachable, but empty — no post on this deployment carries comments.
  name: Flare Therapeutics Comments API
  slug: flare-therapeutics-comments-api
- baseURL: https://www.flaretx.com/wp-json
  baseurl_source: declared
  description: Route, type, taxonomy and status discovery documents.
  name: Flare Therapeutics Discovery API
  slug: flare-therapeutics-discovery-api
- baseURL: https://www.flaretx.com/wp-json
  baseurl_source: declared
  description: Media library (419 attachments at harvest time — 400 images, 19 application/* documents, 0 video).
  name: Flare Therapeutics Media API
  slug: flare-therapeutics-media-api
- baseURL: https://www.flaretx.com/wp-json
  baseurl_source: declared
  description: oEmbed 1.0 provider endpoint for www.flaretx.com URLs.
  name: Flare Therapeutics Oembed API
  slug: flare-therapeutics-oembed-api
- baseURL: https://www.flaretx.com/wp-json
  baseurl_source: declared
  description: Corporate pages (14 published at harvest time) — home, about, science, pipeline, fx-909, fx-111, publications, news, press-releases, join-us, contact, privacy-policy, terms-of-use, flaretx.
  name: Flare Therapeutics Pages API
  slug: flare-therapeutics-pages-api
- baseURL: https://www.flaretx.com/wp-json
  baseurl_source: declared
  description: Reusable block patterns and their categories. Registered and anonymously reachable, but both report zero published items.
  name: Flare Therapeutics Patterns API
  slug: flare-therapeutics-patterns-api
- baseURL: https://www.flaretx.com/wp-json
  baseurl_source: declared
  description: News archive — press releases, news coverage and scientific presentations, 2021-05-13 (Series A launch) to 2026-06-30 (Series C and CEO appointment). 42 published at harvest time.
  name: Flare Therapeutics Posts API
  slug: flare-therapeutics-posts-api
- baseURL: https://www.flaretx.com/wp-json
  baseurl_source: declared
  description: Cross-content search across published objects.
  name: Flare Therapeutics Search API
  slug: flare-therapeutics-search-api
- baseURL: https://www.flaretx.com/wp-json
  baseurl_source: declared
  description: Categories and tags. Four categories are registered (News 36, Press Release 8, FlareTx 3, Uncategorized 3); the post_tag taxonomy is registered but empty.
  name: Flare Therapeutics Taxonomy API
  slug: flare-therapeutics-taxonomy-api
artifact_total: 14
collections:
- collection_type: open
  name: Flare Therapeutics Content API
  slug: open-flare-therapeutics-content
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/flare-therapeutics-content-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flare-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.flaretx.com/
- group: company
  title: ''
  type: About
  url: https://www.flaretx.com/about/
- group: other
  title: ''
  type: Science
  url: https://www.flaretx.com/science/
- group: other
  title: ''
  type: Pipeline
  url: https://www.flaretx.com/pipeline/
- group: other
  title: ''
  type: Publications
  url: https://www.flaretx.com/publications/
- group: company
  title: ''
  type: News
  url: https://www.flaretx.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.flaretx.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://www.flaretx.com/join-us/
- group: operate
  title: ''
  type: Contact
  url: https://www.flaretx.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flaretx.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flaretx.com/terms-of-use/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flare-therapeutics
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FlareTx
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/flare-therapeutics_stock/
- group: auth
  title: ''
  type: Authentication
  url: authentication/flare-therapeutics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flare-therapeutics-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flare-therapeutics-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/flare-therapeutics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flare-therapeutics-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/flare-therapeutics-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flare-therapeutics-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-12'
description: Flare Therapeutics is a clinical-stage biotechnology company headquartered at 400 Technology Square, Cambridge, Massachusetts, developing small-molecule precision medicines against transcription factors — a target class long considered undruggable. Its platform combines a "switch site" hypothesis with cell-based ligand discovery and chemoproteomics to find binding pockets on transcription factors that control cancer cell states. The company launched publicly in May 2021 with an $82 million Series A led by Third Rock Ventures, and closed an $85 million insider-led Series C on 30 June 2026 led by Third Rock Ventures and Nextech Invest with Pfizer Ventures, Boxer Capital, GordonMD Global Investments, Invus, Casdin Capital, Eli Lilly, Novartis, Agent Capital and Eventide Asset Management participating, appointing Anna Protopapas as Chief Executive Officer at the same time. Its clinical-stage lead FX-909 is a PPARG inverse agonist in advanced urothelial cancer; FX-111 is an androgen-receptor-directed
  program in prostate cancer that received FDA IND clearance ahead of a clinical start in the third quarter of 2026. Flare also runs a discovery collaboration with Roche on undrugged transcription factor targets in oncology. Flare Therapeutics operates no developer program and publishes no product API, developer portal or API documentation. The only machine-readable surface reachable without credentials is the WordPress REST content API behind www.flaretx.com, catalogued here.
image: https://www.flaretx.com/wp-content/uploads/2021/05/Flare-website-social-card-051221.jpg
layout: provider
modified: '2026-08-12'
name: Flare Therapeutics
nav: Providers
network: true
overview: 'Flare Therapeutics publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Discovery API, Media API, and 6 more. Tagged areas include Company, Biotechnology, Pharmaceuticals, Oncology, and Precision Medicine.


  Flare Therapeutics'' developer surface includes product news, authentication, and 22 more developer resources.'
plans:
- name: Flare Therapeutics Plans Pricing
  plan_count: 0
  slug: flare-therapeutics-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Flare Therapeutics Rate Limits
  slug: flare-therapeutics-rate-limits
score:
  band: thin
  composite: 29.6
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
    contract_quality: 49.1
    developer_ergonomics: 13.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 29.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flare-therapeutics/refs/heads/main/screenshots/flare-therapeutics-2026-09-02T145521.png
security:
- kind: authentication
  name: Flare Therapeutics Authentication
  slug: flare-therapeutics-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Flare Therapeutics Domain Security
  slug: flare-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flare-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Oncology
- Precision Medicine
- transcription-factors
- Drug Discovery
- Clinical Trials
- Life Sciences
- content-api
website: https://www.flaretx.com/
---
