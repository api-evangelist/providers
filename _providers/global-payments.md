---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.8
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Global Payments Agentic Access
  operation_count: 6
  slug: global-payments-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 1
apis:
- description: The Global Payments Integrated API provides ISVs and software partners with payment integration capabilities including credit card processing, ACH payments, and reporting. The platform supports semi-i
  name: Global Payments Integrated API
  slug: integrated-api
- baseURL: https://apis.globalpay.com
  baseurl_source: declared
  description: Manage chargebacks and disputes.
  name: Global Payments Disputes API
  slug: global-payments-disputes-api
- baseURL: https://apis.globalpay.com
  baseurl_source: declared
  description: Manage stored payment methods and tokenization.
  name: Global Payments Payment Methods API
  slug: global-payments-payment-methods-api
- baseURL: https://apis.globalpay.com
  baseurl_source: declared
  description: Access settlement and funding information.
  name: Global Payments Settlements API
  slug: global-payments-settlements-api
- baseURL: https://apis.globalpay.com
  baseurl_source: declared
  description: Process and manage payment transactions.
  name: Global Payments Transactions API
  slug: global-payments-transactions-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Global Payments Unified Payments Disputes API
  slug: open-global-payments-disputes-api
- collection_type: open
  name: Global Payments Unified Payments Disputes Payment Methods API
  slug: open-global-payments-payment-methods-api
- collection_type: open
  name: Global Payments Unified Payments Disputes Settlements API
  slug: open-global-payments-settlements-api
- collection_type: open
  name: Global Payments Unified Payments Disputes Transactions API
  slug: open-global-payments-transactions-api
- collection_type: open
  name: Global Payments Unified Payments API
  slug: open-global-payments-unified-payments-api
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/global-payments/refs/heads/main/plans/global-payments-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/global-payments-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/global-payments/refs/heads/main/rate-limits/global-payments-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/global-payments-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/global-payments/refs/heads/main/finops/global-payments-finops.yml
  title: ''
  type: FinOps
  url: finops/global-payments-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.globalpayments.com/insights
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/global-payments/refs/heads/main/capabilities/global-payments-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/global-payments-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/global-payments/refs/heads/main/agentic-access/global-payments-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/global-payments-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/global-payments/refs/heads/main/security/global-payments-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/global-payments-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/global-payments/refs/heads/main/authentication/global-payments-authentication.yml
  title: ''
  type: Authentication
  url: authentication/global-payments-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/global-payments/refs/heads/main/scopes/global-payments-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/global-payments-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/globalpayments
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/global-payments
- group: start
  title: ''
  type: Portal
  url: https://developer.globalpayments.com/
- group: company
  title: ''
  type: Website
  url: https://www.globalpayments.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.globalpayments.com/llms.txt
created: '2026-03-21'
description: Global Payments is a leading worldwide provider of payment technology and software solutions delivering innovative services to customers globally. The company operates developer portals at developer.globalpayments.com and developer.globalpaymentsintegrated.com, offering a unified cloud-powered REST API for payment facilitation, card issuing, and multi-currency processing, along with integrated payment solutions for ISVs and software partners.
finops:
- has_sources: true
  method: generated
  name: Global Payments Finops
  primary_unit: ''
  service_category: Payments
  slug: global-payments-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/global-payments.png
layout: provider
modified: '2026-10-06'
name: Global Payments
nav: Providers
network: true
overview: 'Global Payments publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Disputes API, Payment Methods API, Settlements API, and 2 more. Tagged areas include E-Commerce, Payment Processing, Payment Technology, Payments, and Point-of-Sale.


  Global Payments'' developer surface includes engineering blog, authentication, developer portal, and 11 more developer resources.'
plans:
- name: Global Payments Plans Pricing
  plan_count: 2
  slug: global-payments-plans-pricing
press:
- date: ''
  title: Global Payments Inc. (@GlobalPaymentsInc)
  url: https://www.facebook.com/GlobalPaymentsInc/
- date: ''
  title: AI's vital role in payments and commerce
  url: https://www.globalpayments.com/insights/ai-in-payments-and-commerce
- date: ''
  title: BofA's New GenAI Assistant Transforms Global Payments ...
  url: https://www.prnewswire.com/news-releases/bofas-new-genai-assistant-transforms-global-payments-solutions-302570314.html
- date: ''
  title: Global Payments Unveils AI-First Genius Handheld Built for ...
  url: https://www.businesswire.com/news/home/20260512297137/en/Global-Payments-Unveils-AI-First-Genius-Handheld-Built-for-the-Future-of-Commerce
- date: ''
  title: Global Payments Joins Forces with AWS to Deliver ...
  url: https://investors.globalpayments.com/news-events/press-releases/detail/49/global-payments-joins-forces-with-aws-to-deliver-the-future
random_paper: 11
rate_limits:
- limit_count: 2
  name: Global Payments Rate Limits
  slug: global-payments-rate-limits
scopes:
- name: Global Payments Scopes
  scope_count: 4
  slug: global-payments-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 44.7
    developer_ergonomics: 28.6
    discoverability: 73.2
    operational_transparency: 7.9
  previous_composite: 26.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/global-payments/refs/heads/main/screenshots/global-payments-2026-06-20T181917.png
security:
- kind: authentication
  name: Global Payments Authentication
  slug: global-payments-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Global Payments Domain Security
  slug: global-payments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: global-payments
tags:
- E-Commerce
- Payment Processing
- Payment Technology
- Payments
- Point-of-Sale
- Fortune 1000
website: https://www.globalpayments.com/
---
