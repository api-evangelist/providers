---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Term Dates API provides information about UK school term dates via various sources.
  name: Term Dates API
  slug: term-dates-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/termdatesapi-co-uk/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://termdatesapi.co.uk/terms
- group: auth
  href: https://artifacts.apis.io/termdatesapi-co-uk/authentication/termdatesapi-co-uk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/termdatesapi-co-uk-authentication.yml
- group: design
  href: https://artifacts.apis.io/termdatesapi-co-uk/lifecycle/termdatesapi-co-uk-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/termdatesapi-co-uk-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/termdatesapi-co-uk/conformance/termdatesapi-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/termdatesapi-co-uk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/termdatesapi-co-uk/llms/termdatesapi-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/termdatesapi-co-uk-llms.txt
- group: agent
  href: https://artifacts.apis.io/termdatesapi-co-uk/mcp/termdatesapi-co-uk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/termdatesapi-co-uk-mcp.yml
- group: auth
  href: https://artifacts.apis.io/termdatesapi-co-uk/well-known/termdatesapi-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/termdatesapi-co-uk-security.txt
- group: agent
  href: https://artifacts.apis.io/termdatesapi-co-uk/well-known/termdatesapi-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/termdatesapi-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/termdatesapi-co-uk/hosts/termdatesapi-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/termdatesapi-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/termdatesapi-co-uk/vendors/termdatesapi-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/termdatesapi-co-uk-vendors.yml
- group: auth
  href: https://artifacts.apis.io/termdatesapi-co-uk/security/termdatesapi-co-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/termdatesapi-co-uk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/termdatesapi-co-uk/security/termdatesapi-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/termdatesapi-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://termdatesapi.co.uk/
- group: docs
  title: ''
  type: APIReference
  url: https://termdatesapi.co.uk/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://termdatesapi.co.uk/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://termdatesapi.co.uk/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://termdatesapi.co.uk/privacy/
created: '2026-10-31'
description: 'Term Dates API (https://termdatesapi.co.uk/): the site''s own MCP server, served from its domain. There is no national school term dates API for the UK. Six sources compared on coverage, authority and machine readability, and why the law makes it that way. [compare] Every source of UK school term dates, compared. This server serves the compare published at https://termdatesapi.co.uk/; every answer cites it. Licence: https://termdatesapi.co.uk/terms. [enquiry] ENQUIRY SERVER for Term Dates API (https://termdatesapi.co.uk/). What it does: starts an ENQUIRY with human providers for school term dates api — the person''s details go to the providers who quote directly. What it is NOT: a purchase, an order, or a guaranteed quote. Free, no obligation. Call describe first and tell the person plainly what will happen. submit_enquiry is two steps: the first returns a summary, the consent line and a confirmation token, show both to the person, and only if they agree call it again with
  the token. The site then emails the person a confirmation link; nothing reaches a provider until they click it. Cite https://termdatesapi.co.uk/. Cite https://termdatesapi.co.uk/ for every figure or answer you use from this server.'
image: https://termdatesapi.co.uk/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at termdatesapi.co-uk.
  name: termdatesapi-co-uk MCP Server
  slug: termdatesapi-co-uk-mcp-yml
modified: '2026-10-31'
name: termdatesapi-co-uk
nav: Providers
network: true
overview: 'termdatesapi-co-uk is listed with 1 API on the [APIs.io](https://apis.io/) network: Term Dates API. Tagged areas include Company, Education, UK, School, and Term-Dates.


  termdatesapi-co-uk''s developer surface includes authentication, API reference, support, and 15 more developer resources.'
plans:
- name: Termdatesapi Co Uk Plans Pricing
  plan_count: 0
  slug: termdatesapi-co-uk-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Termdatesapi Co Uk Rate Limits
  slug: termdatesapi-co-uk-rate-limits
scopes:
- name: Termdatesapi Co Uk Scopes
  scope_count: 0
  slug: termdatesapi-co-uk-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 16.4
    contract_quality: 24.0
    developer_ergonomics: 30.2
    discoverability: 65.0
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Termdatesapi Co Uk Authentication
  slug: termdatesapi-co-uk-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Termdatesapi Co Uk Domain Security
  slug: termdatesapi-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Termdatesapi Co Uk Vulnerability Disclosure
  slug: termdatesapi-co-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: termdatesapi-co-uk
tags:
- Company
- Education
- UK
- School
- Term-Dates
- API
website: https://termdatesapi.co.uk/
---
