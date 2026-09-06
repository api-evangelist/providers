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
api_count: 2
apis:
- baseURL: https://neomorph.com/wp-json
  baseurl_source: declared
  description: Corporate pages — About, Platform, Pipeline, Publications, Patients, Careers, News, Contact and the policy set (15 published at harvest time, including the NEO-811 programme page).
  name: Neomorph Pages API
  slug: neomorph-pages-api
- baseURL: https://neomorph.com/wp-json
  baseurl_source: declared
  description: Publications custom post type — the peer-reviewed molecular glue and targeted protein degradation literature Neomorph's founders and scientists authored (11 published at harvest time, from the 2014 CR
  name: Neomorph Publications API
  slug: neomorph-publications-api
- baseURL: https://neomorph.com/wp-json
  baseurl_source: declared
  description: Team custom post type and its team_category taxonomy — management, board of directors and scientific founders (19 people across 4 registered categories at harvest time).
  name: Neomorph Team API
  slug: neomorph-team-api
- baseURL: https://neomorph.com/wp-json
  baseurl_source: declared
  description: Media library — team portraits, pipeline and platform figures, and press assets (111 attachments at harvest time).
  name: Neomorph Media API
  slug: neomorph-media-api
- baseURL: https://neomorph.com/wp-json
  baseurl_source: declared
  description: Comment collection. Registered and anonymously reachable, but empty — no post on this deployment carries comments.
  name: Neomorph Comments API
  slug: neomorph-comments-api
- baseURL: https://neomorph.com/wp-json
  baseurl_source: declared
  description: Cross-content search across every publicly queryable object type on the deployment (post, page, team, resource).
  name: Neomorph Search API
  slug: neomorph-search-api
- baseURL: https://neomorph.com/wp-json
  baseurl_source: declared
  description: Route, post-type, taxonomy and status discovery documents — the 432-route, 23-namespace index the deployment publishes about itself.
  name: Neomorph Discovery API
  slug: neomorph-discovery-api
- baseURL: https://neomorph.com/wp-json
  baseurl_source: declared
  description: oEmbed 1.0 provider endpoint for neomorph.com permalinks.
  name: Neomorph oEmbed API
  slug: neomorph-oembed-api
- baseURL: https://neomorph.com/wp-json
  baseurl_source: declared
  description: 'News taxonomy. Two terms are registered on this deployment: Press Release (13 posts) and In The Media (1 post).'
  name: Neomorph Categories API
  slug: neomorph-categories-api
- baseURL: https://neomorph.com/wp-json
  baseurl_source: declared
  description: News archive - Neomorph press releases and media coverage (14 published at harvest time, spanning the December 2020 $109M Series A through the May 2026 appointment of Robert J. Hugin as Chairman of th
  name: Neomorph Posts API
  slug: neomorph-posts-api
- baseURL: https://neomorph.com/wp-json
  baseurl_source: declared
  description: The post_tag taxonomy is registered and anonymously reachable but empty - no term has been created on this deployment.
  name: Neomorph Tags API
  slug: neomorph-tags-api
- baseURL: https://neomorph.com/wp-json
  baseurl_source: declared
  description: 'team_category taxonomy grouping the Team collection. Four terms are registered: Management (11), Board of Directors (7), Scientific Founders (4) and Scientific Advisory Board (0).'
  name: Neomorph Team Categories API
  slug: neomorph-team-categories-api
artifact_total: 16
common:
- group: company
  title: ''
  type: Website
  url: https://neomorph.com/
- group: company
  title: ''
  type: About
  url: https://neomorph.com/about-us/
- group: other
  title: ''
  type: Platform
  url: https://neomorph.com/platform/
- group: other
  title: ''
  type: Pipeline
  url: https://neomorph.com/pipeline/
- group: other
  title: ''
  type: Publications
  url: https://neomorph.com/publications/
- group: other
  title: ''
  type: PatientResources
  url: https://neomorph.com/patients/
- group: company
  title: ''
  type: News
  url: https://neomorph.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://neomorph.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://neomorph.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://neomorph.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://neomorph.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://neomorph.com/terms-of-use/
- group: other
  title: ''
  type: CookiePolicy
  url: https://neomorph.com/cookie-policy/
- group: other
  title: ''
  type: Accessibility
  url: https://neomorph.com/accessibility-statement/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/neomorph-llc/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/neomorphinc
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/neomorph_stock/
- group: auth
  title: ''
  type: Authentication
  url: authentication/neomorph-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/neomorph-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/neomorph-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/neomorph-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/neomorph-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/neomorph-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/neomorph-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/neomorph-plans-pricing.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/neomorph-content-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/neomorph-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/neomorph-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-26'
description: Neomorph, Inc. is a venture-backed, clinical-stage biotechnology company headquartered at 5590 Morehouse Drive in San Diego, California, founded in 2020 to design molecular glue degraders — small molecules that bind an E3 ubiquitin ligase, reshape it into a new "neomorphic" surface, and recruit disease-causing proteins to the proteasome for destruction. The approach targets the roughly 85% of the human proteome considered undruggable by conventional small molecules because it needs no traditional binding pocket. Neomorph's platform reaches beyond cereblon to hundreds of E3 ligases and multiple proprietary degrons, which the company describes as the largest proprietary molecular glue target space in the field. Its lead programme, NEO-811, targets ARNT/HIF-1β in clear cell renal cell carcinoma and entered a Phase 1/2 trial in February 2026; the rest of the pipeline spans undisclosed solid tumors plus partnered oncology/immunology, neurology and cardiometabolic/rare disease targets.
  The company closed a $109 million Series A in December 2020 and a $100 million Series B in April 2026, and runs multi-target discovery collaborations with Novo Nordisk (February 2024), Biogen (October 2024) and AbbVie (January 2025). Philip Chamberlain, DPhil is CEO and Robert J. Hugin was appointed Chairman of the Board in May 2026. Neomorph runs no developer program and publishes no product API, developer portal, API reference, SDK or pricing. The only machine-readable surface reachable without credentials is the WordPress REST content API behind neomorph.com, catalogued here.
image: https://neomorph.com/wp-content/uploads/2026/03/OG-Neomorph.png
layout: provider
modified: '2026-08-26'
name: Neomorph
nav: Providers
network: true
overview: 'Neomorph publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Pages API, Publications API, Team API, and 9 more. Tagged areas include Company, Biotechnology, Pharmaceuticals, Drug Discovery, and Targeted Protein Degradation.


  Neomorph''s developer surface includes product news, authentication, and 27 more developer resources.'
plans:
- name: Neomorph Plans Pricing
  plan_count: 0
  slug: neomorph-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Neomorph Rate Limits
  slug: neomorph-rate-limits
score:
  band: thin
  composite: 34.3
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
    contract_governance: 18.2
    contract_quality: 52.4
    developer_ergonomics: 13.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 34.3
  provenance:
    conformance: first-party
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
    score: 48.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/neomorph/refs/heads/main/screenshots/neomorph-2026-09-02T150731.png
security:
- kind: authentication
  name: Neomorph Authentication
  slug: neomorph-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Neomorph Domain Security
  slug: neomorph-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: neomorph
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Drug Discovery
- Targeted Protein Degradation
- molecular-glue
- Oncology
- Immunology
- Rare Disease
- Clinical Trials
- Life Sciences
- content-api
website: https://neomorph.com/
---
