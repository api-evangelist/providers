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
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vinted-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.vinted.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vinted-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vinted-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/vinted-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vinted-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.vinted.com
- group: operate
  title: ''
  type: Support
  url: https://www.vinted.com/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vinted.com/terms_and_conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vinted.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://company.vinted.com/en/newsroom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vinted
created: '2026-07-17'
description: Vinted is a European consumer-to-consumer (C2C) online marketplace for buying and selling secondhand clothes, shoes, accessories, and other lifestyle items, operating across web and mobile apps in dozens of markets. Founded in Vilnius, Lithuania, it is one of Europe's largest secondhand fashion platforms and is backed by Accel, Insight Partners, and Lightspeed Venture Partners. Vinted does not publish a public developer API, SDKs, or a developer portal; this API Evangelist profile captures the company's public identity, legal, and security (security.txt / domain-security) surfaces.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vinted.png
layout: provider
modified: '2026-07-21'
name: Vinted
nav: Providers
network: true
overview: 'Vinted is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Marketplace, E-Commerce, and Secondhand.


  Vinted''s developer surface includes support, engineering blog, and 10 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 12.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vinted/refs/heads/main/screenshots/vinted-2026-09-02T165937.png
security:
- kind: domain-security
  name: Vinted Domain Security
  slug: vinted-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Vinted Vulnerability Disclosure
  slug: vinted-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: vinted
tags:
- Company
- Consumer
- Marketplace
- E-Commerce
- Secondhand
- Fashion
- C2C
- Europe
website: https://www.vinted.com
---
