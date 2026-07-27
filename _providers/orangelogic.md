---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 7
apis:
- description: Authenticate against an Orange Logic instance and obtain tokens for subsequent calls. Supports OAuth 2.0 (client ID and secret), non-expiring bearer tokens, and basic username/password login. The OAut
  name: Orange Logic Authentication API
  slug: orangelogic-authentication-api
- description: Find assets across the DAM with query criteria, field selection, pagination, sorting, and AI-powered semantic search. The confirmed endpoint is GET or POST /API/search/v4.0/search, accepting query, fi
  name: Orange Logic Search API
  slug: orangelogic-search-api
- description: Upload, import, retrieve, and manage digital assets and their representations - single-file uploads, batch uploads, cloud-storage imports, and large-file (>1.5GB) handling, plus content delivery via p
  name: Orange Logic Assets and Media API
  slug: orangelogic-assets-media-api
- description: Work directly with database objects - assets (images, video, audio), folders, groups, users, tags, keywords, and relationships - through generic CREATE, READ, UPDATE, and DELETE calls. Paths follow th
  name: Orange Logic DataTable API
  slug: orangelogic-datatable-api
- description: List and modify asset metadata - retrieve all metadata fields, update tags and linked fields, and manage language-specific field values. Includes batch edit and batch upsert operations. Endpoint ident
  name: Orange Logic Metadata API
  slug: orangelogic-metadata-api
- description: 'Manage user and contact accounts, group assignments, permissions, and organizational hierarchies. Handled through the DataTable object model (Users, Groups, Contacts). Exact endpoint identifiers vary '
  name: Orange Logic Users and Contacts API
  slug: orangelogic-users-contacts-api
- description: 'Subscribe to asset lifecycle events and send webhooks to a third-party service when assets are created, edited, or deleted. This is a server-to-endpoint HTTP callback surface, not a persistent socket '
  name: Orange Logic Webhooks API
  slug: orangelogic-webhooks-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/orangelogic-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orangelogic-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/orange-logic
- group: company
  title: ''
  type: Website
  url: https://www.orangelogic.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.orangelogic.com
- group: commercial
  title: ''
  type: Plans
  url: plans/orangelogic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/orangelogic-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/orangelogic-finops.yml
created: '2026-07-05'
description: Orange Logic builds OrangeDAM (formerly branded Cortex), an enterprise digital asset management (DAM) and media asset management (MAM) platform used by museums, media companies, financial institutions, healthcare, and government archives. OrangeDAM exposes a documented REST API for assets, metadata, search, users, folders, and webhooks. The API is per-instance and customer-gated - every call is made against your own organization's Orange Logic instance host rather than a single shared public gateway, so the base URL is written here as the placeholder https://{OrangeLogicURL}/webapi. Endpoints come in two families - the newer /webapi/ endpoints (each ending in a unique identifier and version, e.g. token_48I_v1) and the legacy /api/ endpoints (with a version number in the path); Orange Logic recommends the /webapi/ family. Responses are JSON or XML. Pricing is enterprise contact-sales only.
finops:
- name: Orangelogic Finops
  service_category: Digital Asset Management
  slug: orangelogic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/orangelogic.png
layout: provider
modified: '2026-07-05'
name: Orange Logic
nav: Providers
network: true
overview: 'Orange Logic publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Digital Asset Management, DAM, Media Asset Management, MAM, and Enterprise.


  Orange Logic''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Orangelogic Plans Pricing
  plan_count: 1
  slug: orangelogic-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Orangelogic Rate Limits
  slug: orangelogic-rate-limits
score:
  band: emerging
  composite: 23.2
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 23.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: domain-security
  name: Orangelogic Domain Security
  slug: orangelogic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Orangelogic Trust Center
  slug: orangelogic-trust-center
  summary_line: HIPAA, GDPR
slug: orangelogic
tags:
- Digital Asset Management
- DAM
- Media Asset Management
- MAM
- Enterprise
- Metadata
- Archive
website: https://www.orangelogic.com
---
