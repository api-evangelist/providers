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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://api.attestari.ai/v1
  baseurl_source: declared
  description: The Health API from Attestari — 1 operation(s) for health.
  name: Attestari Health API
  slug: attestari-ai-health-api
- baseURL: https://api.attestari.ai/v1
  baseurl_source: declared
  description: The Manifest API from Attestari — 2 operation(s) for manifest.
  name: Attestari Manifest API
  slug: attestari-ai-manifest-api
- baseURL: https://api.attestari.ai/v1
  baseurl_source: declared
  description: The Remote API from Attestari — 1 operation(s) for remote.
  name: Attestari Remote API
  slug: attestari-ai-remote-api
- baseURL: https://api.attestari.ai/v1
  baseurl_source: declared
  description: The Verdict API from Attestari — 3 operation(s) for verdict.
  name: Attestari Verdict API
  slug: attestari-ai-verdict-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/attestari-ai/plans/attestari-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/attestari-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/attestari-ai/conformance/attestari-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/attestari-ai-conformance.yml
- group: other
  href: https://artifacts.apis.io/attestari-ai/hosts/attestari-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/attestari-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/attestari-ai/vendors/attestari-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/attestari-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/attestari-ai/security/attestari-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/attestari-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://attestari.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://attestari.ai/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://attestari.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://attestari.ai/terms
- group: start
  title: ''
  type: SignUp
  url: https://app.attestari.ai/signup
- group: start
  title: ''
  type: Login
  url: https://app.attestari.ai/sign-in
created: '2026-11-02'
description: Attestari examines the published artifact of MCP servers and agent tooling, not the repository, publishes the file, line and bytes behind every finding, and refuses to grade what it could not examine. The verdict is public so anyone can check it. No publisher pays.
image: https://attestari.ai/opengraph-image?f0b46a0dce1d99e8
layout: provider
modified: '2026-11-02'
name: Attestari
nav: Providers
network: true
overview: 'Attestari publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Health API, Manifest API, Remote API, and 1 more. Tagged areas include Artificial Intelligence, MCP, Security, Compliance, and Open Source.


  Attestari''s developer surface includes pricing, signup flow, and 9 more developer resources.'
plans:
- name: Attestari Ai Plans Pricing
  plan_count: 13
  slug: attestari-ai-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Attestari Ai Rate Limits
  slug: attestari-ai-rate-limits
scopes:
- name: Attestari Ai Scopes
  scope_count: 0
  slug: attestari-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 37.3
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 33.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Attestari Ai Authentication
  slug: attestari-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Attestari Ai Domain Security
  slug: attestari-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: attestari-ai
tags:
- Artificial Intelligence
- MCP
- Security
- Compliance
- Open Source
website: https://attestari.ai/
---
