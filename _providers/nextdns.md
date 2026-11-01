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
  score: 13.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Public API for managing NextDNS profiles, analytics, logs, and settings.
  name: NextDNS API
  slug: nextdns-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/nextdns/well-known/nextdns-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nextdns-well-known.yml
- group: other
  href: https://artifacts.apis.io/nextdns/hosts/nextdns-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nextdns-hosts.yml
- group: other
  href: https://artifacts.apis.io/nextdns/vendors/nextdns-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nextdns-vendors.yml
- group: build
  href: https://artifacts.apis.io/nextdns/packages/nextdns-packages.yml
  title: ''
  type: SDKs
  url: packages/nextdns-packages.yml
- group: build
  href: https://artifacts.apis.io/nextdns/packages/nextdns-packages.yml
  title: ''
  type: Packages
  url: packages/nextdns-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nextdns
- group: auth
  href: https://artifacts.apis.io/nextdns/security/nextdns-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nextdns-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nextdns.io/
- group: docs
  title: ''
  type: Documentation
  url: https://nextdns.github.io/api/
- group: docs
  title: ''
  type: APIReference
  url: https://nextdns.github.io/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://nextdns.io/pricing
- group: operate
  title: ''
  type: Support
  url: https://help.nextdns.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nextdns.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.google.com/document/d/1gG2nq9fQ5lOyTlWXo5GIm7kEpcgZxFc22w11qvkLZ0o/preview
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract was found; standard spec URLs returned 404 or HTML shells.
  evidence:
  - status: 404
    url: https://api.nextdns.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: NextDNS provides a DNS filtering service that protects users from security threats, blocks ads and trackers, and offers parental controls. It offers a public API for managing profiles, analytics, logs, and settings, enabling integration with custom applications and automation.
image: https://nextdns.io/static/og-image.jpg
layout: provider
modified: '2026-10-28'
name: NextDNS
nav: Providers
network: true
overview: 'NextDNS is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include DNS, Security, Privacy, Filtering, and Analytics.


  NextDNS''s developer surface includes documentation, API reference, pricing, support, and 10 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    mcp: derived
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
  name: Nextdns Domain Security
  slug: nextdns-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: nextdns
tags:
- DNS
- Security
- Privacy
- Filtering
- Analytics
website: https://nextdns.io/
---
