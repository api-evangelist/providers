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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Fastmail email service API documented at the developer portal.
  name: Fastmail API
  slug: fastmail-api
artifact_total: 5
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/fastmail/refs/heads/main/rate-limits/fastmail-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fastmail-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/fastmail/refs/heads/main/plans/fastmail-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fastmail-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fastmail/refs/heads/main/conformance/fastmail-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fastmail-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fastmail/refs/heads/main/well-known/fastmail-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fastmail-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fastmail/refs/heads/main/well-known/fastmail-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fastmail-app-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fastmail/refs/heads/main/well-known/fastmail-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fastmail-api-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fastmail/refs/heads/main/well-known/fastmail-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fastmail-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fastmail/refs/heads/main/hosts/fastmail-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fastmail-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fastmail/refs/heads/main/vendors/fastmail-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fastmail-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/fastmail/refs/heads/main/packages/fastmail-packages.yml
  title: ''
  type: SDKs
  url: packages/fastmail-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/fastmail/refs/heads/main/packages/fastmail-packages.yml
  title: ''
  type: Packages
  url: packages/fastmail-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.fastmail.com/features/security/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.fastmail.com/blog/why-replication-took-time-to-setup/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fastmail
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fastmail/refs/heads/main/security/fastmail-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/fastmail-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fastmail/refs/heads/main/security/fastmail-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fastmail-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fastmail.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.fastmail.com/dev/
- group: docs
  title: ''
  type: Documentation
  url: https://www.fastmail.com/dev/
- group: docs
  title: ''
  type: APIReference
  url: https://www.fastmail.com/dev/
- group: operate
  title: ''
  type: Support
  url: https://fastmail.help/
- group: company
  title: ''
  type: Blog
  url: https://www.fastmail.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fastmail.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fastmail.com/policies/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fastmail.com/policies/privacy/
coverage:
  checked: '2026-10-14'
  detail: Developer portal returns HTML pages without a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://api.fastmail.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: Fastmail provides secure, private email and calendar services for individuals and businesses. Founded in 1999, Fastmail emphasizes data protection, user privacy, and a feature‑rich experience with powerful filtering, custom domains, and cross‑platform synchronization. Their service includes robust spam protection, two‑factor authentication, and a focus on delivering a fast, reliable email platform without advertising or data mining. Fastmail also offers business plans with administrative controls, migration tools, and dedicated support, catering to professionals who need secure communication and reliable uptime.
image: https://www.fastmail.com/assets/images/opengraph/Fastmail-OG.png
layout: provider
modified: '2026-10-13'
name: Fastmail
nav: Providers
network: true
overview: 'Fastmail is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Email, Privacy, Security, Business, and Cloud.


  Fastmail''s developer surface includes getting-started guide, documentation, API reference, support, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Fastmail Plans Pricing
  plan_count: 3
  slug: fastmail-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Fastmail Rate Limits
  slug: fastmail-rate-limits
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 52.0
    catalog_earned_first_party: 20.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 57.1
    operational_transparency: 36.8
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
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Fastmail Domain Security
  slug: fastmail-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fastmail Vulnerability Disclosure
  slug: fastmail-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: fastmail
tags:
- Email
- Privacy
- Security
- Business
- Cloud
website: https://www.fastmail.com
---
