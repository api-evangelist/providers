---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 61
  human_in_the_loop: 1
  name: Usewrit App Agentic Access
  operation_count: 116
  slug: usewrit-app-agentic-access
  summary_line: 116 operations · 61 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.usewrit.app
  baseurl_source: declared
  description: Daemon status and deep health (both require auth like every other route).
  name: usewrit-app Agent API
  slug: usewrit-app-agent-api
- baseURL: https://api.usewrit.app
  baseurl_source: declared
  description: Event → action rules (change_detected, webhook_received, workflow lifecycle).
  name: usewrit-app Automations API
  slug: usewrit-app-automations-api
- baseURL: https://api.usewrit.app
  baseurl_source: declared
  description: Tiered Writ CLOUD surface (scrape / map / crawl) — runs on the cloud, NOT the local daemon. These operations target the cloud server (`https://api.usewrit.app`), overriding the daemon `servers` above.
  name: usewrit-app Cloud API
  slug: usewrit-app-cloud-api
- baseURL: https://api.usewrit.app
  baseurl_source: declared
  description: Dragnet whole-site crawl — start/list/poll/cancel; pages aggregate under a synthetic workflow.
  name: usewrit-app Crawl API
  slug: usewrit-app-crawl-api
- baseURL: https://api.usewrit.app
  baseurl_source: declared
  description: Extracted-data explorer — aggregate tables, facets, exports, lineage runs.
  name: usewrit-app Data API
  slug: usewrit-app-data-api
- baseURL: https://api.usewrit.app
  baseurl_source: declared
  description: 'Unified read-only catalogue over everything that has accumulated extracted data — crawl and workflow origins alike, keyed by the same id (`source_type` tells them apart). Records/export/search accept '
  name: usewrit-app Datasets API
  slug: usewrit-app-datasets-api
- baseURL: https://api.usewrit.app
  baseurl_source: declared
  description: Field extractors that turn a selector's captured content into typed values.
  name: usewrit-app Extractors API
  slug: usewrit-app-extractors-api
- baseURL: https://api.usewrit.app
  baseurl_source: declared
  description: OpenAI-style encrypted-at-rest file handles (metadata + byte I/O).
  name: usewrit-app Files API
  slug: usewrit-app-files-api
- baseURL: https://api.usewrit.app
  baseurl_source: declared
  description: Scoped `wlk_` API keys for external clients (requires the full-access `wlt_` token).
  name: usewrit-app Keys API
  slug: usewrit-app-keys-api
- baseURL: https://api.usewrit.app
  baseurl_source: declared
  description: Page monitors (the `targets` table), device check capacity, and change history.
  name: usewrit-app Monitors API
  slug: usewrit-app-monitors-api
- baseURL: https://api.usewrit.app
  baseurl_source: declared
  description: Login identities (credentials, TOTP, fingerprint, proxy) — secrets sealed daemon-side.
  name: usewrit-app Personas API
  slug: usewrit-app-personas-api
- baseURL: https://api.usewrit.app
  baseurl_source: declared
  description: Read-only run feed, per-run results/data, live SSE events, and cancel-by-run-id.
  name: usewrit-app Runs API
  slug: usewrit-app-runs-api
- baseURL: https://api.usewrit.app
  baseurl_source: declared
  description: Vault secrets addressed by unique text key; values never leave the daemon.
  name: usewrit-app Secrets API
  slug: usewrit-app-secrets-api
- baseURL: https://api.usewrit.app
  baseurl_source: declared
  description: Per-monitor content selectors (text / html / visual) nested under monitors.
  name: usewrit-app Selectors API
  slug: usewrit-app-selectors-api
- baseURL: https://api.usewrit.app
  baseurl_source: declared
  description: App-lock control surface (status / lock / unlock).
  name: usewrit-app Vault API
  slug: usewrit-app-vault-api
- baseURL: https://api.usewrit.app
  baseurl_source: declared
  description: Recorded workflow CRUD, async run/cancel, and the browserless HTTP-lane session.
  name: usewrit-app Workflows API
  slug: usewrit-app-workflows-api
- baseURL: https://api.usewrit.app
  baseurl_source: declared
  description: Single-use WebSocket connect tickets (`wtk_…`) for the recorder / AI-preview sockets.
  name: usewrit-app Ws Ticket API
  slug: usewrit-app-ws-ticket-api
artifact_total: 33
common:
- group: agent
  href: https://artifacts.apis.io/usewrit-app/agentic-access/usewrit-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/usewrit-app-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/usewrit-app/plans/usewrit-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/usewrit-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/usewrit-app/rules/usewrit-app-rules.yml
  title: ''
  type: Spectral
  url: rules/usewrit-app-rules.yml
