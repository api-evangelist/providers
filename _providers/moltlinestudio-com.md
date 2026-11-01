---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Moltlinestudio Com Agentic Access
  operation_count: 6
  slug: moltlinestudio-com-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 1
apis:
- baseURL: https://moltlinestudio.com
  baseurl_source: declared
  description: The Agent Check API from moltlinestudio-com — 2 operation(s) for agent check.
  name: moltlinestudio-com Agent Check API
  slug: moltlinestudio-com-agent-check-api
- baseURL: https://moltlinestudio.com
  baseurl_source: declared
  description: The Auth.md API from moltlinestudio-com — 1 operation(s) for auth.md.
  name: moltlinestudio-com Auth.md API
  slug: moltlinestudio-com-auth-md-api
- baseURL: https://moltlinestudio.com
  baseurl_source: declared
  description: The Badge API from moltlinestudio-com — 1 operation(s) for badge.
  name: moltlinestudio-com Badge API
  slug: moltlinestudio-com-badge-api
- baseURL: https://moltlinestudio.com
  baseurl_source: declared
  description: The Premium API from moltlinestudio-com — 2 operation(s) for premium.
  name: moltlinestudio-com Premium API
  slug: moltlinestudio-com-premium-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/moltlinestudio-com/agentic-access/moltlinestudio-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/moltlinestudio-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/moltlinestudio-com/plans/moltlinestudio-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/moltlinestudio-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/moltlinestudio-com/rules/moltlinestudio-com-rules.yml
  title: ''
  type: Spectral
  url: rules/moltlinestudio-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/moltlinestudio-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://moltlinestudio.com/terms.html
- group: auth
  href: https://artifacts.apis.io/moltlinestudio-com/authentication/moltlinestudio-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/moltlinestudio-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/moltlinestudio-com/errors/moltlinestudio-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/moltlinestudio-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/moltlinestudio-com/conformance/moltlinestudio-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/moltlinestudio-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/moltlinestudio-com/llms/moltlinestudio-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/moltlinestudio-com-llms.txt
- group: other
  href: https://artifacts.apis.io/moltlinestudio-com/a2a/moltlinestudio-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/moltlinestudio-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/moltlinestudio-com/well-known/moltlinestudio-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/moltlinestudio-com-security.txt
- group: auth
  href: https://artifacts.apis.io/moltlinestudio-com/well-known/moltlinestudio-com-community-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/moltlinestudio-com-community-security.txt
- group: auth
  href: https://artifacts.apis.io/moltlinestudio-com/well-known/moltlinestudio-com-articles-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/moltlinestudio-com-articles-security.txt
- group: auth
  href: https://artifacts.apis.io/moltlinestudio-com/well-known/moltlinestudio-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/moltlinestudio-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/moltlinestudio-com/well-known/moltlinestudio-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/moltlinestudio-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/moltlinestudio-com/hosts/moltlinestudio-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/moltlinestudio-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/moltlinestudio-com/vendors/moltlinestudio-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/moltlinestudio-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/moltlinestudio-com/security/moltlinestudio-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/moltlinestudio-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/moltlinestudio-com/security/moltlinestudio-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/moltlinestudio-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://moltlinestudio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://moltlinestudio.com/servers.html
- group: docs
  title: ''
  type: APIReference
  url: https://moltlinestudio.com/.well-known/api-catalog
- group: start
  title: ''
  type: GettingStarted
  url: https://moltlinestudio.com/connect.html
- group: operate
  title: ''
  type: Support
  url: mailto:support@moltlinestudio.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://moltlinestudio.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://moltlinestudio.com/privacy.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GarphenGate
created: '2026-10-29'
description: Moltline Studio provides AI agent skills, persona bundles, and hosted MCP servers. With 22 MCP servers and 138 skill bundles, the free tier never expires, offering 110 free tools. An All‑Access license for $19 unlocks premium tools. The platform integrates with Claude and other AI agents via a single URL, requires no account, API key, or OAuth, and includes comprehensive support terms. It offers real analyzers, code review, governance audits, and a marketplace for kits and bundles.
image: https://moltlinestudio.com/og-image.png
layout: provider
modified: '2026-10-29'
name: moltlinestudio-com
nav: Providers
network: true
overview: 'moltlinestudio-com publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Check API, Auth.md API, Badge API, and 1 more. Tagged areas include AI, MCP, Agent Skills, Platform, and Tools.


  The moltlinestudio-com catalog on APIs.io includes 1 Spectral governance ruleset.


  moltlinestudio-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, and 22 more developer resources.'
plans:
- name: Moltlinestudio Com Plans Pricing
  plan_count: 2
  slug: moltlinestudio-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Moltlinestudio Com Rate Limits
  slug: moltlinestudio-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: moltlinestudio-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: moltlinestudio-com-rules
scopes:
- name: Moltlinestudio Com Scopes
  scope_count: 0
  slug: moltlinestudio-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 31.8
    contract_quality: 45.9
    developer_ergonomics: 51.7
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 37.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Moltlinestudio Com Authentication
  slug: moltlinestudio-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Moltlinestudio Com Domain Security
  slug: moltlinestudio-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Moltlinestudio Com Vulnerability Disclosure
  slug: moltlinestudio-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: agent-readiness
  slug: moltlinestudio-com-agent-readiness
- name: purchase-all-access
  slug: moltlinestudio-com-purchase-all-access
slug: moltlinestudio-com
tags:
- AI
- MCP
- Agent Skills
- Platform
- Tools
website: https://moltlinestudio.com/
---
