---
access_model:
  confidence: high
  label: Free · no signup
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.1
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://t2r2.star.titech.ac.jp/oaipmh/OAIHandler
  baseurl_source: declared
  description: OAI-PMH 2.0 metadata harvesting interface for T2R2, the Science Tokyo / Tokyo Tech Research Repository, operated by the university library on the institution's own host. Repository name "T2R2 -Tokyo T
  name: T2R2 Research Repository OAI-PMH
  slug: t2r2-oaipmh
- description: Shibboleth / SAML 2.0 Identity Provider for institutional single sign-on, registered in GakuNin, Japan's national academic access management federation operated by NII. Advertises the Shibboleth 1.0 A
  name: GakuNin Shibboleth Identity Provider (SAML 2.0)
  slug: gakunin-shibboleth
- description: OAI-PMH 2.0 endpoint for the institution's tenancy on JAIRO Cloud — the successor repository named in the T2R2 discontinuation notice as the destination for full-text research outputs. Identify return
  name: Science Tokyo Repository OAI-PMH (JAIRO Cloud tenant)
  slug: science-tokyo-repository-oaipmh
- description: A second GakuNin-registered SAML 2.0 entity carrying the Institute of Science Tokyo identity, hosted on the commercial EX-TIC platform and pointing at the pre-merger medical/dental side of the institu
  name: EX-TIC GakuNin SAML entity (tenant)
  slug: ex-tic-gakunin-entity
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.isct.ac.jp/en
- group: company
  title: ''
  type: Website
  url: https://www.titech.ac.jp/
- group: start
  title: ''
  type: Portal
  url: https://portal.titech.ac.jp/
- group: docs
  title: ''
  type: Documentation
  url: https://t2r2.star.titech.ac.jp/index_en.html
- group: operate
  title: ''
  type: Support
  url: https://www.isct.ac.jp/en/inquiries
- group: company
  title: ''
  type: Blog
  url: https://www.isct.ac.jp/en/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.isct.ac.jp/en/001/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.isct.ac.jp/en/001/web-accessibility-policy
- group: other
  title: ''
  type: AIPolicy
  url: https://www.isct.ac.jp/en/001/about/policies
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/science-tokyo
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/prg-titech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/sciencetokyo/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/sciencetokyo_en
- group: other
  title: ''
  type: IdentityFederation
  url: https://metadata.gakunin.nii.ac.jp/gakunin-metadata.xml
- group: other
  title: ''
  type: ResearchRepository
  url: https://isct.repo.nii.ac.jp/
- group: other
  title: ''
  type: ResearchDirectory
  url: https://strdb.s.isct.ac.jp/html/home_en.html
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.libra.titech.ac.jp/en
- group: learn
  title: ''
  type: CourseCatalog
  url: https://syllabus.s.isct.ac.jp/
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.t4.cii.isct.ac.jp/en
- group: docs
  title: ''
  type: Documentation
  url: https://www.t4.cii.isct.ac.jp/docs/
- group: auth
  title: ''
  type: Authentication
  url: authentication/tokyo-institute-of-technology-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tokyo-institute-of-technology-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tokyo-institute-of-technology-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tokyo-institute-of-technology-errors.yml
- group: build
  title: ''
  type: Examples
  url: examples/tokyo-institute-of-technology-t2r2-oaipmh-examples.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/tokyo-institute-of-technology-t2r2-oaipmh-openapi.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tokyo-institute-of-technology-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tokyo-institute-of-technology-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tokyo-institute-of-technology-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tokyo-institute-of-technology-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tokyo-institute-of-technology-context.jsonld
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Tokyo Institute of Technology (Tokyo Tech / Titech) was Japan''s leading national institute of technology and ranked #76 in the QS World University Rankings 2025. On 2024-10-01 it merged with Tokyo Medical and Dental University to form the Institute of Science Tokyo (Science Tokyo); the corporate web presence moved to isct.ac.jp while most academic and service systems still run on titech.ac.jp. Its institution-operated programmable footprint is small and, as of 2026-08-30, shrinking. There is no developer portal, no public REST API, no open-data portal and no OAuth or OpenID Connect surface anywhere on its domains. What the institution genuinely operates and we verified live is two protocol endpoints: the T2R2 research repository''s OAI-PMH 2.0 harvesting interface (oai_dc and junii2), and a Shibboleth/SAML 2.0 Identity Provider registered in GakuNin, Japan''s national academic access management federation. The first is being switched off — the operator published a discontinuation
  schedule on 2026-07-22 that ended T2R2 search on 2026-08-20 and ends T2R2 registration on 2026-10-01, moving full text to the Science Tokyo Repository on JAIRO Cloud, which is a TENANT surface run by NII and JPCOAR rather than by the university. The library discovery layer, the syllabus system, the STRDB researcher database and the TSUBAME4 supercomputer service are all real institution-run systems with human interfaces only — none of them publishes a machine-readable contract.'
finops:
- name: Tokyo Institute Of Technology Finops
  service_category: Education
  slug: tokyo-institute-of-technology-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tokyo-institute-of-technology.png
jsonld:
- class_count: 22
  name: Tokyo Institute Of Technology Context
  property_count: 1
  slug: tokyo-institute-of-technology-context
layout: provider
modified: '2026-08-30'
name: Tokyo Institute of Technology
nav: Providers
network: true
overview: 'Tokyo Institute of Technology publishes 1 API on the [APIs.io](https://apis.io/) network: T2R2 Research Repository OAI-PMH. Tagged areas include Education, Higher Education, University, Institute of Technology, and Japan.


  The Tokyo Institute of Technology catalog on APIs.io includes 1 JSON-LD context.


  Tokyo Institute of Technology''s developer surface includes developer portal, documentation, support, engineering blog, authentication, code examples, and 26 more developer resources.'
plans:
- name: Tokyo Institute Of Technology Plans Pricing
  plan_count: 2
  slug: tokyo-institute-of-technology-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Tokyo Institute Of Technology Rate Limits
  slug: tokyo-institute-of-technology-rate-limits
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 13
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 22.3
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 38.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 61.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tokyo-institute-of-technology/refs/heads/main/screenshots/tokyo-institute-of-technology-2026-06-20T195440.png
security:
- kind: authentication
  name: Tokyo Institute Of Technology Authentication
  slug: tokyo-institute-of-technology-authentication
  summary_line: saml2 · 2 schemes
- kind: domain-security
  name: Tokyo Institute Of Technology Domain Security
  slug: tokyo-institute-of-technology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tokyo-institute-of-technology
tags:
- Education
- Higher Education
- University
- Institute of Technology
- Japan
- Research
- Research Data
- Open Access
- Institutional Repository
- OAI-PMH
- Identity Federation
- Shibboleth
- SAML
- Research Computing
- Course Catalog
- Library
website: https://www.isct.ac.jp/en
---
