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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
api_count: 4
apis:
- description: Lead and CRM integration surface. Includes the outbound Lead Forwarding Service (forwards incoming and processed dealership lead data to a third-party vendor as XML or email), inbound Activity Insert/
  name: DealerSocket CRM & Leads API
  slug: dealersocket-crm-leads-api
- description: Inbound customer integration surface. The Customer Update integration modifies customer records in DealerSocket CRM (with insert of not-yet-found customers noted as forthcoming on the public integrati
  name: DealerSocket Customers API
  slug: dealersocket-customers-api
- description: Outbound deal integration surface. Deal Push Basic performs a one-way push of basic deal data (customer, co-buyer, salesperson, and vehicle of interest) to the DMS, and Deal Push Advanced extends it w
  name: DealerSocket Deals & Desking API
  slug: dealersocket-deals-api
- description: Inbound call-tracking and activity-logging surface. CTI Direct Post logs inbound and outbound call information for activity tracking, Call Vendor Direct Post Work Note Update appends call follow-up da
  name: DealerSocket CTI & Activity Logging API
  slug: dealersocket-cti-activity-api
artifact_total: 8
asyncapis:
- description: ''
  name: Dealersocket Outbound Webhooks
  slug: dealersocket-outbound-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dealersocket-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dealersocket
- group: company
  title: ''
  type: Website
  url: https://dealersocket.com
- group: docs
  title: ''
  type: Documentation
  url: https://dealersocket.com/apis/
- group: company
  title: ''
  type: CertifiedPartners
  url: https://dealersocket.com/resources/certified-partners/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.solera.com/solutions/dealers/dealersocket/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dealersocket-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dealersocket.com/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/dealersocket-outbound-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dealersocket-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/dealersocket-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dealersocket-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dealersocket-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dealersocket-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://dealersocket.com/support/
- group: company
  title: ''
  type: Blog
  url: https://dealersocket.com/resources/dealersocket-blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://dealersocket.com/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dealersocket.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.solera.com/privacy-center/
- group: start
  title: ''
  type: Login
  url: https://www.dealer.solera.com/login/
created: '2026-07-10'
description: DealerSocket is an automotive dealership CRM and Dealer Management System (DMS) software platform for franchise and independent auto dealers, covering customer relationship management, inventory management, websites, digital marketing, and desking/deals. DealerSocket is a Solera company (acquired 2021; part of Solera's Vehicle Solutions line of business). DealerSocket exposes a set of inbound and outbound integration APIs - lead forwarding, deal push to the DMS, customer updates, activity and CTI/call logging - but access is not self-serve. It is delivered through DealerSocket's Certified Partners program (launched 2013, 500-plus integration points) and is application-, contract-, and certification-gated. There is no public developer portal, no published authentication reference, and no public endpoint or base-URL documentation; the logical APIs below are modeled from DealerSocket's public integrations page rather than a self-serve API reference.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dealersocket.png
layout: provider
modified: '2026-08-10'
name: DealerSocket
nav: Providers
network: true
overview: 'DealerSocket publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Dealership, CRM, DMS, and Leads.


  The DealerSocket catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  DealerSocket''s developer surface includes documentation, support, engineering blog, and 17 more developer resources.'
plans:
- name: Dealersocket Plans Pricing
  plan_count: 0
  slug: dealersocket-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Dealersocket Rate Limits
  slug: dealersocket-rate-limits
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 11
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 16.7
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 30.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dealersocket/refs/heads/main/screenshots/dealersocket-2026-07-25T211514.png
security:
- kind: domain-security
  name: Dealersocket Domain Security
  slug: dealersocket-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dealersocket
tags:
- Automotive
- Dealership
- CRM
- DMS
- Leads
- Inventory
- Deals
- Solera
- Partner API
- Certified Partners
website: https://dealersocket.com
---
