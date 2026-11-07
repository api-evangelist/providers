---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Kpmg Agentic Access
  operation_count: 6
  slug: kpmg-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: KPMG Origins is the public-facing platform implementing the NSW Integrated Waste Tracking System (IWTS) and is the single discoverable public REST API surface inside the KPMG brand. It exposes two API
  name: KPMG Origins (IWTS)
  slug: kpmg-origins-iwts
- baseURL: https://app.kpmgorigins.com/client-api/
  baseurl_source: declared
  description: APIs for Locations
  name: KPMG Locations API
  slug: kpmg-locations-api
- baseURL: https://app.kpmgorigins.com/client-api/
  baseurl_source: declared
  description: APIs to query Organizations
  name: KPMG Organizations API
  slug: kpmg-organizations-api
- baseURL: https://app.kpmgorigins.com/client-api/
  baseurl_source: declared
  description: APIs for Product Catalogue/Product Templates/Materials
  name: KPMG Product Templates API
  slug: kpmg-producttemplates-api
- baseURL: https://app.kpmgorigins.com/client-api/
  baseurl_source: declared
  description: APIs for Access Token
  name: KPMG Token API
  slug: kpmg-token-api
artifact_total: 17
collections:
- collection_type: open
  name: KPMG Origins APIs Discovery API
  slug: open-kpmg-discovery-api
- collection_type: open
  name: KPMG Origins APIs Discovery Movements API
  slug: open-kpmg-movements-api
- collection_type: open
  name: KPMG Origins APIs Discovery Registries API
  slug: open-kpmg-registries-api
- collection_type: open
  name: KPMG Origins APIs
  slug: open-kpmg
common:
- group: commercial
  href: https://artifacts.apis.io/kpmg/plans/kpmg-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kpmg-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/kpmg/rate-limits/kpmg-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kpmg-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/kpmg/finops/kpmg-finops.yml
  title: ''
  type: FinOps
  url: finops/kpmg-finops.yml
- group: agent
  href: https://artifacts.apis.io/kpmg/agentic-access/kpmg-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kpmg-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/kpmg/security/kpmg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kpmg-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/kpmg/authentication/kpmg-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kpmg-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://kpmg.com/
- group: company
  title: ''
  type: About
  url: https://kpmg.com/xx/en/about.html
- group: other
  title: ''
  type: Services
  url: https://kpmg.com/xx/en/what-we-do.html
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://kpmg.com/xx/en/our-insights.html
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://kpmg.com/us/en/insights-and-resources.html
- group: other
  title: ''
  type: Hub
  url: https://kpmg.com/xx/en/what-we-do/services/ai/ai-services.html
- group: other
  title: ''
  type: Framework
  url: https://kpmg.com/xx/en/what-we-do/services/ai/trusted-ai-framework.html
- group: other
  title: ''
  type: Services
  url: https://kpmg.com/us/en/capabilities-services/ai/trusted-ai.html
- group: other
  title: ''
  type: Facility
  url: https://kpmg.com/us/en/capabilities-services/kpmg-innovation-services/lakehouse.html
- group: company
  title: ''
  type: Newsletter
  url: https://kpmg.com/us/en/subscription.html
- group: other
  title: ''
  type: Registration
  url: https://kpmg.com/xx/en/account/register.html
- group: operate
  title: ''
  type: Help
  url: https://kpmg.com/us/en/home/misc/how-to-use-rss-feeds.html
- group: other
  title: ''
  type: RSS
  url: https://kpmg-career.talent-soft.com/job/all-rss-feeds.aspx
- group: other
  title: ''
  type: Podcast
  url: https://feeds.blubrry.com/feeds/kpmg_au_bi.xml
- group: other
  title: ''
  type: Product
  url: https://kpmgorigins.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kpmg
- group: other
  title: ''
  type: X
  url: https://x.com/KPMG
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/KPMG
- group: build
  title: ''
  type: ClientStories
  url: https://kpmg.com/xx/en/client-stories.html
- group: company
  title: ''
  type: Careers
  url: https://kpmg.com/xx/en/careers.html
- group: company
  title: ''
  type: PressRoom
  url: https://kpmg.com/xx/en/about/press-releases.html
- group: agent
  title: ''
  type: LlmsText
  url: https://kpmg.com/llms.txt
