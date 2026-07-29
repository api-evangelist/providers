---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Google Admob Agentic Access
  operation_count: 6
  slug: google-admob-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 5
apis:
- description: The Accounts API from Google AdMob — 1 operation(s) for accounts.
  name: Google AdMob Accounts API
  slug: google-admob-accounts-api
- description: The adUnits API from Google AdMob — 1 operation(s) for adunits.
  name: Google AdMob adUnits API
  slug: google-admob-adunits-api
- description: The Apps API from Google AdMob — 1 operation(s) for apps.
  name: Google AdMob Apps API
  slug: google-admob-apps-api
- description: The mediationGroups API from Google AdMob — 1 operation(s) for mediationgroups.
  name: Google AdMob mediationGroups API
  slug: google-admob-mediationgroups-api
- description: The networkReport:generate API from Google AdMob — 1 operation(s) for networkreport:generate.
  name: Google AdMob networkReport:generate API
  slug: google-admob-networkreport-generate-api
artifact_total: 15
collections:
- collection_type: open
  name: Google AdMob API
  slug: open-openapi
common:
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
  type: Authentication
  url: authentication/google-admob-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-admob-scopes.yml
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
  type: GettingStarted
  url: https://developers.google.com/admob/api/v1/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://admob.google.com/home/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/json-ld.yml
created: '2026-03-13'
description: The Google AdMob API provides programmatic access to information about AdMob accounts, allowing publishers to retrieve details about ad sources, ad units, apps, and mediation groups, and to generate campaign, mediation, and network reports for mobile app monetization.
finops:
- name: Google Admob Finops
  service_category: API
  slug: google-admob-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-admob.png
layout: provider
modified: '2026-05-19'
name: Google AdMob
nav: Providers
network: true
overview: 'Google AdMob publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, adUnits API, Apps API, and 2 more. Tagged areas include Ad Mediation, AdMob, App Monetization, Mobile Advertising, and Mobile Apps.


  The Google AdMob catalog on APIs.io includes 1 Spectral governance ruleset.


  Google AdMob''s developer surface includes authentication, getting-started guide, pricing, and 7 more developer resources.'
plans:
- name: Google Admob Plans Pricing
  plan_count: 3
  slug: google-admob-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 5
  name: Google Admob Rate Limits
  slug: google-admob-rate-limits
rules:
- name: Google AdMob API Rules
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
  band: developing
  composite: 49.4
  delta: -4.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 63.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 53.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
slug: google-admob
tags:
- Ad Mediation
- AdMob
- App Monetization
- Mobile Advertising
- Mobile Apps
- Reports
---
