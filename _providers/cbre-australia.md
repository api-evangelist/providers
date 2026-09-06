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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cbre-australia-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cbre-australia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.cbre.com/about-us/corporate-responsibility/vulnerability-disclosure
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cbre-australia-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.cbre.com.au/
- group: company
  title: ''
  type: About
  url: https://www.cbre.com.au/about-us
- group: other
  title: ''
  type: Services
  url: https://www.cbre.com.au/services
- group: other
  title: ''
  type: PropertySearch
  url: https://www.cbre.com.au/properties
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cbre.com/about-us/disclaimer-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cbre.com.au/about-us/pacific-privacy-notice
- group: commercial
  title: ''
  type: Privacy
  url: https://www.cbre.com.au/about-us/protecting-your-data-at-cbre
- group: other
  title: ''
  type: ResponsibleAI
  url: https://www.cbre.com.au/about-us/responsible-ai-at-cbre
- group: company
  title: ''
  type: Newsroom
  url: https://www.cbre.com.au/about-us/newsroom
- group: company
  title: ''
  type: Blog
  url: https://www.cbre.com.au/insights
- group: other
  title: ''
  type: Research
  url: https://www.cbre.com.au/insights
- group: operate
  title: ''
  type: Support
  url: https://www.cbre.com.au/about-us/culture-and-history/contact-us
- group: company
  title: ''
  type: Careers
  url: https://www.cbre.com.au/careers
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.cbre.com/investor-relations-home/default.aspx
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cbre-asia-pacific
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/cbre
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/cbre
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CBRE
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-07-26'
description: 'CBRE Australia is the Australian arm of CBRE Group, the global commercial real estate services and investment firm, trading locally as CBRE (Gwsla) Pty Ltd (AU09949) and operating across the Pacific from cbre.com.au. It sits on the advisory and management side of the Australian property value chain rather than the data-infrastructure side: capital markets and investment sales, leasing and occupier advisory, valuation and advisory services, property and asset management, and project and design-and-build delivery across office, retail, industrial and logistics, build-to-rent, and alternative asset classes. Its API posture is closed. As of 26 July 2026 no public developer portal, API documentation, machine-readable contract, or self-serve onboarding exists for CBRE Australia: developer.cbre.com.au, developers.cbre.com.au, api.cbre.com.au, and docs.cbre.com.au do not resolve, and the global developer.cbre.com host is NXDOMAIN as well. CBRE does run API infrastructure — api.cbre.com
  sits behind an Imperva WAF that returns 403 to every anonymous request, api-dev.cbre.com serves a default WSO2 API Manager landing page, and eipportal.cbre.com is a login-gated "Integration Platform" SPA — but none of it is published, catalogued, or reachable by an outside developer. Commercial listings are distributed through the cbre.com.au property search and Australia''s portal duopoly, and CBRE''s terms of use explicitly prohibit scraping property listings from the site. RESO is absent entirely, which is the honest answer for Australia: there is no MLS here, no RESO-certified Australian organization, and the country''s mandated machine-readable property rail is PEXA''s electronic conveyancing network, not a RESO Web API. Access to CBRE data in Australia is a client or partner relationship, not a developer signup.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cbre.png
layout: provider
modified: '2026-07-26'
name: CBRE Australia
nav: Providers
network: true
overview: 'CBRE Australia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real-Estate, Australia, Commercial Real Estate, Property Listings, and Valuation.


  CBRE Australia''s developer surface includes privacy policy, engineering blog, support, and 20 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 13.1
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
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 13.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cbre-australia/refs/heads/main/screenshots/cbre-australia-2026-07-27T125331.png
security:
- kind: domain-security
  name: Cbre Australia Domain Security
  slug: cbre-australia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cbre Australia Vulnerability Disclosure
  slug: cbre-australia-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: cbre-australia
tags:
- Real-Estate
- Australia
- Commercial Real Estate
- Property Listings
- Valuation
- Property Management
- Capital Markets
- PropTech
- Leasing
website: https://www.cbre.com.au/
---
