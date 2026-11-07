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
    agent_skills: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/ce-net-com/llms/ce-net-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ce-net-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/ce-net-com/well-known/ce-net-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ce-net-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ce-net-com/hosts/ce-net-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ce-net-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ce-net-com/vendors/ce-net-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ce-net-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ce-net.com/terms/
- group: auth
  title: ''
  type: Security
  url: https://ce-net.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apps.ce-net.com/privacy
- group: auth
  href: https://artifacts.apis.io/ce-net-com/security/ce-net-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ce-net-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ce-net.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://ce-net.com/
  reason: no-developer-program
  state: none
created: '2026-11-04'
description: CE-Net is the public cell network offering a single MCP address that provides typed cells, capabilities, and shared compute. It enables any person or agent to access tools, results, and compute across a decentralized network. The platform includes Huebot, Trana, and compute services, with a focus on openness and community-driven development. Users can request beta access, explore the MCP endpoint at /mcp, and engage with the network via various tools and APIs.
image: https://design.ce-net.com/v1/logo/ce-net-og.png
layout: provider
modified: '2026-11-04'
name: CE-Net
nav: Providers
network: true
overview: CE-Net is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Networks, MCP, Compute, and Open Source.
random_paper: 0
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ce Net Com Domain Security
  slug: ce-net-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ce-net-com
tags:
- Company
- Networks
- MCP
- Compute
- Open Source
website: https://ce-net.com/
---
