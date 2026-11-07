---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
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
    error_semantics: derived
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
  score: 19.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Practical help for privacy, recovery codes, reporting, message retention and AI permissions on AnonPing.
  name: AnonPing API
  slug: anonping-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/anonping-com/rules/anonping-com-rules.yml
  title: ''
  type: Spectral
  url: rules/anonping-com-rules.yml
- group: auth
  href: https://artifacts.apis.io/anonping-com/authentication/anonping-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/anonping-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/anonping-com/scopes/anonping-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/anonping-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/anonping-com/errors/anonping-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/anonping-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/anonping-com/conformance/anonping-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anonping-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/anonping-com/well-known/anonping-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anonping-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/anonping-com/hosts/anonping-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anonping-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/anonping-com/security/anonping-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anonping-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anonping.com/
- group: docs
  title: ''
  type: Documentation
  url: https://anonping.com/guides/
- group: start
  title: ''
  type: GettingStarted
  url: https://anonping.com/guides/
- group: operate
  title: ''
  type: Support
  url: https://anonping.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anonping.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anonping.com/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://anonping.com/app/
coverage:
  checked: '2026-11-01'
  detail: Documentation pages are HTML only and no OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL files were found.
  evidence:
  - status: 404
    url: https://anonping.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AnonPing is an anonymous chat platform for adults that enables random text conversations, friend connections, media sharing, and AI integration via MCP. Users can start chats without email or phone, keep connections, share pictures and voice messages, and post public thoughts in Time Square. The service emphasizes privacy, provides recovery codes, and offers guides on safety, privacy, and community rules.
image: https://anonping.com/favicon.svg
layout: provider
modified: '2026-11-01'
name: AnonPing
nav: Providers
network: true
overview: 'AnonPing publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Chat, Anonymous, Social, Artificial Intelligence, and Privacy.


  The AnonPing catalog on APIs.io includes 1 Spectral governance ruleset.


  AnonPing''s developer surface includes authentication, documentation, getting-started guide, support, signup flow, and 10 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: AnonPing API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: anonping-com-rules
scopes:
- name: Anonping Com Scopes
  scope_count: 3
  slug: anonping-com-scopes
  summary_line: 3 scopes
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 17.1
    contract_governance: 31.8
    contract_quality: 0.0
    developer_ergonomics: 25.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 26.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Anonping Com Authentication
  slug: anonping-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Anonping Com Domain Security
  slug: anonping-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: anonping-com
tags:
- Chat
- Anonymous
- Social
- Artificial Intelligence
- Privacy
website: https://anonping.com/
---
