---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Cypruscompanycost Com Agentic Access
  operation_count: 5
  slug: cypruscompanycost-com-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 1
apis:
- baseURL: https://cypruscompanycost.com
  baseurl_source: declared
  description: enquiry
  name: Cyprus Company Cost Enquiry API
  slug: cypruscompanycost-com-enquiry-api
- baseURL: https://cypruscompanycost.com
  baseurl_source: declared
  description: The mcp API from Cyprus Company Cost — 1 operation(s) for mcp.
  name: Cyprus Company Cost MCP API
  slug: cypruscompanycost-com-mcp-api
artifact_total: 11
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://cypruscompanycost.com/mcp
- group: agent
  href: https://artifacts.apis.io/cypruscompanycost-com/agentic-access/cypruscompanycost-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cypruscompanycost-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/cypruscompanycost-com/rate-limits/cypruscompanycost-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cypruscompanycost-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/cypruscompanycost-com/rules/cypruscompanycost-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cypruscompanycost-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cypruscompanycost-com/vocabulary/cypruscompanycost-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cypruscompanycost-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cypruscompanycost-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cypruscompanycost-com/conventions/cypruscompanycost-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cypruscompanycost-com-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://cypruscompanycost.com/terms
- group: design
  href: https://artifacts.apis.io/cypruscompanycost-com/errors/cypruscompanycost-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cypruscompanycost-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cypruscompanycost-com/conformance/cypruscompanycost-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cypruscompanycost-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/cypruscompanycost-com/overlays/cypruscompanycost-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cypruscompanycost-com-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/cypruscompanycost-com/llms/cypruscompanycost-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cypruscompanycost-com-llms.txt
- group: build
  href: https://artifacts.apis.io/cypruscompanycost-com/mcp/cypruscompanycost-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cypruscompanycost-com-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/cypruscompanycost-com/well-known/cypruscompanycost-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cypruscompanycost-com-security.txt
- group: agent
  href: https://artifacts.apis.io/cypruscompanycost-com/well-known/cypruscompanycost-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cypruscompanycost-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cypruscompanycost-com/hosts/cypruscompanycost-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cypruscompanycost-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cypruscompanycost-com/vendors/cypruscompanycost-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cypruscompanycost-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cypruscompanycost-com/authentication/cypruscompanycost-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cypruscompanycost-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cypruscompanycost-com/security/cypruscompanycost-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cypruscompanycost-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cypruscompanycost-com/security/cypruscompanycost-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cypruscompanycost-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cypruscompanycost.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cypruscompanycost.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cypruscompanycost.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://cypruscompanycost.com/contact/
created: '2026-11-05'
description: 'Cyprus Company Cost (cypruscompanycost.com) is a free introduction and reference site on what a Cyprus company costs to form and keep, built from the Cyprus Registrar of Companies'' published fee schedule and the Tax Department''s rates: name approval and incorporation fees, annual return filings, the repealed €350 annual levy, and the 15% corporate income tax from 2026. It publishes citable datasets (a Cyprus Formation Price Index, registrar statutory fees, company tax rates), guides, and a quote form that connects users with Cyprus formation firms. Listed in the API Evangelist network via the MCP registry harvest.'
image: https://cypruscompanycost.com/og.png
layout: provider
mcp_servers:
- description: ''
  name: Cyprus Company Cost MCP Server
  slug: mcp
modified: '2026-11-05'
name: Cyprus Company Cost
nav: Providers
network: true
overview: 'Cyprus Company Cost publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Enquiry API and MCP API. Tagged areas include Company, Cyprus, Company Formation, Corporate Tax, and Business Registration.


  The Cyprus Company Cost catalog on APIs.io includes 1 Spectral governance ruleset.


  Cyprus Company Cost''s developer surface includes authentication, support, and 22 more developer resources.'
plans:
- name: Cypruscompanycost Com Plans Pricing
  plan_count: 0
  slug: cypruscompanycost-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Cypruscompanycost Com Rate Limits
  slug: cypruscompanycost-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Cyprus Company Cost API Rules
  rule_count: 48
  severity_counts:
    error: 43
    hint: 0
    info: 4
    warn: 1
  slug: cypruscompanycost-com-rules
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 50.8
    catalog_earned_first_party: 8.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 47.4
    developer_ergonomics: 18.5
    discoverability: 65.0
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cypruscompanycost Com Authentication
  slug: cypruscompanycost-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cypruscompanycost Com Domain Security
  slug: cypruscompanycost-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cypruscompanycost Com Vulnerability Disclosure
  slug: cypruscompanycost-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: cypruscompanycost-com-submit-formation-enquiry
  slug: cypruscompanycost-com-submit-formation-enquiry
slug: cypruscompanycost-com
tags:
- Company
- Cyprus
- Company Formation
- Corporate Tax
- Business Registration
- Datasets
- Fees
website: https://cypruscompanycost.com/
---
