---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-09-04'
api_count: 2
apis:
- baseURL: https://api.myome.com/0/
  baseurl_source: declared
  description: Institution onboarding and institution-scoped operations (requisitions, orders, campaigns).
  name: MyOme Institutional Interface API
  slug: myome-institutional-interface-api
- baseURL: https://api.myome.com/0/
  baseurl_source: declared
  description: Submit, list, and fetch requisitions and orders; get order results; list re-requisitionable products.
  name: MyOme Requisitions and Orders API
  slug: myome-requisitions-and-orders-api
- baseURL: https://api.myome.com/0/
  baseurl_source: declared
  description: Reference data—orderable products and consent types (general and product-specific).
  name: MyOme Resources API
  slug: myome-resources-api
artifact_total: 7
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/myome-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/myome-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://myome.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.myome.com/0/ui/
- group: docs
  title: ''
  type: APIReference
  url: https://api.myome.com/0/ui/
- group: operate
  title: ''
  type: Support
  url: https://myome.com/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://myome.com/resources/faq
- group: company
  title: ''
  type: Blog
  url: https://myome.com/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/myome
- group: commercial
  title: ''
  type: TermsOfService
  url: https://myome.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://myome.com/legal/privacy-notice
- group: start
  title: ''
  type: SignUp
  url: https://providers.myome.com/
- group: start
  title: ''
  type: Login
  url: https://patients.myome.com/
- group: auth
  title: ''
  type: Compliance
  url: https://myome.com/about-us/privacy-and-security
- group: commercial
  title: ''
  type: Plans
  url: plans/myome-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/myome-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/myome-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/myome-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/myome-domain-security.yml
created: '2026-08-26'
description: 'MyOme is a CLIA-certified and CAP-accredited clinical laboratory in Menlo Park, California that builds a whole-genome analysis platform for inherited disease risk. A single patient sample is sequenced once and re-interpreted over time to produce clinically actionable reports: Single-Gene Risk, Medication Response (pharmacogenomics), and cross-ancestry Integrated Polygenic Risk Scores (iPRS) for breast cancer, coronary artery disease, prostate cancer and type 2 diabetes, alongside a rare-disease portfolio spanning genome, exome and copy-number analysis. MyOme publishes a partner-facing REST API (OpenAPI 3.0.2, version 2.51.0) at api.myome.com that lets institutional clients list orderable products, submit sequencing requisitions, track requisition and order status, and retrieve results including sequencing data, structured interpretation data and PDF reports. Authorization is bearer JWT issued by MyOme''s Keycloak at auth.myome.com using partner-specific credentials, and a separate
  external sandbox instance (api.sbx.myome.com) is published for partner testing and development.'
image: https://myome.com/ext/myome.png
layout: provider
modified: '2026-08-26'
name: MyOme
nav: Providers
network: true
overview: 'MyOme publishes 3 APIs on the [APIs.io](https://apis.io/) network: Institutional Interface API, Requisitions and Orders API, and Resources API. Tagged areas include Company, Genomics, Healthcare, Clinical Laboratory, and Whole Genome Sequencing.


  MyOme''s developer surface includes documentation, API reference, support, engineering blog, signup flow, and 15 more developer resources.'
plans:
- name: Myome Plans Pricing
  plan_count: 0
  slug: myome-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Myome Rate Limits
  slug: myome-rate-limits
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 4.5
    contract_quality: 56.2
    developer_ergonomics: 44.6
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 44.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 62.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/myome/refs/heads/main/screenshots/myome-2026-09-02T150707.png
security:
- kind: authentication
  name: Myome Authentication
  slug: myome-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Myome Domain Security
  slug: myome-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: myome
tags:
- Company
- Genomics
- Healthcare
- Clinical Laboratory
- Whole Genome Sequencing
- Precision Medicine
- Bioinformatics
- Polygenic Risk Scores
- Pharmacogenomics
- Rare Disease
- Diagnostics
- Life Sciences
website: https://myome.com/
---
