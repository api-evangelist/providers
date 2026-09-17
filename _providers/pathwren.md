---
access_model:
  confidence: high
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 48.1
  scored_at: '2026-09-16'
api_count: 2
apis:
- baseURL: https://www.pathwren.workers.dev
  baseurl_source: declared
  description: The whole dataset in several shapes.
  name: AI Crawler Index Bulk API
  slug: pathwren-bulk-api
- baseURL: https://www.pathwren.workers.dev
  baseurl_source: declared
  description: One record per crawler.
  name: AI Crawler Index Crawlers API
  slug: pathwren-crawlers-api
- baseURL: https://www.pathwren.workers.dev
  baseurl_source: declared
  description: Operator-published prefixes, normalised.
  name: AI Crawler Index Ip Ranges API
  slug: pathwren-ip-ranges-api
- baseURL: https://www.pathwren.workers.dev
  baseurl_source: declared
  description: Ready-made robots.txt policy files.
  name: AI Crawler Index Robots API
  slug: pathwren-robots-api
- baseURL: https://www.pathwren.workers.dev
  baseurl_source: declared
  description: Freshness of the upstream sources.
  name: AI Crawler Index Status API
  slug: pathwren-status-api
artifact_total: 12
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pathwren/refs/heads/main/overlays/pathwren-ai-crawler-index-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pathwren-ai-crawler-index-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://pathwren.workers.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.pathwren.workers.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pathwren.workers.dev/api.html
- group: operate
  title: ''
  type: Support
  url: https://www.pathwren.workers.dev/about.html
- group: commercial
  title: ''
  type: License
  url: https://creativecommons.org/publicdomain/zero/1.0/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.pathwren.workers.dev/status.html
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/pathwren/refs/heads/main/changelog/pathwren-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/pathwren-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pathwren/refs/heads/main/well-known/pathwren-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pathwren-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pathwren/refs/heads/main/well-known/pathwren-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pathwren-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pathwren/refs/heads/main/security/pathwren-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/pathwren-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pathwren/refs/heads/main/security/pathwren-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pathwren-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pathwren/refs/heads/main/security/pathwren-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pathwren-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pathwren/refs/heads/main/llms/pathwren-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pathwren-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pathwren/refs/heads/main/mcp/pathwren-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pathwren-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pathwren/refs/heads/main/a2a/pathwren-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/pathwren-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pathwren/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pathwren/refs/heads/main/packages/pathwren-packages.yml
  title: ''
  type: Packages
  url: packages/pathwren-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pathwren/refs/heads/main/conformance/pathwren-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pathwren-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pathwren/refs/heads/main/lifecycle/pathwren-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pathwren-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/pathwren/refs/heads/main/plans/pathwren-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pathwren-plans-pricing.yml
created: '2026-08-31'
description: 'Every AI crawler on the web, what it is for, what blocking it costs you, and the IP ranges its operator publishes — as JSON, CSV, robots.txt and regex. 56 crawlers from 30 operators, 1887 IPv4 and 1056 IPv6 prefixes mirrored from 12 operator-published endpoints and refreshed every six hours. Read-only static files: no key, no signup, no rate limit, CORS open, CC0.'
image: https://www.pathwren.workers.dev/icon.png
json_schemas:
- name: Crawler
  property_count: 17
  slug: pathwren-crawler.schema
layout: provider
mcp_servers:
- description: ''
  name: AI Crawler Index MCP Server
  slug: ai-crawler-index-mcp-server
modified: '2026-09-16'
name: AI Crawler Index
nav: Providers
network: true
overview: 'AI Crawler Index publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Bulk API, Crawlers API, Ip Ranges API, and 2 more. Tagged areas include AI crawlers, web crawlers, Robots.txt, User Agents, and Bot Detection.


  AI Crawler Index''s developer surface includes documentation, support, changelog, and 18 more developer resources.'
plans:
- name: Pathwren Plans Pricing
  plan_count: 1
  slug: pathwren-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Pathwren Rate Limits
  slug: pathwren-rate-limits
score:
  band: developing
  composite: 47.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 51.0
    catalog_earned_first_party: 8.0
    catalog_gap: 64.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.3
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 50.7
    developer_ergonomics: 56.5
    discoverability: 83.3
    operational_transparency: 42.1
  previous_composite: 45.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 42.6
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/pathwren/refs/heads/main/screenshots/pathwren-2026-09-02T150912.png
security:
- kind: authentication
  name: Pathwren Authentication
  slug: pathwren-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Pathwren Domain Security
  slug: pathwren-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pathwren Vulnerability Disclosure
  slug: pathwren-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: pathwren
tags:
- AI crawlers
- web crawlers
- Robots.txt
- User Agents
- Bot Detection
- GPTBot
- ClaudeBot
- crawler IP ranges
- llms-txt
- Open Data
website: https://pathwren.workers.dev
---
