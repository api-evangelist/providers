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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Dovemails Com Agentic Access
  operation_count: 3
  slug: dovemails-com-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- baseURL: https://app.dovemails.com
  baseurl_source: declared
  description: The Send API from dovemails-com — 2 operation(s) for send.
  name: dovemails-com Send API
  slug: dovemails-com-send-api
- baseURL: https://app.dovemails.com
  baseurl_source: declared
  description: The Status API from dovemails-com — 1 operation(s) for status.
  name: dovemails-com Status API
  slug: dovemails-com-status-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/dovemails-com/data-model/dovemails-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dovemails-com-data-model.yml
- group: agent
  href: https://artifacts.apis.io/dovemails-com/agentic-access/dovemails-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dovemails-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/dovemails-com/rules/dovemails-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dovemails-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dovemails-com/vocabulary/dovemails-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dovemails-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dovemails-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dovemails-com/conventions/dovemails-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/dovemails-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/dovemails-com/conventions/dovemails-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dovemails-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/dovemails-com/authentication/dovemails-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dovemails-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/dovemails-com/lifecycle/dovemails-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dovemails-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/dovemails-com/errors/dovemails-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dovemails-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dovemails-com/conformance/dovemails-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dovemails-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dovemails-com/llms/dovemails-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dovemails-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dovemails-com/mcp/dovemails-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dovemails-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dovemails-com/well-known/dovemails-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dovemails-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dovemails-com/hosts/dovemails-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dovemails-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dovemails-com/vendors/dovemails-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dovemails-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/dovemails-com/packages/dovemails-com-packages.yml
  title: ''
  type: SDKs
  url: packages/dovemails-com-packages.yml
- group: build
  href: https://artifacts.apis.io/dovemails-com/packages/dovemails-com-packages.yml
  title: ''
  type: Packages
  url: packages/dovemails-com-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://dovemails.com/trust/
- group: auth
  href: https://artifacts.apis.io/dovemails-com/security/dovemails-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dovemails-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dovemails.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dovemails.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://dovemails.com/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://dovemails.com/docs/quickstart.html
- group: start
  title: ''
  type: SignUp
  url: https://app.dovemails.com/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dovemails.com/#privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://app.dovemails.com/openapi.json
  - status: 401
    url: https://app.dovemails.com/mcp
  - status: 200
    url: https://dovemails.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Dovemails is a hosted email platform offering a unified API for transactional email, newsletters, and marketing campaigns. It provides drop‑in endpoints compatible with Postmark, Mailgun, and Resend, supports SMTP on port 587, delivers messages via Dovemails' own mail servers with SPF, DKIM, DMARC, and MTA‑STS, and includes signed webhooks for event notifications. The service includes a dashboard for team‑managed mail, DNS setup guides, and SDKs for multiple languages, enabling developers to send mail programmatically while the provider handles infrastructure and deliverability.
image: https://dovemails.com/logo-mark-256.png
json_schemas:
- name: Health
  property_count: 0
  slug: dovemails-com-health
- name: SendRequest
  property_count: 0
  slug: dovemails-com-send-request
- name: SendResult
  property_count: 0
  slug: dovemails-com-send-result
layout: provider
mcp_servers:
- description: Remote MCP server at app.dovemails.com.
  name: dovemails-com MCP Server
  slug: dovemails-com-mcp-yml
modified: '2026-10-30'
name: dovemails-com
nav: Providers
network: true
overview: 'dovemails-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Send API and Status API. Tagged areas include Company, Email, Software-as-a-Service, and Marketing.


  The dovemails-com catalog on APIs.io includes 1 Spectral governance ruleset.


  dovemails-com''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, and 21 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 73
  extends:
  - spectral:oas
  name: dovemails-com API Rules
  rule_count: 32
  severity_counts:
    error: 30
    hint: 0
    info: 1
    warn: 1
  slug: dovemails-com-rules
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 46.8
    catalog_earned_first_party: 0.0
    catalog_gap: 68.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 15.8
    contract_governance: 35.6
    contract_quality: 44.1
    developer_ergonomics: 39.8
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/dovemails-com/dovemails-com-2026-11-03T131001.png
security:
- kind: authentication
  name: Dovemails Com Authentication
  slug: dovemails-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dovemails Com Domain Security
  slug: dovemails-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: send-email
  slug: dovemails-com-send-email
slug: dovemails-com
tags:
- Company
- Email
- Software-as-a-Service
- Marketing
website: https://dovemails.com/
---
