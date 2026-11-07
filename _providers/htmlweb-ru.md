---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Htmlweb Ru Agentic Access
  operation_count: 14
  slug: htmlweb-ru-agentic-access
  summary_line: 14 operations · 2 acting
api_count: 1
apis:
- baseURL: https://htmlweb.ru/
  baseurl_source: declared
  description: The Json API from htmlweb-ru — 7 operation(s) for json.
  name: htmlweb-ru JSON API
  slug: htmlweb-ru-json-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/htmlweb-ru/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/htmlweb-ru/agentic-access/htmlweb-ru-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/htmlweb-ru-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/htmlweb-ru/rules/htmlweb-ru-rules.yml
  title: ''
  type: Spectral
  url: rules/htmlweb-ru-rules.yml
- group: design
  href: https://artifacts.apis.io/htmlweb-ru/errors/htmlweb-ru-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/htmlweb-ru-problem-types.yml
- group: design
  href: https://artifacts.apis.io/htmlweb-ru/conformance/htmlweb-ru-conformance.yml
  title: ''
  type: Conformance
  url: conformance/htmlweb-ru-conformance.yml
- group: agent
  href: https://artifacts.apis.io/htmlweb-ru/llms/htmlweb-ru-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/htmlweb-ru-llms.txt
- group: other
  href: https://artifacts.apis.io/htmlweb-ru/a2a/htmlweb-ru-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/htmlweb-ru-a2a.yml
- group: agent
  href: https://artifacts.apis.io/htmlweb-ru/mcp/htmlweb-ru-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/htmlweb-ru-mcp.yml
- group: agent
  href: https://artifacts.apis.io/htmlweb-ru/well-known/htmlweb-ru-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/htmlweb-ru-well-known.yml
- group: other
  href: https://artifacts.apis.io/htmlweb-ru/hosts/htmlweb-ru-hosts.yml
  title: ''
  type: Hosts
  url: hosts/htmlweb-ru-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://htmlweb.ru/user/privacy_policy_new.php
- group: auth
  href: https://artifacts.apis.io/htmlweb-ru/security/htmlweb-ru-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/htmlweb-ru-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://htmlweb.ru/
- group: docs
  title: ''
  type: Documentation
  url: https://htmlweb.ru/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://htmlweb.ru/geo/
created: '2026-10-30'
description: htmlweb.ru provides a collection of Russian-focused web utilities and data APIs, including services for IP geolocation, phone operator lookup, organization verification by INN/OGRN, bank information by BIK, email validation, holiday calendars, QR code generation, domain WHOIS, OCR, anti-spam classification, SMS gateway, and MAX/Telegram bots. The platform offers both web interfaces and HTTP APIs, documented in llms.txt, and supports API key and bearer token authentication. It targets developers building Russian market applications.
image: https://htmlweb.ru/images/og-image/index.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.htmlweb.ru requiring an API key.
  name: htmlweb-ru MCP Server
  slug: htmlweb-ru-mcp-yml
modified: '2026-10-30'
name: htmlweb-ru
nav: Providers
network: true
overview: 'htmlweb-ru publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: JSON API. Tagged areas include Company, Web, Russia, Data, and Utilities.


  The htmlweb-ru catalog on APIs.io includes 1 Spectral governance ruleset.


  htmlweb-ru''s developer surface includes documentation, API reference, and 13 more developer resources.'
plans:
- name: Htmlweb Ru Plans Pricing
  plan_count: 0
  slug: htmlweb-ru-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Htmlweb Ru Rate Limits
  slug: htmlweb-ru-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: htmlweb-ru API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: htmlweb-ru-rules
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 25
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 5.3
    contract_governance: 18.2
    contract_quality: 42.9
    developer_ergonomics: 14.8
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - russia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 26.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 10.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/htmlweb-ru/htmlweb-ru-2026-11-03T133507.png
security:
- kind: authentication
  name: Htmlweb Ru Authentication
  slug: htmlweb-ru-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Htmlweb Ru Domain Security
  slug: htmlweb-ru-domain-security
  summary_line: TLSv1.2 · DMARC
slug: htmlweb-ru
tags:
- Company
- Web
- Russia
- Data
- Utilities
website: https://htmlweb.ru/
---
