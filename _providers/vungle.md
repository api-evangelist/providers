---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  - '{''url'': ''https://vungle.com'', ''status'': 301, ''note'': ''declared website redirects to https://liftoff.ai/ — a different registrable domain (vungle.com -> liftoff.ai), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-04'
api_count: 4
apis:
- description: 'Automated access to Vungle/Liftoff campaign performance reports — impressions, clicks, installs, and in-app events — with configurable groupings, metrics, and cohort (look-back window) analysis. HTTP '
  name: Liftoff Reporting API
  slug: liftoff-reporting-api
- description: Closed-beta API to programmatically launch UA expansion campaigns, manage spend and targeting, upload assets, and assemble creatives. Standard REST/JSON at https://cm-api.liftoff.io/v1.
  name: Liftoff Campaign Management API
  slug: liftoff-campaign-management-api
- description: Audience ingestion/validation API for partners working on behalf of multiple clients, at https://analytics.liftoff.io/audiences/v1.
  name: Liftoff Audiences Integration API
  slug: liftoff-audiences-integration-api
- description: Submit GDPR-compliant opt-out requests to remove user data by device ID, at https://analytics.liftoff.io/opt_out/v3.
  name: Liftoff GDPR Opt-Out API
  slug: liftoff-gdpr-opt-out-api
artifact_total: 8
asyncapis:
- description: ''
  name: Vungle S2S Webhooks
  slug: vungle-s2s-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vungle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vungle.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.liftoff.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.liftoff.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.liftoff.io/advertiser
- group: auth
  title: ''
  type: Authentication
  url: authentication/vungle-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vungle-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vungle-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vungle-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vungle-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/vungle-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/vungle-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vungle-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/vungle-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vungle-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/vungle-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vungle-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/vungle-s2s-webhooks.yml
- group: company
  title: ''
  type: Blog
  url: https://liftoff.io/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://liftoff.io/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://liftoff.io/terms-of-service
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Vungle
created: '2026-07-17'
description: Vungle is a mobile app monetization and user-acquisition platform, now operated as part of Liftoff (the merged Liftoff + Vungle mobile growth company). Vungle's in-app advertising SDKs help mobile publishers monetize with performance-focused ad formats (video, interactive, and playable ads), while Liftoff's advertiser APIs let growth teams launch and manage user-acquisition campaigns, assemble creatives, ingest audiences, and pull automated performance reporting. The programmatic surface is documented at docs.liftoff.io and includes a Reporting API, a closed-beta Campaign Management API, an Audiences Integration API, a GDPR Opt-Out API, and a server-to-server (S2S) postback integration. All advertiser APIs authenticate with an HTTP Basic API key and secret issued by a Liftoff Account Manager.
image: https://liftoff.ai/wp-content/uploads/2025/01/B-Meta-Image-20240912-122239.jpg
layout: provider
modified: '2026-07-21'
name: Vungle
nav: Providers
network: true
overview: 'Vungle publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Mobile, Monetization, and User Acquisition.


  The Vungle catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Vungle''s developer surface includes documentation, getting-started guide, authentication, sandbox, engineering blog, and 17 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 1
  name: Vungle Rate Limits
  slug: vungle-rate-limits
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 59.5
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 31.6
  previous_composite: 39.3
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vungle/refs/heads/main/screenshots/vungle-2026-09-02T170329.png
security:
- kind: authentication
  name: Vungle Authentication
  slug: vungle-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vungle Domain Security
  slug: vungle-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vungle
tags:
- Company
- Advertising
- Mobile
- Monetization
- User Acquisition
- AdTech
- Analytics
- Reporting
website: https://vungle.com
---
