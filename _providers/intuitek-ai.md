---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: flavored
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 1.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/intuitek-ai/llms/intuitek-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/intuitek-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/intuitek-ai/a2a/intuitek-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/intuitek-ai-a2a.yml
- group: other
  href: https://artifacts.apis.io/intuitek-ai/hosts/intuitek-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/intuitek-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/intuitek-ai/vendors/intuitek-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/intuitek-ai-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/KyleMillion
- group: auth
  href: https://artifacts.apis.io/intuitek-ai/security/intuitek-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/intuitek-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://intuitek.ai/
coverage:
  checked: '2026-10-30'
  detail: IntuiTek is a research organization that does not offer a software API.
  evidence:
  - status: 200
    url: https://intuitek.ai/
  reason: not-a-software-company
  state: none
created: '2026-10-30'
description: IntuiTek¹ is an original artificial intelligence research and systems investigation organization founded by William Kyle Million in Poplar Bluff, Missouri. The company publishes evidence‑driven AI research, explores operational system reliability, and develops applied intelligence tools. Its public work includes research papers, open‑source code, and engineering documentation, while commercial offerings are separate. IntuiTek aims to advance AI reliability and decision‑support systems through rigorous investigation and transparent publishing.
image: https://intuitek.ai/og-image.jpg
layout: provider
modified: '2026-10-30'
name: intuitek-ai
nav: Providers
network: true
overview: intuitek-ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Research, Systems, and Missouri.
plans:
- name: Intuitek Ai Plans Pricing
  plan_count: 0
  slug: intuitek-ai-plans-pricing
random_paper: 20
scopes:
- name: Intuitek Ai Scopes
  scope_count: 0
  slug: intuitek-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 5.4
  coverage:
    artifact_dirs: 20
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
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Intuitek Ai Authentication
  slug: intuitek-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Intuitek Ai Domain Security
  slug: intuitek-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: intuitek-ai
tags:
- Company
- AI
- Research
- Systems
- Missouri
website: https://intuitek.ai/
---
