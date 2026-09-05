---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Memco enables AI agents to share knowledge across a platform while maintaining security and privacy controls, providing collective memory capabilities for AI-powered applications.
  name: Memco API
  slug: memco-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/memco-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.memco.ai/
- group: company
  title: ''
  type: Blog
  url: https://memco.ai/rss.xml
created: '2026-01-02'
description: Memco transforms platforms into hubs of shared knowledge by enabling AI agents to learn from each other while maintaining security and privacy. It provides a platform for collective AI memory management.
finops:
- name: Memco Finops
  service_category: API
  slug: memco-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/memco.png
layout: provider
modified: '2026-04-28'
name: Memco
nav: Providers
network: true
overview: 'Memco publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agents, Artificial Intelligence, Knowledge-Management, and Memory.


  Memco''s developer surface includes engineering blog and 2 more developer resources.'
plans:
- name: Memco Plans Pricing
  plan_count: 3
  slug: memco-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Memco Rate Limits
  slug: memco-rate-limits
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 9.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/memco/refs/heads/main/screenshots/memco-2026-06-20T185134.png
security:
- kind: domain-security
  name: Memco Domain Security
  slug: memco-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: memco
tags:
- Agents
- Artificial Intelligence
- Knowledge-Management
- Memory
website: https://www.memco.ai/
---
