---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 17.6
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The RapidDeploy platform API host that backs Nimbus CAD, Radius Mapping, Lightning and Eclipse Analytics. The host is live and answers with a JSON envelope, but every anonymous path returns 404 "Resou
  name: RapidDeploy Platform API
  slug: rapiddeploy-platform
artifact_total: 6
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/motorola-solutions/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rapiddeploy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.motorolasolutions.com/en_us/products/command-center-software/public-safety-software/ng9-1-1-call-management.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rapiddeploy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rapiddeploy.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rapiddeploy-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rapiddeploy-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rapiddeploy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/rapiddeploy-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rapiddeploy-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/rapiddeploy-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rapiddeploy-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/rapiddeploy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rapiddeploy-rate-limits.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.motorolasolutions.com/en_us/about/privacy-policy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.motorolasolutions.com/en_us/about/terms-use.html
coverage:
  checked: '2026-08-26'
  detail: RapidDeploy has no developer portal at all after the Motorola Solutions acquisition - rapiddeploy.com and every path under it 301s to a Motorola Solutions NG9-1-1 marketing page that never mentions RapidDeploy - while api.rapiddeploy.com stays live and answers every anonymous path with a JSON 404, so the contract is reachable only by an agency tenant holding credentials from the company's Auth0 tenant at auth.rapiddeploy.com.
  evidence:
  - status: 301
    url: https://rapiddeploy.com/
  - status: 404
    url: https://api.rapiddeploy.com/openapi.json
  - status: 404
    url: https://api.rapiddeploy.com/
  - status: 200
    url: https://auth.rapiddeploy.com/.well-known/openid-configuration
  - status: 0
    url: https://developer.rapiddeploy.com/
  reason: customer-only-docs
  state: gated
created: '2026-08-26'
description: 'RapidDeploy is a cloud-native Next Generation 9-1-1 (NG911) software company founded in 2013 in South Africa and headquartered in Austin, Texas from 2018. It builds call-taking, dispatch, mapping and analytics software for Public Safety Answering Points (PSAPs) on Microsoft Azure: Nimbus CAD (cloud computer-aided dispatch), Radius Mapping (NG911 primary call-taking tactical map with a deep ESRI integration and supplemental location data sources), Lightning (a first-responder mobile application) and Eclipse Analytics (response-time and staffing analytics). The company was acquired by Motorola Solutions and folded into its Command Center software portfolio; rapiddeploy.com and every path beneath it now HTTP 301 to a Motorola Solutions NG9-1-1 product page. RapidDeploy markets an open-API framework for integrating third-party systems such as Priority Dispatch for police, fire and EMS, but publishes no public API reference or machine-readable contract.'
image: https://avatars.githubusercontent.com/u/85182598?v=4
layout: provider
modified: '2026-08-26'
name: RapidDeploy
nav: Providers
network: true
overview: 'RapidDeploy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Public Safety, Emergency Services, NG911, and Computer-Aided Dispatch.


  RapidDeploy''s developer surface includes authentication and 15 more developer resources.'
plans:
- name: Rapiddeploy Plans Pricing
  plan_count: 0
  slug: rapiddeploy-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Rapiddeploy Rate Limits
  slug: rapiddeploy-rate-limits
scopes:
- name: Rapiddeploy Scopes
  scope_count: 0
  slug: rapiddeploy-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 25.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 64.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: authentication
  name: Rapiddeploy Authentication
  slug: rapiddeploy-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Rapiddeploy Domain Security
  slug: rapiddeploy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: rapiddeploy
tags:
- Company
- Public Safety
- Emergency Services
- NG911
- Computer-Aided Dispatch
- Mapping
- Analytics
- Government
- Cloud
website: https://www.motorolasolutions.com/en_us/products/command-center-software/public-safety-software/ng9-1-1-call-management.html
---
