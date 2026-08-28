---
agent_readiness:
  band: agent-aware
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.2
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: OpenAPI 3.1 platform API for MNTN Performance TV. Covers advertisers and organizations, campaign and flight lifecycle (create, update, launch, pause, archive), creatives, audiences including geo lists
  name: MNTN Performance TV (PTV) API
  slug: mntn-performance-tv-ptv-api
- description: Public partner reporting surface at api3.mountain.com. GET /apilist returns the tables and columns available to the authenticated advertiser; GET and POST /apidata execute multidimensional queries ove
  name: MNTN Reporting API 3.0
  slug: mntn-reporting-api-30
- description: Asynchronous CSV export API under /batch on api3.mountain.com, for reporting queries too large or slow to run synchronously (a 413 on /apidata is the documented trigger). POST /batch enqueues a job an
  name: MNTN Async Batch Export API
  slug: mntn-async-batch-export-api
artifact_total: 26
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
  title: ''
  type: ChangeLog
  url: changelog/mntn-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mntn-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/mntn-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mntn-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mntn-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mntn-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mntn-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mntn-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mntn-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/mntn-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mntn-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/mntn-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mntn-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mntn-domain-security.yml
- group: design
  title: ''
  type: Components
  url: components/mntn-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mntn-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-12'
description: 'MNTN (mountain.com) is a Connected TV performance marketing platform that lets brands plan, launch, target, measure, and optimize outcome-based TV advertising across streaming inventory. Its programmable surface is two distinct HTTP APIs: the Performance TV (PTV) platform API at api.mountain.com, an OpenAPI 3.1 contract covering advertisers, organizations, campaigns, flights, creatives, audiences and geo-lists, conversion pixel setup and verification, attribution windows and estimates, private marketplace (PMP) partners/deals/deal-groups/channels, reference vocabularies, and reporting; and the Reporting API 3.0 at api3.mountain.com, a partner reporting surface (/apilist metadata, /apidata query execution) plus an asynchronous /batch CSV export API that returns time-limited signed download URLs. Both are documented with published OpenAPI definitions rendered through Scalar. Authentication is an MNTN-issued advertiser API key (X-API-Key header on the platform API, key query parameter
  on the reporting API) or a bearer JWT. Errors are RFC 9457 problem+json with traceId and errorCode.'
image: https://mountain.com/wp-content/uploads/2025/02/MNTN_Homepage_Open-Graph-1200x630-1.jpg
layout: provider
modified: '2026-08-12'
name: MNTN
nav: Providers
network: true
overview: 'MNTN publishes 3 APIs on the [APIs.io](https://apis.io/) network: Performance TV (PTV) API, Reporting API 3.0, and Async Batch Export API. Tagged areas include Connected TV, ctv-advertising, Advertising, Performance Marketing, and Streaming TV.


  MNTN''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 23 more developer resources.'
plans:
- name: Mntn Plans Pricing
  plan_count: 0
  slug: mntn-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Mntn Rate Limits
  slug: mntn-rate-limits
score:
  band: developing
  composite: 50.8
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 16.7
    contract_quality: 60.8
    developer_ergonomics: 49.4
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 34.2
  previous_composite: 50.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mntn/refs/heads/main/screenshots/mntn-2026-08-17T081059.png
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
- marketing-reporting
- AdTech
website: https://mountain.com/
---
