---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Markifact Com Agentic Access
  operation_count: 11
  slug: markifact-com-agentic-access
  summary_line: 11 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.markifact.com
  baseurl_source: declared
  description: The Connections API from markifact-com — 5 operation(s) for connections.
  name: markifact-com Connections API
  slug: markifact-com-connections-api
- baseURL: https://api.markifact.com
  baseurl_source: declared
  description: The Credits API from markifact-com — 2 operation(s) for credits.
  name: markifact-com Credits API
  slug: markifact-com-credits-api
- baseURL: https://api.markifact.com
  baseurl_source: declared
  description: The Logs API from markifact-com — 2 operation(s) for logs.
  name: markifact-com Logs API
  slug: markifact-com-logs-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/markifact-com/agentic-access/markifact-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/markifact-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/markifact-com/plans/markifact-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/markifact-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/markifact-com/rules/markifact-com-rules.yml
  title: ''
  type: Spectral
  url: rules/markifact-com-rules.yml
- group: design
  href: https://artifacts.apis.io/markifact-com/json-ld/markifact-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/markifact-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/markifact-com/vocabulary/markifact-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/markifact-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/markifact-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/markifact-com/data-model/markifact-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/markifact-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/markifact-com/changelog/markifact-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/markifact-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/markifact-com/authentication/markifact-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/markifact-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/markifact-com/errors/markifact-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/markifact-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/markifact-com/conformance/markifact-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/markifact-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/markifact-com/llms/markifact-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/markifact-com-llms.txt
- group: other
  href: https://artifacts.apis.io/markifact-com/a2a/markifact-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/markifact-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/markifact-com/well-known/markifact-com-platform-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/markifact-com-platform-security.txt
- group: agent
  href: https://artifacts.apis.io/markifact-com/well-known/markifact-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/markifact-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/markifact-com/hosts/markifact-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/markifact-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/markifact-com/vendors/markifact-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/markifact-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.markifact.com/trust-center
- group: start
  title: ''
  type: Login
  url: https://www.markifact.com/auth/signin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/markifact
- group: auth
  href: https://artifacts.apis.io/markifact-com/security/markifact-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/markifact-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.markifact.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.markifact.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.markifact.com/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.markifact.com/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://www.markifact.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.markifact.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.markifact.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.markifact.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.markifact.com/terms-conditions
- group: operate
  title: ''
  type: Changelog
  url: https://www.markifact.com/changelog
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://docs.markifact.com/openapi.json
  - status: null
    url: https://docs.markifact.com/mcp
  - status: 401
    url: https://api.markifact.com/mcp
  - status: 200
    url: https://markifact.com/
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Markifact provides AI-driven marketing automation platform that enables marketers to create, analyze, and automate campaigns across multiple channels. Leveraging large language models, Markifact offers agents and workflows to generate ad creatives, produce performance reports, and integrate with advertising platforms like Google and Meta. The service includes a marketplace of pre-built templates, white‑label connections, and a credit‑based usage model, targeting enterprises and agencies seeking scalable AI marketing solutions.
image: https://www.markifact.com/images/og-image.webp
json_schemas:
- name: AuthLinkStatus
  property_count: 10
  slug: markifact-com-auth-link-status
- name: ConnectionType
  property_count: 5
  slug: markifact-com-connection-type
- name: CreateAuthLinkRequest
  property_count: 4
  slug: markifact-com-create-auth-link-request
- name: CreateConnectionRequest
  property_count: 4
  slug: markifact-com-create-connection-request
- name: CreditBalance
  property_count: 5
  slug: markifact-com-credit-balance
- name: Log
  property_count: 13
  slug: markifact-com-log
jsonld:
- class_count: 15
  name: Markifact Com Context
  property_count: 42
  slug: markifact-com-context
layout: provider
modified: '2026-10-29'
name: markifact-com
nav: Providers
network: true
overview: 'markifact-com publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Connections API, Credits API, and Logs API. Tagged areas include AI Marketing Automation, Ad Management, Reporting, Workflow Automation, and Marketing Operations.


  The markifact-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  markifact-com''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, engineering blog, and 24 more developer resources.'
plans:
- name: Markifact Com Plans Pricing
  plan_count: 2
  slug: markifact-com-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Markifact Com Rate Limits
  slug: markifact-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: markifact-com API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: markifact-com-rules
scopes:
- name: Markifact Com Scopes
  scope_count: 0
  slug: markifact-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 57.7
  coverage:
    artifact_dirs: 30
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.7
    contract_governance: 22.0
    contract_quality: 64.4
    developer_ergonomics: 49.4
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Markifact Com Authentication
  slug: markifact-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Markifact Com Domain Security
  slug: markifact-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: list-connections
  slug: list-connections
- name: markifact-com-create-and-list-connections
  slug: markifact-com-create-and-list-connections
slug: markifact-com
tags:
- AI Marketing Automation
- Ad Management
- Reporting
- Workflow Automation
- Marketing Operations
- Data Integration
website: https://www.markifact.com/
---
