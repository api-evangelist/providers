---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/digilocker/hosts/digilocker-hosts.yml
  title: ''
  type: Hosts
  url: hosts/digilocker-hosts.yml
- group: other
  href: https://artifacts.apis.io/digilocker/vendors/digilocker-vendors.yml
  title: ''
  type: Vendors
  url: vendors/digilocker-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.digilocker.gov.in:443/web/login
- group: auth
  href: https://artifacts.apis.io/digilocker/security/digilocker-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/digilocker-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.digilocker.gov.in/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.digilocker.gov.in/web/partners/introductions
- group: start
  title: ''
  type: GettingStarted
  url: https://www.digilocker.gov.in/web/signup
- group: operate
  title: ''
  type: Support
  url: https://www.digilocker.gov.in/web/about/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.digilocker.gov.in/web/about/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.digilocker.gov.in/web/about/digilocker-policy
coverage:
  checked: '2026-10-28'
  detail: The provider's documentation site returns 403 for attempted OpenAPI spec URLs, offering no machine‑readable contract.
  evidence:
  - status: 403
    url: https://www.digilocker.gov.in/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: DigiLocker is a government-backed digital locker service in India that enables citizens to store, access, share, and verify their digital documents securely online. It provides a platform for uploading identity documents, educational certificates, and other official records, allowing seamless verification by authorized agencies and easy sharing with service providers. The service aims to reduce paperwork, enhance security, and promote digital inclusion across the country.
image: https://cdn.digilocker.gov.in/digilocker-landing-page/assets/img/meta/social-share-og.jpg
layout: provider
modified: '2026-10-28'
name: DigiLocker
nav: Providers
network: true
overview: 'DigiLocker is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  DigiLocker''s developer surface includes getting-started guide, support, and 8 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 39.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/digilocker/digilocker-2026-11-03T130705.png
security:
- kind: domain-security
  name: Digilocker Domain Security
  slug: digilocker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: digilocker
tags:
- Company
website: https://www.digilocker.gov.in/
---
