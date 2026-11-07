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
- description: The provider offers an API referenced on its site but no machine‑readable contract was found. Documentation appears at the main website.
  name: Congress Plus API
  slug: congress-plus-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/congress-plus/hosts/congress-plus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/congress-plus-hosts.yml
- group: auth
  href: https://artifacts.apis.io/congress-plus/security/congress-plus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/congress-plus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://congressplus.com/
coverage:
  checked: '2026-10-27'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract files were found on any discovered host.
  evidence:
  - status: 404
    url: https://www.congressplus.com/openapi.json
  - status: 404
    url: https://api.congressplus.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Congress Plus provides an online platform that appears to offer services related to congressional information and mobile access. The website features links to a mobile login portal and a contact page, indicating a focus on delivering congressional data or tools to users. Further details are limited, but the site identifies itself as "Congress Plus Online" and includes branding and navigation elements typical of a service-oriented web application.
layout: provider
modified: '2026-10-27'
name: Congress Plus
nav: Providers
network: true
overview: Congress Plus is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government, Data, Platform, Mobile, and Services.
random_paper: 21
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 4.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/congress-plus/congress-plus-2026-11-03T125101.png
security:
- kind: domain-security
  name: Congress Plus Domain Security
  slug: congress-plus-domain-security
  summary_line: TLSv1.3 · DMARC
slug: congress-plus
tags:
- Government
- Data
- Platform
- Mobile
- Services
- Congress
website: https://congressplus.com/
---
