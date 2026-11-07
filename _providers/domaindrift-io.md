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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Domaindrift Io Agentic Access
  operation_count: 13
  slug: domaindrift-io-agentic-access
  summary_line: 13 operations · 4 acting
api_count: 1
apis:
- baseURL: https://domaindrift.io
  baseurl_source: declared
  description: The Alerts API from DomainDrift — 2 operation(s) for alerts.
  name: DomainDrift Alerts API
  slug: domaindrift-io-alerts-api
- baseURL: https://domaindrift.io
  baseurl_source: declared
  description: The Changes API from DomainDrift — 1 operation(s) for changes.
  name: DomainDrift Changes API
  slug: domaindrift-io-changes-api
- baseURL: https://domaindrift.io
  baseurl_source: declared
  description: The Domains API from DomainDrift — 5 operation(s) for domains.
  name: DomainDrift Domains API
  slug: domaindrift-io-domains-api
- baseURL: https://domaindrift.io
  baseurl_source: declared
  description: The Health API from DomainDrift — 1 operation(s) for health.
  name: DomainDrift Health API
  slug: domaindrift-io-health-api
- baseURL: https://domaindrift.io
  baseurl_source: declared
  description: The Scan API from DomainDrift — 1 operation(s) for scan.
  name: DomainDrift Scan API
  slug: domaindrift-io-scan-api
- baseURL: https://domaindrift.io
  baseurl_source: declared
  description: The Stream API from DomainDrift — 1 operation(s) for stream.
  name: DomainDrift Stream API
  slug: domaindrift-io-stream-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/domaindrift-io/agentic-access/domaindrift-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/domaindrift-io-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/domaindrift-io/rules/domaindrift-io-rules.yml
  title: ''
  type: Spectral
  url: rules/domaindrift-io-rules.yml
- group: design
  href: https://artifacts.apis.io/domaindrift-io/json-ld/domaindrift-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/domaindrift-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/domaindrift-io/vocabulary/domaindrift-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/domaindrift-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/domaindrift-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/domaindrift-io/data-model/domaindrift-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/domaindrift-io-data-model.yml
- group: auth
  href: https://artifacts.apis.io/domaindrift-io/authentication/domaindrift-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/domaindrift-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/domaindrift-io/errors/domaindrift-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/domaindrift-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/domaindrift-io/conformance/domaindrift-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/domaindrift-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/domaindrift-io/llms/domaindrift-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/domaindrift-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/domaindrift-io/well-known/domaindrift-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/domaindrift-io-security.txt
- group: agent
  href: https://artifacts.apis.io/domaindrift-io/well-known/domaindrift-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/domaindrift-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/domaindrift-io/hosts/domaindrift-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/domaindrift-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/domaindrift-io/vendors/domaindrift-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/domaindrift-io-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://domaindrift.io/security
- group: start
  title: ''
  type: Sandbox
  url: https://domaindrift.io/playground
- group: start
  title: ''
  type: DeveloperPortal
  url: https://domaindrift.io/for/developers
- group: company
  title: ''
  type: Blog
  url: https://domaindrift.io/blog
- group: auth
  href: https://artifacts.apis.io/domaindrift-io/security/domaindrift-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/domaindrift-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/domaindrift-io/security/domaindrift-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/domaindrift-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://domaindrift.io/
- group: docs
  title: ''
  type: Documentation
  url: https://domaindrift.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://domaindrift.io/api
- group: start
  title: ''
  type: GettingStarted
  url: https://domaindrift.io/docs/getting-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://domaindrift.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://domaindrift.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://domaindrift.io/pricing
created: '2026-11-05'
description: DomainDrift provides verifiable internet telemetry by continuously scanning and signing observations of domain infrastructure changes. It offers a keyless API to retrieve domain data such as DNS, mail, certificate, and reachability, with each observation cryptographically signed and timestamped on-chain. The platform helps organizations detect look‑alike domains, monitor vendor posture, and automate security and compliance workflows.
image: https://domaindrift.io/og/home.png
json_schemas:
- name: DeltaChange
  property_count: 5
  slug: domaindrift-io-delta-change
- name: DomainSummary
  property_count: 13
  slug: domaindrift-io-domain-summary
- name: ProvenanceReceipt
  property_count: 7
  slug: domaindrift-io-provenance-receipt
jsonld:
- class_count: 4
  name: Domaindrift Io Context
  property_count: 25
  slug: domaindrift-io-context
layout: provider
modified: '2026-11-05'
name: DomainDrift
nav: Providers
network: true
overview: 'DomainDrift publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alerts API, Changes API, Domains API, and 3 more. Tagged areas include Security, Monitoring, Domain, and Telemetry.


  The DomainDrift catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DomainDrift''s developer surface includes authentication, sandbox, engineering blog, documentation, API reference, getting-started guide, pricing, and 20 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: DomainDrift API Rules
  rule_count: 39
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 2
  slug: domaindrift-io-rules
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 59.7
    developer_ergonomics: 66.0
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Domaindrift Io Authentication
  slug: domaindrift-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Domaindrift Io Domain Security
  slug: domaindrift-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Domaindrift Io Vulnerability Disclosure
  slug: domaindrift-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: domaindrift-io
tags:
- Security
- Monitoring
- Domain
- Telemetry
website: https://domaindrift.io/
---
