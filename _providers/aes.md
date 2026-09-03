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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: Mosaic is an AI-powered intelligent bidding application developed by Fluence (an AES and Siemens company) for optimizing energy market participation. Mosaic automates bidding strategies for battery en
  name: Fluence Mosaic API
  slug: fluence-mosaic-api
- description: Nispera is an asset performance management software platform by Fluence (an AES and Siemens company) for optimizing the performance of renewable energy and battery storage assets. Nispera provides mon
  name: Fluence Nispera API
  slug: fluence-nispera-api
artifact_total: 29
common:
- group: company
  title: ''
  type: Website
  url: https://www.aes.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aes-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aes-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/aes-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aes-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aes-conventions.yml
- group: auth
  title: AES Global Ethics and Compliance
  type: Compliance
  url: https://www.aes.com/about-us/our-people/ethics-and-compliance
- group: operate
  title: Contact the AES clean energy solutions team
  type: Support
  url: https://www.aes.com/customer-contact-form
- group: docs
  title: FERC-registered AES entities and standards-of-conduct posting
  type: Documentation
  url: https://www.aes.com/ferc-registered-entities
- group: start
  title: ''
  type: Portal
  url: https://www.aes.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.aes.com/about-aes
- group: company
  title: ''
  type: Blog
  url: https://www.aes.com/newsroom
- group: start
  title: Investor Relations
  type: Portal
  url: https://www.aes.com/investors
- group: start
  title: Careers
  type: Portal
  url: https://www.aes.com/careers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aes.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aes.com/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.aes.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aes-corporation/
- group: start
  title: Fluence Energy
  type: Portal
  url: https://fluenceenergy.com
coverage:
  checked: '2026-08-30'
  detail: AES Corporation runs no developer program at all — its 485-URL sitemap contains no developer, API or documentation section, and the one host that ever looked like an API, api.aes.com, is now a dangling CNAME to a decommissioned Azure App Service (microgridenergy-api.azurewebsites.net, NXDOMAIN), so the only machine-readable contract AES ever had has been retired without notice.
  evidence:
  - status: 404
    url: https://www.aes.com/openapi.json
  - status: 404
    url: https://www.aes.com/.well-known/api-catalog
  - status: 404
    url: https://www.aes.com/.well-known/agent-card.json
  - status: 200
    url: https://www.aes.com/sitemap.xml
  - status: 0
    url: https://api.aes.com/
  - status: 404
    url: https://fluenceenergy.com/openapi.json
  - status: 404
    url: https://www.aesindiana.com/openapi.json
  - status: 404
    url: https://www.aesohio.com/openapi.json
  reason: no-developer-program
  state: none
created: '2025-03-01'
description: The AES Corporation is a Fortune 500 global energy company that generates and distributes electrical power. AES operates a diverse portfolio of renewable, thermal, LNG, and battery storage facilities across multiple countries, serving utilities, industrial facilities, and end users. AES is the largest global supplier of clean energy to corporations in the Americas and operates 34.7 GW globally with $12.2 billion in annual revenue. The company serves 18.7 million household equivalents through utilities in Indiana, Ohio, and El Salvador. AES also co-founded Fluence Energy, a leading energy storage and software platform company.
features:
- description: AES is the largest global supplier of clean energy to corporations in the Americas, offering renewable energy from solar, wind, and hydro sources through long-term power purchase agreements.
  name: Carbon-Free Energy Supply
- description: Natural gas and LNG infrastructure providing reliable backup power and grid stability to complement intermittent renewable energy sources.
  name: Flexible Capacity
- description: Large-scale battery energy storage systems for grid stabilization, renewable integration, and energy arbitrage through Fluence, a joint venture with Siemens.
  name: Battery Energy Storage
- description: Transmission, distribution, and digital solutions for optimizing electricity delivery networks across AES utility operations in the US and Latin America.
  name: Grid Infrastructure
- description: Maximo, an AI-enabled solar installation robot, and AI safety platforms deployed across US operations to improve efficiency and reduce incident response time.
  name: AI-Powered Operations
- description: AI and machine learning digital platform developed by Fluence for intelligent asset optimization of energy storage and renewable generation facilities.
  name: Fluence IQ Platform
- description: Mosaic intelligent bidding application and Nispera asset performance management software enabling data-driven energy market participation and O&M optimization.
  name: Energy Market Software
- description: AES Indiana and AES Ohio provide regulated electric service to over 2.7 million customers with digital customer portals for account management.
  name: Regulated Utilities
