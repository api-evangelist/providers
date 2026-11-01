---
agent_readiness:
  band: agent-ready
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Biobricks Org Agentic Access
  operation_count: 12
  slug: biobricks-org-agentic-access
  summary_line: 12 operations · 10 acting
api_count: 1
apis:
- baseURL: https://biobricks.org
  baseurl_source: declared
  description: dataset
  name: biobricks-org Dataset API
  slug: biobricks-org-dataset-api
- baseURL: https://biobricks.org
  baseurl_source: declared
  description: enquiry
  name: biobricks-org Enquiry API
  slug: biobricks-org-enquiry-api
- baseURL: https://biobricks.org
  baseurl_source: declared
  description: The mcp API from biobricks-org — 1 operation(s) for mcp.
  name: biobricks-org MCP API
  slug: biobricks-org-mcp-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/biobricks-org/agentic-access/biobricks-org-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/biobricks-org-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/biobricks-org/rules/biobricks-org-rules.yml
  title: ''
  type: Spectral
  url: rules/biobricks-org-rules.yml
- group: design
  href: https://artifacts.apis.io/biobricks-org/vocabulary/biobricks-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/biobricks-org-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/biobricks-org/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://biobricks.org/terms
- group: design
  href: https://artifacts.apis.io/biobricks-org/errors/biobricks-org-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/biobricks-org-problem-types.yml
- group: design
  href: https://artifacts.apis.io/biobricks-org/conformance/biobricks-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/biobricks-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/biobricks-org/llms/biobricks-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/biobricks-org-llms.txt
- group: build
  href: https://artifacts.apis.io/biobricks-org/mcp/biobricks-org-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/biobricks-org-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/biobricks-org/mcp/biobricks-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/biobricks-org-mcp.yml
- group: auth
  href: https://artifacts.apis.io/biobricks-org/well-known/biobricks-org-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/biobricks-org-security.txt
- group: agent
  href: https://artifacts.apis.io/biobricks-org/well-known/biobricks-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/biobricks-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/biobricks-org/hosts/biobricks-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biobricks-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/biobricks-org/vendors/biobricks-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/biobricks-org-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://biobricks.org/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://biobricks.org/privacy/
- group: auth
  href: https://artifacts.apis.io/biobricks-org/security/biobricks-org-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/biobricks-org-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/biobricks-org/security/biobricks-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biobricks-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://biobricks.org/
- group: docs
  title: ''
  type: APIReference
  url: https://biobricks.org/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://biobricks.org/quote/
- group: operate
  title: ''
  type: Support
  url: https://biobricks.org/answers/
- group: commercial
  title: ''
  type: Pricing
  url: https://biobricks.org/services/
created: '2026-10-29'
description: BioBricks aggregates and publishes advertised gene synthesis and sequencing prices from multiple vendors, fetching each price directly from vendor service pages and presenting them verbatim with verification dates. The site also provides extensive guides, product listings, and resources for laboratory equipment and protocols, aiming to offer transparent, up-to-date pricing data for researchers and biotech professionals.
image: https://biobricks.org/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at biobricks.org.
  name: biobricks-org MCP Server
  slug: biobricks-org-mcp-yml
modified: '2026-10-29'
name: biobricks-org
nav: Providers
network: true
overview: 'biobricks-org publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Dataset API, Enquiry API, and MCP API. Tagged areas include Bioinformatics, Gene Synthesis, Pricing, Laboratory Equipment, and Open Data.


  The biobricks-org catalog on APIs.io includes 1 Spectral governance ruleset.


  biobricks-org''s developer surface includes API reference, getting-started guide, support, pricing, and 19 more developer resources.'
plans:
- name: Biobricks Org Plans Pricing
  plan_count: 0
  slug: biobricks-org-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Biobricks Org Rate Limits
  slug: biobricks-org-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: biobricks-org API Rules
  rule_count: 16
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 1
  slug: biobricks-org-rules
scopes:
- name: Biobricks Org Scopes
  scope_count: 0
  slug: biobricks-org-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 27
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 48.8
    developer_ergonomics: 30.2
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Biobricks Org Authentication
  slug: biobricks-org-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Biobricks Org Domain Security
  slug: biobricks-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Biobricks Org Vulnerability Disclosure
  slug: biobricks-org-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: dataset-search
  slug: biobricks-org-dataset-search-skill
slug: biobricks-org
tags:
- Bioinformatics
- Gene Synthesis
- Pricing
- Laboratory Equipment
- Open Data
website: https://biobricks.org/
---
