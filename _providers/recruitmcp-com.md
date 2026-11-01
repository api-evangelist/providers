---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: unknown
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 74.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 44
  human_in_the_loop: 3
  name: Recruitmcp Com Agentic Access
  operation_count: 85
  slug: recruitmcp-com-agentic-access
  summary_line: 85 operations · 44 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.recruitmcp.com
  baseurl_source: declared
  description: The workspace and API keys.
  name: recruitmcp-com Account API
  slug: recruitmcp-com-account-api
- baseURL: https://api.recruitmcp.com
  baseurl_source: declared
  description: Balance, usage, plans, checkout, and auto-refill.
  name: recruitmcp-com Billing API
  slug: recruitmcp-com-billing-api
- baseURL: https://api.recruitmcp.com
  baseurl_source: declared
  description: Known companies, and resolving a company name to a URL.
  name: recruitmcp-com Companies API
  slug: recruitmcp-com-companies-api
- baseURL: https://api.recruitmcp.com
  baseurl_source: declared
  description: Email and phone for a person, when you ask.
  name: recruitmcp-com Contacts API
  slug: recruitmcp-com-contacts-api
- baseURL: https://api.recruitmcp.com
  baseurl_source: declared
  description: 'One workspace per end customer: its own seen register, lists, and caps. Credits stay on the account.'
  name: recruitmcp-com Customers API
  slug: recruitmcp-com-customers-api
- baseURL: https://api.recruitmcp.com
  baseurl_source: declared
  description: Account events and signed webhook endpoints.
  name: recruitmcp-com Events API
  slug: recruitmcp-com-events-api
- baseURL: https://api.recruitmcp.com
  baseurl_source: declared
  description: Saved lists and the seen register.
  name: recruitmcp-com Lists API
  slug: recruitmcp-com-lists-api
- baseURL: https://api.recruitmcp.com
  baseurl_source: declared
  description: Erasure, suppression, cache deletion, and the public opt-out.
  name: recruitmcp-com Privacy API
  slug: recruitmcp-com-privacy-api
- baseURL: https://api.recruitmcp.com
  baseurl_source: declared
  description: Cached profiles, live profile fetches, a name and company match, and profile jobs.
  name: recruitmcp-com Profiles API
  slug: recruitmcp-com-profiles-api
- baseURL: https://api.recruitmcp.com
  baseurl_source: declared
  description: Search people, and look up places, areas, and filter ids.
  name: recruitmcp-com Search API
  slug: recruitmcp-com-search-api
artifact_total: 28
asyncapis:
- description: ''
  name: Recruitmcp Com Webhooks
  slug: recruitmcp-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/recruitmcp-com/agentic-access/recruitmcp-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/recruitmcp-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/recruitmcp-com/rate-limits/recruitmcp-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/recruitmcp-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/recruitmcp-com/plans/recruitmcp-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/recruitmcp-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/recruitmcp-com/rules/recruitmcp-com-rules.yml
  title: ''
  type: Spectral
  url: rules/recruitmcp-com-rules.yml
- group: design
  href: https://artifacts.apis.io/recruitmcp-com/json-ld/recruitmcp-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/recruitmcp-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/recruitmcp-com/vocabulary/recruitmcp-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/recruitmcp-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/recruitmcp-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/recruitmcp-com/asyncapi/recruitmcp-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/recruitmcp-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/recruitmcp-com/data-model/recruitmcp-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/recruitmcp-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/recruitmcp-com/changelog/recruitmcp-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/recruitmcp-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/recruitmcp-com/conventions/recruitmcp-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/recruitmcp-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/recruitmcp-com/conventions/recruitmcp-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/recruitmcp-com-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://recruitmcp.com/security
- group: auth
  href: https://artifacts.apis.io/recruitmcp-com/authentication/recruitmcp-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/recruitmcp-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/recruitmcp-com/scopes/recruitmcp-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/recruitmcp-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/recruitmcp-com/lifecycle/recruitmcp-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/recruitmcp-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/recruitmcp-com/errors/recruitmcp-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/recruitmcp-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/recruitmcp-com/conformance/recruitmcp-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/recruitmcp-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/recruitmcp-com/llms/recruitmcp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/recruitmcp-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/recruitmcp-com/mcp/recruitmcp-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/recruitmcp-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/recruitmcp-com/well-known/recruitmcp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/recruitmcp-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/recruitmcp-com/hosts/recruitmcp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/recruitmcp-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://recruitmcp.com/legal/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://recruitmcp.com/status
