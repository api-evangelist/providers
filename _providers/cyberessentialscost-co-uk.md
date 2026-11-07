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
  name: Cyberessentialscost Co Uk Agentic Access
  operation_count: 5
  slug: cyberessentialscost-co-uk-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 1
apis:
- baseURL: https://cyberessentialscost.co.uk
  baseurl_source: declared
  description: enquiry
  name: Cyber Essentials Cost Enquiry API
  slug: cyberessentialscost-co-uk-enquiry-api
- baseURL: https://cyberessentialscost.co.uk
  baseurl_source: declared
  description: The mcp API from Cyber Essentials Cost — 1 operation(s) for mcp.
  name: Cyber Essentials Cost MCP API
  slug: cyberessentialscost-co-uk-mcp-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/cyberessentialscost-co-uk/agentic-access/cyberessentialscost-co-uk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cyberessentialscost-co-uk-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/cyberessentialscost-co-uk/rules/cyberessentialscost-co-uk-rules.yml
  title: ''
  type: Spectral
  url: rules/cyberessentialscost-co-uk-rules.yml
- group: design
  href: https://artifacts.apis.io/cyberessentialscost-co-uk/vocabulary/cyberessentialscost-co-uk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cyberessentialscost-co-uk-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cyberessentialscost-co-uk/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://cyberessentialscost.co.uk/terms
- group: design
  href: https://artifacts.apis.io/cyberessentialscost-co-uk/errors/cyberessentialscost-co-uk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cyberessentialscost-co-uk-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cyberessentialscost-co-uk/conformance/cyberessentialscost-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cyberessentialscost-co-uk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cyberessentialscost-co-uk/llms/cyberessentialscost-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cyberessentialscost-co-uk-llms.txt
- group: build
  href: https://artifacts.apis.io/cyberessentialscost-co-uk/mcp/cyberessentialscost-co-uk-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cyberessentialscost-co-uk-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/cyberessentialscost-co-uk/mcp/cyberessentialscost-co-uk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cyberessentialscost-co-uk-mcp.yml
- group: auth
  href: https://artifacts.apis.io/cyberessentialscost-co-uk/well-known/cyberessentialscost-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cyberessentialscost-co-uk-security.txt
- group: agent
  href: https://artifacts.apis.io/cyberessentialscost-co-uk/well-known/cyberessentialscost-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cyberessentialscost-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/cyberessentialscost-co-uk/hosts/cyberessentialscost-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cyberessentialscost-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/cyberessentialscost-co-uk/vendors/cyberessentialscost-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cyberessentialscost-co-uk-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cyberessentialscost.co.uk/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cyberessentialscost.co.uk/privacy/
- group: auth
  href: https://artifacts.apis.io/cyberessentialscost-co-uk/authentication/cyberessentialscost-co-uk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cyberessentialscost-co-uk-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cyberessentialscost-co-uk/security/cyberessentialscost-co-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cyberessentialscost-co-uk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cyberessentialscost-co-uk/security/cyberessentialscost-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cyberessentialscost-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cyberessentialscost.co.uk/
created: '2026-11-04'
description: Cyber Essentials Cost provides a price comparison service for Cyber Essentials and Cyber Essentials Plus certifications in the UK, detailing costs by organisation size, offering quotes from multiple certification bodies, and explaining requirements, benefits, and related FAQs. The site includes a dataset of certification price indexes and tools to help businesses obtain accurate quotes and understand compliance obligations.
image: https://cyberessentialscost.co.uk/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at cyberessentialscost.co.uk.
  name: Cyber Essentials Cost MCP Server
  slug: cyberessentialscost-co-uk-mcp-yml
modified: '2026-11-04'
name: Cyber Essentials Cost
nav: Providers
network: true
overview: 'Cyber Essentials Cost publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Enquiry API and MCP API. Tagged areas include Company, Cyber Essentials, Pricing, United Kingdom, and Certification.


  The Cyber Essentials Cost catalog on APIs.io includes 1 Spectral governance ruleset.


  Cyber Essentials Cost''s developer surface includes authentication and 19 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Cyber Essentials Cost API Rules
  rule_count: 48
  severity_counts:
    error: 43
    hint: 0
    info: 4
    warn: 1
  slug: cyberessentialscost-co-uk-rules
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 47.4
    developer_ergonomics: 13.7
    discoverability: 65.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
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
  name: Cyberessentialscost Co Uk Authentication
  slug: cyberessentialscost-co-uk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cyberessentialscost Co Uk Domain Security
  slug: cyberessentialscost-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cyberessentialscost Co Uk Vulnerability Disclosure
  slug: cyberessentialscost-co-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: cyberessentialscost-co-uk-enquiry-process
  slug: cyberessentialscost-co-uk-enquiry-process
- name: cyberessentialscost-co-uk-mcp-interaction
  slug: cyberessentialscost-co-uk-mcp-interaction
slug: cyberessentialscost-co-uk
tags:
- Company
- Cyber Essentials
- Pricing
- United Kingdom
- Certification
- Comparison
website: https://cyberessentialscost.co.uk/
---
