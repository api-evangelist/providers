---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 14.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Cardmachinepricing Co Uk Agentic Access
  operation_count: 1
  slug: cardmachinepricing-co-uk-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Provides the latest printed in‑person transaction rates for UK card‑machine providers.
  name: Card Machine Pricing API
  slug: pricing-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/cardmachinepricing-co-uk/agentic-access/cardmachinepricing-co-uk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cardmachinepricing-co-uk-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/cardmachinepricing-co-uk/rules/cardmachinepricing-co-uk-rules.yml
  title: ''
  type: Spectral
  url: rules/cardmachinepricing-co-uk-rules.yml
- group: design
  href: https://artifacts.apis.io/cardmachinepricing-co-uk/vocabulary/cardmachinepricing-co-uk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cardmachinepricing-co-uk-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cardmachinepricing-co-uk/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://cardmachinepricing.co.uk/terms
- group: auth
  href: https://artifacts.apis.io/cardmachinepricing-co-uk/authentication/cardmachinepricing-co-uk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cardmachinepricing-co-uk-authentication.yml
- group: design
  href: https://artifacts.apis.io/cardmachinepricing-co-uk/errors/cardmachinepricing-co-uk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cardmachinepricing-co-uk-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cardmachinepricing-co-uk/conformance/cardmachinepricing-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cardmachinepricing-co-uk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cardmachinepricing-co-uk/llms/cardmachinepricing-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cardmachinepricing-co-uk-llms.txt
- group: build
  href: https://artifacts.apis.io/cardmachinepricing-co-uk/mcp/cardmachinepricing-co-uk-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cardmachinepricing-co-uk-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/cardmachinepricing-co-uk/mcp/cardmachinepricing-co-uk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cardmachinepricing-co-uk-mcp.yml
- group: auth
  href: https://artifacts.apis.io/cardmachinepricing-co-uk/well-known/cardmachinepricing-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cardmachinepricing-co-uk-security.txt
- group: agent
  href: https://artifacts.apis.io/cardmachinepricing-co-uk/well-known/cardmachinepricing-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cardmachinepricing-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/cardmachinepricing-co-uk/hosts/cardmachinepricing-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cardmachinepricing-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/cardmachinepricing-co-uk/vendors/cardmachinepricing-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cardmachinepricing-co-uk-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cardmachinepricing-co-uk/security/cardmachinepricing-co-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cardmachinepricing-co-uk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cardmachinepricing-co-uk/security/cardmachinepricing-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cardmachinepricing-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cardmachinepricing.co.uk/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cardmachinepricing.co.uk/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cardmachinepricing.co.uk/privacy/
- group: operate
  title: ''
  type: Support
  url: mailto:quotes@cardmachinepricing.co.uk
created: '2026-10-29'
description: Card Machine Pricing aggregates the in‑person transaction rates that UK card‑machine providers publish on their own websites. By regularly scraping each provider’s pricing page, the service records the quoted rate together with the date it was read, offering a transparent, up‑to‑date comparison of merchant‑card‑machine costs across the UK market. The data is provided via a public API that returns the provider name, the printed rate, the source URL and the read date, enabling developers to build pricing dashboards, cost‑analysis tools, or integrate the information into fintech applications.
image: https://cardmachinepricing.co.uk/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at cardmachinepricing.co.uk.
  name: cardmachinepricing-co-uk MCP Server
  slug: cardmachinepricing-co-uk-mcp-yml
modified: '2026-10-29'
name: cardmachinepricing-co-uk
nav: Providers
network: true
overview: 'cardmachinepricing-co-uk is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Pricing, UK, and Card-Machines.


  The cardmachinepricing-co-uk catalog on APIs.io includes 1 Spectral governance ruleset.


  cardmachinepricing-co-uk''s developer surface includes authentication, support, and 19 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: cardmachinepricing-co-uk API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: cardmachinepricing-co-uk-rules
scopes:
- name: Cardmachinepricing Co Uk Scopes
  scope_count: 0
  slug: cardmachinepricing-co-uk-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 39.8
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 36.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cardmachinepricing Co Uk Authentication
  slug: cardmachinepricing-co-uk-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cardmachinepricing Co Uk Domain Security
  slug: cardmachinepricing-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Cardmachinepricing Co Uk Vulnerability Disclosure
  slug: cardmachinepricing-co-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: dataset-skill
  slug: cardmachinepricing-co-uk-dataset-skill
- name: enquiry-skill
  slug: cardmachinepricing-co-uk-enquiry-skill
slug: cardmachinepricing-co-uk
tags:
- Company
- Finance
- Pricing
- UK
- Card-Machines
website: https://cardmachinepricing.co.uk/
---
