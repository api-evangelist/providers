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
api_count: 1
apis:
- description: API for Convosight platform (no public documentation found)
  name: Convosight API
  slug: convosight-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/convosight/llms/convosight-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/convosight-llms.txt
- group: other
  href: https://artifacts.apis.io/convosight/hosts/convosight-hosts.yml
  title: ''
  type: Hosts
  url: hosts/convosight-hosts.yml
- group: other
  href: https://artifacts.apis.io/convosight/vendors/convosight-vendors.yml
  title: ''
  type: Vendors
  url: vendors/convosight-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.convosight.com/policies/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.convosight.com/policies/privacy
- group: auth
  href: https://artifacts.apis.io/convosight/security/convosight-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/convosight-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.convosight.com
coverage:
  checked: '2026-10-11'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found at the API host.
  evidence:
  - status: 404
    url: https://api.convosight.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: Convosight provides an enterprise video social intelligence platform that analyzes social video and comments across channels to deliver consumer insights for brand, marketing, research, and product development teams. It serves large brands that need multilingual, multi‑channel video analysis to inform decisions.
image: https://www.convosight.com/og-image.png
layout: provider
modified: '2026-10-10'
name: Convosight
nav: Providers
network: true
overview: Convosight is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Social Intelligence, Video Analytics, Consumer Insights, Market Research, and Brand Analytics.
random_paper: 12
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 73.2
    operational_transparency: 0.0
  previous_composite: 11.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/convosight/convosight-2026-11-03T125252.png
security:
- kind: domain-security
  name: Convosight Domain Security
  slug: convosight-domain-security
  summary_line: TLSv1.3 · DMARC
slug: convosight
tags:
- Social Intelligence
- Video Analytics
- Consumer Insights
- Market Research
- Brand Analytics
- Multilingual Intelligence
website: https://www.convosight.com
---
