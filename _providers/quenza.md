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
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Quenza Agentic Access
  operation_count: 12
  slug: quenza-agentic-access
  summary_line: 12 operations · 8 acting
api_count: 1
apis:
- baseURL: https://developers.quenza.com/v1
  baseurl_source: declared
  description: The Clients API from Quenza — 4 operation(s) for clients.
  name: Quenza Clients API
  slug: quenza-clients-api
- baseURL: https://developers.quenza.com/v1
  baseurl_source: declared
  description: The Groups API from Quenza — 2 operation(s) for groups.
  name: Quenza Groups API
  slug: quenza-groups-api
- baseURL: https://developers.quenza.com/v1
  baseurl_source: declared
  description: The Members API from Quenza — 2 operation(s) for members.
  name: Quenza Members API
  slug: quenza-members-api
- baseURL: https://developers.quenza.com/v1
  baseurl_source: declared
  description: The Tasks API from Quenza — 1 operation(s) for tasks.
  name: Quenza Tasks API
  slug: quenza-tasks-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Quenza ArchiveClient API
  slug: open-quenza-archiveclient-api
- collection_type: open
  name: Quenza ArchiveClient AttachGroupMembers API
  slug: open-quenza-attachgroupmembers-api
- collection_type: open
  name: Quenza ArchiveClient Clients API
  slug: open-quenza-clients-api
- collection_type: open
  name: Quenza ArchiveClient CreateClient API
  slug: open-quenza-createclient-api
- collection_type: open
  name: Quenza ArchiveClient CreateGroup API
  slug: open-quenza-creategroup-api
- collection_type: open
  name: Quenza ArchiveClient CreateMember API
  slug: open-quenza-createmember-api
- collection_type: open
  name: Quenza ArchiveClient Groups API
  slug: open-quenza-groups-api
- collection_type: open
  name: Quenza ArchiveClient ListClient API
  slug: open-quenza-listclient-api
- collection_type: open
  name: Quenza ArchiveClient ListMember API
  slug: open-quenza-listmember-api
- collection_type: open
  name: Quenza ArchiveClient ListTask API
  slug: open-quenza-listtask-api
- collection_type: open
  name: Quenza ArchiveClient Members API
  slug: open-quenza-members-api
- collection_type: open
  name: Quenza ArchiveClient ShowClient API
  slug: open-quenza-showclient-api
- collection_type: open
  name: Quenza ArchiveClient Tasks API
  slug: open-quenza-tasks-api
- collection_type: open
  name: Quenza ArchiveClient UnarchiveClient API
  slug: open-quenza-unarchiveclient-api
- collection_type: open
  name: Quenza ArchiveClient UpdateClient API
  slug: open-quenza-updateclient-api
- collection_type: open
  name: Quenza ArchiveClient UpdateMember API
  slug: open-quenza-updatemember-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/quenza-capability-edges.yml
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
overview: 'Quenza publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Clients API, Groups API, Members API, and 1 more. Tagged areas include Coaching, Therapy, Client Engagement, Digital Health, and Mental Health.


  Quenza''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Quenza Plans Pricing
  plan_count: 5
  slug: quenza-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 4
  name: Quenza Rate Limits
  slug: quenza-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/quenza/refs/heads/main/screenshots/quenza-2026-09-02T152638.png
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
