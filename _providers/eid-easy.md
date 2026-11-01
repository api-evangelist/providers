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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/eid-easy/security/eid-easy-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/eid-easy-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/eid-easy/conformance/eid-easy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/eid-easy-conformance.yml
- group: auth
  href: https://artifacts.apis.io/eid-easy/well-known/eid-easy-id-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/eid-easy-id-security.txt
- group: agent
  href: https://artifacts.apis.io/eid-easy/well-known/eid-easy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/eid-easy-well-known.yml
- group: other
  href: https://artifacts.apis.io/eid-easy/hosts/eid-easy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eid-easy-hosts.yml
- group: other
  href: https://artifacts.apis.io/eid-easy/vendors/eid-easy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/eid-easy-vendors.yml
- group: build
  href: https://artifacts.apis.io/eid-easy/packages/eid-easy-packages.yml
  title: ''
  type: SDKs
  url: packages/eid-easy-packages.yml
- group: build
  href: https://artifacts.apis.io/eid-easy/packages/eid-easy-packages.yml
  title: ''
  type: Packages
  url: packages/eid-easy-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eideasy.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eideasy.com/legal/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.eideasy.com/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.eideasy.com/tag/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.eideasy.com/es/blog/richer-eid-data-idv-aml-onboarding
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eideasy
- group: auth
  href: https://artifacts.apis.io/eid-easy/security/eid-easy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/eid-easy-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/eid-easy/security/eid-easy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eid-easy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eideasy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.eideasy.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.eideasy.com/guide
- group: commercial
  title: ''
  type: Pricing
  url: https://www.eideasy.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.eideasy.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.eideasy.com/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://status.eideasy.com
- group: auth
  href: https://artifacts.apis.io/eid-easy/security/eid-easy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/eid-easy-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/eid-easy/security/eid-easy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eid-easy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eideasy.com/
coverage:
  checked: '2026-10-27'
  detail: Documentation at https://docs.eideasy.com/ is HTML without a machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://docs.eideasy.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: eID Easy provides a cloud‑based platform for electronic signatures, e‑sealing and digital identity verification. Their API lets businesses integrate qualified electronic signatures, batch signing, one‑shot signatures, hash‑based signing, timestamping and seal creation into workflows. It also offers OAuth‑2.0 based identity‑as‑a‑service, supporting European Digital Identity Wallets and national eID systems via OpenID Connect. The service targets fintech, document management, healthcare, HR and compliance use‑cases, offering on‑premise seal options and SDKs for web and mobile integration.
image: https://cdn.prod.website-files.com/67ce33d5a79e102efad685c9/67ef9e8f7816421b03ee6ff7_eideasy_og_1.avif
layout: provider
modified: '2026-10-27'
name: eID Easy
nav: Providers
network: true
overview: 'eID Easy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, eSignature, eSealing, eID, and DigitalIdentity.


  eID Easy''s developer surface includes getting-started guide, documentation, API reference, pricing, engineering blog, support, and 20 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 50.0
    operational_transparency: 31.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Eid Easy Domain Security
  slug: eid-easy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Eid Easy Vulnerability Disclosure
  slug: eid-easy-vulnerability-disclosure
  summary_line: no policy recorded
slug: eid-easy
tags:
- Company
- eSignature
- eSealing
- eID
- DigitalIdentity
website: https://eideasy.com/
---
