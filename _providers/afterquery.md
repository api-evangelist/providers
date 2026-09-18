---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.8
  scored_at: '2026-09-17'
api_count: 1
apis:
- description: A read-only Model Context Protocol server over the AfterQuery Experts Help Center, served anonymously from AfterQuery's documentation host. Three tools - full-text documentation search, a sandboxed re
  name: AfterQuery Experts Help Center MCP
  slug: afterquery-experts-help-center-mcp
artifact_total: 6
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/afterquery/refs/heads/main/security/afterquery-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/afterquery-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.afterquery.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.afterquery.com/
- group: company
  title: ''
  type: Blog
  url: https://www.afterquery.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.afterquery.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.afterquery.com/report-a-bug
- group: start
  title: ''
  type: SignUp
  url: https://experts.afterquery.com/apply
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AfterQuery
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.afterquery.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.afterquery.com/privacy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/afterquery/refs/heads/main/mcp/afterquery-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/afterquery-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/afterquery/refs/heads/main/a2a/afterquery-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/afterquery-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/afterquery/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/afterquery/refs/heads/main/llms/afterquery-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/afterquery-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/afterquery/refs/heads/main/well-known/afterquery-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/afterquery-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/afterquery/refs/heads/main/authentication/afterquery-authentication.yml
  title: ''
  type: Authentication
  url: authentication/afterquery-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/afterquery/refs/heads/main/conventions/afterquery-conventions.yml
  title: ''
  type: Conventions
  url: conventions/afterquery-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/afterquery/refs/heads/main/conformance/afterquery-conformance.yml
  title: ''
  type: Conformance
  url: conformance/afterquery-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/afterquery/refs/heads/main/plans/afterquery-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/afterquery-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/afterquery/refs/heads/main/rate-limits/afterquery-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/afterquery-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/afterquery/refs/heads/main/packages/afterquery-packages.yml
  title: ''
  type: Packages
  url: packages/afterquery-packages.yml
- group: operate
  title: ''
  type: Contact
  url: mailto:sales@afterquery.com
created: '2026-09-12'
description: 'AfterQuery is a San Francisco applied research lab that curates expert reasoning data for frontier foundation models - supervised fine-tuning sets, rubric- and verifier-based reinforcement-learning environments, tool-calling and computer-use environments, RLHF, deep research tasks, multimodal data, and custom evaluation suites - produced with a network of verified professionals in finance, healthcare, law and software engineering through its AfterQuery Experts contributor platform. It publishes the IDE-Bench, App-Bench, Market-Bench, FinanceArena and FinanceQA benchmarks and sells data and evaluation engagements directly to AI labs and enterprises. AfterQuery ships no public product API: its only machine-callable surface is an anonymous documentation MCP server on its help-centre host, alongside an A2A agent card, a published agent skill and two llms.txt files.'
image: https://www.afterquery.com/og-default.png
layout: provider
mcp_servers:
- description: A read-only documentation MCP server over the AfterQuery Experts Help Center - full-text search across the help centre, a sandboxed read-only filesystem view of the documentation pages, and a feedback
  name: AfterQuery Experts Help Center MCP
  slug: afterquery-experts-help-center-mcp
modified: '2026-09-12'
name: AfterQuery
nav: Providers
network: true
overview: 'AfterQuery publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Training Data, and Data.


  AfterQuery''s developer surface includes documentation, engineering blog, support, signup flow, authentication, and 17 more developer resources.'
plans:
- name: Afterquery Plans Pricing
  plan_count: 0
  slug: afterquery-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Afterquery Rate Limits
  slug: afterquery-rate-limits
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 75.9
    operational_transparency: 2.6
  previous_composite: 22.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Afterquery Authentication
  slug: afterquery-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Afterquery Domain Security
  slug: afterquery-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: afterquery
tags:
- Company
- Artificial Intelligence
- Machine-Learning
- Training Data
- Data
- Evaluation
- Reinforcement Learning
- Benchmarks
- Research
- Agents
- MCP
website: https://www.afterquery.com/
---
