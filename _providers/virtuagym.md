---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Virtuagym Agentic Access
  operation_count: 27
  slug: virtuagym-agentic-access
  summary_line: 27 operations · 13 acting
api_count: 7
apis:
- description: Member credits and club invoices.
  name: Virtuagym Billing API
  slug: virtuagym-billing-api
- description: Staff / employees of a club.
  name: Virtuagym Club Employees API
  slug: virtuagym-club-employees-api
- description: Members of a club - list, retrieve, create, update, and activate.
  name: Virtuagym Club Members API
  slug: virtuagym-club-members-api
- description: Assign coaching workout plans to members.
  name: Virtuagym Coaching API
  slug: virtuagym-coaching-api
- description: Club events (classes) and event participants (bookings).
  name: Virtuagym Events API
  slug: virtuagym-events-api
- description: Membership definitions (plans) and membership instances (enrollments).
  name: Virtuagym Memberships API
  slug: virtuagym-memberships-api
- description: Club visits - member check-in / attendance records.
  name: Virtuagym Visits API
  slug: virtuagym-visits-api
artifact_total: 14
collections:
- collection_type: open
  name: Virtuagym Public API (v1)
  slug: open-virtuagym
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/virtuagym-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/virtuagym-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/virtuagym-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/virtuagym
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/virtuagym
- group: company
  title: ''
  type: Website
  url: https://virtuagym.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.virtuagym.com/s/article/API-Link-To-Your-Website
- group: commercial
  title: ''
  type: Plans
  url: plans/virtuagym-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/virtuagym-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/virtuagym-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://business.virtuagym.com/blog/
created: '2026-07-12'
description: Virtuagym is a Netherlands-based fitness and health club management platform that combines member management, membership and billing administration, class and appointment scheduling, access control / check-ins, and digital coaching (workouts, nutrition, and a branded member app) into one SaaS suite for gyms, studios, personal trainers, and corporate wellness programs. Its Public API (v1) is club-scoped and lets partners and businesses read and write members, employees, membership definitions and instances, member credits, invoices, visits (check-ins), events (classes) and participants, and coaching workout assignments. v1 endpoints authenticate with an api_key plus a club_secret passed as query parameters over HTTPS. Authoritative reference documentation is access-gated (request via api@virtuagym.com); the endpoints modeled here are grounded in Virtuagym's publicly mirrored API wiki and live host probes.
finops:
- name: Virtuagym Finops
  service_category: Fitness and Health Club Management Software
  slug: virtuagym-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/virtuagym.png
layout: provider
modified: '2026-07-12'
name: Virtuagym
nav: Providers
network: true
overview: 'Virtuagym publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Billing API, Club Employees API, Club Members API, and 4 more. Tagged areas include Fitness, Health Club Management, Gym Management, Coaching, and Membership Management.


  Virtuagym''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Virtuagym Plans Pricing
  plan_count: 3
  slug: virtuagym-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 2
  name: Virtuagym Rate Limits
  slug: virtuagym-rate-limits
score:
  band: thin
  composite: 38.1
  delta: -2.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Virtuagym Authentication
  slug: virtuagym-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Virtuagym Domain Security
  slug: virtuagym-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: virtuagym
tags:
- Fitness
- Health Club Management
- Gym Management
- Coaching
- Membership Management
- Fitness Software
- Wellness
- Scheduling
- SaaS
website: https://virtuagym.com
---
