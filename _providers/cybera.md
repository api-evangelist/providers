---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: unknown
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 11.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'CYBERA APIs (per the provider A2A agent card at docs.cybera.io/.well-known/agent-card.json, name: "CYBERA API", description: "Prevent fraud using CYBERA''s APIs"): the fraud-prevention and mule-intelli'
  name: Cybera API
  slug: cybera-api
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/cybera/a2a/cybera-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cybera-a2a.yml
- group: agent
  href: https://artifacts.apis.io/cybera/well-known/cybera-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cybera-well-known.yml
- group: other
  href: https://artifacts.apis.io/cybera/vendors/cybera-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cybera-vendors.yml
- group: agent
  href: https://artifacts.apis.io/cybera/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/cybera/hosts/cybera-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cybera-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://www.cybera.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cybera.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cybera.io/reference/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cybera.io/reference/privacy-policy
- group: auth
  href: https://artifacts.apis.io/cybera/security/cybera-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cybera-domain-security.yml
coverage:
  checked: '2026-11-03'
  detail: The public website at www.cybera.io has no developer portal or published OpenAPI; a documentation portal exists at docs.cybera.io but is gated behind OIDC authentication (Redocly), so no machine-readable contract is reachable to a non-customer.
  evidence:
  - status: 200
    url: https://www.cybera.io
  - status: 302
    url: https://docs.cybera.io
  - status: 404
    url: https://docs.cybera.io/openapi.json
  - status: 200
    url: https://www.cybera.io/reference/terms-of-use
  - status: 200
    url: https://www.cybera.io/reference/privacy-policy
  reason: partner-login
  state: gated
created: '2026-10-21'
description: Cybera is an AI-powered mule intelligence and scam response company that helps financial institutions detect, prevent, and respond to authorized payment fraud. Its platform delivers verified, non-probabilistic intelligence on mule accounts to block scam payments in real time, integrates with existing fraud and anti-money laundering (AML) systems, and supports victim recovery through structured case reporting and collaboration with law enforcement and crypto-tracing experts. Cybera serves banks, crypto platforms, and cyber insurance providers.
layout: provider
mcp_servers:
- description: Prevent fraud using CYBERA's APIs
  name: CYBERA API
  slug: cybera-api
modified: '2026-11-03'
name: Cybera
nav: Providers
network: true
overview: 'Cybera is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Platform, Data, and Fraud Prevention.


  Cybera''s developer surface includes documentation and 9 more developer resources.'
plans:
- name: Cybera Plans Pricing
  plan_count: 0
  slug: cybera-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Cybera Rate Limits
  slug: cybera-rate-limits
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.2
    discoverability: 53.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  previous_composite: 4.4
  provenance:
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cybera/cybera-2026-11-03T125943.png
security:
- kind: domain-security
  name: Cybera Domain Security
  slug: cybera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cybera
tags:
- Company
- Technology
- Platform
- Data
- Fraud Prevention
- Scam Response
- Mule Intelligence
- Financial Services
- AML
- Banking
- Cryptocurrency
website: https://www.cybera.io
---
