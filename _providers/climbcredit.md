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
api_count: 1
apis:
- description: Climbcredit offers financing APIs for students and partners, but no public machine‑readable contract was found.
  name: Climbcredit API
  slug: climbcredit-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/climbcredit/hosts/climbcredit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/climbcredit-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://climbcredit.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://climbcredit.com/resources/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://climbcredit.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/climbcredit
- group: auth
  href: https://artifacts.apis.io/climbcredit/security/climbcredit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/climbcredit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://climbcredit.com
coverage:
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract files were found at standard endpoints on api.climbcredit.com or sandbox.climbcredit.com.
  evidence:
  - status: 404
    url: https://api.climbcredit.com/openapi.json
  - status: 404
    url: https://sandbox.climbcredit.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Climbcredit provides flexible financing options for students pursuing career-focused education and training programs. It partners with educational institutions to offer loans and payment plans, aiming to make upskilling and credential programs more affordable and accessible. The platform offers an online portal for applications, loan management, and resources about financing education, targeting adult learners and professionals seeking new career paths.
layout: provider
modified: '2026-10-08'
name: Climbcredit
nav: Providers
network: true
overview: Climbcredit is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Education, Loans, Students, and Careers.
random_paper: 2
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 2.6
  previous_composite: 12.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/climbcredit/climbcredit-2026-11-03T124427.png
security:
- kind: domain-security
  name: Climbcredit Domain Security
  slug: climbcredit-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: climbcredit
tags:
- Finance
- Education
- Loans
- Students
- Careers
website: https://climbcredit.com
---
