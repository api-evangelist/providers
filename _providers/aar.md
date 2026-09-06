---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-05'
api_count: 9
apis:
- description: AAR's parts supply division distributes new and used aircraft and engine parts to commercial airlines, MROs, and government customers globally. Shipped and received 23 million commercial parts in FY20
  name: AAR Parts Supply
  slug: aar-parts-supply
- description: AAR provides airframe maintenance, repair, and overhaul (MRO) services as the leading North American MRO provider. Services cover complete airframe checks, structural repairs, modifications, and aircr
  name: AAR Airframe MRO
  slug: aar-airframe-mro
- description: AAR component MRO services provide comprehensive maintenance, repair, and overhaul for aircraft components, avionics, landing gear, and accessories for commercial and government aviation platforms.
  name: AAR Component MRO
  slug: aar-component-mro
- description: Trax is AAR's aviation software subsidiary, wholly owned since 2023. Its flagship eMRO is a browser-based, cloud-hosted aviation ERP unifying engineering, planning, production, inventory, quality, doc
  name: AAR Trax Aviation Software
  slug: aar-trax
- description: Aerostrat is AAR's maintenance planning software subsidiary, acquired in 2025 and run under Trax. Its flagship product Aerros is an ERP-agnostic solution for long-range maintenance scheduling, capacit
  name: AAR Aerostrat (Aerros)
  slug: aar-aerostrat
- description: Airinmar is AAR's aviation warranty management and components repair solution, providing warranty claim processing, repair order management, and vendor management for airlines and MRO organizations.
  name: AAR Airinmar Warranty and Claims
  slug: aar-airinmar
- description: AAR's government services division provides comprehensive maintenance and supply chain programs, shelters and sustainment systems, and aircraft parts and services to government and defense customers a
  name: AAR Government Services
  slug: aar-government-services
- description: The AAR PAARTS Store is AAR's online aviation parts storefront, running on Adobe Commerce (Magento 2). It exposes the platform's standard REST webapi at https://shop.aarcorp.com/rest/V1/ and a SOAP en
  name: AAR PAARTS Store Commerce API
  slug: aar-paarts-store
- description: Airvoyant is AAR's AI-driven parts procurement platform, launched April 2026 with Delta Air Lines and Air Canada as early adopters and AWS as its agentic-AI technology partner. It connects buyers to t
  name: AAR Airvoyant
  slug: aar-airvoyant
artifact_total: 31
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aar-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aar-corp
- group: company
  title: ''
  type: Website
  url: https://www.aarcorp.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aarcorp.com/en/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aarcorp.com/en/terms-and-conditions/privacy-notice/
- group: operate
  title: ''
  type: Support
  url: https://www.aarcorp.com/en/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.aarcorp.com/en/newsroom/press-releases/
- group: auth
  title: ''
  type: Compliance
  url: https://www.aarcorp.com/en/about/certifications/
- group: design
  title: ''
  type: Conformance
  url: conformance/aar-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aar-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aar-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aar-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aar-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aar-llms.txt
created: '2026-04-19'
description: 'AAR CORP. (NYSE: AIR) is a global aerospace and defense aftermarket solutions company and the number one aviation maintenance, repair and overhaul (MRO) provider in North America. It supplies new and used airframe and engine parts, performs airframe and component MRO, runs expeditionary and sustainment programs for government and defense customers on five continents, and operates four aviation software businesses — Trax (eMRO/eMobility aviation ERP), Aerostrat (Aerros maintenance scheduling), Airvoyant (AI-driven parts procurement, launched April 2026) and Airinmar (component repair and warranty management) — whose software covers more than 10,000 aircraft. AAR publishes no developer program, no API reference and no machine-readable contract; its only anonymously reachable API surface is the undocumented Adobe Commerce webapi behind the AAR PAARTS Store at shop.aarcorp.com/rest/V1/.'
features:
- description: Global distribution of new and used aircraft and engine parts for commercial and government aviation platforms with 23 million parts processed annually.
  name: Aircraft Parts Distribution
- description: North America's leading airframe maintenance, repair, and overhaul services including full structural checks, modifications, and aircraft painting.
  name: Airframe MRO
- description: Comprehensive component, avionics, and landing gear maintenance and repair services for commercial and military aviation.
  name: Component MRO
