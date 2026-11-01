---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: No public developer API is provided; the site is an e‑commerce storefront built on Shopify.
  name: Brother's Bond Bourbon API
  slug: brother-s-bond-bourbon-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/brother-s-bond-bourbon/llms/brother-s-bond-bourbon-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brother-s-bond-bourbon-llms.txt
- group: agent
  href: https://artifacts.apis.io/brother-s-bond-bourbon/well-known/brother-s-bond-bourbon-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brother-s-bond-bourbon-well-known.yml
- group: other
  href: https://artifacts.apis.io/brother-s-bond-bourbon/hosts/brother-s-bond-bourbon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brother-s-bond-bourbon-hosts.yml
- group: other
  href: https://artifacts.apis.io/brother-s-bond-bourbon/vendors/brother-s-bond-bourbon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brother-s-bond-bourbon-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://brothersbondbourbon.com/pages/press
- group: auth
  href: https://artifacts.apis.io/brother-s-bond-bourbon/security/brother-s-bond-bourbon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brother-s-bond-bourbon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brothersbondbourbon.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brothersbondbourbon.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brothersbondbourbon.com/policies/terms-of-service
- group: start
  title: ''
  type: SignUp
  url: https://brothersbondbourbon.com/account
- group: operate
  title: ''
  type: Support
  url: https://brothersbondbourbon.com/pages/find-us
- group: start
  title: ''
  type: DeveloperPortal
  url: https://store.brothersbondbourbon.com
coverage:
  checked: '2026-10-06'
  detail: Main site renders via JavaScript and the API is a Shopify storefront with no public developer docs.
  evidence:
  - status: 200
    url: https://brothersbondbourbon.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-06'
description: Brother's Bond Bourbon is a craft bourbon brand founded by actors Ian Somerhalder and Paul Wesley. The company produces award‑winning straight bourbon, blended rye, and limited‑edition releases, emphasizing sustainability and innovative grain blends. Their website showcases the story, method, product lineup, and press coverage, positioning the brand within the premium spirits market.
image: http://brothersbondbourbon.com/cdn/shop/files/bbb-website-social-share-01.jpg?v=1727736451&width=2048
layout: provider
modified: '2026-10-06'
name: Brother's Bond Bourbon
nav: Providers
network: true
overview: 'Brother''s Bond Bourbon is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Spirits, CraftBourbon, Sustainability, and Premium.


  Brother''s Bond Bourbon''s developer surface includes signup flow, support, and 10 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 15.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 58.9
    operational_transparency: 0.0
  previous_composite: 15.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brother S Bond Bourbon Domain Security
  slug: brother-s-bond-bourbon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brother-s-bond-bourbon
tags:
- Company
- Spirits
- CraftBourbon
- Sustainability
- Premium
website: https://brothersbondbourbon.com
---
