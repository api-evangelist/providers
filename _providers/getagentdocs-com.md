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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
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
  score: 6.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/getagentdocs-com/conformance/getagentdocs-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getagentdocs-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/getagentdocs-com/llms/getagentdocs-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getagentdocs-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/getagentdocs-com/well-known/getagentdocs-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getagentdocs-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/getagentdocs-com/hosts/getagentdocs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getagentdocs-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/getagentdocs-com/vendors/getagentdocs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getagentdocs-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getagentdocs.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getagentdocs.com/privacy
- group: start
  title: ''
  type: Login
  url: https://getagentdocs.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://getagentdocs.com/features/docs/
- group: company
  title: ''
  type: Blog
  url: https://getagentdocs.com/blog/
- group: auth
  href: https://artifacts.apis.io/getagentdocs-com/security/getagentdocs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getagentdocs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getagentdocs.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://getagentdocs.com/mcp
  - status: 200
    url: https://getagentdocs.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: AgentDocs provides an AI‑powered office suite designed for personal AI agents. It offers Docs, Sheets, Slides, Database, Drive, and Pages that agents can read, write, and edit in real time. The platform emphasizes cheap, fast, agent‑first collaboration, with markdown‑native live co‑editing, version history, and integration with Claude. Publicly available at getagentdocs.com, it includes guides, a blog, and pricing information, targeting developers and enterprises building AI‑agent workflows.
image: https://getagentdocs.com/connect-poster.png
layout: provider
modified: '2026-10-30'
name: getagentdocs-com
nav: Providers
network: true
overview: 'getagentdocs-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Office Suite, Collaboration, Agent-first, and Productivity.


  getagentdocs-com''s developer surface includes documentation, engineering blog, and 10 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 16.6
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/getagentdocs-com/getagentdocs-com-2026-11-03T132640.png
security:
- kind: domain-security
  name: Getagentdocs Com Domain Security
  slug: getagentdocs-com-domain-security
  summary_line: TLSv1.3
slug: getagentdocs-com
tags:
- Artificial Intelligence
- Office Suite
- Collaboration
- Agent-first
- Productivity
website: https://getagentdocs.com/
---
