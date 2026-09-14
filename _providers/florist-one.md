---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Florist One Agentic Access
  operation_count: 12
  slug: florist-one-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 1
apis:
- description: Florist One provides a free REST API for searching available flower products, retrieving product details and imagery, placing orders for delivery through the Florist One network, and checking order st
  name: Florist One API
  slug: florist-one-api
- baseURL: https://www.floristone.com/api/rest
  baseurl_source: declared
  description: The Affiliate API from Florist One — 1 operation(s) for affiliate.
  name: Florist One Affiliate API
  slug: florist-one-affiliate-api
- baseURL: https://www.floristone.com/api/rest
  baseurl_source: declared
  description: The FlowerShop API from Florist One — 5 operation(s) for flowershop.
  name: Florist One FlowerShop API
  slug: florist-one-flowershop-api
- baseURL: https://www.floristone.com/api/rest
  baseurl_source: declared
  description: The GiftBaskets API from Florist One — 3 operation(s) for giftbaskets.
  name: Florist One GiftBaskets API
  slug: florist-one-giftbaskets-api
- baseURL: https://www.floristone.com/api/rest
  baseurl_source: declared
  description: The ShoppingCart API from Florist One — 1 operation(s) for shoppingcart.
  name: Florist One ShoppingCart API
  slug: florist-one-shoppingcart-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Florist One REST Affiliate API
  slug: open-florist-one-affiliate-api
- collection_type: open
  name: Florist One REST Affiliate FlowerShop API
  slug: open-florist-one-flowershop-api
- collection_type: open
  name: Florist One REST Affiliate GiftBaskets API
  slug: open-florist-one-giftbaskets-api
- collection_type: open
  name: Florist One REST Affiliate ShoppingCart API
  slug: open-florist-one-shoppingcart-api
- collection_type: open
  name: Florist One REST API
  slug: open-florist-one
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/florist-one-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/florist-one-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/florist-one-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FloristOne
- group: company
  title: ''
  type: Website
  url: https://www.floristone.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.floristone.com/api/
- group: other
  title: ''
  type: TechnicalInformation
  url: https://www.floristone.com/api/technical-information/
- group: operate
  title: ''
  type: FAQ
  url: https://www.floristone.com/api/flowers-api-faq/
- group: operate
  title: ''
  type: Contact
  url: https://www.floristone.com/api/api-contact/
- group: build
  title: ''
  type: Packages
  url: packages/florist-one-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/florist-one-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/florist-one-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/florist-one-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/florist-one-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/florist-one-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.floristone.com/api/print_api_legal/
- group: design
  title: ''
  type: Conventions
  url: conventions/florist-one-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/florist-one-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/florist-one-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/florist-one-rate-limits.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.floristone.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.floristone.com/api/how-it-works/
- group: operate
  title: ''
  type: Support
  url: https://www.floristone.com/api/api-contact/
- group: start
  title: ''
  type: SignUp
  url: https://www.floristone.com/api/api-signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.floristone.com/api/print_api_legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.floristone.com/privacy/
created: '2025-02-24'
description: Florist One is an online flower delivery service that specializes in creating and delivering floral arrangements through a network of local florists across the United States and Canada. Florist One offers a free REST web service that lets developers integrate flower products, ordering, and delivery into their own applications. The API is documented for use from any common web language including Java, PHP, ASP.NET, JavaScript, Node, Python, Perl, Ruby, and ColdFusion.
finops:
- name: Florist One Finops
  service_category: API
  slug: florist-one-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/florist-one.png
layout: provider
modified: '2026-09-10'
name: Florist One
nav: Providers
network: true
overview: 'Florist One publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Affiliate API, FlowerShop API, GiftBaskets API, and 1 more. Tagged areas include Delivery, E-Commerce, Florists, Flowers, and Gifts.


  Florist One''s developer surface includes authentication, documentation, FAQ, getting-started guide, support, signup flow, and 21 more developer resources.'
plans:
- name: Florist One Plans Pricing
  plan_count: 1
  slug: florist-one-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Florist One Rate Limits
  slug: florist-one-rate-limits
security:
- kind: authentication
  name: Florist One Authentication
  slug: florist-one-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Florist One Domain Security
  slug: florist-one-domain-security
  summary_line: TLSv1.3 · DMARC
slug: florist-one
tags:
- Delivery
- E-Commerce
- Florists
- Flowers
- Gifts
website: https://www.floristone.com/
---
