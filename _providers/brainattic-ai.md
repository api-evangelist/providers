---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 9.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Brainattic knowledge base, documented at the provider's docs site.
  name: Brainattic API
  slug: brainattic-api
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/brainattic-ai/authentication/brainattic-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/brainattic-ai-authentication.yml
- group: agent
  href: https://artifacts.apis.io/brainattic-ai/llms/brainattic-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brainattic-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/brainattic-ai/well-known/brainattic-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/brainattic-ai-security.txt
- group: auth
  href: https://artifacts.apis.io/brainattic-ai/well-known/brainattic-ai-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/brainattic-ai-app-security.txt
- group: agent
  href: https://artifacts.apis.io/brainattic-ai/well-known/brainattic-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brainattic-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/brainattic-ai/hosts/brainattic-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brainattic-ai-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brainattic.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://brainattic.ai/support
- group: auth
  title: ''
  type: Security
  url: https://brainattic.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brainattic.ai/privacy
- group: start
  title: ''
  type: Login
  url: https://app.brainattic.ai/login
- group: start
  title: ''
  type: GettingStarted
  url: https://brainattic.ai/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/brainattic-ai/security/brainattic-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/brainattic-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/brainattic-ai/security/brainattic-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brainattic-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brainattic.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://brainattic.ai/docs
coverage:
  checked: '2026-11-03'
  detail: Docs pages are served as HTML rendered by JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://brainattic.ai/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Brainattic provides a governed knowledge base that teams and AI agents can read and write. It operates over an MCP with hybrid search and customizable rules, supporting Claude, ChatGPT, and Mistral. The platform emphasizes data governance, security, and seamless integration for enterprise knowledge management.
image: https://brainattic.ai/assets/brainattic-og.png
layout: provider
modified: '2026-11-02'
name: brainattic
nav: Providers
network: true
overview: 'brainattic is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Knowledge Base, Artificial Intelligence, Enterprise, Governance, and MCP.


  brainattic''s developer surface includes authentication, support, getting-started guide, documentation, and 12 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 16.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 25.0
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Brainattic Ai Authentication
  slug: brainattic-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Brainattic Ai Domain Security
  slug: brainattic-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Brainattic Ai Vulnerability Disclosure
  slug: brainattic-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: brainattic-ai
tags:
- Knowledge Base
- Artificial Intelligence
- Enterprise
- Governance
- MCP
- Company
website: https://brainattic.ai/
---
