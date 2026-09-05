---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://getenjoyhq.com'', ''status'': 308, ''note'': ''declared website redirects to https://www.usertesting.com/platform — a different registrable domain (getenjoyhq.com -> usertesting.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/usertesting/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/enjoyhq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getenjoyhq.com
created: '2026-07-17'
description: EnjoyHQ was a centralized user-research and customer-feedback repository — a single source of truth where product and UX teams stored, tagged, searched, and analyzed qualitative and quantitative research (interviews, surveys, support tickets, NPS scores, and app-store reviews). Backed by Point Nine Capital, it was acquired by UserTesting in 2021 and folded into the UserTesting Human Insight Platform. Its brand domain getenjoyhq.com now issues a permanent (HTTP 308) redirect to usertesting.com/platform/enjoyhq, and EnjoyHQ no longer operates an independent developer, documentation, or API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/enjoyhq.png
layout: provider
modified: '2026-07-19'
name: EnjoyHQ
nav: Providers
network: true
overview: EnjoyHQ is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, User Research, Customer Feedback, Insights Management, and Research Repository.
random_paper: 10
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/enjoyhq/refs/heads/main/screenshots/enjoyhq-2026-07-25T213408.png
security:
- kind: domain-security
  name: Enjoyhq Domain Security
  slug: enjoyhq-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: enjoyhq
tags:
- Company
- User Research
- Customer Feedback
- Insights Management
- Research Repository
- User Experience
- Product Management
- Software-as-a-Service
website: https://getenjoyhq.com
---
