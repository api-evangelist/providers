---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 49
  human_in_the_loop: 1
  name: Fluentedi Agentic Access
  operation_count: 99
  slug: fluentedi-agentic-access
  summary_line: 99 operations · 49 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://fluentedi.com
  baseurl_source: spec
  description: Calculation and conversion
  name: FluentEDI Compute API
  slug: fluentedi-compute-api
- baseURL: https://fluentedi.com
  baseurl_source: spec
  description: Hashing, signatures, encoding and identifiers
  name: FluentEDI Crypto API
  slug: fluentedi-crypto-api
- baseURL: https://fluentedi.com
  baseurl_source: spec
  description: JSON and tabular data
  name: FluentEDI Data API
  slug: fluentedi-data-api
- baseURL: https://fluentedi.com
  baseurl_source: spec
  description: Documents (PDF, Word, Excel)
  name: FluentEDI Doc API
  slug: fluentedi-doc-api
- baseURL: https://fluentedi.com
  baseurl_source: spec
  description: EDI and retail supply chain (X12)
  name: FluentEDI Edi API
  slug: fluentedi-edi-api
- baseURL: https://fluentedi.com
  baseurl_source: spec
  description: Finding your way around
  name: FluentEDI Meta API
  slug: fluentedi-meta-api
- baseURL: https://fluentedi.com
  baseurl_source: spec
  description: Scheduling
  name: FluentEDI Schedule API
  slug: fluentedi-schedule-api
- baseURL: https://fluentedi.com
  baseurl_source: spec
  description: Text
  name: FluentEDI Text API
  slug: fluentedi-text-api
- baseURL: https://fluentedi.com
  baseurl_source: spec
  description: Time, dates and windows
  name: FluentEDI Time API
  slug: fluentedi-time-api
- baseURL: https://fluentedi.com
  baseurl_source: spec
  description: Web and network
  name: FluentEDI Web API
  slug: fluentedi-web-api
artifact_total: 22
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://fluentedi.com/llms.txt
- group: company
  title: ''
  type: BlogRSS
  url: https://www.fluentedi.com/feed.xml
- group: agent
  title: ''
  type: MCPServer
  url: https://fluentedi.com/mcp
- group: agent
  href: https://artifacts.apis.io/fluentedi/mcp/fluentedi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fluentedi-mcp.yml
- group: other
  href: https://artifacts.apis.io/fluentedi/overlays/fluentedi-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fluentedi-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.fluentedi.com/
- group: auth
  href: https://artifacts.apis.io/fluentedi/security/fluentedi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fluentedi-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/fluentedi/well-known/fluentedi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fluentedi-well-known.yml
- group: auth
  href: https://artifacts.apis.io/fluentedi/authentication/fluentedi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fluentedi-authentication.yml
- group: design
  href: https://artifacts.apis.io/fluentedi/errors/fluentedi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fluentedi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fluentedi/conventions/fluentedi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fluentedi-conventions.yml
- group: design
  href: https://artifacts.apis.io/fluentedi/conventions/fluentedi-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/fluentedi-conventions.yml
- group: design
  href: https://artifacts.apis.io/fluentedi/lifecycle/fluentedi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fluentedi-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://fluentedi.com/health
- group: design
  href: https://artifacts.apis.io/fluentedi/conformance/fluentedi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fluentedi-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/fluentedi/plans/fluentedi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fluentedi-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/fluentedi/rate-limits/fluentedi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fluentedi-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/fluentedi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/fluentedi/agentic-access/fluentedi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fluentedi-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fluentedi.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fluentedi.com/privacy
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mastermanas805/fluentedi-mcp
created: '2026-09-03'
description: 45 deterministic tools for AI agents, free and with no API key, signup or rate limit. Every tool is a single stateless GET or POST returning JSON, read-only and idempotent. Coverage runs deepest in retail EDI -- X12 850/856/810/855/997 parsing, generating an 856 with correct HL parent pointers and a fixed-width 106-character ISA, envelope validation, decoding a 997 acknowledgment into plain language, and GS1 check digits -- alongside timezone and delivery-window arithmetic, cron, exact maths, JSON repair with line/column error localisation, JSONPath, RFC 8785 canonical JSON with CIDv1, Ed25519/ECDSA/RSA signature verification, secret and PII scanning, link-liveness checking with retraction detection, endpoint assertion, and text position conversion.
image: https://fluentedi.com/favicon.svg
layout: provider
mcp_servers:
- description: ''
  name: FluentEDI MCP Server
  slug: mcp
modified: '2026-10-06'
name: FluentEDI
nav: Providers
network: true
overview: 'FluentEDI publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Compute API, Crypto API, Data API, and 7 more. Tagged areas include EDI, X12, Retail EDI, AI Agents, and MCP.


  The FluentEDI catalog on APIs.io includes 1 Spectral governance ruleset.


  FluentEDI''s developer surface includes pricing, authentication, GitHub presence, and 19 more developer resources.'
plans:
- name: Fluentedi Plans Pricing
  plan_count: 1
  slug: fluentedi-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Fluentedi Rate Limits
  slug: fluentedi-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: FluentEDI API Rules
  rule_count: 50
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 3
  slug: fluentedi-rules
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 26
    catalog_earned: 41.5
    catalog_earned_first_party: 8.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 55.1
    developer_ergonomics: 39.9
    discoverability: 71.7
    operational_transparency: 13.2
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fluentedi/fluentedi-2026-10-11T104557.png
security:
- kind: authentication
  name: Fluentedi Authentication
  slug: fluentedi-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Fluentedi Domain Security
  slug: fluentedi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
skill_count: 5
skills:
- name: fluentedi-build-856-asn
  slug: fluentedi-build-856-asn
- name: fluentedi-decode-997-acknowledgment
  slug: fluentedi-decode-997-acknowledgment
- name: fluentedi-delivery-window-arithmetic
  slug: fluentedi-delivery-window-arithmetic
- name: fluentedi-repair-and-hash-json
  slug: fluentedi-repair-and-hash-json
- name: fluentedi-scan-agent-output-for-leaks
  slug: fluentedi-scan-agent-output-for-leaks
slug: fluentedi
tags:
- EDI
- X12
- Retail EDI
- AI Agents
- MCP
- Developer Tools
- JSON
- Cryptography
- Data Validation
- Supply Chain
website: https://www.fluentedi.com/
---
