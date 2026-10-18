---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.9
  scored_at: '2026-10-17'
api_count: 15
apis:
- baseURL: https://api.contactout.com
  baseurl_source: declared
  description: The API Usage Stats API from ContactOut — 1 operation(s) for api usage stats.
  name: ContactOut API Usage Stats API
  slug: contactout-api-usage-stats-api
- baseURL: https://api.contactout.com
  baseurl_source: declared
  description: The Campaigns API API from ContactOut — 5 operation(s) for campaigns api.
  name: ContactOut Campaigns API
  slug: contactout-campaigns-api-api
- baseURL: https://api.contactout.com
  baseurl_source: declared
  description: The Company information from domains API from ContactOut — 1 operation(s) for company information from domains.
  name: ContactOut Company information from domains API
  slug: contactout-company-information-from-domains-api
- baseURL: https://api.contactout.com
  baseurl_source: declared
  description: The Company Search API API from ContactOut — 1 operation(s) for company search api.
  name: ContactOut Company Search API
  slug: contactout-company-search-api-api
- baseURL: https://api.contactout.com
  baseurl_source: declared
  description: The Contact Checker API API from ContactOut — 3 operation(s) for contact checker api.
  name: ContactOut Contact Checker API
  slug: contactout-contact-checker-api-api
- baseURL: https://api.contactout.com
  baseurl_source: declared
  description: The Contact Info API - Bulk API from ContactOut — 3 operation(s) for contact info api - bulk.
  name: ContactOut Contact Info API - Bulk API
  slug: contactout-contact-info-api-bulk-api
- baseURL: https://api.contactout.com
  baseurl_source: declared
  description: The Contact Info API - Single API from ContactOut — 1 operation(s) for contact info api - single.
  name: ContactOut Contact Info API - Single API
  slug: contactout-contact-info-api-single-api
- baseURL: https://api.contactout.com
  baseurl_source: declared
  description: The Decision Makers API API from ContactOut — 1 operation(s) for decision makers api.
  name: ContactOut Decision Makers API
  slug: contactout-decision-makers-api-api
- baseURL: https://api.contactout.com
  baseurl_source: declared
  description: The Email to LinkedIn API API from ContactOut — 1 operation(s) for email to linkedin api.
  name: ContactOut Email to LinkedIn API
  slug: contactout-email-to-linkedin-api-api
- baseURL: https://api.contactout.com
  baseurl_source: declared
  description: The Email Verifier API API from ContactOut — 3 operation(s) for email verifier api.
  name: ContactOut Email Verifier API
  slug: contactout-email-verifier-api-api
- baseURL: https://api.contactout.com
  baseurl_source: declared
  description: The Hashed Email API API from ContactOut — 1 operation(s) for hashed email api.
  name: ContactOut Hashed Email API
  slug: contactout-hashed-email-api-api
- baseURL: https://api.contactout.com
  baseurl_source: declared
  description: The LinkedIn Profile API API from ContactOut — 2 operation(s) for linkedin profile api.
  name: ContactOut LinkedIn Profile API
  slug: contactout-linkedin-profile-api-api
- baseURL: https://api.contactout.com
  baseurl_source: declared
  description: The People Count API API from ContactOut — 1 operation(s) for people count api.
  name: ContactOut People Count API
  slug: contactout-people-count-api-api
- baseURL: https://api.contactout.com
  baseurl_source: declared
  description: The People Enrich API API from ContactOut — 1 operation(s) for people enrich api.
  name: ContactOut People Enrich API
  slug: contactout-people-enrich-api-api
- baseURL: https://api.contactout.com
  baseurl_source: declared
  description: The People Search API API from ContactOut — 1 operation(s) for people search api.
  name: ContactOut People Search API
  slug: contactout-people-search-api-api
artifact_total: 30
asyncapis:
- description: ''
  name: Contactout Webhooks
  slug: contactout-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contactout/refs/heads/main/json-ld/contactout-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/contactout-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contactout/refs/heads/main/vocabulary/contactout-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/contactout-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/contactout/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contactout/refs/heads/main/asyncapi/contactout-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/contactout-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contactout/refs/heads/main/data-model/contactout-data-model.yml
  title: ''
  type: DataModel
  url: data-model/contactout-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contactout/refs/heads/main/conventions/contactout-conventions.yml
  title: ''
  type: Conventions
  url: conventions/contactout-conventions.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contactout/refs/heads/main/overlays/contactout-openapi-generated-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/contactout-openapi-generated-overlay.yaml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/contactout/refs/heads/main/mcp/contactout-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/contactout-tool-crosswalk.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/contactout/refs/heads/main/rate-limits/contactout-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/contactout-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/contactout/refs/heads/main/plans/contactout-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/contactout-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contactout/refs/heads/main/rules/contactout-rules.yml
  title: ''
  type: Spectral
  url: rules/contactout-rules.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contactout/refs/heads/main/authentication/contactout-authentication.yml
  title: ''
  type: Authentication
  url: authentication/contactout-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contactout/refs/heads/main/scopes/contactout-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/contactout-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contactout/refs/heads/main/lifecycle/contactout-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/contactout-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contactout/refs/heads/main/errors/contactout-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/contactout-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contactout/refs/heads/main/conformance/contactout-conformance.yml
  title: ''
  type: Conformance
  url: conformance/contactout-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/contactout/refs/heads/main/llms/contactout-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contactout-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/contactout/refs/heads/main/mcp/contactout-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/contactout-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/contactout/refs/heads/main/well-known/contactout-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contactout-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contactout/refs/heads/main/hosts/contactout-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contactout-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contactout/refs/heads/main/vendors/contactout-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contactout-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/contactout/refs/heads/main/packages/contactout-packages.yml
  title: ''
  type: SDKs
  url: packages/contactout-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/contactout/refs/heads/main/packages/contactout-packages.yml
  title: ''
  type: Packages
  url: packages/contactout-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contactout/refs/heads/main/security/contactout-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contactout-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contactout.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.contactout.com
