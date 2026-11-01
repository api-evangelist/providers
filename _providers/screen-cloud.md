---
agent_readiness:
  band: agent-aware
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for managing digital signage content and devices.
  name: ScreenCloud API
  slug: screencloud-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/screen-cloud/plans/screen-cloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/screen-cloud-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://screencloud.com/security
- group: design
  href: https://artifacts.apis.io/screen-cloud/conformance/screen-cloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/screen-cloud-conformance.yml
- group: agent
  href: https://artifacts.apis.io/screen-cloud/llms/screen-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/screen-cloud-llms.txt
- group: auth
  href: https://artifacts.apis.io/screen-cloud/well-known/screen-cloud-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/screen-cloud-help-security.txt
- group: agent
  href: https://artifacts.apis.io/screen-cloud/well-known/screen-cloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/screen-cloud-well-known.yml
- group: other
  href: https://artifacts.apis.io/screen-cloud/hosts/screen-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/screen-cloud-hosts.yml
- group: other
  href: https://artifacts.apis.io/screen-cloud/vendors/screen-cloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/screen-cloud-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://screencloud.com/apps/webhooks
- group: auth
  title: ''
  type: Security
  url: https://screencloud.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://screencloud.com/apps/news
- group: auth
  href: https://artifacts.apis.io/screen-cloud/security/screen-cloud-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/screen-cloud-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/screen-cloud/security/screen-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/screen-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://screen.cloud
- group: start
  title: ''
  type: DeveloperPortal
  url: https://screencloud.com/
- group: docs
  title: ''
  type: Documentation
  url: https://screencloud.com/resources?content_types=articles
- group: start
  title: ''
  type: GettingStarted
  url: https://screencloud.com/get-started
- group: operate
  title: ''
  type: Support
  url: https://screencloud.com/support
- group: company
  title: ''
  type: Blog
  url: https://screencloud.com/resources?content_types=articles
- group: commercial
  title: ''
  type: Pricing
  url: https://screencloud.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://screencloud.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://screencloud.com/privacy
coverage:
  checked: '2026-10-28'
  detail: Developer portal requires JavaScript rendering and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://developer.screencloud.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: ScreenCloud provides a cloud‑based digital signage platform that lets users create, schedule, and display content across any screen or TV. The service supports a wide range of hardware, offers remote device management, integrates with popular apps, and includes analytics dashboards. It targets businesses of all sizes, from retail and education to healthcare and logistics, enabling centralized control of visual communications.
image: https://screencloud.com/img/meta/revamp/home.jpg
layout: provider
modified: '2026-10-28'
name: ScreenCloud
nav: Providers
network: true
overview: 'ScreenCloud is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DigitalSignage, SaaS, Cloud, and Marketing.


  ScreenCloud''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Screen Cloud Plans Pricing
  plan_count: 3
  slug: screen-cloud-plans-pricing
random_paper: 20
score:
  band: thin
  composite: 35.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 58.9
    operational_transparency: 18.4
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Screen Cloud Domain Security
  slug: screen-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Screen Cloud Trust Center
  slug: screen-cloud-trust-center
  summary_line: SOC 2, GDPR
slug: screen-cloud
tags:
- Company
- DigitalSignage
- SaaS
- Cloud
- Marketing
website: https://screen.cloud
---
