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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-27'
api_count: 0
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bhp-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bhp
- group: company
  title: ''
  type: Website
  url: https://www.bhp.com/
- group: other
  title: ''
  type: Suppliers
  url: https://www.bhp.com/suppliers
- group: other
  title: ''
  type: LocalBuying
  url: https://www.bhp.com/suppliers/local-buying-program
- group: other
  title: ''
  type: Customers
  url: https://www.bhp.com/about/our-businesses
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.bhp.com/investors
- group: other
  title: ''
  type: Sustainability
  url: https://www.bhp.com/sustainability
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bhp.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bhp.com/legal-disclaimer
- group: operate
  title: ''
  type: Contact
  url: https://www.bhp.com/contact
- group: auth
  title: ''
  type: Compliance
  url: ''
created: '2026-05-05'
description: BHP is one of the world's largest mining companies, headquartered in Melbourne, Australia. BHP does not publish a public developer portal; integration is delivered through enterprise procurement systems for tier-1 and tier-2 suppliers, charter and shipping data exchanges for commodity logistics, and standard commodity-trading and assay data exchange formats with customers and exchanges (LME, SHFE).
features:
- description: BHP's procurement platform supports supplier registration, prequalification, RFP responses, purchase orders, ASNs, and invoicing for tier-1 and tier-2 suppliers.
  name: Procurement and Supplier Integration
- description: BHP's Local Buying Program connects small regional suppliers with BHP sites via a managed portal.
  name: Local Buying Program
- description: Shipment, charter, and assay data for iron ore, copper concentrate, and other commodities are exchanged with carriers, ports, and customers via private channels.
  name: Commodity Logistics
- description: BHP publishes climate, water, biodiversity, and tailings disclosures aligned with TCFD, GRI, and the Global Industry Standard on Tailings Management.
  name: ESG and Sustainability Disclosures
- description: ASX, LSE, NYSE, and JSE listings drive regulated disclosure and shareholder communications.
  name: Investor and Market Communications
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bhp.png
layout: provider
modified: '2026-05-16'
name: BHP
nav: Providers
network: true
overview: BHP is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Mining, Resources, Commodities, Iron Ore, and Copper.
random_paper: 42
score:
  band: minimal
  composite: 12.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bhp/refs/heads/main/screenshots/bhp-2026-06-20T173224.png
security:
- kind: domain-security
  name: Bhp Domain Security
  slug: bhp-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bhp
tags:
- Mining
- Resources
- Commodities
- Iron Ore
- Copper
use_cases:
- description: Tier-1 and tier-2 suppliers register with BHP and exchange commercial documents through the procurement portal.
  name: Supplier Onboarding and Procurement
- description: Customers (steel mills, smelters, traders) coordinate shipments, assays, demurrage, and settlements with BHP via private commercial channels.
  name: Commodity Sales and Logistics
- description: Operating joint ventures (e.g. Escondida, Antamina, Samarco) exchange operational and financial data with BHP and other JV partners.
  name: Joint Venture Operations
- description: BHP integrates operational, environmental, and tailings monitoring data into Global Industry Standard on Tailings Management disclosures.
  name: Tailings and Environmental Monitoring
website: https://www.bhp.com/
---
