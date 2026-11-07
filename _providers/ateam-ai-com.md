---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
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
api_count: 1
apis:
- description: A-Team MCP provides endpoints for building, deploying, and managing AI applications.
  name: A-Team API
  slug: a-team-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/ateam-ai-com/hosts/ateam-ai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ateam-ai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ateam-ai-com/vendors/ateam-ai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ateam-ai-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/ateam-ai-com/packages/ateam-ai-com-packages.yml
  title: ''
  type: SDKs
  url: packages/ateam-ai-com-packages.yml
- group: build
  href: https://artifacts.apis.io/ateam-ai-com/packages/ateam-ai-com-packages.yml
  title: ''
  type: Packages
  url: packages/ateam-ai-com-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ateam-ai.com/privacy
- group: auth
  href: https://artifacts.apis.io/ateam-ai-com/security/ateam-ai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ateam-ai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ateam-ai.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ateam-ai.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://get-started.ateam-ai.com
- group: docs
  title: ''
  type: APIReference
  url: https://get-started.ateam-ai.com
- group: start
  title: ''
  type: GettingStarted
  url: https://get-started.ateam-ai.com
- group: start
  title: ''
  type: SignUp
  url: https://get-started.ateam-ai.com
coverage:
  checked: '2026-11-02'
  detail: Documentation pages are public but no machine‑readable API specification (OpenAPI/GraphQL/AsyncAPI) could be retrieved.
  evidence:
  - status: 404
    url: https://api.ateam-ai.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: A-Team is an AI Application Platform that enables users to design, build, deploy, govern, and operate complete AI-powered applications. It supports multiple large language models including OpenAI, Anthropic, Ollama, and SGLang, and can run in the cloud, on managed services, or on‑premises. The platform offers low‑code skill creation, tool integration, governance policies, and runtime monitoring, allowing enterprises to create AI teams that automate tasks across email, messaging, documents, and more.
image: https://ateam-ai.com/favicon.ico
layout: provider
modified: '2026-11-01'
name: A-Team
nav: Providers
network: true
overview: 'A-Team is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Platform, Low-Code, Integration, and Automation.


  A-Team''s developer surface includes documentation, API reference, getting-started guide, signup flow, and 8 more developer resources.'
plans:
- name: Ateam Ai Com Plans Pricing
  plan_count: 0
  slug: ateam-ai-com-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Ateam Ai Com Rate Limits
  slug: ateam-ai-com-rate-limits
scopes:
- name: Ateam Ai Com Scopes
  scope_count: 0
  slug: ateam-ai-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 20.9
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ateam Ai Com Authentication
  slug: ateam-ai-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ateam Ai Com Domain Security
  slug: ateam-ai-com-domain-security
  summary_line: TLSv1.3
slug: ateam-ai-com
tags:
- Artificial Intelligence
- Platform
- Low-Code
- Integration
- Automation
- Governance
website: https://ateam-ai.com/
---
