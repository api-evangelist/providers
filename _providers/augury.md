---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://www.augury.com/security/coordinated-vulnerability-disclosure
- group: design
  href: https://artifacts.apis.io/augury/json-ld/augury-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/augury-context.jsonld
- group: design
  href: https://artifacts.apis.io/augury/vocabulary/augury-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/augury-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/augury/llms/augury-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/augury-llms.txt
- group: auth
  href: https://artifacts.apis.io/augury/well-known/augury-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/augury-security.txt
- group: auth
  href: https://artifacts.apis.io/augury/well-known/augury-endpoint-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/augury-endpoint-security.txt
- group: agent
  href: https://artifacts.apis.io/augury/well-known/augury-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/augury-well-known.yml
- group: other
  href: https://artifacts.apis.io/augury/hosts/augury-hosts.yml
  title: ''
  type: Hosts
  url: hosts/augury-hosts.yml
- group: build
  href: https://artifacts.apis.io/augury/integrations/augury-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/augury-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/augury/vendors/augury-vendors.yml
  title: ''
  type: Vendors
  url: vendors/augury-vendors.yml
- group: auth
  href: https://artifacts.apis.io/augury/security/augury-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/augury-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/augury/security/augury-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/augury-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.augury.com
- group: other
  title: ''
  type: MachineHealth
  url: https://www.augury.com/machine-health/
- group: other
  title: ''
  type: ProcessHealth
  url: https://www.augury.com/process-health/
- group: company
  title: ''
  type: Partners
  url: https://www.augury.com/partners/
- group: other
  title: ''
  type: KnowledgeBase
  url: https://endpoint.augury.com/
- group: operate
  title: ''
  type: Support
  url: https://www.augury.com/access-our-knowledge-base/
- group: company
  title: ''
  type: About
  url: https://www.augury.com/about/
- group: company
  title: ''
  type: Newsroom
  url: https://www.augury.com/media-center/press/
- group: company
  title: ''
  type: Blog
  url: https://www.augury.com/blog/
- group: company
  title: ''
  type: Careers
  url: https://www.augury.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.augury.com/contact-us/
- group: start
  title: ''
  type: Login
  url: https://app.augury.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.augury.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.augury.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.augury.com/terms-of-use/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.augury.com
coverage:
  checked: '2026-10-20'
  detail: Augury's Halo platform API is referenced only for customers and certified integrators; no public reference, spec or MCP schema exists, and endpoint.augury.com/mcp and app.augury.com/mcp answer 403 before routing.
  evidence:
  - status: 403
    url: https://endpoint.augury.com/mcp
  - status: 404
    url: https://api.augury.com/openapi.json
  reason: customer-only-docs
  state: gated
created: '2026-05-25'
description: Augury is a New York City-headquartered industrial AI company founded in 2011 by Gal Shaul and Saar Yoskovitz that profiles itself as the leader in Machine Health and Production Health for manufacturing. Its flagship offering pairs purpose-built IoT vibration, temperature, and magnetic sensors — most prominently the Halo Node and earlier Auguscope hardware — with a cloud platform that applies prescriptive AI diagnostics to rotating and electrical equipment, advertised as delivering 75% fewer false alarms than threshold-based vibration systems and trained on more than one billion hours of machine monitoring data. Augury's product portfolio spans Machine Health (predictive maintenance for assets such as motors, pumps, fans, compressors, and gearboxes), Process Health (process optimization software acquired with Seebo in 2022 for yield, waste, and energy improvements), and an Industrial AI Workforce of AI agents that act on combined machine and operational data. The company runs
  an integration ecosystem branded Augury Plus (CMMS/EAM connectors for SAP PM, IBM Maximo, Infor EAM, MaintainX, and cloud/industrial platforms including Microsoft Azure, PTC, and AVEVA Connect), Augury On (OEM-embedded Machine Health with partners such as Grundfos, Schneider Electric, Trane, Carrier, Bently Nevada, and Baker Hughes), and Augury By (service partners including Accenture, Deloitte, Bain, McKinsey, Sodexo, Aramark, and AECOM). Augury closed a $75M Series F in February 2025 at a $1B+ valuation led by Lightrock with Insight Partners, Eclipse, Qumra Capital, La Maison Partners, SE Ventures, and Qualcomm Ventures, reports a 5x revenue increase since 2021, and serves 170+ global manufacturers across 40+ countries including Heineken, PepsiCo (Frito-Lay), Colgate-Palmolive, Shell, and Hershey's. The company commercializes through hardware-plus-subscription contracts and embedded OEM agreements, references public APIs and certified system integrator partners for custom integrations
  into customer enterprise systems, and does not publish an open developer portal, OpenAPI description, SDK, or public-facing API reference for the Halo platform.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/augury.png
jsonld:
- class_count: 19
  name: Augury Context
  property_count: 14
  slug: augury-context
layout: provider
modified: '2026-05-25'
name: Augury
nav: Providers
network: true
overview: 'Augury is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Industrial AI, Machine Health, Process Health, Predictive Maintenance, and Vibration Analysis.


  The Augury catalog on APIs.io includes 1 JSON-LD context.


  Augury''s developer surface includes support, engineering blog, pricing, and 25 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.3
    catalog_earned_first_party: 0.0
    catalog_gap: 75.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 26.3
    contract_governance: 3.8
    contract_quality: 14.7
    developer_ergonomics: 7.1
    discoverability: 56.3
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 25.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/augury/augury-2026-06-20T172558.png
security:
- kind: domain-security
  name: Augury Domain Security
  slug: augury-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Augury Vulnerability Disclosure
  slug: augury-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: augury
tags:
- Industrial AI
- Machine Health
- Process Health
- Predictive Maintenance
- Vibration Analysis
- Condition Monitoring
- IoT Sensors
- Halo
- Manufacturing
- Reliability
- Asset Performance
- OT
- CMMS
- EAM
website: https://www.augury.com
---
