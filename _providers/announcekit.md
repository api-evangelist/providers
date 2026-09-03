---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.8
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The AnnounceKit API provides GraphQL and REST endpoints for programmatically creating and updating posts, syncing user data, managing widgets, and automating product changelog workflows. Supports 11 w
  name: AnnounceKit API
  slug: announcekit-api
artifact_total: 11
asyncapis:
- description: ''
  name: Announcekit Webhooks
  slug: announcekit-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/announcekit-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/announcekit-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/announcekit
- group: company
  title: ''
  type: Website
  url: https://announcekit.app/
- group: docs
  title: ''
  type: Documentation
  url: https://announcekit.app/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://announcekit.app/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://changelog.announcekit.app/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/announcekitapp
- group: build
  title: ''
  type: Examples
  url: https://announcekit.app/examples
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://announcekit.app/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://announcekit.app/terms-of-service
- group: company
  title: ''
  type: Blog
  url: https://announcekit.app/blog/
- group: build
  title: ''
  type: Packages
  url: packages/announcekit-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/announcekit-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/announcekit-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/announcekit-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/announcekit-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/announcekit-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/announcekit-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: security/announcekit-trust-center.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.announcekit.app/
- group: operate
  title: ''
  type: Support
  url: https://help.announcekit.app
- group: operate
  title: ''
  type: Roadmap
  url: https://announcekit.app/product-roadmap
- group: start
  title: ''
  type: SignUp
  url: https://announcekit.app/dashboard/register
- group: start
  title: ''
  type: Login
  url: https://announcekit.app/dashboard/login
- group: docs
  title: ''
  type: Documentation
  url: https://announcekit.app/docs/mcp
created: '2026-03-29'
description: AnnounceKit is a product communication platform providing changelog management, in-app notification widgets, feature request boards, roadmaps, and NPS surveys. It enables product teams to communicate updates to users via 10+ widget display modes, email digests, Slack, webhooks, and RSS, with GraphQL and REST APIs for programmatic integration.
finops:
- name: Announcekit Finops
  service_category: API
  slug: announcekit-finops
graphqls:
- description: 'generated: ''2026-09-02'''
  name: AnnounceKit GraphQL API
  slug: announcekit-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/announcekit.png
layout: provider
mcp_servers:
- description: 'AnnounceKit publishes a first-party Model Context Protocol server that wraps its GraphQL API. It ships two ways from one codebase: a hosted Streamable-HTTP endpoint an agent can call today, and an npx'
  name: AnnounceKit MCP Server
  slug: announcekit-mcp-server
modified: '2026-09-02'
name: AnnounceKit
nav: Providers
network: true
overview: 'AnnounceKit publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Changelog, Feature Requests, NPS, Notification, and Product Communication.


  The AnnounceKit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AnnounceKit''s developer surface includes documentation, pricing, changelog, code examples, engineering blog, support, signup flow, and 20 more developer resources.'
plans:
- name: Announcekit Plans Pricing
  plan_count: 5
  slug: announcekit-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Announcekit Rate Limits
  slug: announcekit-rate-limits
scopes:
- name: Announcekit Scopes
  scope_count: 0
  slug: announcekit-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.7
  coverage:
    artifact_dirs: 22
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 35.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 54.2
    developer_ergonomics: 44.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 71.1
  previous_composite: 25.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/announcekit/refs/heads/main/screenshots/announcekit-2026-06-20T172011.png
security:
- kind: authentication
  name: Announcekit Authentication
  slug: announcekit-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Announcekit Domain Security
  slug: announcekit-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: trust-center
  name: Announcekit Trust Center
  slug: announcekit-trust-center
  summary_line: SOC 2 Type II, GDPR
slug: announcekit
tags:
- Changelog
- Feature Requests
- NPS
- Notification
- Product Communication
- Roadmaps
- Software-as-a-Service
- Widgets
website: https://announcekit.app/
---
