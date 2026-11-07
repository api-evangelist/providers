---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 11.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Dsarvo Com Agentic Access
  operation_count: 1
  slug: dsarvo-com-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Dataset API providing privacy compliance data via MCP tools.
  name: Dsarvo API
  slug: dsarvo-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/dsarvo-com/agentic-access/dsarvo-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dsarvo-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/dsarvo-com/plans/dsarvo-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dsarvo-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dsarvo-com/rules/dsarvo-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dsarvo-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dsarvo-com/vocabulary/dsarvo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dsarvo-com-vocabulary.yml
- group: auth
  title: ''
  type: Security
  url: https://dsarvo.com/terms
- group: design
  href: https://artifacts.apis.io/dsarvo-com/errors/dsarvo-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dsarvo-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dsarvo-com/conformance/dsarvo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dsarvo-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dsarvo-com/llms/dsarvo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dsarvo-com-llms.txt
- group: build
  href: https://artifacts.apis.io/dsarvo-com/mcp/dsarvo-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dsarvo-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/dsarvo-com/mcp/dsarvo-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dsarvo-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/dsarvo-com/well-known/dsarvo-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dsarvo-com-security.txt
- group: auth
  href: https://artifacts.apis.io/dsarvo-com/well-known/dsarvo-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dsarvo-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/dsarvo-com/well-known/dsarvo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dsarvo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dsarvo-com/hosts/dsarvo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dsarvo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dsarvo-com/vendors/dsarvo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dsarvo-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dsarvo.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://dsarvo.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dsarvo.com/privacy/
- group: auth
  href: https://artifacts.apis.io/dsarvo-com/authentication/dsarvo-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dsarvo-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dsarvo-com/security/dsarvo-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dsarvo-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dsarvo-com/security/dsarvo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dsarvo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dsarvo.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://dsarvo.com/pricing/
- group: operate
  title: ''
  type: Contact
  url: https://dsarvo.com/contact/
created: '2026-11-06'
description: Dsarvo provides software solutions for small companies, offering free builders to size privacy paperwork. Their platform helps firms generate disclosures, manage vendor agreements, and ensure compliance with privacy regulations. The site showcases sample firms with multiple disclosures and vendor contracts, emphasizing ease of use and comprehensive privacy management tools.
image: https://dsarvo.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at dsarvo.com.
  name: Dsarvo MCP Server
  slug: dsarvo-com-mcp-yml
modified: '2026-11-06'
name: Dsarvo
nav: Providers
network: true
overview: 'Dsarvo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Privacy, Compliance, Software, and Small Business.


  The Dsarvo catalog on APIs.io includes 1 Spectral governance ruleset.


  Dsarvo''s developer surface includes support, authentication, pricing, and 21 more developer resources.'
plans:
- name: Dsarvo Com Plans Pricing
  plan_count: 2
  slug: dsarvo-com-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Dsarvo API Rules
  rule_count: 50
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 1
  slug: dsarvo-com-rules
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 50.8
    catalog_earned_first_party: 8.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
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
  name: Dsarvo Com Authentication
  slug: dsarvo-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dsarvo Com Domain Security
  slug: dsarvo-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Dsarvo Com Vulnerability Disclosure
  slug: dsarvo-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dsarvo-com
tags:
- Company
- Privacy
- Compliance
- Software
- Small Business
website: https://dsarvo.com/
---
