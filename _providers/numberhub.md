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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: REST API for prepaid wallet, SMS verification, number rentals, eSIMs, email OTP and residential proxies.
  name: NumberHub API
  slug: numberhub-api
artifact_total: 3
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/numberhub/refs/heads/main/changelog/numberhub-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/numberhub-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/numberhub/refs/heads/main/conformance/numberhub-conformance.yml
  title: ''
  type: Conformance
  url: conformance/numberhub-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/numberhub/refs/heads/main/llms/numberhub-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/numberhub-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/numberhub/refs/heads/main/hosts/numberhub-hosts.yml
  title: ''
  type: Hosts
  url: hosts/numberhub-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/numberhub/refs/heads/main/vendors/numberhub-vendors.yml
  title: ''
  type: Vendors
  url: vendors/numberhub-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://numberhub.io/terms/
- group: operate
  title: ''
  type: StatusPage
  url: https://numberhub.io/status/
- group: auth
  title: ''
  type: Security
  url: https://numberhub.io/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://numberhub.io/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://numberhub.io/pricing/
- group: start
  title: ''
  type: Login
  url: https://numberhub.io/app/login/
- group: operate
  title: ''
  type: ChangeLog
  url: https://numberhub.io/changelog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/numberhub/refs/heads/main/security/numberhub-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/numberhub-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/numberhub/refs/heads/main/security/numberhub-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/numberhub-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://numberhub.io/
- group: docs
  title: ''
  type: Documentation
  url: https://numberhub.io/api-docs/
created: '2026-09-28'
description: NumberHub provides a REST API for a prepaid USD wallet offering SMS verification numbers, number rentals, travel eSIM data plans, email OTP services, and residential proxy data packages. The platform enables developers to programmatically order numbers, rent eSIMs, send OTPs via SMS or email, and access proxy endpoints, with pricing and catalog updates reflected in real time. It supports idempotent operations via Idempotency-Key and detailed retry semantics for action endpoints.
image: https://numberhub.io/og.jpg
layout: provider
modified: '2026-09-28'
name: NumberHub
nav: Providers
network: true
overview: 'NumberHub publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, SMS Verification, eSIM, and Residential Proxies.


  NumberHub''s developer surface includes changelog, pricing, documentation, and 13 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.3
    operational_transparency: 42.1
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 20.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Numberhub Domain Security
  slug: numberhub-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Numberhub Vulnerability Disclosure
  slug: numberhub-vulnerability-disclosure
  summary_line: disclosure policy published
slug: numberhub
tags:
- Telecommunications
- SMS Verification
- eSIM
- Residential Proxies
website: https://numberhub.io/
---
