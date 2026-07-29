---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 6
  human_in_the_loop: 0
  name: Linksquares Agentic Access
  operation_count: 18
  slug: linksquares-agentic-access
  summary_line: 18 operations · 6 acting
api_count: 6
apis:
- description: User and group lifecycle management is offered through SCIM 2.0 provisioning on the Enterprise tier rather than a public REST endpoint. There is no documented public REST user-management API, base pat
  name: LinkSquares User and Group Provisioning (SCIM)
  slug: linksquares-scim-provisioning-api
- description: Identity and status of the API user (confirmed).
  name: LinkSquares Account API
  slug: linksquares-account-api
- description: Analyze agreements and document import/upload (confirmed).
  name: LinkSquares Agreements API
  slug: linksquares-agreements-api
- description: Additional attachments on Analyze agreements (confirmed).
  name: LinkSquares Attachments API
  slug: linksquares-attachments-api
- description: Finalize templates, tasks, and agreement creation (MODELED paths).
  name: LinkSquares Finalize API
  slug: linksquares-finalize-api
- description: Terms, Smart Values, hierarchy, and agreement types (confirmed).
  name: LinkSquares Metadata and Smart Values API
  slug: linksquares-metadata-and-smart-values-api
artifact_total: 13
collections:
- collection_type: open
  name: LinkSquares API
  slug: open-linksquares
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/linksquares-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/linksquares-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://linksquares.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.linksquares.com/hc/en-us/sections/26436087990551-LinkSquares-APIs-Overview
- group: start
  title: ''
  type: SignUp
  url: https://help.linksquares.com/hc/en-us/articles/10575849523735-Managing-API-Keys
- group: commercial
  title: ''
  type: Plans
  url: plans/linksquares-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/linksquares-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/linksquares-finops.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linksquares-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/linksquares
- group: company
  title: ''
  type: Blog
  url: https://blog.linksquares.com
created: '2026-07-12'
description: LinkSquares is an AI-powered contract lifecycle management (CLM) platform that helps legal teams draft, review, execute, and analyze agreements. Its public REST API is split across two products - Analyze, which surfaces processed agreements plus the metadata, Smart Values, terms, types, tags, and parent/child hierarchy extracted from them, and lets you import DOCX/PDF documents for AI processing; and Finalize, which lets external systems retrieve templates, create draft/intake/request agreements, and retrieve and approve tasks so stakeholders can collaborate on contracts without leaving their own tools. A single API token is shared across Analyze and Finalize and is passed as an x-api-key header. API access is gated to LinkSquares customers, and keys are self-managed by Administrator users; user and group provisioning is offered through SCIM 2.0 on the Enterprise tier rather than a public REST endpoint.
finops:
- name: Linksquares Finops
  service_category: Contract Lifecycle Management
  slug: linksquares-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/linksquares.png
layout: provider
modified: '2026-07-12'
name: LinkSquares
nav: Providers
network: true
overview: 'LinkSquares publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Account API, Agreements API, Attachments API, and 2 more. Tagged areas include Contract Management, Contract Lifecycle Management, CLM, Contracts, and AI.


  LinkSquares'' developer surface includes authentication, documentation, signup flow, engineering blog, and 7 more developer resources.'
plans:
- name: Linksquares Plans Pricing
  plan_count: 1
  slug: linksquares-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 2
  name: Linksquares Rate Limits
  slug: linksquares-rate-limits
score:
  band: thin
  composite: 38.0
  delta: -2.1
  facets:
    commercial_clarity: 42.1
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linksquares/refs/heads/main/screenshots/linksquares-2026-07-25T225259.png
security:
- kind: authentication
  name: Linksquares Authentication
  slug: linksquares-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Linksquares Domain Security
  slug: linksquares-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: linksquares
tags:
- Contract Management
- Contract Lifecycle Management
- CLM
- Contracts
- AI
- Legal
- Agreements
- Document Management
- Contract Analytics
website: https://linksquares.com
---
