---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/icite/plans/icite-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/icite-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/icite/llms/icite-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/icite-llms.txt
- group: agent
  href: https://artifacts.apis.io/icite/well-known/icite-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/icite-well-known.yml
- group: other
  href: https://artifacts.apis.io/icite/hosts/icite-hosts.yml
  title: ''
  type: Hosts
  url: hosts/icite-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/icite
- group: auth
  href: https://artifacts.apis.io/icite/security/icite-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/icite-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://icite.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.icite.io/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.icite.io/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.icite.io/terms-of-service
coverage:
  checked: '2026-10-29'
  detail: No public API documentation or machine-readable contract was found for Icite.
  evidence:
  - status: 404
    url: https://api.icite.io/
  - status: 200
    url: https://app.icite.io/
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Icite provides an Identity Intelligence Platform for Security Operations, enabling correlation of identity, access, and activity across all connected systems. It helps detect threats that traditional EDR, cloud, and SIEM solutions miss, offering comprehensive ITDR capabilities for enterprises seeking unified security visibility and response.
image: https://framerusercontent.com/images/Vcd2rUSkEM6DUcfByGvfaN1vYXk.png
layout: provider
modified: '2026-10-29'
name: Icite
nav: Providers
network: true
overview: 'Icite is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Identity, ITDR, Platform, and Software-as-a-Service.


  Icite''s developer surface includes pricing and 9 more developer resources.'
plans:
- name: Icite Plans Pricing
  plan_count: 2
  slug: icite-plans-pricing
random_paper: 22
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/icite/icite-2026-11-03T133611.png
security:
- kind: domain-security
  name: Icite Domain Security
  slug: icite-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: icite
tags:
- Security
- Identity
- ITDR
- Platform
- Software-as-a-Service
- Company
website: https://icite.io/
---
