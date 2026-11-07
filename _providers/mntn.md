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
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.5
  scored_at: '2026-11-06'
api_count: 19
apis:
- baseURL: https://api3.mountain.com
  baseurl_source: declared
  description: Public partner reporting surface at api3.mountain.com. GET /apilist returns the tables and columns available to the authenticated advertiser; GET and POST /apidata execute multidimensional queries ove
  name: MNTN Reporting API 3.0
  slug: mntn-reporting-api-30
- baseURL: https://api.mountain.com/ptv
  baseurl_source: declared
  description: Advertiser directory.
  name: MNTN Advertisers API
  slug: mntn-advertisers-api
- baseURL: https://api.mountain.com/ptv
  baseurl_source: declared
  description: Advertiser attribution windows, estimates, sales cycle, and verified-visit blacklist settings.
  name: MNTN Attribution API
  slug: mntn-attribution-api
- baseURL: https://api.mountain.com/ptv
  baseurl_source: declared
  description: Audience and geo-list management.
  name: MNTN Audiences API
  slug: mntn-audiences-api
- baseURL: https://api.mountain.com/ptv
  baseurl_source: declared
  description: Async CSV exports under **`/batch`…** (submit, poll status, signed download URLs)
  name: MNTN Batch API
  slug: mntn-batch-api
- baseURL: https://api.mountain.com/ptv
  baseurl_source: declared
  description: Campaign list, lookup, and lifecycle.
  name: MNTN Campaigns API
  slug: mntn-campaigns-api
- baseURL: https://api.mountain.com/ptv
  baseurl_source: declared
  description: Creative library lookup, with normalized video processing status.
  name: MNTN Creatives API
  slug: mntn-creatives-api
- baseURL: https://api.mountain.com/ptv
  baseurl_source: declared
  description: Flight (budget window) reads and updates within a campaign.
  name: MNTN Flights API
  slug: mntn-flights-api
- baseURL: https://api.mountain.com/ptv
  baseurl_source: declared
  description: Organization name and mode updates (proxied to advertiser-service).
  name: MNTN Organizations API
  slug: mntn-organizations-api
- baseURL: https://api.mountain.com/ptv
  baseurl_source: declared
  description: Pixel configuration, health, verification, and GA4 management.
  name: MNTN Pixel API
  slug: mntn-pixel-api
- baseURL: https://api.mountain.com/ptv
  baseurl_source: declared
  description: Deal-group assignment to campaigns.
  name: MNTN Pmp Campaign Deals API
  slug: mntn-pmp-campaign-deals-api
- baseURL: https://api.mountain.com/ptv
  baseurl_source: declared
  description: Private marketplace channel reference set.
  name: MNTN Pmp Channels API
  slug: mntn-pmp-channels-api
- baseURL: https://api.mountain.com/ptv
  baseurl_source: declared
  description: Private marketplace deal-group management and deal membership.
  name: MNTN Pmp Deal Groups API
  slug: mntn-pmp-deal-groups-api
- baseURL: https://api.mountain.com/ptv
  baseurl_source: declared
  description: Private marketplace deal reads and lifecycle.
  name: MNTN Pmp Deals API
  slug: mntn-pmp-deals-api
- baseURL: https://api.mountain.com/ptv
  baseurl_source: declared
  description: Private marketplace partner directory.
  name: MNTN Pmp Partners API
  slug: mntn-pmp-partners-api
- baseURL: https://api.mountain.com/ptv
  baseurl_source: declared
  description: Enumerations and lookup data shared across endpoints.
  name: MNTN Reference API
  slug: mntn-reference-api
- baseURL: https://api3.mountain.com
  baseurl_source: declared
  description: The Apidata API from MNTN — 1 operation(s) for apidata.
  name: MNTN Apidata API
  slug: mntn-apidata-api
- baseURL: https://api3.mountain.com
  baseurl_source: declared
  description: The Apilist API from MNTN — 1 operation(s) for apilist.
  name: MNTN Apilist API
  slug: mntn-apilist-api
artifact_total: 47
collections:
- collection_type: open
  name: MNTN Async Batch Export API - Batch
  slug: open-mntn-batch-export
- collection_type: open
  name: PTV API - advertisers
  slug: open-mntn-ptv-advertisers
- collection_type: open
  name: PTV API - attribution
  slug: open-mntn-ptv-attribution
- collection_type: open
  name: PTV API - audiences
  slug: open-mntn-ptv-audiences
- collection_type: open
  name: PTV API - campaigns
  slug: open-mntn-ptv-campaigns
- collection_type: open
  name: PTV API - creatives
  slug: open-mntn-ptv-creatives
- collection_type: open
  name: PTV API - flights
  slug: open-mntn-ptv-flights
- collection_type: open
  name: PTV API - organizations
  slug: open-mntn-ptv-organizations
- collection_type: open
  name: PTV API - pixel
  slug: open-mntn-ptv-pixel
- collection_type: open
  name: PTV API - pmp-campaign-deals
  slug: open-mntn-ptv-pmp-campaign-deals
- collection_type: open
  name: PTV API - pmp-channels
  slug: open-mntn-ptv-pmp-channels
- collection_type: open
  name: PTV API - pmp-deal-groups
  slug: open-mntn-ptv-pmp-deal-groups
- collection_type: open
  name: PTV API - pmp-deals
  slug: open-mntn-ptv-pmp-deals
- collection_type: open
  name: PTV API - pmp-partners
  slug: open-mntn-ptv-pmp-partners
- collection_type: open
  name: PTV API - reference
  slug: open-mntn-ptv-reference
- collection_type: open
  name: PTV API - reporting
  slug: open-mntn-ptv-reporting
- collection_type: open
  name: MNTN Reporting API - API
  slug: open-mntn-reporting-api
