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
api_count: 1
apis:
- description: Telehealth platform offering video calls for clinicians and patients.
  name: Doxy.me API
  slug: doxy-me-api
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/doxy-me/well-known/doxy-me-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/doxy-me-status-security.txt
- group: operate
  href: https://artifacts.apis.io/doxy-me/changelog/doxy-me-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/doxy-me-changelog.yml
- group: design
  href: https://artifacts.apis.io/doxy-me/conformance/doxy-me-conformance.yml
  title: ''
  type: Conformance
  url: conformance/doxy-me-conformance.yml
- group: agent
  href: https://artifacts.apis.io/doxy-me/llms/doxy-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/doxy-me-llms.txt
- group: auth
  href: https://artifacts.apis.io/doxy-me/well-known/doxy-me-helpcenter-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/doxy-me-helpcenter-security.txt
- group: agent
  href: https://artifacts.apis.io/doxy-me/well-known/doxy-me-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/doxy-me-well-known.yml
- group: other
  href: https://artifacts.apis.io/doxy-me/hosts/doxy-me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/doxy-me-hosts.yml
- group: other
  href: https://artifacts.apis.io/doxy-me/vendors/doxy-me-vendors.yml
  title: ''
  type: Vendors
  url: vendors/doxy-me-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://doxy.me/site/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://doxy.me/site/about/contact/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.doxy.me/
- group: auth
  title: ''
  type: Security
  url: https://doxy.me/site/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://doxy.me/site/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://doxy.me/site/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://doxy.me/site/media/doxy-me-pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://doxy.me/site/product/releases
- group: company
  title: ''
  type: Blog
  url: https://doxy.me/site/media/blog
- group: docs
  title: ''
  type: Documentation
  url: https://developer.doxy.me/
- group: auth
  href: https://artifacts.apis.io/doxy-me/security/doxy-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doxy-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doxy.me/
coverage:
  checked: '2026-10-27'
  detail: Doxy.me provides a telehealth platform but no OpenAPI or other machine‑readable API spec is publicly available.
  evidence:
  - status: 200
    url: https://doxy.me/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Doxy.me provides a simple, free, and secure telehealth platform that enables healthcare providers to conduct video visits with patients without the need for downloads or installations. The service supports up to one million providers worldwide, offering HIPAA‑compliant video, screen sharing, and chat features. Users can sign up in under a minute, and the platform emphasizes privacy, ease of use, and integration with existing practice workflows.
image: https://framerusercontent.com/assets/MU291SUIPq1s82zgml4MsL3OKc.jpg
layout: provider
modified: '2026-10-27'
name: Doxy.me
nav: Providers
network: true
overview: 'Doxy.me is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telehealth, Video, HIPAA, and Free.


  Doxy.me''s developer surface includes changelog, support, pricing, engineering blog, documentation, and 15 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 23.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 58.9
    operational_transparency: 42.1
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
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Doxy Me Domain Security
  slug: doxy-me-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: doxy-me
tags:
- Company
- Telehealth
- Video
- HIPAA
- Free
- Secure
website: https://doxy.me/
---
