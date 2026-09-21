---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.6
  scored_at: '2026-09-20'
api_count: 1
apis:
- description: Publish identity, resource and authorization metadata from custom or unsupported applications into the Veza Entity Catalog, and run authorization assessment queries and reports.
  name: Veza Open Authorization API (OAA)
  slug: veza-open-authorization-api-oaa
artifact_total: 4
asyncapis:
- description: ''
  name: Veza Webhooks
  slug: veza-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.veza.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.veza.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.veza.com/oaa/reference/api/oaa-push-api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.veza.com/oaa/guide/getting-started.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/veza
- group: company
  title: ''
  type: Blog
  url: https://www.veza.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.veza.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.veza.com/demo/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.veza.com/privacy-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/veza/refs/heads/main/authentication/veza-authentication.yml
  title: ''
  type: Authentication
  url: authentication/veza-authentication.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/veza/refs/heads/main/packages/veza-packages.yml
  title: ''
  type: Packages
  url: packages/veza-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/veza/refs/heads/main/packages/veza-packages.yml
  title: ''
  type: SDKs
  url: packages/veza-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/veza/refs/heads/main/cli/veza-cli.yml
  title: ''
  type: CLI
  url: cli/veza-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/veza/refs/heads/main/mcp/veza-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/veza-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/veza/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/veza/refs/heads/main/llms/veza-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/veza-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/veza/refs/heads/main/conventions/veza-conventions.yml
  title: ''
  type: Conventions
  url: conventions/veza-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/veza/refs/heads/main/errors/veza-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/veza-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/veza/refs/heads/main/lifecycle/veza-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/veza-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/veza/refs/heads/main/conformance/veza-conformance.yml
  title: ''
  type: Conformance
  url: conformance/veza-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/veza/refs/heads/main/data-model/veza-data-model.yml
  title: ''
  type: DataModel
  url: data-model/veza-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/veza/refs/heads/main/asyncapi/veza-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/veza-webhooks.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/veza/refs/heads/main/security/veza-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/veza-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.veza.com/
created: '2026-07-17'
description: Veza is an identity security platform. Its Open Authorization API (OAA) publishes identity, resource, and authorization metadata from custom or unsupported applications into the Veza Entity Catalog, making access across systems searchable and governable for least-privilege enforcement, access reviews, and rules and alerts. The REST API manages custom providers and their data sources, pushes OAA JSON payloads (users, groups, roles, resources, permissions), and runs authorization assessment queries and reports. It authenticates with a per-tenant API key presented as a bearer token, with official Python and C# SDKs and a command-line client.
image: https://veza.com/wp-content/uploads/2024/01/Veza_Stacked-1.png
layout: provider
modified: '2026-07-21'
name: Veza
nav: Providers
network: true
overview: 'Veza publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Identity Security, Authorization, and Access Management.


  The Veza catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Veza''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, authentication, CLI, and 17 more developer resources.'
random_paper: 20
score:
  band: developing
  composite: 40.4
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
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 68.5
    discoverability: 75.9
    operational_transparency: 26.3
  previous_composite: 40.4
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/veza/refs/heads/main/screenshots/veza-2026-08-17T082737.png
security:
- kind: authentication
  name: Veza Authentication
  slug: veza-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Veza Domain Security
  slug: veza-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: veza
tags:
- Company
- Security
- Identity Security
- Authorization
- Access Management
- Identity Governance
website: https://www.veza.com/
---
