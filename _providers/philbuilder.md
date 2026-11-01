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
  href: https://artifacts.apis.io/philbuilder/hosts/philbuilder-hosts.yml
  title: ''
  type: Hosts
  url: hosts/philbuilder-hosts.yml
- group: other
  href: https://artifacts.apis.io/philbuilder/vendors/philbuilder-vendors.yml
  title: ''
  type: Vendors
  url: vendors/philbuilder-vendors.yml
- group: auth
  href: https://artifacts.apis.io/philbuilder/security/philbuilder-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/philbuilder-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apiphilbuilder.netlify.app
- group: docs
  title: ''
  type: Documentation
  url: https://apiphilbuilder.netlify.app/#intro
- group: other
  title: ''
  type: Image
  url: https://apiphilbuilder.netlify.app/favicon.ico
- group: start
  title: ''
  type: GettingStarted
  url: https://apiphilbuilder.netlify.app/#intro
- group: commercial
  title: ''
  type: Pricing
  url: https://apiphilbuilder.netlify.app/#plans
coverage:
  checked: '2026-10-28'
  detail: The documentation site provides only HTML pages and returns 404 for typical OpenAPI spec URLs.
  evidence:
  - status: 404
    url: https://apiphilbuilder.netlify.app/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: PhilBuilder provides an API (v1) that allows developers to generate Android and Windows builds, manage API keys, upload ZIP or icon packages, and monitor build status and quotas. The service is documented in French and offers endpoints for key creation, revocation, and usage tracking, as well as plan information and pricing details. It aims to streamline mobile and desktop application distribution via automated build pipelines.
layout: provider
modified: '2026-10-28'
name: PhilBuilder
nav: Providers
network: true
overview: 'PhilBuilder is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API, BuildAutomation, Mobile, and Desktop.


  PhilBuilder''s developer surface includes documentation, getting-started guide, pricing, and 5 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Philbuilder Domain Security
  slug: philbuilder-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: philbuilder
tags:
- Company
- API
- BuildAutomation
- Mobile
- Desktop
website: https://apiphilbuilder.netlify.app
---
