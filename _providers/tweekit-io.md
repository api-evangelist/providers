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
  score: 8.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/tweekit-io/plans/tweekit-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tweekit-io-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/tweekit-io/authentication/tweekit-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tweekit-io-authentication.yml
- group: other
  href: https://artifacts.apis.io/tweekit-io/hosts/tweekit-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tweekit-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/tweekit-io/vendors/tweekit-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tweekit-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/tweekit-io/packages/tweekit-io-packages.yml
  title: ''
  type: SDKs
  url: packages/tweekit-io-packages.yml
- group: build
  href: https://artifacts.apis.io/tweekit-io/packages/tweekit-io-packages.yml
  title: ''
  type: Packages
  url: packages/tweekit-io-packages.yml
- group: auth
  href: https://artifacts.apis.io/tweekit-io/security/tweekit-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tweekit-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tweekit.io/
- group: docs
  title: ''
  type: Documentation
  url: https://tweekit.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://tweekit.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tweekit.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tweekit.io/privacy
coverage:
  checked: '2026-10-30'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://tweekit.io/docs/rest-api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: TweekIT provides a universal file translation service for AI workflows, offering fast, stateless APIs that convert any media type into optimized assets. The platform includes REST and Widget APIs, detailed documentation, pricing plans, and a managed MCP server for seamless integration into AI pipelines.
image: https://tweekit.io/images/seo_logo.png
layout: provider
modified: '2026-10-30'
name: tweekit-io
nav: Providers
network: true
overview: 'tweekit-io is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, File-Conversion, API, and Media.


  tweekit-io''s developer surface includes authentication, documentation, pricing, and 9 more developer resources.'
plans:
- name: Tweekit Io Plans Pricing
  plan_count: 5
  slug: tweekit-io-plans-pricing
random_paper: 18
score:
  band: emerging
  composite: 23.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Tweekit Io Authentication
  slug: tweekit-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Tweekit Io Domain Security
  slug: tweekit-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tweekit-io
tags:
- Company
- AI
- File-Conversion
- API
- Media
website: https://tweekit.io/
---
