---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 46.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Capacities Io Agentic Access
  operation_count: 22
  slug: capacities-io-agentic-access
  summary_line: 22 operations · 14 acting
api_count: 1
apis:
- baseURL: https://api.capacities.io
  baseurl_source: declared
  description: Block content operations on objects
  name: Capacities Blocks API
  slug: capacities-io-blocks-api
- baseURL: https://api.capacities.io
  baseurl_source: declared
  description: Operations on objects in a space
  name: Capacities Object API
  slug: capacities-io-object-api
- baseURL: https://api.capacities.io
  baseurl_source: declared
  description: Search and list objects in a space
  name: Capacities Objects API
  slug: capacities-io-objects-api
- baseURL: https://api.capacities.io
  baseurl_source: declared
  description: Space related operations
  name: Capacities Space API
  slug: capacities-io-space-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/capacities-io/agentic-access/capacities-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/capacities-io-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/capacities-io/rate-limits/capacities-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/capacities-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/capacities-io/plans/capacities-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/capacities-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/capacities-io/rules/capacities-io-rules.yml
  title: ''
  type: Spectral
  url: rules/capacities-io-rules.yml
- group: design
  href: https://artifacts.apis.io/capacities-io/json-ld/capacities-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/capacities-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/capacities-io/vocabulary/capacities-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/capacities-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/capacities-io/data-model/capacities-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/capacities-io-data-model.yml
- group: auth
  href: https://artifacts.apis.io/capacities-io/authentication/capacities-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/capacities-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/capacities-io/conformance/capacities-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/capacities-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/capacities-io/llms/capacities-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/capacities-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/capacities-io/well-known/capacities-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/capacities-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/capacities-io/hosts/capacities-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/capacities-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/capacities-io/vendors/capacities-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/capacities-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/capacities-io/packages/capacities-io-packages.yml
  title: ''
  type: SDKs
  url: packages/capacities-io-packages.yml
- group: build
  href: https://artifacts.apis.io/capacities-io/packages/capacities-io-packages.yml
  title: ''
  type: Packages
  url: packages/capacities-io-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://capacities.io/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://capacities.io/help
- group: operate
  title: ''
  type: StatusPage
  url: https://status.capacities.io
- group: operate
  title: ''
  type: Roadmap
  url: https://capacities.io/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://capacities.io/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://capacities.io/about/team
- group: operate
  title: ''
  type: ChangeLog
  url: https://capacities.io/whats-new
- group: docs
  title: ''
  type: APIReference
  url: https://docs.capacities.io/raw/developer/api.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/capacities
- group: auth
  href: https://artifacts.apis.io/capacities-io/security/capacities-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/capacities-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://capacities.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.capacities.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.capacities.io
- group: company
  title: ''
  type: Blog
  url: https://capacities.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://capacities.io/pricing
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://developers.capacities.io/openapi.json
  - status: 401
    url: https://feedback.capacities.io/api/mcp
  - status: 200
    url: https://capacities.io/
  reason: partner-login
  state: gated
created: '2026-11-04'
description: Capacities is a note‑taking and knowledge‑management app that organizes ideas as connected objects instead of traditional files and folders. It offers a free tier across macOS, Windows, Linux, iOS, and Android, focusing on linking thoughts, visualizing relationships, and enhancing personal knowledge workflows.
image: https://capacities.io/thumbnail/thumbnail_index.png
json_schemas:
- name: ApiBlock
  property_count: 0
  slug: capacities-io-api-block
- name: ApiIconOutput
  property_count: 2
  slug: capacities-io-api-icon-output
- name: ApiLabelOptionOutput
  property_count: 3
  slug: capacities-io-api-label-option-output
- name: AppendBlocksPosition
  property_count: 0
  slug: capacities-io-append-blocks-position
- name: CreateObjectFromUrlProperties
  property_count: 2
  slug: capacities-io-create-object-from-url-properties
- name: WritableApiBlock
  property_count: 0
  slug: capacities-io-writable-api-block
jsonld:
- class_count: 63
  name: Capacities Io Context
  property_count: 41
  slug: capacities-io-context
layout: provider
modified: '2026-11-04'
name: Capacities
nav: Providers
network: true
overview: 'Capacities publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Blocks API, Object API, Objects API, and 1 more. Tagged areas include Knowledge Management, Note Taking, Productivity, Cross-Platform, and Collaboration.


  The Capacities catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Capacities'' developer surface includes authentication, support, changelog, API reference, documentation, engineering blog, pricing, and 23 more developer resources.'
plans:
- name: Capacities Io Plans Pricing
  plan_count: 3
  slug: capacities-io-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 3
  name: Capacities Io Rate Limits
  slug: capacities-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Capacities API Rules
  rule_count: 53
  severity_counts:
    error: 45
    hint: 0
    info: 4
    warn: 4
  slug: capacities-io-rules
score:
  band: developing
  composite: 50.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 61.8
    developer_ergonomics: 35.7
    discoverability: 67.0
    operational_transparency: 52.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Capacities Io Authentication
  slug: capacities-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Capacities Io Domain Security
  slug: capacities-io-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: capacities-io
tags:
- Knowledge Management
- Note Taking
- Productivity
- Cross-Platform
- Collaboration
website: https://capacities.io/
---
