---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://iplocate.io/api/
  baseurl_source: declared
  description: IPLocate provides IP geolocation, privacy detection, and threat intelligence.
  name: IPLocate API
  slug: iplocate-api
artifact_total: 5
common:
- group: operate
  href: https://artifacts.apis.io/iplocate/rate-limits/iplocate-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/iplocate-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/iplocate/plans/iplocate-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/iplocate-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/iplocate/authentication/iplocate-authentication.yml
  title: ''
  type: Authentication
  url: authentication/iplocate-authentication.yml
- group: design
  href: https://artifacts.apis.io/iplocate/conformance/iplocate-conformance.yml
  title: ''
  type: Conformance
  url: conformance/iplocate-conformance.yml
- group: other
  href: https://artifacts.apis.io/iplocate/overlays/iplocate-openapi-overlay.yml
  title: ''
  type: Overlay
  url: overlays/iplocate-openapi-overlay.yml
- group: agent
  href: https://artifacts.apis.io/iplocate/llms/iplocate-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/iplocate-llms.txt
- group: other
  href: https://artifacts.apis.io/iplocate/hosts/iplocate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/iplocate-hosts.yml
- group: other
  href: https://artifacts.apis.io/iplocate/vendors/iplocate-vendors.yml
  title: ''
  type: Vendors
  url: vendors/iplocate-vendors.yml
- group: build
  href: https://artifacts.apis.io/iplocate/packages/iplocate-packages.yml
  title: ''
  type: SDKs
  url: packages/iplocate-packages.yml
- group: build
  href: https://artifacts.apis.io/iplocate/packages/iplocate-packages.yml
  title: ''
  type: Packages
  url: packages/iplocate-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.iplocate.io/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iplocate.io/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://www.iplocate.io/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/iplocate
- group: auth
  href: https://artifacts.apis.io/iplocate/security/iplocate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iplocate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.iplocate.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.iplocate.io/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.iplocate.io/openapi.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.iplocate.io/docs/quick-start
- group: commercial
  title: ''
  type: Pricing
  url: https://www.iplocate.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.iplocate.io/blog
- group: operate
  title: ''
  type: Support
  url: https://www.iplocate.io/contact
created: '2026-10-26'
description: IPLocate (formerly GeoIPs) provides a free and paid IP geolocation, privacy detection, and threat intelligence API. Developers can query real‑time IP address location, ASN, company, and risk data, with downloadable databases for offline use. The service emphasizes accuracy, speed, and comprehensive data fields for security, personalization, and fraud prevention use cases.
image: https://static.iplocate.io/assets/og/og-homepage-c7c4a668b10c83554e8df85971983a0d295c39d39a3578d5a63f85cc67cc2da0.jpg
layout: provider
modified: '2026-10-26'
name: IPLocate (formerly GeoIPs)
nav: Providers
network: true
overview: 'IPLocate (formerly GeoIPs) is listed with 1 API on the [APIs.io](https://apis.io/) network: IPLocate API. Tagged areas include Company, IP Geolocation, Threat Detection, Privacy, and API.


  IPLocate (formerly GeoIPs)''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, support, and 15 more developer resources.'
plans:
- name: Iplocate Plans Pricing
  plan_count: 2
  slug: iplocate-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Iplocate Rate Limits
  slug: iplocate-rate-limits
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 53.0
    catalog_earned_first_party: 16.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 36.0
    developer_ergonomics: 54.8
    discoverability: 66.1
    operational_transparency: 26.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Iplocate Authentication
  slug: iplocate-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Iplocate Domain Security
  slug: iplocate-domain-security
  summary_line: TLSv1.3 · DMARC
slug: iplocate
tags:
- Company
- IP Geolocation
- Threat Detection
- Privacy
- API
- Data
website: https://www.iplocate.io/
---
