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
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.4
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 45
  human_in_the_loop: 17
  name: Auphonic Agentic Access
  operation_count: 60
  slug: auphonic-agentic-access
  summary_line: 60 operations · 45 acting · 17 human-in-the-loop
api_count: 1
apis:
- baseURL: https://auphonic.com
  baseurl_source: spec
  description: Query available formats, algorithms and service types. See the [Info API documentation](https://auphonic.com/help/api/query.html) for details.
  name: Auphonic Info API
  slug: auphonic-info-api
- baseURL: https://auphonic.com
  baseurl_source: spec
  description: 'Create and manage production presets (templates). Presets can be **Singletrack** or **Multitrack** — each mode has different algorithm parameters. **Use the dropdown selector in the schemas to switch '
  name: Auphonic Presets API
  slug: auphonic-presets-api
- baseURL: https://auphonic.com
  baseurl_source: spec
  description: 'Create, manage and process audio productions. Productions can be **Singletrack** or **Multitrack** — each mode has different algorithm parameters. When viewing the request/response schemas, **use the '
  name: Auphonic Productions API
  slug: auphonic-productions-api
- baseURL: https://auphonic.com
  baseurl_source: spec
  description: Manage external service integrations. See the [External Services documentation](https://auphonic.com/help/api/query.html#external-services) for details.
  name: Auphonic Services API
  slug: auphonic-services-api
- baseURL: https://auphonic.com
  baseurl_source: spec
  description: Simplified **singletrack** production creation in a single multipart/form-data request. Only singletrack productions can be created with the Simple API. See the [Simple API documentation](https://auph
  name: Auphonic Simple API
  slug: auphonic-simple-api-api
- baseURL: https://auphonic.com
  baseurl_source: spec
  description: User account information. See the [User API documentation](https://auphonic.com/help/api/query.html#user-account-info) for details.
  name: Auphonic User API
  slug: auphonic-user-api
artifact_total: 20
asyncapis:
- description: ''
  name: Auphonic Webhooks
  slug: auphonic-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/auphonic/refs/heads/main/agentic-access/auphonic-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/auphonic-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/auphonic/refs/heads/main/rules/auphonic-rules.yml
  title: ''
  type: Spectral
  url: rules/auphonic-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/auphonic/refs/heads/main/json-ld/auphonic-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/auphonic-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/auphonic/refs/heads/main/vocabulary/auphonic-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/auphonic-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/auphonic/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/auphonic/refs/heads/main/asyncapi/auphonic-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/auphonic-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/auphonic/refs/heads/main/data-model/auphonic-data-model.yml
  title: ''
  type: DataModel
  url: data-model/auphonic-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/auphonic/refs/heads/main/cli/auphonic-cli.yml
  title: ''
  type: CLI
  url: cli/auphonic-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/auphonic/refs/heads/main/changelog/auphonic-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/auphonic-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/auphonic/refs/heads/main/authentication/auphonic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/auphonic-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/auphonic/refs/heads/main/errors/auphonic-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/auphonic-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/auphonic/refs/heads/main/conformance/auphonic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/auphonic-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/auphonic/refs/heads/main/llms/auphonic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/auphonic-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/auphonic/refs/heads/main/hosts/auphonic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auphonic-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/auphonic/refs/heads/main/packages/auphonic-packages.yml
  title: ''
  type: SDKs
  url: packages/auphonic-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/auphonic/refs/heads/main/packages/auphonic-packages.yml
  title: ''
  type: Packages
  url: packages/auphonic-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://auphonic.com/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://auphonic.com/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/auphonic
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/auphonic/refs/heads/main/scopes/auphonic-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/auphonic-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/auphonic/refs/heads/main/security/auphonic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auphonic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://auphonic.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://auphonic.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://auphonic.com/help/
- group: docs
  title: ''
  type: APIReference
  url: https://auphonic.com/help/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://auphonic.com/landing
- group: company
  title: ''
  type: Blog
  url: https://auphonic.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://auphonic.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://auphonic.com/accounts/register/
- group: start
  title: ''
  type: Login
  url: https://auphonic.com/accounts/login/
- group: operate
  title: ''
  type: Support
  url: https://auphonic.com/help/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://auphonic.com/impressum
- group: commercial
  title: ''
  type: TermsOfService
  url: https://auphonic.com/impressum
created: '2026-10-13'
description: Auphonic provides an AI‑powered audio post‑production platform that automates tasks such as noise reduction, loudness normalization, speech‑to‑text, and multi‑track mixing. It serves podcasters, educators, video creators, and audiobook producers, offering both a web UI and a robust API for automated workflows, integrations with cloud storage, publishing platforms, and custom processing pipelines.
json_schemas:
- name: MultiInputFileRequest
  property_count: 9
  slug: auphonic-multi-input-file-request
- name: OutgoingService
  property_count: 28
  slug: auphonic-outgoing-service
- name: OutputFileRequest
  property_count: 9
  slug: auphonic-output-file-request
- name: ServiceAccount
  property_count: 20
  slug: auphonic-service-account
- name: SpeechRecognitionRequest
  property_count: 7
  slug: auphonic-speech-recognition-request
- name: User
  property_count: 15
  slug: auphonic-user
jsonld:
- class_count: 33
  name: Auphonic Context
  property_count: 210
  slug: auphonic-context
layout: provider
modified: '2026-10-13'
name: Auphonic
nav: Providers
network: true
overview: 'Auphonic publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Info API, Presets API, Productions API, and 3 more. Tagged areas include Audio, Podcasts, Artificial Intelligence, Automation, and Media.


  The Auphonic catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Auphonic''s developer surface includes CLI, changelog, authentication, documentation, API reference, getting-started guide, engineering blog, and 26 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 0
  name: Auphonic Rate Limits
  slug: auphonic-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Auphonic API Rules
  rule_count: 16
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 4
  slug: auphonic-rules
scopes:
- name: Auphonic Scopes
  scope_count: 0
  slug: auphonic-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 58.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 35.6
    contract_quality: 65.6
    developer_ergonomics: 73.2
    discoverability: 62.5
    operational_transparency: 28.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 22.2
security:
- kind: authentication
  name: Auphonic Authentication
  slug: auphonic-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Auphonic Domain Security
  slug: auphonic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: auphonic
tags:
- Audio
- Podcasts
- Artificial Intelligence
- Automation
- Media
website: https://auphonic.com
---
