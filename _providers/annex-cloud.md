---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 12
apis:
- description: 'Create, enroll, retrieve, update, delete, search, and merge loyalty members, and read a member''s activity and activity summary. Documented operations include POST /users, GET/PATCH /users/{memberId}, '
  name: Annex Cloud Members API
  slug: annex-cloud-members-api
- description: 'Record purchase and non-purchase transactions that issue loyalty points, and manage their lifecycle. Documented operations include POST /issuance (create, including non-purchase), PUT/PATCH /issuance '
  name: Annex Cloud Issuance and Transactions API
  slug: annex-cloud-issuance-transactions-api
- description: Give, redeem, and award loyalty points to members, including across multiple point buckets (Multi-Point Bucket V3). The documented operation is POST /points to add, redeem, or award points for a membe
  name: Annex Cloud Multi-Point Bucket Points API
  slug: annex-cloud-points-api
- description: Track and read the loyalty actions and activities performed against a site. The documented operation is GET /actions/{status} (with status set to "all" to retrieve every activity), complementing per-m
  name: Annex Cloud Activity and Actions API
  slug: annex-cloud-activity-actions-api
- description: Manage the products participating in a loyalty program and their point calculation. Documented operations include POST /products, POST /bulkproducts, GET /products/{prod_id}, PATCH /products/{prod_id}
  name: Annex Cloud Products API
  slug: annex-cloud-products-api
- description: Submit cart and order data and upload purchase receipts to drive loyalty accrual. Documented operations include POST /cart and receipt intake such as upload-by-URL. Endpoint paths are documented on th
  name: Annex Cloud Orders and Receipts API
  slug: annex-cloud-orders-receipts-api
- description: Power Refer A Friend (referral) programs - generate and track referral invitations across email, SMS, social, and unique links, and reward advocates and referred friends. Exposed as the Refer A Friend
  name: Annex Cloud Refer A Friend API
  slug: annex-cloud-refer-a-friend-api
- description: 'Manage internal users and issue the JWT tokens used to authenticate calls to the rest of the Loyalty Experience Platform. The documentation states you can create, update, and fetch an internal user''s '
  name: Annex Cloud Tenant and Authentication API
  slug: annex-cloud-tenant-auth-api
- description: Registration as a Service - hosted member registration and account creation flows that plug into the loyalty program. Listed as a distinct module on the Annex Cloud developer portal; detailed endpoint
  name: Annex Cloud Registration as a Service API
  slug: annex-cloud-registration-as-a-service-api
- description: Incentive Engine Management - configure the rules, promotions, and reward logic that govern how members earn and redeem across the loyalty program. Listed as a distinct module on the developer portal;
  name: Annex Cloud Incentive Engine Management API
  slug: annex-cloud-incentive-engine-api
- description: Privacy Policy Management - manage member consent and privacy-related requests such as transaction erasure (right-to-be-forgotten), complementing the transactionErasure operations documented on the Me
  name: Annex Cloud Privacy Policy Management API
  slug: annex-cloud-privacy-policy-management-api
- description: Webhooks and Webhook Events - subscribe to loyalty events so external systems receive HTTP POST callbacks when members, points, transactions, or referrals change. Server-to-endpoint HTTP callbacks, no
  name: Annex Cloud Webhooks API
  slug: annex-cloud-webhooks-api
artifact_total: 16
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/annex-cloud-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/annex-cloud
- group: company
  title: ''
  type: Website
  url: https://www.annexcloud.com
- group: docs
  title: ''
  type: Documentation
  url: https://annexcloud.redocly.app/introduction-1
- group: start
  title: ''
  type: SignUp
  url: https://www.annexcloud.com/api-documentation/
- group: commercial
  title: ''
  type: Plans
  url: plans/annex-cloud-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/annex-cloud-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/annex-cloud-finops.yml
created: '2026-07-10'
description: Annex Cloud is an enterprise loyalty and customer retention platform. Its Loyalty Experience Platform is built on a set of RESTful APIs that let brands enroll and manage loyalty members, issue and redeem points, track member activity and transactions, run referral (Refer A Friend) programs, and wire loyalty into commerce and marketing stacks. The APIs are documented publicly on a Redocly developer portal, but access is gated - credentials are provisioned per customer and the base host is tenant-specific. Authentication is JWT-based, created through the Tenant API, and prospective users are directed to "Contact your Customer Success Manager for assistance with API Connectors." No public self-serve signup, sandbox, or published pricing is offered; this is an enterprise, partner/customer-gated API.
finops:
- name: Annex Cloud Finops
  service_category: Loyalty and Customer Retention
  slug: annex-cloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/annex-cloud.png
layout: provider
modified: '2026-07-10'
name: Annex Cloud
nav: Providers
network: true
overview: 'Annex Cloud publishes 12 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Loyalty, Customer Retention, Rewards, Points, and Referrals.


  Annex Cloud''s developer surface includes documentation, signup flow, and 6 more developer resources.'
plans:
- name: Annex Cloud Plans Pricing
  plan_count: 1
  slug: annex-cloud-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 2
  name: Annex Cloud Rate Limits
  slug: annex-cloud-rate-limits
score:
  band: emerging
  composite: 19.4
  delta: -2.3
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 21.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/annex-cloud/refs/heads/main/screenshots/annex-cloud-2026-07-25T200301.png
security:
- kind: domain-security
  name: Annex Cloud Domain Security
  slug: annex-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: annex-cloud
tags:
- Loyalty
- Customer Retention
- Rewards
- Points
- Referrals
- Customer Engagement
- Enterprise
- Gated Access
website: https://www.annexcloud.com
---
