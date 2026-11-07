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
  name: Crmagency Co Uk Agentic Access
  operation_count: 5
  slug: crmagency-co-uk-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 1
apis:
- baseURL: https://crmagency.co.uk
  baseurl_source: declared
  description: enquiry
  name: CRM Agency Enquiry API
  slug: crmagency-co-uk-enquiry-api
- baseURL: https://crmagency.co.uk
  baseurl_source: declared
  description: The mcp API from CRM Agency — 1 operation(s) for mcp.
  name: CRM Agency MCP API
  slug: crmagency-co-uk-mcp-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/crmagency-co-uk/agentic-access/crmagency-co-uk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/crmagency-co-uk-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/crmagency-co-uk/rules/crmagency-co-uk-rules.yml
  title: ''
  type: Spectral
  url: rules/crmagency-co-uk-rules.yml
- group: design
  href: https://artifacts.apis.io/crmagency-co-uk/vocabulary/crmagency-co-uk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/crmagency-co-uk-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/crmagency-co-uk/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://crmagency.co.uk/terms
- group: design
  href: https://artifacts.apis.io/crmagency-co-uk/errors/crmagency-co-uk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/crmagency-co-uk-problem-types.yml
- group: design
  href: https://artifacts.apis.io/crmagency-co-uk/conformance/crmagency-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crmagency-co-uk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/crmagency-co-uk/llms/crmagency-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crmagency-co-uk-llms.txt
- group: agent
  href: https://artifacts.apis.io/crmagency-co-uk/mcp/crmagency-co-uk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/crmagency-co-uk-mcp.yml
- group: auth
  href: https://artifacts.apis.io/crmagency-co-uk/well-known/crmagency-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/crmagency-co-uk-security.txt
- group: agent
  href: https://artifacts.apis.io/crmagency-co-uk/well-known/crmagency-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crmagency-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/crmagency-co-uk/hosts/crmagency-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crmagency-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/crmagency-co-uk/vendors/crmagency-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crmagency-co-uk-vendors.yml
- group: auth
  href: https://artifacts.apis.io/crmagency-co-uk/authentication/crmagency-co-uk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/crmagency-co-uk-authentication.yml
- group: auth
  href: https://artifacts.apis.io/crmagency-co-uk/security/crmagency-co-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/crmagency-co-uk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/crmagency-co-uk/security/crmagency-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crmagency-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crmagency.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://crmagency.co.uk/about/
- group: operate
  title: ''
  type: Contact
  url: https://crmagency.co.uk/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crmagency.co.uk/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crmagency.co.uk/privacy/
created: '2026-11-04'
description: CRM Agency provides a UK‑focused CRM selection, set‑up, migration and ongoing support service. It runs its own site crmagency.co.uk, publishing a transparent price calculator and a data‑driven index of CRM agency fees across the UK. The team both operates the site and delivers the CRM implementation projects, offering a single‑project price with no hidden costs. The site includes guides, a pricing calculator, and a public dataset of CRM agency fees, updated regularly.
image: https://crmagency.co.uk/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at crmagency.co.uk.
  name: CRM Agency MCP Server
  slug: crmagency-co-uk-mcp-yml
modified: '2026-11-04'
name: CRM Agency
nav: Providers
network: true
overview: 'CRM Agency publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Enquiry API and MCP API. Tagged areas include CRM, Agency, United Kingdom, Software-as-a-Service, and Consulting.


  The CRM Agency catalog on APIs.io includes 1 Spectral governance ruleset.


  CRM Agency''s developer surface includes authentication, documentation, and 19 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: CRM Agency API Rules
  rule_count: 48
  severity_counts:
    error: 43
    hint: 0
    info: 4
    warn: 1
  slug: crmagency-co-uk-rules
score:
  band: thin
  composite: 33.5
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
    contract_quality: 47.4
    developer_ergonomics: 23.2
    discoverability: 65.0
    operational_transparency: 10.5
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
  name: Crmagency Co Uk Authentication
  slug: crmagency-co-uk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Crmagency Co Uk Domain Security
  slug: crmagency-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Crmagency Co Uk Vulnerability Disclosure
  slug: crmagency-co-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: crmagency-co-uk-enquiry-submit
  slug: crmagency-co-uk-enquiry-submit
slug: crmagency-co-uk
tags:
- CRM
- Agency
- United Kingdom
- Software-as-a-Service
- Consulting
website: https://crmagency.co.uk/
---
