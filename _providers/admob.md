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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 31.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Admob Agentic Access
  operation_count: 25
  slug: admob-agentic-access
  summary_line: 25 operations · 13 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://admob.googleapis.com
  baseurl_source: declared
  description: The accounts API from AdMob — 4 operation(s) for accounts.
  name: AdMob Accounts API
  slug: admob-accounts-api
- baseURL: https://admob.googleapis.com
  baseurl_source: declared
  description: The adapters API from AdMob — 1 operation(s) for adapters.
  name: AdMob Adapters API
  slug: admob-adapters-api
- baseURL: https://admob.googleapis.com
  baseurl_source: declared
  description: The adSources API from AdMob — 1 operation(s) for adsources.
  name: AdMob Ad Sources API
  slug: admob-adsources-api
- baseURL: https://admob.googleapis.com
  baseurl_source: declared
  description: The adUnitMappings API from AdMob — 2 operation(s) for adunitmappings.
  name: AdMob Ad Unit Mappings API
  slug: admob-adunitmappings-api
- baseURL: https://admob.googleapis.com
  baseurl_source: declared
  description: The adUnits API from AdMob — 2 operation(s) for adunits.
  name: AdMob Ad Units API
  slug: admob-adunits-api
- baseURL: https://admob.googleapis.com
  baseurl_source: declared
  description: The apps API from AdMob — 2 operation(s) for apps.
  name: AdMob Apps API
  slug: admob-apps-api
- baseURL: https://admob.googleapis.com
  baseurl_source: declared
  description: The campaignReport API from AdMob — 1 operation(s) for campaignreport.
  name: AdMob Campaign Report API
  slug: admob-campaignreport-api
- baseURL: https://admob.googleapis.com
  baseurl_source: declared
  description: The mediationAbExperiments API from AdMob — 2 operation(s) for mediationabexperiments.
  name: AdMob Mediation Ab Experiments API
  slug: admob-mediationabexperiments-api
- baseURL: https://admob.googleapis.com
  baseurl_source: declared
  description: The mediationGroups API from AdMob — 2 operation(s) for mediationgroups.
  name: AdMob Mediation Groups API
  slug: admob-mediationgroups-api
- baseURL: https://admob.googleapis.com
  baseurl_source: declared
  description: The mediationReport API from AdMob — 2 operation(s) for mediationreport.
  name: AdMob Mediation Report API
  slug: admob-mediationreport-api
- baseURL: https://admob.googleapis.com
  baseurl_source: declared
  description: The networkReport API from AdMob — 2 operation(s) for networkreport.
  name: AdMob Network Report API
  slug: admob-networkreport-api
artifact_total: 21
collections:
- collection_type: open
  name: AdMob API
  slug: open-admob-api-v1
- collection_type: open
  name: AdMob API
  slug: open-admob-api-v1beta
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/admob-api-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/admob-api-v1beta-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/admob-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/admob-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://g.co/vrp
- group: auth
  title: ''
  type: DomainSecurity
  url: security/admob-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/admob-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cloud.google.com/security/compliance
- group: agent
  title: ''
  type: WellKnown
  url: well-known/admob-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/admob-security.txt
- group: company
  title: ''
  type: Website
  url: https://admob.google.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.google.com/admob/api
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/admob/api/v1/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.google.com/admob/api/rest
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/admob/api/v1/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.google.com/admob
- group: company
  title: ''
  type: Blog
  url: https://ads-developers.googleblog.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleads
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.google.com/admob/api/release-notes
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://admob.google.com/home/get-started/
- group: auth
  title: ''
  type: Authentication
  url: authentication/admob-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/admob-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/admob-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/admob-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/admob-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/admob-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/admob-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/admob-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/admob-llms.txt
- group: operate
  title: ''
  type: StatusPage
  url: https://ads.google.com/status/publisher/
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/admob-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/admob-problem-types.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/admob-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/admob-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/admob-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/admob-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Support
  url: https://groups.google.com/g/google-admob-api-developer-forum
created: '2026-07-17'
description: AdMob is Google's mobile app advertising and monetization platform, letting app publishers earn revenue through in-app ads (banner, interstitial, rewarded, rewarded interstitial, native, and app open formats), maximize fill rate and eCPM with AdMob Mediation and open bidding across many ad networks, and understand performance through reporting and user metrics. The AdMob API (admob.googleapis.com) provides programmatic access to AdMob account data, apps, ad units, mediation configuration, and network, mediation and campaign performance reports over REST/JSON, authorized with Google OAuth 2.0 using the admob.readonly and admob.report scopes. The stable v1 channel is read-only; the v1beta channel carries the entire write surface — creating apps, ad units and ad unit mappings, and creating, patching and A/B testing mediation groups. Google publishes no OpenAPI for AdMob; the machine-readable contract is a Google Discovery Document served by the API host itself.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/admob.png
layout: provider
modified: '2026-08-12'
name: AdMob
nav: Providers
network: true
overview: 'AdMob publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Adapters API, Ad Sources API, and 8 more. Tagged areas include Company, Advertising, Mobile, Monetization, and Ads.


  AdMob''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, signup flow, and 33 more developer resources.'
plans:
- name: Admob Plans Pricing
  plan_count: 0
  slug: admob-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Admob Rate Limits
  slug: admob-rate-limits
scopes:
- name: Admob Scopes
  scope_count: 2
  slug: admob-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 54.8
  coverage:
    artifact_dirs: 24
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 53.9
    developer_ergonomics: 61.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 84.2
  previous_composite: 54.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/screenshots/admob-2026-07-25T181651.png
security:
- kind: authentication
  name: Admob Authentication
  slug: admob-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Admob Domain Security
  slug: admob-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Admob Vulnerability Disclosure
  slug: admob-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Admob Trust Center
  slug: admob-trust-center
  summary_line: ISO 27001, ISO 27017, ISO 27018, SOC 2, SOC 3, PCI DSS
slug: admob
tags:
- Company
- Advertising
- Mobile
- Monetization
- Ads
- Google
- Reporting
- Mediation
- AdTech
website: https://admob.google.com
---
