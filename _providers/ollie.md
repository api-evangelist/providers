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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ollie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ollie.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.ollie.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.ollie.com/onboarding/
- group: operate
  title: ''
  type: Support
  url: https://www.ollie.com/faqs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ollie.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ollie.com/privacy-policy/
created: '2026-07-17'
description: Ollie (ollie.com, formerly myollie.com) is a direct-to-consumer pet health company that makes fresh, human-grade dog food tailored to each dog. Customers build a personalized meal plan from their dog's profile (breed, age, weight, activity, allergies), and Ollie delivers pre-portioned, chef-and-vet-developed recipes on a recurring subscription, along with app-based health tracking and check-ins. The company reports having served more than one million dogs. Ollie is a venture-backed consumer brand and a portfolio company of Canaan Partners; it operates as a subscription e-commerce and mobile-app business and does not publish a public developer platform, API, or developer documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ollie.png
layout: provider
modified: '2026-07-20'
name: Ollie
nav: Providers
network: true
overview: 'Ollie is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pets, Pet Food, Dog Food, and Direct to Consumer.


  Ollie''s developer surface includes engineering blog, signup flow, support, and 4 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ollie/refs/heads/main/screenshots/ollie-2026-08-07T190123.png
security:
- kind: domain-security
  name: Ollie Domain Security
  slug: ollie-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ollie
tags:
- Company
- Pets
- Pet Food
- Dog Food
- Direct to Consumer
- Subscription
- E-Commerce
- Consumer Health
website: https://www.ollie.com/
---
