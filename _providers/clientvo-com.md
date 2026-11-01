---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Clientvo Com Agentic Access
  operation_count: 18
  slug: clientvo-com-agentic-access
  summary_line: 18 operations · 14 acting
api_count: 1
apis:
- baseURL: https://clientvo.com
  baseurl_source: declared
  description: dataset
  name: clientvo-com Dataset API
  slug: clientvo-com-dataset-api
- baseURL: https://clientvo.com
  baseurl_source: declared
  description: The mcp API from clientvo-com — 1 operation(s) for mcp.
  name: clientvo-com MCP API
  slug: clientvo-com-mcp-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/clientvo-com/agentic-access/clientvo-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/clientvo-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/clientvo-com/plans/clientvo-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clientvo-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/clientvo-com/rules/clientvo-com-rules.yml
  title: ''
  type: Spectral
  url: rules/clientvo-com-rules.yml
- group: design
  href: https://artifacts.apis.io/clientvo-com/vocabulary/clientvo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clientvo-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/clientvo-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://clientvo.com/terms
- group: design
  href: https://artifacts.apis.io/clientvo-com/errors/clientvo-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clientvo-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/clientvo-com/conformance/clientvo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clientvo-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/clientvo-com/llms/clientvo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clientvo-com-llms.txt
- group: build
  href: https://artifacts.apis.io/clientvo-com/mcp/clientvo-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/clientvo-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/clientvo-com/mcp/clientvo-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/clientvo-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/clientvo-com/well-known/clientvo-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clientvo-com-security.txt
- group: auth
  href: https://artifacts.apis.io/clientvo-com/well-known/clientvo-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clientvo-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/clientvo-com/well-known/clientvo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clientvo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/clientvo-com/hosts/clientvo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clientvo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/clientvo-com/vendors/clientvo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clientvo-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/clientvo-com/packages/clientvo-com-packages.yml
  title: ''
  type: SDKs
  url: packages/clientvo-com-packages.yml
- group: build
  href: https://artifacts.apis.io/clientvo-com/packages/clientvo-com-packages.yml
  title: ''
  type: Packages
  url: packages/clientvo-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clientvo.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clientvo.com/privacy/
- group: start
  title: ''
  type: GettingStarted
  url: https://clientvo.com/answers/kyc-onboarding/
- group: auth
  href: https://artifacts.apis.io/clientvo-com/authentication/clientvo-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clientvo-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/clientvo-com/security/clientvo-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clientvo-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/clientvo-com/security/clientvo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clientvo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clientvo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://clientvo.com/tools/
- group: operate
  title: ''
  type: Support
  url: https://clientvo.com/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://clientvo.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.clientvo.com/?upgrade=pro
created: '2026-10-29'
description: 'Clientvo is software for the person at a small United States firm regulated for who its customers are -- a fintech, a lender, a payments company, a money services business, a marketplace -- who owns KYC. It publishes a free know your customer requirements checklist that sizes what has to be collected on a customer at each risk rating, and sells a plan that keeps the file afterwards: every customer, its risk rating, the identity and ownership evidence held against it, who approved it and the date it is next due a review. It runs no screening engine, monitors no transactions, captures no identity documents and publishes no vendor ranking.'
image: https://clientvo.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at clientvo.com.
  name: clientvo-com MCP Server
  slug: clientvo-com-mcp-yml
modified: '2026-10-29'
name: clientvo-com
nav: Providers
network: true
overview: 'clientvo-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Dataset API and MCP API. Tagged areas include Company, Fintech, Payments, Lending, and Compliance.


  The clientvo-com catalog on APIs.io includes 1 Spectral governance ruleset.


  clientvo-com''s developer surface includes getting-started guide, authentication, documentation, support, pricing, signup flow, and 23 more developer resources.'
plans:
- name: Clientvo Com Plans Pricing
  plan_count: 2
  slug: clientvo-com-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Clientvo Com Rate Limits
  slug: clientvo-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: clientvo-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: clientvo-com-rules
score:
  band: developing
  composite: 47.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 50.8
    catalog_earned_first_party: 8.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 47.4
    developer_ergonomics: 51.7
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 27.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Clientvo Com Authentication
  slug: clientvo-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Clientvo Com Domain Security
  slug: clientvo-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Clientvo Com Vulnerability Disclosure
  slug: clientvo-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: dataset-search
  slug: dataset-search
slug: clientvo-com
tags:
- Company
- Fintech
- Payments
- Lending
- Compliance
- KYC
website: https://clientvo.com/
---
