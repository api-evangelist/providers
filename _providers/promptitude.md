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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.promptitude.io
  baseurl_source: declared
  description: 'Promptitude API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Promptitude API
  slug: promptitude-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/promptitude/plans/promptitude-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/promptitude-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/promptitude/rules/promptitude-rules.yml
  title: ''
  type: Spectral
  url: rules/promptitude-rules.yml
- group: design
  href: https://artifacts.apis.io/promptitude/vocabulary/promptitude-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/promptitude-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/promptitude/authentication/promptitude-authentication.yml
  title: ''
  type: Authentication
  url: authentication/promptitude-authentication.yml
- group: design
  href: https://artifacts.apis.io/promptitude/lifecycle/promptitude-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/promptitude-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/promptitude/conformance/promptitude-conformance.yml
  title: ''
  type: Conformance
  url: conformance/promptitude-conformance.yml
- group: agent
  href: https://artifacts.apis.io/promptitude/llms/promptitude-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/promptitude-llms.txt
- group: auth
  href: https://artifacts.apis.io/promptitude/well-known/promptitude-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/promptitude-help-security.txt
- group: agent
  href: https://artifacts.apis.io/promptitude/well-known/promptitude-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/promptitude-well-known.yml
- group: other
  href: https://artifacts.apis.io/promptitude/hosts/promptitude-hosts.yml
  title: ''
  type: Hosts
  url: hosts/promptitude-hosts.yml
- group: other
  href: https://artifacts.apis.io/promptitude/vendors/promptitude-vendors.yml
  title: ''
  type: Vendors
  url: vendors/promptitude-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.promptitude.io/terms-impressum
- group: operate
  title: ''
  type: Support
  url: https://help.promptitude.io/
- group: operate
  title: ''
  type: Roadmap
  url: https://promptitude.io/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://promptitude.io/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.promptitude.io/changelog
- group: auth
  href: https://artifacts.apis.io/promptitude/security/promptitude-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/promptitude-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://promptitude.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.promptitude.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.promptitude.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.promptitude.io/#getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.promptitude.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.promptitude.io/blog
coverage:
  checked: '2026-10-18'
  detail: No OpenAPI/AsyncAPI/GraphQL spec found at the API host (api.promptitude.io) despite documentation pages.
  evidence:
  - status: 404
    url: https://api.promptitude.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: Promptitude provides a no‑code platform that lets developers and product teams integrate GPT‑based capabilities into applications and workflows quickly. Users can manage prompts, build AI assistants, automate flows, and leverage a suite of AI tools, all through an intuitive interface. The service offers features such as prompt libraries, AI‑assisted content creation, and enterprise‑grade customization, aiming to democratize access to advanced language models for a wide range of use‑cases.
image: https://cdn.prod.website-files.com/63da923dc22302cce176bba6/64f79d214e8135a8a2ea9d99_Promptitude%20_%20Home.webp
layout: provider
modified: '2026-10-18'
name: Promptitude
nav: Providers
network: true
overview: 'Promptitude is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, No-Code, Prompt Engineering, and Automation.


  The Promptitude catalog on APIs.io includes 1 Spectral governance ruleset.


  Promptitude''s developer surface includes authentication, support, changelog, documentation, getting-started guide, pricing, engineering blog, and 16 more developer resources.'
plans:
- name: Promptitude Plans Pricing
  plan_count: 7
  slug: promptitude-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Promptitude API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: promptitude-rules
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 35.6
    contract_quality: 11.9
    developer_ergonomics: 50.0
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Promptitude Authentication
  slug: promptitude-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Promptitude Domain Security
  slug: promptitude-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: promptitude
tags:
- Company
- Artificial Intelligence
- No-Code
- Prompt Engineering
- Automation
website: https://promptitude.io/
---
