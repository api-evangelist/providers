---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Real‑time regulatory analysis and political intelligence API for Latin America. Provides endpoints for bills, regulations, actors, countries, and data freshness.
  name: Dapper API
  slug: dapper-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/dapperglobal-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/dapperglobal-com/cli/dapperglobal-com-cli.yml
  title: ''
  type: CLI
  url: cli/dapperglobal-com-cli.yml
- group: design
  href: https://artifacts.apis.io/dapperglobal-com/conventions/dapperglobal-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dapperglobal-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/dapperglobal-com/authentication/dapperglobal-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dapperglobal-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/dapperglobal-com/conformance/dapperglobal-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dapperglobal-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dapperglobal-com/llms/dapperglobal-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dapperglobal-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/dapperglobal-com/well-known/dapperglobal-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dapperglobal-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/dapperglobal-com/well-known/dapperglobal-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dapperglobal-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dapperglobal-com/hosts/dapperglobal-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dapperglobal-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dapperglobal-com/vendors/dapperglobal-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dapperglobal-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.dapperglobal.com/es/co/auth/login
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.dapperglobal.com/en
- group: docs
  title: ''
  type: Documentation
  url: https://developers.dapperglobal.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.dapperglobal.com\\\
- group: docs
  title: ''
  type: APIReference
  url: https://developers.dapperglobal.com/es/reference
- group: auth
  href: https://artifacts.apis.io/dapperglobal-com/security/dapperglobal-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dapperglobal-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dapperglobal.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.dapperglobal.com
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.dapperglobal.com/openapi.json
  - status: 401
    url: https://api.dapperglobal.com/mcp
  - status: 200
    url: https://dapperglobal.com/
  reason: partner-login
  state: gated
created: '2026-11-04'
description: Dapper provides real‑time regulatory analysis and public affairs data, helping companies monitor and navigate government actions, policy changes, and stakeholder engagements. Their platform aggregates public records, legislative tracking, and media monitoring into actionable insights, offering dashboards, alerts, and API access for seamless integration into compliance workflows.
image: https://interlat.co/wp-content/uploads/2025/09/Logo-Dapper-1.png
layout: provider
modified: '2026-11-04'
name: Dapper
nav: Providers
network: true
overview: 'Dapper is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Regulatory, Data, and Analytics.


  Dapper''s developer surface includes CLI, authentication, getting-started guide, documentation, API reference, engineering blog, and 12 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 66.0
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dapperglobal Com Authentication
  slug: dapperglobal-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dapperglobal Com Domain Security
  slug: dapperglobal-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dapperglobal-com
tags:
- Company
- Regulatory
- Data
- Analytics
website: https://dapperglobal.com/
---
