---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-09-03'
api_count: 35
apis:
- baseURL: https://apis.creatoriq.com
  baseurl_source: declared
  description: SafeIQ brand safety timeline API
  name: CreatorIQ Brand Safety API
  slug: creatoriq-brand-safety-api
- baseURL: https://apis.creatoriq.com
  baseurl_source: declared
  description: Brand Safety Public API (draft)
  name: CreatorIQ Brand Safety API
  slug: creatoriq-brandsafety-api
- baseURL: https://apis.creatoriq.com
  baseurl_source: declared
  description: Campaign information
  name: CreatorIQ Campaign API
  slug: creatoriq-campaign-api
- baseURL: https://apis.creatoriq.com
  baseurl_source: declared
  description: Campaign Conversion Metrics
  name: CreatorIQ Campaign Conversion Metrics API
  slug: creatoriq-campaign-conversion-metrics-api
- baseURL: https://apis.creatoriq.com
  baseurl_source: declared
  description: CJ reports
  name: CreatorIQ CJ API
  slug: creatoriq-cj-api
- baseURL: https://apis.creatoriq.com
  baseurl_source: declared
  description: Creator payment-info collection status
  name: CreatorIQ Creator Payment Info API
  slug: creatoriq-creator-payment-info-api
- baseURL: https://apis.creatoriq.com
  baseurl_source: declared
  description: Divisions public API
  name: CreatorIQ Divisions API
  slug: creatoriq-divisions-api
- baseURL: https://apis.creatoriq.com
  baseurl_source: declared
  description: Ecommerce public API
  name: CreatorIQ Ecommerce API
  slug: creatoriq-ecommerce-api
- baseURL: https://apis.creatoriq.com
  baseurl_source: declared
  description: General section of reporting
  name: CreatorIQ General API
  slug: creatoriq-general-api
- baseURL: https://apis.creatoriq.com
  baseurl_source: declared
  description: Global Conversion Metrics Configuration
  name: CreatorIQ Global Conversion Metrics Configuration API
  slug: creatoriq-global-conversion-metrics-configuration-api
- baseURL: https://apis.creatoriq.com
  baseurl_source: declared
  description: LinkTracking public API
  name: CreatorIQ Link Tracking API
  slug: creatoriq-linktracking-api
- baseURL: https://apis.creatoriq.com
  baseurl_source: declared
  description: Lists public API
  name: CreatorIQ Lists API
  slug: creatoriq-lists-api
- baseURL: https://apis.creatoriq.com
  baseurl_source: declared
  description: Notes public API
  name: CreatorIQ Notes API
  slug: creatoriq-notes-api
- baseURL: https://apis.creatoriq.com
  baseurl_source: declared
  description: Onesheets public API
  name: CreatorIQ Onesheet API
  slug: creatoriq-onesheet-api
- baseURL: https://apis.creatoriq.com
  baseurl_source: declared
  description: Creator payables
  name: CreatorIQ Payables API
  slug: creatoriq-payables-api
- baseURL: https://apis.creatoriq.com
  baseurl_source: declared
  description: Creator payouts
  name: CreatorIQ Payouts API
  slug: creatoriq-payouts-api
- baseURL: https://apis.creatoriq.com
  baseurl_source: declared
  description: Publisher public API
  name: CreatorIQ Publisher API
  slug: creatoriq-publisher-api
- baseURL: https://apis.creatoriq.com
  baseurl_source: declared
  description: Reporting
  name: CreatorIQ Reporting API
  slug: creatoriq-reporting-api
- baseURL: https://apis.creatoriq.com
  baseurl_source: declared
  description: Public social API
  name: CreatorIQ Social API
  slug: creatoriq-social-api
- baseURL: https://apis.creatoriq.com
  baseurl_source: declared
  description: Subscription API part
  name: CreatorIQ Subscription API
  slug: creatoriq-subscription-api
artifact_total: 44
asyncapis:
- description: ''
  name: Creatoriq Webhooks
  slug: creatoriq-webhooks
collections:
- collection_type: open
  name: CreatorIQ Brand Safety (draft)
  slug: open-creatoriq-brand-safety-draft
- collection_type: open
  name: CreatorIQ SafeIQ Brand Safety API
  slug: open-creatoriq-brand-safety
- collection_type: open
  name: CreatorIQ Campaign APIs
  slug: open-creatoriq-campaigns
- collection_type: open
  name: Conversion Metrics API
  slug: open-creatoriq-conversion-metrics
- collection_type: open
  name: CreatorIQ Ecommerce APIs
  slug: open-creatoriq-ecommerce
- collection_type: open
  name: CreatorIQ CRM LinkTracking API
  slug: open-creatoriq-link-tracking
- collection_type: open
  name: CreatorIQ CRM Lists API
  slug: open-creatoriq-lists
- collection_type: open
  name: CreatorIQ CRM Publishers API
  slug: open-creatoriq-notes
