---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 23.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Calculbrutennet Com Agentic Access
  operation_count: 12
  slug: calculbrutennet-com-agentic-access
  summary_line: 12 operations · 10 acting
api_count: 1
apis:
- baseURL: https://calculbrutennet.com
  baseurl_source: declared
  description: dataset
  name: Calcul Brut en Net Dataset API
  slug: calculbrutennet-com-dataset-api
- baseURL: https://calculbrutennet.com
  baseurl_source: declared
  description: enquiry
  name: Calcul Brut en Net Enquiry API
  slug: calculbrutennet-com-enquiry-api
- baseURL: https://calculbrutennet.com
  baseurl_source: declared
  description: The mcp API from Calcul Brut en Net — 1 operation(s) for mcp.
  name: Calcul Brut en Net MCP API
  slug: calculbrutennet-com-mcp-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/calculbrutennet-com/agentic-access/calculbrutennet-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/calculbrutennet-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/calculbrutennet-com/rules/calculbrutennet-com-rules.yml
  title: ''
  type: Spectral
  url: rules/calculbrutennet-com-rules.yml
- group: design
  href: https://artifacts.apis.io/calculbrutennet-com/vocabulary/calculbrutennet-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/calculbrutennet-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/calculbrutennet-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://calculbrutennet.com/terms
- group: design
  href: https://artifacts.apis.io/calculbrutennet-com/errors/calculbrutennet-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/calculbrutennet-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/calculbrutennet-com/conformance/calculbrutennet-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/calculbrutennet-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/calculbrutennet-com/llms/calculbrutennet-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/calculbrutennet-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/calculbrutennet-com/well-known/calculbrutennet-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/calculbrutennet-com-security.txt
- group: agent
  href: https://artifacts.apis.io/calculbrutennet-com/well-known/calculbrutennet-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/calculbrutennet-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/calculbrutennet-com/hosts/calculbrutennet-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calculbrutennet-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/calculbrutennet-com/vendors/calculbrutennet-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/calculbrutennet-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://calculbrutennet.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calculbrutennet.com/privacy/
- group: auth
  href: https://artifacts.apis.io/calculbrutennet-com/authentication/calculbrutennet-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/calculbrutennet-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/calculbrutennet-com/security/calculbrutennet-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/calculbrutennet-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/calculbrutennet-com/security/calculbrutennet-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calculbrutennet-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://calculbrutennet.com/
created: '2026-11-03'
description: Calcul Brut en Net provides French social security and labor code rules, presenting 16 social rules across 5 payroll topics, each with its own page and reading date, cited verbatim from official sources. The site offers detailed explanations of salary, SMIC, social contributions, resignation notice, contract termination, and professional expenses, serving as a reference for employers and employees in France.
image: https://calculbrutennet.com/og.png
layout: provider
modified: '2026-11-03'
name: Calcul Brut en Net
nav: Providers
network: true
overview: 'Calcul Brut en Net publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Dataset API, Enquiry API, and MCP API. Tagged areas include French, Payroll, Social Security, Labor Law, and CalculBrutEnNet.


  The Calcul Brut en Net catalog on APIs.io includes 1 Spectral governance ruleset.


  Calcul Brut en Net''s developer surface includes authentication and 17 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Calcul Brut en Net API Rules
  rule_count: 53
  severity_counts:
    error: 43
    hint: 0
    info: 4
    warn: 6
  slug: calculbrutennet-com-rules
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 48.8
    developer_ergonomics: 13.7
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Calculbrutennet Com Authentication
  slug: calculbrutennet-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Calculbrutennet Com Domain Security
  slug: calculbrutennet-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Calculbrutennet Com Vulnerability Disclosure
  slug: calculbrutennet-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: calculbrutennet-com-enquiry-process
  slug: calculbrutennet-com-enquiry-process
- name: calculbrutennet-com-find-top-rows
  slug: calculbrutennet-com-find-top-rows
slug: calculbrutennet-com
tags:
- French
- Payroll
- Social Security
- Labor Law
- CalculBrutEnNet
- Company
website: https://calculbrutennet.com/
---