common:
- group: other
  href: https://artifacts.apis.io/mntn/capabilities/mntn-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/mntn-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/mntn/overlays/mntn-ptv-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mntn-ptv-overlay.yaml
- group: other
  href: https://artifacts.apis.io/mntn/overlays/mntn-batch-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mntn-batch-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://mountain.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.mountain.com/en/collections/13086998-apis
- group: docs
  title: ''
  type: APIReference
  url: https://api.mountain.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://help.mountain.com/en/articles/6511970-access-your-reporting-api-key
- group: operate
  title: ''
  type: Support
  url: https://help.mountain.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.mountain.com/en/
- group: company
  title: ''
  type: Blog
  url: https://mountain.com/blog/
- group: start
  title: ''
  type: SignUp
  url: https://auth.mountain.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://auth.mountain.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mountain.com/terms-and-conditions/
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://mountain.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mountain.com/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.mountain.com/en/collections/16047071-track-releases
- group: operate
  href: https://artifacts.apis.io/mntn/changelog/mntn-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mntn-changelog.yml
- group: design
  href: https://artifacts.apis.io/mntn/lifecycle/mntn-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mntn-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/mntn/lifecycle/mntn-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/mntn-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/mntn/authentication/mntn-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mntn-authentication.yml
- group: design
  href: https://artifacts.apis.io/mntn/conventions/mntn-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mntn-conventions.yml
- group: design
  href: https://artifacts.apis.io/mntn/errors/mntn-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mntn-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/mntn/rate-limits/mntn-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mntn-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/mntn/plans/mntn-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mntn-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/mntn/conformance/mntn-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mntn-conformance.yml
- group: auth
  href: https://artifacts.apis.io/mntn/security/mntn-trust-center.yml
  title: ''
  type: Compliance
  url: security/mntn-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/mntn/security/mntn-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/mntn-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/mntn/security/mntn-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/mntn-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mntn/security/mntn-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mntn-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mntn/security/mntn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mntn-domain-security.yml
- group: design
  href: https://artifacts.apis.io/mntn/components/mntn-components.yml
  title: ''
  type: Components
  url: components/mntn-components.yml
- group: agent
  href: https://artifacts.apis.io/mntn/llms/mntn-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mntn-llms.txt
- group: agent
  href: https://artifacts.apis.io/mntn/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-12'
description: 'MNTN (mountain.com) is a Connected TV performance marketing platform that lets brands plan, launch, target, measure, and optimize outcome-based TV advertising across streaming inventory. Its programmable surface is two distinct HTTP APIs: the Performance TV (PTV) platform API at api.mountain.com, an OpenAPI 3.1 contract covering advertisers, organizations, campaigns, flights, creatives, audiences and geo-lists, conversion pixel setup and verification, attribution windows and estimates, private marketplace (PMP) partners/deals/deal-groups/channels, reference vocabularies, and reporting; and the Reporting API 3.0 at api3.mountain.com, a partner reporting surface (/apilist metadata, /apidata query execution) plus an asynchronous /batch CSV export API that returns time-limited signed download URLs. Both are documented with published OpenAPI definitions rendered through Scalar. Authentication is an MNTN-issued advertiser API key (X-API-Key header on the platform API, key query parameter
  on the reporting API) or a bearer JWT. Errors are RFC 9457 problem+json with traceId and errorCode.'
finops:
- has_sources: true
  method: derived
  name: Mntn Finops
  primary_unit: ''
  service_category: ''
  slug: mntn-finops
  template: true
image: https://mountain.com/wp-content/uploads/2025/02/MNTN_Homepage_Open-Graph-1200x630-1.jpg
layout: provider
modified: '2026-08-12'
name: MNTN
nav: Providers
network: true
overview: 'MNTN publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Reporting API 3.0, Advertisers API, Attribution API, and 15 more. Tagged areas include Connected TV, ctv-advertising, Advertising, Performance Marketing, and Streaming TV.


  The MNTN catalog on APIs.io includes 1 Spectral governance ruleset.


  MNTN''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 26 more developer resources.'
plans:
- name: Mntn Plans Pricing
  plan_count: 0
  slug: mntn-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Mntn Rate Limits
  slug: mntn-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: MNTN API Rules
  rule_count: 61
  severity_counts:
    error: 41
    hint: 0
    info: 8
    warn: 12
  slug: mntn-rules
score:
  band: developing
  composite: 50.2
  coverage:
    artifact_dirs: 28
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 54.0
    developer_ergonomics: 49.4
    discoverability: 78.6
    operational_transparency: 34.2
  previous_composite: 50.2
  provenance:
    conformance: derived
    contracts:
      callable: 83.3
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/mntn/mntn-2026-08-17T081059.png
security:
- kind: authentication
  name: Mntn Authentication
  slug: mntn-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Mntn Domain Security
  slug: mntn-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Mntn Vulnerability Disclosure
  slug: mntn-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Mntn Trust Center
  slug: mntn-trust-center
  summary_line: SOC 2 Type II
skill_count: 4
skills:
- name: mntn-launch-ctv-campaign
  slug: mntn-launch-ctv-campaign
- name: mntn-manage-pmp-deals
  slug: mntn-manage-pmp-deals
- name: mntn-pull-reporting-data
  slug: mntn-pull-reporting-data
- name: mntn-verify-conversion-pixel
  slug: mntn-verify-conversion-pixel
slug: mntn
tags:
- Connected TV
- ctv-advertising
- Advertising
- Performance Marketing
- Streaming TV
- Media Buying
- Attribution
- Audience Targeting
- Conversion Tracking
- Programmatic Advertising
- private-marketplace
- Marketing Reporting
- AdTech
website: https://mountain.com/
---
