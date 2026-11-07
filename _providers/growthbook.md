---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 144
  human_in_the_loop: 2
  name: Growthbook Agentic Access
  operation_count: 222
  slug: growthbook-agentic-access
  summary_line: 222 operations · 144 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: The AnalyticsExplorations API from GrowthBook — 3 operation(s) for analyticsexplorations.
  name: GrowthBook AnalyticsExplorations API
  slug: growthbook-analyticsexplorations-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Archetypes allow you to simulate the result of targeting rules on pre-set user attributes
  name: GrowthBook Archetypes API
  slug: growthbook-archetypes-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Used when targeting feature flags and experiments.
  name: GrowthBook Attributes API
  slug: growthbook-attributes-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Intended for use with our code reference CI utility, [`gb-find-code-refs`](https://github.com/growthbook/gb-find-code-refs).
  name: GrowthBook Code References API
  slug: growthbook-code-references-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: The Dashboards API from GrowthBook — 3 operation(s) for dashboards.
  name: GrowthBook Dashboards API
  slug: growthbook-dashboards-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: How GrowthBook connects and queries your data, including cached database schema metadata (information schemas) for tables and columns.
  name: GrowthBook Data Sources API
  slug: growthbook-data-sources-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Dimensions used during experiment analysis
  name: GrowthBook Dimensions API
  slug: growthbook-dimensions-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: GrowthBook comes with one environment by default (production), but you can add as many as you need. When used with feature flags, you can enable/disable feature flags on a per-environment basis.
  name: GrowthBook Environments API
  slug: growthbook-environments-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Experiments (A/B Tests)
  name: GrowthBook Experiments API
  slug: growthbook-experiments-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Fact Metrics are metrics built on top of Fact Table definitions
  name: GrowthBook Fact Metrics API
  slug: growthbook-fact-metrics-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Fact Tables describe the shape of your data warehouse tables
  name: GrowthBook Fact Tables API
  slug: growthbook-fact-tables-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Draft revisions for feature flags, including rules, scheduling, and approval workflows. **These are v1 endpoints.** New integrations should use the v2 Feature Revisions endpoints.
  name: GrowthBook Feature Revisions API
  slug: growthbook-feature-revisions-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Draft revisions for feature flags, including rules, scheduling, and approval workflows. Revision `rules` is a flat array with per-rule scope fields.
  name: GrowthBook Feature Revisions V2 API
  slug: growthbook-feature-revisions-v2-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Control your feature flags programatically. **These are v1 endpoints.** New integrations should use the v2 Feature Flags endpoints, which expose a unified per-rule environment scope instead of per-env
  name: GrowthBook Features API
  slug: growthbook-features-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Control your feature flags programatically. Rules are returned as a unified top-level array; each rule carries `allEnvironments` / `environments` scope fields instead of being bucketed by environment.
  name: GrowthBook Features V2 API
  slug: growthbook-features-v2-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Members are users who have been invited to an organization.
  name: GrowthBook Members API
  slug: growthbook-members-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Metrics used as goals and guardrails for experiments
  name: GrowthBook Metrics API
  slug: growthbook-metrics-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Namespaces partition your user population into buckets so that experiments using the same hash attribute do not overlap unintentionally. Each namespace defines a 0–1 range and individual experiments c
  name: GrowthBook Namespaces API
  slug: growthbook-namespaces-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Organizations are used for multi-org deployments where different teams can run their own isolated feature flags and experiments. These endpoints are only via a super-admin's Personal Access Token.
  name: GrowthBook Organizations API
  slug: growthbook-organizations-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Projects are used to organize your feature flags and experiments
  name: GrowthBook Projects API
  slug: growthbook-projects-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Retrieve queries used in experiments to calculate results.
  name: GrowthBook Queries API
  slug: growthbook-queries-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Multi-step rollout schedules that gradually ramp feature rule changes over time, with support for interval, approval, and scheduled triggers.
  name: GrowthBook Ramp Schedules API
  slug: growthbook-ramp-schedules-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Reusable step configurations for ramp schedules.
  name: GrowthBook RampScheduleTemplates API
  slug: growthbook-rampscheduletemplates-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Defined sets of attribute values which can be used with feature rules for targeting features at particular users.
  name: GrowthBook Saved Groups API
  slug: growthbook-saved-groups-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Client keys and settings for connecting SDKs to a GrowthBook instance
  name: GrowthBook SDK Connections API
  slug: growthbook-sdk-connections-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: The Sdk Payload API from GrowthBook — 1 operation(s) for sdk payload.
  name: GrowthBook Sdk Payload API
  slug: growthbook-sdk-payload-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Segments used during experiment analysis
  name: GrowthBook Segments API
  slug: growthbook-segments-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Get the organization settings.
  name: GrowthBook Settings API
  slug: growthbook-settings-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Experiment Snapshots (the individual updates of an experiment)
  name: GrowthBook Snapshots API
  slug: growthbook-snapshots-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: The Teams API from GrowthBook — 3 operation(s) for teams.
  name: GrowthBook Teams API
  slug: growthbook-teams-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: The Transform Copy API from GrowthBook — 1 operation(s) for transform copy.
  name: GrowthBook Transform Copy API
  slug: growthbook-transform-copy-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Usage information for metrics in experiments.
  name: GrowthBook Usage API
  slug: growthbook-usage-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Groups of visual changes made by the visual editor to a single page
  name: GrowthBook Visual Changesets API
  slug: growthbook-visual-changesets-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: The AutoRuns API from GrowthBook — 3 operation(s) for autoruns.
  name: GrowthBook Auto Runs API
  slug: growthbook-autoruns-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: '**Beta** — these endpoints are new and may change in backwards-incompatible ways. Draft revisions for configs, including value and schema edits, schema import (JSON Schema / TypeScript / inferred), ap'
  name: GrowthBook Config Revisions API
  slug: growthbook-config-revisions-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: '**Beta** — these endpoints are new and may change in backwards-incompatible ways. Reusable, typed, inheritable JSON objects referenced from feature flag values as `@config:key`. A config carries a fie'
  name: GrowthBook Configs API
  slug: growthbook-configs-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: '**Beta** — these endpoints are new and may change in backwards-incompatible ways. Draft revisions for constants, including pending changes, approvals, and lifecycle (publish, discard, revert). Pass `v'
  name: GrowthBook Constant Revisions API
  slug: growthbook-constant-revisions-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: '**Beta** — these endpoints are new and may change in backwards-incompatible ways. Reusable named values referenced from feature flag values as `@const:key` and resolved into the SDK payload at build t'
  name: GrowthBook Constants API
  slug: growthbook-constants-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: The ContextualBanditQueries API from GrowthBook — 2 operation(s) for contextualbanditqueries.
  name: GrowthBook Contextual Bandit Queries API
  slug: growthbook-contextualbanditqueries-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: The ContextualBandits API from GrowthBook — 15 operation(s) for contextualbandits.
  name: GrowthBook Contextual Bandits API
  slug: growthbook-contextualbandits-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: 'Sandboxed JavaScript validation hooks that run when features, configs, or their revisions are saved or published. Throwing an Error blocks the save; `addWarning(msg)` raises a soft warning. Hooks are '
  name: GrowthBook Custom Hooks API
  slug: growthbook-custom-hooks-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Hold a share of traffic out of all experiments to measure their combined effect.
  name: GrowthBook Holdouts API
  slug: growthbook-holdouts-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Saved learnings captured across experiments, including AI-discovered patterns.
  name: GrowthBook Learnings API
  slug: growthbook-learnings-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Server metadata, including the running build's version and commit for version-skew checks.
  name: GrowthBook Meta API
  slug: growthbook-meta-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: '**Beta** — these endpoints are new and may change in backwards-incompatible ways. Populations define a set of units by the steps they must complete, such as appearing in a fact table. Populations are '
  name: GrowthBook Populations API
  slug: growthbook-populations-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: '**Beta** — these endpoints are new and may change in backwards-incompatible ways. Coordinated multi-entity publishing: publish a set of revisions across Feature Flags, Saved Groups, configs, and const'
  name: GrowthBook Releases API
  slug: growthbook-releases-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Custom analysis reports built on top of experiment snapshots. Reports let you re-run analysis with different metrics, date ranges, stats engines, and other settings without modifying the underlying ex
  name: GrowthBook Reports API
  slug: growthbook-reports-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: Draft revisions for saved groups, including pending changes, approvals, and lifecycle (publish, discard, revert). Most callers can interact with these endpoints via shorthand actions (`/items/add`, `/
  name: GrowthBook Saved Group Revisions API
  slug: growthbook-saved-group-revisions-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: The Custom Fields API from GrowthBook — 2 operation(s) for custom fields.
  name: GrowthBook Custom Fields API
  slug: growthbook-custom-fields-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: The Experiment Templates API from GrowthBook — 3 operation(s) for experiment templates.
  name: GrowthBook Experiment Templates API
  slug: growthbook-experiment-templates-api
- baseURL: https://api.growthbook.io/api
  baseurl_source: declared
  description: The Metric Groups API from GrowthBook — 2 operation(s) for metric groups.
  name: GrowthBook Metric Groups API
  slug: growthbook-metric-groups-api
artifact_total: 96
collections:
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations API
  slug: open-growthbook-analyticsexplorations-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations archetypes API
  slug: open-growthbook-archetypes-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations attributes API
  slug: open-growthbook-attributes-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations code-references API
  slug: open-growthbook-code-references-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations CustomFields API
  slug: open-growthbook-customfields-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations Dashboards API
  slug: open-growthbook-dashboards-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations data-sources API
  slug: open-growthbook-data-sources-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations dimensions API
  slug: open-growthbook-dimensions-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations environments API
  slug: open-growthbook-environments-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations experiments API
  slug: open-growthbook-experiments-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations ExperimentTemplates API
  slug: open-growthbook-experimenttemplates-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations fact-metrics API
  slug: open-growthbook-fact-metrics-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations fact-tables API
  slug: open-growthbook-fact-tables-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations feature-revisions API
  slug: open-growthbook-feature-revisions-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations feature-revisions-v2 API
  slug: open-growthbook-feature-revisions-v2-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations features API
  slug: open-growthbook-features-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations features-v2 API
  slug: open-growthbook-features-v2-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations members API
  slug: open-growthbook-members-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations MetricGroups API
  slug: open-growthbook-metricgroups-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations metrics API
  slug: open-growthbook-metrics-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations namespaces API
  slug: open-growthbook-namespaces-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations organizations API
  slug: open-growthbook-organizations-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations projects API
  slug: open-growthbook-projects-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations queries API
  slug: open-growthbook-queries-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations ramp-schedules API
  slug: open-growthbook-ramp-schedules-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations RampScheduleTemplates API
  slug: open-growthbook-rampscheduletemplates-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations saved-groups API
  slug: open-growthbook-saved-groups-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations sdk-connections API
  slug: open-growthbook-sdk-connections-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations Sdk Payload API
  slug: open-growthbook-sdk-payload-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations segments API
  slug: open-growthbook-segments-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations settings API
  slug: open-growthbook-settings-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations snapshots API
  slug: open-growthbook-snapshots-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations Teams API
  slug: open-growthbook-teams-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations Transform Copy API
  slug: open-growthbook-transform-copy-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations usage API
  slug: open-growthbook-usage-api
- collection_type: open
  name: GrowthBook REST AnalyticsExplorations visual-changesets API
  slug: open-growthbook-visual-changesets-api
common:
- group: other
  href: https://artifacts.apis.io/growthbook/capabilities/growthbook-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/growthbook-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/growthbook/agentic-access/growthbook-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/growthbook-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/growthbook/security/growthbook-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/growthbook-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/growthbook/security/growthbook-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/growthbook-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/growthbook/authentication/growthbook-authentication.yml
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
  href: https://artifacts.apis.io/growthbook/plans/growthbook-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/growthbook-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/growthbook/rate-limits/growthbook-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/growthbook-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/growthbook/finops/growthbook-finops.yml
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
- has_sources: true
  method: generated
  name: Growthbook Finops
  primary_unit: ''
  service_category: A/B Testing
  slug: growthbook-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/growthbook.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.growthbook.io over HTTP.
  name: GrowthBook MCP Server
  slug: growthbook
modified: '2026-05-19'
name: GrowthBook
nav: Providers
network: true
overview: 'GrowthBook publishes 51 API contracts indexed on the [APIs.io](https://apis.io/) network, including AnalyticsExplorations API, Archetypes API, Attributes API, and 48 more. Tagged areas include Feature Flags, Experimentation, Open Source, A/B Testing, and Analytics.


  The GrowthBook catalog on APIs.io includes 1 Spectral governance ruleset.


  GrowthBook''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Growthbook Plans Pricing
  plan_count: 1
  slug: growthbook-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Growthbook Rate Limits
  slug: growthbook-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: GrowthBook API Rules
  rule_count: 58
  severity_counts:
    error: 45
    hint: 0
    info: 4
    warn: 9
  slug: growthbook-rules
score:
  band: thin
  composite: 35.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.5
    catalog_earned_first_party: 0.0
    catalog_gap: 74.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 50.8
    developer_ergonomics: 23.8
    discoverability: 66.7
    operational_transparency: 7.9
  previous_composite: 34.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 58.0
      total: 88
    mcp: first-party
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
    score: 61.1
screenshot: https://apis.io/screenshots/growthbook/growthbook-2026-06-20T182422.png
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
- A/B Testing
- Analytics
website: https://www.growthbook.io/
---
