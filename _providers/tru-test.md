---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/tru-test/hosts/tru-test-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tru-test-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Tru-Test
- group: auth
  href: https://artifacts.apis.io/tru-test/security/tru-test-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tru-test-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nz.tru-test.com/
- group: operate
  title: ''
  type: Support
  url: https://nz.tru-test.com/contact-us
coverage:
  checked: '2026-10-28'
  detail: The Tru-Test website provides no developer portal or API reference, and attempts to locate an OpenAPI spec on the advertised API host returned no result.
  evidence:
  - status: error
    url: https://api.tru-test.com/openapi.json
  - status: 200
    url: https://tru-test.com/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: Tru-Test, part of Datamars, delivers livestock monitoring and data solutions that help farmers and agribusinesses improve animal health, productivity, and welfare. Their portfolio includes RFID tags, wireless sensors, and cloud‑based analytics platforms that collect real‑time data on movement, weight, and environmental conditions, enabling data‑driven decisions across the livestock supply chain.
image: https://nz.tru-test.com/sites/default/files/2024-04/Tru-Test-SocialMedia.jpg
layout: provider
modified: '2026-10-28'
name: Tru-Test (Datamars)
nav: Providers
network: true
overview: 'Tru-Test (Datamars) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Livestock, Data, and Monitoring.


  Tru-Test (Datamars)''s developer surface includes support and 4 more developer resources.'
plans:
- name: Tru Test Plans Pricing
  plan_count: 0
  slug: tru-test-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Tru Test Rate Limits
  slug: tru-test-rate-limits
scopes:
- name: Tru Test Scopes
  scope_count: 0
  slug: tru-test-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.6
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tru-test/tru-test-2026-11-03T145146.png
security:
- kind: authentication
  name: Tru Test Authentication
  slug: tru-test-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Tru Test Domain Security
  slug: tru-test-domain-security
  summary_line: TLSv1.3
slug: tru-test
tags:
- Company
- Agriculture
- Livestock
- Data
- Monitoring
website: https://nz.tru-test.com/
---
