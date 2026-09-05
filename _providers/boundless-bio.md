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
    agentic_access: derived
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 48
  human_in_the_loop: 0
  name: Boundless Bio Agentic Access
  operation_count: 73
  slug: boundless-bio-agentic-access
  summary_line: 73 operations · 48 acting
api_count: 10
apis:
- baseURL: https://boundlessbio.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Comments API from Boundless Bio — 2 operation(s) for comments.
  name: Boundless Bio Comments API
  slug: boundless-bio-comments-api
- baseURL: https://boundlessbio.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Discovery API from Boundless Bio — 4 operation(s) for discovery.
  name: Boundless Bio Discovery API
  slug: boundless-bio-discovery-api
- baseURL: https://boundlessbio.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Leadership API from Boundless Bio — 2 operation(s) for leadership.
  name: Boundless Bio Leadership API
  slug: boundless-bio-leadership-api
- baseURL: https://boundlessbio.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Media API from Boundless Bio — 3 operation(s) for media.
  name: Boundless Bio Media API
  slug: boundless-bio-media-api
- baseURL: https://boundlessbio.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Pages API from Boundless Bio — 2 operation(s) for pages.
  name: Boundless Bio Pages API
  slug: boundless-bio-pages-api
- baseURL: https://boundlessbio.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Posts API from Boundless Bio — 2 operation(s) for posts.
  name: Boundless Bio Posts API
  slug: boundless-bio-posts-api
- baseURL: https://boundlessbio.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Search API from Boundless Bio — 1 operation(s) for search.
  name: Boundless Bio Search API
  slug: boundless-bio-search-api
- baseURL: https://boundlessbio.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Settings API from Boundless Bio — 1 operation(s) for settings.
  name: Boundless Bio Settings API
  slug: boundless-bio-settings-api
- baseURL: https://boundlessbio.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Taxonomy API from Boundless Bio — 6 operation(s) for taxonomy.
  name: Boundless Bio Taxonomy API
  slug: boundless-bio-taxonomy-api
- baseURL: https://boundlessbio.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Users API from Boundless Bio — 3 operation(s) for users.
  name: Boundless Bio Users API
  slug: boundless-bio-users-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Boundless Bio Content API (WordPress REST wp/v2) Comments API
  slug: open-boundless-bio-comments-api
- collection_type: open
  name: Boundless Bio Content API (WordPress REST wp/v2) Discovery API
  slug: open-boundless-bio-discovery-api
- collection_type: open
  name: Boundless Bio Content API (WordPress REST wp/v2) Leadership API
  slug: open-boundless-bio-leadership-api
- collection_type: open
  name: Boundless Bio Content API (WordPress REST wp/v2) Media API
  slug: open-boundless-bio-media-api
- collection_type: open
  name: Boundless Bio Content API (WordPress REST wp/v2) Pages API
  slug: open-boundless-bio-pages-api
- collection_type: open
  name: Boundless Bio Content API (WordPress REST wp/v2) Posts API
  slug: open-boundless-bio-posts-api
- collection_type: open
  name: Boundless Bio Content API (WordPress REST wp/v2) Search API
  slug: open-boundless-bio-search-api
- collection_type: open
  name: Boundless Bio Content API (WordPress REST wp/v2) Settings API
  slug: open-boundless-bio-settings-api
- collection_type: open
  name: Boundless Bio Content API (WordPress REST wp/v2) Taxonomy API
  slug: open-boundless-bio-taxonomy-api
- collection_type: open
  name: Boundless Bio Content API (WordPress REST wp/v2) Users API
  slug: open-boundless-bio-users-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/boundless-bio-content-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/boundless-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boundlessbio.com/
- group: company
  title: ''
  type: About
  url: https://boundlessbio.com/why-we-are-here/
- group: other
  title: ''
  type: Technology
  url: https://boundlessbio.com/what-we-do/
- group: other
  title: ''
  type: Team
  url: https://boundlessbio.com/who-we-are/
- group: other
  title: ''
  type: Publications
  url: https://boundlessbio.com/publications/
- group: company
  title: ''
  type: Careers
  url: https://boundlessbio.com/work-with-us/
- group: operate
  title: ''
  type: Support
  url: https://boundlessbio.com/contact/
- group: company
  title: ''
  type: Investors
  url: https://investors.boundlessbio.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://boundlessbio.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://boundlessbio.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/boundlessbio
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/BoundlessBio
- group: build
  title: ''
  type: Packages
  url: packages/boundless-bio-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/boundless-bio-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/boundless-bio-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/boundless-bio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/boundless-bio-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/boundless-bio-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/boundless-bio-lifecycle.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/boundless-bio-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/boundless-bio_stock/
created: '2026-08-08'
description: 'Boundless Bio (Nasdaq: BOLD) is a San Diego, California based clinical-stage, next-generation precision oncology company founded in 2018 to target extrachromosomal DNA (ecDNA) — circular, centromere-free DNA that carries high copy-number oncogene amplifications and is observed in roughly 17% of cancer patients, driving tumor heterogeneity and resistance to targeted therapy. Its proprietary Spyglass discovery platform, built on a suite of ecDNA+/- tumor models plus molecular analytics and imaging, identifies targets essential to ecDNA function, which the company drugs with small-molecule ecDNA-directed therapies (ecDTx). The clinical pipeline is led by BBI-940, a kinesin inhibitor targeting ecDNA segregation, in the Phase 1 KOMODO-1 trial in ER+/HER2- and TNBC-LAR breast cancer opened in February 2026, with earlier CHK1 (replication stress) and RNR (DNA assembly and repair) programs behind it; ECHO, its ecDNA diagnostic algorithm, reads ecDNA off routine clinical next-generation
  sequencing and is described by the company as the first ecDNA diagnostic used in clinical trials. Boundless Bio raised a $100M Series C co-led by Leaps by Bayer and RA Capital and listed on Nasdaq in 2024. It publishes no developer program, no product API, no SDKs and no API documentation of any kind; the only machine-readable surface on boundlessbio.com is the WordPress REST API (wp/v2), anonymously readable, which serves the corporate pages, the Leadership directory and the media library as JSON.'
image: https://boundlessbio.com/wp-content/uploads/2019/09/logo-boundless-bio.png
layout: provider
modified: '2026-08-08'
name: Boundless Bio
nav: Providers
network: true
overview: 'Boundless Bio publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Discovery API, Leadership API, and 7 more. Tagged areas include Company, Biotechnology, Oncology, Precision Medicine, and Drug Discovery.


  Boundless Bio''s developer surface includes support, authentication, and 22 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 22.6
  coverage:
    artifact_dirs: 17
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
    contract_quality: 19.5
    developer_ergonomics: 18.5
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 22.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
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
screenshot: https://raw.githubusercontent.com/api-evangelist/boundless-bio/refs/heads/main/screenshots/boundless-bio-2026-09-02T144938.png
security:
- kind: authentication
  name: Boundless Bio Authentication
  slug: boundless-bio-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Boundless Bio Domain Security
  slug: boundless-bio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: boundless-bio
tags:
- Company
- Biotechnology
- Oncology
- Precision Medicine
- Drug Discovery
- Life Sciences
- Pharmaceuticals
- Clinical Trials
- Genomics
- Diagnostics
- Research
- Content
website: https://boundlessbio.com/
---
