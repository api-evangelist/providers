---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 19.4
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: 'Kubernetes-style declarative control-plane API for managing Datum Cloud resources — projects, domains, DNS zones and record sets, gateways, HTTPProxies, HTTPRoutes, traffic protection policies (WAF), '
  name: Datum Cloud API
  slug: datum-cloud-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.datum.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.datum.net/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://www.datum.net/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.datum.net/docs/api/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.datum.net/docs/datumctl/quickstart.md
- group: company
  title: ''
  type: Blog
  url: https://www.datum.net/blog/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.datum.net/roadmap/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/datum-cloud
- group: operate
  title: ''
  type: Support
  url: https://www.datum.net/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.datum.net/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.datum.net/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.datumstatus.net
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/datum/refs/heads/main/authentication/datum-authentication.yml
  title: ''
  type: Authentication
  url: authentication/datum-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/datum/refs/heads/main/scopes/datum-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/datum-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://www.datum.net/.well-known/openid-configuration
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/datum/refs/heads/main/well-known/datum-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datum-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://www.datum.net/.well-known/api-catalog
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/datum/refs/heads/main/mcp/datum-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/datum-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/datum/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/datum/refs/heads/main/cli/datum-cli.yml
  title: ''
  type: CLI
  url: cli/datum-cli.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/datum/refs/heads/main/packages/datum-packages.yml
  title: ''
  type: Packages
  url: packages/datum-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/datum/refs/heads/main/components/datum-components.yml
  title: ''
  type: Components
  url: components/datum-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/datum/refs/heads/main/llms/datum-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datum-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/datum/refs/heads/main/lifecycle/datum-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/datum-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/datum/refs/heads/main/conventions/datum-conventions.yml
  title: ''
  type: Conventions
  url: conventions/datum-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/datum/refs/heads/main/conformance/datum-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datum-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/datum/refs/heads/main/security/datum-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datum-domain-security.yml
created: '2026-07-17'
description: 'Datum is an open source network cloud built for AI, founded in 2024 and backed by $13.6M from Amplify Partners, CRV, Encoded Ventures, Cervin Ventures, Ex/Ante, Step Function, and Vine Ventures, and founded by Zac Smith and Jacob Smith (ex-Equinix, Packet). Datum gives AI-native developers and alternative cloud providers critical, neutral network infrastructure to compete at scale: an Envoy-based AI Edge with a Coraza OWASP WAF, Layer 7 HTTPProxy/HTTPRoute traffic management, authoritative DNS and programmatic domain management, QUIC-based secure tunnels (Connectors) powered by Iroh, and a Galactic VPC global backbone, all deployed across 17+ global network locations. The platform is exposed through a Kubernetes-style declarative control-plane API at api.datum.net, the datumctl CLI, an official MCP server, and packaged agent Skills, with OAuth 2.0 / OIDC authentication and a forever-free Builder tier. Core platform is licensed AGPLv3.'
image: https://www.datum.net/brand/social/
layout: provider
mcp_servers:
- description: ''
  name: Datum MCP Server
  slug: datum-mcp-server
modified: '2026-07-18'
name: Datum
nav: Providers
network: true
overview: 'Datum publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Cloud, Networking, and Edge.


  Datum''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 20 more developer resources.'
random_paper: 11
scopes:
- name: Datum Scopes
  scope_count: 6
  slug: datum-scopes
  summary_line: 6 scopes
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 87.0
    operational_transparency: 23.7
  previous_composite: 33.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/datum/refs/heads/main/screenshots/datum-2026-07-25T211422.png
security:
- kind: authentication
  name: Datum Authentication
  slug: datum-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Datum Domain Security
  slug: datum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: datum
tags:
- Company
- Data
- Cloud
- Networking
- Edge
- Artificial Intelligence
- DNS
- Infrastructure
- CDN
- Developer Tools
website: https://www.datum.net/
---
