---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Reverb Agentic Access
  operation_count: 49
  slug: reverb-agentic-access
  summary_line: 49 operations · 4 acting
api_count: 21
apis:
- description: HATEOAS hypermedia REST API at https://reverb.com/api using application/hal+json. Auth via POST /api/auth/tokens to obtain a token used in X-Auth-Token header. Endpoints exposed via _links include acc
  name: Reverb REST API
  slug: rest-api
- description: The Accounts API from Reverb — 1 operation(s) for accounts.
  name: Reverb Accounts API
  slug: reverb-accounts-api
- description: The Articles API from Reverb — 2 operation(s) for articles.
  name: Reverb Articles API
  slug: reverb-articles-api
- description: The Auth API from Reverb — 4 operation(s) for auth.
  name: Reverb Auth API
  slug: reverb-auth-api
- description: The Autocomplete API from Reverb — 1 operation(s) for autocomplete.
  name: Reverb Autocomplete API
  slug: reverb-autocomplete-api
- description: The Autosuggest API from Reverb — 1 operation(s) for autosuggest.
  name: Reverb Autosuggest API
  slug: reverb-autosuggest-api
- description: The Braintree API from Reverb — 1 operation(s) for braintree.
  name: Reverb Braintree API
  slug: reverb-braintree-api
- description: The Cart API from Reverb — 1 operation(s) for cart.
  name: Reverb Cart API
  slug: reverb-cart-api
- description: The Categories API from Reverb — 2 operation(s) for categories.
  name: Reverb Categories API
  slug: reverb-categories-api
- description: The Collections API from Reverb — 1 operation(s) for collections.
  name: Reverb Collections API
  slug: reverb-collections-api
- description: The Countries API from Reverb — 1 operation(s) for countries.
  name: Reverb Countries API
  slug: reverb-countries-api
- description: The Currencies API from Reverb — 2 operation(s) for currencies.
  name: Reverb Currencies API
  slug: reverb-currencies-api
- description: The Listings API from Reverb — 1 operation(s) for listings.
  name: Reverb Listings API
  slug: reverb-listings-api
- description: The My API from Reverb — 21 operation(s) for my.
  name: Reverb My API
  slug: reverb-my-api
- description: The Payment Methods API from Reverb — 1 operation(s) for payment methods.
  name: Reverb Payment Methods API
  slug: reverb-payment-methods-api
- description: The Priceguide API from Reverb — 1 operation(s) for priceguide.
  name: Reverb Priceguide API
  slug: reverb-priceguide-api
- description: The Push Notifications API from Reverb — 1 operation(s) for push notifications.
  name: Reverb Push Notifications API
  slug: reverb-push-notifications-api
- description: The Reverb API API from Reverb — 1 operation(s) for reverb api.
  name: Reverb Reverb API API
  slug: reverb-reverb-api-api
- description: The Shipping API from Reverb — 2 operation(s) for shipping.
  name: Reverb Shipping API
  slug: reverb-shipping-api
- description: The Shop API from Reverb — 3 operation(s) for shop.
  name: Reverb Shop API
  slug: reverb-shop-api
- description: The Wants API from Reverb — 1 operation(s) for wants.
  name: Reverb Wants API
  slug: reverb-wants-api
artifact_total: 50
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Reverb Accounts API
  slug: open-reverb-accounts-api
- collection_type: open
  name: Reverb Accounts Articles API
  slug: open-reverb-articles-api
- collection_type: open
  name: Reverb Accounts Auth API
  slug: open-reverb-auth-api
- collection_type: open
  name: Reverb Accounts Autocomplete API
  slug: open-reverb-autocomplete-api
- collection_type: open
  name: Reverb Accounts Autosuggest API
  slug: open-reverb-autosuggest-api
- collection_type: open
  name: Reverb Accounts Braintree API
  slug: open-reverb-braintree-api
- collection_type: open
  name: Reverb Accounts Cart API
  slug: open-reverb-cart-api
- collection_type: open
  name: Reverb Accounts Categories API
  slug: open-reverb-categories-api
- collection_type: open
  name: Reverb Accounts Collections API
  slug: open-reverb-collections-api
- collection_type: open
  name: Reverb Accounts Countries API
  slug: open-reverb-countries-api
- collection_type: open
  name: Reverb Accounts Currencies API
  slug: open-reverb-currencies-api
- collection_type: open
  name: Reverb Accounts Listings API
  slug: open-reverb-listings-api
- collection_type: open
  name: Reverb Accounts My API
  slug: open-reverb-my-api
- collection_type: open
  name: Reverb Accounts Payment Methods API
  slug: open-reverb-payment-methods-api
- collection_type: open
  name: Reverb Accounts Priceguide API
  slug: open-reverb-priceguide-api
- collection_type: open
  name: Reverb Accounts Push Notifications API
  slug: open-reverb-push-notifications-api
- collection_type: open
  name: Reverb Accounts Reverb API API
  slug: open-reverb-reverb-api-api
- collection_type: open
  name: Reverb Accounts Shipping API
  slug: open-reverb-shipping-api
- collection_type: open
  name: Reverb Accounts Shop API
  slug: open-reverb-shop-api
- collection_type: open
  name: Reverb Accounts Wants API
  slug: open-reverb-wants-api
- collection_type: open
  name: Reverb API
  slug: open-reverb
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/reverb-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/reverb-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reverb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reverb-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reverbdotcom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/reverbdotcom
- group: company
  title: ''
  type: Website
  url: https://reverb.com/
- group: other
  title: ''
  type: Developer
  url: https://reverb.com/page/api
- group: commercial
  title: ''
  type: Plans
  url: plans/reverb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/reverb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/reverb-finops.yml
created: '2026-05-08'
description: Reverb is a marketplace for musicians to buy and sell new, used, and vintage musical instruments and gear, owned by Etsy. The Reverb API is a HATEOAS hypermedia REST API using application/hal+json, with interactive Swagger documentation and an X-Auth-Token header authentication scheme.
finops:
- name: Reverb Finops
  service_category: Marketplace
  slug: reverb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reverb.png
layout: provider
modified: '2026-05-08'
name: Reverb
nav: Providers
network: true
overview: 'Reverb publishes 21 APIs on the [APIs.io](https://apis.io/) network, including REST API, Accounts API, Articles API, and 18 more. Tagged areas include Marketplace, Music, Instruments, and Ecommerce.


  Reverb''s developer surface includes authentication and 10 more developer resources.'
plans:
- name: Reverb Plans Pricing
  plan_count: 2
  slug: reverb-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Reverb Rate Limits
  slug: reverb-rate-limits
score:
  band: emerging
  composite: 25.5
  delta: -1.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 52.0
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 26.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Reverb Authentication
  slug: reverb-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Reverb Domain Security
  slug: reverb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Reverb Vulnerability Disclosure
  slug: reverb-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: reverb
tags:
- Marketplace
- Music
- Instruments
- Ecommerce
website: https://reverb.com/
---
