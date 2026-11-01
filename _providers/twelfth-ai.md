---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 56.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Twelfth Ai Agentic Access
  operation_count: 2
  slug: twelfth-ai-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: https://api.twelfth.ai
  baseurl_source: declared
  description: The Tasks API from twelfth-ai — 1 operation(s) for tasks.
  name: twelfth-ai Tasks API
  slug: twelfth-ai-tasks-api
- baseURL: https://api.twelfth.ai
  baseurl_source: declared
  description: The Workspace API from twelfth-ai — 1 operation(s) for workspace.
  name: twelfth-ai Workspace API
  slug: twelfth-ai-workspace-api
artifact_total: 12
asyncapis:
- description: ''
  name: Twelfth Ai Webhooks
  slug: twelfth-ai-webhooks
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://twelfth.ai/docs/settings/pricing/
- group: agent
  href: https://artifacts.apis.io/twelfth-ai/agentic-access/twelfth-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/twelfth-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/twelfth-ai/rules/twelfth-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/twelfth-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/twelfth-ai/json-ld/twelfth-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/twelfth-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/twelfth-ai/vocabulary/twelfth-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/twelfth-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/twelfth-ai/asyncapi/twelfth-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/twelfth-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/twelfth-ai/data-model/twelfth-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/twelfth-ai-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.twelfth.ai/
- group: auth
  href: https://artifacts.apis.io/twelfth-ai/security/twelfth-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/twelfth-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/twelfth-ai/authentication/twelfth-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/twelfth-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/twelfth-ai/errors/twelfth-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/twelfth-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/twelfth-ai/conformance/twelfth-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/twelfth-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/twelfth-ai/llms/twelfth-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/twelfth-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/twelfth-ai/well-known/twelfth-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/twelfth-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/twelfth-ai/well-known/twelfth-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/twelfth-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/twelfth-ai/hosts/twelfth-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/twelfth-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/twelfth-ai/vendors/twelfth-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/twelfth-ai-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.twelfth.ai/
- group: company
  title: ''
  type: Newsroom
  url: https://twelfth.ai/news
- group: start
  title: ''
  type: Login
  url: https://twelfth.ai/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trust-center
- group: docs
  title: ''
  type: APIReference
  url: https://twelfth.ai/docs/developers/reference/
- group: auth
  href: https://artifacts.apis.io/twelfth-ai/security/twelfth-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/twelfth-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/twelfth-ai/security/twelfth-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/twelfth-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/twelfth-ai/security/twelfth-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/twelfth-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://twelfth.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://twelfth.ai/docs/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://twelfth.ai/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://twelfth.ai/docs/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://twelfth.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://twelfth.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://twelfth.ai/legals/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://twelfth.ai/legals/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://twelfth.ai/openapi.json
  - status: 401
    url: https://api.twelfth.ai/mcp
  - status: 401
    url: https://status.twelfth.ai/api/graphql
  - status: 401
    url: https://status.twelfth.ai/api/mcp
  - status: 200
    url: https://twelfth.ai/
  reason: partner-login
  state: gated
created: '2026-10-20'
description: Twelfth.ai provides a commercial workspace platform for retail and category teams, integrating pricing, range, promotion, and supplier signals into a unified view. It helps teams make better commercial decisions by ranking priorities, preserving evidence, and streamlining actions. The solution offers forecasting, pricing insights, and collaborative tools to improve retail performance and decision-making across the organization.
image: https://twelfth.ai/brand/og-image.png
json_schemas:
- name: TasksResponse
  property_count: 1
  slug: twelfth-ai-tasks-response
- name: WorkspaceResponse
  property_count: 1
  slug: twelfth-ai-workspace-response
jsonld:
- class_count: 5
  name: Twelfth Ai Context
  property_count: 23
  slug: twelfth-ai-context
layout: provider
modified: '2026-10-20'
name: twelfth-ai
nav: Providers
network: true
overview: 'twelfth-ai publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Tasks API and Workspace API. Tagged areas include Company, Retail, Commerce, AI, and Workspace.


  The twelfth-ai catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  twelfth-ai''s developer surface includes pricing, authentication, API reference, documentation, getting-started guide, support, engineering blog, and 26 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: twelfth-ai API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: twelfth-ai-rules
score:
  band: strong
  composite: 59.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 22.0
    contract_quality: 74.6
    developer_ergonomics: 57.1
    discoverability: 67.9
    operational_transparency: 39.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Twelfth Ai Authentication
  slug: twelfth-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Twelfth Ai Domain Security
  slug: twelfth-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Twelfth Ai Vulnerability Disclosure
  slug: twelfth-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Twelfth Ai Trust Center
  slug: twelfth-ai-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: twelfth-ai
tags:
- Company
- Retail
- Commerce
- AI
- Workspace
website: https://twelfth.ai/
---
