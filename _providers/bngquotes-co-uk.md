---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 7.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: BNG Quotes MCP API
  name: BNG Quotes API
  slug: bng-quotes-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/bngquotes-co-uk/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://bngquotes.co.uk/terms
- group: agent
  href: https://artifacts.apis.io/bngquotes-co-uk/llms/bngquotes-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bngquotes-co-uk-llms.txt
- group: build
  href: https://artifacts.apis.io/bngquotes-co-uk/mcp/bngquotes-co-uk-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/bngquotes-co-uk-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/bngquotes-co-uk/mcp/bngquotes-co-uk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bngquotes-co-uk-mcp.yml
- group: auth
  href: https://artifacts.apis.io/bngquotes-co-uk/well-known/bngquotes-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bngquotes-co-uk-security.txt
- group: agent
  href: https://artifacts.apis.io/bngquotes-co-uk/well-known/bngquotes-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bngquotes-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/bngquotes-co-uk/hosts/bngquotes-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bngquotes-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/bngquotes-co-uk/vendors/bngquotes-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bngquotes-co-uk-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bngquotes-co-uk/security/bngquotes-co-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bngquotes-co-uk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bngquotes-co-uk/security/bngquotes-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bngquotes-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bngquotes.co.uk/
- group: company
  title: ''
  type: About
  url: https://bngquotes.co.uk/about/
- group: operate
  title: ''
  type: Contact
  url: https://bngquotes.co.uk/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bngquotes.co.uk/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bngquotes.co.uk/privacy/
created: '2026-11-02'
description: BNG Quotes provides detailed cost assessments for Biodiversity Net Gain (BNG) projects across the UK. The site offers guides on assessment costs, statutory requirements, exemptions, and unit market pricing, helping developers and consultants navigate the 2026 BNG regulations. It aggregates data from government sources and ecology consultants, presenting transparent quotes and methodology for both assessment fees and delivery costs.
image: https://bngquotes.co.uk/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at bngquotes.co-uk requiring an API key.
  name: BNG Quotes MCP Server
  slug: bngquotes-co-uk-mcp-yml
modified: '2026-11-02'
name: BNG Quotes
nav: Providers
network: true
overview: BNG Quotes is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biodiversity, NetGain, United Kingdom, and Ecology.
random_paper: 20
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.8
    discoverability: 65.0
    operational_transparency: 5.3
  provenance:
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bngquotes Co Uk Domain Security
  slug: bngquotes-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bngquotes Co Uk Vulnerability Disclosure
  slug: bngquotes-co-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: bngquotes-co-uk-enquiry
  slug: bngquotes-co-uk-enquiry
slug: bngquotes-co-uk
tags:
- Company
- Biodiversity
- NetGain
- United Kingdom
- Ecology
website: https://bngquotes.co.uk/
---
