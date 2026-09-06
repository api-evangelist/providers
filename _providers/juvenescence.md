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
api_count: 9
apis:
- baseURL: https://juvlabs.com/wp-json
  baseurl_source: declared
  description: Juvenescence's news stream — 57 published posts across Press Releases, In the News, Juv on the Road, Publications and Videos — read from the WordPress REST content API behind juvlabs.com.
  name: Juvenescence Posts API
  slug: juvenescence-posts-api
- baseURL: https://juvlabs.com/wp-json
  baseurl_source: declared
  description: The 35 published corporate, science, pipeline, leadership-biography and policy pages of juvlabs.com, read from the WordPress REST content API.
  name: Juvenescence Pages API
  slug: juvenescence-pages-api
- baseURL: https://juvlabs.com/wp-json
  baseurl_source: declared
  description: The 466-item juvlabs.com media library — brand marks, leadership portraits, press and conference imagery — with per-item MIME type, source URL and generated size variants.
  name: Juvenescence Media API
  slug: juvenescence-media-api
- baseURL: https://juvlabs.com/wp-json
  baseurl_source: declared
  description: The 7 post categories that organise the Juvenescence news stream, five of which carry posts.
  name: Juvenescence Categories API
  slug: juvenescence-categories-api
- baseURL: https://juvlabs.com/wp-json
  baseurl_source: declared
  description: The 25 post tags on juvlabs.com, a vocabulary dominated by Juvenescence portfolio companies and research collaborators alongside a legacy consumer-nutrition set.
  name: Juvenescence Tags API
  slug: juvenescence-tags-api
- baseURL: https://juvlabs.com/wp-json
  baseurl_source: declared
  description: The comments collection on juvlabs.com. Registered and anonymously readable, but empty — the site does not use comments.
  name: Juvenescence Comments API
  slug: juvenescence-comments-api
- baseURL: https://juvlabs.com/wp-json
  baseurl_source: declared
  description: Cross-content search over Juvenescence posts, pages, the portfolio type and taxonomy terms — the single best entry point for an agent that needs to find material without walking every collection.
  name: Juvenescence Search API
  slug: juvenescence-search-api
- baseURL: https://juvlabs.com/wp-json
  baseurl_source: declared
  description: The site's registered `portfolio` custom post type and its `portfolio_category` taxonomy. Registered, public and REST-exposed, but empty at derivation — Juvenescence's portfolio companies are currentl
  name: Juvenescence Portfolio API
  slug: juvenescence-portfolio-api
- baseURL: https://juvlabs.com/wp-json
  baseurl_source: declared
  description: The juvlabs.com REST discovery surface — site index, `wp/v2` namespace route index with per-argument schemas, registered content types, taxonomies and statuses, plus oEmbed URL resolution.
  name: Juvenescence Discovery API
  slug: juvenescence-discovery-api
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://juvlabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.wordpress.org/rest-api/
- group: docs
  title: ''
  type: APIReference
  url: https://juvlabs.com/wp-json/wp/v2
- group: company
  title: ''
  type: Blog
  url: https://juvlabs.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://juvlabs.com/sitemap.rss
- group: operate
  title: ''
  type: PressReleases
  url: https://juvlabs.com/news/category/press-releases/
- group: other
  title: ''
  type: Publications
  url: https://juvlabs.com/news/category/publications/
- group: other
  title: ''
  type: Science
  url: https://juvlabs.com/science/
- group: other
  title: ''
  type: Pipeline
  url: https://juvlabs.com/our-pipeline/
- group: other
  title: ''
  type: Management
  url: https://juvlabs.com/our-team/
- group: company
  title: ''
  type: About
  url: https://juvlabs.com/our-approach/
- group: operate
  title: ''
  type: Contact
  url: https://juvlabs.com/contact-us/
- group: operate
  title: ''
  type: Support
  url: https://juvlabs.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://juvlabs.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://juvlabs.com/privacy-notice/
- group: other
  title: ''
  type: CookiePolicy
  url: https://juvlabs.com/cookie-notice/
- group: other
  title: ''
  type: RefundPolicy
  url: https://juvlabs.com/refund-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/juvenescence1
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ro5-ai
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/juvenescence_stock/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/juvenescence-content-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/juvenescence-content-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/juvenescence-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/juvenescence-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/juvenescence-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/juvenescence-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/juvenescence-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/juvenescence-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/juvenescence-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/juvenescence-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/juvenescence-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/juvenescence-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/juvenescence-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/juvenescence-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-23'
description: Juvenescence Limited is a clinical-stage, AI-enabled drug development company headquartered in Ramsey, Isle of Man, with operations in the United Kingdom, the United States and Abu Dhabi, founded by Jim Mellon, Dr Gregory Bailey and Dr Declan Doogan and led by CEO Dr Richard Marshall CBE. It develops medicines that target core mechanisms of aging in order to prevent rather than only treat age-related disease, working across small molecules, biologics and cell therapies. Its lead programme is the PAI-1 inhibitor MDI-2517, which completed a Phase 1 trial with a Phase 2 proof-of-concept study planned in metabolic and fibrotic disease, alongside a CD38 inhibitor programme run with the Buck Institute for Research on Aging. The company closed a $76m first tranche of Series B-1 financing led by Abu Dhabi's M42 in 2025 and acquired the AI drug-discovery company Ro5 Inc. in June 2025, bringing in the HydraScreen structure-based screening and ADMET modelling stack. Juvenescence has founded
  or capitalised a portfolio of longevity biotechs including LyGenesis, Napa Therapeutics, Souvien Therapeutics, Morphoceuticals, Relation Therapeutics, Chrysea Labs, Selah Therapeutics and BYOMass. Juvenescence runs no developer program and publishes no product API. The machine-readable surfaces it does expose are the anonymously readable WordPress REST content API behind juvlabs.com, a provider-published llms.txt, and the open-source HydraScreen and bio2d research code released under the Ro5-ai GitHub organisation.
image: https://juvlabs.com/wp-content/uploads/2024/07/juvenescence-logo-green.png
layout: provider
modified: '2026-08-23'
name: Juvenescence
nav: Providers
network: true
overview: 'Juvenescence publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Posts API, Pages API, Media API, and 6 more. Tagged areas include Company, Biotechnology, Pharmaceuticals, Longevity, and Drug Discovery.


  Juvenescence''s developer surface includes documentation, API reference, engineering blog, support, authentication, and 30 more developer resources.'
plans:
- name: Juvenescence Plans Pricing
  plan_count: 0
  slug: juvenescence-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Juvenescence Rate Limits
  slug: juvenescence-rate-limits
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 13.7
    developer_ergonomics: 44.6
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 30.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 100.0
      total: 10
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
screenshot: https://raw.githubusercontent.com/api-evangelist/juvenescence/refs/heads/main/screenshots/juvenescence-2026-09-02T150010.png
security:
- kind: authentication
  name: Juvenescence Authentication
  slug: juvenescence-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Juvenescence Domain Security
  slug: juvenescence-domain-security
  summary_line: TLSv1.3 · DMARC
slug: juvenescence
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Longevity
- Drug Discovery
- Life Sciences
- Clinical Trials
- Artificial Intelligence
- Aging
- content-api
website: https://juvlabs.com/
---
