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
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.flexibits.com/
- group: other
  href: https://artifacts.apis.io/flexibits/hosts/flexibits-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flexibits-hosts.yml
- group: other
  href: https://artifacts.apis.io/flexibits/vendors/flexibits-vendors.yml
  title: ''
  type: Vendors
  url: vendors/flexibits-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flexibits
- group: auth
  href: https://artifacts.apis.io/flexibits/security/flexibits-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/flexibits-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/flexibits/security/flexibits-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flexibits-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flexibits.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://flexibits.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://flexibits.com/blog
- group: operate
  title: ''
  type: Support
  url: https://flexibits.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flexibits.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flexibits.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.flexibits.com
coverage:
  checked: '2026-10-27'
  detail: No OpenAPI, AsyncAPI, or GraphQL spec is publicly accessible; the only discovered GraphQL endpoint requires authentication.
  evidence:
  - status: 404
    url: https://api.flexibits.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Fantastical, developed by Flexibits, offers powerful calendar and productivity applications across macOS, iOS, Windows, and Googlebook platforms. Their flagship apps, Fantastical and Cardhop, focus on intuitive scheduling, contact management, and seamless integration with various services, helping users stay organized and efficient. The company emphasizes flexibility, user-friendly design, and continuous feature enhancements to improve personal and professional productivity.
image: https://flexibits.com/img/flexibits/flexibits-loop-512x512.png
layout: provider
modified: '2026-10-27'
name: Fantastical (Flexibits)
nav: Providers
network: true
overview: 'Fantastical (Flexibits) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Calendar, Productivity, macOS, and iOS.


  Fantastical (Flexibits)''s developer surface includes pricing, engineering blog, support, and 10 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Flexibits Domain Security
  slug: flexibits-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Flexibits Trust Center
  slug: flexibits-trust-center
  summary_line: SOC 2
slug: flexibits
tags:
- Company
- Calendar
- Productivity
- macOS
- iOS
website: https://flexibits.com/
---
