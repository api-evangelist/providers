---
access_model:
  confidence: high
  label: Free with per-project quota · Self-serve signup · OAuth consent required
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Google Admob Agentic Access
  operation_count: 25
  slug: google-admob-agentic-access
  summary_line: 25 operations · 13 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: 'The stable, entirely read-only channel of the AdMob API. Six operations: get and list publisher accounts, list apps, list ad units, and generate network and mediation reports. Converted from Google''s '
  name: Google AdMob API v1
  slug: google-admob-api-v1
- description: The beta channel of the AdMob API and the only one with a write surface. Nineteen operations adding ad source and adapter discovery, ad unit mappings (single and batch create), app and ad unit creatio
  name: Google AdMob API v1beta
  slug: google-admob-api-v1beta
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google AdMob Accounts API
  slug: open-google-admob-accounts-api
- collection_type: open
  name: Google AdMob Accounts adUnits API
  slug: open-google-admob-adunits-api
- collection_type: open
  name: Google AdMob API
  slug: open-google-admob-api-v1
- collection_type: open
  name: Google AdMob API
  slug: open-google-admob-api-v1beta
- collection_type: open
  name: Google AdMob Accounts Apps API
  slug: open-google-admob-apps-api
- collection_type: open
  name: Google AdMob Accounts mediationGroups API
  slug: open-google-admob-mediationgroups-api
- collection_type: open
  name: Google AdMob Accounts networkReport:generate API
  slug: open-google-admob-networkreport-generate-api
- collection_type: open
  name: Google AdMob API
  slug: open-openapi
common:
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
  url: https://groups.google.com/g/google-admob-api
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.google.com/admob
- group: company
  title: ''
  type: Blog
  url: https://ads-developers.googleblog.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleads
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/googleadmob
- group: start
  title: ''
  type: SignUp
  url: https://admob.google.com/home/get-started/
- group: commercial
  title: ''
  type: Pricing
  url: https://admob.google.com/home/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://ads.google.com/status/publisher/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.google.com/admob/api/release-notes
- group: auth
  title: ''
  type: Security
  url: https://g.co/vrp
- group: auth
  title: ''
  type: Compliance
  url: https://business.safety.google/compliance/
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-admob-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-admob-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-admob-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-admob-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-admob-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/google-admob-trust-center.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/google-admob-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/google-admob-security.txt
- group: build
  title: ''
  type: Packages
  url: packages/google-admob-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/google-admob-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/google-admob-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/google-admob-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/google-admob-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/google-admob-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/google-admob-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/google-admob-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/google-admob-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/google-admob-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/google-admob-finops.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/google-admob-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/google-admob-llms.txt
- group: other
  title: ''
  type: Protobuf
  url: grpc/google-admob-admob-api.proto
- group: design
  title: ''
  type: Rules
  url: rules/google-admob-jsonschema-spectral-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/json-ld.yml
created: '2026-03-13'
description: AdMob is Google's mobile app advertising and monetization platform, letting app publishers earn revenue through in-app ads (banner, interstitial, rewarded, rewarded interstitial, native and app open formats), maximize fill rate and eCPM with AdMob Mediation and open bidding across many ad networks, and understand performance through reporting. The AdMob API (admob.googleapis.com) provides programmatic access to AdMob account data, apps, ad units, ad sources and adapters, ad unit mappings, mediation groups and mediation A/B experiments, plus network, mediation and campaign performance reports, over REST/JSON authorized with Google OAuth 2.0 user tokens using the admob.readonly and admob.report scopes. Service accounts are not supported. The stable v1 channel is entirely read-only; the v1beta channel carries the whole write surface. Google publishes no OpenAPI for AdMob — the first-party machine-readable contract is a Google Discovery Document served by the API host itself, alongside
  a protobuf IDL in googleapis/googleapis.
finops:
- name: Google Admob Finops
  service_category: API
  slug: google-admob-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-admob.png
layout: provider
modified: '2026-08-13'
name: Google AdMob
nav: Providers
network: true
overview: 'Google AdMob publishes 2 APIs on the [APIs.io](https://apis.io/) network: API v1 and API v1beta. Tagged areas include Ad Mediation, AdMob, Advertising, App Monetization, and Mobile Advertising.


  The Google AdMob catalog on APIs.io includes 1 Spectral governance ruleset.


  Google AdMob''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 36 more developer resources.'
plans:
- name: Google Admob Plans Pricing
  plan_count: 0
  slug: google-admob-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 4
  name: Google Admob Rate Limits
  slug: google-admob-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google AdMob API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-admob-jsonschema-spectral-rules
scopes:
- name: Google Admob Scopes
  scope_count: 2
  slug: google-admob-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 63.8
  delta: -5.3
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 26.5
    contract_quality: 65.0
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 26.5
    operational_transparency: 76.3
  previous_composite: 69.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/google-admob/refs/heads/main/screenshots/google-admob-2026-06-20T182006.png
security:
- kind: authentication
  name: Google Admob Authentication
  slug: google-admob-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Admob Domain Security
  slug: google-admob-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Admob Vulnerability Disclosure
  slug: google-admob-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Google Admob Trust Center
  slug: google-admob-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, SOC 2 / SOC 3, SOC 1 Type 2, FedRAMP, PCI DSS
slug: google-admob
tags:
- Ad Mediation
- AdMob
- Advertising
- App Monetization
- Mobile Advertising
- Mobile Apps
- Reports
- Reporting
website: https://admob.google.com
---