- group: design
  href: https://artifacts.apis.io/usewrit-app/json-ld/usewrit-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/usewrit-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/usewrit-app/vocabulary/usewrit-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/usewrit-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/usewrit-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/usewrit-app/data-model/usewrit-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/usewrit-app-data-model.yml
- group: operate
  href: https://artifacts.apis.io/usewrit-app/changelog/usewrit-app-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/usewrit-app-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://usewrit.app/trust/
- group: design
  href: https://artifacts.apis.io/usewrit-app/errors/usewrit-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/usewrit-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/usewrit-app/conformance/usewrit-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/usewrit-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/usewrit-app/llms/usewrit-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/usewrit-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/usewrit-app/mcp/usewrit-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/usewrit-app-mcp.yml
- group: auth
  href: https://artifacts.apis.io/usewrit-app/well-known/usewrit-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/usewrit-app-security.txt
- group: agent
  href: https://artifacts.apis.io/usewrit-app/well-known/usewrit-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/usewrit-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/usewrit-app/hosts/usewrit-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/usewrit-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/usewrit-app/vendors/usewrit-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/usewrit-app-vendors.yml
- group: build
  href: https://artifacts.apis.io/usewrit-app/packages/usewrit-app-packages.yml
  title: ''
  type: SDKs
  url: packages/usewrit-app-packages.yml
- group: build
  href: https://artifacts.apis.io/usewrit-app/packages/usewrit-app-packages.yml
  title: ''
  type: Packages
  url: packages/usewrit-app-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://usewrit.app/status
- group: auth
  title: ''
  type: Security
  url: https://usewrit.app/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://usewrit.app/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.usewrit.app
- group: auth
  href: https://artifacts.apis.io/usewrit-app/authentication/usewrit-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/usewrit-app-authentication.yml
- group: auth
  href: https://artifacts.apis.io/usewrit-app/security/usewrit-app-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/usewrit-app-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/usewrit-app/security/usewrit-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/usewrit-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/usewrit-app/security/usewrit-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usewrit-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usewrit.app/
- group: docs
  title: ''
  type: Documentation
  url: https://usewrit.app/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://usewrit.app/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://usewrit.app/docs/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://usewrit.app/contact/
- group: company
  title: ''
  type: Blog
  url: https://usewrit.app/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usewrit
- group: commercial
  title: ''
  type: Pricing
  url: https://usewrit.app/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://usewrit.app/signup
- group: operate
  title: ''
  type: Roadmap
  url: https://usewrit.app/roadmap/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usewrit.app/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usewrit.app/privacy/
created: '2026-10-31'
description: Writ turns any website into a secure, callable REST endpoint and MCP tool, allowing users to record tasks or describe needs, capture website workflows and network requests, run direct API calls when possible, and use browser execution when necessary, publishing results as REST APIs or MCP tools.
image: https://usewrit.app/icon-512.png
json_schemas:
- name: CrawlJob
  property_count: 33
  slug: usewrit-app-crawl-job
- name: Monitor
  property_count: 43
  slug: usewrit-app-monitor
- name: Persona
  property_count: 29
  slug: usewrit-app-persona
- name: PersonaWrite
  property_count: 20
  slug: usewrit-app-persona-write
- name: Workflow
  property_count: 55
  slug: usewrit-app-workflow
- name: WorkflowUpdate
  property_count: 34
  slug: usewrit-app-workflow-update
jsonld:
- class_count: 118
  name: Usewrit App Context
  property_count: 424
  slug: usewrit-app-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.usewrit.app requiring an API key.
  name: usewrit-app MCP Server
  slug: usewrit-app-mcp-yml
modified: '2026-10-31'
name: usewrit-app
nav: Providers
network: true
overview: 'usewrit-app publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, Automations API, Cloud API, and 14 more. Tagged areas include Automation, MCP, No-Code, and Software-as-a-Service.


  The usewrit-app catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  usewrit-app''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 32 more developer resources.'
plans:
- name: Usewrit App Plans Pricing
  plan_count: 4
  slug: usewrit-app-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: usewrit-app API Rules
  rule_count: 15
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 4
  slug: usewrit-app-rules
score:
  band: developing
  composite: 50.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -14.9
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 60.8
    developer_ergonomics: 43.5
    discoverability: 56.7
    operational_transparency: 26.3
  previous_composite: 65.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Usewrit App Authentication
  slug: usewrit-app-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Usewrit App Domain Security
  slug: usewrit-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Usewrit App Vulnerability Disclosure
  slug: usewrit-app-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Usewrit App Trust Center
  slug: usewrit-app-trust-center
  summary_line: GDPR
skill_count: 1
skills:
- name: get-agent-status
  slug: get-agent-status
slug: usewrit-app
tags:
- Automation
- MCP
- No-Code
- Software-as-a-Service
website: https://usewrit.app/
---
