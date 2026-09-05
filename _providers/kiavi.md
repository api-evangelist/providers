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
  url: security/kiavi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.kiavi.com/legal/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kiavi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kiavi.com
- group: company
  title: ''
  type: Blog
  url: https://www.kiavi.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kiavi.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kiavi.com/legal/terms
created: '2026-07-17'
description: Kiavi (formerly LendingHome) is a technology-driven private lender for residential real estate investors, providing fix-and-flip bridge loans, new-construction financing, and DSCR rental loans across 49 states plus Washington, D.C. The company has originated more than $30 billion in loans and funded over 100,000 investment properties, pairing a digital application and portfolio-management experience with institutional capital. Kiavi is backed by Cowboy Ventures and Ribbit Capital. As of this enrichment pass Kiavi publishes no public developer API, OpenAPI, or developer portal; its public surface is a marketing site, a real-estate-investing blog, legal/policy pages, and a HackerOne-based security vulnerability disclosure program.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kiavi.png
layout: provider
modified: '2026-07-19'
name: Kiavi
nav: Providers
network: true
overview: 'Kiavi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Real-Estate, Lending, and Mortgage.


  Kiavi''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 3
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
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kiavi/refs/heads/main/screenshots/kiavi-2026-07-25T223715.png
security:
- kind: domain-security
  name: Kiavi Domain Security
  slug: kiavi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kiavi Vulnerability Disclosure
  slug: kiavi-vulnerability-disclosure
  summary_line: Hackerone
slug: kiavi
tags:
- Company
- Fintech
- Real-Estate
- Lending
- Mortgage
- Financial-Services
- PropTech
website: https://www.kiavi.com
---
