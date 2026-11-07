---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.makeswift.com
  baseurl_source: declared
  description: The locale API from Makeswift — 3 operation(s) for locale.
  name: Makeswift Locale API
  slug: makeswift-locale-api
- baseURL: https://api.makeswift.com
  baseurl_source: declared
  description: The page API from Makeswift — 2 operation(s) for page.
  name: Makeswift Page API
  slug: makeswift-page-api
- baseURL: https://api.makeswift.com
  baseurl_source: declared
  description: The site API from Makeswift — 3 operation(s) for site.
  name: Makeswift Site API
  slug: makeswift-site-api
- baseURL: https://api.makeswift.com
  baseurl_source: declared
  description: The region API from Makeswift — 3 operation(s) for region.
  name: Makeswift Region API
  slug: makeswift-region-api
- baseURL: https://api.makeswift.com
  baseurl_source: declared
  description: The swatch API from Makeswift — 2 operation(s) for swatch.
  name: Makeswift Swatch API
  slug: makeswift-swatch-api
- baseURL: https://api.makeswift.com
  baseurl_source: declared
  description: The typography API from Makeswift — 2 operation(s) for typography.
  name: Makeswift Typography API
  slug: makeswift-typography-api
artifact_total: 19
collections:
- collection_type: open
  name: REST locale API
  slug: open-makeswift-locale-api
- collection_type: open
  name: REST locale page API
  slug: open-makeswift-page-api
- collection_type: open
  name: REST locale site API
  slug: open-makeswift-site-api
common:
- group: other
  href: https://artifacts.apis.io/makeswift/capabilities/makeswift-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/makeswift-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/makeswift/plans/makeswift-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/makeswift-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/makeswift/overlays/makeswift-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/makeswift-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://makeswift.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.makeswift.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://docs.makeswift.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.makeswift.com/developer/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.makeswift.com/developer/docs/get-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://makeswift.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://makeswift.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.makeswift.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.makeswift.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/makeswift
- group: operate
  title: ''
  type: StatusPage
  url: https://status.makeswift.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.makeswift.com/developer/changelog
- group: build
  href: https://artifacts.apis.io/makeswift/packages/makeswift-packages.yml
  title: ''
  type: Packages
  url: packages/makeswift-packages.yml
- group: build
  href: https://artifacts.apis.io/makeswift/packages/makeswift-packages.yml
  title: ''
  type: SDKs
  url: packages/makeswift-packages.yml
- group: build
  href: https://artifacts.apis.io/makeswift/cli/makeswift-cli.yml
  title: ''
  type: CLI
  url: cli/makeswift-cli.yml
- group: agent
  href: https://artifacts.apis.io/makeswift/mcp/makeswift-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/makeswift-mcp.yml
- group: agent
  href: https://artifacts.apis.io/makeswift/llms/makeswift-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/makeswift-llms.txt
- group: agent
  href: https://artifacts.apis.io/makeswift/well-known/makeswift-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/makeswift-well-known.yml
- group: design
  href: https://artifacts.apis.io/makeswift/lifecycle/makeswift-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/makeswift-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/makeswift/security/makeswift-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/makeswift-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/makeswift/authentication/makeswift-authentication.yml
  title: ''
  type: Authentication
  url: authentication/makeswift-authentication.yml
- group: agent
  href: https://artifacts.apis.io/makeswift/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Makeswift is a composable visual page builder for marketing teams and developers, built for Next.js. It lets marketers visually design, edit, and publish modern web frontends while developers register their own React components and keep full control over hosting and code. Makeswift ships an official React runtime SDK (@makeswift/runtime), a CLI, and a REST API at api.makeswift.com for programmatically managing sites, pages, and locales, plus a hosted documentation MCP server for AI clients. Makeswift is backed by Techstars and partners closely with BigCommerce for composable commerce.
finops:
- has_sources: true
  method: derived
  name: Makeswift Finops
  primary_unit: subscription
  service_category: ''
  slug: makeswift-finops
  template: false
image: https://makeswift.com/
layout: provider
mcp_servers:
- description: ''
  name: Makeswift MCP Server
  slug: makeswift-mcp-yml
modified: '2026-07-20'
name: Makeswift
nav: Providers
network: true
overview: 'Makeswift publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Locale API, Page API, Site API, and 3 more. Tagged areas include Company, Visual Page Builder, Website Builder, Next.js, and Headless CMS.


  The Makeswift catalog on APIs.io includes 1 Spectral governance ruleset.


  Makeswift''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 18 more developer resources.'
plans:
- name: Makeswift Plans Pricing
  plan_count: 7
  slug: makeswift-plans-pricing
- name: Makeswift Price Estimates
  plan_count: 0
  slug: makeswift-price-estimates
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Makeswift API Rules
  rule_count: 56
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 3
  slug: makeswift-rules
score:
  band: developing
  composite: 54.2
  coverage:
    artifact_dirs: 28
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 58.0
    developer_ergonomics: 68.5
    discoverability: 71.7
    operational_transparency: 34.2
  previous_composite: 53.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 66.7
      total: 9
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/makeswift/makeswift-2026-07-25T225954.png
security:
- kind: authentication
  name: Makeswift Authentication
  slug: makeswift-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Makeswift Domain Security
  slug: makeswift-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: Configure Makeswift Localization
  slug: makeswift-configure-localization
- name: Manage Makeswift Pages
  slug: makeswift-manage-pages
- name: Manage Makeswift Sites
  slug: makeswift-manage-sites
slug: makeswift
tags:
- Company
- Visual Page Builder
- Website Builder
- Next.js
- Headless CMS
- Composable
- Content Management
- Web Development
- Developer Tools
website: https://makeswift.com/
---
