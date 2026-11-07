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
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Bidmachine Io Agentic Access
  operation_count: 8
  slug: bidmachine-io-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 4
apis:
- description: 'OpenRTB 2.5 bid endpoint for in-house bidders and supply partners integrating through the BidMachine SDK: one impression per bid request, first-price auction, USD only, regional endpoints in the EU, U'
  name: BidMachine OpenRTB Auction API
  slug: bidmachine-openrtb-auction-api
- baseURL: https://api-eu.bidmachine.io/api/v1
  baseurl_source: declared
  description: The Authentication API from BidMachine — 1 operation(s) for authentication.
  name: BidMachine Authentication API
  slug: bidmachine-io-authentication-api
- baseURL: https://api-eu.bidmachine.io/api/v1
  baseurl_source: declared
  description: The Placements API from BidMachine — 2 operation(s) for placements.
  name: BidMachine Placements API
  slug: bidmachine-io-placements-api
- baseURL: https://api-eu.bidmachine.io/api/v1
  baseurl_source: declared
  description: The Reporting API from BidMachine — 3 operation(s) for reporting.
  name: BidMachine Reporting API
  slug: bidmachine-io-reporting-api
artifact_total: 15
common:
- group: other
  href: https://artifacts.apis.io/bidmachine-io/overlays/bidmachine-io-placement-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bidmachine-io-placement-management-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/bidmachine-io/skills/bidmachine-io-manage-placements.md
  title: ''
  type: AgentSkill
  url: skills/bidmachine-io-manage-placements.md
- group: other
  href: https://artifacts.apis.io/bidmachine-io/overlays/bidmachine-io-reporting-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bidmachine-io-reporting-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/bidmachine-io/skills/bidmachine-io-pull-reports.md
  title: ''
  type: AgentSkill
  url: skills/bidmachine-io-pull-reports.md
- group: agent
  href: https://artifacts.apis.io/bidmachine-io/agentic-access/bidmachine-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bidmachine-io-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/bidmachine-io/security/bidmachine-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bidmachine-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bidmachine.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.bidmachine.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.bidmachine.io/
- group: docs
  title: ''
  type: Documentation
  url: https://mediation-docs.bidmachine.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bidmachine.io/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.bidmachine.io/api/bidmachine-placement-management-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.bidmachine.io/sdk/overview
- group: company
  title: ''
  type: Blog
  url: https://www.bidmachine.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bidmachine
- group: start
  title: ''
  type: SignUp
  url: https://www.bidmachine.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://dashboard.bidmachine.io/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bidmachine.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bidmachine.com/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://www.bidmachine.com/about-bidmachine
- group: operate
  title: ''
  type: StatusPage
  url: https://bidmachine.statuspage.io/
- group: auth
  title: ''
  type: Security
  url: https://www.bidmachine.com/responsible-vulnerability-disclosure-policy
- group: auth
  href: https://artifacts.apis.io/bidmachine-io/security/bidmachine-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bidmachine-io-vulnerability-disclosure.yml
- group: operate
  href: https://artifacts.apis.io/bidmachine-io/changelog/bidmachine-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bidmachine-io-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.bidmachine.io/sdk/general/android/android-changelog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bidmachine
- group: agent
  href: https://artifacts.apis.io/bidmachine-io/llms/bidmachine-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bidmachine-io-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://developers.bidmachine.io/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.bidmachine.io/llms.txt
- group: build
  href: https://artifacts.apis.io/bidmachine-io/packages/bidmachine-io-packages.yml
  title: ''
  type: Packages
  url: packages/bidmachine-io-packages.yml
- group: build
  href: https://artifacts.apis.io/bidmachine-io/packages/bidmachine-io-packages.yml
  title: ''
  type: SDKs
  url: packages/bidmachine-io-packages.yml
- group: agent
  href: https://artifacts.apis.io/bidmachine-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: https://github.com/bidmachine/bidmachine-sdk-agents
- group: agent
  href: https://artifacts.apis.io/bidmachine-io/mcp/bidmachine-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bidmachine-io-mcp.yml
- group: design
  href: https://artifacts.apis.io/bidmachine-io/conformance/bidmachine-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bidmachine-io-conformance.yml
- group: design
  href: https://artifacts.apis.io/bidmachine-io/errors/bidmachine-io-sdk-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/bidmachine-io-sdk-error-codes.yml
- group: design
  href: https://artifacts.apis.io/bidmachine-io/lifecycle/bidmachine-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bidmachine-io-lifecycle.yml
- group: start
  href: https://artifacts.apis.io/bidmachine-io/sandbox/bidmachine-io-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/bidmachine-io-sandbox.yml
