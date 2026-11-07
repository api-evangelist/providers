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
- acting_count: 4
  human_in_the_loop: 0
  name: Ciwregistration Co Uk Agentic Access
  operation_count: 5
  slug: ciwregistration-co-uk-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 1
apis:
- baseURL: https://ciwregistration.co.uk
  baseurl_source: declared
  description: enquiry
  name: CIW Registration Enquiry API
  slug: ciwregistration-co-uk-enquiry-api
- baseURL: https://ciwregistration.co.uk
  baseurl_source: declared
  description: The mcp API from CIW Registration — 1 operation(s) for mcp.
  name: CIW Registration MCP API
  slug: ciwregistration-co-uk-mcp-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/ciwregistration-co-uk/agentic-access/ciwregistration-co-uk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ciwregistration-co-uk-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/ciwregistration-co-uk/rules/ciwregistration-co-uk-rules.yml
  title: ''
  type: Spectral
  url: rules/ciwregistration-co-uk-rules.yml
- group: design
  href: https://artifacts.apis.io/ciwregistration-co-uk/vocabulary/ciwregistration-co-uk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ciwregistration-co-uk-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ciwregistration-co-uk/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://ciwregistration.co.uk/terms
- group: design
  href: https://artifacts.apis.io/ciwregistration-co-uk/errors/ciwregistration-co-uk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ciwregistration-co-uk-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ciwregistration-co-uk/conformance/ciwregistration-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ciwregistration-co-uk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ciwregistration-co-uk/llms/ciwregistration-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ciwregistration-co-uk-llms.txt
- group: build
  href: https://artifacts.apis.io/ciwregistration-co-uk/mcp/ciwregistration-co-uk-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ciwregistration-co-uk-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/ciwregistration-co-uk/mcp/ciwregistration-co-uk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ciwregistration-co-uk-mcp.yml
- group: auth
  href: https://artifacts.apis.io/ciwregistration-co-uk/well-known/ciwregistration-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ciwregistration-co-uk-security.txt
- group: agent
  href: https://artifacts.apis.io/ciwregistration-co-uk/well-known/ciwregistration-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ciwregistration-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/ciwregistration-co-uk/hosts/ciwregistration-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ciwregistration-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/ciwregistration-co-uk/vendors/ciwregistration-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ciwregistration-co-uk-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ciwregistration-co-uk/authentication/ciwregistration-co-uk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ciwregistration-co-uk-authentication.yml
- group: auth
  href: https://artifacts.apis.io/ciwregistration-co-uk/security/ciwregistration-co-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ciwregistration-co-uk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ciwregistration-co-uk/security/ciwregistration-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ciwregistration-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ciwregistration.co.uk/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ciwregistration.co.uk/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ciwregistration.co.uk/privacy/
- group: operate
  title: ''
  type: Support
  url: https://ciwregistration.co.uk/contact/
created: '2026-11-03'
description: CIW Registration provides information and free introduction services for entities seeking registration with Care Inspectorate Wales. The site offers guides, data tables, and consultancy contacts to help applicants understand required documents, timelines, and responsible individual requirements under the Regulation and Inspection of Social Care (Wales) Act 2016. It aggregates publicly available regulatory information and does not claim affiliation with the regulator.
image: https://ciwregistration.co.uk/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at ciwregistration.co.uk.
  name: CIW Registration MCP Server
  slug: ciwregistration-co-uk-mcp-yml
modified: '2026-11-03'
name: CIW Registration
nav: Providers
network: true
overview: 'CIW Registration publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Enquiry API and MCP API. Tagged areas include Healthcare, Wales, Registration, Social Care, and Information Services.


  The CIW Registration catalog on APIs.io includes 1 Spectral governance ruleset.


  CIW Registration''s developer surface includes authentication, support, and 19 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: CIW Registration API Rules
  rule_count: 48
  severity_counts:
    error: 43
    hint: 0
    info: 4
    warn: 1
  slug: ciwregistration-co-uk-rules
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 47.4
    developer_ergonomics: 16.1
    discoverability: 65.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ciwregistration Co Uk Authentication
  slug: ciwregistration-co-uk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ciwregistration Co Uk Domain Security
  slug: ciwregistration-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ciwregistration Co Uk Vulnerability Disclosure
  slug: ciwregistration-co-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: ciwregistration-co-uk-enquiry-process
  slug: ciwregistration-co-uk-enquiry-process
slug: ciwregistration-co-uk
tags:
- Healthcare
- Wales
- Registration
- Social Care
- Information Services
website: https://ciwregistration.co.uk/
---
