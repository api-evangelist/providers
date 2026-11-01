---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Public read-only REST twins for the EngineerPro engineering library and tools catalog.
  name: EngineerPro API
  slug: engineerpro-api
- baseURL: https://api.aiengineerprofessional.com
  baseurl_source: declared
  description: Public read-only REST twins for the EngineerPro engineering library (118 books) and software-engineering tools catalog. The same data is available over MCP at https://api.aiengineerprofessional.com/ap
  name: EngineerPro — library & tools API API
  slug: engineerpro-library-tools-api-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/aiengineerprofessional-com/rules/aiengineerprofessional-com-rules.yml
  title: ''
  type: Spectral
  url: rules/aiengineerprofessional-com-rules.yml
- group: design
  href: https://artifacts.apis.io/aiengineerprofessional-com/vocabulary/aiengineerprofessional-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aiengineerprofessional-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aiengineerprofessional-com/errors/aiengineerprofessional-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aiengineerprofessional-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aiengineerprofessional-com/conformance/aiengineerprofessional-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aiengineerprofessional-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aiengineerprofessional-com/llms/aiengineerprofessional-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiengineerprofessional-com-llms.txt
- group: build
  href: https://artifacts.apis.io/aiengineerprofessional-com/mcp/aiengineerprofessional-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aiengineerprofessional-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/aiengineerprofessional-com/mcp/aiengineerprofessional-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aiengineerprofessional-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/aiengineerprofessional-com/hosts/aiengineerprofessional-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiengineerprofessional-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aiengineerprofessional-com/vendors/aiengineerprofessional-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aiengineerprofessional-com-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://aiengineerprofessional.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/aiengineerprofessional-com/security/aiengineerprofessional-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiengineerprofessional-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiengineerprofessional.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aiengineerprofessional.com/guides
- group: operate
  title: ''
  type: Support
  url: https://aiengineerprofessional.com/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aiengineerprofessional.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aiengineerprofessional.com/terms
- group: company
  title: ''
  type: About
  url: https://aiengineerprofessional.com/about
created: '2026-10-29'
description: AI Engineer Professional is a knowledge platform offering guides, books, and resources for AI engineering, data science, and business strategy. It provides curated content, practical tutorials, and community-driven insights to help professionals build, scale, and lead AI-driven initiatives across organizations. The platform emphasizes research-backed guidance, transparent discussion of differing viewpoints, and actionable advice for developing AI systems that ship.
image: https://aiengineerprofessional.com/opengraph-image-1oy18k?29435694197f5727
layout: provider
mcp_servers:
- description: Remote MCP server at aiengineerprofessional.com.
  name: aiengineerprofessional-com MCP Server
  slug: aiengineerprofessional-com-mcp-yml
modified: '2026-10-29'
name: aiengineerprofessional-com
nav: Providers
network: true
overview: 'aiengineerprofessional-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including EngineerPro — library & tools API API, and 1 more. Tagged areas include Company, AI, Engineering, Guides, and Knowledge.


  The aiengineerprofessional-com catalog on APIs.io includes 1 Spectral governance ruleset.


  aiengineerprofessional-com''s developer surface includes API reference, documentation, support, and 14 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: aiengineerprofessional-com API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: aiengineerprofessional-com-rules
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 47.1
    developer_ergonomics: 21.4
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aiengineerprofessional Com Domain Security
  slug: aiengineerprofessional-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aiengineerprofessional-com
tags:
- Company
- AI
- Engineering
- Guides
- Knowledge
website: https://aiengineerprofessional.com/
---
