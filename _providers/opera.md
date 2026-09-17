---
access_model:
  confidence: high
  label: Contact sales for API credentials
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - plans
  trial: false
  try_now: false
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.9
  scored_at: '2026-09-16'
api_count: 4
apis:
- baseURL: https://ofp.adx.opera.com/openapi/inventory/v1
  baseurl_source: declared
  description: Publisher app and placement (inventory) management.
  name: Opera Inventory API
  slug: opera-inventory-api
- baseURL: https://cb.adx.opera.com
  baseurl_source: declared
  description: Server-to-server conversion event reporting.
  name: Opera Marketing API
  slug: opera-marketing-api
- baseURL: https://ofa.adx.opera.com/oapi/v1
  baseurl_source: declared
  description: Advertiser reporting on campaign performance.
  name: Opera Report API
  slug: opera-report-api
- baseURL: https://ofp.adx.opera.com/openapi/inventory/v1
  baseurl_source: declared
  description: DSP-side exchange performance reporting.
  name: Opera DSP Report API
  slug: opera-dspreport-api
- baseURL: https://ofp.adx.opera.com/openapi/inventory/v1
  baseurl_source: declared
  description: Publisher revenue and delivery reporting.
  name: Opera Publisher Report API
  slug: opera-publisherreport-api
- baseURL: https://ofp.adx.opera.com/openapi/inventory/v1
  baseurl_source: declared
  description: TUS resumable upload session lifecycle.
  name: Opera Upload API
  slug: opera-upload-api
- baseURL: https://ofp.adx.opera.com/openapi/inventory/v1
  baseurl_source: declared
  description: Listing and inspecting uploads.
  name: Opera File Management API
  slug: opera-file-management-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Opera Ads Open Inventory API
  slug: open-opera-inventory-api
- collection_type: open
  name: Opera Ads Open Inventory Marketing API
  slug: open-opera-marketing-api
- collection_type: open
  name: Opera Ads Open Inventory Report API
  slug: open-opera-report-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/overlays/opera-ads-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/opera-ads-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/authentication/opera-authentication.yml
  title: ''
  type: Authentication
  url: authentication/opera-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/security/opera-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opera-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/security/opera-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/opera-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://security.opera.com/policy/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/packages/opera-packages.yml
  title: ''
  type: Packages
  url: packages/opera-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/packages/opera-packages.yml
  title: ''
  type: SDKs
  url: packages/opera-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/mcp/opera-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/opera-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/mcp/opera-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/opera-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/llms/opera-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/opera-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/well-known/opera-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/opera-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/well-known/opera-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/opera-security.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/conformance/opera-conformance.yml
  title: ''
  type: Conformance
  url: conformance/opera-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/errors/opera-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/opera-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/errors/opera-sdk-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/opera-sdk-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/lifecycle/opera-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/opera-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/conventions/opera-conventions.yml
  title: ''
  type: Conventions
  url: conventions/opera-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/data-model/opera-data-model.yml
  title: ''
  type: DataModel
  url: data-model/opera-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/rate-limits/opera-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/opera-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/plans/opera-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/opera-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/changelog/opera-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/opera-changelog.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/sandbox/opera-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/opera-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/components/opera-components.yml
  title: ''
  type: Components
  url: components/opera-components.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://doc.adx.opera.com/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.adx.opera.com/
- group: docs
  title: ''
  type: APIReference
  url: https://doc.adx.opera.com/advertiser/report-api
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.adx.opera.com/publisher/onboarding/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/operaads
- group: company
  title: ''
  type: Blog
  url: https://blogs.opera.com/ads/
- group: operate
  title: ''
  type: Support
  url: https://help.opera.com/en/
- group: start
  title: ''
  type: SignUp
  url: https://admanager.opera.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.opera.com/ads
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.opera.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.opera.com/privacy
- group: company
  title: ''
  type: Website
  url: https://opera.com/
created: '2026-07-17'
description: 'Opera is the Norway-based, Nasdaq-listed (OPRA) maker of the Opera, Opera GX, Opera Air, Opera Mini and Opera Neon web browsers, and the operator of the Opera Ads advertising and monetization platform. Opera Ads exposes six documented HTTP APIs: an advertiser Report API for daily campaign performance, a publisher Inventory Management API for apps and placements, a publisher OFP Report API for revenue and delivery, an ADX DSP Report API for exchange performance, a server-to-server Marketing API for conversion postbacks, and a TUS 1.0.0 resumable File Upload API. Around them sit Android and iOS ad SDKs with mediation adapters for AdMob, AppLovin MAX, TopOn, TradPlus and LevelPlay, an OpenRTB/ADX exchange with Prebid.js and Prebid Server adapters, a web JS ad tag, first-party Go OpenRTB and VAST libraries, and the self-serve Opera Ad Manager console. Authentication differs per API — bearer token, token query parameter, X-API-Key or HMAC signature — and every credential is issued
  by contacting Opera Ads.'
image: https://github.com/operaads.png
layout: provider
modified: '2026-08-13'
name: Opera
nav: Providers
network: true
overview: 'Opera publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Inventory API, Marketing API, Report API, and 4 more. Tagged areas include Company, Consumer Technology, Advertising, AdTech, and Browser.


  Opera''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, engineering blog, and 29 more developer resources.'
plans:
- name: Opera Plans Pricing
  plan_count: 0
  slug: opera-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Opera Rate Limits
  slug: opera-rate-limits
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 17.6
    developer_ergonomics: 73.2
    discoverability: 81.5
    operational_transparency: 50.0
  previous_composite: 45.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/opera/refs/heads/main/screenshots/opera-2026-08-17T083429.png
security:
- kind: authentication
  name: Opera Authentication
  slug: opera-authentication
  summary_line: http/apiKey/custom-hmac/unauthenticated · 5 schemes
- kind: domain-security
  name: Opera Domain Security
  slug: opera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Opera Vulnerability Disclosure
  slug: opera-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: opera
tags:
- Company
- Consumer Technology
- Advertising
- AdTech
- Browser
- Monetization
- OpenRTB
- Marketing
- Mobile SDK
- Header Bidding
- Publisher Monetization
- Reporting
website: https://opera.com/
---
