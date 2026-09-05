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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oscar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hioscar.com/
- group: company
  title: ''
  type: About
  url: https://www.hioscar.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.hioscar.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oscarhealth
- group: start
  title: ''
  type: Login
  url: https://www.hioscar.com/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hioscar.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hioscar.com/legal/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.hioscar.com/accreditations
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.hioscar.com/overview
- group: company
  title: ''
  type: Press
  url: https://www.hioscar.com/press
- group: company
  title: ''
  type: Careers
  url: https://www.hioscar.com/careers
created: '2026-07-17'
description: 'Oscar Health (NYSE: OSCR) is a technology-driven health insurance company founded in 2012 and headquartered in New York City. It offers individual and family health plans, small-business and ICHRA employer benefits, and Medicare Advantage in a growing set of U.S. states, pairing coverage with a consumer mobile app, 24/7 virtual urgent care, telemedicine, primary care, and concierge Care Teams. Oscar''s +Oscar division licenses its full-stack technology platform (Campaign Builder and other tools) to other payers and providers. The company is NCQA-accredited across Health Plan, Utilization Management, Credentialing, Provider Network, and Health Equity programs. Oscar is a General Catalyst portfolio company. As a CMS-regulated payer it is subject to the Interoperability and Patient Access rule, though it does not currently publish an open, self-serve developer API portal.'
image: https://avatars.githubusercontent.com/u/6516184?v=4
layout: provider
modified: '2026-07-20'
name: Oscar
nav: Providers
network: true
overview: 'Oscar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Insurance, Healthcare, Insurance, and Health Technology.


  Oscar''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 13.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 28.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oscar/refs/heads/main/screenshots/oscar-2026-08-07T190958.png
security:
- kind: domain-security
  name: Oscar Domain Security
  slug: oscar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oscar
tags:
- Company
- Health Insurance
- Healthcare
- Insurance
- Health Technology
- Telemedicine
- Medicare Advantage
- Digital Health
website: https://www.hioscar.com/
---
