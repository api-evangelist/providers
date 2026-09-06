---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 29.7
  scored_at: '2026-09-05'
api_count: 3
apis:
- baseURL: http://api.appsamurai.com
  baseurl_source: declared
  description: The Campaign Spend API from Appsamurai — 1 operation(s) for campaign spend.
  name: Appsamurai Campaign Spend API
  slug: appsamurai-campaign-spend-api
- baseURL: http://api.appsamurai.com
  baseurl_source: declared
  description: App management endpoints
  name: Appsamurai App API
  slug: appsamurai-app-api
- baseURL: http://api.appsamurai.com
  baseurl_source: declared
  description: Audience management endpoints
  name: Appsamurai Audience API
  slug: appsamurai-audience-api
- baseURL: http://api.appsamurai.com
  baseurl_source: declared
  description: Instance management endpoints
  name: Appsamurai Instance API
  slug: appsamurai-instance-api
- baseURL: http://api.appsamurai.com
  baseurl_source: declared
  description: Segment management endpoints
  name: Appsamurai Segment API
  slug: appsamurai-segment-api
- baseURL: http://api.appsamurai.com
  baseurl_source: declared
  description: Story management endpoints
  name: Appsamurai Story API
  slug: appsamurai-story-api
- baseURL: http://api.appsamurai.com
  baseurl_source: declared
  description: Story group management endpoints
  name: Appsamurai Story Group API
  slug: appsamurai-story-group-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AppSamurai Campaign Spend API
  slug: open-appsamurai-campaign-spend-api
- collection_type: open
  name: Storyly External API
  slug: open-appsamurai-storyly-external-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/appsamurai-storyly-external-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appsamurai-campaign-spend-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appsamurai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appsamurai.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.storyly.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.storyly.io/docs
- group: operate
  title: ''
  type: HelpCenter
  url: https://appsamurai.com/help/
- group: operate
  title: ''
  type: Support
  url: https://appsamurai.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://appsamurai.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Netvent
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.appsamurai.com/login
- group: start
  title: ''
  type: Login
  url: https://dashboard.appsamurai.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appsamurai.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appsamurai.com/terms-of-use/
- group: auth
  title: ''
  type: Compliance
  url: https://appsamurai.com/information-security-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/appsamurai-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/appsamurai-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/appsamurai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/appsamurai-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/appsamurai-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/appsamurai-mcp.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/appsamurai-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/appsamurai-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/appsamurai-conformance.yml
- group: docs
  title: ''
  type: APIReference
  url: https://help.appsamurai.com/en/articles/11105087-appsamurai-campaign-spend-api
- group: operate
  title: ''
  type: StatusPage
  url: https://status.storyly.io/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/appsamurai-lifecycle.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/appsamurai-tool-crosswalk.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/appsamurai-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/appsamurai-components.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/appsamurai-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/appsamurai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/appsamurai-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.storyly.io/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.storyly.io/docs/introduction
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/appsamurai-storyly-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: AppSamurai (legally Apps Medya Teknoloji A.S., engineering org Netvent) is a global, AI-powered mobile app growth platform founded in 2016. It offers user acquisition, retargeting, OEM / on-device app discovery, rewarded user acquisition and monetization across one platform, plus Storyly, its AI-powered in-app content experience product for mobile commerce, and the Interceptd ad fraud detection product. AppSamurai reaches over two billion users across more than 130 countries and works with mobile operators and device manufacturers such as Samsung, Xiaomi, Huawei, Oppo and Lenovo. It publishes two APIs. The Storyly External API covers 18 operations over apps, instances, story groups, stories, audiences and segments, authenticated with a bearer JWT, with a provider-published OpenAPI advertised through an RFC 9727 api-catalog on its docs host. The AppSamurai Campaign Spend API is a single keyed HTTP GET returning campaign spend reporting. AppSamurai also runs a live remote MCP
  server at mcp.storyly.io serving Storyly Placement SDK knowledge to agents, and ships embeddable Placement widget SDKs for Android, iOS, Web, React Native and Flutter. AppSamurai is ISO 27001 certified for information security. This profile was surfaced as a 500 Global portfolio company and enriched by the API Evangelist pipeline.
image: https://appsamurai.com/og-default.png
layout: provider
modified: '2026-08-13'
name: Appsamurai
nav: Providers
network: true
overview: 'Appsamurai publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Campaign Spend API, App API, Audience API, and 4 more. Tagged areas include Company, Mobile, Advertising, User Acquisition, and Marketing.


  Appsamurai''s developer surface includes documentation, support, engineering blog, signup flow, authentication, API reference, changelog, and 30 more developer resources.'
plans:
- name: Appsamurai Plans Pricing
  plan_count: 3
  slug: appsamurai-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Appsamurai Rate Limits
  slug: appsamurai-rate-limits
score:
  band: developing
  composite: 53.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 53.9
    developer_ergonomics: 55.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 53.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 7
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/appsamurai/refs/heads/main/screenshots/appsamurai-2026-07-25T200844.png
security:
- kind: authentication
  name: Appsamurai Authentication
  slug: appsamurai-authentication
  summary_line: http-bearer/apiKey · 2 schemes
- kind: domain-security
  name: Appsamurai Domain Security
  slug: appsamurai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Appsamurai Vulnerability Disclosure
  slug: appsamurai-vulnerability-disclosure
  summary_line: Hackerone
slug: appsamurai
tags:
- Company
- Mobile
- Advertising
- User Acquisition
- Marketing
- App Growth
- Attribution
- Analytics
- Mobile Marketing
- SDK
- Storyly
- Content Experience
- In-App Stories
- MCP
- Mobile Commerce
website: https://appsamurai.com
---