- group: docs
  title: ''
  type: APIReference
  url: https://api.contactout.com
- group: company
  title: ''
  type: Blog
  url: https://blog.contactout.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.contactout.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://contactout.com/pricing
- group: start
  title: ''
  type: Login
  url: https://contactout.com/login
- group: start
  title: ''
  type: SignUp
  url: https://contactout.com/register?from=home
- group: commercial
  title: ''
  type: TermsOfService
  url: https://contactout.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://contactout.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/contactout
- group: operate
  title: ''
  type: HelpCenter
  url: https://contactout.freshdesk.com/support/home
- group: agent
  title: ''
  type: LLMsTxt
  url: https://contactout.com/llms.txt
created: '2026-10-07'
description: ContactOut is a B2B email finder and professional contact data platform (ContactOut Pty Ltd, founded 2015, San Francisco) that provides verified personal and work emails, phone numbers and enriched people and company profiles for 350M professionals across 40M companies, delivered through a Chrome extension, search portal, bulk tools, a REST API at api.contactout.com and a hosted MCP server at contactout.com/mcp. Used by recruiters and sales teams; GDPR and CCPA compliant with a published opt-out, and intended for professional B2B use only.
image: https://contactout.com/images/logo-square-200px.png
json_schemas:
- name: CompanyInformationFromDomainsResponse
  property_count: 2
  slug: contactout-company-information-from-domains-response
- name: CompanySearchRequest
  property_count: 12
  slug: contactout-company-search-request
- name: LinkedinProfileFromEmailAddressResponse
  property_count: 2
  slug: contactout-linkedin-profile-from-email-address-response
- name: LinkedinProfileFromLinkedinUrlResponse
  property_count: 2
  slug: contactout-linkedin-profile-from-linkedin-url-response
- name: PeopleEnrichResponse
  property_count: 2
  slug: contactout-people-enrich-response
- name: PeopleSearchRequest
  property_count: 37
  slug: contactout-people-search-request
jsonld:
- class_count: 31
  name: Contactout Context
  property_count: 87
  slug: contactout-context
layout: provider
mcp_servers:
- description: ContactOut provides an MCP (Model Context Protocol) server that lets AI assistants like Claude, Cursor, and other MCP-compatible clients call ContactOut APIs directly. Use natural language to find con
  name: ContactOut MCP
  slug: contactout-mcp
modified: '2026-10-07'
name: ContactOut
nav: Providers
network: true
overview: 'ContactOut is listed with 15 APIs on the [APIs.io](https://apis.io/) network, including API Usage Stats API, Campaigns API, Company information from domains API, and 12 more. Tagged areas include Company, Contact Data, Email Finder, Data Enrichment, and People Search.


  The ContactOut catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  ContactOut''s developer surface includes authentication, documentation, API reference, engineering blog, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Contactout Plans Pricing
  plan_count: 4
  slug: contactout-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Contactout Rate Limits
  slug: contactout-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: ContactOut API Rules
  rule_count: 16
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 0
  slug: contactout-rules
scopes:
- name: Contactout Scopes
  scope_count: 1
  slug: contactout-scopes
  summary_line: 1 scope
score:
  band: developing
  composite: 53.5
  coverage:
    artifact_dirs: 28
    catalog_earned: 89.0
    catalog_earned_first_party: 24.0
    catalog_gap: 26.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 76.3
    contract_governance: 19.7
    contract_quality: 35.7
    developer_ergonomics: 44.6
    discoverability: 80.0
    operational_transparency: 60.5
  previous_composite: 51.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 16
      marker_coverage: 100.0
      total: 16
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/contactout/refs/heads/main/screenshots/contactout-2026-10-11T103232.png
security:
- kind: authentication
  name: Contactout Authentication
  slug: contactout-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Contactout Domain Security
  slug: contactout-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: contactout
tags:
- Company
- Contact Data
- Email Finder
- Data Enrichment
- People Search
- Company Search
- Email Verification
- Sales Intelligence
- Recruiting
- B2B Data
website: https://contactout.com
---
