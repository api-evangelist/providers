---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'Undocumented private HTTP/JSON API at api.rightwayhealthcare.com that backs the Rightway member mobile apps (iOS/Android) and the member web app at member.rightwayhealthcare.com. The host is publicly '
  name: Rightway Member API
  slug: member-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rightway-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rightway-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rightway-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rightway-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.rightwayhealthcare.com/
- group: company
  title: ''
  type: Blog
  url: https://www.rightwayhealthcare.com/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://www.rightwayhealthcare.com/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.rightwayhealthcare.com/members/get-help
- group: start
  title: ''
  type: Login
  url: https://member.rightwayhealthcare.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rightwayhealthcare.com/terms-services
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rightwayhealthcare.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.rightwayhealthcare.com/compliance
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rightwayhealthcare.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/roadmaphealthcare
- group: company
  title: ''
  type: Careers
  url: https://www.rightwayhealthcare.com/careers
- group: company
  title: ''
  type: Press
  url: https://www.rightwayhealthcare.com/press
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rightway-healthcare
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/rightway_stock/
created: '2026-08-02'
description: Rightway Healthcare is a New York-based healthcare navigation and pharmacy benefit management (PBM) company founded by Jordan Feldman and Dr. Theodore Feldman. It pairs a clinical care-navigation service — licensed pharmacists, nurses and care guides reachable by phone and in-app — with a fully transparent, 100% pass-through PBM that earns revenue from a single administrative fee rather than rebate spread. Rightway serves employers, health systems and public-sector plans covering roughly three million members, with named clients including Tyson Foods, TikTok and Zoom, and ships member-facing iOS, Android and web apps backed by a private mobile API. The company is HITRUST CSF certified and SOC 2 attested. It publishes no public developer program, API documentation or machine-readable API contract as of this profiling pass.
image: https://cdn.sanity.io/images/c67aqxu5/production/8ebd5e736e6fed503510282e4032d6a90c9041e5-2400x1260.png
layout: provider
modified: '2026-08-02'
name: Rightway
nav: Providers
network: true
overview: 'Rightway publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Pharmacy Benefits, PBM, and Care Navigation.


  Rightway''s developer surface includes engineering blog, support, and 16 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 23.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 47.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rightway/refs/heads/main/screenshots/rightway-2026-09-02T153819.png
security:
- kind: domain-security
  name: Rightway Domain Security
  slug: rightway-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rightway
tags:
- Company
- Healthcare
- Pharmacy Benefits
- PBM
- Care Navigation
- Health Insurance
- Employee Benefits
- Digital Health
- HIPAA
website: https://www.rightwayhealthcare.com/
---
