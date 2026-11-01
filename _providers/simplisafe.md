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
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/simplisafe/well-known/simplisafe-bugcrowd-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/simplisafe-bugcrowd-security.txt
- group: commercial
  href: https://artifacts.apis.io/simplisafe/plans/simplisafe-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/simplisafe-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://bugcrowd.com/engagements/simplisafe
- group: auth
  href: https://artifacts.apis.io/simplisafe/well-known/simplisafe-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/simplisafe-security.txt
- group: agent
  href: https://artifacts.apis.io/simplisafe/well-known/simplisafe-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/simplisafe-well-known.yml
- group: other
  href: https://artifacts.apis.io/simplisafe/hosts/simplisafe-hosts.yml
  title: ''
  type: Hosts
  url: hosts/simplisafe-hosts.yml
- group: other
  href: https://artifacts.apis.io/simplisafe/vendors/simplisafe-vendors.yml
  title: ''
  type: Vendors
  url: vendors/simplisafe-vendors.yml
- group: build
  href: https://artifacts.apis.io/simplisafe/packages/simplisafe-packages.yml
  title: ''
  type: SDKs
  url: packages/simplisafe-packages.yml
- group: build
  href: https://artifacts.apis.io/simplisafe/packages/simplisafe-packages.yml
  title: ''
  type: Packages
  url: packages/simplisafe-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://simplisafe.com/legal/terms-sale
- group: operate
  title: ''
  type: Support
  url: https://support.simplisafe.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://simplisafe.com/legal/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://simplisafe.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://support.simplisafe.com/categories/getting-started?lang=en-US
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/simplisafe
- group: auth
  href: https://artifacts.apis.io/simplisafe/security/simplisafe-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/simplisafe-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/simplisafe/security/simplisafe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/simplisafe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://simplisafe.com/
coverage:
  checked: '2026-10-28'
  detail: Developer pages return a JavaScript-rendered 404 page with no machine‑readable spec.
  evidence:
  - status: 404
    url: https://simplisafe.com/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: SimpliSafe provides wireless home security systems that include professionally monitored alarm devices, cameras, and smart home integration. The company offers easy‑to‑install equipment, a mobile app for real‑time alerts, and 24/7 professional monitoring services for residential customers across the United States, focusing on user‑friendly design and reliable protection.
layout: provider
modified: '2026-10-28'
name: SimpliSafe
nav: Providers
network: true
overview: 'SimpliSafe is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Home Security, Wireless, Alarms, and Security Systems.


  SimpliSafe''s developer surface includes support, engineering blog, getting-started guide, and 15 more developer resources.'
plans:
- name: Simplisafe Plans Pricing
  plan_count: 8
  slug: simplisafe-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 22.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 12.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 35.7
    operational_transparency: 15.8
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Simplisafe Domain Security
  slug: simplisafe-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Simplisafe Vulnerability Disclosure
  slug: simplisafe-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: simplisafe
tags:
- Home Security
- Wireless
- Alarms
- Security Systems
website: https://simplisafe.com/
---
