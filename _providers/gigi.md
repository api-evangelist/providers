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
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/gigi/llms/gigi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gigi-llms.txt
- group: other
  href: https://artifacts.apis.io/gigi/hosts/gigi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gigi-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gigi.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gigi.co/privacy
- group: auth
  href: https://artifacts.apis.io/gigi/security/gigi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gigi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gigi.co/
coverage:
  checked: '2026-10-29'
  detail: The provider's site https://gigi.co/ returns HTML but no machine‑readable API specification was found.
  evidence:
  - status: 200
    url: https://gigi.co/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Gigi is an AI‑driven networking platform that connects people through intelligent agents. It enables agents to search, introduce, and communicate with contacts, providing tools for automated outreach, warm introductions, and data‑driven networking. The service offers a free tier for individuals and paid plans for teams, focusing on trust, privacy, and seamless integration with existing workflows.
image: https://gigi.co/assets/gigiog.jpg
layout: provider
modified: '2026-10-29'
name: Gigi
nav: Providers
network: true
overview: Gigi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Networking, Agents, and Privacy.
random_paper: 8
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  previous_composite: 9.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Gigi Domain Security
  slug: gigi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: gigi
tags:
- Company
- Artificial Intelligence
- Networking
- Agents
- Privacy
website: https://gigi.co/
---
