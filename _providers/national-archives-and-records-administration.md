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
    agentic_access: derived
    auth_clarity: false
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
  score: 24.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: National Archives And Records Administration Agentic Access
  operation_count: 64
  slug: national-archives-and-records-administration-agentic-access
  summary_line: 64 operations · 22 acting
api_count: 16
apis:
- description: The Accounts API from National Archives and Records Administration — 4 operation(s) for accounts.
  name: National Archives and Records Administration Accounts API
  slug: national-archives-and-records-administration-accounts-api
- description: For important announcements
  name: National Archives and Records Administration Announcements API
  slug: national-archives-and-records-administration-announcements-api
- description: Comment search and data retrieval
  name: National Archives and Records Administration Comments API
  slug: national-archives-and-records-administration-comments-api
- description: Contribution search and data retrieval; Contributions include Tags, Transcriptions, and Comments - search/retrieve contributions when you want to return any contribution type.
  name: National Archives and Records Administration Contributions API
  slug: national-archives-and-records-administration-contributions-api
- description: The Extracted Text API from National Archives and Records Administration — 1 operation(s) for extracted text.
  name: National Archives and Records Administration Extracted Text API
  slug: national-archives-and-records-administration-extracted-text-api
- description: The Justifications API from National Archives and Records Administration — 1 operation(s) for justifications.
  name: National Archives and Records Administration Justifications API
  slug: national-archives-and-records-administration-justifications-api
- description: The Metadata API from National Archives and Records Administration — 1 operation(s) for metadata.
  name: National Archives and Records Administration Metadata API
  slug: national-archives-and-records-administration-metadata-api
- description: Information about record online availability
  name: National Archives and Records Administration Online Availability API
  slug: national-archives-and-records-administration-online-availability-api
- description: The Other Extracted Text API from National Archives and Records Administration — 1 operation(s) for other extracted text.
  name: National Archives and Records Administration Other Extracted Text API
  slug: national-archives-and-records-administration-other-extracted-text-api
- description: The Partner API from National Archives and Records Administration — 5 operation(s) for partner.
  name: National Archives and Records Administration Partner API
  slug: national-archives-and-records-administration-partner-api
- description: Record description search and data retrieval
  name: National Archives and Records Administration Records API
  slug: national-archives-and-records-administration-records-api
- description: The Statistics API from National Archives and Records Administration — 1 operation(s) for statistics.
  name: National Archives and Records Administration Statistics API
  slug: national-archives-and-records-administration-statistics-api
- description: Tag search and data retrieval
  name: National Archives and Records Administration Tags API
  slug: national-archives-and-records-administration-tags-api
- description: Transcription search and data retrieval
  name: National Archives and Records Administration Transcriptions API
  slug: national-archives-and-records-administration-transcriptions-api
- description: The Users API from National Archives and Records Administration — 3 operation(s) for users.
  name: National Archives and Records Administration Users API
  slug: national-archives-and-records-administration-users-api
- description: The Utilities API from National Archives and Records Administration — 1 operation(s) for utilities.
  name: National Archives and Records Administration Utilities API
  slug: national-archives-and-records-administration-utilities-api
artifact_total: 22
collections:
- collection_type: open
  name: NextGen Catalog API
  slug: open-national-archives-and-records-administration
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/national-archives-and-records-administration-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-archives-and-records-administration-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usnatarchives
- group: company
  title: ''
  type: Website
  url: https://www.archives.gov/
- group: start
  title: ''
  type: Portal
  url: https://www.archives.gov/developer
created: '2024-12-03'
description: The National Archives Catalog API is a read-write web API for the National Archives Catalog. This API can be used to perform fielded search of archival metadata, bulk export of metadata and digital media, and post contributions to records.
finops:
- name: National Archives And Records Administration Finops
  service_category: API
  slug: national-archives-and-records-administration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-archives-and-records-administration.png
layout: provider
modified: '2026-05-19'
name: National Archives and Records Administration
nav: Providers
network: true
overview: 'National Archives and Records Administration publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Announcements API, Comments API, and 13 more. Tagged areas include Archives, Federal Government, Records, and Catalog.


  National Archives and Records Administration''s developer surface includes developer portal and 4 more developer resources.'
plans:
- name: National Archives And Records Administration Plans Pricing
  plan_count: 3
  slug: national-archives-and-records-administration-plans-pricing
random_paper: 88
rate_limits:
- limit_count: 5
  name: National Archives And Records Administration Rate Limits
  slug: national-archives-and-records-administration-rate-limits
score:
  band: thin
  composite: 34.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 52.7
    developer_ergonomics: 8.7
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 34.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-archives-and-records-administration/refs/heads/main/screenshots/national-archives-and-records-administration-2026-06-20T185959.png
security:
- kind: domain-security
  name: National Archives And Records Administration Domain Security
  slug: national-archives-and-records-administration-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: national-archives-and-records-administration
tags:
- Archives
- Federal Government
- Records
- Catalog
website: https://www.archives.gov/
---
