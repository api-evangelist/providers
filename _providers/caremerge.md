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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/caremerge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.caremerge.com/web/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/caremerge
created: '2026-07-17'
description: CareMerge is a senior living technology company that builds family engagement, care coordination, community engagement, and communications software for senior living and long-term / post-acute care communities. Its platform connects residents, families, and care staff so communities can coordinate care, share activities and calendars, and keep families informed. The company was surfaced as a portfolio company of Insight Partners and added to the API Evangelist network for enrichment. As of this pass CareMerge publishes no public developer API, developer portal, OpenAPI/AsyncAPI specification, or /.well-known discovery surface; its marketing site sits behind a SiteGround (sg-captcha) challenge and its GitHub organization contains internal tooling and open-source forks rather than a first-party client SDK.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/caremerge.png
layout: provider
modified: '2026-07-18'
name: CareMerge
nav: Providers
network: true
overview: CareMerge is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Senior Living, Care Coordination, and Family Engagement.
random_paper: 15
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 3.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/caremerge/refs/heads/main/screenshots/caremerge-2026-07-25T204549.png
security:
- kind: domain-security
  name: Caremerge Domain Security
  slug: caremerge-domain-security
  summary_line: TLSv1.3 · DMARC
slug: caremerge
tags:
- Company
- Healthcare
- Senior Living
- Care Coordination
- Family Engagement
- Long-Term Care
- Community Engagement
- Health Technology
website: http://www.caremerge.com/web/
---
