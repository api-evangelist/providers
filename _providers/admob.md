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
  schema_version: '0.2'
  score: 31.8
  scored_at: '2026-09-15'
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
  href: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/overlays/admob-api-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/admob-api-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/overlays/admob-api-v1beta-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/admob-api-v1beta-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/agentic-access/admob-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/admob-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/security/admob-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/admob-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://g.co/vrp
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/security/admob-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/admob-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/security/admob-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/admob-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cloud.google.com/security/compliance
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/well-known/admob-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/admob-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/well-known/admob-security.txt
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
  href: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/authentication/admob-authentication.yml
  title: ''
  type: Authentication
  url: authentication/admob-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/scopes/admob-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/admob-scopes.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/packages/admob-packages.yml
  title: ''
  type: Packages
  url: packages/admob-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/packages/admob-packages.yml
  title: ''
  type: SDKs
  url: packages/admob-packages.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/changelog/admob-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/admob-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/lifecycle/admob-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/admob-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/lifecycle/admob-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/admob-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/conventions/admob-conventions.yml
  title: ''
  type: Conventions
  url: conventions/admob-conventions.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/llms/admob-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/admob-llms.txt
- group: operate
  title: ''
  type: StatusPage
  url: https://ads.google.com/status/publisher/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/rate-limits/admob-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/admob-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/errors/admob-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/admob-problem-types.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/plans/admob-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/admob-plans-pricing.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/sandbox/admob-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/admob-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/data-model/admob-data-model.yml
  title: ''
  type: DataModel
  url: data-model/admob-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/conformance/admob-conformance.yml
  title: ''
  type: Conformance
  url: conformance/admob-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/admob/refs/heads/main/skills/_index.yml
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
  band: developing
  composite: 54.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 53.9
    developer_ergonomics: 61.3
    discoverability: 75.9
    operational_transparency: 84.2
  previous_composite: 54.1
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
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
