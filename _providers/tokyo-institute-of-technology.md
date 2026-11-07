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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Shibboleth / SAML 2.0 Identity Provider for institutional single sign-on, registered in GakuNin, Japan's national academic access management federation operated by NII. Advertises the Shibboleth 1.0 A
  name: GakuNin Shibboleth Identity Provider (SAML 2.0)
  slug: gakunin-shibboleth
- description: OAI-PMH 2.0 endpoint for the institution's tenancy on JAIRO Cloud — the successor repository named in the T2R2 discontinuation notice as the destination for full-text research outputs. Identify return
  name: Science Tokyo Repository OAI-PMH (JAIRO Cloud tenant)
  slug: science-tokyo-repository-oaipmh
- description: A second GakuNin-registered SAML 2.0 entity carrying the Institute of Science Tokyo identity, hosted on the commercial EX-TIC platform and pointing at the pre-merger medical/dental side of the institu
  name: EX-TIC GakuNin SAML entity (tenant)
  slug: ex-tic-gakunin-entity
- baseURL: https://t2r2.star.titech.ac.jp/oaipmh/OAIHandler
  baseurl_source: declared
  description: OAI-PMH 2.0 protocol verbs. All six verbs are dispatched from a single path via the `verb` query parameter.
  name: Tokyo Institute of Technology OAI PMH API
  slug: tokyo-institute-of-technology-oai-pmh-api
artifact_total: 11
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
  href: https://artifacts.apis.io/tokyo-institute-of-technology/authentication/tokyo-institute-of-technology-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tokyo-institute-of-technology-authentication.yml
- group: design
  href: https://artifacts.apis.io/tokyo-institute-of-technology/conformance/tokyo-institute-of-technology-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tokyo-institute-of-technology-conformance.yml
- group: design
  href: https://artifacts.apis.io/tokyo-institute-of-technology/lifecycle/tokyo-institute-of-technology-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tokyo-institute-of-technology-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/tokyo-institute-of-technology/errors/tokyo-institute-of-technology-errors.yml
  title: ''
  type: ErrorCatalog
  url: errors/tokyo-institute-of-technology-errors.yml
- group: build
  href: https://artifacts.apis.io/tokyo-institute-of-technology/examples/tokyo-institute-of-technology-t2r2-oaipmh-examples.yml
  title: ''
  type: Examples
  url: examples/tokyo-institute-of-technology-t2r2-oaipmh-examples.yml
- group: docs
  href: https://artifacts.apis.io/tokyo-institute-of-technology/openapi/_original/tokyo-institute-of-technology-t2r2-oaipmh-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/tokyo-institute-of-technology-t2r2-oaipmh-openapi.yml
- group: auth
  href: https://artifacts.apis.io/tokyo-institute-of-technology/security/tokyo-institute-of-technology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tokyo-institute-of-technology-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/tokyo-institute-of-technology/plans/tokyo-institute-of-technology-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tokyo-institute-of-technology-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/tokyo-institute-of-technology/rate-limits/tokyo-institute-of-technology-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tokyo-institute-of-technology-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tokyo-institute-of-technology/finops/tokyo-institute-of-technology-finops.yml
  title: ''
  type: FinOps
  url: finops/tokyo-institute-of-technology-finops.yml
- group: design
  href: https://artifacts.apis.io/tokyo-institute-of-technology/json-ld/tokyo-institute-of-technology-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tokyo-institute-of-technology-context.jsonld
- group: other
  href: https://artifacts.apis.io/tokyo-institute-of-technology/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Tokyo Institute of Technology (Tokyo Tech / Titech) was Japan''s leading national institute of technology and ranked #76 in the QS World University Rankings 2025. On 2024-10-01 it merged with Tokyo Medical and Dental University to form the Institute of Science Tokyo (Science Tokyo); the corporate web presence moved to isct.ac.jp while most academic and service systems still run on titech.ac.jp. Its institution-operated programmable footprint is small and, as of 2026-08-30, shrinking. There is no developer portal, no public REST API, no open-data portal and no OAuth or OpenID Connect surface anywhere on its domains. What the institution genuinely operates and we verified live is two protocol endpoints: the T2R2 research repository''s OAI-PMH 2.0 harvesting interface (oai_dc and junii2), and a Shibboleth/SAML 2.0 Identity Provider registered in GakuNin, Japan''s national academic access management federation. The first is being switched off — the operator published a discontinuation
  schedule on 2026-07-22 that ended T2R2 search on 2026-08-20 and ends T2R2 registration on 2026-10-01, moving full text to the Science Tokyo Repository on JAIRO Cloud, which is a TENANT surface run by NII and JPCOAR rather than by the university. The library discovery layer, the syllabus system, the STRDB researcher database and the TSUBAME4 supercomputer service are all real institution-run systems with human interfaces only — none of them publishes a machine-readable contract.'
finops:
- has_sources: true
  method: generated
  name: Tokyo Institute Of Technology Finops
  primary_unit: ''
  service_category: Education
  slug: tokyo-institute-of-technology-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tokyo-institute-of-technology.png
jsonld:
- class_count: 22
  name: Tokyo Institute Of Technology Context
  property_count: 1
  slug: tokyo-institute-of-technology-context
layout: provider
modified: '2026-09-16'
name: Tokyo Institute of Technology
nav: Providers
network: true
overview: 'Tokyo Institute of Technology publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including OAI PMH API, and 3 more. Tagged areas include Education, Higher Education, University, Institute of Technology, and Japan.


  The Tokyo Institute of Technology catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Tokyo Institute of Technology''s developer surface includes developer portal, documentation, support, engineering blog, authentication, code examples, and 26 more developer resources.'
plans:
- name: Tokyo Institute Of Technology Plans Pricing
  plan_count: 2
  slug: tokyo-institute-of-technology-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 1
  name: Tokyo Institute Of Technology Rate Limits
  slug: tokyo-institute-of-technology-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Tokyo Institute of Technology API Rules
  rule_count: 51
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 1
  slug: tokyo-institute-of-technology-rules
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 53.5
    catalog_earned_first_party: 0.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 22.3
    developer_ergonomics: 38.1
    discoverability: 66.1
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 30.4
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
    score: 32.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/tokyo-institute-of-technology/tokyo-institute-of-technology-2026-06-20T195440.png
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
