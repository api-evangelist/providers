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
- description: API for Resilience cyber risk management platform
  name: Resilience API
  slug: resilience-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/resilienceinsurance-com/hosts/resilienceinsurance-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/resilienceinsurance-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/resilienceinsurance-com/vendors/resilienceinsurance-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/resilienceinsurance-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/resilienceinsurance-com/security/resilienceinsurance-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/resilienceinsurance-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://resilienceinsurance.com
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract discovered on provider hosts.
  evidence:
  - status: 404
    url: https://api.resilienceinsurance.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Resilience provides cyber risk management and insurance solutions, combining real‑time security posture data with AI‑driven risk quantification and tailored cyber insurance products. The platform helps enterprises assess, prioritize, and mitigate cyber threats while offering coverage that translates technical risk into financial protection.
image: https://cyberresilience.com/wp-content/uploads/2026/01/homepage_hero_hero_xl_1-1.webp
layout: provider
modified: '2026-10-29'
name: Resilience
nav: Providers
network: true
overview: Resilience is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cyber Risk, Insurance, Artificial Intelligence, and Enterprise.
random_paper: 15
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 4.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 4.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/resilienceinsurance-com/resilienceinsurance-com-2026-11-03T142211.png
security:
- kind: domain-security
  name: Resilienceinsurance Com Domain Security
  slug: resilienceinsurance-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: resilienceinsurance-com
tags:
- Company
- Cyber Risk
- Insurance
- Artificial Intelligence
- Enterprise
website: https://resilienceinsurance.com
---
