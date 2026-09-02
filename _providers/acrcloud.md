---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
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
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Acrcloud Agentic Access
  operation_count: 21
  slug: acrcloud-agentic-access
  summary_line: 21 operations · 13 acting
api_count: 1
apis:
- description: Upload and manage audio files and fingerprints within a bucket.
  name: ACRCloud Audio Files API
  slug: acrcloud-audio-files-api
- description: Manage broadcast-database monitoring projects and result callbacks.
  name: ACRCloud Broadcast Monitoring API
  slug: acrcloud-broadcast-monitoring-api
- description: Manage custom recognition buckets.
  name: ACRCloud Buckets API
  slug: acrcloud-buckets-api
- description: Manage file-scanning containers that detect content from buckets.
  name: ACRCloud File Scanning API
  slug: acrcloud-file-scanning-api
- description: Recognize music, custom audio, and humming from a sample or fingerprint.
  name: ACRCloud Identification API
  slug: acrcloud-identification-api
- description: Look up enriched third-party music metadata.
  name: ACRCloud Metadata API
  slug: acrcloud-metadata-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ACRCloud Audio Files API
  slug: open-acrcloud-audio-files-api
- collection_type: open
  name: ACRCloud Audio Files Broadcast Monitoring API
  slug: open-acrcloud-broadcast-monitoring-api
- collection_type: open
  name: ACRCloud Audio Files Buckets API
  slug: open-acrcloud-buckets-api
- collection_type: open
  name: ACRCloud Audio Files File Scanning API
  slug: open-acrcloud-file-scanning-api
- collection_type: open
  name: ACRCloud Audio Files Identification API
  slug: open-acrcloud-identification-api
- collection_type: open
  name: ACRCloud Audio Files Metadata API
  slug: open-acrcloud-metadata-api
- collection_type: open
  name: ACRCloud API
  slug: open-acrcloud
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/acrcloud-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acrcloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/acrcloud-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/acrcloud
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acrcloud
- group: company
  title: ''
  type: Website
  url: https://www.acrcloud.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.acrcloud.com
- group: commercial
  title: ''
  type: Plans
  url: plans/acrcloud-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acrcloud-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/acrcloud-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://acrcloud.com/blog
created: '2026-06-21'
description: ACRCloud provides automatic content recognition (ACR) APIs for music and audio. The HMAC-signed Identification API recognizes music, custom audio, live channels, and humming from short audio samples or fingerprints, while the bearer-token Console and Metadata APIs manage buckets, file-scanning containers, broadcast-monitoring projects, and rich third-party music metadata.
finops:
- name: Acrcloud Finops
  service_category: AI and Machine Learning
  slug: acrcloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/acrcloud.png
layout: provider
modified: '2026-06-21'
name: ACRCloud
nav: Providers
network: true
overview: 'ACRCloud publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Audio Files API, Broadcast Monitoring API, Buckets API, and 3 more. Tagged areas include Audio, Music Recognition, Audio Fingerprinting, Broadcast Monitoring, and Metadata.


  ACRCloud''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Acrcloud Plans Pricing
  plan_count: 5
  slug: acrcloud-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Acrcloud Rate Limits
  slug: acrcloud-rate-limits
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 51.7
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acrcloud/refs/heads/main/screenshots/acrcloud-2026-07-25T181514.png
security:
- kind: authentication
  name: Acrcloud Authentication
  slug: acrcloud-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Acrcloud Domain Security
  slug: acrcloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: acrcloud
tags:
- Audio
- Music Recognition
- Audio Fingerprinting
- Broadcast Monitoring
- Metadata
website: https://www.acrcloud.com
---
