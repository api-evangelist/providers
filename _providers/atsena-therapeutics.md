---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 33.6
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: The anonymously readable WordPress REST API behind atsenatx.com. It exposes Atsena Therapeutics press releases and company news (posts), the program pages for ATSN-201/XLRS, ATSN-101/LCA1, ATSN-301/US
  name: Atsena Therapeutics Content API
  slug: atsena-therapeutics-content-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://atsenatx.com/
- group: company
  title: ''
  type: About
  url: https://atsenatx.com/about/overview/
- group: company
  title: ''
  type: Blog
  url: https://atsenatx.com/news/
- group: company
  title: ''
  type: News
  url: https://atsenatx.com/news/
- group: operate
  title: ''
  type: PressReleases
  url: https://atsenatx.com/news/press-releases/
- group: company
  title: ''
  type: BlogRSS
  url: https://atsenatx.com/feed/
- group: other
  title: ''
  type: Publications
  url: https://atsenatx.com/news/presentations-and-publications/
- group: other
  title: ''
  type: Pipeline
  url: https://atsenatx.com/programs/pipeline/
- group: other
  title: ''
  type: Technology
  url: https://atsenatx.com/our-approach/
- group: start
  title: ''
  type: ClinicalTrials
  url: https://atsenatx.com/clinical-trials/
- group: other
  title: ''
  type: Patients
  url: https://atsenatx.com/for-patients/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atsenatx.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://atsenatx.com/contact/
- group: operate
  title: ''
  type: Contact
  url: https://atsenatx.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://atsenatx.com/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/atsenatx
- group: company
  title: ''
  type: Investors
  url: https://atsenatx.com/about/investors/
- group: company
  title: ''
  type: Partners
  url: https://atsenatx.com/about/partners/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/atsena-therapeutics_stock/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/atsena-therapeutics-wp-rest-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/atsena-therapeutics-wp-rest-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/atsena-therapeutics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/atsena-therapeutics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/atsena-therapeutics-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/atsena-therapeutics-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/atsena-therapeutics-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/atsena-therapeutics-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/atsena-therapeutics-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/atsena-therapeutics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/atsena-therapeutics-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-02'
description: 'Atsena Therapeutics is a clinical-stage gene therapy company based in Durham, North Carolina, in the Research Triangle, developing first- and best-in-class genetic medicines for inherited retinal diseases with the goal of reversing or preventing blindness. Founded by ocular gene therapy pioneers Shannon Boye and Sanford Boye, the company builds on two proprietary AAV delivery platforms: a laterally spreading AAV.SPR capsid engineered to reach retinal cells without the surgical trauma of a subretinal bleb, and a dual-vector technology that splits genes too large for a single AAV across two vectors. Its clinical pipeline includes ATSN-201 for X-linked retinoschisis (XLRS) in a pivotal Phase 3 trial, ATSN-101 for LCA1 (Leber congenital amaurosis 1) advancing to a pivotal trial with partner Nippon Shinyaku, and IND-enabling programs ATSN-301 for Usher syndrome 1B and ATSN-401 for Stargardt disease. Atsena runs no developer program and publishes no product API, no developer documentation
  and no specification of its own. The only machine-readable surface it exposes is the anonymously readable WordPress REST content API behind atsenatx.com, which serves the company''s press releases, program and platform pages, and media library as JSON; the OpenAPI in this repo is derived by API Evangelist from that surface''s own live route index.'
image: https://atsenatx.com/wp-content/themes/atsenatx/img/touch-icon-ipad-retina.png
layout: provider
modified: '2026-08-02'
name: Atsena Therapeutics
nav: Providers
network: true
overview: 'Atsena Therapeutics publishes 1 API on the [APIs.io](https://apis.io/) network: Content API. Tagged areas include Company, Biotechnology, Gene Therapy, Life Sciences, and Pharmaceuticals.


  Atsena Therapeutics'' developer surface includes engineering blog, product news, support, authentication, and 27 more developer resources.'
random_paper: 57
score:
  band: thin
  composite: 30.4
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 60.5
    developer_ergonomics: 19.0
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 30.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Atsena Therapeutics Authentication
  slug: atsena-therapeutics-authentication
  summary_line: none/http/apiKey · 3 schemes
- kind: domain-security
  name: Atsena Therapeutics Domain Security
  slug: atsena-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atsena-therapeutics
tags:
- Company
- Biotechnology
- Gene Therapy
- Life Sciences
- Pharmaceuticals
- Clinical Trials
- Ophthalmology
- Rare Disease
- Healthcare
- Research and Development
- Content API
- WordPress
website: https://atsenatx.com/
---