- description: Integrated aviation maintenance management software covering fleet management, maintenance tracking, inventory, and regulatory compliance.
  name: Trax MRO Software
- description: Aviation supply chain software for inventory optimization, demand forecasting, and procurement automation.
  name: Aerostrat Parts Management
- description: Warranty claim processing and components repair management software for airlines and MRO organizations.
  name: Airinmar Warranty Management
- description: Defense and government aviation services including maintenance programs, shelter systems, and supply chain support in over 20 countries.
  name: Government Expeditionary Services
finops:
- name: Aar Finops
  service_category: Aerospace / MRO
  slug: aar-finops
image: /assets/icons/aar.png
integrations:
- description: Direct partnerships with major commercial airlines for MRO contracts, parts supply, and software implementation.
  name: Airlines and Commercial Operators
- description: Contracts with US and international government defense agencies for aircraft sustainment and supply chain services.
  name: Government and Defense Agencies
- description: Regulatory approvals and compliance integration with FAA, EASA, and other civil aviation authority regulatory frameworks.
  name: FAA and EASA
- description: Authorized maintenance and parts relationships with major aircraft OEMs including Boeing, Airbus, and engine manufacturers.
  name: OEM Partnerships
layout: provider
modified: '2026-08-29'
name: AAR Corp
nav: Providers
network: true
overview: 'AAR Corp publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Aviation, MRO, Aerospace, Defense, and Parts Supply.


  AAR Corp''s developer surface includes support, engineering blog, authentication, and 12 more developer resources.'
plans:
- name: Aar Plans Pricing
  plan_count: 1
  slug: aar-plans-pricing
press:
- date: '2026-05-25'
  title: AAR is excited to announce the launch of Airvoyant, an AI- ...
  url: https://www.instagram.com/p/DXZDtFaCleM/
- date: '2026-05-25'
  title: AAR launches Airvoyant℠, an AI-driven procurement ...
  url: https://www.prnewswire.com/news-releases/aar-launches-airvoyant-an-ai-driven-procurement-platform-for-airlines-and-mros-302748577.html
- date: '2026-05-25'
  title: AAR launches Airvoyant AI buying platform for airlines
  url: https://www.stocktitan.net/news/AIR/aar-launches-airvoyant-sm-an-ai-driven-procurement-platform-for-eyurv106zf5r.html
- date: '2026-05-25'
  title: News & Events | AAR
  url: https://www.aar.org/news/
- date: '2026-05-25'
  title: After-Action Review for AI (AAR/AI)
  url: https://dl.acm.org/doi/10.1145/3453173
random_paper: 14
rate_limits:
- limit_count: 1
  name: Aar Rate Limits
  slug: aar-rate-limits
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 54.0
    catalog_earned_first_party: 16.0
    catalog_gap: 61.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 29.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 55.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aar/refs/heads/main/screenshots/aar-2026-06-20T162956.png
security:
- kind: authentication
  name: Aar Authentication
  slug: aar-authentication
  summary_line: http-bearer · 1 scheme
- kind: domain-security
  name: Aar Domain Security
  slug: aar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aar
tags:
- Aviation
- MRO
- Aerospace
- Defense
- Parts Supply
- Maintenance
- Government
- Aviation Software
- Supply Chain
- E-Commerce
- Fortune 1000
use_cases:
- description: Commercial airlines outsourcing airframe and component maintenance to AAR for cost-effective, FAA/EASA-approved maintenance programs.
  name: Commercial Airline MRO
- description: Airlines and MROs sourcing new and used aircraft parts through AAR's global parts distribution network for aircraft-on-ground (AOG) situations.
  name: Aviation Parts Sourcing
- description: Airlines and MROs implementing Trax MRO software for end-to-end aircraft maintenance management, inventory control, and compliance reporting.
  name: Fleet Management Software
- description: Defense agencies contracting AAR for aircraft maintenance, supply chain, and expeditionary sustainment programs in deployed environments.
  name: Government Aircraft Sustainment
- description: Airlines using Airinmar to streamline warranty claim submissions, track repair orders, and manage vendor relationships for component warranties.
  name: Warranty Claims Processing
- description: MRO organizations using Aerostrat to optimize parts inventory levels, reduce carrying costs, and improve procurement efficiency.
  name: Supply Chain Optimization
website: https://www.aarcorp.com
---
