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
  scored_at: '2026-08-30'
api_count: 9
apis:
- description: Route, type, taxonomy and status discovery documents.
  name: MBrace Therapeutics Discovery API
  slug: mbrace-therapeutics-discovery-api
- description: Media library (224 attachments at harvest time).
  name: MBrace Therapeutics Media API
  slug: mbrace-therapeutics-media-api
- description: Company news archive — press releases, scientific presentations and publications (8 published at harvest time, spanning November 2023 through July 2025).
  name: MBrace Therapeutics News API
  slug: mbrace-therapeutics-news-api
- description: oEmbed 1.0 provider endpoint for mbracetrx.com URLs.
  name: MBrace Therapeutics Oembed API
  slug: mbrace-therapeutics-oembed-api
- description: Corporate site pages (12 published at harvest time).
  name: MBrace Therapeutics Pages API
  slug: mbrace-therapeutics-pages-api
- description: 'The five company-specific custom post types MBrace Therapeutics registered for its own governance and backer disclosures: board members, executive committee, founders, investors and the scientific adv'
  name: MBrace Therapeutics People API
  slug: mbrace-therapeutics-people-api
- description: Cross-content search across every published object on the deployment (76 searchable objects at harvest time).
  name: MBrace Therapeutics Search API
  slug: mbrace-therapeutics-search-api
- description: Category and tag terms. Four categories are registered; the post_tag taxonomy is registered but empty.
  name: MBrace Therapeutics Taxonomy API
  slug: mbrace-therapeutics-taxonomy-api
- description: Post authors exposed by the users collection (3 at harvest time).
  name: MBrace Therapeutics Users API
  slug: mbrace-therapeutics-users-api
artifact_total: 13
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/mbrace-therapeutics-news-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mbrace-therapeutics-people-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://mbracetrx.com/
- group: company
  title: ''
  type: About
  url: https://mbracetrx.com/about-us/
- group: other
  title: ''
  type: Pipeline
  url: https://mbracetrx.com/pipeline/
- group: other
  title: ''
  type: DiscoveryPlatform
  url: https://mbracetrx.com/discovery-platform/
- group: build
  title: ''
  type: ClinicalProgram
  url: https://mbracetrx.com/clinical-program-mbrc-101/
- group: build
  title: ''
  type: ClinicalProgram
  url: https://mbracetrx.com/clinical-program-mbrc-201/
- group: other
  title: ''
  type: ExpandedAccess
  url: https://mbracetrx.com/expanded-access-statement/
- group: company
  title: ''
  type: News
  url: https://mbracetrx.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://mbracetrx.com/feed/
- group: operate
  title: ''
  type: Contact
  url: https://mbracetrx.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mbracetrx.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mbracetrx.com/terms-of-use/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mbrace-therapeutics
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/mbrace-therapeutics_stock/
- group: auth
  title: ''
  type: Authentication
  url: authentication/mbrace-therapeutics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mbrace-therapeutics-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mbrace-therapeutics-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mbrace-therapeutics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mbrace-therapeutics-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mbrace-therapeutics-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mbrace-therapeutics-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/mbrace-therapeutics-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mbrace-therapeutics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mbrace-therapeutics-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mbrace-therapeutics-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-25'
description: MBrace Therapeutics is a privately held, clinical-stage biopharmaceutical company developing antibody-drug conjugates (ADCs) against novel oncology targets. Co-founded by Renata Pasqualini, Ph.D. and Isan Chen, MD, the company builds its pipeline on SPARTA, an in vivo antibody selection and target discovery process it uses to find ADC targets that conventional in vitro discovery misses. Its lead candidate MBRC-101 is an anti-EphA5 monomethyl auristatin E (MMAE) antibody-drug conjugate in a multi-centre, open-label Phase 1/1b dose-finding, safety and pharmacokinetic study in advanced refractory solid tumours; MBRC-201 is in Phase 2, MBRC-301 is in IND-enabling studies against solid tumours, and MBRC-401 is in discovery. MBrace emerged from stealth in November 2023 with an $85 million Series B led by TPG through TPG Life Sciences Innovations, alongside Avidity Partners, Blue Owl Capital, Venrock and Alta Partners, bringing total capital raised to $110 million. MBRC-101 was named
  Most Promising Clinical Candidate at the 11th Annual World ADC Awards. MBrace Therapeutics runs no developer program and publishes no product API, developer portal, API reference or SDK. The only machine-readable surface reachable without credentials is the WordPress REST content API behind mbracetrx.com, catalogued here — notable because the company registered five of its own custom post types, so its board, executive committee, founders, named investors and scientific advisory board are all published as structured JSON rather than only as rendered HTML.
image: https://mbracetrx.com/wp-content/uploads/2021/12/logo-mbrace.svg
layout: provider
modified: '2026-08-25'
name: MBrace Therapeutics
nav: Providers
network: true
overview: 'MBrace Therapeutics publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, Media API, News API, and 6 more. Tagged areas include Company, biotechnology, pharmaceuticals, oncology, and antibody-drug-conjugates.


  MBrace Therapeutics'' developer surface includes product news, authentication, and 26 more developer resources.'
plans:
- name: Mbrace Therapeutics Plans Pricing
  plan_count: 0
  slug: mbrace-therapeutics-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Mbrace Therapeutics Rate Limits
  slug: mbrace-therapeutics-rate-limits
score:
  band: thin
  composite: 30.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 52.6
    developer_ergonomics: 13.7
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 30.0
  provenance:
    conformance: derived
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
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Mbrace Therapeutics Authentication
  slug: mbrace-therapeutics-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Mbrace Therapeutics Domain Security
  slug: mbrace-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mbrace-therapeutics
tags:
- Company
- biotechnology
- pharmaceuticals
- oncology
- antibody-drug-conjugates
- drug-discovery
- clinical-trials
- life-sciences
- precision-medicine
- content-api
website: https://mbracetrx.com/
---
