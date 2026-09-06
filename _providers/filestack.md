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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://www.filestack.com
  baseurl_source: declared
  description: Filestack File Uploader & File Upload API
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
random_paper: 5
score:
  band: emerging
  composite: 20.9
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 20.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
