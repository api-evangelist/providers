---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.1
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Janus Machine Market Agentic Access
  operation_count: 4
  slug: janus-machine-market-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 2
apis:
- baseURL: https://api.github.com/repos/Hawkar-usls/JANUS-MACHINE-MARKET
  baseurl_source: declared
  description: Places one bounded JANUS.SEARCH research order by opening a GitHub issue with a fixed title and a JANUS_BUYER_QUERY_SHADOW_JSON body marker (query up to 4000 UTF-8 bytes), then reads the reconciled re
  name: JANUS.SEARCH GitHub Issues Ingress
  slug: janus-search-github-ingress
- baseURL: https://api.github.com/repos/Hawkar-usls/JANUS-MACHINE-MARKET
  baseurl_source: declared
  description: Requests one structural/policy-risk review of a public GitHub pull request, frozen at its exact 40-hex head SHA (maximum 300 changed files; target code is never executed), by opening a GitHub issue wi
  name: JANUS.PR_REVIEW GitHub Issues Ingress
  slug: janus-pr-review-github-ingress
artifact_total: 8
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/janus-machine-market/refs/heads/main/agentic-access/janus-machine-market-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/janus-machine-market-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/janus-machine-market/refs/heads/main/rate-limits/janus-machine-market-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/janus-machine-market-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/janus-machine-market/refs/heads/main/plans/janus-machine-market-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/janus-machine-market-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/janus-machine-market/refs/heads/main/rules/janus-machine-market-rules.yml
  title: ''
  type: Spectral
  url: rules/janus-machine-market-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/janus-machine-market/refs/heads/main/vocabulary/janus-machine-market-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/janus-machine-market-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/janus-machine-market/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/janus-machine-market/refs/heads/main/conventions/janus-machine-market-conventions.yml
  title: ''
  type: Conventions
  url: conventions/janus-machine-market-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/janus-machine-market/refs/heads/main/security/janus-machine-market-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/janus-machine-market-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/janus-machine-market/refs/heads/main/lifecycle/janus-machine-market-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/janus-machine-market-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/janus-machine-market/refs/heads/main/errors/janus-machine-market-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/janus-machine-market-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/janus-machine-market/refs/heads/main/conformance/janus-machine-market-conformance.yml
  title: ''
  type: Conformance
  url: conformance/janus-machine-market-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/janus-machine-market/refs/heads/main/overlays/janus-machine-market-pr-review-github-ingress-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/janus-machine-market-pr-review-github-ingress-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/janus-machine-market/refs/heads/main/hosts/janus-machine-market-hosts.yml
  title: ''
  type: Hosts
  url: hosts/janus-machine-market-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/janus-machine-market/refs/heads/main/vendors/janus-machine-market-vendors.yml
  title: ''
  type: Vendors
  url: vendors/janus-machine-market-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/janus-machine-market/refs/heads/main/authentication/janus-machine-market-authentication.yml
  title: ''
  type: Authentication
  url: authentication/janus-machine-market-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://hawkar-usls.github.io/JANUS-MACHINE-MARKET/
- group: docs
  title: ''
  type: Documentation
  url: https://hawkar-usls.github.io/JANUS-MACHINE-MARKET/AGENTS.md
- group: start
  title: ''
  type: GettingStarted
  url: https://hawkar-usls.github.io/JANUS-MACHINE-MARKET/docs/AGENT_INTEGRATION_RECIPES.md
- group: other
  title: ''
  type: APIsJSON
  url: https://hawkar-usls.github.io/JANUS-MACHINE-MARKET/apis.json
- group: commercial
  title: ''
  type: Pricing
  url: https://hawkar-usls.github.io/JANUS-MACHINE-MARKET/PRICING.json
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Hawkar-usls/JANUS-MACHINE-MARKET
- group: operate
  title: ''
  type: Support
  url: https://github.com/Hawkar-usls/JANUS-MACHINE-MARKET/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/Hawkar-usls/JANUS-MACHINE-MARKET/blob/main/LICENSE
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/Hawkar-usls/JANUS-MACHINE-MARKET/blob/main/SECURITY.md
- group: agent
  title: ''
  type: LLMsTxt
  url: https://hawkar-usls.github.io/JANUS-MACHINE-MARKET/llms.txt
created: '2026-09-25'
description: 'JANUS Machine Market (styled JANUS MACHINE MARKET) is an agent-native research and review service operated by GitHub user Hawkar-usls. Two capabilities are live as a public beta: JANUS.SEARCH, which returns bounded research results with provenance, evidence, contradiction/uncertainty notes and receipt lineage, and JANUS.PR_REVIEW, a structural/policy-risk review of a public GitHub pull request frozen at an exact head SHA. The machine ingress is the GitHub Issues REST API on the provider''s own repository: an agent places an order by opening an issue with its own GitHub credential and reads the result from the issue comments; the first order per external GitHub principal is free. The provider states that MCP, A2A, x402, paid SEARCH and a general transaction API are prepared but not live. Hosted on GitHub Pages.'
layout: provider
modified: '2026-09-25'
name: JANUS Machine Market
nav: Providers
network: true
overview: 'JANUS Machine Market publishes 2 APIs on the [APIs.io](https://apis.io/) network: JANUS.SEARCH GitHub Issues Ingress and JANUS.PR_REVIEW GitHub Issues Ingress. Tagged areas include AI Agents, Research, Search, Provenance, and Code Review.


  The JANUS Machine Market catalog on APIs.io includes 1 Spectral governance ruleset.


  JANUS Machine Market''s developer surface includes authentication, documentation, getting-started guide, pricing, support, and 20 more developer resources.'
plans:
- name: Janus Machine Market Plans Pricing
  plan_count: 2
  slug: janus-machine-market-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Janus Machine Market Rate Limits
  slug: janus-machine-market-rate-limits
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: JANUS Machine Market API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: janus-machine-market-rules
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 60.8
    catalog_earned_first_party: 20.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 44.1
    developer_ergonomics: 45.2
    discoverability: 69.6
    operational_transparency: 47.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Janus Machine Market Authentication
  slug: janus-machine-market-authentication
  summary_line: http · 1 scheme
- kind: vulnerability-disclosure
  name: Janus Machine Market Vulnerability Disclosure
  slug: janus-machine-market-vulnerability-disclosure
  summary_line: contact published
slug: janus-machine-market
tags:
- AI Agents
- Research
- Search
- Provenance
- Code Review
- GitHub Issues
- Agent Marketplace
website: https://hawkar-usls.github.io/JANUS-MACHINE-MARKET/
---
