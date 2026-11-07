---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'al.ink/you is a public page that receives people for you: it shows your card, works, and files; visitors ask and state their business with no sign-up, and AI answers, follows up, and filters by your r'
  name: alink Core API
  slug: alink-core-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/al-ink/plans/al-ink-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/al-ink-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/al-ink/cli/al-ink-cli.yml
  title: ''
  type: CLI
  url: cli/al-ink-cli.yml
- group: agent
  href: https://artifacts.apis.io/al-ink/llms/al-ink-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/al-ink-llms.txt
- group: agent
  href: https://artifacts.apis.io/al-ink/well-known/al-ink-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/al-ink-well-known.yml
- group: other
  href: https://artifacts.apis.io/al-ink/hosts/al-ink-hosts.yml
  title: ''
  type: Hosts
  url: hosts/al-ink-hosts.yml
- group: other
  href: https://artifacts.apis.io/al-ink/vendors/al-ink-vendors.yml
  title: ''
  type: Vendors
  url: vendors/al-ink-vendors.yml
- group: build
  href: https://artifacts.apis.io/al-ink/packages/al-ink-packages.yml
  title: ''
  type: SDKs
  url: packages/al-ink-packages.yml
- group: build
  href: https://artifacts.apis.io/al-ink/packages/al-ink-packages.yml
  title: ''
  type: Packages
  url: packages/al-ink-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://al.ink/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://al.ink/terms
- group: operate
  title: ''
  type: Support
  url: https://al.ink/support
- group: start
  title: ''
  type: Sandbox
  url: https://al.ink/-/console
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://al.ink/privacy
- group: auth
  href: https://artifacts.apis.io/al-ink/security/al-ink-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/al-ink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://al.ink/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ldclabs
- group: docs
  title: ''
  type: Documentation
  url: https://api.al.ink/
- group: start
  title: ''
  type: GettingStarted
  url: https://al.ink/#how
- group: commercial
  title: ''
  type: Pricing
  url: https://al.ink/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://al.ink/login?mode=signup
coverage:
  checked: '2026-11-01'
  detail: GraphQL endpoint at https://api.al.ink/v1/graphql requires authentication (401 Unauthorized).
  evidence:
  - status: 401
    url: https://api.al.ink/v1/graphql
  reason: auth-required
  state: gated
created: '2026-11-01'
description: 'al.ink/you is a public page that receives people for you: it shows your card, works, and files; visitors ask and state their business with no sign-up, and AI answers, follows up, and filters by your rules. What needs you arrives as one clean request. You can switch the page off at any time.'
image: https://al.ink/_assets/images/alink-og-card.png
layout: provider
modified: '2026-11-01'
name: alink
nav: Providers
network: true
overview: 'alink is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Automation, Public-Page, and Link-Service.


  alink''s developer surface includes CLI, support, sandbox, documentation, getting-started guide, pricing, signup flow, and 13 more developer resources.'
plans:
- name: Al Ink Plans Pricing
  plan_count: 4
  slug: al-ink-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Al Ink Rate Limits
  slug: al-ink-rate-limits
scopes:
- name: Al Ink Scopes
  scope_count: 0
  slug: al-ink-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.7
  facets:
    access_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 48.2
    operational_transparency: 2.6
  previous_composite: 35.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Al Ink Authentication
  slug: al-ink-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Al Ink Domain Security
  slug: al-ink-domain-security
  summary_line: TLSv1.3 · DMARC
slug: al-ink
tags:
- Artificial Intelligence
- Automation
- Public-Page
- Link-Service
website: https://al.ink/
---
