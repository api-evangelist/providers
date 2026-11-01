---
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 13
  human_in_the_loop: 2
  name: Pterodactyl Agentic Access
  operation_count: 33
  slug: pterodactyl-agentic-access
  summary_line: 33 operations · 13 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: The Admin API from Pterodactyl — 17 operation(s) for admin.
  name: Pterodactyl Admin API
  slug: pterodactyl-admin-api
- description: The Application API from Pterodactyl — 1 operation(s) for application.
  name: Pterodactyl Application API
  slug: pterodactyl-application-api
- description: The Client API from Pterodactyl — 1 operation(s) for client.
  name: Pterodactyl Client API
  slug: pterodactyl-client-api
- description: The Gpg API from Pterodactyl — 1 operation(s) for gpg.
  name: Pterodactyl Gpg API
  slug: pterodactyl-gpg-api
- description: The Installer API from Pterodactyl — 1 operation(s) for installer.
  name: Pterodactyl Installer API
  slug: pterodactyl-installer-api
- description: The Pterodactyl API API from Pterodactyl — 1 operation(s) for pterodactyl api.
  name: Pterodactyl Pterodactyl API
  slug: pterodactyl-pterodactyl-api-api
- description: The Pterodactyl API from Pterodactyl — 3 operation(s) for pterodactyl.
  name: Pterodactyl Pterodactyl API
  slug: pterodactyl-pterodactyl-api
- description: The Setup 22 API from Pterodactyl — 1 operation(s) for setup 22.
  name: Pterodactyl Setup 22 API
  slug: pterodactyl-setup-22-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/pterodactyl/agentic-access/pterodactyl-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pterodactyl-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/pterodactyl/rules/pterodactyl-rules.yml
  title: ''
  type: Spectral
  url: rules/pterodactyl-rules.yml
- group: design
  href: https://artifacts.apis.io/pterodactyl/json-ld/pterodactyl-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pterodactyl-context.jsonld
- group: design
  href: https://artifacts.apis.io/pterodactyl/vocabulary/pterodactyl-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pterodactyl-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/pterodactyl/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/pterodactyl/data-model/pterodactyl-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pterodactyl-data-model.yml
- group: operate
  href: https://artifacts.apis.io/pterodactyl/changelog/pterodactyl-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/pterodactyl-changelog.yml
- group: auth
  href: https://artifacts.apis.io/pterodactyl/authentication/pterodactyl-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pterodactyl-authentication.yml
- group: design
  href: https://artifacts.apis.io/pterodactyl/conformance/pterodactyl-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pterodactyl-conformance.yml
- group: other
  href: https://artifacts.apis.io/pterodactyl/overlays/pterodactyl-openapi-generated-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pterodactyl-openapi-generated-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/pterodactyl/llms/pterodactyl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pterodactyl-llms.txt
- group: other
  href: https://artifacts.apis.io/pterodactyl/hosts/pterodactyl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pterodactyl-hosts.yml
- group: other
  href: https://artifacts.apis.io/pterodactyl/vendors/pterodactyl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pterodactyl-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/pterodactyl/panel/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/pterodactyl/panel/releases
- group: auth
  href: https://artifacts.apis.io/pterodactyl/security/pterodactyl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pterodactyl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pterodactyl.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pterodactyl.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pterodactyl.io/v2/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pterodactyl.io/v2/panel/getting-started
- group: start
  title: ''
  type: DeveloperPortal
  url: https://eggs.pterodactyl.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pterodactyl
created: '2026-10-28'
description: Pterodactyl is a free, open‑source game server management panel built with PHP, React, and Go. It runs every game server in an isolated Docker container, providing a web‑based control panel, a daemon called Wings, and a RESTful API. The platform offers extensive documentation, including getting‑started guides, an API reference, and community‑contributed server templates via the Eggs portal.
image: https://pterodactyl.io/favicon.svg?v=4
json_schemas:
- name: GetApiAdminExtensionsArchitectoSettingsResponse
  property_count: 2
  slug: pterodactyl-get-api-admin-extensions-architecto-settings-response
- name: GetApiAdminExtensionsResponse
  property_count: 2
  slug: pterodactyl-get-api-admin-extensions-response
- name: GetApiApplicationUsersResponse
  property_count: 3
  slug: pterodactyl-get-api-application-users-response
- name: PostApiAdminExtensionsArchitectoDisableResponse
  property_count: 1
  slug: pterodactyl-post-api-admin-extensions-architecto-disable-response
- name: PostApiAdminExtensionsArchitectoEnableResponse
  property_count: 1
  slug: pterodactyl-post-api-admin-extensions-architecto-enable-response
- name: PostApiAdminExtensionsResponse
  property_count: 1
  slug: pterodactyl-post-api-admin-extensions-response
jsonld:
- class_count: 16
  name: Pterodactyl Context
  property_count: 32
  slug: pterodactyl-context
layout: provider
modified: '2026-10-28'
name: Pterodactyl
nav: Providers
network: true
overview: 'Pterodactyl publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Application API, Client API, and 5 more. Tagged areas include Company, Game Server, Open Source, Docker, and API.


  The Pterodactyl catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Pterodactyl''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, and 17 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Pterodactyl API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: pterodactyl-rules
scopes:
- name: Pterodactyl Scopes
  scope_count: 0
  slug: pterodactyl-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 24.3
    developer_ergonomics: 56.4
    discoverability: 57.1
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Pterodactyl Authentication
  slug: pterodactyl-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pterodactyl Domain Security
  slug: pterodactyl-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: admin-extensions
  slug: pterodactyl-admin-extensions
slug: pterodactyl
tags:
- Company
- Game Server
- Open Source
- Docker
- API
website: https://pterodactyl.io/
---
