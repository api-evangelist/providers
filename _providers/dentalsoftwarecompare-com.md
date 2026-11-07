---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Dentalsoftwarecompare Com Agentic Access
  operation_count: 8
  slug: dentalsoftwarecompare-com-agentic-access
  summary_line: 8 operations · 7 acting
api_count: 1
apis:
- baseURL: https://dentalsoftwarecompare.com
  baseurl_source: declared
  description: enquiry
  name: Dental Software Compare Enquiry API
  slug: dentalsoftwarecompare-com-enquiry-api
- baseURL: https://dentalsoftwarecompare.com
  baseurl_source: declared
  description: compare
  name: Dental Software Compare Guide API
  slug: dentalsoftwarecompare-com-guide-api
- baseURL: https://dentalsoftwarecompare.com
  baseurl_source: declared
  description: The mcp API from Dental Software Compare — 1 operation(s) for mcp.
  name: Dental Software Compare MCP API
  slug: dentalsoftwarecompare-com-mcp-api
artifact_total: 13
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://dentalsoftwarecompare.com/mcp
- group: agent
  href: https://artifacts.apis.io/dentalsoftwarecompare-com/agentic-access/dentalsoftwarecompare-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dentalsoftwarecompare-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/dentalsoftwarecompare-com/rate-limits/dentalsoftwarecompare-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dentalsoftwarecompare-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dentalsoftwarecompare-com/plans/dentalsoftwarecompare-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dentalsoftwarecompare-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dentalsoftwarecompare-com/rules/dentalsoftwarecompare-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dentalsoftwarecompare-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dentalsoftwarecompare-com/vocabulary/dentalsoftwarecompare-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dentalsoftwarecompare-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dentalsoftwarecompare-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dentalsoftwarecompare-com/conventions/dentalsoftwarecompare-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dentalsoftwarecompare-com-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://dentalsoftwarecompare.com/terms
- group: design
  href: https://artifacts.apis.io/dentalsoftwarecompare-com/errors/dentalsoftwarecompare-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dentalsoftwarecompare-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dentalsoftwarecompare-com/conformance/dentalsoftwarecompare-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dentalsoftwarecompare-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/dentalsoftwarecompare-com/overlays/dentalsoftwarecompare-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dentalsoftwarecompare-com-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/dentalsoftwarecompare-com/llms/dentalsoftwarecompare-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dentalsoftwarecompare-com-llms.txt
- group: build
  href: https://artifacts.apis.io/dentalsoftwarecompare-com/mcp/dentalsoftwarecompare-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dentalsoftwarecompare-com-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/dentalsoftwarecompare-com/well-known/dentalsoftwarecompare-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dentalsoftwarecompare-com-security.txt
- group: agent
  href: https://artifacts.apis.io/dentalsoftwarecompare-com/well-known/dentalsoftwarecompare-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dentalsoftwarecompare-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dentalsoftwarecompare-com/hosts/dentalsoftwarecompare-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dentalsoftwarecompare-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dentalsoftwarecompare-com/vendors/dentalsoftwarecompare-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dentalsoftwarecompare-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dentalsoftwarecompare-com/authentication/dentalsoftwarecompare-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dentalsoftwarecompare-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dentalsoftwarecompare-com/security/dentalsoftwarecompare-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dentalsoftwarecompare-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dentalsoftwarecompare-com/security/dentalsoftwarecompare-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dentalsoftwarecompare-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dentalsoftwarecompare.com/
- group: company
  title: ''
  type: About
  url: https://dentalsoftwarecompare.com/about/
- group: operate
  title: ''
  type: Support
  url: https://dentalsoftwarecompare.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dentalsoftwarecompare.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dentalsoftwarecompare.com/terms/
created: '2026-11-05'
description: 'Dental Software Compare (dentalsoftwarecompare.com, branded DentalCompare) is a UK comparison site for dental practice management software. It compares systems on facts it cites: whether NHS Dental Services (NHSBSA) certifies them to transmit FP17 claims, the UK price each supplier publishes, NHS claims and UDA tracking, and whether the software runs in the cloud or on a practice server. It publishes guides on NHS certification, software cost, FP17 claims and CQC dental records, plus datasets such as a dental PMS pricing index and NHS dental charges/UDA data. It was surfaced via the MCP registry harvest.'
image: https://dentalsoftwarecompare.com/og.png
layout: provider
mcp_servers:
- description: ''
  name: Dental Software Compare MCP Server
  slug: mcp
modified: '2026-11-05'
name: Dental Software Compare
nav: Providers
network: true
overview: 'Dental Software Compare publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Enquiry API, Guide API, and MCP API. Tagged areas include Company, Dental Software, Practice Management, Healthcare, and NHS.


  The Dental Software Compare catalog on APIs.io includes 1 Spectral governance ruleset.


  Dental Software Compare''s developer surface includes authentication, support, and 24 more developer resources.'
plans:
- name: Dentalsoftwarecompare Com Plans Pricing
  plan_count: 2
  slug: dentalsoftwarecompare-com-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 1
  name: Dentalsoftwarecompare Com Rate Limits
  slug: dentalsoftwarecompare-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Dental Software Compare API Rules
  rule_count: 49
  severity_counts:
    error: 43
    hint: 0
    info: 5
    warn: 1
  slug: dentalsoftwarecompare-com-rules
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 58.8
    catalog_earned_first_party: 16.0
    catalog_gap: 56.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 35.6
    contract_quality: 48.8
    developer_ergonomics: 18.5
    discoverability: 65.0
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 24.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dentalsoftwarecompare Com Authentication
  slug: dentalsoftwarecompare-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dentalsoftwarecompare Com Domain Security
  slug: dentalsoftwarecompare-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dentalsoftwarecompare Com Vulnerability Disclosure
  slug: dentalsoftwarecompare-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: compare-dental-software
  slug: dentalsoftwarecompare-com-compare-dental-software
- name: submit-dental-software-enquiry
  slug: dentalsoftwarecompare-com-submit-dental-software-enquiry
slug: dentalsoftwarecompare-com
tags:
- Company
- Dental Software
- Practice Management
- Healthcare
- NHS
- Software Comparison
- United Kingdom
- Datasets
website: https://dentalsoftwarecompare.com/
---
