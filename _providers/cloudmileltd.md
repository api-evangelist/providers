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
- group: other
  href: https://artifacts.apis.io/cloudmileltd/hosts/cloudmileltd-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudmileltd-hosts.yml
- group: other
  href: https://artifacts.apis.io/cloudmileltd/vendors/cloudmileltd-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudmileltd-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://cloudmile.ai/en/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloudmile.ai/en/privacy
- group: auth
  href: https://artifacts.apis.io/cloudmileltd/security/cloudmileltd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudmileltd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloudmile.ai
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://cloudmile.ai
  - status: 403
    url: https://equityzen.com/company/cloudmileltd
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: CloudMile (Cloudmile Ltd.) is a leading AI solutions provider based in Asia, offering services such as MileAI, MileData, MileInfra, MileOps, MileSec, and LumiTure.ai FinOps platform. The company focuses on enterprise AI, cloud infrastructure, and technical training, serving clients across multiple regions with a strong emphasis on innovation and partnership.
layout: provider
modified: '2026-10-09'
name: Cloudmileltd
nav: Providers
network: true
overview: Cloudmileltd is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Cloud, Enterprise, Services, and Asia.
random_paper: 10
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.0
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 5.3
  previous_composite: 7.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cloudmileltd/cloudmileltd-2026-11-03T124535.png
security:
- kind: domain-security
  name: Cloudmileltd Domain Security
  slug: cloudmileltd-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cloudmileltd
tags:
- Artificial Intelligence
- Cloud
- Enterprise
- Services
- Asia
website: https://cloudmile.ai
---
