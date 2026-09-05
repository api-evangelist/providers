---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - '{''url'': ''https://www.sessionstack.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.playbookux.com/ — a different registrable domain (sessionstack.com -> playbookux.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The SessionStack REST API provides programmatic access to session recordings, user events, errors, and logs. Developers can retrieve and search sessions associated with their websites, get details abo
  name: SessionStack REST API
  slug: sessionstack-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sessionstack-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sessionstack.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sessionstack.com/docs/overview
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/sessionstack
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sessionstack
- group: company
  title: ''
  type: Blog
  url: https://medium.com/sessionstack-blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sessionstack.com/pricing
- group: other
  title: ''
  type: X
  url: https://x.com/sessionstack
- group: commercial
  title: ''
  type: Plans
  url: plans/sessionstack-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sessionstack-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sessionstack-finops.yml
created: '2026-06-13'
description: SessionStack is an AI-driven session replay and digital experience analytics platform that enables product and support teams to record, replay, and analyze real user sessions on web applications. It provides a REST API for retrieving session recordings, events, errors, and user-generated logs, enabling teams to integrate session playback into support workflows, export data to external systems, and automate session management. SessionStack integrates with tools such as Zendesk and Sentry to surface session replays directly alongside support tickets and error reports. The platform uses tagless autocapture and retroactive data history to ensure no user interaction is missed, and supports co-browsing for live collaborative troubleshooting sessions.
finops:
- name: Sessionstack Finops
  service_category: ''
  slug: sessionstack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sessionstack.png
jsonld:
- class_count: 11
  name: Sessionstack Context
  property_count: 0
  slug: sessionstack-context
layout: provider
modified: '2026-06-13'
name: SessionStack
nav: Providers
network: true
overview: 'SessionStack publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Session Replay, User Monitoring, Digital Experience Analytics, Session Recording, and Co-Browsing.


  The SessionStack catalog on APIs.io includes 1 JSON-LD context.


  SessionStack''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Sessionstack Plans Pricing
  plan_count: 4
  slug: sessionstack-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 4
  name: Sessionstack Rate Limits
  slug: sessionstack-rate-limits
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 72.0
    catalog_earned_first_party: 0.0
    catalog_gap: 43.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 37.3
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 31.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Sessionstack Domain Security
  slug: sessionstack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sessionstack
tags:
- Session Replay
- User Monitoring
- Digital Experience Analytics
- Session Recording
- Co-Browsing
- Error Tracking
- Support Workflows
- User Behavior Analytics
website: https://www.sessionstack.com
---
