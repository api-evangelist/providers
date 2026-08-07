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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Weyerhaeuser's API Management platform enabling partner and customer integration with wood products ordering, supply chain management, and customer connect portal services. The portal provides automat
  name: Weyerhaeuser API
  slug: weyerhaeuser-api
artifact_total: 18
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weyerhaeuser-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/weyerhaeuser
- group: company
  title: ''
  type: Website
  url: https://www.weyerhaeuser.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apimportal.weyerhaeuser.com/
- group: start
  title: ''
  type: Portal
  url: https://www.weyerhaeuser.com/woodproducts/customer-connect/customer-connect-portal-resources/
- group: start
  title: ''
  type: Signup
  url: https://devapimportal.weyerhaeuser.com/signup
- group: company
  title: ''
  type: Blog
  url: https://www.weyerhaeuser.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.weyerhaeuser.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.weyerhaeuser.com/privacy-policy
created: '2026-05-03'
description: Weyerhaeuser is one of the world's largest private owners and managers of timberlands, operating approximately 10.4 million acres of timberlands in the U.S. with management rights over 14 million additional acres in Canada. The company grows and harvests trees, builds homes, and manufactures forest products including engineered lumber, oriented strand board (OSB), plywood, and lumber. Weyerhaeuser operates a developer-facing API Management (APIM) portal enabling partners and customers to integrate with its digital systems for wood products ordering and supply chain management.
features:
- description: Azure API Management-powered developer portal for discovering, learning, and interactively testing Weyerhaeuser APIs with automatic documentation generation and multi-language code samples.
  name: API Management Portal
- description: Digital ordering and account management portal for wood products customers enabling order status tracking, railcar tracking, and search functionality.
  name: Customer Connect Portal
- description: ForteWEB, Javelin, and Stellar software tools for building professionals to size, specify, and design with Weyerhaeuser engineered lumber products.
  name: Engineered Lumber Software
- description: AI-driven forest digitization initiative creating a digital twin of timberlands operations to optimize harvest decisions and crew efficiency.
  name: Digital Twin Operations
- description: Western timberlands land access requests portal for managing recreational access, leases, and land-use permits on managed forest lands.
  name: Land Access Portal
finops:
- name: Weyerhaeuser Finops
  service_category: API
  slug: weyerhaeuser-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/weyerhaeuser.png
integrations:
- description: Azure API Management platform powering the Weyerhaeuser developer portal with subscription management, authentication, and documentation.
  name: Microsoft Azure APIM
- description: Enterprise resource planning integration for wood products manufacturing, order management, and financial operations.
  name: SAP ERP
- description: Structural engineering software integration for automated sizing and load calculations with Weyerhaeuser engineered lumber products.
  name: ForteWEB
jsonld:
- class_count: 8
  name: Weyerhaeuser Context
  property_count: 26
  slug: weyerhaeuser-context
layout: provider
modified: '2026-05-03'
name: Weyerhaeuser
nav: Providers
network: true
overview: 'Weyerhaeuser publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Timberlands, Wood Products, Forestry, Lumber, and Construction.


  The Weyerhaeuser catalog on APIs.io includes 1 JSON-LD context.


  Weyerhaeuser''s developer surface includes developer portal, signup flow, engineering blog, and 6 more developer resources.'
plans:
- name: Weyerhaeuser Plans Pricing
  plan_count: 3
  slug: weyerhaeuser-plans-pricing
press:
- date: '2026-05-25'
  title: Weyerhaeuser Trains AI to Map Every Tree in its 10M-Acre ...
  url: https://woodcentral.com.au/weyerhaeuser-trains-ai-to-map-every-tree-in-its-10m-acre-estate/
- date: '2026-05-25'
  title: Using Artificial Intelligence to Fine-Tune the Dryers at Our ...
  url: https://www.weyerhaeuser.com/blog/innovation-sutton-osb-mill-ai-power/
- date: '2026-05-25'
  title: 'Weyerhaeuser AI: 7 bold moves digitizing the forest'
  url: https://www.progressiverobot.com/2026/04/24/weyerhaeuser-ai-forest-digitization/
- date: '2026-05-25'
  title: Weyerhaeuser targets $1 billion profit gain with AI forestry ...
  url: https://www.nipimpressions.com/weyerhaeuser-targets-1-billion-profit-gain-with-ai-forestry-tools-cms-20306
- date: '2026-05-25'
  title: America's Largest Landowner Is Using AI to Digitize the ...
  url: https://www.wsj.com/tech/ai/americas-largest-landowner-is-using-ai-to-digitize-the-forest-bd3eec86
random_paper: 62
rate_limits:
- limit_count: 5
  name: Weyerhaeuser Rate Limits
  slug: weyerhaeuser-rate-limits
score:
  band: thin
  composite: 29.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 17.7
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 29.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/weyerhaeuser/refs/heads/main/screenshots/weyerhaeuser-2026-06-20T201416.png
security:
- kind: domain-security
  name: Weyerhaeuser Domain Security
  slug: weyerhaeuser-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: weyerhaeuser
tags:
- Timberlands
- Wood Products
- Forestry
- Lumber
- Construction
- Real Estate
- Fortune 500
use_cases:
- description: API integration for placing and managing wood products orders, checking inventory availability, and tracking shipment status.
  name: Wood Products Ordering
- description: Partner integration with Weyerhaeuser's supply chain systems for automated procurement, forecasting, and logistics coordination.
  name: Supply Chain Integration
- description: Integration with structural engineering software for automated sizing and specification of engineered lumber in building designs.
  name: Building Design Integration
- description: Digital systems for managing harvest schedules, silviculture planning, and forest inventory across millions of acres of timberlands.
  name: Timberlands Management
website: https://www.weyerhaeuser.com
---
