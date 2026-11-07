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
- group: agent
  href: https://artifacts.apis.io/healthleap/llms/healthleap-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/healthleap-llms.txt
- group: other
  href: https://artifacts.apis.io/healthleap/hosts/healthleap-hosts.yml
  title: ''
  type: Hosts
  url: hosts/healthleap-hosts.yml
- group: other
  href: https://artifacts.apis.io/healthleap/vendors/healthleap-vendors.yml
  title: ''
  type: Vendors
  url: vendors/healthleap-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://healthleap.ai/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HealthLeap
- group: auth
  href: https://artifacts.apis.io/healthleap/security/healthleap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/healthleap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.healthleap.ai
- group: docs
  title: ''
  type: Documentation
  url: https://healthleap.ai/about
- group: start
  title: ''
  type: GettingStarted
  url: https://healthleap.ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://healthleap.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://healthleap.ai/terms
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: 404
    url: https://api.healthleap.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Healthleap is an AI-driven healthcare technology company focused on early detection of inpatient risks such as malnutrition, delirium, and aspiration pneumonia. By integrating daily risk scoring into electronic health record (EHR) flowsheets, Healthleap enables clinicians to prioritize at‑risk patients for timely interventions, improving outcomes and reducing undiagnosed conditions. Backed by Sequoia Capital, the company aims to expand its screening platform across multiple clinical conditions.
image: https://storage.googleapis.com/ployai/e6009860-d40b-42ea-bd3d-23ffcc1884fd/user/352a630c-healthleap-share-1200x630.webp
layout: provider
modified: '2026-10-29'
name: Healthleap
nav: Providers
network: true
overview: 'Healthleap is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Healthcare, Risk Screening, and Nutrition.


  Healthleap''s developer surface includes documentation, getting-started guide, and 9 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 56.3
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/healthleap/healthleap-2026-11-03T133321.png
security:
- kind: domain-security
  name: Healthleap Domain Security
  slug: healthleap-domain-security
  summary_line: TLSv1.3 · DMARC
slug: healthleap
tags:
- Company
- Artificial Intelligence
- Healthcare
- Risk Screening
- Nutrition
website: https://www.healthleap.ai
---
