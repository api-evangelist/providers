---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.7
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Real-time B2B data enrichment API providing company and people information.
  name: CompanyEnrich API
  slug: companyenrich-api
artifact_total: 7
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/companyenrich/refs/heads/main/well-known/companyenrich-companyenrich-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/companyenrich-companyenrich-security.txt
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/companyenrich/refs/heads/main/rate-limits/companyenrich-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/companyenrich-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/companyenrich/refs/heads/main/plans/companyenrich-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/companyenrich-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://companyenrich.com/trust
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/companyenrich/refs/heads/main/authentication/companyenrich-authentication.yml
  title: ''
  type: Authentication
  url: authentication/companyenrich-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/companyenrich/refs/heads/main/llms/companyenrich-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/companyenrich-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/companyenrich/refs/heads/main/a2a/companyenrich-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/companyenrich-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/companyenrich/refs/heads/main/mcp/companyenrich-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/companyenrich-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/companyenrich/refs/heads/main/well-known/companyenrich-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/companyenrich-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/companyenrich/refs/heads/main/hosts/companyenrich-hosts.yml
  title: ''
  type: Hosts
  url: hosts/companyenrich-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/companyenrich/refs/heads/main/vendors/companyenrich-vendors.yml
  title: ''
  type: Vendors
  url: vendors/companyenrich-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://companyenrich.com/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://help.companyenrich.com
- group: operate
  title: ''
  type: StatusPage
  url: https://companyenrich.statuspage.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://companyenrich.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://companyenrich.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://product.companyenrich.com/news/changelogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/companyenrich
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.companyenrich.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://companyenrich.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.companyenrich.com/docs/getting-started
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/companyenrich/refs/heads/main/security/companyenrich-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/companyenrich-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/companyenrich/refs/heads/main/security/companyenrich-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/companyenrich-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://companyenrich.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.companyenrich.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.companyenrich.com/reference
coverage:
  checked: '2026-10-05'
  detail: Docs are served via ReadMe platform rendering HTML, no machine‑readable OpenAPI spec found.
  evidence:
  - status: 200
    url: https://docs.companyenrich.com/reference
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-05'
description: CompanyEnrich provides real-time B2B data APIs that enrich company and people information for AI agents and platforms. Its services include company enrichment, company search, people search, CRM enrichment, similar companies discovery, reverse email lookup, funding data, ad intelligence, job listings, and headcount insights. The APIs return verified firmographics, technology stacks, funding rounds, and contact details, enabling developers to build intelligent business intelligence and automation solutions.
image: https://companyenrich.com/og/index-og.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.companyenrich.com.
  name: CompanyEnrich MCP Server
  slug: companyenrich-mcp-yml
modified: '2026-10-05'
name: CompanyEnrich
nav: Providers
network: true
overview: 'CompanyEnrich is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, B2B, Data, Data Enrichment, and Artificial Intelligence.


  CompanyEnrich''s developer surface includes authentication, support, pricing, changelog, engineering blog, getting-started guide, documentation, and 19 more developer resources.'
plans:
- name: Companyenrich Plans Pricing
  plan_count: 3
  slug: companyenrich-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Companyenrich Rate Limits
  slug: companyenrich-rate-limits
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 52.0
    catalog_earned_first_party: 20.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 68.3
    operational_transparency: 57.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Companyenrich Authentication
  slug: companyenrich-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Companyenrich Domain Security
  slug: companyenrich-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Companyenrich Trust Center
  slug: companyenrich-trust-center
  summary_line: GDPR
slug: companyenrich
tags:
- Company
- B2B
- Data
- Data Enrichment
- Artificial Intelligence
website: https://companyenrich.com
---
