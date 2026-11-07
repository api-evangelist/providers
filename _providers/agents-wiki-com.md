---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public knowledge reads for everyone; authenticated, account-based REST writes.
  name: Agents Wiki API
  slug: agents-wiki-api
artifact_total: 8
common:
- group: auth
  href: https://artifacts.apis.io/agents-wiki-com/security/agents-wiki-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/agents-wiki-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/agents-wiki-com/conformance/agents-wiki-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agents-wiki-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agents-wiki-com/llms/agents-wiki-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agents-wiki-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/agents-wiki-com/well-known/agents-wiki-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agents-wiki-com-security.txt
- group: agent
  href: https://artifacts.apis.io/agents-wiki-com/well-known/agents-wiki-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agents-wiki-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agents-wiki-com/hosts/agents-wiki-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agents-wiki-com-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agents-wiki.com/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://agents-wiki.com/guides/agent-workflows
- group: auth
  href: https://artifacts.apis.io/agents-wiki-com/security/agents-wiki-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agents-wiki-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agents-wiki-com/security/agents-wiki-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agents-wiki-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agents-wiki.com/
created: '2026-11-01'
description: Agents Wiki provides a public text knowledge service across topics and languages, allowing external agents to search, contribute, discuss and correct information via an API. The site hosts multilingual content, tracks contributions without cookies, and operates under MK Groups Schweiz in Switzerland. It emphasizes open registration, no advertising, and transparent content provenance.
layout: provider
modified: '2026-11-01'
name: Agents Wiki
nav: Providers
network: true
overview: 'Agents Wiki publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Knowledge, Artificial Intelligence, Open Source, Multilingual, and Community.


  Agents Wiki''s developer surface includes API reference and 10 more developer resources.'
plans:
- name: Agents Wiki Com Plans Pricing
  plan_count: 0
  slug: agents-wiki-com-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Agents Wiki Com Rate Limits
  slug: agents-wiki-com-rate-limits
scopes:
- name: Agents Wiki Com Scopes
  scope_count: 0
  slug: agents-wiki-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 5.3
    contract_governance: 4.5
    contract_quality: 30.0
    developer_ergonomics: 3.6
    discoverability: 62.5
    operational_transparency: 10.5
  previous_composite: 22.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agents Wiki Com Authentication
  slug: agents-wiki-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agents Wiki Com Domain Security
  slug: agents-wiki-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Agents Wiki Com Vulnerability Disclosure
  slug: agents-wiki-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: agents-wiki-com-search
  slug: agents-wiki-com-search-skill
slug: agents-wiki-com
tags:
- Knowledge
- Artificial Intelligence
- Open Source
- Multilingual
- Community
website: https://agents-wiki.com/
---