- collection_type: open
  name: CreatorIQ CRM Onesheets API
  slug: open-creatoriq-onesheets
- collection_type: open
  name: CreatorIQ Payments API
  slug: open-creatoriq-payments
- collection_type: open
  name: CreatorIQ CRM Publishers API
  slug: open-creatoriq-publishers
- collection_type: open
  name: CreatorIQ Reporting APIs
  slug: open-creatoriq-reports
- collection_type: open
  name: CreatorIQ Social Account APIs
  slug: open-creatoriq-socials
- collection_type: open
  name: CreatorIQ Divisions APIs
  slug: open-creatoriq-v1-divisions
- collection_type: open
  name: CreatorIQ CRM Campaigns API V2
  slug: open-creatoriq-v2-campaigns
- collection_type: open
  name: CreatorIQ CRM Publishers API V2
  slug: open-creatoriq-v2-publishers
- collection_type: open
  name: CreatorIQ Public APIs
  slug: open-creatoriq-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/creatoriq-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.creatoriq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.creatoriq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.creatoriq.com/docs/ciq-api-documentation/o5yqwvpp1lbnb-overview
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.creatoriq.com/docs/ciq-api-documentation/6e239b2598043-creator-iq-crm-publishers-api
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.creatoriq.com/docs/ciq-api-documentation/05lf89tv60rvy-introduction-to-api-keys
- group: auth
  title: ''
  type: Authentication
  url: authentication/creatoriq-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://www.creatoriq.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.creatoriq.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.creatoriq.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/creatoriq-plans-pricing.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.creatoriq.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.creatoriq.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.creatoriq.com/legal/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.creatoriq.com/legal/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/creatoriq-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/creatoriq-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.creatoriq.com/trust
- group: auth
  title: ''
  type: DomainSecurity
  url: security/creatoriq-domain-security.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.creatoriq.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://apidocs.creatoriq.com/docs/ciq-api-documentation/o5yqwvpp1lbnb-overview
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/creatoriq-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://apidocs.creatoriq.com/docs/ciq-api-documentation/6b7999d265a29-changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/creatoriq-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/creatoriq-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/creatoriq-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/creatoriq-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/creatoriq-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/creatoriq-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/creatoriq-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/creatoriq-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/creatoriq-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/_index.yml
created: '2026-08-11'
description: 'CreatorIQ is an enterprise creator- and influencer-marketing platform used by brands and agencies to discover creators, build and manage a private creator network, run and measure campaigns, handle creator payouts, and report on performance across Instagram, TikTok, YouTube and other social networks. Its public REST API — documented on a Stoplight portal at apidocs.creatoriq.com and served from https://apis.creatoriq.com — exposes the customer''s own CRM: publishers (creators), campaigns, lists, one-sheets, notes, divisions, social accounts and post/account metrics, an asynchronous reporting surface of forty report views, ecommerce promo codes and transactions, affiliate link tracking, conversion metrics, SafeIQ brand-safety scoring, and a Payments API for payouts and payables. A pub/sub webhook API lets integrators subscribe to campaign, creator, one-sheet and list events with MD5 and SHA-256 signed callbacks. Authentication is a single `x-api-key` header issued per partner
  or per division by a CreatorIQ account manager; there is no self-serve signup.'
image: https://www.creatoriq.com/hubfs/2025%20Rebrading%20Assets%20%3E%20DO%20NOT%20DELETE/Logos/creatorIQ-logo-new.svg
layout: provider
modified: '2026-08-11'
name: CreatorIQ
nav: Providers
network: true
overview: 'CreatorIQ publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Brand Safety API, Campaign API, and 18 more. Tagged areas include Influencer Marketing, Creator Economy, Social-Media, Marketing, and Campaign Management.


  The CreatorIQ catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CreatorIQ''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, pricing, and 27 more developer resources.'
plans:
- name: Creatoriq Plans Pricing
  plan_count: 0
  slug: creatoriq-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Creatoriq Rate Limits
  slug: creatoriq-rate-limits
score:
  band: strong
  composite: 63.9
  coverage:
    artifact_dirs: 23
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 69.4
    developer_ergonomics: 66.1
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 78.9
  previous_composite: 63.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/creatoriq/refs/heads/main/screenshots/creatoriq-2026-08-17T080838.png
security:
- kind: authentication
  name: Creatoriq Authentication
  slug: creatoriq-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Creatoriq Domain Security
  slug: creatoriq-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Creatoriq Vulnerability Disclosure
  slug: creatoriq-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Creatoriq Trust Center
  slug: creatoriq-trust-center
  summary_line: ISO/IEC 27001:2022
slug: creatoriq
tags:
- Influencer Marketing
- Creator Economy
- Social-Media
- Marketing
- Campaign Management
- creator-crm
- Social Analytics
- Brand Safety
- Affiliate Marketing
- creator-payments
- E-Commerce
- Reporting
- Webhook
website: https://www.creatoriq.com/
---
