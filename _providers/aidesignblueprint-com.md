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
    agent_card: flavored
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'AI Design Blueprint API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AI Design Blueprint API
  slug: aidesignblueprint-com-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/aidesignblueprint-com/plans/aidesignblueprint-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aidesignblueprint-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aidesignblueprint-com/rules/aidesignblueprint-com-rules.yml
  title: ''
  type: Spectral
  url: rules/aidesignblueprint-com-rules.yml
- group: design
  href: https://artifacts.apis.io/aidesignblueprint-com/vocabulary/aidesignblueprint-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aidesignblueprint-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aidesignblueprint-com/conformance/aidesignblueprint-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aidesignblueprint-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aidesignblueprint-com/llms/aidesignblueprint-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aidesignblueprint-com-llms.txt
- group: other
  href: https://artifacts.apis.io/aidesignblueprint-com/a2a/aidesignblueprint-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aidesignblueprint-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/aidesignblueprint-com/well-known/aidesignblueprint-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aidesignblueprint-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aidesignblueprint-com/hosts/aidesignblueprint-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aidesignblueprint-com-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://aidesignblueprint.com/en/principles/cluster/trust
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aidesignblueprint
- group: docs
  title: ''
  type: Documentation
  url: https://aidesignblueprint.com/en/guides
- group: auth
  href: https://artifacts.apis.io/aidesignblueprint-com/security/aidesignblueprint-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aidesignblueprint-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aidesignblueprint.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://aidesignblueprint.com/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aidesignblueprint.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aidesignblueprint.com/en/privacy
- group: operate
  title: ''
  type: Support
  url: https://aidesignblueprint.com/en/support
created: '2026-11-01'
description: AI Design Blueprint provides a doctrine and runtime standard for production agentic AI. It offers principles, examples, runtime architecture guidance, privacy policies, pricing, and tools for building, validating, and deploying agentic systems. The platform includes a handbook, case studies, and integration with major AI coding assistants, aiming to help product designers, engineers, and founders create trustworthy, auditable AI agents.
image: https://aidesignblueprint.com/en/opengraph-image
layout: provider
modified: '2026-11-01'
name: AI Design Blueprint
nav: Providers
network: true
overview: 'AI Design Blueprint is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, AI Agents, Design, Platform, and Blueprints.


  The AI Design Blueprint catalog on APIs.io includes 1 Spectral governance ruleset.


  AI Design Blueprint''s developer surface includes documentation, pricing, support, and 14 more developer resources.'
plans:
- name: Aidesignblueprint Com Plans Pricing
  plan_count: 3
  slug: aidesignblueprint-com-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: AI Design Blueprint API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: aidesignblueprint-com-rules
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 51.3
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 2.6
  previous_composite: 30.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aidesignblueprint Com Domain Security
  slug: aidesignblueprint-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aidesignblueprint-com
tags:
- Artificial Intelligence
- AI Agents
- Design
- Platform
- Blueprints
website: https://aidesignblueprint.com/
---
