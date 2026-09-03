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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 13.3
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.andersonsinc.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/theandersonsinc
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/the-andersons-inc
- group: operate
  title: ''
  type: Support
  url: https://www.andersonsinc.com/contact/contact-information/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.andersonsinc.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.andersonsinc.com/privacy/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/andersons-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/andersons-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/andersons-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/andersons-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/andersons-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/andersons-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/andersons-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/andersons-llms.txt
coverage:
  checked: '2026-09-02'
  detail: The Andersons ships customer software — the GRAINweb grain portal, the Farm2Market SmartTicket web app and two mobile apps — but only as authenticated end-user products behind an ADFS single sign-on; there is no developer program, no API reference and no machine-readable contract on any of the seven hosts probed, and the corporate sitemap's 49 URLs contain no developer, API or pricing page at all.
  evidence:
  - status: 404
    url: https://www.andersonsinc.com/developers/
  - status: 404
    url: https://www.andersonsinc.com/openapi.json
  - status: 404
    url: https://www.andersonsinc.com/api-docs
  - status: 404
    url: https://www.andersonsgrain.com/swagger/v1/swagger.json
  - status: 404
    url: https://portal.andersonsinc.com/.well-known/agent-card.json
  - status: 200
    url: https://portalauth.andersonsinc.com/adfs/.well-known/openid-configuration
  reason: no-developer-program
  state: none
created: '2026-03-21'
description: 'The Andersons, Inc. (NASDAQ: ANDE) is a diversified North American agribusiness headquartered in Maumee, Ohio and founded in 1947, operating across four segments: Agribusiness / commodity merchandising through The Andersons Trade Group grain elevators and terminals, Nutrient & Industrial through The Andersons Plant Nutrient Group and its turf and specialty products, Renewables through its ethanol production and marketing joint ventures, and premium food and pet-food ingredients. The company publishes NO public developer API, no developer portal, no OpenAPI or other machine-readable contract, and no SDKs. Its customer-facing digital surface is a set of authenticated end-user applications — the GRAINweb grain account portal, the Farm2Market SmartTicket delivery-ticket web app at andersonstickets.com, the AndeConnect and Trade Group mobile apps (the AndeConnect app is operated on the company''s behalf by the ag platform vendor Bushel), and portal.andersonsinc.com account management
  — all federated through an Active Directory Federation Services identity provider at portalauth.andersonsinc.com. Business-to-business integration is handled through EDI and direct merchant relationships rather than a self-service API. NOTE ON IDENTITY: the domain andersons.com belongs to Anderson''s of White Bear Lake, Minnesota, an unrelated prom and school-spirit party-supply retailer; The Andersons, Inc. is at andersonsinc.com.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/andersons.png
layout: provider
modified: '2026-09-02'
name: The Andersons
nav: Providers
network: true
overview: 'The Andersons is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Agribusiness, Agriculture, Grain, Commodity Merchandising, and Plant Nutrients.


  The Andersons'' developer surface includes support, authentication, and 12 more developer resources.'
plans:
- name: Andersons Plans Pricing
  plan_count: 0
  slug: andersons-plans-pricing
press:
- date: '2026-05-25'
  title: The Andersons launches corporate VC arm, Maumee ...
  url: https://agfundernews.com/andersons-launches-corporate-vc-arm-maumee-ventures-invest-agtech
- date: '2026-05-25'
  title: The Andersons, Inc. - Terms of Use
  url: https://www.andersonsinc.com/terms-of-use/
- date: '2026-05-25'
  title: The Andersons reaffirms $7 EPS target by end of 2028 ...
  url: https://seekingalpha.com/news/4587102-the-andersons-reaffirms-7-eps-target-by-end-of-2028-while-guiding-to-225m-2026-capex
- date: '2026-05-25'
  title: The Andersons, Inc. Acquires Majority Ownership ...
  url: https://www.linkedin.com/posts/theandersonsinc_the-andersons-inc-acquires-majority-ownership-activity-7259199698412961792-ouL3
- date: '2026-05-25'
  title: The Andersons, Inc. Reports First Quarter Results
  url: https://www.prnewswire.com/news-releases/the-andersons-inc-reports-first-quarter-results-302762937.html
random_paper: 7
rate_limits:
- limit_count: 0
  name: Andersons Rate Limits
  slug: andersons-rate-limits
scopes:
- name: Andersons Scopes
  scope_count: 0
  slug: andersons-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.0
  coverage:
    artifact_dirs: 14
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 14.1
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 5.3
  previous_composite: 6.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/andersons/refs/heads/main/screenshots/andersons-2026-06-20T171949.png
security:
- kind: authentication
  name: Andersons Authentication
  slug: andersons-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Andersons Domain Security
  slug: andersons-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: andersons
tags:
- Agribusiness
- Agriculture
- Grain
- Commodity Merchandising
- Plant Nutrients
- Fertilizer
- Renewables
- Ethanol
- Food and Feed Ingredients
- Turf and Specialty Products
- Rail Leasing
- Supply Chain
website: https://www.andersonsinc.com/
---
