---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Grabmail Io Agentic Access
  operation_count: 6
  slug: grabmail-io-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 1
apis:
- description: Disposable email API providing temporary inboxes, message retrieval and deletion via REST.
  name: GrabMail API
  slug: grabmail-api
- baseURL: https://grabmail.io
  baseurl_source: declared
  description: 'What an API key opens. A key follows its account''s plan on every call: on the free plan it counts the free allowance per account instead of per IP address; on a paid plan it removes the caps and opens'
  name: grabmail-io Account API
  slug: grabmail-io-account-api
- baseURL: https://grabmail.io
  baseurl_source: declared
  description: Read and empty a disposable inbox.
  name: grabmail-io Mailbox API
  slug: grabmail-io-mailbox-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/grabmail-io/agentic-access/grabmail-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/grabmail-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/grabmail-io/plans/grabmail-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/grabmail-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/grabmail-io/rules/grabmail-io-rules.yml
  title: ''
  type: Spectral
  url: rules/grabmail-io-rules.yml
- group: design
  href: https://artifacts.apis.io/grabmail-io/json-ld/grabmail-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/grabmail-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/grabmail-io/vocabulary/grabmail-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/grabmail-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/grabmail-io/data-model/grabmail-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/grabmail-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/grabmail-io/errors/grabmail-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/grabmail-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/grabmail-io/conformance/grabmail-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/grabmail-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/grabmail-io/llms/grabmail-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/grabmail-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/grabmail-io/mcp/grabmail-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/grabmail-io-mcp.yml
- group: other
  href: https://artifacts.apis.io/grabmail-io/hosts/grabmail-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/grabmail-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/grabmail-io/vendors/grabmail-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/grabmail-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/grabmail-io/authentication/grabmail-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/grabmail-io-authentication.yml
- group: auth
  href: https://artifacts.apis.io/grabmail-io/security/grabmail-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/grabmail-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://grabmail.io/
- group: docs
  title: ''
  type: Documentation
  url: https://grabmail.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://grabmail.io/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://grabmail.io/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://grabmail.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://grabmail.io/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://grabmail.io/legal/privacy
- group: operate
  title: ''
  type: Support
  url: https://grabmail.io/status
- group: company
  title: ''
  type: Blog
  url: https://grabmail.io/guides
created: '2026-10-30'
description: GrabMail.io provides free disposable email addresses with a simple REST API. Users can generate temporary inboxes, read messages, and delete them without registration. The service auto‑deletes emails after five days, offers custom domain support, and includes rate limits of 60 requests per minute for free users. It targets developers needing quick email verification in CI pipelines or testing environments.
image: https://grabmail.io/assets/img/og-card.png
jsonld:
- class_count: 5
  name: Grabmail Io Context
  property_count: 35
  slug: grabmail-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at grabmail.io.
  name: grabmail-io MCP Server
  slug: grabmail-io-mcp-yml
modified: '2026-10-30'
name: grabmail-io
nav: Providers
network: true
overview: 'grabmail-io publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Mailbox API, and 1 more. Tagged areas include Company, Email, and Developer Tools.


  The grabmail-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  grabmail-io''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, support, engineering blog, and 16 more developer resources.'
plans:
- name: Grabmail Io Plans Pricing
  plan_count: 4
  slug: grabmail-io-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: grabmail-io API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: grabmail-io-rules
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 60.8
    catalog_earned_first_party: 12.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 59.2
    developer_ergonomics: 29.8
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
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
screenshot: https://apis.io/screenshots/grabmail-io/grabmail-io-2026-11-03T133005.png
security:
- kind: authentication
  name: Grabmail Io Authentication
  slug: grabmail-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Grabmail Io Domain Security
  slug: grabmail-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: grabmail-io
tags:
- Company
- Email
- Developer Tools
website: https://grabmail.io/
---
