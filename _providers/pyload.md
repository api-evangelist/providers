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
    agentic_access: derived
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
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 88
  human_in_the_loop: 10
  name: Pyload Agentic Access
  operation_count: 168
  slug: pyload-agentic-access
  summary_line: 168 operations · 88 acting · 10 human-in-the-loop
api_count: 1
apis:
- description: The pyLoad REST API from pyLoad — 84 operation(s) for pyload rest.
  name: pyLoad pyLoad REST API
  slug: pyload-pyload-rest-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/pyload/agentic-access/pyload-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pyload-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/pyload/rules/pyload-rules.yml
  title: ''
  type: Spectral
  url: rules/pyload-rules.yml
- group: design
  href: https://artifacts.apis.io/pyload/json-ld/pyload-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pyload-context.jsonld
- group: design
  href: https://artifacts.apis.io/pyload/vocabulary/pyload-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pyload-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/pyload/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/pyload/data-model/pyload-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pyload-data-model.yml
- group: design
  href: https://artifacts.apis.io/pyload/conformance/pyload-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pyload-conformance.yml
- group: other
  href: https://artifacts.apis.io/pyload/overlays/pyload-openapi-generator-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pyload-openapi-generator-overlay.yaml
- group: other
  href: https://artifacts.apis.io/pyload/hosts/pyload-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pyload-hosts.yml
- group: other
  href: https://artifacts.apis.io/pyload/vendors/pyload-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pyload-vendors.yml
- group: build
  href: https://artifacts.apis.io/pyload/packages/pyload-packages.yml
  title: ''
  type: SDKs
  url: packages/pyload-packages.yml
- group: build
  href: https://artifacts.apis.io/pyload/packages/pyload-packages.yml
  title: ''
  type: Packages
  url: packages/pyload-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/pyload/pyload/releases
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.github.com/en/github-cli/github-cli/quickstart
- group: auth
  href: https://artifacts.apis.io/pyload/authentication/pyload-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pyload-authentication.yml
- group: auth
  href: https://artifacts.apis.io/pyload/security/pyload-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pyload-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pyload.net/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/pyload/pyload/wiki
- group: operate
  title: ''
  type: Support
  url: https://github.com/pyload/pyload/issues
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/pyload/pyload/milestones
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pyload
created: '2026-10-28'
description: pyLoad is an open-source, lightweight download manager written in Python. It provides a web UI for managing downloads, supports many hosters and plugins, runs headlessly on servers, NAS devices, or desktops, and offers a documented API for integration and automation.
image: https://raw.githubusercontent.com/pyload/pyload/main/media/banner.png
json_schemas:
- name: AccountInfo
  property_count: 7
  slug: pyload-account-info
- name: DownloadInfo
  property_count: 17
  slug: pyload-download-info
- name: FileData
  property_count: 11
  slug: pyload-file-data
- name: PackageData
  property_count: 13
  slug: pyload-package-data
- name: ServerStatus
  property_count: 9
  slug: pyload-server-status
- name: UserData
  property_count: 6
  slug: pyload-user-data
jsonld:
- class_count: 14
  name: Pyload Context
  property_count: 62
  slug: pyload-context
layout: provider
modified: '2026-10-28'
name: pyLoad
nav: Providers
network: true
overview: 'pyLoad publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: pyLoad REST API. Tagged areas include Download-Manager, Open Source, Python, Automation, and File Transfer.


  The pyLoad catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  pyLoad''s developer surface includes changelog, getting-started guide, authentication, documentation, support, and 16 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: pyLoad API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: pyload-rules
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.3
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 57.1
    developer_ergonomics: 38.6
    discoverability: 57.1
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/pyload/pyload-2026-11-03T141730.png
security:
- kind: authentication
  name: Pyload Authentication
  slug: pyload-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pyload Domain Security
  slug: pyload-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: add-files
  slug: pyload-add-files
slug: pyload
tags:
- Download-Manager
- Open Source
- Python
- Automation
- File Transfer
website: https://pyload.net/
---
