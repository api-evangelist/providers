---
access_model:
  confidence: high
  label: Paid (free trial) · Open access
  onboarding: open
  pricing: paid
  public: true
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Quenza Agentic Access
  operation_count: 12
  slug: quenza-agentic-access
  summary_line: 12 operations · 8 acting
api_count: 16
apis:
- description: The ArchiveClient API from Quenza — 1 operation(s) for archiveclient.
  name: Quenza ArchiveClient API
  slug: quenza-archiveclient-api
- description: The AttachGroupMembers API from Quenza — 1 operation(s) for attachgroupmembers.
  name: Quenza AttachGroupMembers API
  slug: quenza-attachgroupmembers-api
- description: The Clients API from Quenza — 4 operation(s) for clients.
  name: Quenza Clients API
  slug: quenza-clients-api
- description: The CreateClient API from Quenza — 1 operation(s) for createclient.
  name: Quenza CreateClient API
  slug: quenza-createclient-api
- description: The CreateGroup API from Quenza — 1 operation(s) for creategroup.
  name: Quenza CreateGroup API
  slug: quenza-creategroup-api
- description: The CreateMember API from Quenza — 1 operation(s) for createmember.
  name: Quenza CreateMember API
  slug: quenza-createmember-api
- description: The Groups API from Quenza — 2 operation(s) for groups.
  name: Quenza Groups API
  slug: quenza-groups-api
- description: The ListClient API from Quenza — 1 operation(s) for listclient.
  name: Quenza ListClient API
  slug: quenza-listclient-api
- description: The ListMember API from Quenza — 1 operation(s) for listmember.
  name: Quenza ListMember API
  slug: quenza-listmember-api
- description: The ListTask API from Quenza — 1 operation(s) for listtask.
  name: Quenza ListTask API
  slug: quenza-listtask-api
- description: The Members API from Quenza — 2 operation(s) for members.
  name: Quenza Members API
  slug: quenza-members-api
- description: The ShowClient API from Quenza — 1 operation(s) for showclient.
  name: Quenza ShowClient API
  slug: quenza-showclient-api
- description: The Tasks API from Quenza — 1 operation(s) for tasks.
  name: Quenza Tasks API
  slug: quenza-tasks-api
- description: The UnarchiveClient API from Quenza — 1 operation(s) for unarchiveclient.
  name: Quenza UnarchiveClient API
  slug: quenza-unarchiveclient-api
- description: The UpdateClient API from Quenza — 1 operation(s) for updateclient.
  name: Quenza UpdateClient API
  slug: quenza-updateclient-api
- description: The UpdateMember API from Quenza — 1 operation(s) for updatemember.
  name: Quenza UpdateMember API
  slug: quenza-updatemember-api
artifact_total: 22
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/quenza-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quenza-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/quenza-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://quenza.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quenza
- group: docs
  title: ''
  type: Documentation
  url: https://developers.quenza.com/docs/v1
- group: operate
  title: ''
  type: SupportKnowledgeBase
  url: https://help.quenza.com
- group: commercial
  title: ''
  type: Plans
  url: plans/quenza-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/quenza-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/quenza-finops.yml
created: '2026-07-10'
description: Quenza is a digital care and client-engagement platform for coaches, therapists, and other helping professionals. Practitioners build activities - worksheets, exercises, psycho-education, intake forms, reflection prompts, and surveys - bundle them into timed pathways (care programs), and share them with clients through a branded client portal and mobile apps, then track responses, results, notes, tasks, and chat. Quenza exposes a documented public REST API (v1) for programmatically managing clients, team members, groups, and tasks, authenticated with a workspace Bearer token. API access is available on the Collective and Beyond plans; webhooks are available from the Growth plan up.
finops:
- name: Quenza Finops
  service_category: Practice Management and Client Engagement
  slug: quenza-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quenza.png
layout: provider
modified: '2026-07-10'
name: Quenza
nav: Providers
network: true
overview: 'Quenza publishes 16 APIs on the [APIs.io](https://apis.io/) network, including ArchiveClient API, AttachGroupMembers API, Clients API, and 13 more. Tagged areas include Coaching, Therapy, Client Engagement, Digital Health, and Mental Health.


  Quenza''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Quenza Plans Pricing
  plan_count: 5
  slug: quenza-plans-pricing
random_paper: 80
rate_limits:
- limit_count: 4
  name: Quenza Rate Limits
  slug: quenza-rate-limits
score:
  band: thin
  composite: 34.8
  delta: -4.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.0
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 38.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Quenza Authentication
  slug: quenza-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Quenza Domain Security
  slug: quenza-domain-security
  summary_line: TLSv1.3 · DMARC
slug: quenza
tags:
- Coaching
- Therapy
- Client Engagement
- Digital Health
- Mental Health
- Practice Management
- Positive Psychology
website: https://quenza.com
---
