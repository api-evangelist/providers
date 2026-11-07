---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Chat Master lead qualification platform, documented at the guides page.
  name: Chat Master API
  slug: chat-master-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/chat-master-pro/llms/chat-master-pro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chat-master-pro-llms.txt
- group: agent
  href: https://artifacts.apis.io/chat-master-pro/well-known/chat-master-pro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chat-master-pro-well-known.yml
- group: other
  href: https://artifacts.apis.io/chat-master-pro/hosts/chat-master-pro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chat-master-pro-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chat-master.pro/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chat-master.pro/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://chat-master.pro/login
- group: docs
  title: ''
  type: Documentation
  url: https://chat-master.pro/guides/click-to-whatsapp-ads-lead-management
- group: auth
  href: https://artifacts.apis.io/chat-master-pro/security/chat-master-pro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chat-master-pro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chat-master.pro/
coverage:
  checked: '2026-11-03'
  detail: Provider documentation is public HTML without any OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://chat-master.pro/guides/click-to-whatsapp-ads-lead-management
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Chat Master provides AI‑powered lead qualification for WhatsApp and other messaging channels. It classifies each lead by purchase intent before a sales team responds, increasing closures and reducing response time. The platform automates lead scoring, enabling teams to focus on high‑intent prospects and improve conversion rates.
image: https://chat-master.pro/img/chat-master-og.jpg
layout: provider
modified: '2026-11-03'
name: Chat Master
nav: Providers
network: true
overview: 'Chat Master is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Chat Master''s developer surface includes documentation and 8 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
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
  name: Chat Master Pro Domain Security
  slug: chat-master-pro-domain-security
  summary_line: TLSv1.3
slug: chat-master-pro
tags:
- Company
website: https://chat-master.pro/
---
