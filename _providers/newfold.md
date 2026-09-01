---
access_model:
  confidence: medium
  label: Open Source
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://github.com/newfold-labs
  - https://newfold-labs.github.io/satis/
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.3
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: The Newfold Labs WordPress MCP module (wp-module-mcp) registers an MCP server, id blu-mcp, on the WordPress REST route /wp-json/blu/mcp of every site running a Newfold brand plugin. It exposes WordPre
  name: Newfold BLU MCP Server (WordPress)
  slug: blu-mcp
- description: Hiive is Newfold's site-connection platform API. The GPL-licensed Newfold data module (wp-module-data), installed on every site running a Newfold brand plugin, defines the base https://hiive.cloud/api
  name: Hiive Platform API
  slug: hiive
- description: 'HUAPI is Newfold''s internal hosting control-plane API, versioned under /v1, covering account, hosting, sites, domains, addons (backup, CodeGuard, SiteLock, Xcitium, Cloudflare, SpamExperts, Jetpack), '
  name: HUAPI (Hosting Unified API)
  slug: huapi
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/newfold-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://newfold.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/newfold-labs
- group: docs
  title: ''
  type: Documentation
  url: https://newfold-labs.github.io/standards/
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/newfold-labs/wp-module-mcp/blob/main/docs/api.md
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/newfold-labs/wp-module-mcp/blob/main/docs/getting-started.md
- group: operate
  title: ''
  type: Support
  url: https://github.com/newfold-labs/wp-module-mcp/issues
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://newfold.com/privacy-center/privacy
- group: auth
  title: ''
  type: Security
  url: https://newfold.com/disclosure
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/newfold-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: https://newfold.com/privacy-center/information-security-policy
- group: build
  title: ''
  type: Packages
  url: packages/newfold-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/newfold-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/newfold-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/newfold-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/newfold-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/newfold-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/newfold-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/newfold-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/newfold-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/newfold-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/newfold-cli.yml
- group: design
  title: ''
  type: Components
  url: components/newfold-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/newfold-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/newfold-rate-limits.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/newfold-standards-frontmatter.schema.json
created: '2026-07-17'
description: Newfold Digital is a web presence and technology solutions company serving small and medium businesses worldwide with domain registration, web hosting, website building, e-commerce, security, and digital marketing. It was formed in 2021 from the merger of Web.com Group and Endurance International Group and operates a portfolio of consumer and reseller brands including Bluehost, HostGator, Network Solutions, Register.com, Web.com, and Domain.com. The corporate site newfold.com is an investor and company presence rather than a unified developer portal, and it sits behind a Cloudflare interactive challenge. The company's real public developer surface is Newfold Labs (github.com/newfold-labs), an 85-repository engineering org that ships the brand WordPress plugins, a Composer module fleet distributed from its own Satis registry, public npm packages under the @newfold scope, a published engineering standards site with an llms.txt, and an MCP server module that exposes WordPress abilities
  to AI assistants from each customer site.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/newfold.png
json_schemas:
- name: Newfold Labs standards document front matter
  property_count: 11
  slug: newfold-standards-frontmatter.schema
layout: provider
mcp_servers:
- description: Newfold Labs ships an MCP server as a WordPress module (newfold-labs/wp-module-mcp, Composer, GPL-2.0-or-later) that brand plugins — Bluehost and siblings — load into the customer's own WordPress inst
  name: Newfold BLU MCP Server
  slug: newfold-blu-mcp-server
modified: '2026-08-13'
name: Newfold
nav: Providers
network: true
overview: 'Newfold publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Web Hosting, Domains, Web Presence, and Website Builder.


  Newfold''s developer surface includes documentation, API reference, getting-started guide, support, authentication, changelog, CLI, and 20 more developer resources.'
plans:
- name: Newfold Plans Pricing
  plan_count: 0
  slug: newfold-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Newfold Rate Limits
  slug: newfold-rate-limits
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 18
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 61.3
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 29.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/newfold/refs/heads/main/screenshots/newfold-2026-08-07T185102.png
security:
- kind: authentication
  name: Newfold Authentication
  slug: newfold-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Newfold Domain Security
  slug: newfold-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Newfold Vulnerability Disclosure
  slug: newfold-vulnerability-disclosure
  summary_line: Hackerone
slug: newfold
tags:
- Company
- Web Hosting
- Domains
- Web Presence
- Website Builder
- Digital Marketing
- Small Business
- WordPress
- Open-Source
- MCP
- E-Commerce
website: https://newfold.com
---
