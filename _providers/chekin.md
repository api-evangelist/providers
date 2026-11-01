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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/chekin/llms/chekin-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chekin-llms.txt
- group: agent
  href: https://artifacts.apis.io/chekin/well-known/chekin-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chekin-well-known.yml
- group: other
  href: https://artifacts.apis.io/chekin/hosts/chekin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chekin-hosts.yml
- group: other
  href: https://artifacts.apis.io/chekin/vendors/chekin-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chekin-vendors.yml
- group: build
  title: ''
  type: SDKs
  url: https://chekin.com/sdk/
- group: start
  title: ''
  type: Login
  url: https://chekin.com/onboarding/login/
- group: auth
  href: https://artifacts.apis.io/chekin/security/chekin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chekin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chekin.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://chekin.com/en/sdk/
- group: docs
  title: ''
  type: Documentation
  url: https://chekin.com/en/sdk/
- group: docs
  title: ''
  type: APIReference
  url: https://chekin.com/en/sdk/
- group: start
  title: ''
  type: GettingStarted
  url: https://chekin.com/en/pricing/
- group: operate
  title: ''
  type: Support
  url: https://support.chekin.com/en
- group: company
  title: ''
  type: Blog
  url: https://chekin.com/en/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://chekin.com/en/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chekin.com/en/terms/
coverage:
  checked: '2026-10-27'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's documented hosts.
  evidence:
  - status: 404
    url: https://docs.chekin.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Chekin provides a comprehensive online check‑in platform for hospitality businesses, automating guest registration, identity verification, e‑invoicing, tax compliance and remote key access. Their solution includes a developer SDK and API that enable property managers to integrate check‑in, compliance reporting and payment processing into their own systems, supporting multi‑language and multi‑country regulations.
image: https://chekin.com/wp-content/uploads/2021/02/social-e1619167787636.jpg
layout: provider
modified: '2026-10-27'
name: Chekin
nav: Providers
network: true
overview: 'Chekin is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Hospitality, Check-in, Compliance, API, and SDK.


  Chekin''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 10 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chekin Domain Security
  slug: chekin-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chekin
tags:
- Hospitality
- Check-in
- Compliance
- API
- SDK
website: https://chekin.com/
---
