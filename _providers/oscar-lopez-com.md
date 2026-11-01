---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: near-conformant
    agent_skills: unknown
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Oscar Lopez Com Agentic Access
  operation_count: 6
  slug: oscar-lopez-com-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: Daily source-cited Argentina food and beverage price index dataset.
  name: Argentina Food & Beverage Price Index API
  slug: price-index-api
- description: Source-cited record of how AI products handle your data.
  name: AI Vendor Data-Trust Index API
  slug: ai-trust-index-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/oscar-lopez-com/agentic-access/oscar-lopez-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/oscar-lopez-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/oscar-lopez-com/plans/oscar-lopez-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/oscar-lopez-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/oscar-lopez-com/rules/oscar-lopez-com-rules.yml
  title: ''
  type: Spectral
  url: rules/oscar-lopez-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/oscar-lopez-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/oscar-lopez-com/changelog/oscar-lopez-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/oscar-lopez-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/oscar-lopez-com/conformance/oscar-lopez-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/oscar-lopez-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/oscar-lopez-com/llms/oscar-lopez-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/oscar-lopez-com-llms.txt
- group: other
  href: https://artifacts.apis.io/oscar-lopez-com/a2a/oscar-lopez-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/oscar-lopez-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/oscar-lopez-com/well-known/oscar-lopez-com-data-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/oscar-lopez-com-data-security.txt
- group: agent
  href: https://artifacts.apis.io/oscar-lopez-com/well-known/oscar-lopez-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/oscar-lopez-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/oscar-lopez-com/hosts/oscar-lopez-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/oscar-lopez-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/oscar-lopez-com/vendors/oscar-lopez-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/oscar-lopez-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/oscar-lopez-com/security/oscar-lopez-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oscar-lopez-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://oscar-lopez.com/
created: '2026-10-29'
description: Oscar E. López, Ph.D. is an academic researcher and lecturer at the University of Massachusetts Amherst, specializing in information systems, business intelligence, data analytics, artificial intelligence in business, and online privacy. This site serves as his professional profile, showcasing his research interests, publications, and academic contributions. While listed as a company stub in the API Evangelist network, the entity primarily represents an individual scholar rather than a commercial organization, providing insight into his expertise and academic activities.
layout: provider
modified: '2026-10-29'
name: oscar-lopez-com
nav: Providers
network: true
overview: 'oscar-lopez-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Argentina Food & Beverage Price Index API, and 1 more. Tagged areas include Academic, Researcher, Information-Systems, Data-Analytics, and Artificial-Intelligence.


  The oscar-lopez-com catalog on APIs.io includes 1 Spectral governance ruleset.


  oscar-lopez-com''s developer surface includes changelog and 13 more developer resources.'
plans:
- name: Oscar Lopez Com Plans Pricing
  plan_count: 2
  slug: oscar-lopez-com-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Oscar Lopez Com Rate Limits
  slug: oscar-lopez-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 46
  extends:
  - spectral:oas
  name: oscar-lopez-com API Rules
  rule_count: 5
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 1
  slug: oscar-lopez-com-rules
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 47.5
    catalog_earned_first_party: 8.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 42.2
    developer_ergonomics: 16.0
    discoverability: 62.5
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 10.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Oscar Lopez Com Domain Security
  slug: oscar-lopez-com-domain-security
  summary_line: TLSv1.3
skill_count: 2
skills:
- name: ai-trust-index-api
  slug: oscar-lopez-com-ai-trust-index-api
- name: price-index-api
  slug: oscar-lopez-com-price-index-api
slug: oscar-lopez-com
tags:
- Academic
- Researcher
- Information-Systems
- Data-Analytics
- Artificial-Intelligence
website: https://oscar-lopez.com/
---
