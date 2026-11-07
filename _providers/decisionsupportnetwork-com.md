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
    agent_skills: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Decisionsupportnetwork Com Agentic Access
  operation_count: 4
  slug: decisionsupportnetwork-com-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: REST API for discovering and routing to CCA verified Decision Support Assets.
  name: Decision Support Network API
  slug: decision-support-network-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/decisionsupportnetwork-com/agentic-access/decisionsupportnetwork-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/decisionsupportnetwork-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/decisionsupportnetwork-com/rules/decisionsupportnetwork-com-rules.yml
  title: ''
  type: Spectral
  url: rules/decisionsupportnetwork-com-rules.yml
- group: design
  href: https://artifacts.apis.io/decisionsupportnetwork-com/errors/decisionsupportnetwork-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/decisionsupportnetwork-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/decisionsupportnetwork-com/conformance/decisionsupportnetwork-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/decisionsupportnetwork-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/decisionsupportnetwork-com/hosts/decisionsupportnetwork-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/decisionsupportnetwork-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/decisionsupportnetwork-com/vendors/decisionsupportnetwork-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/decisionsupportnetwork-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/decisionsupportnetwork-com/security/decisionsupportnetwork-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/decisionsupportnetwork-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://decisionsupportnetwork.com/
- group: docs
  title: ''
  type: Documentation
  url: https://decisionsupportnetwork.com/docs
- group: company
  title: ''
  type: About
  url: https://decisionsupportnetwork.com/about
created: '2026-11-05'
description: Decision Support Network (DSN) provides a platform that connects humans and AI agents with verified decision-support tools, enabling better-informed choices across various domains. Powered by CCA, the service offers searchable tool listings, detailed documentation, and an API for programmatic access to decision-relevant resources, helping users discover the right tool for any decision scenario.
image: https://decisionsupportnetwork.com/og-image.png
layout: provider
modified: '2026-11-05'
name: Decision Support Network
nav: Providers
network: true
overview: 'Decision Support Network is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Decision Tools, AI Agents, Decision Support, Non-Profit, and Home Buying.


  The Decision Support Network catalog on APIs.io includes 1 Spectral governance ruleset.


  Decision Support Network''s developer surface includes documentation and 9 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 72
  extends:
  - spectral:oas
  name: Decision Support Network API Rules
  rule_count: 31
  severity_counts:
    error: 29
    hint: 0
    info: 1
    warn: 1
  slug: decisionsupportnetwork-com-rules
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 8.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Decisionsupportnetwork Com Domain Security
  slug: decisionsupportnetwork-com-domain-security
  summary_line: TLSv1.3
slug: decisionsupportnetwork-com
tags:
- Decision Tools
- AI Agents
- Decision Support
- Non-Profit
- Home Buying
- Health and Wellness
- Safety
website: https://decisionsupportnetwork.com/
---
