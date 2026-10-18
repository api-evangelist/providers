---
agent_readiness:
  band: human-only
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 3
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/clearyst/refs/heads/main/rate-limits/clearyst-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/clearyst-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/clearyst/refs/heads/main/plans/clearyst-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clearyst-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clearyst/refs/heads/main/conformance/clearyst-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clearyst-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clearyst/refs/heads/main/llms/clearyst-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clearyst-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clearyst/refs/heads/main/well-known/clearyst-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clearyst-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clearyst/refs/heads/main/well-known/clearyst-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clearyst-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clearyst/refs/heads/main/hosts/clearyst-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clearyst-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clearyst/refs/heads/main/vendors/clearyst-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clearyst-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clearyst.com/legal/terms/
- group: operate
  title: ''
  type: Support
  url: https://help.clearyst.com/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clearyst.com/legal/privacy/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.clearyst.com/en/articles/15889727-getting-started-with-clearyst-benchmark
- group: docs
  title: ''
  type: Documentation
  url: https://help.clearyst.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clearyst/refs/heads/main/security/clearyst-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clearyst-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clearyst.com/
coverage:
  checked: '2026-10-09'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: 404
    url: https://api.clearyst.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Clearyst provides a sustainability operating system for mid‑market and enterprise organizations, offering tools for EPR compliance, GHG reporting, supply‑chain sustainability, workforce engagement, and other ESG initiatives. Their platform integrates data‑driven solutions to help companies meet regulatory requirements and sustainability goals across multiple jurisdictions.
image: https://www.clearyst.com/images/og-default.jpg
layout: provider
modified: '2026-10-08'
name: Clearyst
nav: Providers
network: true
overview: 'Clearyst is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Sustainability, ESG, Platform, Software, and Enterprise.


  Clearyst''s developer surface includes support, getting-started guide, documentation, and 12 more developer resources.'
plans:
- name: Clearyst Plans Pricing
  plan_count: 2
  slug: clearyst-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Clearyst Rate Limits
  slug: clearyst-rate-limits
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 43.0
    catalog_earned_first_party: 16.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 55.4
    operational_transparency: 21.1
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clearyst Domain Security
  slug: clearyst-domain-security
  summary_line: TLSv1.3 · DMARC
slug: clearyst
tags:
- Sustainability
- ESG
- Platform
- Software
- Enterprise
website: https://www.clearyst.com/
---
