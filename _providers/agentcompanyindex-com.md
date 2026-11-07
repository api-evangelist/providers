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
  href: https://artifacts.apis.io/agentcompanyindex-com/llms/agentcompanyindex-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentcompanyindex-com-llms.txt
- group: other
  href: https://artifacts.apis.io/agentcompanyindex-com/hosts/agentcompanyindex-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentcompanyindex-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentcompanyindex-com/vendors/agentcompanyindex-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentcompanyindex-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentcompanyindex.com/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://agentcompanyindex.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentcompanyindex.com/legal/privacy
- group: auth
  href: https://artifacts.apis.io/agentcompanyindex-com/security/agentcompanyindex-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentcompanyindex-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentcompanyindex.com/
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found on documented API reference.
  evidence:
  - status: 0
    url: https://api.agentcompanyindex.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Agent Company Index (ACI) is a directory of companies, services and providers designed for AI agents. It provides structured, evidence‑backed profiles that both humans and AI assistants can read. The platform is operated by Viacheslav Spitsyn in Leipzig, Germany, and also runs related businesses such as SL‑SP, LocalLLMGear, WebPrüfer, and Alles Geräumt. ACI aims to help AI understand offerings, fit, and gaps across a wide range of industries, supporting use‑cases from software agencies to local services.
layout: provider
modified: '2026-10-31'
name: Agent Company Index
nav: Providers
network: true
overview: 'Agent Company Index is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Directory, Artificial Intelligence, Companies, Services, and Marketplace.


  Agent Company Index''s developer surface includes support and 7 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 9.3
  provenance:
    conformance: unknown
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
  name: Agentcompanyindex Com Domain Security
  slug: agentcompanyindex-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agentcompanyindex-com
tags:
- Directory
- Artificial Intelligence
- Companies
- Services
- Marketplace
website: https://agentcompanyindex.com/
---
