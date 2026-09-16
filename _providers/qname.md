---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 11.5
  scored_at: '2026-09-15'
api_count: 1
apis:
- description: 'Approval-gated REST API for WHOIS/RDAP lookups: GET /api/whois/{domain} (single), POST /api/whois/batch (batch), and GET /api/domain-traffic (traffic). Requires an admin-approved API key (qname_ prefi'
  name: QName AI WHOIS REST API
  slug: qname-ai-whois-rest-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://qname.ai
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qname/refs/heads/main/security/qname-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qname-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://qname.ai/cli
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/QNameAI
- group: operate
  title: ''
  type: Roadmap
  url: https://qname.ai/roadmap
- group: commercial
  title: ''
  type: TermsOfService
  url: https://qname.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://qname.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://qname.ai/contact
- group: start
  title: ''
  type: Login
  url: https://qname.ai/auth/login
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/qname/refs/heads/main/llms/qname-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/qname-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/qname/refs/heads/main/skills/qname-cli.md
  title: ''
  type: AgentSkill
  url: skills/qname-cli.md
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/qname/refs/heads/main/packages/qname-packages.yml
  title: ''
  type: Packages
  url: packages/qname-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/qname/refs/heads/main/cli/qname-cli.yml
  title: ''
  type: CLI
  url: cli/qname-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qname/refs/heads/main/authentication/qname-authentication.yml
  title: ''
  type: Authentication
  url: authentication/qname-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qname/refs/heads/main/conventions/qname-conventions.yml
  title: ''
  type: Conventions
  url: conventions/qname-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qname/refs/heads/main/errors/qname-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/qname-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qname/refs/heads/main/data-model/qname-data-model.yml
  title: ''
  type: DataModel
  url: data-model/qname-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/qname/refs/heads/main/mcp/qname-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/qname-mcp.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/qname/refs/heads/main/changelog/qname-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/qname-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://qname.ai/changelog
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/qname/refs/heads/main/plans/qname-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/qname-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/qname/refs/heads/main/rate-limits/qname-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/qname-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qname/refs/heads/main/lifecycle/qname-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/qname-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qname/refs/heads/main/conformance/qname-conformance.yml
  title: ''
  type: Conformance
  url: conformance/qname-conformance.yml
created: '2026-09-13'
description: QName AI (qname.ai) is a domain-research workspace whose WHOIS/RDAP capability is exposed programmatically through a small, approval-gated REST API and an agent-native CLI (@qname/cli). It offers authenticated single-domain and batch WHOIS/domain lookups plus a domain-traffic scope, consumable via the CLI, an installable Agent Skill, or direct REST calls.
layout: provider
mcp_servers:
- description: ''
  name: QName AI WHOIS API MCP Server
  slug: qname-ai-whois-api-mcp-server
modified: '2026-09-14'
name: QName AI WHOIS API
nav: Providers
network: true
overview: 'QName AI WHOIS API publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include WHOIS, rdap, domain-research, Domain Search, and batch-lookup.


  QName AI WHOIS API''s developer surface includes support, CLI, authentication, changelog, and 20 more developer resources.'
plans:
- name: Qname Plans Pricing
  plan_count: 0
  slug: qname-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Qname Rate Limits
  slug: qname-rate-limits
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 72.2
    operational_transparency: 26.3
  previous_composite: 27.5
  provenance:
    conformance: derived
    mcp: derived
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Qname Authentication
  slug: qname-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Qname Domain Security
  slug: qname-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qname
tags:
- WHOIS
- rdap
- domain-research
- Domain Search
- batch-lookup
- CLI
- Agent Tooling
- AgentSkill
- llms-txt
- Developer Tools
- Domain Intelligence
website: https://qname.ai
---
