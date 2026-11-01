---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 17.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: CallerKit provides a Caller ID API and global phone lookup service as described on the documentation page.
  name: CallerKit API
  slug: callerkit-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/caller-kit-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/caller-kit-com/well-known/caller-kit-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/caller-kit-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/caller-kit-com/hosts/caller-kit-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caller-kit-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/caller-kit-com/vendors/caller-kit-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caller-kit-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/callerkit01
- group: auth
  href: https://artifacts.apis.io/caller-kit-com/security/caller-kit-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caller-kit-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caller-kit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://caller-kit.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://caller-kit.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://caller-kit.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://caller-kit.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://caller-kit.com/page/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://caller-kit.com/page/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://caller-kit.com/contact-us
coverage:
  checked: '2026-10-30'
  detail: Documentation pages are HTML without a published OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://caller-kit.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: CallerKit provides a Caller ID API and global phone lookup service, offering access to a database of over 3 billion phone numbers with verified contact names and aliases. The platform supports real‑time search by number, name, or email, bulk verification, and enriched data delivery for developers, CRMs, verification systems, and other applications. Features include fast, scalable lookups, rate‑limited API access, detailed analytics, and secure encrypted data handling.
image: https://caller-kit.com/assets/imgs/og-image.png
layout: provider
modified: '2026-10-30'
name: caller-kit-com
nav: Providers
network: true
overview: 'caller-kit-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API, PhoneLookup, CallerID, and DataEnrichment.


  caller-kit-com''s developer surface includes documentation, API reference, pricing, and 11 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 57.1
    operational_transparency: 5.3
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
  name: Caller Kit Com Domain Security
  slug: caller-kit-com-domain-security
  summary_line: TLSv1.3
slug: caller-kit-com
tags:
- Company
- API
- PhoneLookup
- CallerID
- DataEnrichment
website: https://caller-kit.com/
---
