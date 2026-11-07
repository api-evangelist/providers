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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Factrail provides an evidence infrastructure for AI agents via its MCP endpoint. Documentation is not publicly machine‑readable.
  name: Factrail API
  slug: factrail-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/factrail-online/llms/factrail-online-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/factrail-online-llms.txt
- group: other
  href: https://artifacts.apis.io/factrail-online/hosts/factrail-online-hosts.yml
  title: ''
  type: Hosts
  url: hosts/factrail-online-hosts.yml
- group: other
  href: https://artifacts.apis.io/factrail-online/vendors/factrail-online-vendors.yml
  title: ''
  type: Vendors
  url: vendors/factrail-online-vendors.yml
- group: auth
  href: https://artifacts.apis.io/factrail-online/security/factrail-online-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/factrail-online-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://factrail.online/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mcp.factrail.online
- group: docs
  title: ''
  type: Documentation
  url: https://factrail.online/docs
- group: docs
  title: ''
  type: APIReference
  url: https://factrail.online/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://factrail.online/docs
- group: operate
  title: ''
  type: Support
  url: https://factrail.online/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/baronsigma
coverage:
  checked: '2026-10-30'
  detail: Documentation pages return HTML shells and no machine‑readable OpenAPI spec is available.
  evidence:
  - status: 200
    url: https://factrail.online/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Factrail provides an evidence infrastructure for AI agents, offering structured, source‑backed real‑world data with provenance, freshness, and conflict resolution. The platform delivers capabilities such as factrail_capabilities, factrail_verify, factrail_assess, and factrail_get_receipt via its MCP endpoint, enabling agents to retrieve verified company, trade, and import information, along with reusable receipts for result integrity. Public beta access is available, with integration guides on GitHub and developer documentation.
layout: provider
modified: '2026-10-30'
name: factrail-online
nav: Providers
network: true
overview: 'factrail-online is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Evidence, Data, Platform, and Company.


  factrail-online''s developer surface includes documentation, API reference, getting-started guide, support, and 7 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.7
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 60.7
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/factrail-online/factrail-online-2026-11-03T131810.png
security:
- kind: domain-security
  name: Factrail Online Domain Security
  slug: factrail-online-domain-security
  summary_line: TLSv1.3
slug: factrail-online
tags:
- Artificial Intelligence
- Evidence
- Data
- Platform
- Company
website: https://factrail.online/
---
