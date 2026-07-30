---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.8
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: JSON/REST API for hotels and PMS/channel-manager systems to push availability, rates and inventory (ARI), manage property, room, rate-plan and channel configuration, and exchange reservations across 5
  name: DerbySoft Property Connector Integration API
  slug: derbysoft-property-connector-integration-api
- description: OTA 2016B XML API for distributors (OTAs, metasearch, corporate travel, travel agencies) to access hotel content in DerbySoft Content Solutions via OTA_HotelSearchRQ/RS and OTA_HotelDescriptiveInfoRQ/
  name: DerbySoft Content Distributor API
  slug: derbysoft-content-distributor-api
- description: API for property-industry suppliers to query and write hotel content — property information, guestrooms, and rate plans — into DerbySoft Content Solutions using GET and POST operations.
  name: DerbySoft Content Supplier API
  slug: derbysoft-content-supplier-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.derbysoft.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://pc.knowledgebase.derbysoftsec.com/support/home
- group: docs
  title: ''
  type: Documentation
  url: https://contentsolutions.knowledgebase.derbysoftsec.com/support/home
- group: docs
  title: ''
  type: APIReference
  url: https://pc.knowledgebase.derbysoftsec.com/en/support/solutions/articles/70000157127-api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://pc.knowledgebase.derbysoftsec.com/en/support/solutions/articles/70000157120-overview
- group: operate
  title: ''
  type: Support
  url: https://www.derbysoft.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.derbysoft.com/resources/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.derbysoft.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.derbysoft.com/legal/
- group: auth
  title: ''
  type: Authentication
  url: authentication/derbysoft-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/derbysoft-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/derbysoft-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/derbysoft-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/derbysoft-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/derbysoft-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/derbysoft-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/derbysoft-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/derbysoft-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/derbysoft-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/derbysoft-llms.txt
created: '2026-07-17'
description: 'DerbySoft is a global travel-technology company — "The Travel Commerce Accelerator" — that provides high-performance distribution connectivity, content management, and digital-marketing services to the travel industry. Founded in 2002 and operating worldwide, DerbySoft connects hotel suppliers, channel managers, OTAs, metasearch engines, and TMCs through standardized APIs: a JSON/REST Property Connector Integration API for pushing rates, availability, inventory and reservations across 500+ channels, and OTA 2016B-based Content Distributor and Content Supplier APIs for querying and writing hotel content (properties, guestrooms, rate plans, images). The platform also covers streamlined connectivity, business-travel and flight distribution, and AI-driven marketing. This profile was enriched from DerbySoft''s public developer knowledge bases.'
image: https://www.derbysoft.com/wp-content/uploads/2026/03/DS-home-1.png
layout: provider
modified: '2026-07-18'
name: DerbySoft
nav: Providers
network: true
overview: 'DerbySoft publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Travel, Hospitality, and Hotels.


  DerbySoft''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 13 more developer resources.'
random_paper: 76
rate_limits:
- limit_count: 1
  name: Derbysoft Rate Limits
  slug: derbysoft-rate-limits
score:
  band: thin
  composite: 32.1
  delta: 1.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 83.3
    governance: 12.5
    operational_transparency: 36.8
  previous_composite: 31.1
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/derbysoft/refs/heads/main/screenshots/derbysoft-2026-07-25T211736.png
security:
- kind: authentication
  name: Derbysoft Authentication
  slug: derbysoft-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Derbysoft Domain Security
  slug: derbysoft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: derbysoft
tags:
- Company
- Enterprise
- Travel
- Hospitality
- Hotels
- Distribution
- Connectivity
- Content
- Channel Management
- Travel Technology
website: https://www.derbysoft.com/
---
