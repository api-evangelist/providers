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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for AskYourStack, providing endpoints for server management, SEO automation, and AI integration as documented.
  name: AskYourStack API
  slug: askyourstack-api
- description: 'AskYourStack API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: AskYourStack API
  slug: askyourstack-com-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/askyourstack-com/rules/askyourstack-com-rules.yml
  title: ''
  type: Spectral
  url: rules/askyourstack-com-rules.yml
- group: design
  href: https://artifacts.apis.io/askyourstack-com/vocabulary/askyourstack-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/askyourstack-com-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/askyourstack-com/changelog/askyourstack-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/askyourstack-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/askyourstack-com/conformance/askyourstack-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/askyourstack-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/askyourstack-com/llms/askyourstack-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/askyourstack-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/askyourstack-com/well-known/askyourstack-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/askyourstack-com-security.txt
- group: agent
  href: https://artifacts.apis.io/askyourstack-com/well-known/askyourstack-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/askyourstack-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/askyourstack-com/hosts/askyourstack-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/askyourstack-com-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://askyourstack.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://askyourstack.com/privacy
- group: start
  title: ''
  type: Login
  url: https://askyourstack.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://askyourstack.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://askyourstack.com/vps-setup
- group: auth
  href: https://artifacts.apis.io/askyourstack-com/security/askyourstack-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/askyourstack-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/askyourstack-com/security/askyourstack-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/askyourstack-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://askyourstack.com/
- group: docs
  title: ''
  type: Documentation
  url: https://askyourstack.com/docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://askyourstack.com/terms
coverage:
  checked: '2026-11-02'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found despite probing known locations.
  evidence:
  - status: 0
    url: https://api.askyourstack.com/openapi.json
  - status: 0
    url: https://api.askyourstack.com/openapi.yaml
  - status: 0
    url: https://api.askyourstack.com/swagger.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AskYourStack provides AI-driven server management and SEO automation, allowing users to connect large language models like Claude, ChatGPT, or Cursor to their Linux servers. The platform offers tools for installing and managing Magento, WordPress, and other web applications, handling backups, security hardening, and SEO tasks through natural language commands. It features open-source agents, a simple one-line installation, and flexible pricing plans, catering to developers and businesses seeking automated infrastructure and SEO workflows.
image: https://askyourstack.com/opengraph-image
layout: provider
modified: '2026-11-01'
name: AskYourStack
nav: Providers
network: true
overview: 'AskYourStack is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Server Management, SEO, and Automation.


  The AskYourStack catalog on APIs.io includes 1 Spectral governance ruleset.


  AskYourStack''s developer surface includes changelog, getting-started guide, documentation, and 15 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: AskYourStack API Rules
  rule_count: 19
  severity_counts:
    error: 17
    hint: 0
    info: 1
    warn: 1
  slug: askyourstack-com-rules
score:
  band: emerging
  composite: 21.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 17.1
    contract_governance: 35.6
    contract_quality: 9.4
    developer_ergonomics: 10.7
    discoverability: 57.1
    operational_transparency: 13.2
  previous_composite: 28.8
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Askyourstack Com Domain Security
  slug: askyourstack-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Askyourstack Com Vulnerability Disclosure
  slug: askyourstack-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: askyourstack-com
tags:
- Company
- Artificial Intelligence
- Server Management
- SEO
- Automation
website: https://askyourstack.com/
---
