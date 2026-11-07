---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Calculator Tools Agentic Access
  operation_count: 5
  slug: calculator-tools-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.calculator.tools/
  baseurl_source: declared
  description: The Openai API from Calculator Tools — 5 operation(s) for openai.
  name: Calculator Tools Openai API
  slug: calculator-tools-openai-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/calculator-tools/agentic-access/calculator-tools-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/calculator-tools-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/calculator-tools/rules/calculator-tools-rules.yml
  title: ''
  type: Spectral
  url: rules/calculator-tools-rules.yml
- group: design
  href: https://artifacts.apis.io/calculator-tools/conformance/calculator-tools-conformance.yml
  title: ''
  type: Conformance
  url: conformance/calculator-tools-conformance.yml
- group: agent
  href: https://artifacts.apis.io/calculator-tools/llms/calculator-tools-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/calculator-tools-llms.txt
- group: agent
  href: https://artifacts.apis.io/calculator-tools/well-known/calculator-tools-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/calculator-tools-well-known.yml
- group: other
  href: https://artifacts.apis.io/calculator-tools/hosts/calculator-tools-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calculator-tools-hosts.yml
- group: other
  href: https://artifacts.apis.io/calculator-tools/vendors/calculator-tools-vendors.yml
  title: ''
  type: Vendors
  url: vendors/calculator-tools-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://calculator.tools/user/login/
- group: auth
  href: https://artifacts.apis.io/calculator-tools/security/calculator-tools-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calculator-tools-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://calculator.tools/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://calculator.tools/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calculator.tools/privacy-policy/
created: '2026-11-03'
description: Calculator Tools provides an AI-powered no‑code platform that lets users instantly create apps, calculators, websites, tools, or games. By describing what they want in natural language, the AI generates fully functional code and deploys it online for free, enabling rapid prototyping and sharing with friends. The service emphasizes ease of use, instant results, and a wide range of possible creations, positioning itself as a versatile tool for developers and non‑technical creators alike.
image: https://calculator.tools/images/og-image.png
layout: provider
modified: '2026-11-03'
name: Calculator Tools
nav: Providers
network: true
overview: 'Calculator Tools publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Openai API. Tagged areas include Artificial Intelligence, No-Code, Platform, Calculator, and Tools.


  The Calculator Tools catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 71
  extends:
  - spectral:oas
  name: Calculator Tools API Rules
  rule_count: 30
  severity_counts:
    error: 28
    hint: 0
    info: 1
    warn: 1
  slug: calculator-tools-rules
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 41.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Calculator Tools Domain Security
  slug: calculator-tools-domain-security
  summary_line: TLSv1.3
slug: calculator-tools
tags:
- Artificial Intelligence
- No-Code
- Platform
- Calculator
- Tools
- Automation
website: https://calculator.tools/
---
