---
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-10'
api_count: 1
apis:
- description: Read-only JSON API for country calling code lookup, phone number formatting, analysis, batch normalization, comparison, dialing guidance and capabilities. Includes a hosted Streamable HTTP MCP server,
  name: Country Calling Codes API
  slug: country-calling-codes-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.countrycalling.codes
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/country-calling-codes-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/country-calling-codes-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/country-calling-codes-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/country-calling-codes-well-known.yml
- group: auth
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
overview: 'Country Calling Codes publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include data, reference, telecom, phone, and openapi.


  Country Calling Codes'' developer surface includes support and 7 more developer resources.'
plans:
- name: Country Calling Codes Plans Pricing
  plan_count: 1
  slug: country-calling-codes-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Country Calling Codes Rate Limits
  slug: country-calling-codes-rate-limits
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 26.7
    developer_ergonomics: 40.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  provenance:
    conformance: derived
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 37.5
  schema_version: 0.20.0
  scored_at: '2026-09-10'
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
- data
- reference
- telecom
- phone
- openapi
- mcp
website: https://www.countrycalling.codes
---
