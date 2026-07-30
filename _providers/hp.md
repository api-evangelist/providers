---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
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
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Hp Agentic Access
  operation_count: 6
  slug: hp-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 3
apis:
- description: Device analytics operations
  name: HP Analytics API
  slug: hp-analytics-api
- description: Print device management operations
  name: HP Devices API
  slug: hp-devices-api
- description: Incident management operations
  name: HP Incidents API
  slug: hp-incidents-api
artifact_total: 11
collections:
- collection_type: open
  name: HP PrintOS Device API
  slug: open-hp-printos-device-api
- collection_type: open
  name: HP Workforce Solutions Analytics API
  slug: open-hp-workforce-solutions-analytics-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hp-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hp-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hp-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HPInc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hp
- group: company
  title: ''
  type: Website
  url: https://www.hp.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.hp.com/
created: '2026-03-21'
description: HP Inc. is a global technology company that provides personal computing devices, printers, 3D printing solutions, hyperscale computing solutions, and related supplies, services, and software.
finops:
- name: Hp Finops
  service_category: Device Management & Industrial Printing
  slug: hp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hp.png
layout: provider
modified: '2026-05-19'
name: HP
nav: Providers
network: true
overview: 'HP publishes 3 APIs on the [APIs.io](https://apis.io/) network: Analytics API, Devices API, and Incidents API. Tagged areas include Computer Hardware, Device Management, Printing, Technology, and Fortune 100.'
plans:
- name: Hp Plans Pricing
  plan_count: 3
  slug: hp-plans-pricing
press:
- date: '2026-05-25'
  title: HP Raises the Bar for AI in the Workplace
  url: https://quocirca.com/content/hp-raises-the-bar-for-ai-in-the-workplace/
- date: '2026-05-25'
  title: 'Unlocking AI: Machine Learning as a Service'
  url: https://www.hp.com/us-en/workstations/learning-hub/ai-for-all.html
- date: '2026-05-25'
  title: 'HP Imagine 2026: HP Demonstrates Its Vision for a ...'
  url: https://www.hp.com/us-en/newsroom/press-releases/2026/hp-introduces-hp-iq-connected-ecosystem.html
- date: '2026-05-25'
  title: 'HP Imagine 2026: HP Enables People''s Best Work in More ...'
  url: https://www.hp.com/us-en/newsroom/press-releases/2026/hp-enables-best-work-in-more-places.html
- date: '2026-05-25'
  title: HP acquires Humane Platform and team for $116M
  url: https://www.facebook.com/groups/AIUGM/posts/4020109041603394/
random_paper: 52
rate_limits:
- limit_count: 2
  name: Hp Rate Limits
  slug: hp-rate-limits
score:
  band: thin
  composite: 33.0
  delta: -1.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.7
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 34.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hp/refs/heads/main/screenshots/hp-2026-06-20T182854.png
security:
- kind: domain-security
  name: Hp Domain Security
  slug: hp-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Hp Vulnerability Disclosure
  slug: hp-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: hp
tags:
- Computer Hardware
- Device Management
- Printing
- Technology
- Fortune 100
website: https://www.hp.com/
---
