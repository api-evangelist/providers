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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Provides REST and WebSocket APIs for data sharing and workflow automation as described on the platform API page.
  name: ipushpull API
  slug: ipushpull-api-2
- description: 'Ipushpull API as documented publicly: 36 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: Ipushpull API
  slug: ipushpull-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/ipushpull/rules/ipushpull-rules.yml
  title: ''
  type: Spectral
  url: rules/ipushpull-rules.yml
- group: design
  href: https://artifacts.apis.io/ipushpull/json-ld/ipushpull-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ipushpull-context.jsonld
- group: design
  href: https://artifacts.apis.io/ipushpull/vocabulary/ipushpull-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ipushpull-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ipushpull/data-model/ipushpull-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ipushpull-data-model.yml
- group: design
  href: https://artifacts.apis.io/ipushpull/conformance/ipushpull-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ipushpull-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ipushpull/llms/ipushpull-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ipushpull-llms.txt
- group: agent
  href: https://artifacts.apis.io/ipushpull/well-known/ipushpull-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ipushpull-well-known.yml
- group: other
  href: https://artifacts.apis.io/ipushpull/hosts/ipushpull-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ipushpull-hosts.yml
- group: other
  href: https://artifacts.apis.io/ipushpull/vendors/ipushpull-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ipushpull-vendors.yml
- group: build
  href: https://artifacts.apis.io/ipushpull/packages/ipushpull-packages.yml
  title: ''
  type: SDKs
  url: packages/ipushpull-packages.yml
- group: build
  href: https://artifacts.apis.io/ipushpull/packages/ipushpull-packages.yml
  title: ''
  type: Packages
  url: packages/ipushpull-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ipushpull.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/iPushPull
- group: auth
  href: https://artifacts.apis.io/ipushpull/security/ipushpull-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ipushpull-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ipushpull.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ipushpull.com/platform/api
- group: docs
  title: ''
  type: APIReference
  url: https://ipushpull.com/platform/api
- group: start
  title: ''
  type: GettingStarted
  url: https://ipushpull.com/platform?hsLang=en
- group: operate
  title: ''
  type: Support
  url: https://ipushpull.com/resources/faq
- group: company
  title: ''
  type: Blog
  url: https://ipushpull.com/blog
created: '2026-10-20'
description: Ipushpull provides a governed data layer for over‑the‑counter (OTC) financial markets, enabling real‑time data sharing, chat‑based workflow automation, and secure data services across banks, asset managers, brokers, exchanges, hedge funds and technology providers. Their platform connects unstructured messages and data into valuable assets, driving automation, client service improvements and liquidity enhancements for financial institutions.
image: https://ipushpull.com/hubfs/Untitled%20(62)-1.png
json_schemas:
- name: GetReferenceViewsAdvancedViewFiltersMdResponse
  property_count: 1
  slug: ipushpull-get-reference-views-advanced-view-filters-md-response
- name: GetReferenceViewsViewCustomColumnsMdResponse
  property_count: 1
  slug: ipushpull-get-reference-views-view-custom-columns-md-response
jsonld:
- class_count: 2
  name: Ipushpull Context
  property_count: 2
  slug: ipushpull-context
layout: provider
modified: '2026-10-20'
name: Ipushpull
nav: Providers
network: true
overview: 'Ipushpull is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Data Sharing, Real-Time, and Automation.


  The Ipushpull catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ipushpull''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 15 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Ipushpull API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: ipushpull-rules
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 48.3
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 20.0
    developer_ergonomics: 29.8
    discoverability: 64.3
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 24.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/ipushpull/ipushpull-2026-11-03T134030.png
security:
- kind: domain-security
  name: Ipushpull Domain Security
  slug: ipushpull-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ipushpull
tags:
- Company
- Fintech
- Data Sharing
- Real-Time
- Automation
website: https://ipushpull.com/
---
