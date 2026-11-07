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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: unknown
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Developer API reference as listed on the provider site
  name: Chorilo API
  slug: chorilo-api
- baseURL: https://backend.chorilo.com
  baseurl_source: declared
  description: 'Chorilo API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Chorilo API
  slug: chorilo-com-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/chorilo-com/rules/chorilo-com-rules.yml
  title: ''
  type: Spectral
  url: rules/chorilo-com-rules.yml
- group: design
  href: https://artifacts.apis.io/chorilo-com/vocabulary/chorilo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chorilo-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/chorilo-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/chorilo-com/conventions/chorilo-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/chorilo-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/chorilo-com/conformance/chorilo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chorilo-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chorilo-com/llms/chorilo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chorilo-com-llms.txt
- group: other
  href: https://artifacts.apis.io/chorilo-com/a2a/chorilo-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/chorilo-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/chorilo-com/well-known/chorilo-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chorilo-com-security.txt
- group: auth
  href: https://artifacts.apis.io/chorilo-com/well-known/chorilo-com-chorilo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chorilo-com-chorilo-security.txt
- group: agent
  href: https://artifacts.apis.io/chorilo-com/well-known/chorilo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chorilo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/chorilo-com/hosts/chorilo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chorilo-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chorilo.com/terms
- group: operate
  title: ''
  type: Support
  url: https://support.chorilo.com/login
- group: operate
  title: ''
  type: StatusPage
  url: https://www.chorilo.com/status
- group: auth
  title: ''
  type: Security
  url: https://www.chorilo.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chorilo.com/privacy
- group: start
  title: ''
  type: Login
  url: https://www.chorilo.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.chorilo.com/docs/Chorilo_AVV.pdf
- group: company
  title: ''
  type: Blog
  url: https://www.chorilo.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.chorilo.com/agent.txt
- group: auth
  href: https://artifacts.apis.io/chorilo-com/security/chorilo-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/chorilo-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/chorilo-com/security/chorilo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chorilo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chorilo.com/
coverage:
  checked: '2026-11-03'
  detail: API documentation page returns HTML without a discoverable OpenAPI or other machine-readable contract.
  evidence:
  - status: 200
    url: https://www.chorilo.com/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Chorilo provides a modern choir management platform based in Germany, offering tools for managing scores, schedules, and finances. The SaaS solution supports ensembles of all sizes, complies with GDPR, and includes features like digital sheet music, event planning, and member communication. It aims to simplify choir administration for conductors and administrators.
image: https://www.chorilo.com/logo.png
layout: provider
modified: '2026-11-03'
name: Chorilo
nav: Providers
network: true
overview: 'Chorilo is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Choir Management, Sheet Music, Event Planning, Finance, and Membership.


  The Chorilo catalog on APIs.io includes 1 Spectral governance ruleset.


  Chorilo''s developer surface includes support, documentation, engineering blog, getting-started guide, and 19 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: Chorilo API Rules
  rule_count: 35
  severity_counts:
    error: 32
    hint: 0
    info: 2
    warn: 1
  slug: chorilo-com-rules
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 35.6
    contract_quality: 11.7
    developer_ergonomics: 20.7
    discoverability: 57.1
    operational_transparency: 13.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chorilo Com Domain Security
  slug: chorilo-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Chorilo Com Vulnerability Disclosure
  slug: chorilo-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: get-embed-events
  slug: get-embed-events
- name: get-event
  slug: get-event
- name: Get public ensemble website
  slug: get-public-ensemble
- name: list-public-associations
  slug: list-public-associations
- name: list-public-events
  slug: list-public-events
slug: chorilo-com
tags:
- Choir Management
- Sheet Music
- Event Planning
- Finance
- Membership
- Collaboration
- GDPR
- Mobile App
website: https://chorilo.com/
---
