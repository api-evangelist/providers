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
  href: https://artifacts.apis.io/aixmed/vendors/aixmed-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aixmed-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AIxMed
- group: auth
  href: https://artifacts.apis.io/aixmed/security/aixmed-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aixmed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aixmed.com/
- group: company
  title: ''
  type: About
  url: https://aixmed.com/about
- group: operate
  title: ''
  type: Contact
  url: https://aixmed.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aixmed.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aixmed.com/terms-conditions-of-use
coverage:
  checked: 2026-09-22
  detail: Portal page returns HTML without a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://portal.aixmed.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-22'
description: AIxMed, Inc. provides AI-driven digital cytology solutions that enhance pathology workflows and improve patient care outcomes. Their platform offers quantitative and qualitative data insights, supporting cancer detection and diagnosis through advanced computational tools. The company focuses on delivering efficient, data‑driven pathology solutions across various medical settings, aiming to streamline processes and elevate diagnostic accuracy.
layout: provider
modified: '2026-09-22'
name: AIxMed
nav: Providers
network: true
overview: AIxMed is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Healthcare, Pathology, and Digital Health.
random_paper: 8
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 2.6
  previous_composite: 9.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/aixmed/aixmed-2026-10-11T093510.png
security:
- kind: domain-security
  name: Aixmed Domain Security
  slug: aixmed-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aixmed
tags:
- Company
- Artificial Intelligence
- Healthcare
- Pathology
- Digital Health
website: https://aixmed.com/
---
