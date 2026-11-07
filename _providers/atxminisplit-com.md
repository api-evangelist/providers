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
  band: human-only
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Atxminisplit Com Agentic Access
  operation_count: 2
  slug: atxminisplit-com-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: Request a flat-price mini split quote from Mini Split Reef ($2,000 per unit installed).
  name: ATX Mini Split Quote API
  slug: atx-mini-split-quote-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/atxminisplit-com/agentic-access/atxminisplit-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/atxminisplit-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/atxminisplit-com/rules/atxminisplit-com-rules.yml
  title: ''
  type: Spectral
  url: rules/atxminisplit-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/atxminisplit-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/atxminisplit-com/conformance/atxminisplit-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/atxminisplit-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/atxminisplit-com/llms/atxminisplit-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atxminisplit-com-llms.txt
- group: other
  href: https://artifacts.apis.io/atxminisplit-com/hosts/atxminisplit-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atxminisplit-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/atxminisplit-com/security/atxminisplit-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atxminisplit-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atxminisplit.com/
created: '2026-11-02'
description: ATX Mini Split provides a data‑driven ranking of licensed heating and air contractors in Austin, Texas. Using public licensing records and contractor websites, it compares 71 mini‑split installers, posted prices, financing options, warranties, and other services, offering transparent insights for consumers.
image: https://atxminisplit.com/favicon.svg
layout: provider
modified: '2026-11-02'
name: ATX Mini Split
nav: Providers
network: true
overview: 'ATX Mini Split is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include HVAC, Mini Split, Austin, Rankings, and Data.


  The ATX Mini Split catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 63
  extends:
  - spectral:oas
  name: ATX Mini Split API Rules
  rule_count: 22
  severity_counts:
    error: 20
    hint: 0
    info: 1
    warn: 1
  slug: atxminisplit-com-rules
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 1.8
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 8.5
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atxminisplit Com Domain Security
  slug: atxminisplit-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: atxminisplit-com-list-companies-skill
  slug: atxminisplit-com-list-companies-skill
- name: atxminisplit-com-quote-skill
  slug: atxminisplit-com-quote-skill
slug: atxminisplit-com
tags:
- HVAC
- Mini Split
- Austin
- Rankings
- Data
website: https://atxminisplit.com/
---
