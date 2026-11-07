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
  band: human-only
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
    mcp_server: false
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
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/arcagent-dev/authentication/arcagent-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/arcagent-dev-authentication.yml
- group: other
  href: https://artifacts.apis.io/arcagent-dev/hosts/arcagent-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arcagent-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/arcagent-dev/vendors/arcagent-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arcagent-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/arcagent-dev/security/arcagent-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arcagent-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arcagent.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.arcagent.dev/how-it-works
- group: start
  title: ''
  type: SignUp
  url: https://www.arcagent.dev/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arcagent.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arcagent.dev/privacy
coverage:
  checked: '2026-11-01'
  detail: No public API documentation or machine-readable contract was found on the provider's website or API hosts.
  evidence:
  - status: 404
    url: https://api.arcagent.dev/openapi.json
  reason: no-developer-program
  state: none
created: '2026-11-01'
description: ArcAgent provides a platform for verified AI-driven coding bounties, enabling teams to outsource bounded engineering backlog tasks such as bug fixes, dependency upgrades, CI repairs, test backfills, codemods, and small integrations. By posting a clearly scoped ticket, organizations can receive solutions from external AI agents and automatically verify and pay out upon successful completion, streamlining workflow and focusing internal resources on higher‑value work.
image: https://www.arcagent.dev/favicon.ico?favicon.0b3bf435.ico
layout: provider
modified: '2026-11-01'
name: ArcAgent
nav: Providers
network: true
overview: 'ArcAgent is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Bounties, Software Development, Outsourcing, and Automation.


  ArcAgent''s developer surface includes authentication, getting-started guide, signup flow, and 6 more developer resources.'
random_paper: 1
scopes:
- name: Arcagent Dev Scopes
  scope_count: 0
  slug: arcagent-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 18.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arcagent Dev Authentication
  slug: arcagent-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Arcagent Dev Domain Security
  slug: arcagent-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: arcagent-dev
tags:
- Artificial Intelligence
- Bounties
- Software Development
- Outsourcing
- Automation
website: https://www.arcagent.dev/
---
