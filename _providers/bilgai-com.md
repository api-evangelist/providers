---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
api_count: 1
apis:
- description: Bilg provides an MCP endpoint for agents to read and write projects, tasks, and documents via HTTP with API keys. Documentation is at https://app.bilgai.com/docs/connect.
  name: Bilg API
  slug: bilg-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/bilgai-com/plans/bilgai-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bilgai-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/bilgai-com/authentication/bilgai-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bilgai-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/bilgai-com/well-known/bilgai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bilgai-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bilgai-com/hosts/bilgai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bilgai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bilgai-com/vendors/bilgai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bilgai-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.bilgai.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.bilgai.com/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://app.bilgai.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.bilgai.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://app.bilgai.com/docs/connect
- group: auth
  href: https://artifacts.apis.io/bilgai-com/security/bilgai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bilgai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://app.bilgai.com/
coverage:
  checked: '2026-11-02'
  detail: Documentation pages are HTML without a published OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://app.bilgai.com/docs/connect
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Bilg provides a shared context platform for teams and AI agents, enabling collaborative knowledge bases, prompt sharing, and integrated tooling. The service offers a unified workspace where users can store, search, and manage prompts, code snippets, and documentation, with AI-powered assistance to streamline workflows. It supports connections to Claude, Claude Desktop, Cursor, and other MCP clients, allowing seamless integration into existing development pipelines. The platform emphasizes security, privacy, and team collaboration, making it suitable for enterprises and developers seeking to enhance productivity through AI-driven knowledge management.
layout: provider
modified: '2026-11-02'
name: Bilg
nav: Providers
network: true
overview: 'Bilg is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Collaboration, Knowledge Base, and Productivity.


  Bilg''s developer surface includes authentication, pricing, getting-started guide, and 9 more developer resources.'
plans:
- name: Bilgai Com Plans Pricing
  plan_count: 2
  slug: bilgai-com-plans-pricing
random_paper: 20
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 8.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 53.6
    operational_transparency: 0.0
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bilgai Com Authentication
  slug: bilgai-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bilgai Com Domain Security
  slug: bilgai-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bilgai-com
tags:
- Company
- Artificial Intelligence
- Collaboration
- Knowledge Base
- Productivity
- Team Workspace
website: https://app.bilgai.com/
---