- group: auth
  title: ''
  type: Security
  url: https://recruitmcp.com/security
- group: start
  title: ''
  type: Sandbox
  url: https://recruitmcp.com/console/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://recruitmcp.com/legal/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://recruitmcp.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://recruitmcp.com/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/recruitmcp-com/security/recruitmcp-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/recruitmcp-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/recruitmcp-com/security/recruitmcp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/recruitmcp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://recruitmcp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://recruitmcp.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://recruitmcp.com/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://recruitmcp.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://recruitmcp.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://recruitmcp.com/app
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://recruitmcp.com/openapi.json
  - status: null
    url: https://api.recruitmcp.com/openapi.json
  - status: null
    url: https://mcp.recruitmcp.com/openapi.json
  - status: 401
    url: https://recruitmcp.com/mcp
  - status: 401
    url: https://api.recruitmcp.com/mcp
  - status: 401
    url: https://mcp.recruitmcp.com/mcp
  reason: partner-login
  state: gated
created: '2026-10-31'
description: RecruitMCP provides a recruiting data API and Managed Cloud Platform (MCP) that enables developers and agents to search for people, enrich candidate profiles, and retrieve company and contact information. The service offers searchable candidate data, email and phone enrichment, and integrates with AI assistants. It includes usage credits, preview mode, idempotency guarantees, and detailed error handling. The platform is accessible via a web console and RESTful endpoints, and is positioned as an alternative to traditional recruiting CRMs.
image: https://recruitmcp.com/og?title=RecruitMCP
json_schemas:
- name: ContactsLookup
  property_count: 9
  slug: recruitmcp-com-contacts-lookup
- name: Contacts
  property_count: 5
  slug: recruitmcp-com-contacts
- name: Job
  property_count: 12
  slug: recruitmcp-com-job
- name: PeopleSearchPage
  property_count: 10
  slug: recruitmcp-com-people-search-page
- name: Profile
  property_count: 17
  slug: recruitmcp-com-profile
- name: Workspace
  property_count: 17
  slug: recruitmcp-com-workspace
jsonld:
- class_count: 66
  name: Recruitmcp Com Context
  property_count: 211
  slug: recruitmcp-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at recruitmcp.com.
  name: recruitmcp-com MCP Server
  slug: recruitmcp-com-mcp-yml
modified: '2026-10-31'
name: recruitmcp-com
nav: Providers
network: true
overview: 'recruitmcp-com publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Billing API, Companies API, and 7 more. Tagged areas include Company, Recruitment, API, MCP, and HR.


  The recruitmcp-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  recruitmcp-com''s developer surface includes changelog, authentication, sandbox, getting-started guide, documentation, API reference, pricing, and 30 more developer resources.'
plans:
- name: Recruitmcp Com Plans Pricing
  plan_count: 1
  slug: recruitmcp-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Recruitmcp Com Rate Limits
  slug: recruitmcp-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: recruitmcp-com API Rules
  rule_count: 18
  severity_counts:
    error: 14
    hint: 0
    info: 2
    warn: 2
  slug: recruitmcp-com-rules
scopes:
- name: Recruitmcp Com Scopes
  scope_count: 0
  slug: recruitmcp-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 75.6
  coverage:
    artifact_dirs: 30
    catalog_earned: 92.1
    catalog_earned_first_party: 0.0
    catalog_gap: 22.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 79.5
    contract_governance: 79.1
    contract_quality: 73.5
    developer_ergonomics: 63.6
    discoverability: 65.0
    operational_transparency: 68.9
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
  name: Recruitmcp Com Authentication
  slug: recruitmcp-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Recruitmcp Com Domain Security
  slug: recruitmcp-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Recruitmcp Com Trust Center
  slug: recruitmcp-com-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 1
skills:
- name: workspace
  slug: recruitmcp-com-workspace
slug: recruitmcp-com
tags:
- Company
- Recruitment
- API
- MCP
- HR
website: https://recruitmcp.com/
---
