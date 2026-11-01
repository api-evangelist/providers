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
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/linkdrip/hosts/linkdrip-hosts.yml
  title: ''
  type: Hosts
  url: hosts/linkdrip-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://app.linkdrip.com/signin
- group: auth
  href: https://artifacts.apis.io/linkdrip/security/linkdrip-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/linkdrip-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.linkdrip.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.linkdrip.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.linkdrip.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.linkdrip.com/apis/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.linkdrip.com/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.linkdrip.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.linkdrip.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linkdrip.com/privacy-policy
coverage:
  checked: '2026-10-27'
  detail: Documentation pages are HTML shells requiring JavaScript to access API details, and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://docs.linkdrip.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: LinkDrip provides a no‑code link engagement platform that lets users create, customize, and track short links with advanced analytics, QR codes, and call‑to‑action overlays. The service supports custom domains, real‑time performance dashboards, and easy integration via a pixel or API, helping marketers and businesses maximize link effectiveness without writing code.
image: https://www.linkdrip.com/images/og-image.png
layout: provider
modified: '2026-10-26'
name: LinkDrip
nav: Providers
network: true
overview: 'LinkDrip is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Link Management, No-Code, Marketing, Analytics, and URL Shortener.


  LinkDrip''s developer surface includes documentation, API reference, getting-started guide, pricing, and 7 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Linkdrip Domain Security
  slug: linkdrip-domain-security
  summary_line: TLSv1.3
slug: linkdrip
tags:
- Link Management
- No-Code
- Marketing
- Analytics
- URL Shortener
website: https://www.linkdrip.com/
---
