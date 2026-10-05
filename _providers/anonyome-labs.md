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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/anonyome-labs/refs/heads/main/plans/anonyome-labs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/anonyome-labs-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anonyome-labs/refs/heads/main/conformance/anonyome-labs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anonyome-labs-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anonyome-labs/refs/heads/main/hosts/anonyome-labs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anonyome-labs-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anonyome-labs/refs/heads/main/vendors/anonyome-labs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anonyome-labs-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anonyome.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anonyome.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://anonyome.com/pricing-plans-with-a-content-carousel/
- group: company
  title: ''
  type: Newsroom
  url: https://anonyome.com/home/media/
- group: other
  title: ''
  type: Leadership
  url: https://anonyome.com/team/jd-mumford/frame-1068-1/
- group: docs
  title: ''
  type: Documentation
  url: https://anonyome.com/resources/guides/
- group: company
  title: ''
  type: Blog
  url: https://anonyome.com/resources/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anonyome-labs/refs/heads/main/security/anonyome-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anonyome-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anonyome.com/
coverage:
  checked: 2026-09-25
  detail: The developer documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 0
    url: https://api.anonyome.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-24'
description: Anonyome Labs provides identity protection solutions through its MySudo suite, offering tools such as password management, VPN, and secure digital identity for individuals and businesses. The platform enables developers to integrate identity protection via APIs and SDKs, supporting privacy, secure communications, and verifiable credentials across multiple industries.
image: https://anonyome.com/wp-content/uploads/2024/04/woman-making-call-mysudo-1-jpg.webp
layout: provider
modified: '2026-09-24'
name: Anonyome Labs
nav: Providers
network: true
overview: 'Anonyome Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity, Privacy, and Security.


  Anonyome Labs'' developer surface includes pricing, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Anonyome Labs Plans Pricing
  plan_count: 19
  slug: anonyome-labs-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 34.0
    catalog_earned_first_party: 12.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 42.9
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Anonyome Labs Domain Security
  slug: anonyome-labs-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: anonyome-labs
tags:
- Company
- Identity
- Privacy
- Security
website: https://anonyome.com/
---
