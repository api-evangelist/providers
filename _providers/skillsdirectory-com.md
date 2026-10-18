---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-10-17'
api_count: 7
apis:
- description: Key-authenticated REST API (v1) to list, search (including Pro semantic search) and retrieve agent skills with their security grades, list categories, read key usage statistics, and scan a skill (ZIP,
  name: Skills Directory API
  slug: skills-directory-api
- description: Public, unauthenticated JSON API for CLI tools (designed for openskills) to list, search and fetch skills from the Skills Directory registry.
  name: Skills Directory Registry API
  slug: registry-api
- baseURL: https://www.skillsdirectory.com/api/v1
  baseurl_source: declared
  description: The Categories API from Skills Directory — 1 operation(s) for categories.
  name: Skills Directory Categories API
  slug: skillsdirectory-com-categories-api
- baseURL: https://www.skillsdirectory.com/api/v1
  baseurl_source: declared
  description: The Registry API from Skills Directory — 2 operation(s) for registry.
  name: Skills Directory Registry API
  slug: skillsdirectory-com-registry-api
- baseURL: https://www.skillsdirectory.com/api/v1
  baseurl_source: declared
  description: The Scan API from Skills Directory — 1 operation(s) for scan.
  name: Skills Directory Scan API
  slug: skillsdirectory-com-scan-api
- baseURL: https://www.skillsdirectory.com/api/v1
  baseurl_source: declared
  description: The Skills API from Skills Directory — 3 operation(s) for skills.
  name: Skills Directory Skills API
  slug: skillsdirectory-com-skills-api
- baseURL: https://www.skillsdirectory.com/api/v1
  baseurl_source: declared
  description: The Stats API from Skills Directory — 1 operation(s) for stats.
  name: Skills Directory Stats API
  slug: skillsdirectory-com-stats-api
artifact_total: 20
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/skillsdirectory-com/refs/heads/main/rate-limits/skillsdirectory-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/skillsdirectory-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/skillsdirectory-com/refs/heads/main/plans/skillsdirectory-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/skillsdirectory-com-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/skillsdirectory-com/refs/heads/main/authentication/skillsdirectory-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/skillsdirectory-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/skillsdirectory-com/refs/heads/main/errors/skillsdirectory-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/skillsdirectory-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/skillsdirectory-com/refs/heads/main/rules/skillsdirectory-com-rules.yml
  title: ''
  type: Spectral
  url: rules/skillsdirectory-com-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/skillsdirectory-com/refs/heads/main/json-ld/skillsdirectory-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/skillsdirectory-com-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/skillsdirectory-com/refs/heads/main/vocabulary/skillsdirectory-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/skillsdirectory-com-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/skillsdirectory-com/refs/heads/main/data-model/skillsdirectory-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/skillsdirectory-com-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/skillsdirectory-com/refs/heads/main/conformance/skillsdirectory-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/skillsdirectory-com-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/skillsdirectory-com/refs/heads/main/llms/skillsdirectory-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/skillsdirectory-com-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/skillsdirectory-com/refs/heads/main/hosts/skillsdirectory-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/skillsdirectory-com-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/skillsdirectory-com/refs/heads/main/vendors/skillsdirectory-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/skillsdirectory-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.skillsdirectory.com/security
- group: start
  title: ''
  type: Login
  url: https://app.skillsdirectory.com/sign-in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aggarcinuno
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.skillsdirectory.com/skills/for/developers
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/skillsdirectory-com/refs/heads/main/security/skillsdirectory-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/skillsdirectory-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/skillsdirectory-com/refs/heads/main/security/skillsdirectory-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/skillsdirectory-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.skillsdirectory.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.skillsdirectory.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.skillsdirectory.com/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.skillsdirectory.com/docs/getting-started
- group: agent
  title: ''
  type: MCPServer
  url: https://www.skillsdirectory.com/api/mcp
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.skillsdirectory.com/llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://www.skillsdirectory.com/pro
- group: company
  title: ''
  type: Blog
  url: https://www.skillsdirectory.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.skillsdirectory.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.skillsdirectory.com/privacy
- group: company
  title: ''
  type: About
  url: https://www.skillsdirectory.com/about
- group: other
  title: ''
  type: Sitemap
  url: https://www.skillsdirectory.com/sitemap.xml
- group: other
  title: ''
  type: RobotsTxt
  url: https://www.skillsdirectory.com/robots.txt
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.skillsdirectory.com/api/mcp
  - status: 401
    url: https://www.skillsdirectory.com/api/mcp
  - status: 200
    url: https://www.skillsdirectory.com/
  reason: partner-login
  state: gated
created: '2026-10-13'
description: Skills Directory (skillsdirectory.com) is a security-first directory of agent skills for Claude, Claude Code and other coding agents. It indexes over 100,000 skills, scans each one automatically for credential reads, network exfiltration, unpinned remote code and prompt-injection vectors, and publishes a public A-F security grade. It offers a key-authenticated REST API (v1) for listing, searching and scanning skills, a public Registry API for CLI installers, live security-grade badges, and a hosted MCP server for Claude Code for Pro members.
image: https://www.skillsdirectory.com/og-image.png
json_schemas:
- name: GetApiRegistryResponse
  property_count: 4
  slug: skillsdirectory-com-get-api-registry-response
- name: GetApiRegistrySlugResponse
  property_count: 3
  slug: skillsdirectory-com-get-api-registry-slug-response
- name: GetApiV1SkillsSlugResponse
  property_count: 2
  slug: skillsdirectory-com-get-api-v1-skills-slug-response
- name: PostApiV1ScanRequest
  property_count: 3
  slug: skillsdirectory-com-post-api-v1-scan-request
- name: PostApiV1ScanResponse
  property_count: 2
  slug: skillsdirectory-com-post-api-v1-scan-response
jsonld:
- class_count: 5
  name: Skillsdirectory Com Context
  property_count: 10
  slug: skillsdirectory-com-context
layout: provider
mcp_servers:
- description: ''
  name: Skills Directory MCP Server
  slug: mcp
modified: '2026-10-13'
name: Skills Directory
nav: Providers
network: true
overview: 'Skills Directory is listed with 7 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Registry API, Scan API, and 4 more. Tagged areas include Agent Skills, AI Agents, Claude, Directory, and Security Scanning.


  The Skills Directory catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Skills Directory''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, and 25 more developer resources.'
plans:
- name: Skillsdirectory Com Plans Pricing
  plan_count: 3
  slug: skillsdirectory-com-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Skillsdirectory Com Rate Limits
  slug: skillsdirectory-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Skills Directory API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: skillsdirectory-com-rules
score:
  band: developing
  composite: 50.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 89.8
    catalog_earned_first_party: 24.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 25.6
    developer_ergonomics: 52.4
    discoverability: 80.0
    operational_transparency: 47.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Skillsdirectory Com Authentication
  slug: skillsdirectory-com-authentication
  summary_line: apiKey/http-bearer · 2 schemes
- kind: domain-security
  name: Skillsdirectory Com Domain Security
  slug: skillsdirectory-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Skillsdirectory Com Vulnerability Disclosure
  slug: skillsdirectory-com-vulnerability-disclosure
  summary_line: no policy recorded
slug: skillsdirectory-com
tags:
- Agent Skills
- AI Agents
- Claude
- Directory
- Security Scanning
website: https://www.skillsdirectory.com/
---
