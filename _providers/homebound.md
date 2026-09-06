---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/homebound-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.homebound.com/
- group: company
  title: ''
  type: Blog
  url: https://www.homebound.com/learn
- group: start
  title: ''
  type: Login
  url: https://app.homebound.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.homebound.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.homebound.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/homebound-team
- group: build
  title: ''
  type: Packages
  url: packages/homebound-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/homebound-llms.txt
created: '2026-07-17'
description: Homebound is a tech-enabled, personalized homebuilder that pairs a proprietary software platform with a managed network of trade partners to build homes on a customer's lot, sell finished and in-progress inventory homes, and run disaster rebuild programs — most notably wildfire recovery in California. Homeowners track budget, schedule, documents, and construction progress through a Homeowner Portal. Backed by Fifth Wall, Forerunner Ventures, and GV, Homebound operates in the construction-tech sector. Homebound does not publish a public developer API or developer portal; its public engineering footprint is the homebound-team GitHub organization and the first-party open-source packages it publishes to the @homebound npm scope (the Beam design system, form-state, and truss). This profile was added to the API Evangelist network as a VC-portfolio lead and enriched from public company surfaces.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/homebound.png
layout: provider
modified: '2026-07-19'
name: Homebound
nav: Providers
network: true
overview: 'Homebound is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction Tech, Homebuilding, Real-Estate, and PropTech.


  Homebound''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 12.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/homebound/refs/heads/main/screenshots/homebound-2026-07-25T221338.png
security:
- kind: domain-security
  name: Homebound Domain Security
  slug: homebound-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: homebound
tags:
- Company
- Construction Tech
- Homebuilding
- Real-Estate
- PropTech
- Home Construction
- Disaster Rebuild
website: https://www.homebound.com/
---
