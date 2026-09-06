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
api_count: 5
apis:
- description: The Lumen Developer Center publishes Lumen's enterprise API catalog, including Location, Quoting, Ordering, Service Inventory, Billing, Outbound Notification, and Trouble Ticket APIs. All APIs use OAu
  name: Lumen Developer Center APIs
  slug: lumen-developer-center
- description: The Lumen API Marketplace was the enterprise catalog where partners and customers browsed APIs and requested credentials. It has been folded into the Lumen Developer Center and Lumen Connect. As of 20
  name: Lumen API Marketplace
  slug: lumen-api-marketplace
- description: 'The Level 3 / Lumen OpenAPI Services portal provided OpenAPI-described REST services such as the Lumen Location API. The portal is GONE: developer.level3.com no longer resolves in DNS (probed 2026-09-'
  name: Lumen OpenAPI Services (Level 3 legacy)
  slug: lumen-openapi-services
- description: The Public Sector API Center offers government-tailored REST APIs for Lumen network services, enabling federal, state, and local agencies to programmatically order, provision, and monitor connectivity
  name: Lumen Public Sector API Center
  slug: lumen-public-sector-api-center
- description: Quantum Fiber is Lumen's residential multi-gigabit fiber brand that supersedes CenturyLink in markets with fiber deployment, with account and service management exposed through consumer web and mobile
  name: Quantum Fiber Residential Services
  slug: quantum-fiber
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.centurylink.com
- group: other
  title: ''
  type: Corporate
  url: https://www.lumen.com/
- group: other
  title: ''
  type: Developer
  url: https://developer.lumen.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.lumen.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.lumen.com/devcenter/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lumen.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.lumen.com/devcenter/getting-started
- group: operate
  title: ''
  type: Support
  url: https://developer.lumen.com/devcenter/support
- group: company
  title: ''
  type: Blog
  url: https://www.lumen.com/blog-and-news/en-us/home
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/centurylink
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lumentechnologies
- group: other
  title: ''
  type: QuantumFiber
  url: https://www.quantumfiber.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lumen.com/en-us/about/legal/api-developer-terms-and-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lumen.com/en-us/about/legal/privacy-notice.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/centurylink-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/centurylink-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/centurylink-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/centurylink-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/centurylink-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/centurylink-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/centurylink-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/centurylink-packages.yml
- group: design
  title: ''
  type: Components
  url: components/centurylink-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/centurylink-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/centurylink-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/centurylink-domain-security.yml
created: '2026-03-23'
description: 'CenturyLink is the residential broadband and home services brand of Lumen Technologies, a Fortune 500 telecommunications provider operating one of the largest fiber networks in North America. Following the Level 3 acquisition and rebrand to Lumen, CenturyLink''s developer surface is exposed through the Lumen Developer Center, which publishes REST APIs secured by OAuth 2.0 for enterprise location qualification, quote-to-order, provisioning, billing, notifications, CDN and edge compute, DDoS mitigation, and Public Sector networking products. The production API gateway answers at api.lumen.com, but no OpenAPI, AsyncAPI or GraphQL contract is published anonymously: the Developer Center is a module-federation single-page app that returns the same HTML shell for every path and loads its specifications from a sign-in-gated service.'
finops:
- name: Centurylink Finops
  service_category: Telecommunications / Network
  slug: centurylink-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/centurylink.png
layout: provider
modified: '2026-09-05'
name: CenturyLink (Lumen Technologies)
nav: Providers
network: true
overview: 'CenturyLink (Lumen Technologies) publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Broadband, Connectivity, Edge, Fiber, and Lumen.


  CenturyLink (Lumen Technologies)''s developer surface includes API reference, documentation, getting-started guide, support, engineering blog, authentication, and 20 more developer resources.'
plans:
- name: Centurylink Plans Pricing
  plan_count: 2
  slug: centurylink-plans-pricing
press:
- date: '2026-05-25'
  title: Press Releases
  url: https://www.blueplanet.com/about/press-releases
- date: '2026-05-25'
  title: How Lumen and Corning Are Enabling AI with Fiber
  url: https://blog.centurylink.com/from-glass-to-global-impact-how-lumen-and-corning-are-building-the-fiber-behind-ai-innovation/
- date: '2026-05-25'
  title: CenturyLink completes acquisition of Level 3
  url: https://www.prnewswire.com/news-releases/centurylink-completes-acquisition-of-level-3-300547357.html
- date: '2026-05-25'
  title: CenturyLink Data Center Sale Continues Trend
  url: https://www.telecompetitor.com/centurylink-data-center-sale-continues-telecom-data-center-divestiture-trend/
- date: '2026-05-25'
  title: Finance Press
  url: https://centurylink.net/finance/category/press
random_paper: 11
rate_limits:
- limit_count: 2
  name: Centurylink Rate Limits
  slug: centurylink-rate-limits
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 54.0
    catalog_earned_first_party: 16.0
    catalog_gap: 61.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 16.8
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 13.9
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 43.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/centurylink/refs/heads/main/screenshots/centurylink-2026-06-20T174132.png
security:
- kind: authentication
  name: Centurylink Authentication
  slug: centurylink-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Centurylink Domain Security
  slug: centurylink-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: centurylink
tags:
- Broadband
- Connectivity
- Edge
- Fiber
- Lumen
- Network
- Authentication
- Quantum Fiber
- SD-WAN
- Telecom
- Fortune 500
website: https://www.centurylink.com
---
