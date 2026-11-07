---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Mailprobe Dev Agentic Access
  operation_count: 2
  slug: mailprobe-dev-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- baseURL: https://mailprobe.dev
  baseurl_source: declared
  description: Credit balance
  name: mailprobe-dev Account API
  slug: mailprobe-dev-account-api
- baseURL: https://mailprobe.dev
  baseurl_source: declared
  description: Email address verification
  name: mailprobe-dev Verification API
  slug: mailprobe-dev-verification-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/mailprobe-dev/agentic-access/mailprobe-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mailprobe-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/mailprobe-dev/plans/mailprobe-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mailprobe-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/mailprobe-dev/rules/mailprobe-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/mailprobe-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/mailprobe-dev/json-ld/mailprobe-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mailprobe-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/mailprobe-dev/vocabulary/mailprobe-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mailprobe-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/mailprobe-dev/data-model/mailprobe-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mailprobe-dev-data-model.yml
- group: auth
  href: https://artifacts.apis.io/mailprobe-dev/authentication/mailprobe-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mailprobe-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/mailprobe-dev/errors/mailprobe-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mailprobe-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mailprobe-dev/conformance/mailprobe-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mailprobe-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mailprobe-dev/llms/mailprobe-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mailprobe-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/mailprobe-dev/mcp/mailprobe-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mailprobe-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/mailprobe-dev/well-known/mailprobe-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mailprobe-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/mailprobe-dev/hosts/mailprobe-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mailprobe-dev-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mailprobe.dev/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mailprobe.dev/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://mailprobe.dev/pricing/
- group: start
  title: ''
  type: Login
  url: https://mailprobe.dev/login/
- group: company
  title: ''
  type: Blog
  url: https://mailprobe.dev/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://mailprobe.dev/api-docs/#mcp
- group: docs
  title: ''
  type: APIReference
  url: https://mailprobe.dev/api-docs/
- group: auth
  href: https://artifacts.apis.io/mailprobe-dev/security/mailprobe-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mailprobe-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mailprobe.dev/
created: '2026-10-30'
description: MailProbe.dev provides a real-time email verification API that checks the deliverability of email addresses, detects disposable, role-based, and typo-squatted emails. It offers developers a simple RESTful interface to validate user inputs, improve inbox placement, and reduce bounce rates for transactional communications. The service includes detailed response codes, confidence scores, and optional bulk verification, supporting integration across web, mobile, and enterprise applications.
image: https://mailprobe.dev/og-image.png
json_schemas:
- name: Credits
  property_count: 1
  slug: mailprobe-dev-credits
- name: VerifyEntry
  property_count: 0
  slug: mailprobe-dev-verify-entry
- name: VerifyRequest
  property_count: 2
  slug: mailprobe-dev-verify-request
jsonld:
- class_count: 5
  name: Mailprobe Dev Context
  property_count: 22
  slug: mailprobe-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at mailprobe.dev requiring an API key.
  name: mailprobe-dev MCP Server
  slug: mailprobe-dev-mcp-yml
modified: '2026-10-30'
name: mailprobe-dev
nav: Providers
network: true
overview: 'mailprobe-dev publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Account API and Verification API. Tagged areas include Company, Email Verification, Real-Time, and Developer Tools.


  The mailprobe-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  mailprobe-dev''s developer surface includes authentication, pricing, engineering blog, getting-started guide, API reference, and 17 more developer resources.'
plans:
- name: Mailprobe Dev Plans Pricing
  plan_count: 5
  slug: mailprobe-dev-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: mailprobe-dev API Rules
  rule_count: 53
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 1
  slug: mailprobe-dev-rules
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 66.0
    developer_ergonomics: 22.6
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 50.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mailprobe-dev/mailprobe-dev-2026-11-03T135245.png
security:
- kind: authentication
  name: Mailprobe Dev Authentication
  slug: mailprobe-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mailprobe Dev Domain Security
  slug: mailprobe-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: mailprobe-dev
tags:
- Company
- Email Verification
- Real-Time
- Developer Tools
website: https://mailprobe.dev/
---
