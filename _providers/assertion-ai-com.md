---
access_model:
  confidence: low
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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/assertion-ai-com/hosts/assertion-ai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/assertion-ai-com-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://assertion-ai.com/security
- group: auth
  href: https://artifacts.apis.io/assertion-ai-com/security/assertion-ai-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/assertion-ai-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/assertion-ai-com/security/assertion-ai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/assertion-ai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://assertion-ai.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://assertion-ai.com/install
- group: operate
  title: ''
  type: Support
  url: mailto:support@assertion-ai.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Assertion-AI/assertion
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://assertion-ai.com/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://assertion-ai.com/terms.html
coverage:
  checked: '2026-11-02'
  detail: No public developer program or API documentation was found on the company's website.
  evidence:
  - status: 200
    url: https://assertion-ai.com/
  reason: no-developer-program
  state: none
created: '2026-11-01'
description: Assertion AI provides a shared memory platform for AI coding agents such as Claude Code, Cursor, and Codex, enabling every session to build on prior team decisions, experiments, and insights. The service offers a free starter tier and an optional agent with no compaction and half the price, aiming to boost productivity and reduce duplicated effort across development teams.
image: https://www.assertion-ai.com/assets/og-agent.png
layout: provider
modified: '2026-11-01'
name: Assertion AI
nav: Providers
network: true
overview: 'Assertion AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Memory, Collaboration, LLM, and Productivity.


  Assertion AI''s developer surface includes getting-started guide, support, and 8 more developer resources.'
random_paper: 11
scopes:
- name: Assertion Ai Com Scopes
  scope_count: 0
  slug: assertion-ai-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 48.2
    operational_transparency: 7.9
  previous_composite: 16.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Assertion Ai Com Authentication
  slug: assertion-ai-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Assertion Ai Com Domain Security
  slug: assertion-ai-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Assertion Ai Com Vulnerability Disclosure
  slug: assertion-ai-com-vulnerability-disclosure
  summary_line: no policy recorded
slug: assertion-ai-com
tags:
- Artificial Intelligence
- Memory
- Collaboration
- LLM
- Productivity
website: https://assertion-ai.com/
---
