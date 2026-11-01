---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Agent-first image hosting API. Upload images via API, get instant CDN URLs. Free tier: 200 MB storage, 500 uploads/month, 1 GB bandwidth/month.'
  name: PixelVault API
  slug: pixelvault-api
artifact_total: 8
common:
- group: operate
  href: https://artifacts.apis.io/pixelvault-dev/rate-limits/pixelvault-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pixelvault-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/pixelvault-dev/plans/pixelvault-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pixelvault-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/pixelvault-dev/json-ld/pixelvault-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pixelvault-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/pixelvault-dev/vocabulary/pixelvault-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pixelvault-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/pixelvault-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/pixelvault-dev/data-model/pixelvault-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pixelvault-dev-data-model.yml
- group: build
  href: https://artifacts.apis.io/pixelvault-dev/cli/pixelvault-dev-cli.yml
  title: ''
  type: CLI
  url: cli/pixelvault-dev-cli.yml
- group: auth
  href: https://artifacts.apis.io/pixelvault-dev/authentication/pixelvault-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pixelvault-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/pixelvault-dev/conformance/pixelvault-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pixelvault-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/pixelvault-dev/llms/pixelvault-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pixelvault-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/pixelvault-dev/mcp/pixelvault-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pixelvault-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/pixelvault-dev/well-known/pixelvault-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pixelvault-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/pixelvault-dev/hosts/pixelvault-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pixelvault-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/pixelvault-dev/vendors/pixelvault-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pixelvault-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/pixelvault-dev/packages/pixelvault-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/pixelvault-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/pixelvault-dev/packages/pixelvault-dev-packages.yml
  title: ''
  type: Packages
  url: packages/pixelvault-dev-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://pixelvault.dev/status/
- group: auth
  href: https://artifacts.apis.io/pixelvault-dev/security/pixelvault-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pixelvault-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pixelvault.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://pixelvault.dev/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.pixelvault.dev/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://pixelvault.dev/docs/#quickstart
- group: operate
  title: ''
  type: Support
  url: https://pixelvault.dev/contact/
- group: company
  title: ''
  type: Blog
  url: https://pixelvault.dev/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pixelvault-dev
- group: commercial
  title: ''
  type: Pricing
  url: https://pixelvault.dev/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://pixelvault.dev/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pixelvault.dev/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pixelvault.dev/privacy/
created: '2026-10-30'
description: PixelVault provides image infrastructure for AI agents and developers, offering an API and CDN to upload, transform, and deliver images. Users can register via a password‑less account, upload images through REST, MCP, or CLI, and obtain permanent CDN URLs. The service includes on‑the‑fly transformations, AI background removal, and a free tier with 200 MB storage, 500 uploads/month, and 1 GB bandwidth. Built by RumboLabs, PixelVault aims to simplify image handling in applications and AI workflows.
image: https://pixelvault.dev/og-image.png
jsonld:
- class_count: 2
  name: Pixelvault Dev Context
  property_count: 15
  slug: pixelvault-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.pixelvault.dev requiring an API key.
  name: pixelvault-dev MCP Server
  slug: pixelvault-dev-mcp-yml
modified: '2026-10-30'
name: pixelvault-dev
nav: Providers
network: true
overview: 'pixelvault-dev is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Image Hosting, CDN, API, AI Agents, and Developer Tools.


  The pixelvault-dev catalog on APIs.io includes 1 JSON-LD context.


  pixelvault-dev''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 22 more developer resources.'
plans:
- name: Pixelvault Dev Plans Pricing
  plan_count: 3
  slug: pixelvault-dev-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 7
  name: Pixelvault Dev Rate Limits
  slug: pixelvault-dev-rate-limits
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 71.1
    catalog_earned_first_party: 0.0
    catalog_gap: 43.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 30.0
    contract_quality: 10.7
    developer_ergonomics: 68.3
    discoverability: 65.0
    operational_transparency: 49.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Pixelvault Dev Authentication
  slug: pixelvault-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pixelvault Dev Domain Security
  slug: pixelvault-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: claude-code
  slug: pixelvault-dev-claude-code
slug: pixelvault-dev
tags:
- Image Hosting
- CDN
- API
- AI Agents
- Developer Tools
website: https://pixelvault.dev/
---
