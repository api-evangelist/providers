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
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/limehome-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/limehome-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/limehome-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.limehome.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.limehome.com/en/tech-blog/
- group: operate
  title: ''
  type: Support
  url: https://www.limehome.com/help?lang=en
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/limehome
- group: start
  title: ''
  type: Login
  url: https://www.limehome.com/en/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.limehome.com/en/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.limehome.com/en/privacy-policy/
- group: build
  title: ''
  type: Packages
  url: packages/limehome-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/limehome-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/limehome-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/limehome-llms.txt
created: '2026-07-17'
description: 'Limehome is a Munich-headquartered digital hospitality operator founded in 2018 that designs, leases and runs fully-equipped design apartments and aparthotels across Europe, from Berlin to Barcelona and Linz to Lecce. The company runs a 100% digital guest journey: guests browse and book units online, receive an access code, and complete check-in and check-out contactlessly with no on-site reception staff. Limehome operates offices in Munich and Madrid with more than 200 employees, is led by CEOs Dr. Josef Vollmayr and Cesar de Sousa Freitas, and is backed by Picus Capital, HV Capital and Lakestar. Revenue comes from direct bookings (fee-free, with a 15% membership discount) alongside a "Lease to Limehome" real-estate partnership model. Limehome runs a production API host at api.limehome.com behind AWS API Gateway, but publishes no public developer portal, documentation or machine-readable specification; that surface is first-party/private. The company does maintain a public
  GitHub organization with a small number of open-source engineering libraries, and an engineering blog.'
image: https://cdn.sanity.io/images/x7iv72nk/production/97cc8c1f97a4a959913d6b75ce965a66f48dda00-1821x1366.jpg
layout: provider
modified: '2026-07-19'
name: Limehome
nav: Providers
network: true
overview: 'Limehome is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Hospitality, Travel, and Real-Estate.


  Limehome''s developer surface includes engineering blog, support, and 12 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 6
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
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 14.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/limehome/refs/heads/main/screenshots/limehome-2026-07-25T225217.png
security:
- kind: domain-security
  name: Limehome Domain Security
  slug: limehome-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Limehome Vulnerability Disclosure
  slug: limehome-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: limehome
tags:
- Company
- Consumer
- Hospitality
- Travel
- Real-Estate
- PropTech
- Short-Term Rental
- Aparthotel
- Germany
- Europe
website: https://www.limehome.com/en/
---
