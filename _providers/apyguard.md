---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 23.4
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Apyguard Agentic Access
  operation_count: 6
  slug: apyguard-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: Machine-readable discovery resources exposed by apyguard.com for agents and integrators.
  name: ApyGuard Public Discovery API
  slug: apyguard-public-discovery-api
artifact_total: 6
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apyguard/refs/heads/main/agentic-access/apyguard-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apyguard-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/apyguard/refs/heads/main/plans/apyguard-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apyguard-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apyguard/refs/heads/main/rules/apyguard-rules.yml
  title: ''
  type: Spectral
  url: rules/apyguard-rules.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apyguard/refs/heads/main/authentication/apyguard-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apyguard-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apyguard/refs/heads/main/conformance/apyguard-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apyguard-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apyguard/refs/heads/main/llms/apyguard-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apyguard-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apyguard/refs/heads/main/a2a/apyguard-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/apyguard-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apyguard/refs/heads/main/well-known/apyguard-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apyguard-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apyguard/refs/heads/main/hosts/apyguard-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apyguard-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apyguard/refs/heads/main/vendors/apyguard-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apyguard-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://www.apyguard.com/resources/playground
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.apyguard.com/get-started/quick-start
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apyguard/refs/heads/main/security/apyguard-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apyguard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apyguard.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.apyguard.com/features
- group: commercial
  title: ''
  type: Pricing
  url: https://www.apyguard.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apyguard.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apyguard.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.apyguard.com/signup
- group: company
  title: ''
  type: Blog
  url: https://www.apyguard.com/resources/blog
created: '2026-10-16'
description: ApyGuard is an API security platform that discovers endpoints, generates OpenAPI specs, and tests APIs for authorization, authentication, and business‑logic risks before production. It offers features such as OWASP API Top 10 scanning, AI‑generated attacks, CI/CD integration, behavior profiling, and a free developer‑first scanning tool.
image: https://www.apyguard.com/images/og-image.png
layout: provider
modified: '2026-10-16'
name: Apyguard
nav: Providers
network: true
overview: 'Apyguard is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API Security, Developer Tools, Software-as-a-Service, and Cloud.


  The Apyguard catalog on APIs.io includes 1 Spectral governance ruleset.


  Apyguard''s developer surface includes authentication, sandbox, getting-started guide, documentation, pricing, signup flow, engineering blog, and 13 more developer resources.'
plans:
- name: Apyguard Plans Pricing
  plan_count: 3
  slug: apyguard-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: Apyguard API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 1
  slug: apyguard-rules
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 73.2
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Apyguard Authentication
  slug: apyguard-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Apyguard Domain Security
  slug: apyguard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apyguard
tags:
- Company
- API Security
- Developer Tools
- Software-as-a-Service
- Cloud
website: https://apyguard.com/
---
