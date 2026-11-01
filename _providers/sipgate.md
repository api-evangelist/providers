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
  score: 12.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/sipgate/plans/sipgate-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sipgate-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/sipgate/security/sipgate-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/sipgate-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sipgate/scopes/sipgate-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/sipgate-scopes.yml
- group: agent
  href: https://artifacts.apis.io/sipgate/llms/sipgate-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sipgate-llms.txt
- group: other
  href: https://artifacts.apis.io/sipgate/hosts/sipgate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sipgate-hosts.yml
- group: other
  href: https://artifacts.apis.io/sipgate/vendors/sipgate-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sipgate-vendors.yml
- group: build
  href: https://artifacts.apis.io/sipgate/packages/sipgate-packages.yml
  title: ''
  type: SDKs
  url: packages/sipgate-packages.yml
- group: build
  href: https://artifacts.apis.io/sipgate/packages/sipgate-packages.yml
  title: ''
  type: Packages
  url: packages/sipgate-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.sipgate.io/webhooks
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sipgate
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.sipgate.com
- group: auth
  href: https://artifacts.apis.io/sipgate/security/sipgate-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sipgate-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sipgate/security/sipgate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sipgate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sipgate.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.sipgate.io/restapi
- group: docs
  title: ''
  type: APIReference
  url: https://www.sipgate.io/restapi
- group: start
  title: ''
  type: GettingStarted
  url: https://www.sipgate.io/fuer-entwickler
- group: operate
  title: ''
  type: Support
  url: https://www.sipgate.io/support
- group: company
  title: ''
  type: Blog
  url: https://www.sipgate.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sipgate.io/preise
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sipgate.io/datenschutz
coverage:
  checked: '2026-10-26'
  detail: Swagger UI page at https://api.sipgate.com/v2/doc returns HTML without a downloadable OpenAPI spec.
  evidence:
  - status: 200
    url: https://api.sipgate.com/v2/doc
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Sipgate provides cloud telephony services, offering voice, SMS, fax, and real‑time communication APIs for developers to integrate calling, messaging, and fax capabilities into software projects. Their platform includes a REST API, Push API, webhooks, and extensive documentation, enabling businesses to build communication features such as call handling, SMS notifications, and fax transmission programmatically.
image: https://www.sipgate.io/wp-content/uploads/io_stage-Deutsch-1.png
layout: provider
modified: '2026-10-26'
name: sipgate
nav: Providers
network: true
overview: 'sipgate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telephony, Cloud, API, and Communications.


  sipgate''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Sipgate Plans Pricing
  plan_count: 1
  slug: sipgate-plans-pricing
random_paper: 5
scopes:
- name: Sipgate Scopes
  scope_count: 5
  slug: sipgate-scopes
  summary_line: 5 scopes
score:
  band: thin
  composite: 28.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 48.2
    operational_transparency: 23.7
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sipgate Domain Security
  slug: sipgate-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Sipgate Vulnerability Disclosure
  slug: sipgate-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sipgate
tags:
- Company
- Telephony
- Cloud
- API
- Communications
website: https://www.sipgate.io/
---
