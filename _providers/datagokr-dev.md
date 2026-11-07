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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 21.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/datagokr-dev/llms/datagokr-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datagokr-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/datagokr-dev/well-known/datagokr-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datagokr-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/datagokr-dev/hosts/datagokr-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datagokr-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/datagokr-dev/vendors/datagokr-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datagokr-dev-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datagokr.dev/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/datagokr-dev/datagokr/releases/latest/download/datagokr.mcpb
- group: auth
  href: https://artifacts.apis.io/datagokr-dev/security/datagokr-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datagokr-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datagokr.dev/
- group: other
  title: ''
  type: Image
  url: https://datagokr.dev/icon.png
coverage:
  checked: '2026-11-05'
  detail: The provider’s website is a JavaScript‑rendered page with no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://datagokr.dev/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: datagokr provides an AI-powered extension (MCP) that enables users to search the Korean public data portal (data.go.kr) via natural language, apply for usage, and download datasets directly through an integrated desktop app. It indexes 109,000 datasets, supports voice interaction, and streamlines the data request workflow for developers and analysts.
layout: provider
modified: '2026-11-04'
name: datagokr
nav: Providers
network: true
overview: 'datagokr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Data, Artificial Intelligence, Public Data, Korean, and MCP.


  datagokr''s developer surface includes changelog and 8 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Datagokr Dev Domain Security
  slug: datagokr-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: datagokr-dev
tags:
- Data
- Artificial Intelligence
- Public Data
- Korean
- MCP
website: https://datagokr.dev/
---
