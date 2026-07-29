---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
api_count: 1
apis:
- description: The BNSF API Center provides customer APIs for programmatic integration with BNSF Railway freight shipping operations. APIs enable real-time shipment tracing, intermodal hub operations, pricing and ra
  name: BNSF Railway API
  slug: bnsf-api
artifact_total: 16
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/berkshire-hathaway-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/berkshire-hathaway
- group: company
  title: ''
  type: Website
  url: https://www.berkshirehathaway.com
created: '2026-03-21'
description: Berkshire Hathaway is a multinational conglomerate holding company headquartered in Omaha, Nebraska. The company's diversified subsidiaries span insurance (GEICO, Berkshire Hathaway Specialty Insurance, National Indemnity), freight rail transportation (BNSF Railway), utilities and energy (Berkshire Hathaway Energy), manufacturing (Precision Castparts, Iscar), wholesale distribution (McLane Company), and services and retailing. BNSF Railway, one of North America's largest freight rail networks, operates a public API Center providing customer APIs for shipment tracking, pricing, scheduling, and waybill management.
features:
- description: BNSF Railway operates one of North America's largest freight rail networks, transporting consumer goods, agricultural products, industrial materials, coal, and intermodal containers across 32,500 route miles in 28 states and 3 Canadian provinces.
  name: BNSF Freight Rail Network
- description: Berkshire Hathaway's insurance operations include GEICO (auto insurance), Berkshire Hathaway Specialty Insurance, National Indemnity, General Re, and MedPro Group, providing insurance and reinsurance across personal and commercial lines.
  name: Insurance Operations
- description: Berkshire Hathaway Energy operates regulated electric and natural gas utilities, pipelines, and renewable energy facilities across the United States, United Kingdom, Canada, and Australia.
  name: Energy and Utilities
- description: Manufacturing subsidiaries include Precision Castparts (aerospace components), Iscar (cutting tools), Marmon Group (industrial products), and Lubrizol (specialty chemicals).
  name: Manufacturing and Industrial
- description: McLane Company provides wholesale distribution of grocery and foodservice products to retail and restaurant customers across the United States.
  name: Wholesale Distribution
finops:
- name: Berkshire Hathaway Finops
  service_category: API
  slug: berkshire-hathaway-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/berkshire-hathaway.png
integrations:
- description: BNSF APIs integrate with TMS platforms used by shippers and third-party logistics providers to automate freight booking, tracking, and documentation within existing supply chain workflows.
  name: Transportation Management Systems
- description: BNSF customer APIs enable direct integration with ERP and procurement systems to automate freight cost management, scheduling, and shipment visibility without manual portal access.
  name: Enterprise Resource Planning
layout: provider
modified: '2026-04-19'
name: Berkshire Hathaway
nav: Providers
network: true
overview: Berkshire Hathaway publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Conglomerate, Energy, Finance, Freight Rail, and Insurance.
plans:
- name: Berkshire Hathaway Plans Pricing
  plan_count: 3
  slug: berkshire-hathaway-plans-pricing
press:
- date: '2026-05-25'
  title: Greg Abel said at the 2026 Berkshire Hathaway annual ...
  url: https://www.facebook.com/cnbc/posts/greg-abel-said-at-the-2026-berkshire-hathaway-annual-shareholders-meeting-that-t/1361201429214580/
- date: '2026-05-25'
  title: 'Berkshire Hathaway Uses AI Agents: 10 Ways to ...'
  url: https://www.klover.ai/berkshire-hathaway-uses-ai-agents-10-ways-to-use-ai-in-depth-analysis-2025/
- date: '2026-05-25'
  title: Berkshire Hathaway Takes Reserved Stance on Artificial ...
  url: https://www.linkedin.com/posts/cnbc_berkshire-annual-meeting-live-warren-buffetts-activity-7456363880903176192-fOVM
- date: '2026-05-25'
  title: Why Buffett's Alphabet Bet Raises AI Cycle Questions
  url: https://www.vantagemarkets.com/en/academy/buffett-alphabet-ai-cycle-analysis/
- date: '2026-05-25'
  title: 'Berkshire Hathaway Specialty''s Mirza: How Generative AI ...'
  url: https://www.ambest.com/video/MediaArchive.aspx?lid=1068187747001&vid=6341117189112
random_paper: 77
rate_limits:
- limit_count: 5
  name: Berkshire Hathaway Rate Limits
  slug: berkshire-hathaway-rate-limits
score:
  band: emerging
  composite: 16.5
  delta: -2.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 19.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/berkshire-hathaway/refs/heads/main/screenshots/berkshire-hathaway-2026-06-20T173143.png
security:
- kind: domain-security
  name: Berkshire Hathaway Domain Security
  slug: berkshire-hathaway-domain-security
  summary_line: TLSv1.3 · DMARC
slug: berkshire-hathaway
tags:
- Conglomerate
- Energy
- Finance
- Freight Rail
- Insurance
- Investment
- Manufacturing
- Retail
- Utilities
- Fortune 100
use_cases:
- description: Shippers and logistics providers integrate the BNSF API to display real-time freight tracking in their transportation management systems and customer-facing applications.
  name: Freight Shipment Tracking
- description: Customers use the BNSF pricing and schedules APIs to obtain freight rates, compare transit times, and automate rate shopping in procurement and logistics workflows.
  name: Freight Pricing and Scheduling
- description: Shippers submit bills of lading and retrieve waybill information programmatically through the BNSF Waybill Management API to reduce manual data entry and streamline freight documentation.
  name: Waybill Submission
- description: Intermodal customers access container and trailer status, storage location, and driver pickup/delivery details at BNSF intermodal facilities through the Hub Operations API.
  name: Intermodal Hub Operations
website: https://www.berkshirehathaway.com
---
