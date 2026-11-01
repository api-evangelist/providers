---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 42
  human_in_the_loop: 6
  name: Mindcloud Agentic Access
  operation_count: 98
  slug: mindcloud-agentic-access
  summary_line: 98 operations · 42 acting · 6 human-in-the-loop
api_count: 1
apis:
- description: Primary API for MindCloud services
  name: MindCloud API
  slug: mindcloud-api
- baseURL: https://connect.mindcloud.co/v2
  baseurl_source: declared
  description: The api-keys API from MindCloud — 2 operation(s) for api-keys.
  name: MindCloud API Keys API
  slug: mindcloud-api-keys-api
- baseURL: https://connect.mindcloud.co/v2
  baseurl_source: declared
  description: The child-companies API from MindCloud — 2 operation(s) for child-companies.
  name: MindCloud Child Companies API
  slug: mindcloud-child-companies-api
- baseURL: https://connect.mindcloud.co/v2
  baseurl_source: declared
  description: The companies API from MindCloud — 2 operation(s) for companies.
  name: MindCloud Companies API
  slug: mindcloud-companies-api
- baseURL: https://connect.mindcloud.co/v2
  baseurl_source: declared
  description: The connections API from MindCloud — 3 operation(s) for connections.
  name: MindCloud Connections API
  slug: mindcloud-connections-api
- baseURL: https://connect.mindcloud.co/v2
  baseurl_source: declared
  description: The embedded API from MindCloud — 2 operation(s) for embedded.
  name: MindCloud Embedded API
  slug: mindcloud-embedded-api
- baseURL: https://connect.mindcloud.co/v2
  baseurl_source: declared
  description: The environments API from MindCloud — 1 operation(s) for environments.
  name: MindCloud Environments API
  slug: mindcloud-environments-api
- baseURL: https://connect.mindcloud.co/v2
  baseurl_source: declared
  description: The me API from MindCloud — 1 operation(s) for me.
  name: MindCloud Me API
  slug: mindcloud-me-api
- baseURL: https://connect.mindcloud.co/v2
  baseurl_source: declared
  description: The members API from MindCloud — 2 operation(s) for members.
  name: MindCloud Members API
  slug: mindcloud-members-api
- baseURL: https://connect.mindcloud.co/v2
  baseurl_source: declared
  description: The meta API from MindCloud — 1 operation(s) for meta.
  name: MindCloud Meta API
  slug: mindcloud-meta-api
- baseURL: https://connect.mindcloud.co/v2
  baseurl_source: declared
  description: The roles API from MindCloud — 2 operation(s) for roles.
  name: MindCloud Roles API
  slug: mindcloud-roles-api
- baseURL: https://connect.mindcloud.co/v2
  baseurl_source: declared
  description: The runs API from MindCloud — 5 operation(s) for runs.
  name: MindCloud Runs API
  slug: mindcloud-runs-api
- baseURL: https://connect.mindcloud.co/v2
  baseurl_source: declared
  description: The universal API from MindCloud — 5 operation(s) for universal.
  name: MindCloud Universal API
  slug: mindcloud-universal-api
- baseURL: https://connect.mindcloud.co/v2
  baseurl_source: declared
  description: The usage API from MindCloud — 3 operation(s) for usage.
  name: MindCloud Usage API
  slug: mindcloud-usage-api
- baseURL: https://connect.mindcloud.co/v2
  baseurl_source: declared
  description: The workflows API from MindCloud — 6 operation(s) for workflows.
  name: MindCloud Workflows API
  slug: mindcloud-workflows-api
artifact_total: 30
common:
- group: operate
  href: https://artifacts.apis.io/mindcloud/lifecycle/mindcloud-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/mindcloud-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/mindcloud/lifecycle/mindcloud-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mindcloud-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/mindcloud/overlays/mindcloud-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mindcloud-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/mindcloud/mcp/mindcloud-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mindcloud-mcp.yml
- group: agent
  href: https://artifacts.apis.io/mindcloud/agentic-access/mindcloud-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mindcloud-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/mindcloud/rules/mindcloud-rules.yml
  title: ''
  type: Spectral
  url: rules/mindcloud-rules.yml
