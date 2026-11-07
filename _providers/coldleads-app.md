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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Coldleads App Agentic Access
  operation_count: 15
  slug: coldleads-app-agentic-access
  summary_line: 15 operations · 5 acting
api_count: 1
apis:
- baseURL: https://coldleads.app/api/v1
  baseurl_source: declared
  description: The Activity API from Cold Leads — 1 operation(s) for activity.
  name: Cold Leads Activity API
  slug: coldleads-app-activity-api
- baseURL: https://coldleads.app/api/v1
  baseurl_source: declared
  description: The Credits API from Cold Leads — 1 operation(s) for credits.
  name: Cold Leads Credits API
  slug: coldleads-app-credits-api
- baseURL: https://coldleads.app/api/v1
  baseurl_source: declared
  description: The Find API from Cold Leads — 1 operation(s) for find.
  name: Cold Leads Find API
  slug: coldleads-app-find-api
- baseURL: https://coldleads.app/api/v1
  baseurl_source: declared
  description: The Follow Ups API from Cold Leads — 1 operation(s) for follow ups.
  name: Cold Leads Follow Ups API
  slug: coldleads-app-follow-ups-api
- baseURL: https://coldleads.app/api/v1
  baseurl_source: declared
  description: The Leads API from Cold Leads — 2 operation(s) for leads.
  name: Cold Leads Leads API
  slug: coldleads-app-leads-api
- baseURL: https://coldleads.app/api/v1
  baseurl_source: declared
  description: The Next Actions API from Cold Leads — 1 operation(s) for next actions.
  name: Cold Leads Next Actions API
  slug: coldleads-app-next-actions-api
- baseURL: https://coldleads.app/api/v1
  baseurl_source: declared
  description: The Social API from Cold Leads — 5 operation(s) for social.
  name: Cold Leads Social API
  slug: coldleads-app-social-api
- baseURL: https://coldleads.app/api/v1
  baseurl_source: declared
  description: The Verify API from Cold Leads — 3 operation(s) for verify.
  name: Cold Leads Verify API
  slug: coldleads-app-verify-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/coldleads-app/agentic-access/coldleads-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/coldleads-app-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/coldleads-app/rules/coldleads-app-rules.yml
  title: ''
  type: Spectral
  url: rules/coldleads-app-rules.yml
- group: design
  href: https://artifacts.apis.io/coldleads-app/json-ld/coldleads-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/coldleads-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/coldleads-app/vocabulary/coldleads-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/coldleads-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/coldleads-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/coldleads-app/data-model/coldleads-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/coldleads-app-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://coldleads.app/security
- group: design
  href: https://artifacts.apis.io/coldleads-app/errors/coldleads-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/coldleads-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/coldleads-app/conformance/coldleads-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coldleads-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/coldleads-app/llms/coldleads-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coldleads-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/coldleads-app/mcp/coldleads-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/coldleads-app-mcp.yml
- group: auth
  href: https://artifacts.apis.io/coldleads-app/well-known/coldleads-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coldleads-app-security.txt
- group: agent
  href: https://artifacts.apis.io/coldleads-app/well-known/coldleads-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coldleads-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/coldleads-app/hosts/coldleads-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coldleads-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/coldleads-app/vendors/coldleads-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coldleads-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coldleads.app/terms
- group: operate
  title: ''
  type: Support
  url: https://coldleads.app/help
- group: auth
  title: ''
  type: Security
  url: https://coldleads.app/security
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@coldleads/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coldleads.app/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://coldleads.app/help/plans-and-billing
- group: start
  title: ''
  type: Login
  url: https://coldleads.app/login
- group: start
  title: ''
  type: GettingStarted
  url: https://coldleads.app/help/getting-started
- group: company
  title: ''
  type: Blog
  url: https://blog.coldleads.app/
- group: docs
  title: ''
  type: APIReference
  url: https://coldleads.app/developers
- group: auth
  href: https://artifacts.apis.io/coldleads-app/authentication/coldleads-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/coldleads-app-authentication.yml
- group: auth
  href: https://artifacts.apis.io/coldleads-app/security/coldleads-app-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/coldleads-app-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/coldleads-app/security/coldleads-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/coldleads-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/coldleads-app/security/coldleads-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coldleads-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coldleads.app/
created: '2026-11-04'
description: Cold Leads provides a simple CRM platform for small businesses, turning website visitors and cold contacts into paying clients. It aggregates enquiries from websites into a single place, offers verified B2B lists, enables personal email campaigns from the user’s own mailbox, and supports multilingual communication in Czech, Ukrainian, German, Spanish, and English. Pricing starts at $19 per month with a cancel‑anytime policy, making it accessible for startups and growing teams.
image: https://coldleads.app/og?p=%2F&l=en&v=2
json_schemas:
- name: LeadContext
  property_count: 5
  slug: coldleads-app-lead-context
- name: NextAction
  property_count: 15
  slug: coldleads-app-next-action
- name: VerifyResult
  property_count: 10
  slug: coldleads-app-verify-result
jsonld:
- class_count: 3
  name: Coldleads App Context
  property_count: 29
  slug: coldleads-app-context
layout: provider
mcp_servers:
- description: Remote MCP server at coldleads.app requiring OAuth.
  name: Cold Leads MCP Server
  slug: coldleads-app-mcp-yml
modified: '2026-11-04'
name: Cold Leads
nav: Providers
network: true
overview: 'Cold Leads publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activity API, Credits API, Find API, and 5 more. Tagged areas include CRM, Software-as-a-Service, Small Business, Lead Management, and Cold Leads.


  The Cold Leads catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cold Leads'' developer surface includes support, pricing, getting-started guide, engineering blog, API reference, authentication, and 24 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Cold Leads API Rules
  rule_count: 44
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 1
  slug: coldleads-app-rules
score:
  band: developing
  composite: 51.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 35.6
    contract_quality: 55.6
    developer_ergonomics: 47.0
    discoverability: 71.7
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Coldleads App Authentication
  slug: coldleads-app-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Coldleads App Domain Security
  slug: coldleads-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Coldleads App Vulnerability Disclosure
  slug: coldleads-app-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Coldleads App Trust Center
  slug: coldleads-app-trust-center
  summary_line: PCI DSS, GDPR
skill_count: 1
skills:
- name: coldleads-app-verify-email-list
  slug: coldleads-app-verify-email-list
slug: coldleads-app
tags:
- CRM
- Software-as-a-Service
- Small Business
- Lead Management
- Cold Leads
website: https://coldleads.app/
---
