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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 16
  human_in_the_loop: 4
  name: Windstream Holdings Agentic Access
  operation_count: 38
  slug: windstream-holdings-agentic-access
  summary_line: 38 operations · 16 acting · 4 human-in-the-loop
api_count: 2
apis:
- description: Agent state management
  name: Windstream Holdings agents API
  slug: windstream-holdings-agents-api
- description: Auto-attendant configuration
  name: Windstream Holdings auto-attendants API
  slug: windstream-holdings-auto-attendants-api
- description: Call management and control
  name: Windstream Holdings calls API
  slug: windstream-holdings-calls-api
- description: Extension management
  name: Windstream Holdings extensions API
  slug: windstream-holdings-extensions-api
- description: Product catalog operations
  name: Windstream Holdings products API
  slug: windstream-holdings-products-api
- description: Role and permission management
  name: Windstream Holdings roles API
  slug: windstream-holdings-roles-api
- description: System-level operations
  name: Windstream Holdings system API
  slug: windstream-holdings-system-api
- description: Tenant management and configuration
  name: Windstream Holdings tenants API
  slug: windstream-holdings-tenants-api
- description: User account management
  name: Windstream Holdings users API
  slug: windstream-holdings-users-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Windstream Enterprise Contact Center Services API
  slug: open-windstream-contact-center
- collection_type: open
  name: Windstream Enterprise Contact Center Services agents API
  slug: open-windstream-holdings-agents-api
- collection_type: open
  name: Windstream Enterprise Contact Center Services agents auto-attendants API
  slug: open-windstream-holdings-auto-attendants-api
- collection_type: open
  name: Windstream Enterprise Contact Center Services agents calls API
  slug: open-windstream-holdings-calls-api
- collection_type: open
  name: Windstream Enterprise Contact Center Services agents extensions API
  slug: open-windstream-holdings-extensions-api
- collection_type: open
  name: Windstream Enterprise Contact Center Services agents products API
  slug: open-windstream-holdings-products-api
- collection_type: open
  name: Windstream Enterprise Contact Center Services agents roles API
  slug: open-windstream-holdings-roles-api
- collection_type: open
  name: Windstream Enterprise Contact Center Services agents system API
  slug: open-windstream-holdings-system-api
- collection_type: open
  name: Windstream Enterprise Contact Center Services agents tenants API
  slug: open-windstream-holdings-tenants-api
- collection_type: open
  name: Windstream Enterprise Contact Center Services agents users API
  slug: open-windstream-holdings-users-api
- collection_type: open
  name: Windstream Enterprise Voice API
  slug: open-windstream-voice
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/windstream-holdings-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/windstream-holdings-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/windstream-holdings-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/windstream-holdings-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.windstreamenterprise.com/
- group: start
  title: ''
  type: Portal
  url: https://api.solutions.uniti.com/
- group: other
  title: ''
  type: DeveloperHub
  url: https://solutions.uniti.com/developer-hub
- group: other
  title: ''
  type: APIMarketplace
  url: https://api.solutions.uniti.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.solutions.uniti.com/
- group: build
  title: ''
  type: SalesforcIntegration
  url: https://solutions.uniti.com/developer-hub/app-gallery/salesforce-api
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/windstream-enterprise
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/windstream-holdings/refs/heads/main/json-ld/windstream-holdings-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/windstream-holdings/refs/heads/main/vocabulary/windstream-holdings-vocabulary.yml
created: '2026-05-03'
description: Windstream Holdings is a leading provider of advanced network communications and technology solutions including managed services, cloud computing, and broadband to consumers and businesses across the United States. The company operates the Kinetic broadband brand for consumer and small business customers and Windstream Enterprise (now Uniti Solutions) for business customers, offering SD-WAN, UCaaS, OfficeSuite UC, contact center services, and high-capacity network transport. Windstream delivers voice, data, and managed networking solutions to more than 18 states with over 2.1 million fiber-to-the-premise passings.
examples:
- key_count: 6
  name: Windstream List Calls Example
  slug: windstream-list-calls-example
- key_count: 6
  name: Windstream Make Call Example
  slug: windstream-make-call-example
finops:
- name: Windstream Holdings Finops
  service_category: API
  slug: windstream-holdings-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/windstream-holdings.png
json_schemas:
- name: Call
  property_count: 8
  slug: windstream-call
- name: Extension
  property_count: 6
  slug: windstream-extension
jsonld:
- class_count: 14
  name: Windstream Holdings Context
  property_count: 13
  slug: windstream-holdings-context
layout: provider
modified: '2026-05-19'
name: Windstream Holdings
nav: Providers
network: true
overview: 'Windstream Holdings publishes 9 APIs on the [APIs.io](https://apis.io/) network, including agents API, auto-attendants API, calls API, and 6 more. Tagged areas include Broadband, Contact Center, Managed Service, Network Communications, and SD-WAN.


  The Windstream Holdings catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Windstream Holdings'' developer surface includes authentication, developer portal, documentation, and 10 more developer resources.'
plans:
- name: Windstream Holdings Plans Pricing
  plan_count: 3
  slug: windstream-holdings-plans-pricing
press:
- date: '2026-05-25'
  title: Windstream Enterprise and Talkdesk Partner to Deliver AI- ...
  url: https://news.windstream.com/news/news-details/2023/Windstream-Enterprise-and-Talkdesk-Partner-to-Deliver-AI-Powered-CCaaS-Solution/default.aspx
- date: '2026-05-25'
  title: Windstream Enterprise Launches Talkdesk Express for ...
  url: https://www.businesswire.com/news/home/20241118364771/en/Windstream-Enterprise-Launches-Talkdesk-Express-for-Small-and-Midsized-Businesses
- date: '2026-05-25'
  title: F-Secure, Windstream, and Actiontec win broadband marketing ...
  url: https://www.pressreleasepoint.com/f-secure-windstream-and-actiontec-win-broadband-marketing-award-connected-home-security-offering?lang=es
- date: '2026-05-25'
  title: Uniti Group completes the merger with Windstream Holdings II ...
  url: https://news.mergerlinks.com/daily-review/uniti-group-completes-the-merger-with-windstream-holdings-ii-in-a-$-13-4bn-deal
- date: '2026-05-25'
  title: Windstream Enterprise and Amazon Web Services ...
  url: https://news.windstream.com/news/news-details/2023/Windstream-Enterprise-and-Amazon-Web-Services-Advance-the-Virtual-Meeting-Experience-for-Businesses/default.aspx
random_paper: 13
rate_limits:
- limit_count: 5
  name: Windstream Holdings Rate Limits
  slug: windstream-holdings-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Windstream Holdings API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: windstream-holdings-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Windstream Holdings API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 2
  slug: windstream-holdings-rules
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 18
    catalog_gap: 48.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 60.9
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/windstream-holdings/refs/heads/main/screenshots/windstream-holdings-2026-06-20T201507.png
security:
- kind: authentication
  name: Windstream Holdings Authentication
  slug: windstream-holdings-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Windstream Holdings Domain Security
  slug: windstream-holdings-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: windstream-holdings
tags:
- Broadband
- Contact Center
- Managed Service
- Network Communications
- SD-WAN
- Telecom
- UCaaS
- Unified Communications
- Fortune 500
website: https://www.windstreamenterprise.com/
---
