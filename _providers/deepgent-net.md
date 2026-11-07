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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documentation hosted on the portal deepgent.net, but no machine‑readable spec was found.
  name: Deepgent Portal API
  slug: deepgent-portal-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/deepgent-net/llms/deepgent-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deepgent-net-llms.txt
- group: agent
  href: https://artifacts.apis.io/deepgent-net/well-known/deepgent-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deepgent-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/deepgent-net/hosts/deepgent-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deepgent-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/deepgent-net/vendors/deepgent-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deepgent-net-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pablo-albaladejo
- group: auth
  href: https://artifacts.apis.io/deepgent-net/security/deepgent-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deepgent-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deepgent.net/
coverage:
  checked: '2026-11-05'
  detail: Portal pages are a JavaScript‑rendered single‑page app with no machine‑readable spec discovered.
  evidence:
  - status: 200
    url: https://portal.deepgent.net/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: 'deepgent-net is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://deepgent.net/og-image.png
layout: provider
modified: '2026-11-05'
name: deepgent-net
nav: Providers
network: true
overview: deepgent-net is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Chatbots, E-Commerce, and Multi-Tenant.
random_paper: 16
score:
  band: minimal
  composite: 2.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deepgent Net Domain Security
  slug: deepgent-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: deepgent-net
tags:
- Chatbots
- E-Commerce
- Multi-Tenant
website: https://deepgent.net/
---
