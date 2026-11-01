---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://demo.owncloud.com
  baseurl_source: declared
  description: 'ownCloud API as documented publicly: 108 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: ownCloud API
  slug: owncloud-api
artifact_total: 13
common:
- group: other
  href: https://artifacts.apis.io/owncloud/vendors/owncloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/owncloud-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/owncloud/plans/owncloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/owncloud-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/owncloud/rules/owncloud-rules.yml
  title: ''
  type: Spectral
  url: rules/owncloud-rules.yml
- group: design
  href: https://artifacts.apis.io/owncloud/json-ld/owncloud-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/owncloud-context.jsonld
- group: design
  href: https://artifacts.apis.io/owncloud/vocabulary/owncloud-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/owncloud-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/owncloud/data-model/owncloud-data-model.yml
  title: ''
  type: DataModel
  url: data-model/owncloud-data-model.yml
- group: operate
  href: https://artifacts.apis.io/owncloud/changelog/owncloud-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/owncloud-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://owncloud.com/security
- group: design
  href: https://artifacts.apis.io/owncloud/conformance/owncloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/owncloud-conformance.yml
- group: agent
  href: https://artifacts.apis.io/owncloud/llms/owncloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/owncloud-llms.txt
- group: auth
  href: https://artifacts.apis.io/owncloud/well-known/owncloud-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/owncloud-security.txt
- group: agent
  href: https://artifacts.apis.io/owncloud/well-known/owncloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/owncloud-well-known.yml
- group: other
  href: https://artifacts.apis.io/owncloud/hosts/owncloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/owncloud-hosts.yml
- group: build
  href: https://artifacts.apis.io/owncloud/packages/owncloud-packages.yml
  title: ''
  type: SDKs
  url: packages/owncloud-packages.yml
- group: build
  href: https://artifacts.apis.io/owncloud/packages/owncloud-packages.yml
  title: ''
  type: Packages
  url: packages/owncloud-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://owncloud.com/support
- group: auth
  title: ''
  type: Security
  url: https://owncloud.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://owncloud.com/privacy-statement/
- group: commercial
  title: ''
  type: Pricing
  url: https://owncloud.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://owncloud.com/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/owncloud
- group: start
  title: ''
  type: GettingStarted
  url: https://owncloud.com/get-started/
- group: operate
  title: ''
  type: ChangeLog
  url: https://owncloud.com/changelog/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.owncloud.com/
- group: auth
  href: https://artifacts.apis.io/owncloud/security/owncloud-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/owncloud-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/owncloud/security/owncloud-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/owncloud-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/owncloud/security/owncloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/owncloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://owncloud.com/
coverage:
  checked: '2026-10-27'
  detail: ownCloud provides documentation but no machine‑readable API specification was found.
  evidence:
  - status: 200
    url: https://owncloud.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: ownCloud provides open-source file sync and share solutions for enterprises and individuals, offering on‑premises and cloud‑based deployments. It enables secure collaboration, file access across devices, and integration with third‑party services, emphasizing data sovereignty and compliance.
image: https://owncloud.com/wp-content/uploads/2020/08/ownCloud-Trademark.png
json_schemas:
- name: DeleteGraphV10DrivesStorageUsers1535Aa42DA3C743299Eba5Ef48Fc
  property_count: 1
  slug: owncloud-delete-graph-v10-drives-storage-users1535-aa42-da3-c743299-eba5-ef48-fc
- name: GetMeResponse
  property_count: 4
  slug: owncloud-get-me-response
- name: PatchDrivesDriveidRequest
  property_count: 4
  slug: owncloud-patch-drives-driveid-request
- name: PostUsersRequest
  property_count: 4
  slug: owncloud-post-users-request
- name: PutDavSpacesStorageUsers124SomeAdminUserId0000000000000000Re
  property_count: 6
  slug: owncloud-put-dav-spaces-storage-users124-some-admin-user-id0000000000000000-re
- name: PutDavSpacesStorageUsers124SomeAdminUserId0000000000000000Re2
  property_count: 6
  slug: owncloud-put-dav-spaces-storage-users124-some-admin-user-id0000000000000000-re2
jsonld:
- class_count: 44
  name: Owncloud Context
  property_count: 30
  slug: owncloud-context
layout: provider
modified: '2026-10-27'
name: ownCloud
nav: Providers
network: true
overview: 'ownCloud is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include File Sharing, Secure Collaboration, Cloud Storage, Data Sovereignty, and SaaS.


  The ownCloud catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ownCloud''s developer surface includes changelog, support, pricing, getting-started guide, documentation, and 23 more developer resources.'
plans:
- name: Owncloud Plans Pricing
  plan_count: 3
  slug: owncloud-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: ownCloud API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: owncloud-rules
score:
  band: developing
  composite: 44.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    contract_governance: 35.6
    contract_quality: 26.3
    developer_ergonomics: 33.3
    discoverability: 67.9
    operational_transparency: 31.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 22
      marker_coverage: 100.0
      total: 22
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
    score: 31.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Owncloud Domain Security
  slug: owncloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Owncloud Vulnerability Disclosure
  slug: owncloud-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Owncloud Trust Center
  slug: owncloud-trust-center
  summary_line: HIPAA, GDPR
slug: owncloud
tags:
- File Sharing
- Secure Collaboration
- Cloud Storage
- Data Sovereignty
- SaaS
- On-Premises
- Compliance
website: https://owncloud.com/
---
