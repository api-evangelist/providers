---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: operate
  href: https://artifacts.apis.io/air-platforms/changelog/air-platforms-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/air-platforms-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.airplatforms.com/
- group: design
  href: https://artifacts.apis.io/air-platforms/conformance/air-platforms-conformance.yml
  title: ''
  type: Conformance
  url: conformance/air-platforms-conformance.yml
- group: other
  href: https://artifacts.apis.io/air-platforms/hosts/air-platforms-hosts.yml
  title: ''
  type: Hosts
  url: hosts/air-platforms-hosts.yml
- group: other
  href: https://artifacts.apis.io/air-platforms/vendors/air-platforms-vendors.yml
  title: ''
  type: Vendors
  url: vendors/air-platforms-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.airplatforms.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.airplatforms.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.airplatforms.com/use-cases/pricing-valuation
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.airplatforms.com/release-notes
- group: auth
  href: https://artifacts.apis.io/air-platforms/security/air-platforms-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/air-platforms-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/air-platforms/security/air-platforms-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/air-platforms-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.airplatforms.com/
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI or other machine-readable contract was found on the provider's hosts.
  evidence:
  - status: 200
    url: https://www.airplatforms.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: AIR Platforms provides AI-native credit intelligence solutions, offering real-time risk monitoring, exposure analysis, and AI-driven credit scoring for financial institutions. Their platform delivers explainable intelligence across companies, helping banks, asset managers, and hedge funds make informed credit decisions with daily scoring and rapid deployment.
image: https://www.airplatforms.com/og-image.png
layout: provider
modified: '2026-10-29'
name: AIR Platforms
nav: Providers
network: true
overview: 'AIR Platforms is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Credit, Finance, and Risk.


  AIR Platforms'' developer surface includes changelog, pricing, and 10 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Air Platforms Domain Security
  slug: air-platforms-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Air Platforms Trust Center
  slug: air-platforms-trust-center
  summary_line: SOC 2
slug: air-platforms
tags:
- Company
- AI
- Credit
- Finance
- Risk
website: https://www.airplatforms.com/
---
