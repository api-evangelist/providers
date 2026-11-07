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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/approval-studio/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: https://approval.studio/security/
- group: agent
  href: https://artifacts.apis.io/approval-studio/llms/approval-studio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/approval-studio-llms.txt
- group: other
  href: https://artifacts.apis.io/approval-studio/hosts/approval-studio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/approval-studio-hosts.yml
- group: other
  href: https://artifacts.apis.io/approval-studio/vendors/approval-studio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/approval-studio-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.approval.studio/account/login
- group: auth
  href: https://artifacts.apis.io/approval-studio/security/approval-studio-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/approval-studio-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/approval-studio/security/approval-studio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/approval-studio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://approval.studio/
coverage:
  checked: '2026-11-01'
  detail: The public website is HTML with no machine‑readable API spec and all attempts to fetch OpenAPI files returned redirects or 404s.
  evidence:
  - status: 301
    url: https://approval.studio/openapi.json
  - status: 301
    url: https://approval.studio/api/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: Approval Studio provides modern artwork and design approval software that streamlines the sign‑off process for creative teams. Users can markup designs, compare versions, and proof online with clients, while AI‑driven reporting automates feedback collection. The platform supports fast collaboration, version control, and secure client portals, helping brands accelerate time‑to‑market for marketing assets.
image: https://approval.studio/wp-content/uploads/2025/09/Gallery-Images-Approval-Studio.jpg
layout: provider
modified: '2026-11-01'
name: Approval Studio
nav: Providers
network: true
overview: Approval Studio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artwork, Design, Approval, Collaboration, and Artificial Intelligence.
random_paper: 18
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.4
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 11.1
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Approval Studio Domain Security
  slug: approval-studio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Approval Studio Trust Center
  slug: approval-studio-trust-center
  summary_line: ISO 27001, PCI DSS
slug: approval-studio
tags:
- Artwork
- Design
- Approval
- Collaboration
- Artificial Intelligence
website: https://approval.studio/
---
