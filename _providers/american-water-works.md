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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 16
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/american-water-works-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/american-water-works-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://www.amwater.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/american-water-works-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/american-water-works-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/american-water-works-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/american-water-works-llms.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amwater.com/corp/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amwater.com/corp/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.amwater.com/corp/contact-us
- group: company
  title: ''
  type: Blog
  url: https://newsroom.amwater.com/
- group: start
  title: ''
  type: Login
  url: https://login.amwater.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/American-Water
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/american-water
- group: company
  title: ''
  type: Website
  url: https://www.amwater.com
- group: start
  title: ''
  type: Portal
  url: https://www.amwater.com/mywater
coverage:
  checked: '2026-09-02'
  detail: American Water ships software only as end-user products — the MyWater web portal and mobile app — and publishes nothing for software developers; every "Developers" page on amwater.com is a land-developer water-main-extension page, and developer.amwater.com and api.amwater.com do not resolve at all.
  evidence:
  - status: 404
    url: https://www.amwater.com/openapi.json
  - status: 404
    url: https://www.amwater.com/api-docs
  - status: 404
    url: https://www.amwater.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/American-Water/repos
  - status: 200
    url: https://www.amwater.com/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2024-11-15'
description: American Water Works Company is the largest publicly traded U.S. water and wastewater utility company, providing drinking water, wastewater, and other related services to approximately 14 million people in more than 1,700 communities across 14 states. The company operates through regulated utility subsidiaries and offers customer self-service through its MyWater online portal and mobile app.
features:
- description: Safe, reliable drinking water service to approximately 14 million people in 1,700+ communities across California, Georgia, Hawaii, Illinois, Indiana, Iowa, Kentucky, Maryland, Missouri, New Jersey, Pennsylvania, Tennessee, Virginia, and West Virginia.
  name: Drinking Water Service
- description: Wastewater collection, treatment, and disposal services for municipalities and communities under long-term service contracts and regulated utility operations.
  name: Wastewater Treatment
- description: Online customer self-service portal for bill payment, account management, usage monitoring, service start/stop, and alert enrollment.
  name: MyWater Customer Portal
- description: Operation and maintenance of water treatment plants, distribution systems, storage tanks, and pumping stations across 14 states.
  name: Water Infrastructure Management
- description: Partnering with municipalities and communities to take over operation of their water and wastewater systems, providing expertise and capital investment.
  name: Community Water Solutions
- description: Operating water and wastewater systems on U.S. military installations through 50-year privatization contracts.
  name: Military Base Water Services
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/american-water-works.png
integrations:
- description: Participation in open data initiatives enabling customers to download and share their water usage data with authorized third-party conservation and analytics applications.
  name: Green Button Water Data
- description: Advanced metering infrastructure (AMI) enabling real-time water usage monitoring, leak detection alerts, and data-driven conservation programs for customers.
  name: Smart Meter Infrastructure
layout: provider
modified: '2026-09-02'
name: American Water Works
nav: Providers
network: true
overview: 'American Water Works is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Water Utility, Wastewater, Public Utility, Infrastructure, and Environmental Services.


  American Water Works'' developer surface includes support, engineering blog, developer portal, and 13 more developer resources.'
plans:
- name: American Water Works Plans Pricing
  plan_count: 0
  slug: american-water-works-plans-pricing
press:
- date: '2026-05-25'
  title: The Role of Generative AI (GenAI) for the Global Water ...
  url: https://www.waterrf.org/research/projects/role-generative-ai-genai-global-water-sector
- date: '2026-05-25'
  title: AWWA releases white paper to help water utilities plan for ...
  url: https://www.awwa.org/AWWA-Articles/awwa-releases-white-paper-to-help-water-utilities-plan-for-data-centers/
- date: '2026-05-25'
  title: American Water Reinforces Need for Long Term ...
  url: https://www.prnewswire.com/news-releases/american-water-reinforces-need-for-long-term-investments-as-awwa-issues-new-report-on-us-water-systems-302740639.html
- date: '2026-05-25'
  title: 'AWWA''s new white paper, Cooling the Cloud: Water ...'
  url: https://www.facebook.com/AmericanWaterWorksAssociation/posts/awwas-new-white-paper-cooling-the-cloud-water-utilities-in-a-data-driven-world-h/1229587995870572/
- date: '2026-05-25'
  title: Financial Release Details
  url: https://ir.amwater.com/news-and-events/financial-releases/financial-release-details/2019/American-Water-Announces-10-Year-Capital-Spending-Plan-Sets-Long-Term-Growth-Targets-and-Announces-2020-Earnings-Guidance/default.aspx
random_paper: 19
rate_limits:
- limit_count: 0
  name: American Water Works Rate Limits
  slug: american-water-works-rate-limits
score:
  band: emerging
  composite: 16.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 18.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 27.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/american-water-works/refs/heads/main/screenshots/american-water-works-2026-06-20T171919.png
security:
- kind: domain-security
  name: American Water Works Domain Security
  slug: american-water-works-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: American Water Works Vulnerability Disclosure
  slug: american-water-works-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: american-water-works
tags:
- Water Utility
- Wastewater
- Public Utility
- Infrastructure
- Environmental Services
- Water Management
- Fortune 1000
use_cases:
- description: Providing reliable, safe, and affordable drinking water and wastewater service to homes and apartments across American Water's service territory.
  name: Residential Water Service
- description: Acquiring or taking over operations of financially stressed or aging municipal water systems to provide professional management and capital investment.
  name: Municipal System Acquisition
- description: Managing drinking water and wastewater systems on military bases under long-term privatization agreements with the U.S. Department of Defense.
  name: Military Installation Water Privatization
- description: Providing industrial-grade water supply and wastewater treatment services to manufacturing, food processing, and commercial facilities.
  name: Industrial Water Supply
website: https://www.amwater.com
---
