---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Fizzl Eu Agentic Access
  operation_count: 2
  slug: fizzl-eu-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: 'The inkoper: one call buys the right paid x402 API for your agent, picked by the platform.'
  name: Fizzl Buy API
  slug: fizzl-buy-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/fizzl-eu/agentic-access/fizzl-eu-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fizzl-eu-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/fizzl-eu/rules/fizzl-eu-rules.yml
  title: ''
  type: Spectral
  url: rules/fizzl-eu-rules.yml
- group: design
  href: https://artifacts.apis.io/fizzl-eu/errors/fizzl-eu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fizzl-eu-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fizzl-eu/conformance/fizzl-eu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fizzl-eu-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fizzl-eu/llms/fizzl-eu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fizzl-eu-llms.txt
- group: agent
  href: https://artifacts.apis.io/fizzl-eu/well-known/fizzl-eu-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fizzl-eu-well-known.yml
- group: other
  href: https://artifacts.apis.io/fizzl-eu/hosts/fizzl-eu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fizzl-eu-hosts.yml
- group: other
  href: https://artifacts.apis.io/fizzl-eu/vendors/fizzl-eu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fizzl-eu-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fizzl.eu/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fizzl.eu/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Fizzl13
- group: auth
  href: https://artifacts.apis.io/fizzl-eu/security/fizzl-eu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fizzl-eu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fizzl.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://fizzl.eu/guides/
created: '2026-10-29'
description: Fizzl provides a suite of tools that enable AI agents to make and verify payments autonomously. By checking payments before an agent signs them and after responses, Fizzl ensures safe transactions across multiple payment networks without requiring API keys. The platform offers live services, a wallet, and a marketplace of over 50,000 paid endpoints, supporting AI-driven applications in finance, data retrieval, and more.
image: https://fizzl.eu/og-image.jpg?v=4
layout: provider
modified: '2026-10-29'
name: fizzl-eu
nav: Providers
network: true
overview: 'fizzl-eu is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Payments, Automation, Tools, and Platform.


  The fizzl-eu catalog on APIs.io includes 1 Spectral governance ruleset.


  fizzl-eu''s developer surface includes documentation and 13 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: fizzl-eu API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: fizzl-eu-rules
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 20.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Fizzl Eu Domain Security
  slug: fizzl-eu-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fizzl-eu
tags:
- AI
- Payments
- Automation
- Tools
- Platform
website: https://fizzl.eu/
---
