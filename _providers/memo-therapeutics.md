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
  scored_at: '2026-09-01'
api_count: 9
apis:
- description: News archive — press releases, Q&A interviews, event listings and scientific presentations (36 published on 2026-08-25).
  name: Memo Therapeutics Posts API
  slug: memo-therapeutics-posts-api
- description: Corporate pages — About us, BKV, Contact us, Latest News, Further Information, Expanded Access Policy, and the privacy, cookie and terms documents (10 published on 2026-08-25).
  name: Memo Therapeutics Pages API
  slug: memo-therapeutics-pages-api
- description: Media library — corporate imagery, partner and investor logos and leadership portraits (163 attachments on 2026-08-25).
  name: Memo Therapeutics Media API
  slug: memo-therapeutics-media-api
- description: Categories and tags. Eight categories are registered and populated; the post_tag taxonomy is registered but empty.
  name: Memo Therapeutics Taxonomy API
  slug: memo-therapeutics-taxonomy-api
- description: Comment collection. Registered and anonymously reachable, but empty — no post on this deployment carries comments.
  name: Memo Therapeutics Comments API
  slug: memo-therapeutics-comments-api
- description: Cross-content search across published objects (154 searchable objects on 2026-08-25).
  name: Memo Therapeutics Search API
  slug: memo-therapeutics-search-api
- description: Route, namespace, type, taxonomy and status discovery documents — the machine-readable index this profile was derived from.
  name: Memo Therapeutics Discovery API
  slug: memo-therapeutics-discovery-api
- description: oEmbed 1.0 provider endpoint for memo-therapeutics.com URLs.
  name: Memo Therapeutics oEmbed API
  slug: memo-therapeutics-oembed-api
- description: Block-theme navigation menus exposed as a post type (1 published on 2026-08-25).
  name: Memo Therapeutics Navigation API
  slug: memo-therapeutics-navigation-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/memo-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://memo-therapeutics.com/
- group: company
  title: ''
  type: About
  url: https://memo-therapeutics.com/about-us/
- group: company
  title: ''
  type: News
  url: https://memo-therapeutics.com/latest-news/
- group: company
  title: ''
  type: BlogRSS
  url: https://memo-therapeutics.com/feed/
- group: operate
  title: ''
  type: Contact
  url: https://memo-therapeutics.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://memo-therapeutics.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://memo-therapeutics.com/terms-and-conditions/
- group: other
  title: ''
  type: CookiePolicy
  url: https://memo-therapeutics.com/cookie-policy/
- group: other
  title: ''
  type: PatientResources
  url: https://memo-therapeutics.com/expanded-access-policy/
- group: other
  title: ''
  type: Disclaimer
  url: https://memo-therapeutics.com/further-information/
- group: other
  title: ''
  type: Science
  url: https://memo-therapeutics.com/bkv/
- group: company
  title: ''
  type: Careers
  url: https://www.ipsen.com/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/memo-therapeutics-ag/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.ipsen.com/
- group: other
  title: ''
  type: Sitemap
  url: https://memo-therapeutics.com/sitemap.xml
- group: auth
  title: ''
  type: Authentication
  url: authentication/memo-therapeutics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/memo-therapeutics-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/memo-therapeutics-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/memo-therapeutics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/memo-therapeutics-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/memo-therapeutics-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/memo-therapeutics-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/memo-therapeutics-plans-pricing.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/memo-therapeutics-content-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/memo-therapeutics-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-25'
description: Memo Therapeutics AG ("MTx"), an Ipsen company, is a late-stage biotechnology company headquartered at Wagistrasse 27 in Schlieren / Zurich, Switzerland, with a US office as Memo Therapeutics US, Inc. in Wilson, North Carolina. It develops best-in-class therapeutic antibodies to transform the lives of patients with viral infections and cancer, built on DROPZYLLA, a microfluidic single-cell platform that makes a recombinant in vitro copy of an individual donor's B-cell antibody repertoire, banks it as a library, and screens it functionally at high throughput. Its lead program, potravitug, is a first-in-class monoclonal antibody against BK polyomavirus (BKPyV) reactivation in kidney transplant recipients; the Phase II SAFE KIDNEY II trial reported biopsy-proven resolution of BKPyV-associated nephropathy with sustained viral-load reduction to week 38, and the asset holds EU orphan designation. In February 2026 the company entered a collaboration and option agreement with CSL for
  its recombinant polyclonal IgG technology carrying milestones of up to CHF 265 million, and it has run an oncology antibody-discovery collaboration with Ono Pharmaceutical since 2022 alongside nephrology collaborations with the University Hospital of Zurich and the University Hospital of Bern. Ipsen completed its acquisition of Memo Therapeutics AG on 22 July 2026, adding potravitug to Ipsen's rare-disease pipeline. Memo Therapeutics runs no developer program and publishes no product API, developer portal, SDK or API documentation. The only machine-readable surface reachable without credentials is the WordPress REST content API behind memo-therapeutics.com, catalogued here, together with an llms.txt the site's SEO plugin publishes.
image: https://memo-therapeutics.com/wp-content/uploads/2024/07/memo-therapeutics-ipsen-logo.webp
layout: provider
modified: '2026-08-25'
name: Memo Therapeutics
nav: Providers
network: true
overview: 'Memo Therapeutics publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Posts API, Pages API, Media API, and 6 more. Tagged areas include Company, Biotechnology, Pharmaceuticals, Antibody Therapeutics, and Rare Disease.


  Memo Therapeutics'' developer surface includes product news, authentication, and 25 more developer resources.'
plans:
- name: Memo Therapeutics Plans Pricing
  plan_count: 0
  slug: memo-therapeutics-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Memo Therapeutics Rate Limits
  slug: memo-therapeutics-rate-limits
score:
  band: thin
  composite: 32.3
  coverage:
    artifact_dirs: 16
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 52.4
    developer_ergonomics: 13.7
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 32.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Memo Therapeutics Authentication
  slug: memo-therapeutics-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Memo Therapeutics Domain Security
  slug: memo-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: memo-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Antibody Therapeutics
- Rare Disease
- Nephrology
- transplantation
- virology
- Oncology
- Clinical Trials
- Life Sciences
- Switzerland
- content-api
website: https://memo-therapeutics.com/
---
