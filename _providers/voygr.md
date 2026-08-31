---
access_model:
  confidence: high
  label: Self-Service
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://api.voygr.tech/checkout
  - https://api.voygr.tech/checkout/packs
  - https://api.voygr.tech/docs
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.1
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Programmatic outbound phone calls executed by an AI voice agent. Submit a task either as a plain-language brief or as a structured intent plus slots (inquiry, info_gathering, issue_resolution, booking
  name: Voygr Calls API
  slug: voygr-calls-api
- description: Business existence and operating-status validation. POST /v1/business-status takes a business name and a full street address and returns existence_status (exists, not_exists, uncertain) and open_close
  name: Voygr Business Validation API
  slug: voygr-business-validation-api
- description: The core API from VOYGR — 2 operation(s) for core.
  name: VOYGR Core API
  slug: voygr-core-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://voygr.tech/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.voygr.tech/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.voygr.tech/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.voygr.tech/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/voygr-tech/callwright-skill#readme
- group: start
  title: ''
  type: SignUp
  url: https://api.voygr.tech/checkout
- group: commercial
  title: ''
  type: Pricing
  url: https://api.voygr.tech/checkout
- group: commercial
  title: ''
  type: Plans
  url: plans/voygr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/voygr-rate-limits.yml
- group: operate
  title: ''
  type: Support
  url: mailto:support@voygr.tech
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/voygr-tech
- group: build
  title: ''
  type: SDKs
  url: packages/voygr-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/voygr-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/voygr-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/voygr-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/voygr-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/voygr-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voygr-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://voygr.tech/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://voygr.tech/terms
- group: commercial
  title: ''
  type: TermsOfService
  url: https://voygr.tech/terms-api
created: '2026-07-17'
description: VOYGR provides real-world place intelligence for AI apps and agents, delivering continuous location and point-of-interest (POI) data validation and enrichment. Its Location Freshness Validation confirms historical existence and current operating status, detecting relocations, rebrands, and closures across multiple attributes with up to 99.62% validation precision and configurable decision thresholds. Its Location Data Enrichment populates and continuously enriches place records from web, social, authoritative, and other sources, spanning foundational attributes (address, contacts, web presence), operating data (hours, menus, prices), and fresh context (articles, reviews, news, events). Two APIs are public and self-serve. The Voygr Calls API (api.voygr.tech) places real outbound phone calls with an AI voice agent — submit a task, the agent dials, conducts the conversation, and returns a structured outcome with a full transcript — which is how VOYGR reaches the businesses that
  have a phone but no API. The Voygr Business Validation API (dev.voygr.tech) returns existence and open/closed status for a business name and address. Both authenticate with an X-API-Key header, share one prepaid credit balance, and issue keys self-serve by email. VOYGR is a Y Combinator (Winter 2026) and SNR.VC backed seed-stage company based in San Francisco, founded by Vlad Baskakov (CEO, ex-Google Maps) and Yarik Markov (CTO, ex-Google/Meta/Apple ML). Its maps API goes beyond the 10-15 standard attributes of existing mapping providers. The location-data products themselves remain demo-gated on voygr.tech, but the calling and validation APIs are documented, priced, and reachable without a sales conversation.
image: https://framerusercontent.com/images/AwhsRnVKsS6stDyzf60Vzj7jew.png
layout: provider
modified: '2026-08-14'
name: VOYGR
nav: Providers
network: true
overview: 'VOYGR publishes 2 APIs on the [APIs.io](https://apis.io/) network: Calls API and Core API. Tagged areas include Company, Location Intelligence, POI Data, Data Enrichment, and Data Validation.


  VOYGR''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, support, CLI, and 15 more developer resources.'
plans:
- name: Voygr Plans Pricing
  plan_count: 4
  slug: voygr-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Voygr Rate Limits
  slug: voygr-rate-limits
score:
  band: strong
  composite: 55.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 52.7
    developer_ergonomics: 76.2
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 56.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/voygr/refs/heads/main/screenshots/voygr-2026-08-17T082827.png
security:
- kind: authentication
  name: Voygr Authentication
  slug: voygr-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Voygr Domain Security
  slug: voygr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: voygr
tags:
- Company
- Location Intelligence
- POI Data
- Data Enrichment
- Data Validation
- Geospatial
- Places
- AI Agents
- Agent Skills
- Voice AI
- Telephony
- Outbound Calls
- Business Validation
- Y Combinator
website: https://voygr.tech/
---
