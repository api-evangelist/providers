---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 144
  human_in_the_loop: 2
  name: Growthbook Agentic Access
  operation_count: 222
  slug: growthbook-agentic-access
  summary_line: 222 operations · 144 acting · 2 human-in-the-loop
api_count: 36
apis:
- description: The AnalyticsExplorations API from GrowthBook — 3 operation(s) for analyticsexplorations.
  name: GrowthBook AnalyticsExplorations API
  slug: growthbook-analyticsexplorations-api
- description: Archetypes allow you to simulate the result of targeting rules on pre-set user attributes
  name: GrowthBook archetypes API
  slug: growthbook-archetypes-api
- description: Used when targeting feature flags and experiments.
  name: GrowthBook attributes API
  slug: growthbook-attributes-api
- description: Intended for use with our code reference CI utility, [`gb-find-code-refs`](https://github.com/growthbook/gb-find-code-refs).
  name: GrowthBook code-references API
  slug: growthbook-code-references-api
- description: The CustomFields API from GrowthBook — 2 operation(s) for customfields.
  name: GrowthBook CustomFields API
  slug: growthbook-customfields-api
- description: The Dashboards API from GrowthBook — 3 operation(s) for dashboards.
  name: GrowthBook Dashboards API
  slug: growthbook-dashboards-api
- description: How GrowthBook connects and queries your data, including cached database schema metadata (information schemas) for tables and columns.
  name: GrowthBook data-sources API
  slug: growthbook-data-sources-api
- description: Dimensions used during experiment analysis
  name: GrowthBook dimensions API
  slug: growthbook-dimensions-api
- description: GrowthBook comes with one environment by default (production), but you can add as many as you need. When used with feature flags, you can enable/disable feature flags on a per-environment basis.
  name: GrowthBook environments API
  slug: growthbook-environments-api
- description: Experiments (A/B Tests)
  name: GrowthBook experiments API
  slug: growthbook-experiments-api
- description: The ExperimentTemplates API from GrowthBook — 3 operation(s) for experimenttemplates.
  name: GrowthBook ExperimentTemplates API
  slug: growthbook-experimenttemplates-api
- description: Fact Metrics are metrics built on top of Fact Table definitions
  name: GrowthBook fact-metrics API
  slug: growthbook-fact-metrics-api
- description: Fact Tables describe the shape of your data warehouse tables
  name: GrowthBook fact-tables API
  slug: growthbook-fact-tables-api
- description: Draft revisions for feature flags, including rules, scheduling, and approval workflows. **These are v1 endpoints.** New integrations should use the v2 Feature Revisions endpoints.
  name: GrowthBook feature-revisions API
  slug: growthbook-feature-revisions-api
- description: Draft revisions for feature flags, including rules, scheduling, and approval workflows. Revision `rules` is a flat array with per-rule scope fields.
  name: GrowthBook feature-revisions-v2 API
  slug: growthbook-feature-revisions-v2-api
- description: Control your feature flags programatically. **These are v1 endpoints.** New integrations should use the v2 Feature Flags endpoints, which expose a unified per-rule environment scope instead of per-env
  name: GrowthBook features API
  slug: growthbook-features-api
- description: Control your feature flags programatically. Rules are returned as a unified top-level array; each rule carries `allEnvironments` / `environments` scope fields instead of being bucketed by environment.
  name: GrowthBook features-v2 API
  slug: growthbook-features-v2-api
- description: Members are users who have been invited to an organization.
  name: GrowthBook members API
  slug: growthbook-members-api
- description: The MetricGroups API from GrowthBook — 2 operation(s) for metricgroups.
  name: GrowthBook MetricGroups API
  slug: growthbook-metricgroups-api
- description: Metrics used as goals and guardrails for experiments
  name: GrowthBook metrics API
  slug: growthbook-metrics-api
- description: Namespaces partition your user population into buckets so that experiments using the same hash attribute do not overlap unintentionally. Each namespace defines a 0–1 range and individual experiments c
  name: GrowthBook namespaces API
  slug: growthbook-namespaces-api
- description: Organizations are used for multi-org deployments where different teams can run their own isolated feature flags and experiments. These endpoints are only via a super-admin's Personal Access Token.
  name: GrowthBook organizations API
  slug: growthbook-organizations-api
- description: Projects are used to organize your feature flags and experiments
  name: GrowthBook projects API
  slug: growthbook-projects-api
- description: Retrieve queries used in experiments to calculate results.
  name: GrowthBook queries API
  slug: growthbook-queries-api
- description: Multi-step rollout schedules that gradually ramp feature rule changes over time, with support for interval, approval, and scheduled triggers.
  name: GrowthBook ramp-schedules API
  slug: growthbook-ramp-schedules-api
- description: Reusable step configurations for ramp schedules.
  name: GrowthBook RampScheduleTemplates API
  slug: growthbook-rampscheduletemplates-api
- description: Defined sets of attribute values which can be used with feature rules for targeting features at particular users.
  name: GrowthBook saved-groups API
  slug: growthbook-saved-groups-api
- description: Client keys and settings for connecting SDKs to a GrowthBook instance
  name: GrowthBook sdk-connections API
  slug: growthbook-sdk-connections-api
- description: The Sdk Payload API from GrowthBook — 1 operation(s) for sdk payload.
  name: GrowthBook Sdk Payload API
  slug: growthbook-sdk-payload-api
- description: Segments used during experiment analysis
  name: GrowthBook segments API
  slug: growthbook-segments-api
- description: Get the organization settings.
  name: GrowthBook settings API
  slug: growthbook-settings-api
- description: Experiment Snapshots (the individual updates of an experiment)
  name: GrowthBook snapshots API
  slug: growthbook-snapshots-api
- description: The Teams API from GrowthBook — 3 operation(s) for teams.
  name: GrowthBook Teams API
  slug: growthbook-teams-api
- description: The Transform Copy API from GrowthBook — 1 operation(s) for transform copy.
  name: GrowthBook Transform Copy API
  slug: growthbook-transform-copy-api
- description: Usage information for metrics in experiments.
  name: GrowthBook usage API
  slug: growthbook-usage-api
- description: Groups of visual changes made by the visual editor to a single page
  name: GrowthBook visual-changesets API
  slug: growthbook-visual-changesets-api
artifact_total: 43
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/growthbook-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/growthbook-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/growthbook-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/growthbook-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/growthbook
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/growthbook
- group: company
  title: ''
  type: Website
  url: https://www.growthbook.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.growthbook.io/api
- group: commercial
  title: ''
  type: Plans
  url: plans/growthbook-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/growthbook-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/growthbook-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.growthbook.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.growthbook.io/blog
created: '2026-05-08'
description: GrowthBook is an open source feature flagging and experimentation platform with a warehouse-native statistics engine.
finops:
- name: Growthbook Finops
  service_category: A/B Testing
  slug: growthbook-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/growthbook.png
layout: provider
modified: '2026-05-19'
name: GrowthBook
nav: Providers
network: true
overview: 'GrowthBook publishes 36 APIs on the [APIs.io](https://apis.io/) network, including AnalyticsExplorations API, archetypes API, attributes API, and 33 more. Tagged areas include Feature Flags, Experimentation, Open Source, AB Testing, and Analytics.


  GrowthBook''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Growthbook Plans Pricing
  plan_count: 1
  slug: growthbook-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 1
  name: Growthbook Rate Limits
  slug: growthbook-rate-limits
score:
  band: thin
  composite: 35.3
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 54.8
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 35.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 36
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/growthbook/refs/heads/main/screenshots/growthbook-2026-06-20T182422.png
security:
- kind: authentication
  name: Growthbook Authentication
  slug: growthbook-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Growthbook Domain Security
  slug: growthbook-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Growthbook Trust Center
  slug: growthbook-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: growthbook
tags:
- Feature Flags
- Experimentation
- Open Source
- AB Testing
- Analytics
website: https://www.growthbook.io/
---
