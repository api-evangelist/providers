---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomingdales-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bloomingdales
- group: company
  title: ''
  type: Website
  url: https://www.bloomingdales.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.macysinc.com/
- group: other
  title: ''
  type: VendorRelations
  url: https://www.bloomingdales.com/b/contact-us-vendor-faq/
- group: other
  title: ''
  type: Affiliate
  url: https://www.bloomingdales.com/c/affiliate-program/
- group: other
  title: ''
  type: CorporateSales
  url: https://www.bloomingdales.com/b/bloomingdales-corporate/
- group: other
  title: ''
  type: Loyalty
  url: https://www.bloomingdales.com/c/loyallist/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://customerservice-bloomingdales.com/app/answers/detail/a_id/2167/~/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://customerservice-bloomingdales.com/app/answers/detail/a_id/1075
- group: operate
  title: ''
  type: Contact
  url: https://customerservice-bloomingdales.com/app/answers/list/
- group: auth
  title: ''
  type: Compliance
  url: ''
created: '2026-05-05'
description: Bloomingdale's is an American luxury department store chain and a subsidiary of Macy's, Inc. Bloomingdale's does not publish a public developer portal; partner integration is delivered through the parent Macy's Inc. vendor and trade partner programs, drop-ship and EDI channels with suppliers, the Bloomingdale's affiliate program for marketing partners, and the shared Macy's Inc. technology platform powering Bloomingdale's commerce, loyalty, and fulfillment.
features:
- description: Bloomingdale's runs an affiliate program for media, review sites, and influencers, administered through major affiliate networks.
  name: Affiliate Marketing Program
- description: Suppliers integrate with Bloomingdale's via the shared Macy's Inc. vendor program, exchanging purchase orders, ASNs, invoices, and drop-ship orders over EDI.
  name: Vendor and Drop-Ship Integration
- description: The Loyallist loyalty program rewards customers across Bloomingdale's stores and online, with point accrual and redemption managed inside Bloomingdale's commerce platform.
  name: Loyallist Program
- description: Bloomingdale's offers a corporate sales program for bulk gifting and incentive purchases.
  name: Corporate and Bulk Gifting
- description: Commerce, fulfillment, and customer-data services are operated by parent Macy's Inc. on a shared technology platform.
  name: Macy's Inc. Shared Platform
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomingdales.png
layout: provider
modified: '2026-05-16'
name: Bloomingdale's
nav: Providers
network: true
overview: Bloomingdale's is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Retail, Fashion, Department Store, and Luxury.
random_paper: 11
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 2
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomingdales/refs/heads/main/screenshots/bloomingdales-2026-06-20T173522.png
security:
- kind: domain-security
  name: Bloomingdales Domain Security
  slug: bloomingdales-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bloomingdales
tags:
- Retail
- Fashion
- Department Store
- Luxury
use_cases:
- description: Publishers, review sites, and influencers monetize Bloomingdale's traffic via affiliate links and commission.
  name: Affiliate Commerce
- description: Luxury and fashion brands integrate with Bloomingdale's drop-ship and wholesale flows via the Macy's Inc. vendor program.
  name: Brand Vendor Integration
- description: Loyallist members accrue and redeem rewards across in-store and online shopping.
  name: Loyalty Program Engagement
- description: Businesses purchase bulk gifts and incentives through Bloomingdale's corporate sales program.
  name: Corporate Gifting Programs
website: https://www.bloomingdales.com/
---
