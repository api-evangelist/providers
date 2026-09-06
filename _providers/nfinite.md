---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Undocumented internal oEmbed endpoint backing the Nfinite applications. Returns embeddable representations of product visuals. Requires an opaque `token` query parameter plus a resource `url`; there i
  name: Nfinite oEmbed
  slug: nfinite-oembed
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nfinite-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nfinite.app/
- group: company
  title: ''
  type: Blog
  url: https://www.nfinite.app/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nfinite.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nfinite.app/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://my.nfinite.app/
created: '2026-07-17'
description: Nfinite (formerly Hubstairs) is a visual intelligence platform for the digital shelf. It helps consumer brands and retailers automatically analyze, generate, and monitor compliant product visuals — detecting visual compliance gaps across every retailer and brand and fixing them at scale using AI-generated 3D and synthetic product imagery. The product is delivered as a web application (my.nfinite.app) rather than a public developer API; no OpenAPI, developer portal, or published documentation exists at the time of enrichment. Backed by Insight Partners.
image: https://cdn.prod.website-files.com/63ebb9bcdb3fa05b439326d3/6a3a44ec48916bf40cbc2d69_Website%20Banner.png
layout: provider
modified: '2026-07-20'
name: Nfinite
nav: Providers
network: true
overview: 'Nfinite publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Visual Intelligence, Digital Shelf, Product Imagery, and Retail.


  Nfinite''s developer surface includes engineering blog, signup flow, and 4 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nfinite/refs/heads/main/screenshots/nfinite-2026-08-07T185225.png
security:
- kind: authentication
  name: Nfinite Authentication
  slug: nfinite-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nfinite Domain Security
  slug: nfinite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nfinite
tags:
- Company
- Visual Intelligence
- Digital Shelf
- Product Imagery
- Retail
- E-Commerce
- Artificial Intelligence
- Content Generation
website: https://www.nfinite.app/
---
