---
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
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.4
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 26
  human_in_the_loop: 26
  name: Beam Ai Agentic Access
  operation_count: 48
  slug: beam-ai-agentic-access
  summary_line: 48 operations · 26 acting · 26 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.beamstudio.ai
  baseurl_source: declared
  description: The Agent Context Files API from Beam AI — 3 operation(s) for agent context files.
  name: Beam AI Agent Context Files API
  slug: beam-ai-agent-context-files-api
- baseURL: https://api.beamstudio.ai
  baseurl_source: declared
  description: The Agent Graph API from Beam AI — 12 operation(s) for agent graph.
  name: Beam AI Agent Graph API
  slug: beam-ai-agent-graph-api
- baseURL: https://api.beamstudio.ai
  baseurl_source: declared
  description: The Agent Setup API from Beam AI — 6 operation(s) for agent setup.
  name: Beam AI Agent Setup API
  slug: beam-ai-agent-setup-api
- baseURL: https://api.beamstudio.ai
  baseurl_source: declared
  description: The Agent Skills API from Beam AI — 1 operation(s) for agent skills.
  name: Beam AI Agent Skills API
  slug: beam-ai-agent-skills-api
- baseURL: https://api.beamstudio.ai
  baseurl_source: declared
  description: The Agent Task API from Beam AI — 12 operation(s) for agent task.
  name: Beam AI Agent Task API
  slug: beam-ai-agent-task-api
- baseURL: https://api.beamstudio.ai
  baseurl_source: declared
  description: The Agent Views API from Beam AI — 4 operation(s) for agent views.
  name: Beam AI Agent Views API
  slug: beam-ai-agent-views-api
- baseURL: https://api.beamstudio.ai
  baseurl_source: declared
  description: The Agents API from Beam AI — 2 operation(s) for agents.
  name: Beam AI Agents API
  slug: beam-ai-agents-api
- baseURL: https://api.beamstudio.ai
  baseurl_source: declared
  description: The Complete Agent Graph API from Beam AI — 2 operation(s) for complete agent graph.
  name: Beam AI Complete Agent Graph API
  slug: beam-ai-complete-agent-graph-api
- baseURL: https://api.beamstudio.ai
  baseurl_source: declared
  description: The Custom Tool API from Beam AI — 1 operation(s) for custom tool.
  name: Beam AI Custom Tool API
  slug: beam-ai-custom-tool-api
- baseURL: https://api.beamstudio.ai
  baseurl_source: declared
  description: The Tool API from Beam AI — 3 operation(s) for tool.
  name: Beam AI Tool API
  slug: beam-ai-tool-api
- baseURL: https://api.beamstudio.ai
  baseurl_source: declared
  description: The User API from Beam AI — 1 operation(s) for user.
  name: Beam AI User API
  slug: beam-ai-user-api
artifact_total: 22
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/beam-ai/refs/heads/main/agentic-access/beam-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/beam-ai-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beam-ai/refs/heads/main/rules/beam-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/beam-ai-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beam-ai/refs/heads/main/json-ld/beam-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/beam-ai-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beam-ai/refs/heads/main/vocabulary/beam-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/beam-ai-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/beam-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beam-ai/refs/heads/main/data-model/beam-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/beam-ai-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/beam-ai/refs/heads/main/changelog/beam-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/beam-ai-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beam-ai/refs/heads/main/authentication/beam-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/beam-ai-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beam-ai/refs/heads/main/errors/beam-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/beam-ai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beam-ai/refs/heads/main/conformance/beam-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/beam-ai-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/beam-ai/refs/heads/main/llms/beam-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beam-ai-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beam-ai/refs/heads/main/a2a/beam-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/beam-ai-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/beam-ai/refs/heads/main/well-known/beam-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beam-ai-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beam-ai/refs/heads/main/hosts/beam-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beam-ai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beam-ai/refs/heads/main/vendors/beam-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beam-ai-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://beam.ai/integrations/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beam.ai/legal/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://beam.ai/legal/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beam.ai/legal/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://beam.ai/media
- group: operate
  title: ''
  type: ChangeLog
  url: https://beam.ai/resources/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.beam.ai/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beam-ai/refs/heads/main/security/beam-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beam-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beam.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.beam.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.beam.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.beam.ai/01-getting-started/welcome/welcome
- group: operate
  title: ''
  type: Support
  url: https://beam.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://beam.ai/articles
- group: commercial
  title: ''
  type: Pricing
  url: https://beam.ai/roi-calculator
created: '2026-10-13'
description: Beam AI provides a leading platform for agentic automation and AI agents, enabling enterprises to create self‑learning AI agents that automate operations, reduce costs, and improve efficiency. Their solutions include AI‑driven workflows, integrations with databases and SaaS tools, and a suite of industry‑specific applications for finance, healthcare, and customer service. Beam AI serves Fortune 500 companies and scale‑ups, offering a no‑code interface, robust security, and customizable agents that can learn from SOPs and execute tasks autonomously.
image: https://framerusercontent.com/assets/K1wsaUBWV7twBiKRliuySFqiHE.png
json_schemas:
- name: AgentGraphNode
  property_count: 30
  slug: beam-ai-agent-graph-node
- name: AgentTaskWithUrlDto
  property_count: 25
  slug: beam-ai-agent-task-with-url-dto
- name: AgentToolConfigurationOutputParams
  property_count: 13
  slug: beam-ai-agent-tool-configuration-output-params
- name: MinimalAgentGraphNodeDto
  property_count: 26
  slug: beam-ai-minimal-agent-graph-node-dto
- name: MinimalAgentTaskDto
  property_count: 24
  slug: beam-ai-minimal-agent-task-dto
- name: SetupBeamAgentDTO
  property_count: 4
  slug: beam-ai-setup-beam-agent-dto
jsonld:
- class_count: 120
  name: Beam Ai Context
  property_count: 380
  slug: beam-ai-context
layout: provider
modified: '2026-10-13'
name: Beam AI
nav: Providers
network: true
overview: 'Beam AI publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Context Files API, Agent Graph API, Agent Setup API, and 8 more. Tagged areas include Company, Artificial Intelligence, Automation, Enterprise, and Platform.


  The Beam AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Beam AI''s developer surface includes changelog, authentication, API reference, documentation, getting-started guide, support, engineering blog, and 23 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Beam AI API Rules
  rule_count: 12
  severity_counts:
    error: 7
    hint: 0
    info: 2
    warn: 3
  slug: beam-ai-rules
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 39.5
    contract_governance: 35.6
    contract_quality: 54.8
    developer_ergonomics: 58.9
    discoverability: 75.0
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Beam Ai Authentication
  slug: beam-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Beam Ai Domain Security
  slug: beam-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beam-ai
tags:
- Company
- Artificial Intelligence
- Automation
- Enterprise
- Platform
website: https://beam.ai
---
