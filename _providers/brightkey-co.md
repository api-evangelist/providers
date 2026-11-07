---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    auth_clarity: false
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Brightkey Co Agentic Access
  operation_count: 7
  slug: brightkey-co-agentic-access
  summary_line: 7 operations · 1 acting
api_count: 1
apis:
- baseURL: https://brightkey.co/v1
  baseurl_source: declared
  description: The Answers API from BrightKey — 1 operation(s) for answers.
  name: BrightKey Answers API
  slug: brightkey-co-answers-api
- baseURL: https://brightkey.co/v1
  baseurl_source: declared
  description: The Compare API from BrightKey — 1 operation(s) for compare.
  name: BrightKey Compare API
  slug: brightkey-co-compare-api
- baseURL: https://brightkey.co/v1
  baseurl_source: declared
  description: The Roi API from BrightKey — 2 operation(s) for roi.
  name: BrightKey Roi API
  slug: brightkey-co-roi-api
- baseURL: https://brightkey.co/v1
  baseurl_source: declared
  description: The Schools API from BrightKey — 1 operation(s) for schools.
  name: BrightKey Schools API
  slug: brightkey-co-schools-api
- baseURL: https://brightkey.co/v1
  baseurl_source: declared
  description: The Universities API from BrightKey — 2 operation(s) for universities.
  name: BrightKey Universities API
  slug: brightkey-co-universities-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/brightkey-co/agentic-access/brightkey-co-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/brightkey-co-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/brightkey-co/plans/brightkey-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brightkey-co-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/brightkey-co/rules/brightkey-co-rules.yml
  title: ''
  type: Spectral
  url: rules/brightkey-co-rules.yml
- group: agent
  href: https://artifacts.apis.io/brightkey-co/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/brightkey-co/errors/brightkey-co-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/brightkey-co-problem-types.yml
- group: design
  href: https://artifacts.apis.io/brightkey-co/conformance/brightkey-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brightkey-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/brightkey-co/llms/brightkey-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brightkey-co-llms.txt
- group: other
  href: https://artifacts.apis.io/brightkey-co/hosts/brightkey-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brightkey-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/brightkey-co/vendors/brightkey-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brightkey-co-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brightkey.co/en/terms
- group: commercial
  title: ''
  type: Pricing
  url: https://brightkey.co/en/pricing
- group: other
  title: ''
  type: Leadership
  url: https://brightkey.co/en/about/team
- group: company
  title: ''
  type: Blog
  url: https://brightkey.co/en/blog
- group: auth
  href: https://artifacts.apis.io/brightkey-co/security/brightkey-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brightkey-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brightkey.co/
- group: docs
  title: ''
  type: Documentation
  url: https://brightkey.co/en/about
- group: operate
  title: ''
  type: Support
  url: https://brightkey.co/en/contact
created: '2026-11-03'
description: BrightKey provides independent strategic education consulting for international families across Asia Pacific. It offers bilingual EN/ZH coverage of 299 universities in 55 countries, helping with school selection, university admissions, and career discovery for ages 0-18. The service operates from Singapore and Tokyo, emphasizing no payments from schools or agents.
layout: provider
modified: '2026-11-03'
name: BrightKey
nav: Providers
network: true
overview: 'BrightKey publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Answers API, Compare API, Roi API, and 2 more. Tagged areas include Education, Consulting, International, Family, and Asia Pacific.


  The BrightKey catalog on APIs.io includes 1 Spectral governance ruleset.


  BrightKey''s developer surface includes pricing, engineering blog, documentation, support, and 13 more developer resources.'
plans:
- name: Brightkey Co Plans Pricing
  plan_count: 4
  slug: brightkey-co-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: BrightKey API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: brightkey-co-rules
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 51.5
    catalog_earned_first_party: 12.0
    catalog_gap: 63.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 42.5
    developer_ergonomics: 10.1
    discoverability: 63.4
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brightkey Co Domain Security
  slug: brightkey-co-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: brightkey-co-compare-universities
  slug: brightkey-co-compare-universities
slug: brightkey-co
tags:
- Education
- Consulting
- International
- Family
- Asia Pacific
website: https://brightkey.co/
---
