---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ch2m-hill-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/ch2m-hill-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ch2m-hill-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ch2m-hill-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ch2m-hill-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ch2m-hill-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CH2M
- group: company
  title: ''
  type: Website
  url: https://www.jacobs.com/
- group: other
  title: ''
  type: Acquisition
  url: https://www.jacobs.com/newsroom/press-release/jacobs-completes-ch2m-acquisition-creating-15-billion-professional-services
- group: other
  title: ''
  type: ParentCompany
  url: https://www.jacobs.com/
- group: company
  title: ''
  type: About
  url: https://www.jacobs.com/about
- group: company
  title: ''
  type: News
  url: https://www.jacobs.com/newsroom
- group: company
  title: ''
  type: Careers
  url: https://careers.jacobs.com/
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/CH2M_Hill
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jacobs/
- group: other
  title: ''
  type: X
  url: https://x.com/JacobsConnects
- group: other
  title: ''
  type: Services
  url: ''
- group: other
  title: ''
  type: Markets
  url: ''
coverage:
  checked: '2026-09-05'
  detail: CH2M Hill's own web presence is fully decommissioned — ch2mhill.com and ch2m.com resolve to a shared parking host that answers HTTP 404 "Web Site Not Found" for every path including the root, www.ch2mhill.com does not resolve at all because its CNAME target is an IP literal, and the brand was absorbed into Jacobs in December 2017 with no developer program in either era.
  evidence:
  - status: 404
    url: http://ch2mhill.com/
  - status: 404
    url: http://ch2m.com/
  - status: 0
    url: https://www.ch2mhill.com/
  - status: 404
    url: https://www.jacobs.com/.well-known/api-catalog
  reason: defunct
  state: none
created: '2025-01-01'
description: CH2M Hill was a global engineering, consulting, design, construction and operations firm providing services for corporations and federal, state, and local governments. Headquartered in Englewood, Colorado, the firm delivered work in water, transportation, environment, energy, industrial, and facilities markets. In December 2017 CH2M was acquired by Jacobs Engineering (now Jacobs Solutions) and its operations have been integrated into Jacobs. As of the acquisition, CH2M Hill no longer publishes a standalone public API program; relevant digital engineering, project delivery, and data services are now offered under the Jacobs brand.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ch2m-hill.png
layout: provider
modified: '2026-09-05'
name: CH2M Hill
nav: Providers
network: true
overview: 'CH2M Hill is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Acquired, Construction, Consulting, Engineering, and Government.


  CH2M Hill''s developer surface includes product news and 15 more developer resources.'
plans:
- name: Ch2M Hill Plans Pricing
  plan_count: 0
  slug: ch2m-hill-plans-pricing
press:
- date: '2026-05-25'
  title: Jacobs Engineering to buy CH2M Hill in $3.27 bln deal
  url: https://www.reuters.com/article/business/jacobs-engineering-to-buy-ch2m-hill-in-327-bln-deal-idUSL4N1KO3KZ/
- date: '2026-05-25'
  title: OSU celebrates groundbreaking of the Huang Complex
  url: https://www.fororegonstate.org/stay-informed/impact-stories/detail/Huang_Complex_groundbreaking
- date: '2026-05-25'
  title: Jacobs posts strong Q3, touts last year's acquisition of ...
  url: https://www.constructiondive.com/news/jacobs-posts-strong-q3-touts-last-years-acquisition-of-ch2m-hill/529460/
- date: '2026-05-25'
  title: CH2M Hill Provides Design of Pilot Bioenergy Facility in UAE
  url: https://www.executivebiz.com/articles/ch2m-hill-provides-design-of-pilot-bioenergy-facility-in-uae-neil-reynolds-comments
- date: '2026-05-25'
  title: Microsoft Virtualization Beats VMware at CH2M Hill - Datamation
  url: https://www.datamation.com/applications/microsoft-virtualization-beats-vmware-at-ch2m-hill/
random_paper: 13
rate_limits:
- limit_count: 0
  name: Ch2M Hill Rate Limits
  slug: ch2m-hill-rate-limits
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 3.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ch2m-hill/refs/heads/main/screenshots/ch2m-hill-2026-06-20T174155.png
security:
- kind: domain-security
  name: Ch2M Hill Domain Security
  slug: ch2m-hill-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ch2m-hill
tags:
- Acquired
- Construction
- Consulting
- Engineering
- Government
- Infrastructure
website: https://www.jacobs.com/
---
