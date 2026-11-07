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
    agent_skills: derived
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Caspchecklist Com Agentic Access
  operation_count: 8
  slug: caspchecklist-com-agentic-access
  summary_line: 8 operations · 7 acting
api_count: 1
apis:
- baseURL: https://caspchecklist.com
  baseurl_source: declared
  description: enquiry
  name: CASP Checklist Enquiry API
  slug: caspchecklist-com-enquiry-api
- baseURL: https://caspchecklist.com
  baseurl_source: declared
  description: checker
  name: CASP Checklist Guide API
  slug: caspchecklist-com-guide-api
- baseURL: https://caspchecklist.com
  baseurl_source: declared
  description: The mcp API from CASP Checklist — 1 operation(s) for mcp.
  name: CASP Checklist MCP API
  slug: caspchecklist-com-mcp-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/caspchecklist-com/agentic-access/caspchecklist-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/caspchecklist-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/caspchecklist-com/rules/caspchecklist-com-rules.yml
  title: ''
  type: Spectral
  url: rules/caspchecklist-com-rules.yml
- group: design
  href: https://artifacts.apis.io/caspchecklist-com/vocabulary/caspchecklist-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/caspchecklist-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/caspchecklist-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://caspchecklist.com/terms
- group: design
  href: https://artifacts.apis.io/caspchecklist-com/errors/caspchecklist-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/caspchecklist-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/caspchecklist-com/conformance/caspchecklist-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/caspchecklist-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/caspchecklist-com/llms/caspchecklist-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/caspchecklist-com-llms.txt
- group: build
  href: https://artifacts.apis.io/caspchecklist-com/mcp/caspchecklist-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/caspchecklist-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/caspchecklist-com/mcp/caspchecklist-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/caspchecklist-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/caspchecklist-com/well-known/caspchecklist-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/caspchecklist-com-security.txt
- group: agent
  href: https://artifacts.apis.io/caspchecklist-com/well-known/caspchecklist-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/caspchecklist-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/caspchecklist-com/hosts/caspchecklist-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caspchecklist-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/caspchecklist-com/vendors/caspchecklist-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caspchecklist-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://caspchecklist.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://caspchecklist.com/privacy/
- group: auth
  href: https://artifacts.apis.io/caspchecklist-com/authentication/caspchecklist-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/caspchecklist-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/caspchecklist-com/security/caspchecklist-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/caspchecklist-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/caspchecklist-com/security/caspchecklist-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caspchecklist-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caspchecklist.com/
created: '2026-11-04'
description: CASP Checklist provides a comprehensive authorisation checklist for crypto‑asset service providers (CASPs) under the EU MiCA regulation, detailing capital requirements, service classifications, application documentation, and compliance guidance across multiple EU jurisdictions.
image: https://caspchecklist.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at caspchecklist.com.
  name: CASP Checklist MCP Server
  slug: caspchecklist-com-mcp-yml
modified: '2026-11-04'
name: CASP Checklist
nav: Providers
network: true
overview: 'CASP Checklist publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Enquiry API, Guide API, and MCP API. Tagged areas include Company, Cryptocurrency, EU, MiCA, and Compliance.


  The CASP Checklist catalog on APIs.io includes 1 Spectral governance ruleset.


  CASP Checklist''s developer surface includes authentication and 19 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: CASP Checklist API Rules
  rule_count: 49
  severity_counts:
    error: 43
    hint: 0
    info: 5
    warn: 1
  slug: caspchecklist-com-rules
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 48.8
    developer_ergonomics: 13.7
    discoverability: 65.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
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
  name: Caspchecklist Com Authentication
  slug: caspchecklist-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Caspchecklist Com Domain Security
  slug: caspchecklist-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Caspchecklist Com Vulnerability Disclosure
  slug: caspchecklist-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: caspchecklist-com-enquiry-process
  slug: caspchecklist-com-enquiry-process
- name: caspchecklist-com-guide-checker-flow
  slug: caspchecklist-com-guide-checker-flow
slug: caspchecklist-com
tags:
- Company
- Cryptocurrency
- EU
- MiCA
- Compliance
website: https://caspchecklist.com/
---
