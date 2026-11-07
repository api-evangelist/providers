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
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/colabro-app/well-known/colabro-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/colabro-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/colabro-app/hosts/colabro-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/colabro-app-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://colabro.app/login
- group: auth
  href: https://artifacts.apis.io/colabro-app/security/colabro-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/colabro-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://colabro.app/
- group: docs
  title: ''
  type: Documentation
  url: https://colabro.app/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://colabro.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://colabro.app/privacy
- group: operate
  title: ''
  type: Support
  url: https://colabro.app/help
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract files were found on the API host or documentation host.
  evidence:
  - status: 0
    url: https://api.colabro.app/openapi.json
  - status: 404
    url: https://colabro.app/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Colabro provides a collaborative workspace platform where teams can manage tables, boards, journals, and integrate AI agents via MCP. Users can create spaces, share data, and automate tasks with agents like Claude, ChatGPT, and Cursor. The service emphasizes real-time collaboration, data privacy, and customizable workflows, supporting various business processes such as budgeting, inventory, and client management.
image: https://colabro.app/og-image.png
layout: provider
modified: '2026-11-04'
name: colabro
nav: Providers
network: true
overview: 'colabro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Collaboration, Workspace, AI Agents, Productivity, and Team Management.


  colabro''s developer surface includes documentation, support, and 7 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Colabro App Domain Security
  slug: colabro-app-domain-security
  summary_line: TLSv1.3
slug: colabro-app
tags:
- Collaboration
- Workspace
- AI Agents
- Productivity
- Team Management
website: https://colabro.app/
---
