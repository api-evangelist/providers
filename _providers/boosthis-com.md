---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Boosthis provides an API for accessing performance monitoring data and AI-driven recommendations. Documentation is at the Connect your AI page.
  name: Boosthis API
  slug: boosthis-api
- description: 'Boosthis API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Boosthis API
  slug: boosthis-com-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/boosthis-com/plans/boosthis-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/boosthis-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/boosthis-com/rules/boosthis-com-rules.yml
  title: ''
  type: Spectral
  url: rules/boosthis-com-rules.yml
- group: design
  href: https://artifacts.apis.io/boosthis-com/vocabulary/boosthis-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/boosthis-com-vocabulary.yml
- group: auth
  title: ''
  type: Security
  url: https://www.boosthis.com/trust#reporting
- group: design
  href: https://artifacts.apis.io/boosthis-com/conformance/boosthis-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/boosthis-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/boosthis-com/llms/boosthis-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boosthis-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/boosthis-com/mcp/boosthis-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/boosthis-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/boosthis-com/well-known/boosthis-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/boosthis-com-security.txt
- group: auth
  href: https://artifacts.apis.io/boosthis-com/well-known/boosthis-com-boosthis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/boosthis-com-boosthis-security.txt
- group: agent
  href: https://artifacts.apis.io/boosthis-com/well-known/boosthis-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boosthis-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/boosthis-com/hosts/boosthis-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boosthis-com-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.boosthis.com/trust
- group: operate
  title: ''
  type: Support
  url: https://www.boosthis.com/help
- group: operate
  title: ''
  type: StatusPage
  url: https://www.boosthis.com/status
- group: start
  title: ''
  type: Login
  url: https://www.boosthis.com/dashboard/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Boosthis
- group: auth
  href: https://artifacts.apis.io/boosthis-com/security/boosthis-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/boosthis-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/boosthis-com/security/boosthis-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boosthis-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.boosthis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.boosthis.com/docs/connect-your-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://www.boosthis.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.boosthis.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.boosthis.com/terms#privacy-policy
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract found despite documentation pages.
  evidence:
  - status: 0
    url: https://api.boosthis.com/openapi.json
  - status: 0
    url: https://api.boosthis.com/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Boosthis provides application performance monitoring across twelve programming languages, identifying slow code paths and offering AI‑driven recommendations for fixes. Their platform helps developers optimize apps with detailed metrics, actionable insights, and automated remediation suggestions, aiming to improve speed and reliability for modern software stacks.
image: https://www.boosthis.com/og/product-card.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.boosthis.com.
  name: Boosthis MCP Server
  slug: boosthis-com-mcp-yml
modified: '2026-11-02'
name: Boosthis
nav: Providers
network: true
overview: 'Boosthis is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include App Performance, Developer Tools, Web Performance, and AI Assistant.


  The Boosthis catalog on APIs.io includes 1 Spectral governance ruleset.


  Boosthis'' developer surface includes support, documentation, pricing, and 20 more developer resources.'
plans:
- name: Boosthis Com Plans Pricing
  plan_count: 5
  slug: boosthis-com-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 66
  extends:
  - spectral:oas
  name: Boosthis API Rules
  rule_count: 25
  severity_counts:
    error: 23
    hint: 0
    info: 1
    warn: 1
  slug: boosthis-com-rules
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 44.8
    catalog_earned_first_party: 12.0
    catalog_gap: 70.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 57.9
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 7.1
    discoverability: 48.3
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boosthis Com Domain Security
  slug: boosthis-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Boosthis Com Vulnerability Disclosure
  slug: boosthis-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: boosthis-com
tags:
- App Performance
- Developer Tools
- Web Performance
- AI Assistant
website: https://www.boosthis.com/
---
