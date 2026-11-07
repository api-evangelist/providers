---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 135
  human_in_the_loop: 8
  name: Derive To Agentic Access
  operation_count: 201
  slug: derive-to-agentic-access
  summary_line: 201 operations · 135 acting · 8 human-in-the-loop
api_count: 1
apis:
- description: 'Model accounts: the credential a machine uses to call a model. Write-only.'
  name: Derive Accounts API
  slug: derive-to-accounts-api
- description: The Activity API from Derive — 1 operation(s) for activity.
  name: Derive Activity API
  slug: derive-to-activity-api
- description: 'Agents: named workers with instructions, a machine, and what they can reach. Also the OAuth agents a user has authorized.'
  name: Derive Agents API
  slug: derive-to-agents-api
- description: Aggregate view statistics for an artifact.
  name: Derive Analytics API
  slug: derive-to-analytics-api
- description: 'Documents (files and bundles): browse, publish, version, restore, and control access.'
  name: Derive Artifacts API
  slug: derive-to-artifacts-api
- description: Standalone binary image assets referenced from bundles.
  name: Derive Assets API
  slug: derive-to-assets-api
- description: Shareable groups of artifacts, each with its own members.
  name: Derive Collections API
  slug: derive-to-collections-api
- description: Threaded, anchored comments with reactions, edits, and resolution.
  name: Derive Comments API
  slug: derive-to-comments-api
- description: 'Papers imported from arXiv: each is a read-only Context whose artifact is the paper.'
  name: Derive Contexts API
  slug: derive-to-contexts-api
- description: Custom domains and vanity subdomains bound to artifacts.
  name: Derive Domains API
  slug: derive-to-domains-api
- description: The Exports API from Derive — 1 operation(s) for exports.
  name: Derive Exports API
  slug: derive-to-exports-api
- description: The caller's favorited artifacts.
  name: Derive Favorites API
  slug: derive-to-favorites-api
- description: The Folders API from Derive — 3 operation(s) for folders.
  name: Derive Folders API
  slug: derive-to-folders-api
- description: Follow people to build the activity feed.
  name: Derive Follows API
  slug: derive-to-follows-api
- description: Install-backed GitHub access for reading pull requests and posting comments.
  name: Derive GitHub API
  slug: derive-to-github-api
- description: 'One unit of agent work: someone asked, a schedule fired, or a graph opened a node. People ask, follow, answer, cancel, and retry; runners pull and report.'
  name: Derive Jobs API
  slug: derive-to-jobs-api
- description: Abuse reports and takedown / reinstate actions.
  name: Derive Moderation API
  slug: derive-to-moderation-api
- description: The caller's in-app notification feed.
  name: Derive Notifications API
  slug: derive-to-notifications-api
- description: OAuth 2.1 authorization-server endpoints and sign-in capabilities.
  name: Derive OAuth API
  slug: derive-to-oauth-api
- description: Live presence and cursor sharing on an artifact.
  name: Derive Realtime API
  slug: derive-to-realtime-api
- description: 'Review rounds on an artifact: request a review, or send it back with a note.'
  name: Derive Review API
  slug: derive-to-review-api
- description: 'Identity: the signed-in user, public profiles, and the people directory.'
  name: Derive Session API
  slug: derive-to-session-api
- description: Per-artifact collaborator roles (shares) layered over the workspace baseline.
  name: Derive Sharing API
  slug: derive-to-sharing-api
- description: Slack connection status and integration toggles.
  name: Derive Slack API
  slug: derive-to-slack-api
- description: The Templates API from Derive — 6 operation(s) for templates.
  name: Derive Templates API
  slug: derive-to-templates-api
- description: Client-reported web-vitals ingestion.
  name: Derive Vitals API
  slug: derive-to-vitals-api
- description: Outgoing webhooks and their delivery log.
  name: Derive Webhooks API
  slug: derive-to-webhooks-api
- description: 'The workspace itself: members, settings, invitations, and switching.'
  name: Derive Workspace API
  slug: derive-to-workspace-api
artifact_total: 41
asyncapis:
- description: ''
  name: Derive To Webhooks
  slug: derive-to-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/derive-to/agentic-access/derive-to-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/derive-to-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/derive-to/plans/derive-to-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/derive-to-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/derive-to/rules/derive-to-rules.yml
  title: ''
  type: Spectral
  url: rules/derive-to-rules.yml
- group: design
  href: https://artifacts.apis.io/derive-to/json-ld/derive-to-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/derive-to-context.jsonld
