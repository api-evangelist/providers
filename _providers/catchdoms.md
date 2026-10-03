---
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.9
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Catchdoms Agentic Access
  operation_count: 5
  slug: catchdoms-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- baseURL: https://catchdoms.com/api
  baseurl_source: declared
  description: The Domains API from CatchDoms Expired Domains API — 2 operation(s) for domains.
  name: CatchDoms Expired Domains API Domains API
  slug: catchdoms-domains-api
- baseURL: https://catchdoms.com/api
  baseurl_source: declared
  description: The Free API from CatchDoms Expired Domains API — 1 operation(s) for free.
  name: CatchDoms Expired Domains API Free API
  slug: catchdoms-free-api
- baseURL: https://catchdoms.com/api
  baseurl_source: declared
  description: The Pending-Delete API from CatchDoms Expired Domains API — 2 operation(s) for pending-delete.
  name: CatchDoms Expired Domains API Pending Delete API
  slug: catchdoms-pending-delete-api
artifact_total: 15
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/catchdoms/refs/heads/main/agentic-access/catchdoms-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/catchdoms-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/catchdoms/refs/heads/main/plans/catchdoms-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/catchdoms-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/catchdoms/refs/heads/main/rules/catchdoms-rules.yml
  title: ''
  type: Spectral
  url: rules/catchdoms-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/catchdoms/refs/heads/main/json-ld/catchdoms-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/catchdoms-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/catchdoms/refs/heads/main/vocabulary/catchdoms-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/catchdoms-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/catchdoms/refs/heads/main/data-model/catchdoms-data-model.yml
  title: ''
  type: DataModel
  url: data-model/catchdoms-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/catchdoms/refs/heads/main/changelog/catchdoms-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/catchdoms-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/catchdoms/refs/heads/main/errors/catchdoms-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/catchdoms-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/catchdoms/refs/heads/main/conformance/catchdoms-conformance.yml
  title: ''
  type: Conformance
  url: conformance/catchdoms-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/catchdoms/refs/heads/main/overlays/catchdoms-openapi-overlay.yml
  title: ''
  type: Overlay
  url: overlays/catchdoms-openapi-overlay.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/catchdoms/refs/heads/main/llms/catchdoms-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/catchdoms-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/catchdoms/refs/heads/main/mcp/catchdoms-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/catchdoms-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/catchdoms/refs/heads/main/well-known/catchdoms-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/catchdoms-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/catchdoms/refs/heads/main/hosts/catchdoms-hosts.yml
  title: ''
  type: Hosts
  url: hosts/catchdoms-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/catchdoms/refs/heads/main/vendors/catchdoms-vendors.yml
  title: ''
  type: Vendors
  url: vendors/catchdoms-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://catchdoms.com/tlds/help
- group: start
  title: ''
  type: SignUp
  url: https://catchdoms.com/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://catchdoms.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://catchdoms.com/tlds/news
- group: other
  title: ''
  type: Leadership
  url: https://catchdoms.com/tlds/team
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/catchdoms/refs/heads/main/authentication/catchdoms-authentication.yml
  title: ''
  type: Authentication
  url: authentication/catchdoms-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/catchdoms/refs/heads/main/security/catchdoms-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/catchdoms-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://catchdoms.com/
- group: docs
  title: ''
  type: Documentation
  url: https://catchdoms.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://catchdoms.com/api
- group: commercial
  title: ''
  type: Pricing
  url: https://catchdoms.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://catchdoms.com/terms
- group: company
  title: ''
  type: Blog
  url: https://catchdoms.com/blog
created: '2026-09-27'
description: CatchDoms provides an API to discover expired and expiring domain names across multiple registrars such as Dynadot, GoDaddy, Catched, and DropCatch. Users can filter results by domain age, backlink count, domain authority, and other SEO metrics. The service also assigns a quality score to help identify hidden gem domains for resale or branding. Documentation includes endpoints for searching, retrieving domain details, and accessing historical data, supporting JSON responses and pagination. The platform aims to empower marketers, investors, and developers to capitalize on the secondary domain market efficiently.
image: https://catchdoms.com/images/og.jpg
json_schemas:
- name: Domain
  property_count: 57
  slug: catchdoms-domain
- name: FreeDomain
  property_count: 16
  slug: catchdoms-free-domain
- name: PaginationLinks
  property_count: 4
  slug: catchdoms-pagination-links
- name: PaginationMeta
  property_count: 6
  slug: catchdoms-pagination-meta
- name: PendingDeleteDomain
  property_count: 23
  slug: catchdoms-pending-delete-domain
jsonld:
- class_count: 5
  name: Catchdoms Context
  property_count: 74
  slug: catchdoms-context
layout: provider
mcp_servers:
- description: ''
  name: CatchDoms Expired Domains API MCP Server
  slug: catchdoms-expired-domains-api-mcp-server
modified: '2026-09-27'
name: CatchDoms Expired Domains API
nav: Providers
network: true
overview: 'CatchDoms Expired Domains API publishes 3 APIs on the [APIs.io](https://apis.io/) network: Domains API, Free API, and Pending Delete API. Tagged areas include Company, Domains, SEO, and Expired.


  The CatchDoms Expired Domains API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CatchDoms Expired Domains API''s developer surface includes changelog, support, signup flow, authentication, documentation, API reference, pricing, and 21 more developer resources.'
plans:
- name: Catchdoms Plans Pricing
  plan_count: 5
  slug: catchdoms-plans-pricing
random_paper: 4
rules:
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: CatchDoms Expired Domains API API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: catchdoms-rules
score:
  band: developing
  composite: 51.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 64.2
    developer_ergonomics: 35.7
    discoverability: 70.0
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Catchdoms Authentication
  slug: catchdoms-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Catchdoms Domain Security
  slug: catchdoms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: catchdoms
tags:
- Company
- Domains
- SEO
- Expired
website: https://catchdoms.com/
---
