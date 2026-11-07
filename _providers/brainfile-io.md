---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
    error_semantics: false
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Brainfile provides an MCP for Claude Code automation. Documentation is at https://brainfile.io/guides. No public machine‑readable contract was found.
  name: Brainfile API
  slug: brainfile-api
- description: 'Brainfile API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Brainfile API
  slug: brainfile-io-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/brainfile-io/plans/brainfile-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brainfile-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/brainfile-io/rules/brainfile-io-rules.yml
  title: ''
  type: Spectral
  url: rules/brainfile-io-rules.yml
- group: design
  href: https://artifacts.apis.io/brainfile-io/vocabulary/brainfile-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/brainfile-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/brainfile-io/conformance/brainfile-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brainfile-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/brainfile-io/llms/brainfile-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brainfile-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/brainfile-io/mcp/brainfile-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/brainfile-io-mcp.yml
- group: other
  href: https://artifacts.apis.io/brainfile-io/hosts/brainfile-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brainfile-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/brainfile-io/vendors/brainfile-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brainfile-io-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://brainfile.io/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://brainfile.io/mcp-setup
- group: auth
  href: https://artifacts.apis.io/brainfile-io/security/brainfile-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brainfile-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brainfile.io/
coverage:
  checked: '2026-11-03'
  detail: No public OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract was found despite documentation pages.
  evidence:
  - status: 200
    url: https://brainfile.io/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Brainfile is a maintained operating system for Claude Code, providing an autopilot that remembers how you work. It offers a cloud‑pull delivery model with no downloads, delivering rule sets, a weekly freshness feed, and a memory of your workflow directly to your local Claude Code environment. Users get a 30‑day free trial without requiring a credit card, and can cancel anytime via email or the billing portal. The service emphasizes privacy—your code never leaves your machine, and only a licence‑gated endpoint is contacted for updates.
image: https://brainfile.io/og-brainfile.png
layout: provider
mcp_servers:
- description: Remote MCP server at brainfile.io.
  name: Brainfile MCP Server
  slug: brainfile-io-mcp-yml
modified: '2026-11-02'
name: Brainfile
nav: Providers
network: true
overview: 'Brainfile is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Automation, Developer Tools, Claude, and Productivity.


  The Brainfile catalog on APIs.io includes 1 Spectral governance ruleset.


  Brainfile''s developer surface includes documentation, getting-started guide, and 10 more developer resources.'
plans:
- name: Brainfile Io Plans Pricing
  plan_count: 2
  slug: brainfile-io-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: Brainfile API Rules
  rule_count: 19
  severity_counts:
    error: 17
    hint: 0
    info: 1
    warn: 1
  slug: brainfile-io-rules
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 45.8
    catalog_earned_first_party: 8.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 10.7
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brainfile Io Domain Security
  slug: brainfile-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: brainfile-io
tags:
- Artificial Intelligence
- Automation
- Developer Tools
- Claude
- Productivity
website: https://brainfile.io/
---
