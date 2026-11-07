---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/clearflow/hosts/clearflow-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clearflow-hosts.yml
- group: other
  href: https://artifacts.apis.io/clearflow/vendors/clearflow-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clearflow-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://clearflow.com/news/
- group: auth
  href: https://artifacts.apis.io/clearflow/security/clearflow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clearflow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clearflow.com
- group: docs
  title: ''
  type: Documentation
  url: https://clearflow.com/resources/
- group: operate
  title: ''
  type: Support
  url: https://clearflow.com/support/
- group: company
  title: ''
  type: Blog
  url: https://clearflow.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clearflow.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clearflow.com/privacy-policy/
coverage:
  checked: '2026-10-09'
  detail: API spec endpoints on https://api.clearflow.com return 403, indicating access requires partner credentials.
  evidence:
  - status: 403
    url: https://api.clearflow.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-08'
description: ClearFlow provides innovative medical devices and solutions focused on improving patient recovery after surgery. Their flagship product PleuraFlow offers active chest tube clearance, reducing complications such as retained blood syndrome and postoperative atrial fibrillation. ClearFlow’s technology integrates into enhanced recovery after surgery (ERAS) programs, delivering faster patient discharge, lower ICU stays, and overall better outcomes. The company emphasizes a patient‑centric approach, combining clinical evidence with modern medical device engineering to support hospitals worldwide.
layout: provider
modified: '2026-10-08'
name: ClearFlow
nav: Providers
network: true
overview: 'ClearFlow is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Medical Devices, Surgery, Healthcare, Innovation, and Patient Recovery.


  ClearFlow''s developer surface includes documentation, support, engineering blog, and 7 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 45.5
    operational_transparency: 0.0
  previous_composite: 12.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/clearflow/clearflow-2026-11-03T124345.png
security:
- kind: domain-security
  name: Clearflow Domain Security
  slug: clearflow-domain-security
  summary_line: TLSv1.3 · DMARC
slug: clearflow
tags:
- Medical Devices
- Surgery
- Healthcare
- Innovation
- Patient Recovery
website: https://clearflow.com
---
