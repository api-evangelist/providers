---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Towers Watson Agentic Access
  operation_count: 12
  slug: towers-watson-agentic-access
  summary_line: 12 operations · 4 acting
api_count: 5
apis:
- description: Benefits summary and enrollment status
  name: Towers Watson Benefits API
  slug: towers-watson-benefits-api
- description: HR service case management
  name: Towers Watson Cases API
  slug: towers-watson-cases-api
- description: HR content and communications management
  name: Towers Watson Content API
  slug: towers-watson-content-api
- description: Employee profile and engagement management
  name: Towers Watson Employees API
  slug: towers-watson-employees-api
- description: Total compensation and rewards statements
  name: Towers Watson Total Rewards API
  slug: towers-watson-total-rewards-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WTW HR Portal Benefits API
  slug: open-towers-watson-benefits-api
- collection_type: open
  name: WTW HR Portal Benefits Cases API
  slug: open-towers-watson-cases-api
- collection_type: open
  name: WTW HR Portal Benefits Content API
  slug: open-towers-watson-content-api
- collection_type: open
  name: WTW HR Portal Benefits Employees API
  slug: open-towers-watson-employees-api
- collection_type: open
  name: WTW HR Portal Benefits Total Rewards API
  slug: open-towers-watson-total-rewards-api
- collection_type: open
  name: WTW HR Portal
  slug: open-wtw-hr-portal
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/towers-watson-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/towers-watson-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/towers-watson-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WTW-IM
- group: company
  title: ''
  type: Website
  url: https://www.wtwco.com/
- group: other
  title: ''
  type: Developer
  url: https://www.wtwco.com/en-us/solutions/products
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wtw
- group: design
  title: ''
  type: Rules
  url: rules/wtw-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/towers-watson-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/towers-watson-context.jsonld
created: '2026-03-24'
description: Towers Watson was a global professional services company that provided risk management, actuarial, human capital, and investment consulting services before merging with Willis Group to form Willis Towers Watson (now WTW) in 2016. WTW provides data-driven, insight-led solutions in risk, broking, HR consulting, and benefits administration across 140+ countries. WTW's software products include the HR Portal for employee benefits communication, benefits administration systems, compensation management tools, and actuarial modeling platforms.
examples:
- key_count: 2
  name: Wtw Get Employee Total Rewards Example
  slug: wtw-get-employee-total-rewards-example
finops:
- name: Towers Watson Finops
  service_category: API
  slug: towers-watson-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/towers-watson.png
json_schemas:
- name: Employee
  property_count: 11
  slug: wtw-employee
json_structures:
- name: Wtw Employee Structure
  property_count: 0
  slug: wtw-employee-structure
jsonld:
- class_count: 40
  name: Towers Watson Context
  property_count: 0
  slug: towers-watson-context
layout: provider
modified: '2026-05-19'
name: Towers Watson
nav: Providers
network: true
overview: 'Towers Watson publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Benefits API, Cases API, Content API, and 2 more. Tagged areas include Human Resources, Risk Management, Benefits, Consulting, and Actuarial.


  The Towers Watson catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Towers Watson''s developer surface includes authentication and 9 more developer resources.'
plans:
- name: Towers Watson Plans Pricing
  plan_count: 3
  slug: towers-watson-plans-pricing
press:
- date: '2026-05-25'
  title: Willis Towers Watson earnings loom as AI questions intensify
  url: https://www.investing.com/news/earnings/willis-towers-watson-earnings-loom-as-ai-questions-intensify-93CH-4646311
- date: '2026-05-25'
  title: Employers set to rapidly expand AI use in health and
  url: https://www.globenewswire.com/news-release/2026/05/19/3297669/0/en/employers-set-to-rapidly-expand-ai-use-in-health-and-benefits-but-execution-gaps-remain-wtw-survey-finds.html
- date: '2026-05-25'
  title: WTW adds AI capabilities to its financial modelling software
  url: https://www.wtwco.com/en-gb/news/2024/12/wtw-adds-game-changing-ai-capabilities-to-its-financial-modelling-and-reporting-software-for-life
- date: '2026-05-25'
  title: 'WTW: Employers aiming to bulk up AI use for health and ...'
  url: https://www.fiercehealthcare.com/payers/wtw-employers-aiming-bulk-ai-use-health-and-benefits
- date: '2026-05-25'
  title: What an unforgettable Innovation Day London | AI Made Real ...
  url: https://www.instagram.com/reel/DYg0Pl2jvUE/
random_paper: 48
rate_limits:
- limit_count: 5
  name: Towers Watson Rate Limits
  slug: towers-watson-rate-limits
rules:
- name: Towers Watson API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: towers-watson-jsonschema-spectral-rules
- name: Towers Watson API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 8
  slug: towers-watson-spectral-rules
- name: Towers Watson API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 4
  slug: wtw-spectral-rules
score:
  band: thin
  composite: 36.5
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 66.6
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 13.2
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 25.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Towers Watson Authentication
  slug: towers-watson-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Towers Watson Domain Security
  slug: towers-watson-domain-security
  summary_line: TLSv1.3 · DMARC
slug: towers-watson
tags:
- Human Resources
- Risk Management
- Benefits
- Consulting
- Actuarial
- Insurance Brokerage
- Human Capital
website: https://www.wtwco.com/
---
