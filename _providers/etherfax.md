---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Etherfax Agentic Access
  operation_count: 23
  slug: etherfax-agentic-access
  summary_line: 23 operations · 4 acting
api_count: 1
apis:
- baseURL: https://na.connect.etherfax.net/rest/3.0/api
  baseurl_source: declared
  description: The Accounts API from etherFAX — 2 operation(s) for accounts.
  name: etherFAX Accounts API
  slug: etherfax-accounts-api
- baseURL: https://na.connect.etherfax.net/rest/3.0/api
  baseurl_source: declared
  description: The Devices API from etherFAX — 8 operation(s) for devices.
  name: etherFAX Devices API
  slug: etherfax-devices-api
- baseURL: https://na.connect.etherfax.net/rest/3.0/api
  baseurl_source: declared
  description: The Inbox API from etherFAX — 5 operation(s) for inbox.
  name: etherFAX Inbox API
  slug: etherfax-inbox-api
- baseURL: https://na.connect.etherfax.net/rest/3.0/api
  baseurl_source: declared
  description: The Outbox API from etherFAX — 1 operation(s) for outbox.
  name: etherFAX Outbox API
  slug: etherfax-outbox-api
- baseURL: https://na.connect.etherfax.net/rest/3.0/api
  baseurl_source: declared
  description: The Routes API from etherFAX — 4 operation(s) for routes.
  name: etherFAX Routes API
  slug: etherfax-routes-api
- baseURL: https://na.connect.etherfax.net/rest/3.0/api
  baseurl_source: declared
  description: The Status API from etherFAX — 1 operation(s) for status.
  name: etherFAX Status API
  slug: etherfax-status-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/etherfax/vocabulary/etherfax-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/etherfax-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/etherfax/well-known/etherfax-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/etherfax-status-security.txt
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.etherfax.net/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.etherfax.net/reference
- group: agent
  href: https://artifacts.apis.io/etherfax/agentic-access/etherfax-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/etherfax-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/etherfax/rules/etherfax-rules.yml
  title: ''
  type: Spectral
  url: rules/etherfax-rules.yml
- group: agent
  href: https://artifacts.apis.io/etherfax/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.etherfax.net/security/
- group: design
  href: https://artifacts.apis.io/etherfax/errors/etherfax-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/etherfax-problem-types.yml
- group: design
  href: https://artifacts.apis.io/etherfax/conformance/etherfax-conformance.yml
  title: ''
  type: Conformance
  url: conformance/etherfax-conformance.yml
- group: agent
  href: https://artifacts.apis.io/etherfax/llms/etherfax-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/etherfax-llms.txt
- group: agent
  href: https://artifacts.apis.io/etherfax/well-known/etherfax-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/etherfax-well-known.yml
- group: other
  href: https://artifacts.apis.io/etherfax/hosts/etherfax-hosts.yml
  title: ''
  type: Hosts
  url: hosts/etherfax-hosts.yml
- group: other
  href: https://artifacts.apis.io/etherfax/vendors/etherfax-vendors.yml
  title: ''
  type: Vendors
  url: vendors/etherfax-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.etherfax.net/terms-conditions/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.etherfax.net/
- group: auth
  title: ''
  type: Security
  url: https://www.etherfax.net/security/
- group: company
  title: ''
  type: Newsroom
  url: https://www.etherfax.net/news/
- group: start
  title: ''
  type: Login
  url: https://www.etherfax.net/login/
- group: other
  title: ''
  type: Leadership
  url: https://www.etherfax.net/about/team/
- group: auth
  href: https://artifacts.apis.io/etherfax/authentication/etherfax-authentication.yml
  title: ''
  type: Authentication
  url: authentication/etherfax-authentication.yml
- group: auth
  href: https://artifacts.apis.io/etherfax/security/etherfax-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/etherfax-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/etherfax/security/etherfax-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/etherfax-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.etherfax.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.etherfax.net/developer-apis/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.etherfax.net/
- group: company
  title: ''
  type: Blog
  url: https://www.etherfax.net/blogs/
- group: operate
  title: ''
  type: Support
  url: https://www.etherfax.net/support/
coverage:
  checked: '2026-10-27'
  detail: Documentation site renders OpenAPI spec behind a JavaScript app, preventing machine-readable retrieval.
  evidence:
  - status: 200
    url: https://docs.etherfax.net/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: etherFAX provides secure, cloud-based faxing solutions powered by AI-driven document workflows. Serving government, commercial, and healthcare sectors, it offers FedRAMP-certified and HIPAA-compliant services. The platform enables sending and receiving faxes directly from desktop applications, integrating with various enterprise systems, and automating document exchange processes.
image: https://www.etherfax.net/wp-content/uploads/2026/06/EF-HomePageRefresh26-FeaturedImage2.webp
layout: provider
modified: '2026-10-26'
name: etherFAX
nav: Providers
network: true
overview: 'etherFAX publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Devices API, Inbox API, and 3 more. Tagged areas include Fax, Cloud, Artificial Intelligence, Secure, and Document Automation.


  The etherFAX catalog on APIs.io includes 1 Spectral governance ruleset.


  etherFAX''s developer surface includes changelog, API reference, authentication, documentation, engineering blog, support, and 22 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: etherFAX API Rules
  rule_count: 46
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 1
  slug: etherfax-rules
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 23.7
    contract_governance: 22.0
    contract_quality: 57.1
    developer_ergonomics: 33.9
    discoverability: 66.1
    operational_transparency: 28.9
  previous_composite: 41.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/etherfax/etherfax-2026-11-03T131631.png
security:
- kind: authentication
  name: Etherfax Authentication
  slug: etherfax-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Etherfax Domain Security
  slug: etherfax-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Etherfax Trust Center
  slug: etherfax-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR
skill_count: 1
skills:
- name: etherfax-manage-devices
  slug: etherfax-manage-devices
slug: etherfax
tags:
- Fax
- Cloud
- Artificial Intelligence
- Secure
- Document Automation
website: https://www.etherfax.net/
---
