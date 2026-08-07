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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Filestack File Uploader & File Upload API
  name: Filestack
  slug: filestack
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/filestack-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.filestack.com
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Filestack File Uploader & File Upload API
graphqls:
- description: This conceptual GraphQL schema represents the Filestack file upload, transformation, storage, and CDN delivery API. Filestack provides file uploading, content detection, transformations (image, video,
  name: Filestack GraphQL Schema
  slug: filestack-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/filestack.png
layout: provider
modified: '2026-05-30'
name: Filestack
nav: Providers
network: true
overview: 'Filestack publishes 1 API on the [APIs.io](https://apis.io/) network: Filestack. Tagged areas include Cloud Storage And File Sharing and Public APIs.'
random_paper: 46
score:
  band: emerging
  composite: 20.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 60.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 20.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/filestack/refs/heads/main/screenshots/filestack-2026-06-20T181205.png
security:
- kind: domain-security
  name: Filestack Domain Security
  slug: filestack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: filestack
tags:
- Cloud Storage And File Sharing
- Public APIs
website: https://www.filestack.com
---
