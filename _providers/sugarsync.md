---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for SugarSync cloud file syncing and sharing services. Documentation is available at the developer portal.
  name: SugarSync API
  slug: sugarsync-api-2
- baseURL: https://api.sugarsync.com
  baseurl_source: declared
  description: 'SugarSync API as documented publicly: 19 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: SugarSync API
  slug: sugarsync-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/sugarsync/rules/sugarsync-rules.yml
  title: ''
  type: Spectral
  url: rules/sugarsync-rules.yml
- group: design
  href: https://artifacts.apis.io/sugarsync/json-ld/sugarsync-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sugarsync-context.jsonld
- group: design
  href: https://artifacts.apis.io/sugarsync/vocabulary/sugarsync-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sugarsync-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/sugarsync/data-model/sugarsync-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sugarsync-data-model.yml
- group: auth
  href: https://artifacts.apis.io/sugarsync/authentication/sugarsync-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sugarsync-authentication.yml
- group: design
  href: https://artifacts.apis.io/sugarsync/conformance/sugarsync-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sugarsync-conformance.yml
- group: other
  href: https://artifacts.apis.io/sugarsync/hosts/sugarsync-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sugarsync-hosts.yml
- group: other
  href: https://artifacts.apis.io/sugarsync/vendors/sugarsync-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sugarsync-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sugarsync.com/terms
- group: start
  title: ''
  type: GettingStarted
  url: https://www1.sugarsync.com/developer/getting-started
- group: auth
  href: https://artifacts.apis.io/sugarsync/security/sugarsync-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sugarsync-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www1.sugarsync.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www1.sugarsync.com/developer
- group: commercial
  title: ''
  type: Pricing
  url: https://www1.sugarsync.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://support.sugarsync.com/hc/en-us
coverage:
  checked: '2026-10-28'
  detail: The developer documentation provides HTML pages but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications.
  evidence:
  - status: 200
    url: https://www1.sugarsync.com/developer
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: SugarSync provides cloud file syncing, sharing, and backup services across devices, offering personal and business plans with secure storage, collaboration tools, and mobile apps. Users can store, sync, and share files, photos, and videos, with features like versioning, folder sharing, and automated backups, accessible via web, desktop, and mobile applications.
json_schemas:
- name: GetAlbumSc566494655299318005ContentsResponse
  property_count: 8
  slug: sugarsync-get-album-sc566494655299318005-contents-response
- name: GetFileSc566494655299366025Response
  property_count: 15
  slug: sugarsync-get-file-sc566494655299366025-response
- name: GetFolderSc5664945Response
  property_count: 7
  slug: sugarsync-get-folder-sc5664945-response
- name: GetReceivedshareReceivedshareidSc575745291961610490Response
  property_count: 7
  slug: sugarsync-get-receivedshare-receivedshareid-sc575745291961610490-response
- name: GetUserUseridResponse
  property_count: 18
  slug: sugarsync-get-user-userid-response
- name: GetWorkspaceSc566494655299317004Response
  property_count: 6
  slug: sugarsync-get-workspace-sc566494655299317004-response
jsonld:
- class_count: 15
  name: Sugarsync Context
  property_count: 55
  slug: sugarsync-context
layout: provider
modified: '2026-10-28'
name: SugarSync
nav: Providers
network: true
overview: 'SugarSync is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Storage, File Sync, Backup, Collaboration, and Business.


  The SugarSync catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SugarSync''s developer surface includes authentication, getting-started guide, documentation, pricing, support, and 10 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: SugarSync API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: sugarsync-rules
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 25.0
    discoverability: 53.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 26.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sugarsync/sugarsync-2026-11-03T144000.png
security:
- kind: authentication
  name: Sugarsync Authentication
  slug: sugarsync-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Sugarsync Domain Security
  slug: sugarsync-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sugarsync
tags:
- Cloud Storage
- File Sync
- Backup
- Collaboration
- Business
website: https://www1.sugarsync.com/
---
