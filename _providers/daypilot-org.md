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
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Daypilot Org Agentic Access
  operation_count: 18
  slug: daypilot-org-agentic-access
  summary_line: 18 operations · 2 acting
api_count: 1
apis:
- baseURL: https://builder.daypilot.org
  baseurl_source: declared
  description: Anonymous, read-only Builder capability discovery.
  name: DayPilot Discovery API
  slug: daypilot-org-discovery-api
- baseURL: https://builder.daypilot.org
  baseurl_source: declared
  description: Anonymous, stateless validation and direct project-archive generation. These POST operations deliberately grant no browser CORS permission.
  name: DayPilot Generation API
  slug: daypilot-org-generation-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/daypilot-org/agentic-access/daypilot-org-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/daypilot-org-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/daypilot-org/rules/daypilot-org-rules.yml
  title: ''
  type: Spectral
  url: rules/daypilot-org-rules.yml
- group: design
  href: https://artifacts.apis.io/daypilot-org/json-ld/daypilot-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/daypilot-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/daypilot-org/vocabulary/daypilot-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/daypilot-org-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/daypilot-org/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/daypilot-org/data-model/daypilot-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/daypilot-org-data-model.yml
- group: design
  href: https://artifacts.apis.io/daypilot-org/errors/daypilot-org-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/daypilot-org-problem-types.yml
- group: design
  href: https://artifacts.apis.io/daypilot-org/conformance/daypilot-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/daypilot-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/daypilot-org/llms/daypilot-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/daypilot-org-llms.txt
- group: agent
  href: https://artifacts.apis.io/daypilot-org/well-known/daypilot-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/daypilot-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/daypilot-org/hosts/daypilot-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/daypilot-org-hosts.yml
- group: build
  href: https://artifacts.apis.io/daypilot-org/packages/daypilot-org-packages.yml
  title: ''
  type: SDKs
  url: packages/daypilot-org-packages.yml
- group: build
  href: https://artifacts.apis.io/daypilot-org/packages/daypilot-org-packages.yml
  title: ''
  type: Packages
  url: packages/daypilot-org-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.daypilot.org/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.daypilot.org/legal/privacy-policy/
- group: start
  title: ''
  type: GettingStarted
  url: https://mcp.daypilot.org/
- group: auth
  href: https://artifacts.apis.io/daypilot-org/security/daypilot-org-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/daypilot-org-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/daypilot-org/security/daypilot-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/daypilot-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://daypilot.org/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.daypilot.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.daypilot.org/
- group: operate
  title: ''
  type: Support
  url: https://www.daypilot.org/support/
- group: other
  title: ''
  type: OpenSource
  url: https://www.daypilot.org/open-source/
created: '2026-11-05'
description: DayPilot provides HTML5 calendar, scheduler, and Gantt chart web components for building project management, resource planning, timeline visualization, and time‑tracking applications. With over 15 years of development, the components support JavaScript, TypeScript, React, Angular, and Vue, offering features like drag‑and‑drop, hierarchical resources, real‑time updates, and export to SVG/PNG. DayPilot also offers open‑source versions under the Apache License and commercial products for enterprise needs.
jsonld:
- class_count: 14
  name: Daypilot Org Context
  property_count: 44
  slug: daypilot-org-context
layout: provider
modified: '2026-11-05'
name: DayPilot
nav: Providers
network: true
overview: 'DayPilot publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Discovery API and Generation API. Tagged areas include Calendar, Scheduler, Gantt Chart, UI Components, and Open Source.


  The DayPilot catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DayPilot''s developer surface includes getting-started guide, documentation, support, and 20 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: DayPilot API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: daypilot-org-rules
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 47.9
    developer_ergonomics: 44.6
    discoverability: 62.5
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Daypilot Org Domain Security
  slug: daypilot-org-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Daypilot Org Vulnerability Disclosure
  slug: daypilot-org-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 1
skills:
- name: daypilot-org-validate-and-generate-builder-archive
  slug: daypilot-org-validate-and-generate-builder-archive
slug: daypilot-org
tags:
- Calendar
- Scheduler
- Gantt Chart
- UI Components
- Open Source
website: https://daypilot.org/
---
