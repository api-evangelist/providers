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
  href: https://artifacts.apis.io/comind/hosts/comind-hosts.yml
  title: ''
  type: Hosts
  url: hosts/comind-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.comind.io/legal/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.comind.io/legal/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.comind.io/news
- group: auth
  href: https://artifacts.apis.io/comind/security/comind-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/comind-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.comind.io/
coverage:
  checked: '2026-10-29'
  detail: No documentation or machine-readable API spec was found on the provider's site.
  evidence:
  - status: 200
    url: https://www.comind.io/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: CoMind develops non‑invasive neurotechnology devices that monitor cerebral blood flow and other critical neurophysiological signals at the bedside. Their mission is to redefine how the brain is measured and treated, delivering a simple, single‑measurement solution for clinicians to improve patient outcomes across the care continuum.
image: https://framerusercontent.com/images/rHvELLurfMlPIQlEGFJXxsJqd7U.jpg?scale-down-to=4096
layout: provider
modified: '2026-10-29'
name: CoMind
nav: Providers
network: true
overview: CoMind is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Neurotechnology, Medical Devices, Healthcare, and Monitoring.
random_paper: 10
score:
  band: minimal
  composite: 6.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.0
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
screenshot: https://apis.io/screenshots/comind/comind-2026-11-03T124954.png
security:
- kind: domain-security
  name: Comind Domain Security
  slug: comind-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: comind
tags:
- Company
- Neurotechnology
- Medical Devices
- Healthcare
- Monitoring
website: https://www.comind.io/
---
