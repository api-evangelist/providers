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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 19.8
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'Coral by Vox Media is an open-source commenting platform. Each self-hosted or managed Coral instance exposes a GraphQL API at /api/graphql covering stories, comments, users, sites, moderation queues, '
  name: Coral GraphQL API
  slug: coral-graphql-api
artifact_total: 5
asyncapis:
- description: ''
  name: Vox Media Coral Webhooks
  slug: vox-media-coral-webhooks
common:
- group: auth
  title: ''
  type: Security
  url: https://www.voxmedia.com/security/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vox-media-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vox-media-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.voxmedia.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coralproject.net/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.coralproject.net/api/schema
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.coralproject.net/
- group: operate
  title: ''
  type: Support
  url: https://docs.coralproject.net/contact
- group: company
  title: ''
  type: Blog
  url: https://coralproject.net/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/voxmedia
- group: commercial
  title: ''
  type: Pricing
  url: https://coralproject.net/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.voxmedia.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.voxmedia.com/terms-of-use/
- group: build
  title: ''
  type: Packages
  url: packages/vox-media-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/vox-media-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vox-media-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/vox-media-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vox-media-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vox-media-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/vox-media-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vox-media-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/vox-media-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vox-media-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/vox-media-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/vox-media-coral-webhooks.yml
created: '2026-07-17'
description: Vox Media is a modern media company whose networks include The Verge, Vox, New York Magazine, SB Nation, Eater, Polygon, The Cut, and Vulture. Its developer-facing surface centers on Coral (Coral by Vox Media), the open-source commenting and community-moderation platform used by more than 500 newsrooms in 28 countries, which exposes a GraphQL API, HMAC-signed webhooks, an embeddable comment stream, and the coral-cli developer tool.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vox-media.png
layout: provider
modified: '2026-07-21'
name: Vox Media
nav: Providers
network: true
overview: 'Vox Media publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Media, Publishing, and News.


  The Vox Media catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Vox Media''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, CLI, and 18 more developer resources.'
random_paper: 3
score:
  band: developing
  composite: 44.1
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 53.1
    developer_ergonomics: 61.9
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 36.8
  previous_composite: 44.1
  provenance:
    conformance: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vox-media/refs/heads/main/screenshots/vox-media-2026-08-17T082822.png
security:
- kind: authentication
  name: Vox Media Authentication
  slug: vox-media-authentication
  summary_line: http-bearer/jwt-sso · 2 schemes
- kind: domain-security
  name: Vox Media Domain Security
  slug: vox-media-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vox Media Vulnerability Disclosure
  slug: vox-media-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: vox-media
tags:
- Company
- Consumer
- Media
- Publishing
- News
- Comments
- Community
- Moderation
- GraphQL
website: https://www.voxmedia.com
---
