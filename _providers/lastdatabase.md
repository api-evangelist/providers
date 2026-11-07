---
access_model:
  confidence: high
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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 58.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Lastdatabase Agentic Access
  operation_count: 1
  slug: lastdatabase-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: 'OAuth-protected remote Model Context Protocol server at https://lastdatabase.com/mcp exposing four scope-gated tools: search_people (non-charging masked B2B contact search), unlock_people (entitlement'
  name: LastDatabase MCP Server
  slug: mcp-server
- baseURL: https://lastdatabase.com/mcp
  baseurl_source: declared
  description: Search supported LastDatabase lead inventory.
  name: LastDatabase Leads API
  slug: lastdatabase-leads-api
artifact_total: 16
common:
- group: other
  href: https://artifacts.apis.io/lastdatabase/capabilities/lastdatabase-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/lastdatabase-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/lastdatabase/overlays/lastdatabase-lead-search-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lastdatabase-lead-search-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/lastdatabase/agentic-access/lastdatabase-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lastdatabase-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/lastdatabase/rate-limits/lastdatabase-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lastdatabase-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/lastdatabase/plans/lastdatabase-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lastdatabase-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/lastdatabase/rules/lastdatabase-rules.yml
  title: ''
  type: Spectral
  url: rules/lastdatabase-rules.yml
- group: design
  href: https://artifacts.apis.io/lastdatabase/json-ld/lastdatabase-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lastdatabase-context.jsonld
- group: design
  href: https://artifacts.apis.io/lastdatabase/vocabulary/lastdatabase-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lastdatabase-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/lastdatabase/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/lastdatabase/data-model/lastdatabase-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lastdatabase-data-model.yml
- group: design
  href: https://artifacts.apis.io/lastdatabase/conventions/lastdatabase-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lastdatabase-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://lastdatabase.com/trust-center
- group: auth
  href: https://artifacts.apis.io/lastdatabase/scopes/lastdatabase-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/lastdatabase-scopes.yml
- group: design
  href: https://artifacts.apis.io/lastdatabase/errors/lastdatabase-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/lastdatabase-error-codes.yml
- group: design
  href: https://artifacts.apis.io/lastdatabase/errors/lastdatabase-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lastdatabase-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lastdatabase/conformance/lastdatabase-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lastdatabase-conformance.yml
- group: agent
  href: https://artifacts.apis.io/lastdatabase/llms/lastdatabase-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lastdatabase-llms.txt
- group: build
  href: https://artifacts.apis.io/lastdatabase/mcp/lastdatabase-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/lastdatabase-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/lastdatabase/mcp/lastdatabase-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lastdatabase-mcp.yml
- group: agent
  href: https://artifacts.apis.io/lastdatabase/well-known/lastdatabase-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lastdatabase-well-known.yml
- group: other
  href: https://artifacts.apis.io/lastdatabase/hosts/lastdatabase-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lastdatabase-hosts.yml
- group: other
  href: https://artifacts.apis.io/lastdatabase/vendors/lastdatabase-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lastdatabase-vendors.yml
- group: auth
  href: https://artifacts.apis.io/lastdatabase/authentication/lastdatabase-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lastdatabase-authentication.yml
- group: auth
  href: https://artifacts.apis.io/lastdatabase/security/lastdatabase-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/lastdatabase-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/lastdatabase/security/lastdatabase-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lastdatabase-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lastdatabase.com/
- group: docs
  title: ''
  type: Documentation
  url: https://lastdatabase.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://lastdatabase.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://lastdatabase.com/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://lastdatabase.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://lastdatabase.com/blog
- group: operate
  title: ''
  type: Support
  url: https://lastdatabase.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://lastdatabase.com/register
- group: start
  title: ''
  type: Login
  url: https://lastdatabase.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lastdatabase.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lastdatabase.com/privacy
- group: operate
  title: ''
  type: FAQ
  url: https://lastdatabase.com/faq
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/lastdatabase-9706957/workspace/lastdatabase-developers
created: '2026-09-23'
description: 'LastDatabase is a B2B and consumer contact-data marketplace selling email, phone and fax lead lists organised by country, industry, category and job title, plus data enrichment and email verification. Developers reach it two ways: the Lead Search API, a single Bearer-key REST endpoint (GET /api/leads/search) filterable by type, country, city, industry, keyword and limit, sold on Free, Pro and Enterprise daily-request plans; and an OAuth-protected remote MCP server at lastdatabase.com/mcp exposing search_people, unlock_people, verify_email and get_credits tools gated by scopes. It publishes an OpenAPI 3.1 document, an llms.txt, a public Postman collection and a Trust Center claiming ISO/IEC 27001.'
finops:
- has_sources: true
  method: derived
  name: Lastdatabase Finops
  primary_unit: subscription
  service_category: ''
  slug: lastdatabase-finops
  template: false
image: https://lastdatabase.com/logo.png
json_schemas:
- name: LeadSearchResponse
  property_count: 4
  slug: lastdatabase-lead-search-response
jsonld:
- class_count: 5
  name: Lastdatabase Context
  property_count: 32
  slug: lastdatabase-context
layout: provider
mcp_servers:
- description: Remote MCP server at lastdatabase.com over streamable HTTP requiring OAuth; 4 tools listed.
  name: LastDatabase MCP Server
  slug: lastdatabase-mcp-server
modified: '2026-09-23'
name: LastDatabase
nav: Providers
network: true
overview: 'LastDatabase publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Leads API, and 1 more. Tagged areas include Contact Data, Lead Generation, B2B Data, Email Verification, and Data Enrichment.


  The LastDatabase catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  LastDatabase''s developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, support, signup flow, and 31 more developer resources.'
plans:
- name: Lastdatabase Plans Pricing
  plan_count: 3
  slug: lastdatabase-plans-pricing
- name: Lastdatabase Price Estimates
  plan_count: 0
  slug: lastdatabase-price-estimates
random_paper: 9
rate_limits:
- limit_count: 4
  name: Lastdatabase Rate Limits
  slug: lastdatabase-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: LastDatabase API Rules
  rule_count: 18
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 1
  slug: lastdatabase-rules
scopes:
- name: Lastdatabase Scopes
  scope_count: 9
  slug: lastdatabase-scopes
  summary_line: 9 scopes
score:
  band: strong
  composite: 58.3
  coverage:
    artifact_dirs: 31
    catalog_earned: 86.2
    catalog_earned_first_party: 24.0
    catalog_gap: 28.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.2
  facets:
    access_clarity: 73.7
    contract_governance: 35.6
    contract_quality: 73.1
    developer_ergonomics: 33.8
    discoverability: 75.0
    operational_transparency: 31.6
  previous_composite: 68.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/lastdatabase/lastdatabase-2026-10-11T110322.png
security:
- kind: authentication
  name: Lastdatabase Authentication
  slug: lastdatabase-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Lastdatabase Domain Security
  slug: lastdatabase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Lastdatabase Trust Center
  slug: lastdatabase-trust-center
  summary_line: ISO/IEC 27001, GDPR, CCPA
skill_count: 1
skills:
- name: lastdatabase-search-leads
  slug: lastdatabase-search-leads
slug: lastdatabase
tags:
- Contact Data
- Lead Generation
- B2B Data
- Email Verification
- Data Enrichment
- Sales Prospecting
- MCP
website: https://lastdatabase.com/
---
