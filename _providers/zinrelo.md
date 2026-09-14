---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - '{''url'': ''https://www.zinrelo.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.trueloyal.com/ — a different registrable domain (zinrelo.com -> trueloyal.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: true
  try_now: true
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Zinrelo Agentic Access
  operation_count: 22
  slug: zinrelo-agentic-access
  summary_line: 22 operations · 9 acting
api_count: 1
apis:
- baseURL: https://api.zinrelo.com
  baseurl_source: declared
  description: Retrieve webhook event details by event ID.
  name: Zinrelo Events API
  slug: zinrelo-events-api
- baseURL: https://api.zinrelo.com
  baseurl_source: declared
  description: Enroll, retrieve, update, block, and manage loyalty program members.
  name: Zinrelo Members API
  slug: zinrelo-members-api
- baseURL: https://api.zinrelo.com
  baseurl_source: declared
  description: Award, deduct, and manage member point balances.
  name: Zinrelo Points API
  slug: zinrelo-points-api
- baseURL: https://api.zinrelo.com
  baseurl_source: declared
  description: Redeem points for rewards and list a member's redemptions.
  name: Zinrelo Redemptions API
  slug: zinrelo-redemptions-api
- baseURL: https://api.zinrelo.com
  baseurl_source: declared
  description: List and retrieve the rewards a program offers.
  name: Zinrelo Rewards API
  slug: zinrelo-rewards-api
- baseURL: https://api.zinrelo.com
  baseurl_source: declared
  description: Retrieve loyalty tier configuration and a member's next tier.
  name: Zinrelo Tiers API
  slug: zinrelo-tiers-api
- baseURL: https://api.zinrelo.com
  baseurl_source: declared
  description: Record purchases and returns and list loyalty transactions.
  name: Zinrelo Transactions API
  slug: zinrelo-transactions-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zinrelo Loyalty Events API
  slug: open-zinrelo-events-api
- collection_type: open
  name: Zinrelo Loyalty Events Members API
  slug: open-zinrelo-members-api
- collection_type: open
  name: Zinrelo Loyalty Events Points API
  slug: open-zinrelo-points-api
- collection_type: open
  name: Zinrelo Loyalty Events Redemptions API
  slug: open-zinrelo-redemptions-api
- collection_type: open
  name: Zinrelo Loyalty Events Rewards API
  slug: open-zinrelo-rewards-api
- collection_type: open
  name: Zinrelo Loyalty Events Tiers API
  slug: open-zinrelo-tiers-api
- collection_type: open
  name: Zinrelo Loyalty Events Transactions API
  slug: open-zinrelo-transactions-api
- collection_type: open
  name: Zinrelo Loyalty API
  slug: open-zinrelo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zinrelo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/zinrelo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zinrelo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zinrelo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zinrelo
- group: company
  title: ''
  type: Website
  url: https://www.zinrelo.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.zinrelo.com/reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://zinrelo.github.io/slate/
- group: commercial
  title: ''
  type: Plans
  url: plans/zinrelo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zinrelo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zinrelo-finops.yml
created: '2026-07-10'
description: Zinrelo is an enterprise SaaS loyalty and rewards platform that helps brands run holistic loyalty programs spanning transactional, social, advocacy, engagement, behavioral, and emotional loyalty across web, mobile, and in-store channels. Its documented REST Loyalty API lets you enroll and manage members, award and deduct points, record purchases and returns, list rewards, and redeem points for rewards. Every request is authenticated with a partner-id and an api-key sent as HTTP headers, both provisioned to a Zinrelo account. The API reference is public, but obtaining API credentials requires a Zinrelo account; pricing is quote-based via sales. Zinrelo is rebranding to TrueLoyal, and some documentation now lives under trueloyal.com domains.
finops:
- name: Zinrelo Finops
  service_category: Marketing and Loyalty
  slug: zinrelo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zinrelo.png
layout: provider
modified: '2026-07-10'
name: Zinrelo
nav: Providers
network: true
overview: 'Zinrelo publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Events API, Members API, Points API, and 4 more. Tagged areas include Loyalty, Rewards, Points, Customer Retention, and E-Commerce.


  Zinrelo''s developer surface includes authentication, documentation, API reference, and 8 more developer resources.'
plans:
- name: Zinrelo Plans Pricing
  plan_count: 3
  slug: zinrelo-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Zinrelo Rate Limits
  slug: zinrelo-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/zinrelo/refs/heads/main/screenshots/zinrelo-2026-09-02T171754.png
security:
- kind: authentication
  name: Zinrelo Authentication
  slug: zinrelo-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Zinrelo Domain Security
  slug: zinrelo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Zinrelo Trust Center
  slug: zinrelo-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: zinrelo
tags:
- Loyalty
- Rewards
- Points
- Customer Retention
- E-Commerce
- Software-as-a-Service
website: https://www.zinrelo.com
---
