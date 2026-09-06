---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.seeq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://python-docs.seeq.com/
- group: operate
  title: ''
  type: Support
  url: https://support.seeq.com/
- group: company
  title: ''
  type: Blog
  url: https://www.seeq.com/resources/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.seeq.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.seeq.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.seeq.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/seeq-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seeq-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/seeq-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/seeq-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/seeq-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/seeq-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/seeq-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/seeq-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/seeq-llms.txt
created: '2026-07-17'
description: Seeq is an industrial analytics, machine learning and AI software company (Seattle, WA; backed by Insight Partners) serving process manufacturing industries such as oil & gas, chemicals, pharmaceuticals & life sciences, mining & metals, power & utilities, food & beverage and semiconductors. The Seeq AI Platform combines operational time-series data with employee expertise and historical context to speed investigation, monitoring and decision-making. Programmatic access is through the Seeq Server REST API (served per instance at /api with an interactive Swagger surface) and the official Python modules `seeq` and `seeq-spy` (SPy), which offer Pandas/NumPy/Jupyter-optimized functions for searching, pulling, pushing and calculating on signals, conditions and asset models via Seeq Data Lab.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/seeq.png
layout: provider
modified: '2026-07-21'
name: Seeq
nav: Providers
network: true
overview: 'Seeq is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Industrial Analytics, Time Series, and Machine-Learning.


  Seeq''s developer surface includes documentation, support, engineering blog, authentication, changelog, and 11 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 24.5
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/seeq/refs/heads/main/screenshots/seeq-2026-09-02T154755.png
security:
- kind: authentication
  name: Seeq Authentication
  slug: seeq-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Seeq Domain Security
  slug: seeq-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Seeq Trust Center
  slug: seeq-trust-center
  summary_line: SOC 2, ISO 27001, CSA STAR
slug: seeq
tags:
- Company
- Manufacturing
- Industrial Analytics
- Time Series
- Machine-Learning
- Artificial Intelligence
- Process Manufacturing
- Data Analytics
website: https://www.seeq.com/
---
