---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.2
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Read-only OData v3 service that supplies product and brand data to Conagra's consumer brand websites. The service document at /odata advertises six entity sets; two of them resolve — Products (2,267 r
  name: Conagra Brand Sites API
  slug: conagra-brands-brand-sites-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/conagra-brands-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/conagra-brands-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/conagra-brands-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/conagra-brands-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/conagra-brands-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/conagra
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/conagra-brands
- group: company
  title: ''
  type: Website
  url: https://www.conagrabrands.com
- group: other
  title: ''
  type: x-Foodservice
  url: https://www.conagrafoodservice.com
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.conagrabrands.com/investor-relations
- group: company
  title: ''
  type: Newsroom
  url: https://www.conagrabrands.com/news-room
- group: other
  title: ''
  type: x-Suppliers
  url: https://www.conagrabrands.com/our-company/suppliers
- group: other
  title: ''
  type: x-ConagraRISE
  url: https://conagrarise.com
- group: operate
  title: ''
  type: Support
  url: https://www.conagrabrands.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.conagrabrands.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.conagrabrands.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://conagrabrands.com/rss.xml
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Conagra_Brands
created: '2026-03-21'
description: 'Conagra Brands is a leading North American branded consumer packaged goods (CPG) food company headquartered in Chicago, Illinois. Its portfolio of iconic frozen, refrigerated, and shelf-stable brands includes Marie Callender''s, Healthy Choice, Slim Jim, Reddi-wip, Hunt''s, Banquet, Birds Eye, Duncan Hines, and Orville Redenbacher''s. Conagra runs no developer program: there is no developer portal, no API documentation, no SDKs, no sign-up and no terms of use for API access, and both of its GitHub organizations are empty. It does, however, operate one public, undocumented API — the Brand Sites API at brands-api.conagrafoods.com, a read-only OData v3 service that backs its consumer brand websites and answers anonymous requests for 2,267 products and its brand codes. Partner integrations for foodservice, retail and supplier programs remain managed through direct B2B agreements rather than a public developer surface.'
examples:
- key_count: 2
  name: Conagra Brands Brands Response
  slug: conagra-brands-brands-response
- key_count: 2
  name: Conagra Brands Products Response
  slug: conagra-brands-products-response
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/conagra-brands.png
layout: provider
modified: '2026-09-05'
name: Conagra Brands
nav: Providers
network: true
overview: 'Conagra Brands publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Branded Foods, CPG, Consumer Packaged Goods, Food Service, and Fortune 500.


  Conagra Brands'' developer surface includes support, engineering blog, and 16 more developer resources.'
plans:
- name: Conagra Brands Plans Pricing
  plan_count: 0
  slug: conagra-brands-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Conagra Brands Rate Limits
  slug: conagra-brands-rate-limits
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 13.3
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 6.7
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 5.8
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
security:
- kind: authentication
  name: Conagra Brands Authentication
  slug: conagra-brands-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Conagra Brands Domain Security
  slug: conagra-brands-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: conagra-brands
tags:
- Branded Foods
- CPG
- Consumer Packaged Goods
- Food Service
- Fortune 500
- Frozen Foods
- Grocery
- OData
- Product Data
website: https://www.conagrabrands.com
---
