---
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
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.9
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Lastdatabase Agentic Access
  operation_count: 1
  slug: lastdatabase-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://lastdatabase.com
  baseurl_source: spec
  description: Search LastDatabase email, phone and fax lead inventory by type, country, city, industry, keyword and limit (default 25, capped at 100) through one GET endpoint, authenticated with an active API key s
  name: LastDatabase Lead Search API
  slug: lead-search-api
- description: 'OAuth-protected remote Model Context Protocol server at https://lastdatabase.com/mcp exposing four scope-gated tools: search_people (non-charging masked B2B contact search), unlock_people (entitlement'
  name: LastDatabase MCP Server
  slug: mcp-server
artifact_total: 13
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lastdatabase/refs/heads/main/overlays/lastdatabase-lead-search-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lastdatabase-lead-search-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lastdatabase/refs/heads/main/agentic-access/lastdatabase-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lastdatabase-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/lastdatabase/refs/heads/main/rate-limits/lastdatabase-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lastdatabase-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/lastdatabase/refs/heads/main/plans/lastdatabase-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lastdatabase-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lastdatabase/refs/heads/main/rules/lastdatabase-rules.yml
  title: ''
  type: Spectral
  url: rules/lastdatabase-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lastdatabase/refs/heads/main/json-ld/lastdatabase-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lastdatabase-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lastdatabase/refs/heads/main/vocabulary/lastdatabase-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lastdatabase-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lastdatabase/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lastdatabase/refs/heads/main/data-model/lastdatabase-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lastdatabase-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lastdatabase/refs/heads/main/conventions/lastdatabase-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lastdatabase-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://lastdatabase.com/trust-center
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lastdatabase/refs/heads/main/scopes/lastdatabase-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/lastdatabase-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lastdatabase/refs/heads/main/errors/lastdatabase-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/lastdatabase-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lastdatabase/refs/heads/main/errors/lastdatabase-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lastdatabase-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lastdatabase/refs/heads/main/conformance/lastdatabase-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lastdatabase-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lastdatabase/refs/heads/main/llms/lastdatabase-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lastdatabase-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/lastdatabase/refs/heads/main/mcp/lastdatabase-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/lastdatabase-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lastdatabase/refs/heads/main/mcp/lastdatabase-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lastdatabase-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lastdatabase/refs/heads/main/well-known/lastdatabase-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lastdatabase-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lastdatabase/refs/heads/main/hosts/lastdatabase-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lastdatabase-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lastdatabase/refs/heads/main/vendors/lastdatabase-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lastdatabase-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lastdatabase/refs/heads/main/authentication/lastdatabase-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lastdatabase-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lastdatabase/refs/heads/main/security/lastdatabase-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/lastdatabase-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lastdatabase/refs/heads/main/security/lastdatabase-domain-security.yml
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
- description: ''
  name: LastDatabase MCP Server
  slug: lastdatabase-mcp-server
modified: '2026-09-23'
name: LastDatabase
nav: Providers
network: true
overview: 'LastDatabase publishes 2 APIs on the [APIs.io](https://apis.io/) network, including Lead Search API, and 1 more. Tagged areas include Contact Data, Lead Generation, B2B Data, Email Verification, and Data Enrichment.


  The LastDatabase catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  LastDatabase''s developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, support, signup flow, and 30 more developer resources.'
plans:
- name: Lastdatabase Plans Pricing
  plan_count: 3
  slug: lastdatabase-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 4
  name: Lastdatabase Rate Limits
  slug: lastdatabase-rate-limits
rules:
- effective_rule_count: 59
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
  scope_count: 0
  slug: lastdatabase-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 66.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 78.2
    catalog_earned_first_party: 24.0
    catalog_gap: 36.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 92.1
    contract_governance: 35.6
    contract_quality: 66.9
    developer_ergonomics: 61.2
    discoverability: 66.7
    operational_transparency: 31.6
  previous_composite: 65.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
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
    score: 39.2
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
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
