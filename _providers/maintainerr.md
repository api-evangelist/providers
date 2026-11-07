---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Maintainerr providing endpoints to manage media library automation.
  name: Maintainerr API
  slug: maintainerr-api-2
- description: 'Maintainerr API as documented publicly: 43 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Maintainerr API
  slug: maintainerr-api
artifact_total: 6
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.maintainerr.info/blog/getting-started-s01e01/
- group: design
  href: https://artifacts.apis.io/maintainerr/rules/maintainerr-rules.yml
  title: ''
  type: Spectral
  url: rules/maintainerr-rules.yml
- group: design
  href: https://artifacts.apis.io/maintainerr/json-ld/maintainerr-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/maintainerr-context.jsonld
- group: design
  href: https://artifacts.apis.io/maintainerr/vocabulary/maintainerr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/maintainerr-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/maintainerr/data-model/maintainerr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/maintainerr-data-model.yml
- group: design
  href: https://artifacts.apis.io/maintainerr/conformance/maintainerr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/maintainerr-conformance.yml
- group: other
  href: https://artifacts.apis.io/maintainerr/hosts/maintainerr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/maintainerr-hosts.yml
- group: other
  href: https://artifacts.apis.io/maintainerr/vendors/maintainerr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/maintainerr-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.maintainerr.info/status/maintainerr
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/Maintainerr/Maintainerr/releases
- group: auth
  href: https://artifacts.apis.io/maintainerr/security/maintainerr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/maintainerr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://maintainerr.info/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.maintainerr.info/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.maintainerr.info/
- group: operate
  title: ''
  type: Support
  url: https://discord.maintainerr.info/
- group: company
  title: ''
  type: Blog
  url: https://blog.maintainerr.info/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/maintainerr
- group: commercial
  title: ''
  type: Pricing
  url: https://maintainerr.info/#pricing
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://maintainerr.info/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Maintainerr is a free, self‑hosted tool that automatically cleans up unwatched or unwanted movies and shows from Plex, Jellyfin, and Emby. It offers powerful, customizable rules to keep media libraries tidy, runs in Docker and on Linux, Windows, macOS, and integrates with popular media servers to improve storage efficiency and user experience.
image: https://maintainerr.info/og-image.png
json_schemas:
- name: PostApiOverlaysImagesRequest
  property_count: 1
  slug: maintainerr-post-api-overlays-images-request
jsonld:
- class_count: 1
  name: Maintainerr Context
  property_count: 1
  slug: maintainerr-context
layout: provider
modified: '2026-10-28'
name: Maintainerr
nav: Providers
network: true
overview: 'Maintainerr is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Automation, Self-Hosted, and Docker.


  The Maintainerr catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Maintainerr''s developer surface includes getting-started guide, changelog, documentation, API reference, support, engineering blog, pricing, and 11 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Maintainerr API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: maintainerr-rules
score:
  band: emerging
  composite: 18.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 47.4
    catalog_earned_first_party: 0.0
    catalog_gap: 67.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.9
  facets:
    access_clarity: 5.3
    contract_governance: 19.7
    contract_quality: 17.6
    developer_ergonomics: 17.9
    discoverability: 57.1
    operational_transparency: 18.4
  previous_composite: 25.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/maintainerr/maintainerr-2026-11-03T135253.png
security:
- kind: domain-security
  name: Maintainerr Domain Security
  slug: maintainerr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: maintainerr
tags:
- Company
- Media
- Automation
- Self-Hosted
- Docker
website: https://maintainerr.info/
---
