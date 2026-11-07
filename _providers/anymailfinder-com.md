---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Anymailfinder Com Agentic Access
  operation_count: 17
  slug: anymailfinder-com-agentic-access
  summary_line: 17 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.anymailfinder.com
  baseurl_source: declared
  description: The account API from Anymail Finder — 1 operation(s) for account.
  name: Anymail Finder Account API
  slug: anymailfinder-com-account-api
- baseURL: https://api.anymailfinder.com
  baseurl_source: declared
  description: The bulk API from Anymail Finder — 4 operation(s) for bulk.
  name: Anymail Finder Bulk API
  slug: anymailfinder-com-bulk-api
- baseURL: https://api.anymailfinder.com
  baseurl_source: declared
  description: The domain API from Anymail Finder — 3 operation(s) for domain.
  name: Anymail Finder Domain API
  slug: anymailfinder-com-domain-api
- baseURL: https://api.anymailfinder.com
  baseurl_source: declared
  description: The find-email API from Anymail Finder — 4 operation(s) for find-email.
  name: Anymail Finder Find Email API
  slug: anymailfinder-com-find-email-api
- baseURL: https://api.anymailfinder.com
  baseurl_source: declared
  description: The geo-lead API from Anymail Finder — 3 operation(s) for geo-lead.
  name: Anymail Finder Geo Lead API
  slug: anymailfinder-com-geo-lead-api
- baseURL: https://api.anymailfinder.com
  baseurl_source: declared
  description: The report API from Anymail Finder — 1 operation(s) for report.
  name: Anymail Finder Report API
  slug: anymailfinder-com-report-api
- baseURL: https://api.anymailfinder.com
  baseurl_source: declared
  description: The verify-email API from Anymail Finder — 1 operation(s) for verify-email.
  name: Anymail Finder Verify Email API
  slug: anymailfinder-com-verify-email-api
artifact_total: 24
common:
- group: agent
  href: https://artifacts.apis.io/anymailfinder-com/agentic-access/anymailfinder-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/anymailfinder-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/anymailfinder-com/plans/anymailfinder-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/anymailfinder-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/anymailfinder-com/rules/anymailfinder-com-rules.yml
  title: ''
  type: Spectral
  url: rules/anymailfinder-com-rules.yml
- group: design
  href: https://artifacts.apis.io/anymailfinder-com/json-ld/anymailfinder-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/anymailfinder-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/anymailfinder-com/vocabulary/anymailfinder-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/anymailfinder-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/anymailfinder-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/anymailfinder-com/data-model/anymailfinder-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/anymailfinder-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/anymailfinder-com/authentication/anymailfinder-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/anymailfinder-com-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.anymailfinder.com/
- group: design
  href: https://artifacts.apis.io/anymailfinder-com/lifecycle/anymailfinder-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/anymailfinder-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/anymailfinder-com/errors/anymailfinder-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/anymailfinder-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/anymailfinder-com/conformance/anymailfinder-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anymailfinder-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/anymailfinder-com/llms/anymailfinder-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anymailfinder-com-llms.txt
- group: build
  href: https://artifacts.apis.io/anymailfinder-com/mcp/anymailfinder-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/anymailfinder-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/anymailfinder-com/mcp/anymailfinder-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/anymailfinder-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/anymailfinder-com/well-known/anymailfinder-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anymailfinder-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/anymailfinder-com/hosts/anymailfinder-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anymailfinder-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/anymailfinder-com/vendors/anymailfinder-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anymailfinder-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anymailfinder.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anymailfinder.com/legal/privacy-policy
- group: docs
  title: ''
  type: APIReference
  url: https://anymailfinder.com/email-finder-api/docs
- group: auth
  href: https://artifacts.apis.io/anymailfinder-com/security/anymailfinder-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anymailfinder-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anymailfinder.com/
- group: docs
  title: ''
  type: Documentation
  url: https://anymailfinder.com/email-finder-api
- group: commercial
  title: ''
  type: Pricing
  url: https://anymailfinder.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://anymailfinder.com/blog
- group: operate
  title: ''
  type: Support
  url: https://anymailfinder.com/contact
- group: start
  title: ''
  type: GettingStarted
  url: https://anymailfinder.com/email-finder-api
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.anymailfinder.com/openapi.json
  - status: null
    url: https://help.anymailfinder.com/mcp/v1
  - status: 401
    url: https://api.anymailfinder.com/mcp
  - status: 200
    url: https://anymailfinder.com/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: Anymail Finder provides a real-time email finder and verification service for sales, HR, and lead generation professionals. It offers verified B2B email addresses by name, domain, company, or LinkedIn URL, with bulk upload up to 100,000 rows and a pay‑only‑for‑verified‑results billing model. The platform includes a REST API, webhooks, and integrations with Zapier, Make.com, n8n, and over 7,000 other tools, enabling automated email discovery and validation at scale.
image: https://anymailfinder.com/assets/anymail-finder-200.png
json_schemas:
- name: Api5GeoLeadDto
  property_count: 15
  slug: anymailfinder-com-api5-geo-lead-dto
- name: Api5SearchBulkDto
  property_count: 9
  slug: anymailfinder-com-api5-search-bulk-dto
- name: Api51BulkCreateWithJsonBodyDto
  property_count: 12
  slug: anymailfinder-com-api51-bulk-create-with-json-body-dto
- name: Api51FindEmailDecisionMakerResponseSuccessDto
  property_count: 13
  slug: anymailfinder-com-api51-find-email-decision-maker-response-success-dto
- name: Api51FindEmailPersonResponseSuccessDto
  property_count: 10
  slug: anymailfinder-com-api51-find-email-person-response-success-dto
- name: Api51GeoLeadCreateBodyDto
  property_count: 8
  slug: anymailfinder-com-api51-geo-lead-create-body-dto
jsonld:
- class_count: 19
  name: Anymailfinder Com Context
  property_count: 55
  slug: anymailfinder-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.anymailfinder.com requiring OAuth.
  name: Anymail Finder MCP Server
  slug: anymailfinder-com-mcp-yml
modified: '2026-11-01'
name: Anymail Finder
nav: Providers
network: true
overview: 'Anymail Finder publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Bulk API, Domain API, and 4 more. Tagged areas include Email Finder, B2B, Lead Generation, and Verification.


  The Anymail Finder catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Anymail Finder''s developer surface includes authentication, API reference, documentation, pricing, engineering blog, support, getting-started guide, and 21 more developer resources.'
plans:
- name: Anymailfinder Com Plans Pricing
  plan_count: 6
  slug: anymailfinder-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Anymailfinder Com Rate Limits
  slug: anymailfinder-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Anymail Finder API Rules
  rule_count: 13
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 0
  slug: anymailfinder-com-rules
score:
  band: developing
  composite: 41.6
  coverage:
    artifact_dirs: 26
    catalog_earned: 69.0
    catalog_earned_first_party: 12.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 47.4
    contract_governance: 19.7
    contract_quality: 60.0
    developer_ergonomics: 36.2
    discoverability: 56.7
    operational_transparency: 7.9
  previous_composite: 50.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: unknown
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
security:
- kind: authentication
  name: Anymailfinder Com Authentication
  slug: anymailfinder-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Anymailfinder Com Domain Security
  slug: anymailfinder-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: find-email
  slug: anymailfinder-com-find-email
- name: list-domain-emails
  slug: anymailfinder-com-list-domain
- name: verify-email
  slug: anymailfinder-com-verify-email
slug: anymailfinder-com
tags:
- Email Finder
- B2B
- Lead Generation
- Verification
website: https://anymailfinder.com/
---
