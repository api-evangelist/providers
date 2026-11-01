---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 11.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Free worksheets that size and price a firm's risk assessment and COSHH programme from its own activities and substances, plus a paid plan for record keeping.
  name: Coshhvo API
  slug: coshhvo-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/coshhvo-com/plans/coshhvo-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coshhvo-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/coshhvo-com/vocabulary/coshhvo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/coshhvo-com-vocabulary.yml
- group: auth
  title: ''
  type: Security
  url: https://coshhvo.com/terms
- group: auth
  href: https://artifacts.apis.io/coshhvo-com/authentication/coshhvo-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/coshhvo-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/coshhvo-com/conformance/coshhvo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coshhvo-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/coshhvo-com/llms/coshhvo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coshhvo-com-llms.txt
- group: build
  href: https://artifacts.apis.io/coshhvo-com/mcp/coshhvo-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/coshhvo-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/coshhvo-com/mcp/coshhvo-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/coshhvo-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/coshhvo-com/well-known/coshhvo-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coshhvo-com-security.txt
- group: auth
  href: https://artifacts.apis.io/coshhvo-com/well-known/coshhvo-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coshhvo-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/coshhvo-com/well-known/coshhvo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coshhvo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/coshhvo-com/hosts/coshhvo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coshhvo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/coshhvo-com/vendors/coshhvo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coshhvo-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/coshhvo-com/packages/coshhvo-com-packages.yml
  title: ''
  type: SDKs
  url: packages/coshhvo-com-packages.yml
- group: build
  href: https://artifacts.apis.io/coshhvo-com/packages/coshhvo-com-packages.yml
  title: ''
  type: Packages
  url: packages/coshhvo-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/coshhvo-com/security/coshhvo-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/coshhvo-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/coshhvo-com/security/coshhvo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coshhvo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coshhvo.com/
- group: docs
  title: ''
  type: APIReference
  url: https://coshhvo.com/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://coshhvo.com/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://coshhvo.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coshhvo.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coshhvo.com/privacy/
created: '2026-10-29'
description: 'Coshhvo provides free worksheets that size and price a firm''s risk assessment and COSHH programme from its own activities and substances, and a paid plan that keeps every assessment, sheet, near miss and incident as a record with a date, an author and a review date. 2 free worksheets for the person who writes the risk assessments: what the programme costs, when each one is due, and what the COSHH file has to hold.'
image: https://coshhvo.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at coshhvo.com.
  name: coshhvo-com MCP Server
  slug: coshhvo-com-mcp-yml
modified: '2026-10-29'
name: coshhvo-com
nav: Providers
network: true
overview: 'coshhvo-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Safety, RiskAssessment, and COSHH.


  coshhvo-com''s developer surface includes authentication, API reference, support, pricing, and 19 more developer resources.'
plans:
- name: Coshhvo Com Plans Pricing
  plan_count: 2
  slug: coshhvo-com-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Coshhvo Com Rate Limits
  slug: coshhvo-com-rate-limits
scopes:
- name: Coshhvo Com Scopes
  scope_count: 0
  slug: coshhvo-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 46.3
    catalog_earned_first_party: 8.0
    catalog_gap: 68.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Coshhvo Com Authentication
  slug: coshhvo-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Coshhvo Com Domain Security
  slug: coshhvo-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Coshhvo Com Vulnerability Disclosure
  slug: coshhvo-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: coshhvo-com
tags:
- Company
- Health
- Safety
- RiskAssessment
- COSHH
- Software
website: https://coshhvo.com/
---
