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
    agent_skills: unknown
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
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: OctoPrint REST API documentation
  name: OctoPrint REST API
  slug: octoprint-rest-api
- description: 'OctoPrint API as documented publicly: 54 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: OctoPrint API
  slug: octoprint-api
artifact_total: 15
common:
- group: design
  href: https://artifacts.apis.io/octoprint/rules/octoprint-rules.yml
  title: ''
  type: Spectral
  url: rules/octoprint-rules.yml
- group: design
  href: https://artifacts.apis.io/octoprint/json-ld/octoprint-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/octoprint-context.jsonld
- group: design
  href: https://artifacts.apis.io/octoprint/vocabulary/octoprint-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/octoprint-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/octoprint/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/octoprint/data-model/octoprint-data-model.yml
  title: ''
  type: DataModel
  url: data-model/octoprint-data-model.yml
- group: auth
  href: https://artifacts.apis.io/octoprint/authentication/octoprint-authentication.yml
  title: ''
  type: Authentication
  url: authentication/octoprint-authentication.yml
- group: design
  href: https://artifacts.apis.io/octoprint/conformance/octoprint-conformance.yml
  title: ''
  type: Conformance
  url: conformance/octoprint-conformance.yml
- group: auth
  href: https://artifacts.apis.io/octoprint/well-known/octoprint-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/octoprint-security.txt
- group: agent
  href: https://artifacts.apis.io/octoprint/well-known/octoprint-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/octoprint-well-known.yml
- group: other
  href: https://artifacts.apis.io/octoprint/hosts/octoprint-hosts.yml
  title: ''
  type: Hosts
  url: hosts/octoprint-hosts.yml
- group: other
  href: https://artifacts.apis.io/octoprint/vendors/octoprint-vendors.yml
  title: ''
  type: Vendors
  url: vendors/octoprint-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://octoprint.org/help/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.octoprint.org/
- group: auth
  title: ''
  type: Security
  url: https://octoprint.org/security/
- group: company
  title: ''
  type: Newsroom
  url: https://octoprint.org/media/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.octoprint.org/
- group: auth
  href: https://artifacts.apis.io/octoprint/security/octoprint-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/octoprint-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/octoprint/security/octoprint-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/octoprint-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://octoprint.org/
- group: company
  title: ''
  type: Blog
  url: https://octoprint.org/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://octoprint.org/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OctoPrint
coverage:
  checked: '2026-10-28'
  detail: OctoPrint provides public REST API documentation but no machine‑readable OpenAPI or other spec.
  evidence:
  - status: 200
    url: https://docs.octoprint.org/en/main/api/index.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: 'OctoPrint is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
image: https://octoprint.org/assets/img/octoprint-600x400.png
json_schemas:
- name: PostApiConnectionRequest
  property_count: 6
  slug: octoprint-post-api-connection-request
- name: PostApiFilesLocalSomeFolderSomeModelStlRequest
  property_count: 8
  slug: octoprint-post-api-files-local-some-folder-some-model-stl-request
- name: PostApiFilesLocalWhistleV2GcodeRequest
  property_count: 8
  slug: octoprint-post-api-files-local-whistle-v2-gcode-request
- name: PostApiPrinterToolRequest
  property_count: 6
  slug: octoprint-post-api-printer-tool-request
- name: PostApiUtilTestRequest
  property_count: 22
  slug: octoprint-post-api-util-test-request
- name: PostApiUtilTestResponse
  property_count: 16
  slug: octoprint-post-api-util-test-response
jsonld:
- class_count: 67
  name: Octoprint Context
  property_count: 132
  slug: octoprint-context
layout: provider
modified: '2026-10-28'
name: OctoPrint
nav: Providers
network: true
overview: 'OctoPrint is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, 3D Printing, Open Source, IoT, and Maker.


  The OctoPrint catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OctoPrint''s developer surface includes authentication, support, documentation, engineering blog, and 18 more developer resources.'
random_paper: 10
rate_limits:
- limit_count: 0
  name: Octoprint Rate Limits
  slug: octoprint-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: OctoPrint API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: octoprint-rules
scopes:
- name: Octoprint Scopes
  scope_count: 0
  slug: octoprint-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 26.7
    discoverability: 49.1
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 29.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/octoprint/octoprint-2026-11-03T140433.png
security:
- kind: authentication
  name: Octoprint Authentication
  slug: octoprint-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Octoprint Domain Security
  slug: octoprint-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Octoprint Vulnerability Disclosure
  slug: octoprint-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: octoprint
tags:
- Company
- 3D Printing
- Open Source
- IoT
- Maker
website: https://octoprint.org/
---
