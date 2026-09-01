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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nutrisystem-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nutrisystem.com
- group: other
  title: Wellina by Nutrisystem — the all-in-one nutrition marketplace umbrella
  type: Marketplace
  url: https://www.nutrisystem.com
- group: other
  title: ''
  type: Brands
  url: https://www.nutrisystem.com/products/brands
- group: other
  title: South Beach Diet (acquired by Nutrisystem December 2015, $15M; site now redirects to nutrisystem.com/products/brands)
  type: SisterBrand
  url: https://www.southbeachdiet.com
- group: other
  title: Jenny Craig (IP acquired by Wellful Inc. fall 2023 post-bankruptcy; relaunched as e-commerce meal delivery; copyright JCR Holdings II, LLC)
  type: SisterBrand
  url: https://www.jennycraig.com
- group: other
  title: Wellful, Inc. — parent of Nutrisystem, LLC; created after Kainos Capital acquired Nutrisystem from Tivity Health in October 2020
  type: ParentCompany
  url: https://en.wikipedia.org/wiki/Nutrisystem
- group: operate
  title: ''
  type: FAQ
  url: https://leaf.nutrisystem.com/faqs/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.nutrisystem.com/jsps_hmr/contact_us/contact_us.jsp
- group: other
  title: Nutrisystem app — iOS (food logging, weight tracking, journal, meal plan)
  type: MobileApp
  url: https://apps.apple.com/us/app/nutrisystem/id436875233
- group: other
  title: Nutrisystem app — Android
  type: MobileApp
  url: https://play.google.com/store/apps/details?id=com.nutrisystem
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nutrisystem
- group: company
  title: 501–1,000 employees; Wellness and Fitness Services; Fort Washington, PA
  type: LinkedIn
  url: https://www.linkedin.com/company/nutrisystem
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Nutrisystem
- group: start
  title: ''
  type: Login
  url: https://www.nutrisystem.com/login
created: '2026-05-23'
description: Nutrisystem is a direct-to-consumer subscription meal delivery service for weight loss, founded in 1972 by Harold Katz and headquartered in Fort Washington, Pennsylvania. The company pioneered prepackaged weight-loss meal subscriptions, transitioned from physical retail to a direct-to-consumer Internet and telephone model in 1999, and added mobile delivery beginning in 2010. Nutrisystem is now operated under the marketing umbrella "Wellina by Nutrisystem" — a multi-brand health and wellness marketplace covering Nutrisystem, Jenny Craig, High Protein, Menopause Support, Low Carb (GLP-1 friendly), and the Club Advantage à la carte membership. The legal operating entity is Nutrisystem, LLC, a subsidiary of Wellful, Inc. (the parent organization formed after Kainos Capital acquired Nutrisystem from Tivity Health in October 2020). Tivity Health no longer owns the brand. Wellful's portfolio also includes South Beach Diet (acquired by Nutrisystem in December 2015 for $15 million) and
  the Jenny Craig intellectual property (acquired by Wellful in fall 2023 after Jenny Craig's Chapter 7 bankruptcy and relaunched as an e-commerce meal-delivery brand). LinkedIn classifies the company under Wellness and Fitness Services with 501–1,000 employees. Stephen Mikulak was named President in 2021. Nutrisystem publishes no public developer APIs, OpenAPI specs, SDKs, or developer portal. Its only digital surface beyond the e-commerce sites is the consumer-facing Nutrisystem mobile app (iOS / Android) for food logging, weight tracking, journaling, and meal-plan adjustments — and the equivalent Jenny Craig app — neither of which advertise integrations with Apple Health, Google Fit, Fitbit, or any third-party platform. The github.com/nutrisystem GitHub organization exists but contains a single inactive CSS repository last updated in March 2015. The technology footprint is a closed consumer subscription stack with no public developer touchpoints.
features:
- finding: Public developer portal
  status: None — no developer.nutrisystem.com or equivalent
- finding: Public OpenAPI / AsyncAPI specs
  status: None published
- finding: Public REST or GraphQL APIs
  status: None — e-commerce, account, and app endpoints are private/internal
- finding: SDKs / CLI
  status: None published
- finding: Mobile-app third-party integrations
  status: None advertised — no Apple Health, Google Fit, Fitbit, MyFitnessPal connectivity in FAQ or app documentation
- finding: GitHub organization
  status: github.com/nutrisystem exists with 1 stale public repo ("CSS", last updated March 12, 2015)
- finding: Status page / changelog / release notes
  status: None public
- finding: Sandbox / Console
  status: None
- finding: Public RSS / blog feed
  status: No prominent developer or product-engineering blog
- finding: Webhooks
  status: None documented
- finding: Tier rationale
  status: Tier 3 — no-apis. Pure consumer subscription business; the only programmatic surface (the mobile apps) is closed and serves a single first-party use case. Technology footprint is entirely internal e-commerce / fulfillment / app stack with no public developer touchpoints.
graphqls:
- description: ''
  name: Nutrisystem (Wellina by Nutrisystem) GraphQL API
  slug: nutrisystem-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nutrisystem.png
jsonld:
- class_count: 35
  name: Nutrisystem Context
  property_count: 0
  slug: nutrisystem-context
layout: provider
modified: '2026-05-23'
name: Nutrisystem (Wellina by Nutrisystem)
nav: Providers
network: true
overview: 'Nutrisystem (Wellina by Nutrisystem) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Consumer Subscription, Diet, Direct to Consumer, E-Commerce, and Health and Wellness.


  The Nutrisystem (Wellina by Nutrisystem) catalog on APIs.io includes 1 JSON-LD context.


  Nutrisystem (Wellina by Nutrisystem)''s developer surface includes FAQ and 14 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 5
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 8.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nutrisystem/refs/heads/main/screenshots/nutrisystem-2026-06-20T190532.png
security:
- kind: domain-security
  name: Nutrisystem Domain Security
  slug: nutrisystem-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nutrisystem
tags:
- Consumer Subscription
- Diet
- Direct to Consumer
- E-Commerce
- Health and Wellness
- Meal Delivery
- Mobile App
- Nutrition
- Subscription Commerce
- Weight Loss
website: https://www.nutrisystem.com
---
