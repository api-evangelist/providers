---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/evy/security/evy-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/evy-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/evy/well-known/evy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/evy-well-known.yml
- group: other
  href: https://artifacts.apis.io/evy/hosts/evy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/evy-hosts.yml
- group: other
  href: https://artifacts.apis.io/evy/vendors/evy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/evy-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.evy.eu/en/legal-notice
- group: operate
  title: ''
  type: StatusPage
  url: https://status.evy.eu/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.evy.eu/en/privacy-policy
- group: auth
  href: https://artifacts.apis.io/evy/security/evy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/evy-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/evy/security/evy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/evy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://evy.eu
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.evy.eu/mcp
  - status: 200
    url: https://evy.eu
  reason: partner-login
  state: gated
created: '2026-10-23'
description: Evy provides product protection solutions. Unlock new revenue streams and captivate your customers with Evy by your side.
layout: provider
modified: '2026-10-23'
name: Evy
nav: Providers
network: true
overview: Evy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Product Protection, FinTech, SaaS, Security, and Insurance.
random_paper: 4
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 22.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Evy Domain Security
  slug: evy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Evy Vulnerability Disclosure
  slug: evy-vulnerability-disclosure
  summary_line: no policy recorded
slug: evy
tags:
- Product Protection
- FinTech
- SaaS
- Security
- Insurance
website: https://evy.eu
---
