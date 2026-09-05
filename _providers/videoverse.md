---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL_template: '{PARTNER_BASE_URL}'
  baseurl_source: spec_template
  description: 'Partner REST API for Magnifi by VideoVerse. Partners authenticate with an Access Key and Access Secret pair (x-access-key / x-access-secret headers) and use the API to ingest live or recorded streams '
  name: Magnifi Partner Integration API
  slug: magnifi-partner-integration-api
artifact_total: 8
asyncapis:
- description: ''
  name: Videoverse Magnifi Webhooks
  slug: videoverse-magnifi-webhooks
collections:
- collection_type: postman
  name: Magnifi x Partner Integration Documentation
  slug: postman-videoverse-magnifi-partner-integration
common:
- group: company
  title: ''
  type: Website
  url: https://vverse.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.prod.videoverse.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.prod.videoverse.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.prod.videoverse.dev/
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/34141959/2sA3s6EpXt
- group: operate
  title: ''
  type: Support
  url: https://magnifi.ai/raise-a-ticket
- group: company
  title: ''
  type: Blog
  url: https://magnifi.ai/insights/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/magnifi-codeverse
- group: commercial
  title: ''
  type: TermsOfService
  url: https://magnifi.ai/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://magnifi.ai/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: security/videoverse-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/videoverse-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/videoverse-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/videoverse-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/videoverse-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/videoverse-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/videoverse-authentication.yml
created: '2026-09-04'
description: VideoVerse is an AI video technology company founded in 2016 with offices in the United States, Europe and India, whose flagship SaaS platform Magnifi automatically detects key moments in live and archival footage and turns them into broadcast-ready highlights, vertical cuts, multilingual captions and enriched metadata for sports broadcasters, OTT platforms, leagues, teams, rights holders, news and entertainment. Magnifi publishes a partner REST API covering stream ingestion, clip / highlight / highlight-clip retrieval, match-video export, roster (tournament, team, player) and match-schedule management, entity membership, and HMAC-signed webhook event delivery. The company also ships an Adobe Premiere Pro extension and product lines including Digital Highlight Pro, Logo Detection, Content Moderation Pro, Auto Flip, Web Stories and Reely. VideoVerse was acquired by Minute Media in August 2025.
image: https://wp-dashboard.magnifi.ai/wp-content/uploads/2024/08/image.png
layout: provider
modified: '2026-09-04'
name: VideoVerse
nav: Providers
network: true
overview: 'VideoVerse publishes 1 API on the [APIs.io](https://apis.io/) network: Magnifi Partner Integration API. Tagged areas include Video, Artificial Intelligence, Sports, Media, and Broadcasting.


  The VideoVerse catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  VideoVerse''s developer surface includes documentation, API reference, support, engineering blog, authentication, and 12 more developer resources.'
plans:
- name: Videoverse Plans Pricing
  plan_count: 0
  slug: videoverse-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Videoverse Rate Limits
  slug: videoverse-rate-limits
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 63.7
    developer_ergonomics: 51.8
    discoverability: 59.3
    governance: 4.5
    operational_transparency: 13.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: authentication
  name: Videoverse Authentication
  slug: videoverse-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Videoverse Domain Security
  slug: videoverse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Videoverse Trust Center
  slug: videoverse-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 27701, ISO 9001
slug: videoverse
tags:
- Video
- Artificial Intelligence
- Sports
- Media
- Broadcasting
- Video Editing
- Highlights
- Content Creation
- Machine Learning
- Webhooks
website: https://vverse.ai/
---
