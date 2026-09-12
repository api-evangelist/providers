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
    well_known_catalog: true
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/essendant-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/essendant
- group: company
  title: ''
  type: Website
  url: https://www.essendant.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/essendant-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/essendant-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/essendant-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/essendant-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/essendant-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/essendant-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/essendant-rate-limits.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.essendant.com/privacy-notice/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.essendant.com/essendant-terms-of-sale/
- group: operate
  title: ''
  type: Support
  url: https://www.essendant.com/faqs/
- group: start
  title: ''
  type: Login
  url: https://www.essendant.com/for-existing-customers/
- group: company
  title: ''
  type: Blog
  url: https://www.essendant.com/resources/
created: '2026-05-01'
description: 'Essendant is a national wholesale distributor and third-party logistics provider of workplace products — business and office supplies, furniture, janitorial and breakroom (JanSan), foodservice, industrial and automotive aftermarket items — operating a network of 35+ distribution centers carrying 49,000+ SKUs. Built on the United Stationers, Lagasse Sweet and Azerty brands and owned by Staples since 2019, it sells through independent resellers rather than direct to end users, and its Connected Commerce and Fulfillment Services arms add marketplace access, retail drop-ship, B2C fulfillment and Amazon SFP/FBA prep. Its integration surface is trading-partner EDI and the ECDB product-content feed rather than a public API: no developer portal, OpenAPI, MCP server or agent card is published on any Essendant host.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/essendant.png
layout: provider
modified: '2026-09-07'
name: Essendant
nav: Providers
network: true
overview: 'Essendant is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Wholesale, Distribution, Supply Chain, Office Supplies, and Fulfillment.


  Essendant''s developer surface includes authentication, support, engineering blog, and 12 more developer resources.'
plans:
- name: Essendant Plans Pricing
  plan_count: 0
  slug: essendant-plans-pricing
press:
- date: '2026-05-25'
  title: Essendant Announces Strategic Partnership with Roadie to ...
  url: https://www.prnewswire.com/news-releases/essendant-announces-strategic-partnership-with-roadie-to-enhance-supply-chain-efficiency-and-last-mile-delivery-solutions-302479896.html
- date: '2026-05-25'
  title: Essendant Optimizes Its Supply Chain to Create a More ...
  url: https://www.dcvelocity.com/articles/58077-essendant-optimizes-its-supply-chain-to-create-a-more-streamlined-furniture-fulfillment-program
- date: '2026-05-25'
  title: Essendant Partners with Hub Group to Launch Managed ...
  url: https://www.prnewswire.com/news-releases/essendant-partners-with-hub-group-to-launch-managed-delivery-model-delivering-to-warehouses-within-48-hours-302593582.html
- date: '2026-05-25'
  title: 'Pricing Under Pressure: How SP Richards Stays Profitable ...'
  url: https://pros.com/b2b/learn/case-studies-testimonials/pricing-under-pressure-sp-richards-stays-profitable/
- date: '2026-05-25'
  title: Essendant invests in marketing innovations to help dealers ...
  url: https://www.essendant.com/wp-content/uploads/2024/03/Independent-Dealer-2024-Essendant-Marketing-new.pdf
random_paper: 20
rate_limits:
- limit_count: 0
  name: Essendant Rate Limits
  slug: essendant-rate-limits
scopes:
- name: Essendant Scopes
  scope_count: 9
  slug: essendant-scopes
  summary_line: 9 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    operational_transparency: 0.0
  previous_composite: 17.2
  provenance:
    conformance: first-party
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/essendant/refs/heads/main/screenshots/essendant-2026-06-20T180823.png
security:
- kind: authentication
  name: Essendant Authentication
  slug: essendant-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Essendant Domain Security
  slug: essendant-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: essendant
tags:
- Wholesale
- Distribution
- Supply Chain
- Office Supplies
- Fulfillment
- 3PL
- B2B
- EDI
- Ecommerce
- JanSan
- Foodservice
website: https://www.essendant.com
---
