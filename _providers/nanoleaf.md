---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/nanoleaf/llms/nanoleaf-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nanoleaf-llms.txt
- group: agent
  href: https://artifacts.apis.io/nanoleaf/well-known/nanoleaf-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nanoleaf-well-known.yml
- group: other
  href: https://artifacts.apis.io/nanoleaf/hosts/nanoleaf-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nanoleaf-hosts.yml
- group: other
  href: https://artifacts.apis.io/nanoleaf/vendors/nanoleaf-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nanoleaf-vendors.yml
- group: build
  href: https://artifacts.apis.io/nanoleaf/packages/nanoleaf-packages.yml
  title: ''
  type: SDKs
  url: packages/nanoleaf-packages.yml
- group: build
  href: https://artifacts.apis.io/nanoleaf/packages/nanoleaf-packages.yml
  title: ''
  type: Packages
  url: packages/nanoleaf-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nanoleaf.me/en-us/policies/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://support.nanoleaf.me/hc/en-us/community/topics/42454879266836-Developer-Forum
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nanoleaf.me/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nanoleaf.me/en-us/policies/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://nanoleaf.me/en-us/pages/newsroom
- group: docs
  title: ''
  type: Documentation
  url: https://developers.nanoleaf.me/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nanoleaf
- group: auth
  href: https://artifacts.apis.io/nanoleaf/security/nanoleaf-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nanoleaf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nanoleaf.me/
coverage:
  checked: '2026-10-28'
  detail: Provider documentation is limited to support pages without a machine‑readable API specification.
  evidence:
  - status: 200
    url: https://nanoleaf.me/api/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Nanoleaf designs and manufactures smart lighting products, including LED light panels, light strips, and interactive lighting systems for homes and commercial spaces. Their platform integrates with major smart home ecosystems, offering AI‑powered experiences, wellness features, and developer APIs for controlling lighting, retrieving device status, and building custom integrations.
image: https://cdn.shopify.com/s/files/1/0712/9114/2378/files/All_products_Canvas.LP.Hex_Entertainment_room2_4000x2250_34324b88-17a6-4f73-b25c-c24315df95eb.jpg?v=1793172217
layout: provider
modified: '2026-10-28'
name: Nanoleaf
nav: Providers
network: true
overview: 'Nanoleaf is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Smart Lighting, IoT, Home Automation, and AI.


  Nanoleaf''s developer surface includes support, documentation, and 13 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 50.0
    operational_transparency: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Nanoleaf Domain Security
  slug: nanoleaf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nanoleaf
tags:
- Company
- Smart Lighting
- IoT
- Home Automation
- AI
website: https://nanoleaf.me/
---
