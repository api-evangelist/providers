---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    error_semantics: false
    event_surface_described: false
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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Trimble Navigation Agentic Access
  operation_count: 8
  slug: trimble-navigation-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 1
apis:
- description: The Trimble Advanced Positioning (TAP) Store API is a REST-based eCommerce API for purchasing and managing Trimble positioning service subscriptions including RTX correction services. Enables automate
  name: Trimble Positioning Services API
  slug: trimble-positioning-services
- description: The Catalyst API from Trimble Navigation — 2 operation(s) for catalyst.
  name: Trimble Navigation Catalyst API
  slug: trimble-navigation-catalyst-api
- description: The Corrections API from Trimble Navigation — 2 operation(s) for corrections.
  name: Trimble Navigation Corrections API
  slug: trimble-navigation-corrections-api
- description: The Positioning API from Trimble Navigation — 1 operation(s) for positioning.
  name: Trimble Navigation Positioning API
  slug: trimble-navigation-positioning-api
- description: The Receiver API from Trimble Navigation — 2 operation(s) for receiver.
  name: Trimble Navigation Receiver API
  slug: trimble-navigation-receiver-api
- description: The System API from Trimble Navigation — 1 operation(s) for system.
  name: Trimble Navigation System API
  slug: trimble-navigation-system-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Trimble Mobile Manager API
  slug: open-trimble-mobile-manager
- collection_type: open
  name: Trimble Mobile Manager Catalyst API
  slug: open-trimble-navigation-catalyst-api
- collection_type: open
  name: Trimble Mobile Manager Catalyst Corrections API
  slug: open-trimble-navigation-corrections-api
- collection_type: open
  name: Trimble Mobile Manager Catalyst Positioning API
  slug: open-trimble-navigation-positioning-api
- collection_type: open
  name: Trimble Mobile Manager Catalyst Receiver API
  slug: open-trimble-navigation-receiver-api
- collection_type: open
  name: Trimble Mobile Manager Catalyst System API
  slug: open-trimble-navigation-system-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trimble-navigation-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/trimble-navigation-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trimble-navigation-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trimble-navigation-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trimble-oss
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trimble-navigation
- group: company
  title: ''
  type: Website
  url: https://www.trimble.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.trimble.com/en/developer/docs
- group: docs
  title: ''
  type: Documentation
  url: https://developer.trimble.com/docs/mobile-manager/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.trimble.com/docs/mobile-manager/guides/integrate/
created: '2026-05-03'
description: Trimble Navigation Limited (now Trimble Inc.) is a global technology company founded in 1978 that pioneered commercial GPS technology. Trimble develops positioning, navigation, and geospatial solutions spanning construction, agriculture, transportation, and surveying industries. The company rebranded from Trimble Navigation Limited to Trimble Inc. in 2016. Its developer APIs cover GPS/GNSS positioning through Trimble Mobile Manager, high-accuracy survey integration via the Trimble Precision SDK, and geospatial data services. The positioning technology integrates GPS, laser, optical, and inertial technologies to deliver centimeter-level accuracy for professional applications.
examples:
- key_count: 2
  name: Trimble Mobile Manager Get Tmm Info Example
  slug: trimble-mobile-manager-get-tmm-info-example
- key_count: 3
  name: Trimble Mobile Manager Position Stream Example
  slug: trimble-mobile-manager-position-stream-example
finops:
- name: Trimble Navigation Finops
  service_category: API
  slug: trimble-navigation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trimble-navigation.png
json_schemas:
- name: Trimble Navigation GNSS Position
  property_count: 14
  slug: trimble-navigation-position
json_structures:
- name: Trimble Navigation Position Structure
  property_count: 0
  slug: trimble-navigation-position-structure
jsonld:
- class_count: 4
  name: Trimble Navigation Context
  property_count: 25
  slug: trimble-navigation-context
layout: provider
modified: '2026-05-19'
name: Trimble Navigation
nav: Providers
network: true
overview: 'Trimble Navigation publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Catalyst API, Corrections API, Positioning API, and 2 more. Tagged areas include GPS, GNSS, Positioning, Navigation, and Surveying.


  The Trimble Navigation catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Trimble Navigation''s developer surface includes authentication, documentation, getting-started guide, and 7 more developer resources.'
plans:
- name: Trimble Navigation Plans Pricing
  plan_count: 3
  slug: trimble-navigation-plans-pricing
press:
- date: '2026-05-25'
  title: Trimble to Acquire Document Crunch to Add AI-Powered ...
  url: https://www.barchart.com/story/news/1110119/trimble-to-acquire-document-crunch-to-add-ai-powered-risk-management-and-document-compliance-to-trimble-construction-one-project-delivery-ecosystem
- date: '2026-05-25'
  title: Trimble (TRMB) Latest News & Stock Updates - Page 2
  url: https://public.com/stocks/trmb/news/2
- date: '2026-05-25'
  title: Trimble offers precision for autonomous navigation, launches ...
  url: https://www.automatedwarehouseonline.com/trimble-offers-precision-for-autonomous-navigation-launches-agco-joint-venture/
- date: '2026-05-25'
  title: Trimble Changes Name to Reflect Company's Technology ...
  url: https://www.prnewswire.com/news-releases/trimble-changes-name-to-reflect-companys-technology-evolution-300337474.html
- date: '2026-05-25'
  title: Builder business and will extend Trimble's ability to provide ...
  url: https://www.facebook.com/TrimbleCorporate/posts/more-big-news-happened-todaywe-are-so-excited-to-announce-the-newest-member-of-t/1919754298098753/
random_paper: 20
rate_limits:
- limit_count: 5
  name: Trimble Navigation Rate Limits
  slug: trimble-navigation-rate-limits
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Trimble Navigation API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 5
  slug: trimble-mobile-manager-rules
- effective_rule_count: 5
  extends: []
  name: Trimble Navigation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: trimble-navigation-jsonschema-spectral-rules
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 18
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 54.5
    contract_quality: 55.2
    developer_ergonomics: 42.9
    discoverability: 59.3
    governance: 54.5
    operational_transparency: 10.5
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trimble-navigation/refs/heads/main/screenshots/trimble-navigation-2026-06-20T195716.png
security:
- kind: authentication
  name: Trimble Navigation Authentication
  slug: trimble-navigation-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Trimble Navigation Domain Security
  slug: trimble-navigation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Trimble Navigation Trust Center
  slug: trimble-navigation-trust-center
  summary_line: SOC 2, ISO 27001
slug: trimble-navigation
tags:
- GPS
- GNSS
- Positioning
- Navigation
- Surveying
- Geospatial
- Construction
- Fortune 1000
website: https://www.trimble.com
---
