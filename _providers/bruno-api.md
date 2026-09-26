---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.6
  scored_at: '2026-09-25'
api_count: 6
apis:
- description: The core open-source, git-native desktop API client (a lightweight Postman/Insomnia alternative). Compose and send HTTP, REST, GraphQL, and gRPC requests, organize them into collections, manage enviro
  name: Bruno API Client
  slug: bruno-api-client
- description: Bru is Bruno's plain-text domain-specific markup language. Each request is stored as a .bru file capturing the HTTP method, URL, query params, headers, body, authentication, scripts, tests, assertions
  name: Bru Markup Language (.bru)
  provenance: unpublished
  slug: bruno-bru-language
- description: 'OpenCollection is the open, YAML-based collection format Bruno now recommends for new collections as an alternative representation to .bru. Like .bru it stores requests, folders, auth, and scripts as '
  name: OpenCollection Format
  provenance: unpublished
  slug: bruno-opencollection
- description: The @usebruno/cli command-line runner (invoked as bru, installed via npm install -g @usebruno/cli) executes individual requests or entire collections headlessly for CI/CD, with JSON, JUnit, and HTML t
  name: Bruno CLI (bru)
  slug: bruno-cli
- description: Paid Bruno (Pro and Ultimate) adds native in-app Git integration and OpenAPI sync (5 syncs/month on Pro, unlimited on Ultimate) plus SSO, SCIM, audit logs, and license/admin controls. Collaboration ha
  name: Bruno Git Integration and Sync
  provenance: unpublished
  slug: bruno-git-collaboration
- description: Bruno is an open-source API client for exploring and testing REST, GraphQL, and gRPC APIs. Collections are stored as plain text Bru files on the filesystem, enabling Git-based version control, team co
  name: Bruno API Client
  slug: api-client
artifact_total: 13
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bruno-api/refs/heads/main/vendor-facets/bruno-api-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/bruno-api-vendor-facets.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bruno-api/refs/heads/main/security/bruno-api-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bruno-api-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bruno-api/refs/heads/main/security/bruno-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bruno-api-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usebruno
- group: company
  title: ''
  type: Website
  url: https://www.usebruno.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usebruno.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usebruno
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bruno-api/refs/heads/main/plans/bruno-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bruno-api-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bruno-api/refs/heads/main/rate-limits/bruno-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bruno-api-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bruno-api/refs/heads/main/finops/bruno-api-finops.yml
  title: ''
  type: FinOps
  url: finops/bruno-api-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.usebruno.com/
- group: company
  title: ''
  type: Blog
  url: https://www.usebruno.com/blog
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bruno-api/refs/heads/main/a2a/bruno-api-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/bruno-api-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bruno-api/refs/heads/main/mcp/bruno-api-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bruno-api-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bruno-api/refs/heads/main/well-known/bruno-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bruno-api-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bruno-api/refs/heads/main/llms/bruno-api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bruno-api-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bruno-api/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bruno-api/refs/heads/main/packages/bruno-api-packages.yml
  title: ''
  type: Packages
  url: packages/bruno-api-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bruno-api/refs/heads/main/packages/bruno-api-packages.yml
  title: ''
  type: SDKs
  url: packages/bruno-api-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bruno-api/refs/heads/main/cli/bruno-api-cli.yml
  title: ''
  type: CLI
  url: cli/bruno-api-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bruno-api/refs/heads/main/changelog/bruno-api-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bruno-api-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://www.usebruno.com/changelog
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bruno-api/refs/heads/main/lifecycle/bruno-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bruno-api-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bruno-api/refs/heads/main/conformance/bruno-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bruno-api-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bruno-api/refs/heads/main/security/bruno-api-trust-center.yml
  title: ''
  type: Compliance
  url: security/bruno-api-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bruno-api/refs/heads/main/security/bruno-api-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/bruno-api-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bruno-api/refs/heads/main/security/bruno-api-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bruno-api-vulnerability-disclosure.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.usebruno.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.usebruno.com/introduction/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.usebruno.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.usebruno.com/start-trial
- group: operate
  title: ''
  type: Support
  url: https://www.usebruno.com/support
- group: operate
  title: ''
  type: Community
  url: https://www.usebruno.com/community
- group: operate
  title: ''
  type: Roadmap
  url: https://www.usebruno.com/roadmap
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usebruno.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usebruno.com/privacy-policy
created: '2026-07-11'
description: Bruno is an open-source (MIT), git-native API client - a lightweight, offline-first alternative to Postman and Insomnia for exploring and testing APIs. It is a developer TOOL, not a hosted HTTP API provider. Collections are stored on the local filesystem as folders of plain-text files (the .bru "Bru" markup language, with OpenCollection YAML now recommended for new collections), so API requests are version-controlled in Git alongside code. Bruno sends HTTP, REST, GraphQL, and gRPC requests, manages environments and variables, and runs pre-request/post-response scripts, tests, and assertions. The @usebruno/cli command-line runner (bru) executes collections headlessly in CI/CD with JSON, JUnit, and HTML reporters. Bruno is offline-only and does not sync request data to a Bruno-hosted cloud; paid Pro/Ultimate tiers add native in-app Git integration, OpenAPI sync, and enterprise admin controls that run through your own Git provider and identity systems. Bruno does not expose a documented
  public REST HTTP API.
finops:
- name: Bruno Api Finops
  service_category: Developer Tools
  slug: bruno-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bruno-api.png
layout: provider
mcp_servers:
- description: Bruno ships TWO distinct, first-party MCP surfaces, and they are not interchangeable. (1) A REMOTE, unauthenticated HTTP MCP server on Bruno's own documentation host that any agent can POST to right n
  name: Bruno MCP surfaces
  slug: bruno-mcp-surfaces
modified: '2026-09-18'
name: Bruno
nav: Providers
network: true
overview: 'Bruno publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Client, API Testing, Developer Tools, Open Source, and Git-Native.


  Bruno''s developer surface includes documentation, engineering blog, CLI, changelog, release notes, getting-started guide, pricing, and 29 more developer resources.'
plans:
- name: Bruno Api Plans Pricing
  plan_count: 4
  slug: bruno-api-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Bruno Api Rate Limits
  slug: bruno-api-rate-limits
score:
  band: developing
  composite: 51.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 62.0
    catalog_earned_first_party: 24.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.0
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 71.7
    operational_transparency: 65.8
  previous_composite: 49.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/bruno-api/refs/heads/main/screenshots/bruno-api-2026-07-25T204007.png
security:
- kind: domain-security
  name: Bruno Api Domain Security
  slug: bruno-api-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bruno Api Vulnerability Disclosure
  slug: bruno-api-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Bruno Api Trust Center
  slug: bruno-api-trust-center
  summary_line: SOC 2 Type I
slug: bruno-api
tags:
- API Client
- API Testing
- Developer Tools
- Open Source
- Git-Native
- CLI
- Postman Alternative
- A2A
- Testing
website: https://www.usebruno.com/
---
