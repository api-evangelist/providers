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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-17'
api_count: 4
apis:
- description: The @hcengineering/api-client Node.js package provides typed programmatic access to the Huly Platform. It exposes a WebSocket client (connect) holding a persistent transactor connection and a REST cli
  name: Huly Platform SDK
  slug: huly-platform-sdk
- description: Managed, hosted Huly offered as Huly Cloud with usage-tiered workspaces (Common, Rare, Epic, Legendary, and custom Enterprise plans). Cloud workspaces run the same platform and are reachable programma
  name: Huly Cloud
  slug: huly-cloud
- description: Tracker is Huly's project and issue management module (subtasks, milestones, templates, custom workflows) with optional two-way GitHub Issues/Projects sync. Issues, projects, and related objects are a
  name: Huly Tracker
  slug: huly-tracker
- description: Documents is Huly's collaborative knowledge-management module for rich-text documents with code blocks and real-time editing. Document content is modeled as platform markup and accessed through the Hu
  name: Huly Documents
  slug: huly-documents
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Huly Platform API
  slug: open-huly
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/huly-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hcengineering
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hardcoreeng
- group: company
  title: ''
  type: Website
  url: https://huly.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.huly.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/huly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/huly-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/huly-finops.yml
created: '2026-06-21'
description: Huly is an open-source, all-in-one project management and team collaboration platform (an alternative to Linear, Jira, Slack, and Notion) built around modules like Tracker and Documents. Programmatic access is delivered primarily as a Node.js SDK (@hcengineering/api-client) that connects to the platform transactor over WebSocket or REST, rather than a broad public HTTP API. Huly is available as free, self-hostable open source (github.com/hcengineering) and as managed Huly Cloud.
finops:
- name: Huly Finops
  service_category: Project Management and Collaboration
  slug: huly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/huly.png
layout: provider
modified: '2026-06-21'
name: Huly
nav: Providers
network: true
overview: 'Huly publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Platform SDK, Cloud, Tracker, and 1 more. Tagged areas include Project Management, Collaboration, Open Source, Productivity, and SDK.


  Huly''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Huly Plans Pricing
  plan_count: 6
  slug: huly-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 4
  name: Huly Rate Limits
  slug: huly-rate-limits
score:
  band: thin
  composite: 29.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 30.6
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 29.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/huly/refs/heads/main/screenshots/huly-2026-07-25T221637.png
security:
- kind: domain-security
  name: Huly Domain Security
  slug: huly-domain-security
  summary_line: TLSv1.3 · DMARC
slug: huly
tags:
- Project Management
- Collaboration
- Open Source
- Productivity
- SDK
website: https://huly.io/
---