- group: design
  href: https://artifacts.apis.io/mindcloud/json-ld/mindcloud-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mindcloud-context.jsonld
- group: design
  href: https://artifacts.apis.io/mindcloud/vocabulary/mindcloud-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mindcloud-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/mindcloud/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/mindcloud/data-model/mindcloud-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mindcloud-data-model.yml
- group: operate
  href: https://artifacts.apis.io/mindcloud/changelog/mindcloud-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mindcloud-changelog.yml
- group: auth
  href: https://artifacts.apis.io/mindcloud/authentication/mindcloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mindcloud-authentication.yml
- group: design
  href: https://artifacts.apis.io/mindcloud/errors/mindcloud-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mindcloud-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mindcloud/conformance/mindcloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mindcloud-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mindcloud/llms/mindcloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mindcloud-llms.txt
- group: agent
  href: https://artifacts.apis.io/mindcloud/well-known/mindcloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mindcloud-well-known.yml
- group: other
  href: https://artifacts.apis.io/mindcloud/hosts/mindcloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mindcloud-hosts.yml
- group: other
  href: https://artifacts.apis.io/mindcloud/vendors/mindcloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mindcloud-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.mindcloud.co
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mindcloud.co/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://mindcloud.co/apps/categories/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mindcloud.co/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://mindcloud.co/docs/cirra/cirra-getting-started/what-is-cirra
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mindcloud.co/
- group: docs
  title: ''
  type: APIReference
  url: https://mindcloud.co/changelog
- group: auth
  href: https://artifacts.apis.io/mindcloud/security/mindcloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mindcloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mindcloud.co/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://mindcloud.co/openapi.json
  - status: null
    url: https://connect.mindcloud.co/v1/openapi.json
  - status: 401
    url: https://connect.mindcloud.co/mcp
  - status: 200
    url: https://mindcloud.co/
  reason: partner-login
  state: gated
created: '2026-10-20'
description: MindCloud offers a low-code workflow and integration platform that connects business tools and automates data movement. It provides full‑service custom integrations, a visual integration builder, and a universal API that links to over 3,400 applications. The service is aimed at fast‑growing companies that need expert‑guided, production‑grade integrations without dedicated engineering resources.
image: https://mindcloud.co/opengraph-image
json_schemas:
- name: Me
  property_count: 4
  slug: mindcloud-me
- name: RunDetail
  property_count: 19
  slug: mindcloud-run-detail
- name: Run
  property_count: 16
  slug: mindcloud-run
- name: UniversalActionDetail
  property_count: 19
  slug: mindcloud-universal-action-detail
- name: UniversalAction
  property_count: 20
  slug: mindcloud-universal-action
- name: UniversalLookup
  property_count: 8
  slug: mindcloud-universal-lookup
jsonld:
- class_count: 36
  name: Mindcloud Context
  property_count: 122
  slug: mindcloud-context
layout: provider
mcp_servers:
- description: Remote MCP server at connect.mindcloud.co.
  name: MindCloud MCP Server
  slug: mindcloud-mcp-yml
modified: '2026-10-20'
name: MindCloud
nav: Providers
network: true
overview: 'MindCloud publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Keys API, Child Companies API, Companies API, and 12 more. Tagged areas include Integration Platform, Low-Code, Enterprise Integration, and Workflows.


  The MindCloud catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MindCloud''s developer surface includes changelog, authentication, support, getting-started guide, documentation, API reference, and 21 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: MindCloud API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: mindcloud-rules
score:
  band: developing
  composite: 44.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 22.0
    contract_quality: 62.5
    developer_ergonomics: 47.0
    discoverability: 56.7
    operational_transparency: 23.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Mindcloud Authentication
  slug: mindcloud-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mindcloud Domain Security
  slug: mindcloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: mindcloud-manage-connection
  slug: mindcloud-manage-connection
- name: mindcloud-manage-members
  slug: mindcloud-manage-members
- name: mindcloud-run-universal-action
  slug: mindcloud-run-universal-action
slug: mindcloud
tags:
- Integration Platform
- Low-Code
- Enterprise Integration
- Workflows
website: https://mindcloud.co/
---
