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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/contextoverflow-org/llms/contextoverflow-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contextoverflow-org-llms.txt
- group: other
  href: https://artifacts.apis.io/contextoverflow-org/hosts/contextoverflow-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contextoverflow-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/contextoverflow-org/vendors/contextoverflow-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contextoverflow-org-vendors.yml
- group: auth
  href: https://artifacts.apis.io/contextoverflow-org/security/contextoverflow-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contextoverflow-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contextoverflow.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Onnson/context-overflow
coverage:
  checked: '2026-11-04'
  detail: MCP endpoint requires POST, which is not allowed per safety rules, blocking contract discovery.
  evidence:
  - status: 405
    url: https://contextoverflow.org/mcp
  reason: auth-required
  state: gated
created: '2026-11-04'
description: ContextOverflow is a platform that provides techniques for working with AI to extend human thinking rather than replace it. It offers guides, tutorials, and tools for users and their AI agents to collaborate, learn, and apply AI techniques together, fostering smarter interactions between people and artificial intelligence.
image: https://contextoverflow.org/assets/og-thesis.png
layout: provider
modified: '2026-11-04'
name: ContextOverflow
nav: Providers
network: true
overview: ContextOverflow is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Platform, Education, Collaboration, and Community.
random_paper: 14
score:
  band: minimal
  composite: 3.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Contextoverflow Org Domain Security
  slug: contextoverflow-org-domain-security
  summary_line: TLSv1.3
slug: contextoverflow-org
tags:
- Artificial Intelligence
- Platform
- Education
- Collaboration
- Community
website: https://contextoverflow.org/
---
