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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/stratio/well-known/stratio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/stratio-well-known.yml
- group: other
  href: https://artifacts.apis.io/stratio/hosts/stratio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stratio-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stratio.ai/legal-notice/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stratio.ai/privacy/
- group: other
  title: ''
  type: Leadership
  url: https://stratio.ai/team/david-gavina/
- group: company
  title: ''
  type: Blog
  url: https://stratio.ai/blog/
- group: auth
  href: https://artifacts.apis.io/stratio/security/stratio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stratio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stratio.ai
coverage:
  checked: '2026-10-22'
  detail: No OpenAPI or other machine-readable API contract found on stratio.ai despite checking common spec locations.
  evidence:
  - status: 404
    url: https://stratio.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Stratio's Decision Intelligence software helps regulated enterprises deploy AI safely. Built for banking, insurance and public administration in Europe and LATAM, it provides data governance, model monitoring, and compliance tools to enable trustworthy AI adoption across regulated sectors.
layout: provider
modified: '2026-10-21'
name: Stratio
nav: Providers
network: true
overview: 'Stratio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Decision Intelligence, Regulated-Enterprises, and Data Governance.


  Stratio''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 45.5
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/stratio/stratio-2026-11-03T143906.png
security:
- kind: domain-security
  name: Stratio Domain Security
  slug: stratio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stratio
tags:
- Company
- Artificial Intelligence
- Decision Intelligence
- Regulated-Enterprises
- Data Governance
website: https://stratio.ai
---