created: '2026-05-23'
description: 'KPMG is one of the Big Four professional services organizations, operating through a global network of independent member firms affiliated with KPMG International Limited, a private English company limited by guarantee that itself does not provide services to clients. The network spans more than 276,000 partners and employees across 138 countries and territories. KPMG organizes delivery across six service lines — Audit & Assurance, Tax, Legal, Advisory, ESG, and AI — and serves six industries: Consumer / Retail / Leisure; Energy, Natural Resources & Chemicals; Financial Services; Healthcare; Government & Public Sector; and Private Enterprise. AI is a first-class service line built on the KPMG Trusted AI framework — a ten-pillar approach covering Reliability, Security, Safety, Privacy, Sustainability, Explainability, Integrity, Transparency, Fairness, and Accountability — and packaged through five AI solutions: KPMG AI Jumpstart, AI Strategy, AI Trust, AI Workforce, and AI Technology.
  Alliances anchoring the AI delivery surface include Microsoft, Oracle, Salesforce, SAP, ServiceNow, and Workday, with collaboration noted with the World Economic Forum. KPMG Lakehouse, the firm''s USD 450 million learning-and-innovation campus in Lake Nona, Orlando, is the cultural and AI-upskilling hub for the US firm and a venue for client innovation sessions in generative AI, ESG, and talent strategy. Insights is KPMG''s research-publishing surface, organized across topic categories including AI and Technology, ESG, Operations, Risk and Regulation, Transformation, Value Creation, Workforce, Public Policy & Regulatory Change, Business Transformation, Audit & Assurance, Tax, Advisory, Sustainability, and Transactions, with flagship series such as the KPMG US Technology Survey Report, the KPMG Global Third-Party Risk Management Survey, the KPMG M&A Deal Market Study, Fit for Pillar Two, and AI Governance Principles for Boards. KPMG does not publish a public developer API or corporate developer
  portal at the network level; the firm has no enumerable public GitHub organization at `github.com/kpmg`. The one meaningful public API surface inside the KPMG brand is KPMG Origins (`kpmgorigins.com`) — an Australian regulated-waste tracking platform (initially the NSW Integrated Waste Tracking System / IWTS, with Queensland and other jurisdictions in scope) that exposes two REST APIs (Movements + Registries) over Swagger with API-key authentication, intended for integration with waste-operator software rather than as a general-purpose KPMG developer surface. Distribution to readers and client stakeholders flows through the Insights site, the US Subscription Center (Opportunity (In)sight monthly newsletter), KPMG Australia''s Business Insights podcast, and per-page RSS feeds offered on individual KPMG member-firm pages.'
finops:
- has_sources: true
  method: generated
  name: Kpmg Finops
  primary_unit: ''
  service_category: Professional Services
  slug: kpmg-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kpmg.png
jsonld:
- class_count: 52
  name: Kpmg Context
  property_count: 2
  slug: kpmg-context
layout: provider
modified: '2026-05-23'
name: KPMG
nav: Providers
network: true
overview: 'KPMG publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Locations API, Organizations API, Product Templates API, and 2 more. Tagged areas include Consulting, Audit, Tax, Legal, and Professional Services.


  The KPMG catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  KPMG''s developer surface includes authentication, YouTube channel, and 26 more developer resources.'
plans:
- name: Kpmg Plans Pricing
  plan_count: 3
  slug: kpmg-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 2
  name: Kpmg Rate Limits
  slug: kpmg-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: KPMG API Rules
  rule_count: 50
  severity_counts:
    error: 43
    hint: 0
    info: 2
    warn: 5
  slug: kpmg-rules
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 54.5
    catalog_earned_first_party: 0.0
    catalog_gap: 60.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 21.1
    contract_governance: 13.6
    contract_quality: 48.7
    developer_ergonomics: 26.2
    discoverability: 73.2
    operational_transparency: 21.1
  previous_composite: 32.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 42.9
      derived: 0
      marker_coverage: 57.1
      total: 7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/kpmg/kpmg-2026-06-20T184147.png
security:
- kind: authentication
  name: Kpmg Authentication
  slug: kpmg-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Kpmg Domain Security
  slug: kpmg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kpmg
tags:
- Consulting
- Audit
- Tax
- Legal
- Professional Services
- Big Four
- Advisory
- Artificial Intelligence
- Trusted AI
- ESG
- Sustainability
- Risk Management
- Regulations
- Cybersecurity
- Strategy
- Technology
- Workforce
- Research
- Insights
- Industry Analysis
- Transformation
- Pillar Two
- Waste Tracking
website: https://kpmg.com/
---
