---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.5
  scored_at: '2026-09-16'
api_count: 1
apis:
- baseURL: https://www.countrycalling.codes
  baseurl_source: declared
  description: The Calling codes API from Country Calling Codes — 2 operation(s) for calling codes.
  name: Country Calling Codes Calling codes API
  slug: country-calling-codes-calling-codes-api
- baseURL: https://www.countrycalling.codes
  baseurl_source: declared
  description: The Phone formatting API from Country Calling Codes — 1 operation(s) for phone formatting.
  name: Country Calling Codes Phone formatting API
  slug: country-calling-codes-phone-formatting-api
- baseURL: https://www.countrycalling.codes
  baseurl_source: declared
  description: The Phone workflows API from Country Calling Codes — 9 operation(s) for phone workflows.
  name: Country Calling Codes Phone workflows API
  slug: country-calling-codes-phone-workflows-api
- baseURL: https://www.countrycalling.codes
  baseurl_source: declared
  description: The Service API from Country Calling Codes — 1 operation(s) for service.
  name: Country Calling Codes Service API
  slug: country-calling-codes-service-api
artifact_total: 11
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://www.countrycalling.codes/api/mcp
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/country-calling-codes/refs/heads/main/mcp/country-calling-codes-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/country-calling-codes-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: https://www.countrycalling.codes/skill.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/country-calling-codes/refs/heads/main/skills/country-calling-codes-skill.json
  title: ''
  type: AgentSkill
  url: skills/country-calling-codes-skill.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/country-calling-codes/refs/heads/main/overlays/country-calling-codes-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/country-calling-codes-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.countrycalling.codes
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/country-calling-codes/refs/heads/main/security/country-calling-codes-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/country-calling-codes-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/country-calling-codes/refs/heads/main/security/country-calling-codes-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/country-calling-codes-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/country-calling-codes/refs/heads/main/security/country-calling-codes-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/country-calling-codes-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/country-calling-codes/refs/heads/main/well-known/country-calling-codes-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/country-calling-codes-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/country-calling-codes/refs/heads/main/well-known/country-calling-codes-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/country-calling-codes-security.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.countrycalling.codes/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.countrycalling.codes/contact
created: '2026-09-08'
description: Public read-only reference API for ITU E.164 country calling codes, phone number formatting, batch normalization, comparison, dialing guidance, input rules, and calling windows. Ships a REST API, hosted MCP server, llms.txt, and agent skill manifest simultaneously. No authentication required.
image: https://www.countrycalling.codes/opengraph-image
layout: provider
mcp_servers:
- description: ''
  name: Country Calling Codes MCP Server
  slug: country-calling-codes-mcp-server
- description: ''
  name: Country Calling Codes MCP Server
  slug: country-calling-codes-mcp-server-2
modified: '2026-09-09'
name: Country Calling Codes
nav: Providers
network: true
overview: 'Country Calling Codes publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Calling codes API, Phone formatting API, Phone workflows API, and 1 more. Tagged areas include Data, Reference, Telecom, Phone, and OpenAPI.


  Country Calling Codes'' developer surface includes support and 12 more developer resources.'
plans:
- name: Country Calling Codes Plans Pricing
  plan_count: 1
  slug: country-calling-codes-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Country Calling Codes Rate Limits
  slug: country-calling-codes-rate-limits
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.3
  facets:
    access_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 51.7
    developer_ergonomics: 40.5
    discoverability: 75.9
    operational_transparency: 26.3
  previous_composite: 33.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 37.5
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: rising
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Country Calling Codes Authentication
  slug: country-calling-codes-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Country Calling Codes Domain Security
  slug: country-calling-codes-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Country Calling Codes Vulnerability Disclosure
  slug: country-calling-codes-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: country-calling-codes
tags:
- Data
- Reference
- Telecom
- Phone
- OpenAPI
- MCP
website: https://www.countrycalling.codes
---
