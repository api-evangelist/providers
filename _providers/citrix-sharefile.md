---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Citrix Sharefile Agentic Access
  operation_count: 24
  slug: citrix-sharefile-agentic-access
  summary_line: 24 operations · 11 acting
api_count: 7
apis:
- description: REST API for ShareFile providing access to items, folders, files, users, groups, shares, devices, accounts, and workflows. Authentication uses OAuth 2.0 with multiple supported grant types including a
  name: ShareFile REST API v3
  slug: rest-api-v3
- description: The Accounts API from Citrix ShareFile — 1 operation(s) for accounts.
  name: Citrix ShareFile Accounts API
  slug: citrix-sharefile-accounts-api
- description: The Groups API from Citrix ShareFile — 2 operation(s) for groups.
  name: Citrix ShareFile Groups API
  slug: citrix-sharefile-groups-api
- description: The Items API from Citrix ShareFile — 5 operation(s) for items.
  name: Citrix ShareFile Items API
  slug: citrix-sharefile-items-api
- description: The Sessions API from Citrix ShareFile — 1 operation(s) for sessions.
  name: Citrix ShareFile Sessions API
  slug: citrix-sharefile-sessions-api
- description: The Shares API from Citrix ShareFile — 2 operation(s) for shares.
  name: Citrix ShareFile Shares API
  slug: citrix-sharefile-shares-api
- description: The Users API from Citrix ShareFile — 2 operation(s) for users.
  name: Citrix ShareFile Users API
  slug: citrix-sharefile-users-api
artifact_total: 12
collections:
- collection_type: open
  name: Citrix ShareFile REST API v3
  slug: open-citrix-sharefile
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/citrix-sharefile-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/citrix-sharefile-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/citrix-sharefile-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/citrix-sharefile-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/citrix-sharefile
- group: company
  title: ''
  type: Website
  url: https://www.sharefile.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.sharefile.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sharefile.com/plans
- group: start
  title: ''
  type: Signup
  url: https://www.sharefile.com/plans
- group: operate
  title: ''
  type: Community
  url: https://community.sharefilesupport.com/
- group: other
  title: ''
  type: Parent Company
  url: https://www.progress.com
- group: agent
  title: ''
  type: LlmsText
  url: https://api.sharefile.com/llms.txt
created: '2026-05-11'
description: ShareFile (now part of Progress Software) is a secure document workflow and file sharing platform that lets teams share files, collect e-signatures, request data from clients, and automate document-centric workflows. The ShareFile v3 REST API provides programmatic access to items, folders, files, users, groups, shares, capabilities, and workflows in a customer subdomain, secured with OAuth 2.0.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/citrix-sharefile.png
layout: provider
modified: '2026-05-11'
name: Citrix ShareFile
nav: Providers
network: true
overview: 'Citrix ShareFile publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Groups API, Items API, and 3 more. Tagged areas include File Sharing, Document Workflow, Secure File Transfer, E-Signature, and Client Portal.


  Citrix ShareFile''s developer surface includes authentication, documentation, pricing, signup flow, and 8 more developer resources.'
random_paper: 31
score:
  band: thin
  composite: 29.2
  delta: -2.1
  facets:
    commercial_clarity: 18.4
    contract_quality: 53.4
    developer_ergonomics: 23.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 31.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/citrix-sharefile/refs/heads/main/screenshots/citrix-sharefile-2026-06-20T174414.png
security:
- kind: authentication
  name: Citrix Sharefile Authentication
  slug: citrix-sharefile-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Citrix Sharefile Domain Security
  slug: citrix-sharefile-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Citrix Sharefile Trust Center
  slug: citrix-sharefile-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR, CSA STAR
slug: citrix-sharefile
tags:
- File Sharing
- Document Workflow
- Secure File Transfer
- E-Signature
- Client Portal
- Content Collaboration
website: https://www.sharefile.com
---