finops:
- name: Aes Finops
  service_category: Energy / Asset Management Software
  slug: aes-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aes.png
integrations:
- description: AES co-founded Fluence Energy with Siemens to provide leading energy storage products and software platforms including Mosaic and Nispera.
  name: Fluence Energy
- description: Partnership with Google for 24/7 renewable energy commitments supporting data center operations with carbon-free electricity.
  name: Google
- description: Joint venture partner in Fluence Energy providing grid-scale battery storage systems and energy market optimization software.
  name: Siemens
- description: Participation in Midcontinent and PJM wholesale electricity markets through AES Indiana and AES Ohio utility operations.
  name: MISO and PJM Markets
layout: provider
modified: '2026-08-30'
name: AES Corporation
nav: Providers
network: true
overview: 'AES Corporation publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Power Generation, Renewable Energy, Battery Storage, and Utility.


  AES Corporation''s developer surface includes support, documentation, developer portal, engineering blog, and 15 more developer resources.'
plans:
- name: Aes Plans Pricing
  plan_count: 0
  slug: aes-plans-pricing
press:
- date: '2026-05-25'
  title: AES partners with AI Fund to accelerate AI-driven energy ...
  url: https://www.latitudemedia.com/industry-news/aes-partners-with-ai-fund-to-accelerate-ai-driven-energy-solutions/
- date: '2026-05-25'
  title: 'AES'' AI: Accelerating Renewable Energy Solutions'
  url: https://www.aes.com/about-us/innovation/ai-fund
- date: '2026-05-25'
  title: energy innovation at aes
  url: https://www.aes.com/about-us/innovation
- date: '2026-05-25'
  title: Haven Safety AI Launches AI-Native Safety Intelligence ...
  url: https://www.blufftontoday.com/press-release/story/52645/haven-safety-ai-launches-ai-native-safety-intelligence-platform-co-founded-with-the-aes-corporation-and-ai-fund/
- date: '2026-05-25'
  title: AES Deploys AI Safety Platform in U.S. Operations
  url: https://www.prnewswire.com/news-releases/aes-deploys-ai-safety-platform-in-us-operations-302711682.html
random_paper: 19
rate_limits:
- limit_count: 0
  name: Aes Rate Limits
  slug: aes-rate-limits
score:
  band: emerging
  composite: 22.1
  coverage:
    artifact_dirs: 15
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 22.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 32.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aes/refs/heads/main/screenshots/aes-2026-06-20T165545.png
security:
- kind: domain-security
  name: Aes Domain Security
  slug: aes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aes Vulnerability Disclosure
  slug: aes-vulnerability-disclosure
  summary_line: Hackerone
slug: aes
solutions:
- description: Global clean energy development with 17.9 GW in operation and 67 GW in development, primarily solar and wind projects serving corporate and utility customers.
  name: AES Renewables
- description: Flexible thermal power plants and LNG infrastructure providing reliable capacity to complement renewable generation and support grid reliability.
  name: AES Energy Infrastructure
- description: AES Indiana and AES Ohio regulated electric utilities serving 2.7 million customers with digital customer portals and clean energy transition plans.
  name: AES Utilities
- description: Innovation group developing next-generation energy solutions including AI-powered robotics, advanced energy storage, and grid modernization technologies.
  name: AES New Energy Technologies
tags:
- Energy
- Power Generation
- Renewable Energy
- Battery Storage
- Utility
- Clean Energy
- Fortune 500
use_cases:
- description: Companies seeking carbon-free electricity through power purchase agreements with AES to meet sustainability goals and RE100 commitments.
  name: Corporate Renewable Energy Procurement
- description: Utilities and grid operators deploying Fluence battery energy storage systems to balance supply and demand, provide frequency regulation, and integrate renewables.
  name: Energy Storage for Grid Stability
- description: Storage asset owners using Fluence Mosaic to automate bidding in wholesale electricity markets and maximize revenue from battery storage resources.
  name: Energy Market Revenue Optimization
- description: Solar and wind operators using Fluence Nispera to monitor asset health, optimize energy yield, and reduce operations and maintenance costs.
  name: Renewable Asset Performance Management
- description: Hyperscale technology companies partnering with AES for 24/7 carbon-free electricity to power data centers and meet sustainability commitments.
  name: Data Center Power
- description: Industrial facilities transitioning from fossil fuels to renewable energy through AES clean energy supply agreements and behind-the-meter storage.
  name: Industrial Decarbonization
website: https://www.aes.com/
---