- group: design
  href: https://artifacts.apis.io/bidmachine-io/conventions/bidmachine-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bidmachine-io-conventions.yml
- group: commercial
  href: https://artifacts.apis.io/bidmachine-io/plans/bidmachine-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bidmachine-io-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/bidmachine-io/rate-limits/bidmachine-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bidmachine-io-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/bidmachine-io/data-model/bidmachine-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bidmachine-io-data-model.yml
- group: agent
  href: https://artifacts.apis.io/bidmachine-io/well-known/bidmachine-io-well-known.yml
  title: ''
  type: WellKnownProbe
  url: well-known/bidmachine-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/bidmachine-io/regulatory/bidmachine-io-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/bidmachine-io-regulatory-posture.yml
- group: operate
  title: ''
  type: IncidentNotification
  url: https://www.bidmachine.com/dpa
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://www.bidmachine.com/privacy-policy
- group: other
  title: ''
  type: DataResidency
  url: https://developers.bidmachine.io/dsp/requirements
- group: commercial
  title: ''
  type: DataProcessingAgreement
  url: https://www.bidmachine.com/dpa
created: '2026-09-19'
description: BidMachine is a mobile in-app ad exchange and monetization platform (BidMachine, Inc., McLean, Virginia; spun out of the Appodeal/Stack group) that sells publishers' mobile inventory to demand partners through real-time OpenRTB 2.5 auctions. Publishers integrate the BidMachine SDK (Android, iOS, Unity) or the newer unified BidMachine Plus mediation SDK, or plug BidMachine into AppLovin MAX, Unity LevelPlay, AdMob/GAM or TopOn as a bidding adapter; DSPs and agencies buy through the exchange. Its public APIs are a Placement Management API (create, list, update and delete placements on an ad source with a short-lived bearer token) and a Reporting API (SSP, bidder and P2P revenue reports as NDJSON or CSV over HTTP Basic), both documented as OpenAPI on developers.bidmachine.io, plus the OpenRTB auction endpoints (api-eu / api-us / api-apac) for in-house bidders and supply partners.
image: https://cdn.prod.website-files.com/687616911a76518b8c28e98a/689e12a964ac545560447d4d_BM%20Sign%20256px.svg
layout: provider
mcp_servers:
- description: 'BidMachine publishes no MCP server. Searched: developers.bidmachine.io, docs.bidmachine.io, mediation-docs.bidmachine.io, the github.com/bidmachine organization (38 public repos), the npm registry (no'
  name: bidmachine (candidate)
  slug: bidmachine-candidate
modified: '2026-09-19'
name: BidMachine
nav: Providers
network: true
overview: 'BidMachine publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Placements API, Reporting API, and 1 more. Tagged areas include Advertising, AdTech, Mobile Advertising, Ad Exchange, and Ad Mediation.


  The BidMachine catalog on APIs.io includes 1 Spectral governance ruleset.


  BidMachine''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, changelog, sandbox, and 41 more developer resources.'
plans:
- name: Bidmachine Io Plans Pricing
  plan_count: 0
  slug: bidmachine-io-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Bidmachine Io Rate Limits
  slug: bidmachine-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: BidMachine API Rules
  rule_count: 54
  severity_counts:
    error: 51
    hint: 0
    info: 2
    warn: 1
  slug: bidmachine-io-rules
score:
  band: developing
  composite: 49.2
  coverage:
    artifact_dirs: 27
    catalog_earned: 52.5
    catalog_earned_first_party: 8.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 17.1
    contract_governance: 31.8
    contract_quality: 54.9
    developer_ergonomics: 53.6
    discoverability: 79.5
    operational_transparency: 52.6
  previous_composite: 58.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: coppa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 38.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/bidmachine-io/bidmachine-io-2026-10-11T102112.png
security:
- kind: authentication
  name: Bidmachine Io Authentication
  slug: bidmachine-io-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Bidmachine Io Domain Security
  slug: bidmachine-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bidmachine Io Vulnerability Disclosure
  slug: bidmachine-io-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 3
skills:
- name: bidmachine-android
  slug: bidmachine-android
- name: bidmachine-ios
  slug: bidmachine-ios
- name: bidmachine-unity
  slug: bidmachine-unity
slug: bidmachine-io
tags:
- Advertising
- AdTech
- Mobile Advertising
- Ad Exchange
- Ad Mediation
- In-App Bidding
- OpenRTB
- App Monetization
- Programmatic Advertising
- Mobile SDK
- Reporting
- Company
website: https://bidmachine.io/
---