- group: design
  href: https://artifacts.apis.io/derive-to/vocabulary/derive-to-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/derive-to-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/derive-to/asyncapi/derive-to-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/derive-to-webhooks.yml
- group: design
  href: https://artifacts.apis.io/derive-to/data-model/derive-to-data-model.yml
  title: ''
  type: DataModel
  url: data-model/derive-to-data-model.yml
- group: build
  href: https://artifacts.apis.io/derive-to/cli/derive-to-cli.yml
  title: ''
  type: CLI
  url: cli/derive-to-cli.yml
- group: design
  href: https://artifacts.apis.io/derive-to/errors/derive-to-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/derive-to-problem-types.yml
- group: design
  href: https://artifacts.apis.io/derive-to/conformance/derive-to-conformance.yml
  title: ''
  type: Conformance
  url: conformance/derive-to-conformance.yml
- group: agent
  href: https://artifacts.apis.io/derive-to/llms/derive-to-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/derive-to-llms.txt
- group: other
  href: https://artifacts.apis.io/derive-to/a2a/derive-to-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/derive-to-a2a.yml
- group: auth
  href: https://artifacts.apis.io/derive-to/well-known/derive-to-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/derive-to-security.txt
- group: auth
  href: https://artifacts.apis.io/derive-to/well-known/derive-to-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/derive-to-app-security.txt
- group: agent
  href: https://artifacts.apis.io/derive-to/well-known/derive-to-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/derive-to-well-known.yml
- group: other
  href: https://artifacts.apis.io/derive-to/hosts/derive-to-hosts.yml
  title: ''
  type: Hosts
  url: hosts/derive-to-hosts.yml
- group: other
  href: https://artifacts.apis.io/derive-to/vendors/derive-to-vendors.yml
  title: ''
  type: Vendors
  url: vendors/derive-to-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://derive.to/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://derive.to/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://derive.to/pricing
- group: company
  title: ''
  type: Blog
  url: https://derive.to/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.derive.to/self-hosting/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.derive.to/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.derive.to/reference/api/
- group: auth
  href: https://artifacts.apis.io/derive-to/security/derive-to-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/derive-to-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/derive-to/security/derive-to-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/derive-to-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://derive.to/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://derive.to/openapi.json
  - status: null
    url: https://app.derive.to/openapi.json
  - status: 401
    url: https://derive.to/mcp
  - status: 401
    url: https://app.derive.to/mcp
  - status: 200
    url: https://derive.to/
  reason: partner-login
  state: gated
created: '2026-11-05'
description: Derive is an open‑source, self‑hostable platform where teams and AI agents publish, review, and revise work. It provides a collaborative space for AI artifacts, emphasizing openness, community contribution, and flexible deployment. The service aims to streamline AI workflow management and artifact sharing across organizations.
image: https://derive.to/site/og-approval.png
json_schemas:
- name: Agent
  property_count: 27
  slug: derive-to-agent
- name: Artifact
  property_count: 45
  slug: derive-to-artifact
- name: Collection
  property_count: 16
  slug: derive-to-collection
- name: Comment
  property_count: 20
  slug: derive-to-comment
- name: ContextAnalysisInfo
  property_count: 7
  slug: derive-to-context-analysis-info
- name: Job
  property_count: 28
  slug: derive-to-job
jsonld:
- class_count: 69
  name: Derive To Context
  property_count: 295
  slug: derive-to-context
layout: provider
modified: '2026-11-05'
name: Derive
nav: Providers
network: true
overview: 'Derive publishes 28 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Activity API, Agents API, and 25 more. Tagged areas include Artificial Intelligence, Open Source, Collaboration, Platform, and Community.


  The Derive catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Derive''s developer surface includes CLI, pricing, engineering blog, getting-started guide, documentation, API reference, and 21 more developer resources.'
plans:
- name: Derive To Plans Pricing
  plan_count: 4
  slug: derive-to-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: Derive API Rules
  rule_count: 38
  severity_counts:
    error: 30
    hint: 0
    info: 1
    warn: 7
  slug: derive-to-rules
score:
  band: developing
  composite: 44.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 55.1
    developer_ergonomics: 38.1
    discoverability: 57.1
    operational_transparency: 18.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 28
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Derive To Domain Security
  slug: derive-to-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Derive To Vulnerability Disclosure
  slug: derive-to-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: derive-to
tags:
- Artificial Intelligence
- Open Source
- Collaboration
- Platform
- Community
website: https://derive.to/
---
