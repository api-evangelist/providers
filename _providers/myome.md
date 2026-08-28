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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Partner-facing REST API for MyOme's clinical whole-genome laboratory. Clients list the sequencing and analysis Products available to them (identifiers prefixed PR), submit Requisitions for a sample (p
  name: MyOme API
  slug: myome-api
artifact_total: 5
common:
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
overview: 'MyOme publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Genomics, Healthcare, Clinical Laboratory, and Whole Genome Sequencing.


  MyOme''s developer surface includes documentation, API reference, support, engineering blog, signup flow, and 12 more developer resources.'
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
  composite: 43.1
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 16.7
    contract_quality: 54.8
    developer_ergonomics: 44.6
    discoverability: 68.5
    governance: 16.7
    operational_transparency: 2.6
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 46.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
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
