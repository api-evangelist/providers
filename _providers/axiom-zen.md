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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.8
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: ZenHub API provides endpoints for managing issues, pipelines, and analytics within GitHub repositories.
  name: ZenHub API
  slug: zenhub-api
artifact_total: 7
asyncapis:
- description: ''
  name: Axiom Zen Webhooks
  slug: axiom-zen-webhooks
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/axiom-zen/refs/heads/main/rate-limits/axiom-zen-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/axiom-zen-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/axiom-zen/refs/heads/main/plans/axiom-zen-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/axiom-zen-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axiom-zen/refs/heads/main/asyncapi/axiom-zen-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/axiom-zen-webhooks.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/axiom-zen/refs/heads/main/changelog/axiom-zen-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/axiom-zen-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axiom-zen/refs/heads/main/conventions/axiom-zen-conventions.yml
  title: ''
  type: Conventions
  url: conventions/axiom-zen-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axiom-zen/refs/heads/main/authentication/axiom-zen-authentication.yml
  title: ''
  type: Authentication
  url: authentication/axiom-zen-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/axiom-zen/refs/heads/main/llms/axiom-zen-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/axiom-zen-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/axiom-zen/refs/heads/main/mcp/axiom-zen-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/axiom-zen-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/axiom-zen/refs/heads/main/hosts/axiom-zen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/axiom-zen-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/axiom-zen/refs/heads/main/vendors/axiom-zen-vendors.yml
  title: ''
  type: Vendors
  url: vendors/axiom-zen-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zenhub.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.zenhub.com/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/ZenHubHQ/zenhub-enterprise/releases
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axiom-zen/refs/heads/main/security/axiom-zen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/axiom-zen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zenhub.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.zenhub.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://developers.zenhub.com/graphql-api-docs/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://www.zenhub.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.zenhub.com/
- group: company
  title: ''
  type: Blog
  url: https://www.zenhub.com/blog-posts
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zenhub.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zenhub.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zenhub.com/privacy-policy
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: null
    url: https://api.zenhub.com/mcp
  - status: 403
    url: https://help.zenhub.com/mcp
  - status: 403
    url: https://forgeglobal.com/axiom-zen_stock/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: ZenHub provides advanced project management tools tightly integrated with GitHub, enabling teams to plan, track, and deliver software efficiently. Features include hierarchical issue management, real-time reporting, AI‑assisted automation, and enterprise‑grade on‑premise deployments. ZenHub serves developers, product managers, and engineering leaders across a wide range of industries, helping them streamline workflows directly within GitHub.
image: https://www.zenhub.com/assets/webflow/66705b996a92992273ef8431_home-page-open-graph-image.jpg
layout: provider
mcp_servers:
- description: ''
  name: ZenHub MCP Server
  slug: zenhub-mcp-server
modified: '2026-09-27'
name: ZenHub
nav: Providers
network: true
overview: 'ZenHub publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Project Management, GitHub Integration, AI Automation, and Enterprise.


  The ZenHub catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ZenHub''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 16 more developer resources.'
plans:
- name: Axiom Zen Plans Pricing
  plan_count: 3
  slug: axiom-zen-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Axiom Zen Rate Limits
  slug: axiom-zen-rate-limits
score:
  band: developing
  composite: 47.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 52.0
    catalog_earned_first_party: 20.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 47.6
    discoverability: 68.3
    operational_transparency: 60.5
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Axiom Zen Authentication
  slug: axiom-zen-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Axiom Zen Domain Security
  slug: axiom-zen-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: axiom-zen
tags:
- Company
- Project Management
- GitHub Integration
- AI Automation
- Enterprise
website: https://www.zenhub.com
---
