---
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
    error_semantics: verified
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
  score: 24.6
  scored_at: '2026-08-30'
api_count: 10
apis:
- description: Route, content-type, taxonomy and status discovery documents for the iECURE WordPress REST deployment. Ten namespaces and 351 routes are registered; only these discovery documents and the content coll
  name: iECURE Discovery API
  slug: iecure-discovery-api
- description: The iECURE news archive - press releases, media coverage, awards and scientific publications/presentations. 60 published posts at harvest time across six categories.
  name: iECURE Posts API
  slug: iecure-posts-api
- description: Corporate pages - About, Approach, Programs, Careers, Contact, News, Terms of Service, Privacy Notice, Cookie Notice, Expanded Access Policy, Social Media Community Guidelines and Pharmacy Training. 1
  name: iECURE Pages API
  slug: iecure-pages-api
- description: The media library backing the site - 226 attachments at harvest time, including the corporate logo, pipeline artwork and leadership headshots.
  name: iECURE Media API
  slug: iecure-media-api
- description: Categories and tags. Six news categories are registered (news, press release, in the news, awards, pubs & pres, Uncategorized); the post_tag taxonomy is registered but empty.
  name: iECURE Taxonomy API
  slug: iecure-taxonomy-api
- description: 'The `portfolio` custom post type as deployed by iECURE, which carries team members rather than portfolio work - 35 items at harvest time, classified by the portfolio_entries taxonomy into Leadership, '
  name: iECURE Team API
  slug: iecure-team-api
- description: Cross-content search across every published object on iecure.com. 64 objects were addressable at harvest time.
  name: iECURE Search API
  slug: iecure-search-api
- description: Author directory. Anonymously readable on this deployment - unusually, since most WordPress sites gate it - returning the two accounts that have published content.
  name: iECURE Authors API
  slug: iecure-users-api
- description: Comment collection. Registered and anonymously reachable, but empty - no post on this deployment carries comments.
  name: iECURE Comments API
  slug: iecure-comments-api
- description: oEmbed 1.0 provider endpoint for iecure.com URLs, returning JSON or XML rich/link responses.
  name: iECURE oEmbed API
  slug: iecure-oembed-api
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://iecure.com/
- group: company
  title: ''
  type: About
  url: https://iecure.com/about/
- group: other
  title: ''
  type: Approach
  url: https://iecure.com/approach/
- group: other
  title: ''
  type: Pipeline
  url: https://iecure.com/programs/
- group: company
  title: ''
  type: News
  url: https://iecure.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://iecure.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://iecure.com/careers/
- group: operate
  title: ''
  type: Support
  url: https://iecure.com/contact/
- group: other
  title: ''
  type: ExpandedAccessPolicy
  url: https://iecure.com/expanded-access-policy/
- group: other
  title: ''
  type: PatientResources
  url: https://otc-hope.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://iecure.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://iecure.com/privacy-notice/
- group: other
  title: ''
  type: CookieNotice
  url: https://iecure.com/cookie-notice/
- group: docs
  title: ''
  type: SocialMediaGuidelines
  url: https://iecure.com/social-media-community-guidelines/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/iecure
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.nasdaqprivatemarket.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/iecure-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/iecure-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/iecure-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/iecure-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/iecure-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/iecure-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iecure-domain-security.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/iecure-content-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/iecure-llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/iecure-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/iecure-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-22'
description: iECURE is a clinical-stage genetic medicines company developing variant-agnostic, in vivo targeted gene insertion therapies for rare, life-threatening inherited metabolic diseases, with an initial focus on urea cycle disorders and other neurometabolic conditions of the liver. The company takes its name from iecur, the Latin word for liver, and was founded on the translational gene therapy research of James M. Wilson, M.D., Ph.D., advancing its pipeline in partnership with the University of Pennsylvania Gene Therapy Program. Its lead candidate, ECUR-506, pairs a dual-AAV delivery approach with Precision BioSciences' ARCUS nuclease to insert a functional copy of the OTC gene into the genome of infants with neonatal-onset ornithine transcarbamylase deficiency; it is in the OTC-HOPE study and has received FDA Orphan Drug, Rare Pediatric Disease, Fast Track and RMAT designations plus EU orphan designation, with clinical trial clearances in the United States, United Kingdom, Australia
  and the EU. Discovery-stage programs target citrullinemia type 1 and phenylketonuria. iECURE has raised roughly $115 million across a $50 million Series A in 2021 and a $65 million Series A-1 in 2022 from Versant Ventures, OrbiMed, Novo Holdings, the Qatar Investment Authority, LYFE Capital and Double Point Ventures. iECURE runs no developer program and publishes no product API, developer portal or API documentation. The only machine-readable surface reachable without credentials is the WordPress REST content API behind iecure.com, catalogued here.
image: https://iecure.com/wp-content/uploads/iECURE_White_Logo.png
layout: provider
modified: '2026-08-22'
name: iECURE
nav: Providers
network: true
overview: 'iECURE publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, Posts API, Pages API, and 7 more. Tagged areas include Company, biotechnology, genetic-medicine, gene-editing, and gene-therapy.


  iECURE''s developer surface includes product news, support, authentication, and 25 more developer resources.'
plans:
- name: Iecure Plans Pricing
  plan_count: 0
  slug: iecure-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Iecure Rate Limits
  slug: iecure-rate-limits
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 16
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 52.4
    developer_ergonomics: 18.5
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Iecure Authentication
  slug: iecure-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Iecure Domain Security
  slug: iecure-domain-security
  summary_line: TLSv1.3 · DMARC
slug: iecure
tags:
- Company
- biotechnology
- genetic-medicine
- gene-editing
- gene-therapy
- rare-disease
- clinical-trials
- life-sciences
- pharmaceuticals
- content-api
website: https://iecure.com/
---
