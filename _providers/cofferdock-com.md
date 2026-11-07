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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 48
  human_in_the_loop: 1
  name: Cofferdock Com Agentic Access
  operation_count: 50
  slug: cofferdock-com-agentic-access
  summary_line: 50 operations · 48 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.cofferdock.com
  baseurl_source: declared
  description: Plan and credits.
  name: Cofferdock Account API
  slug: cofferdock-com-account-api
- baseURL: https://api.cofferdock.com
  baseurl_source: declared
  description: Small helpers for workflows.
  name: Cofferdock Data API
  slug: cofferdock-com-data-api
- baseURL: https://api.cofferdock.com
  baseurl_source: declared
  description: Convert between document and data formats.
  name: Cofferdock Documents API
  slug: cofferdock-com-documents-api
- baseURL: https://api.cofferdock.com
  baseurl_source: declared
  description: Zips and temporary downloads.
  name: Cofferdock Files API
  slug: cofferdock-com-files-api
- baseURL: https://api.cofferdock.com
  baseurl_source: declared
  description: Create or transform images.
  name: Cofferdock Images API
  slug: cofferdock-com-images-api
- baseURL: https://api.cofferdock.com
  baseurl_source: declared
  description: Create and edit PDFs.
  name: Cofferdock PDF API
  slug: cofferdock-com-pdf-api
- baseURL: https://api.cofferdock.com
  baseurl_source: declared
  description: Check emails, phones and IBANs.
  name: Cofferdock Validation API
  slug: cofferdock-com-validation-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/cofferdock-com/agentic-access/cofferdock-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cofferdock-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/cofferdock-com/rules/cofferdock-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cofferdock-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cofferdock-com/vocabulary/cofferdock-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cofferdock-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cofferdock-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/cofferdock-com/authentication/cofferdock-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cofferdock-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/cofferdock-com/errors/cofferdock-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cofferdock-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cofferdock-com/conformance/cofferdock-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cofferdock-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cofferdock-com/llms/cofferdock-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cofferdock-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/cofferdock-com/well-known/cofferdock-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cofferdock-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cofferdock-com/hosts/cofferdock-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cofferdock-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cofferdock.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cofferdock.com/privacy
- group: start
  title: ''
  type: Login
  url: https://cofferdock.com/login
- group: company
  title: ''
  type: Blog
  url: https://cofferdock.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.cofferdock.com</code
- group: docs
  title: ''
  type: APIReference
  url: https://cofferdock.com/html-to-image
- group: auth
  href: https://artifacts.apis.io/cofferdock-com/security/cofferdock-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cofferdock-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cofferdock.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://cofferdock.com/openapi.json
  - status: null
    url: https://api.cofferdock.com/openapi.json
  - status: 401
    url: https://cofferdock.com/mcp
  - status: 401
    url: https://api.cofferdock.com/mcp
  - status: 200
    url: https://cofferdock.com/
  reason: partner-login
  state: gated
created: '2026-11-04'
description: 'cofferdock-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://cofferdock.com/static/og.png
layout: provider
modified: '2026-11-04'
name: Cofferdock
nav: Providers
network: true
overview: 'Cofferdock publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Data API, Documents API, and 4 more. Tagged areas include QR Codes, Screenshots, and Automation.


  The Cofferdock catalog on APIs.io includes 1 Spectral governance ruleset.


  Cofferdock''s developer surface includes authentication, engineering blog, API reference, and 15 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Cofferdock API Rules
  rule_count: 65
  severity_counts:
    error: 57
    hint: 0
    info: 1
    warn: 7
  slug: cofferdock-com-rules
score:
  band: thin
  composite: 35.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.8
    catalog_earned_first_party: 0.0
    catalog_gap: 82.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 51.7
    developer_ergonomics: 32.7
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cofferdock Com Authentication
  slug: cofferdock-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cofferdock Com Domain Security
  slug: cofferdock-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: html-to-image
  slug: cofferdock-com-html-to-image
slug: cofferdock-com
tags:
- QR Codes
- Screenshots
- Automation
website: https://cofferdock.com/
---
