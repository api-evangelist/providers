---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Moxtra's REST API for building embedded collaboration experiences, covering users, binders (workspaces), pages, messages, files, meetings, todos, signatures, and webhooks. Authentication uses OAuth 2.
  name: Moxtra REST API
  slug: rest-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/moxtra-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moxtra-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Moxtra
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/moxtra
- group: company
  title: ''
  type: Website
  url: https://www.moxo.com
- group: company
  title: ''
  type: Legacy Website
  url: https://www.moxtra.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.moxtra.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.moxo.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://developer.moxtra.com/
- group: company
  title: ''
  type: Blog
  url: https://www.moxo.com/blog
created: '2026-05-11'
description: Moxtra (now operating as Moxo) is a contextual collaboration and customer engagement platform that lets businesses embed chat, video meetings, voice calls, file sharing, e-signature, digital workflows, and binder-based collaboration into their own mobile and web applications via SDKs and REST APIs. The Moxtra Developer Portal exposes 200+ REST API endpoints for managing users, binders (workspaces), messages, files, meetings, todos, and notifications. Authentication uses OAuth 2.0 access tokens issued against the Moxtra (or self-branded GroupHour) authorization server.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/moxtra.png
layout: provider
modified: '2026-05-11'
name: Moxtra
nav: Providers
network: true
overview: 'Moxtra publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Collaboration, Customer Engagement, Messaging, Video Conferencing, and Workflows.


  Moxtra''s developer surface includes documentation, pricing, signup flow, engineering blog, and 6 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 3
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 17.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moxtra/refs/heads/main/screenshots/moxtra-2026-06-20T185836.png
security:
- kind: domain-security
  name: Moxtra Domain Security
  slug: moxtra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Moxtra Trust Center
  slug: moxtra-trust-center
  summary_line: SOC 2, GDPR
slug: moxtra
tags:
- Collaboration
- Customer Engagement
- Messaging
- Video Conferencing
- Workflows
- Embedded SDK
- Communications
website: https://www.moxo.com
---
