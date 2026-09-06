---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
- group: company
  title: ''
  type: Website
  url: http://www.thredup.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.thredup.com/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thredup.com/help/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thredup.com/help/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://labs.thredup.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thredup
- group: company
  title: ''
  type: Partners
  url: https://www.raas.thredup.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thredup-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thredup-domain-security.yml
created: '2026-07-17'
description: 'ThredUp (NASDAQ: TDUP) is one of the world''s largest online resale and consignment platforms for secondhand women''s and kids'' clothing, shoes, and accessories. Founded in 2009 and headquartered in Oakland, CA, it lets consumers buy and sell pre-owned fashion via mailed Clean Out Kits, and powers branded recommerce for 60+ retailers through its Resale-as-a-Service (RaaS) platform. ThredUp does not publish a public developer API or OpenAPI; RaaS integrations are arranged through its partner sales team, so this API Evangelist profile captures the company''s public web, engineering, and policy surface rather than a documented API program.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thredup.png
layout: provider
modified: '2026-07-21'
name: ThredUp
nav: Providers
network: true
overview: 'ThredUp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Resale, Secondhand, and Fashion.


  ThredUp''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 4
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
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 11.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thredup/refs/heads/main/screenshots/thredup-2026-09-02T163614.png
security:
- kind: domain-security
  name: Thredup Domain Security
  slug: thredup-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: thredup
tags:
- Company
- E-Commerce
- Resale
- Secondhand
- Fashion
- Consignment
- Sustainability
- Retail
website: http://www.thredup.com/
---
