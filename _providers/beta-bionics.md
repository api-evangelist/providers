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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The private cloud API behind the Beta Bionics Bionic (HCP) Portal and the iLet / Bionic Circle mobile apps. Observed as an Amazon API Gateway deployment at us-main-prod.betabionicsapi.com, authenticat
  name: Beta Bionics Bionic Portal API
  slug: hcp-portal-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.betabionics.com/
- group: operate
  title: ''
  type: Support
  url: https://www.betabionics.com/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.betabionics.com/faqs/
- group: company
  title: ''
  type: Blog
  url: https://www.betabionics.com/articles/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.betabionics.com/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.betabionics.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.betabionics.com/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.betabionics.com/privacy/
- group: company
  title: ''
  type: Investors
  url: https://investors.betabionics.com/
- group: company
  title: ''
  type: Careers
  url: https://www.betabionics.com/about-us/careers/
- group: auth
  title: ''
  type: Authentication
  url: authentication/beta-bionics-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/beta-bionics-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/beta-bionics-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beta-bionics-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/beta-bionics-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/beta-bionics-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/beta-bionics-packages.yml
created: '2026-08-02'
description: 'Beta Bionics, Inc. (Nasdaq: BBNX) is a commercial-stage medical technology company in Irvine, California and Boston, Massachusetts that designs, develops and commercializes the iLet Bionic Pancreas — an FDA-cleared automated insulin delivery system made up of the iLet ACE Pump and the iLet Dosing Decision Software, paired with a Dexcom G6/G7 or Abbott FreeStyle Libre 3 Plus continuous glucose monitor. The iLet initializes on body weight alone and determines 100% of insulin doses without carb counting, correction factors or preset basal rates. Device data flows from the pump to the iLet mobile app and on to the Beta Bionics cloud, where it feeds the Bionic Circle follower app (up to 10 caregivers), clinician reporting in the Bionic (HCP) Portal, and uploads to Glooko for remote patient monitoring. Beta Bionics publishes near-real-time real-world outcomes for its whole connected population on a public dashboard. There is no public developer program, no published API documentation
  and no machine-readable API contract: the cloud APIs behind the portal and mobile apps are private, HIPAA-regulated, and gated behind Amazon Cognito.'
image: https://www.betabionics.com/wp-content/uploads/logo-white.svg
layout: provider
modified: '2026-08-02'
name: Beta Bionics
nav: Providers
network: true
overview: 'Beta Bionics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Medical Devices, and Diabetes.


  Beta Bionics'' developer surface includes support, engineering blog, authentication, and 14 more developer resources.'
random_paper: 3
scopes:
- name: Beta Bionics Scopes
  scope_count: 4
  slug: beta-bionics-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 25.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beta-bionics/refs/heads/main/screenshots/beta-bionics-2026-08-07T162324.png
security:
- kind: authentication
  name: Beta Bionics Authentication
  slug: beta-bionics-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Beta Bionics Domain Security
  slug: beta-bionics-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: beta-bionics
tags:
- Company
- Health
- Healthcare
- Medical Devices
- Diabetes
- Automated Insulin Delivery
- Digital Health
- Remote Patient Monitoring
- HIPAA
- Connected Devices
website: https://www.betabionics.com/
---
