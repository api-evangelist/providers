---
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 35.3
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://app.yoodli.ai/api
  baseurl_source: declared
  description: Yoodli's public REST API (OpenAPI 3.1.0, 13 operations) for administrative programmatic access to the platform — listing, inviting and removing Organization members, creating, updating and deleting Us
  name: Yoodli API
  slug: yoodli-api
artifact_total: 8
asyncapis:
- description: ''
  name: Yoodli Web Embed Events
  slug: yoodli-web-embed-events
common:
- group: company
  title: ''
  type: Website
  url: https://yoodli.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.yoodli.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.yoodli.ai/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developers.yoodli.ai/reference/get_v3-orgs-orgid-users
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.yoodli.ai/docs/quickstart
- group: auth
  title: ''
  type: Authentication
  url: authentication/yoodli-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://support.yoodli.ai/
- group: company
  title: ''
  type: Blog
  url: https://yoodli.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Yoodli
- group: commercial
  title: ''
  type: Pricing
  url: https://yoodli.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.yoodli.ai/signup
- group: start
  title: ''
  type: Login
  url: https://app.yoodli.ai/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://yoodli.ai/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://yoodli.ai/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://yoodli.statuspage.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.yoodli.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.yoodli.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.yoodli.ai/changelog
- group: agent
  title: ''
  type: MCPServer
  url: mcp/yoodli-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/yoodli-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yoodli-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/yoodli-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/yoodli-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/yoodli-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/yoodli-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/yoodli-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/yoodli-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/yoodli-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/yoodli-packages.yml
- group: design
  title: ''
  type: Components
  url: components/yoodli-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yoodli-domain-security.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/yoodli-changelog.yml
created: '2026-09-04'
description: 'Yoodli is a Seattle-based AI communication coaching company, founded in 2021 by former Google engineers and spun out of the Allen Institute for AI incubator. Its platform runs AI roleplays and speech analysis so sales, leadership, L&D and customer-facing teams can rehearse high-stakes conversations — pitches, interviews, performance reviews, discovery calls — and get private, rubric-scored feedback on filler words, pacing, and content. Yoodli publishes a REST API (OpenAPI 3.1.0, base https://app.yoodli.ai/api) for administrative programmatic access: managing Organization members, User Groups (hubs), invites and membership expirations, Multi Org seat allocation, and downloading a recording''s rubric goal scores, coaching feedback, reviewer comments and transcript. It also ships a Web Embed API (iframe + postMessage) for embedding Yoodli activities in a host application, and a remote MCP server over its ReadMe developer portal.'
image: https://files.readme.io/00bff5691627b960ef3c81cd866921c2c7e950e9f964ec08eb36d59b5e1d307a-yoodli_logo_purplebg_16_9.svg
layout: provider
mcp_servers:
- description: ''
  name: Yoodli MCP Server
  slug: yoodli-mcp-server
modified: '2026-09-04'
name: Yoodli
nav: Providers
network: true
overview: 'Yoodli publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Communication, Coaching, Learning and Development, and Sales Enablement.


  The Yoodli catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Yoodli''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, pricing, and 26 more developer resources.'
plans:
- name: Yoodli Plans Pricing
  plan_count: 4
  slug: yoodli-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Yoodli Rate Limits
  slug: yoodli-rate-limits
score:
  band: strong
  composite: 61.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 4.5
    contract_quality: 59.1
    developer_ergonomics: 58.9
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 68.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: authentication
  name: Yoodli Authentication
  slug: yoodli-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Yoodli Domain Security
  slug: yoodli-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Yoodli Trust Center
  slug: yoodli-trust-center
  summary_line: SOC 2 Type 2, GDPR
slug: yoodli
tags:
- Artificial Intelligence
- Communication
- Coaching
- Learning and Development
- Sales Enablement
- Speech Analysis
- Human Resources
- Enterprise Software
- SaaS
- Identity Management
website: https://yoodli.ai/
---
