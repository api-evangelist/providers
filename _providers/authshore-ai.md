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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AuthShore provides a pure REST JSON API for authentication, user pools, secrets vault, and JWT management.
  name: AuthShore API
  slug: authshore-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/authshore-ai/llms/authshore-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/authshore-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/authshore-ai/hosts/authshore-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/authshore-ai-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.authshore.ai/
- group: start
  title: ''
  type: SignUp
  url: https://authshore.ai/signup/customer
- group: docs
  title: ''
  type: Documentation
  url: https://authshore.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://authshore.ai/docs/quickstart.html
- group: auth
  href: https://artifacts.apis.io/authshore-ai/security/authshore-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/authshore-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://authshore.ai/
- group: other
  title: ''
  type: Image
  url: https://prodmedia.tyga.host/public/tyga.cloud/landing/authshore.ai/favicon.ico
created: '2026-11-02'
description: AuthShore provides agent‑native authentication infrastructure designed for AI‑assisted development. It offers user pools, secret vaults, and JWT token issuance via pure APIs without a dashboard. The platform supports integration with Claude Code, Cursor, Cline, Windsurf, and Aider, enabling seamless authentication flows for coding agents. AuthShore aims to simplify secure access management for AI‑driven applications, delivering a lightweight, developer‑friendly solution.
layout: provider
modified: '2026-11-02'
name: AuthShore
nav: Providers
network: true
overview: 'AuthShore is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Authentication, Artificial Intelligence, Developer Tools, and Security.


  AuthShore''s developer surface includes signup flow, documentation, getting-started guide, and 6 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 53.6
    operational_transparency: 7.9
  previous_composite: 13.8
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Authshore Ai Domain Security
  slug: authshore-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: authshore-ai
tags:
- Authentication
- Artificial Intelligence
- Developer Tools
- Security
website: https://authshore.ai/
---
