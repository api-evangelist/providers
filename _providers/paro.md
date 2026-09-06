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
  url: security/paro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://paro.ai
- group: company
  title: ''
  type: About
  url: https://paro.ai/about/
- group: company
  title: ''
  type: Blog
  url: https://paro.ai/blog/
- group: other
  title: ''
  type: Resources
  url: https://paro.ai/resources/
- group: operate
  title: ''
  type: Support
  url: https://paro.ai/how-paro-works/
- group: start
  title: ''
  type: SignUp
  url: https://app.paro.io/registration/aigp-onboarding
- group: start
  title: ''
  type: Login
  url: https://app.paro.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://paro.ai/platform-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://paro.ai/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/paro-ai
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/paro-llms.txt
created: '2026-07-17'
description: Paro is an AI-powered professional services marketplace that connects businesses and accounting firms with vetted, on-demand finance and accounting experts. Founded in 2015 and headquartered in Chicago, Paro uses proprietary AI matching to pair clients with the top 2% of finance professionals across 60+ industries and 250+ skill sets — spanning bookkeeping, fractional CFO and controller services, financial planning and analysis, tax and compliance, and full-time recruiting. For accounting firms it provides staff augmentation, busy-season support, and service-expansion consulting. Paro operates a talent platform (app.paro.io) but does not publish a public developer API; this profile captures its identity, content, and public web surface for the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paro.png
layout: provider
modified: '2026-07-20'
name: Paro
nav: Providers
network: true
overview: 'Paro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Accounting, Marketplace, and Talent.


  Paro''s developer surface includes engineering blog, support, signup flow, and 9 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 14.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paro/refs/heads/main/screenshots/paro-2026-08-07T191448.png
security:
- kind: domain-security
  name: Paro Domain Security
  slug: paro-domain-security
  summary_line: TLSv1.3 · DMARC
slug: paro
tags:
- Company
- Finance
- Accounting
- Marketplace
- Talent
- Fractional CFO
- Bookkeeping
- Professional Services
- Artificial Intelligence
website: https://paro.ai
---
