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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Telemetry events endpoint for Cimento agent hub.
  name: Agent Hub
  slug: agent-hub
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/cimento/llms/cimento-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cimento-llms.txt
- group: other
  href: https://artifacts.apis.io/cimento/a2a/cimento-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cimento-a2a.yml
- group: agent
  href: https://artifacts.apis.io/cimento/well-known/cimento-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cimento-well-known.yml
- group: other
  href: https://artifacts.apis.io/cimento/hosts/cimento-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cimento-hosts.yml
- group: other
  href: https://artifacts.apis.io/cimento/vendors/cimento-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cimento-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://cimento.ai/security
- group: auth
  href: https://artifacts.apis.io/cimento/security/cimento-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cimento-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cimento.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cimento.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cimento.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cimento.ai/index
- group: commercial
  title: ''
  type: Pricing
  url: https://cimento.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cimento.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cimento.ai/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cimento
coverage:
  checked: '2026-10-29'
  detail: The API endpoint for telemetry events requires authentication and a tenant, so the contract is not publicly accessible.
  evidence:
  - status: 200
    url: https://docs.cimento.ai/agent-hub/how-it-works.md
  reason: customer-only-docs
  state: gated
created: '2026-10-29'
description: AI-powered human risk management platform offering multi-channel phishing simulations via email, SMS, and voice, coupled with adaptive training that automatically reduces risk. Cimento enables security teams to assess, train, and continuously monitor employee risk, delivering real-time risk scores and personalized security awareness content. The solution integrates with existing security tools, provides detailed reporting, and supports scalable deployment for enterprises seeking to strengthen their human firewall against social engineering attacks.
image: https://framerusercontent.com/images/EV5xYJWWexechVev6A8FlyOg9rY.png
layout: provider
modified: '2026-10-29'
name: Cimento
nav: Providers
network: true
overview: 'Cimento is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Phishing Simulation, Human Risk Management, Security, and Training.


  Cimento''s developer surface includes documentation, API reference, getting-started guide, pricing, and 11 more developer resources.'
plans:
- name: Cimento Plans Pricing
  plan_count: 0
  slug: cimento-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Cimento Rate Limits
  slug: cimento-rate-limits
scopes:
- name: Cimento Scopes
  scope_count: 0
  slug: cimento-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 73.2
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 23.2
  provenance:
    conformance: unknown
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
screenshot: https://apis.io/screenshots/cimento/cimento-2026-11-03T124141.png
security:
- kind: authentication
  name: Cimento Authentication
  slug: cimento-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Cimento Domain Security
  slug: cimento-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cimento
tags:
- Artificial Intelligence
- Phishing Simulation
- Human Risk Management
- Security
- Training
website: https://cimento.ai/
---
