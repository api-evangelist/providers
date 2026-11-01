---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.2
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/viridis-security-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/viridis-security-com/hosts/viridis-security-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/viridis-security-com-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://viridis-security.com/security
- group: auth
  href: https://artifacts.apis.io/viridis-security-com/security/viridis-security-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/viridis-security-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://viridis-security.com/
- group: docs
  title: ''
  type: Documentation
  url: https://viridis-security.com/about
- group: operate
  title: ''
  type: Support
  url: https://viridis-security.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://viridis-security.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://viridis-security.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://viridis-security.com/services
coverage:
  checked: '2026-10-30'
  detail: The provider's website contains no developer program or API documentation.
  evidence:
  - status: 200
    url: https://viridis-security.com/
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Viridis Security provides security assessments for AI agents and MCP (Machine Control Protocol) systems. Their services include agent resilience assessments, authority and architecture reviews, AI control‑boundary reviews, and vulnerability evidence reviews. They offer a proof‑of‑work middleware product called Maxwell’s Defense and publish research on AI agent security. The company helps customers understand risks, choose controls, and obtain inspectable evidence with clear limits.
image: https://viridis-security.com/og.png
layout: provider
modified: '2026-10-29'
name: viridis-security-com
nav: Providers
network: true
overview: 'viridis-security-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Security, Assessment, Cybersecurity, and MCP.


  viridis-security-com''s developer surface includes documentation, support, getting-started guide, and 7 more developer resources.'
random_paper: 19
scopes:
- name: Viridis Security Com Scopes
  scope_count: 0
  slug: viridis-security-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    conformance: unknown
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Viridis Security Com Authentication
  slug: viridis-security-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Viridis Security Com Domain Security
  slug: viridis-security-com-domain-security
  summary_line: TLSv1.3
slug: viridis-security-com
tags:
- Company
- AI Security
- Assessment
- Cybersecurity
- MCP
website: https://viridis-security.com/
---
