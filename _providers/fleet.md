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
    agentic_access: derived
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Fleet Agentic Access
  operation_count: 4
  slug: fleet-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- baseURL: https://rbx.cloud.fleetdm.com/api/v1/fleet
  baseurl_source: declared
  description: The Fleet API from Fleet — 2 operation(s) for fleet.
  name: Fleet API
  slug: fleet-fleet-api
artifact_total: 11
asyncapis:
- description: ''
  name: Fleet Webhooks
  slug: fleet-webhooks
collections:
- collection_type: open
  name: Premium Fleet API
  slug: open-fleet-fleet-api
common:
- group: commercial
  href: https://artifacts.apis.io/fleet/plans/fleet-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fleet-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/fleet/mcp/fleet-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/fleet-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://fleetdm.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fleetdm.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://fleetdm.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://fleetdm.com/docs/rest-api/rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://fleetdm.com/docs/get-started/anatomy
- group: operate
  title: ''
  type: Support
  url: https://fleetdm.com/support
- group: company
  title: ''
  type: Blog
  url: https://fleetdm.com/articles
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fleetdm
- group: commercial
  title: ''
  type: Pricing
  url: https://fleetdm.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://fleetdm.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fleetdm.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fleetdm.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fleetdm.com
- group: operate
  href: https://artifacts.apis.io/fleet/changelog/fleet-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/fleet-changelog.yml
- group: design
  href: https://artifacts.apis.io/fleet/lifecycle/fleet-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fleet-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/fleet/cli/fleet-cli.yml
  title: ''
  type: CLI
  url: cli/fleet-cli.yml
- group: build
  href: https://artifacts.apis.io/fleet/packages/fleet-packages.yml
  title: ''
  type: Packages
  url: packages/fleet-packages.yml
- group: auth
  href: https://artifacts.apis.io/fleet/authentication/fleet-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fleet-authentication.yml
- group: design
  href: https://artifacts.apis.io/fleet/conventions/fleet-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fleet-conventions.yml
- group: design
  href: https://artifacts.apis.io/fleet/errors/fleet-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fleet-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fleet/data-model/fleet-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fleet-data-model.yml
- group: design
  href: https://artifacts.apis.io/fleet/conformance/fleet-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fleet-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.fleetdm.com/
- group: auth
  href: https://artifacts.apis.io/fleet/security/fleet-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/fleet-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/fleet/security/fleet-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/fleet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/fleetdm/fleet/blob/main/SECURITY.md
- group: auth
  href: https://artifacts.apis.io/fleet/security/fleet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fleet-domain-security.yml
- group: design
  href: https://artifacts.apis.io/fleet/asyncapi/fleet-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/fleet-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/fleet/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/fleet/agentic-access/fleet-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fleet-agentic-access.yml
- group: other
  href: https://artifacts.apis.io/fleet/overlays/fleet-premium-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fleet-premium-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/fleet/llms/fleet-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fleet-llms.txt
created: '2026-07-17'
description: Fleet is an open-source device management platform built on osquery. It provides cross-platform MDM, endpoint telemetry, vulnerability and patch management, software inventory, and GitOps-driven configuration for macOS, Windows, Linux, iOS, and Android fleets. Fleet exposes a versioned REST API (/api/v1/fleet, bearer-token auth), the fleetctl CLI for live queries and config-as-code, and outbound webhook automations. It is developed in the open at github.com/fleetdm/fleet and backed by CRV.
finops:
- has_sources: true
  method: derived
  name: Fleet Finops
  primary_unit: host
  service_category: ''
  slug: fleet-finops
  template: false
image: https://avatars.githubusercontent.com/u/70264713?v=4
layout: provider
modified: '2026-09-16'
name: Fleet
nav: Providers
network: true
overview: 'Fleet publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Device Management, MDM, and Endpoint Security.


  The Fleet catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fleet''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Fleet Plans Pricing
  plan_count: 3
  slug: fleet-plans-pricing
random_paper: 0
score:
  band: strong
  composite: 63.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 44.9
    developer_ergonomics: 66.1
    discoverability: 66.1
    operational_transparency: 55.3
  previous_composite: 55.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/fleet/fleet-2026-07-25T214732.png
security:
- kind: authentication
  name: Fleet Authentication
  slug: fleet-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Fleet Domain Security
  slug: fleet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fleet Vulnerability Disclosure
  slug: fleet-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Fleet Trust Center
  slug: fleet-trust-center
  summary_line: SOC 2 Type 2, ISO 27001
skill_count: 1
skills:
- name: Manage Fleet teams
  slug: fleet-manage-teams
slug: fleet
tags:
- Company
- Developer Tools
- Device Management
- MDM
- Endpoint Security
- Vulnerability Management
- osquery
- Open Source
- DevOps
website: https://fleetdm.com/
---
