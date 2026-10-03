---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 31
common:
- group: start
  title: ''
  type: Portal
  url: https://apievangelist.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2026-05-19'
description: An index and topic collection covering site reliability engineering (SRE), reliability platforms, service level objectives (SLOs), error budgets, chaos engineering, resilience testing, and incident response. Reliability platforms help teams define and measure reliability targets, intentionally inject failure to validate resilience, manage on-call rotations and alerting, coordinate incident response, and run blameless post-incident reviews. This collection includes SLO management platforms like Nobl9 and Chronosphere, chaos engineering tools like Gremlin, Chaos Mesh, Litmus, and AWS Fault Injection Simulator, internal developer platforms with reliability scoring like OpsLevel and Cortex, and incident response platforms like PagerDuty, OpsGenie, Incident.io, FireHydrant, Rootly, Blameless, Squadcast, and Zenduty.
examples:
- key_count: 10
  name: Reliability Chaos Experiment Example
  slug: reliability-chaos-experiment-example
- key_count: 9
  name: Reliability Slo Example
  slug: reliability-slo-example
features:
- description: Reliability platforms like Nobl9, Chronosphere, and OpenSLO let teams define service level indicators (SLIs), set service level objectives (SLOs), and track error budgets to balance reliability work against feature delivery.
  name: Service Level Objectives and Error Budgets
- description: Chaos engineering tools like Gremlin, Chaos Mesh, Litmus, and AWS Fault Injection Simulator deliberately inject failures into systems to validate resilience and uncover hidden weaknesses before they cause incidents.
  name: Chaos Engineering and Fault Injection
- description: Incident response platforms like PagerDuty, OpsGenie, Incident.io, FireHydrant, and Rootly orchestrate on-call rotations, alert routing, escalation policies, and incident war rooms across distributed teams.
  name: Incident Response and On-Call Orchestration
- description: Reliability platforms automate runbooks and response workflows that trigger on incidents, capture context from connected systems, and guide responders through remediation steps.
  name: Runbook Automation and Response Workflows
- description: Chaos and incident tools include safeguards such as halt conditions, scope limits, and automated rollback to contain the blast radius of experiments and incidents.
  name: Blast Radius Reduction and Safety Controls
- description: Platforms like Blameless, Jeli, and FireHydrant structure post-incident analysis to extract learning without assigning blame, capturing timelines, contributing factors, and follow-up actions.
  name: Blameless Post-Incident Reviews
- description: Internal developer platforms like OpsLevel and Cortex score services against reliability standards such as ownership, on-call coverage, SLO adoption, and runbook completeness.
  name: Service Standards and Reliability Scoring
- description: Status page platforms like Statuspage, Better Stack, and OneUptime communicate incident state and maintenance windows to customers and stakeholders in real time.
  name: Status Pages and Customer Communication
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: SLO platform that consolidates SLIs from Prometheus, Datadog, New Relic, and other observability sources into managed service level objectives with error budget tracking.
  name: Nobl9
- description: Chaos engineering platform for safely injecting CPU, memory, network, and dependency failures into production and staging systems with built-in halt conditions.
  name: Gremlin
- description: Incident response and on-call platform with rotation scheduling, escalation policies, event intelligence, and a broad integration ecosystem.
  name: PagerDuty
- description: Slack-native incident response platform that automates channel creation, roles, comms, and post-mortems for engineering teams.
  name: Incident.io
- description: Incident management platform combining runbooks, retrospectives, status pages, and service catalog for reliability programs.
  name: FireHydrant
- description: Open-source CNCF chaos engineering platform for Kubernetes that injects pod, network, IO, and time faults via custom resources.
  name: Chaos Mesh
- description: Internal developer portal that tracks service ownership and scores services against reliability standards such as SLOs defined, on-call set, and runbooks linked.
  name: OpsLevel
- description: Hosted status page platform from Atlassian for communicating incidents, maintenance, and component health to customers.
  name: Statuspage
json_schemas:
- name: ChaosExperiment
  property_count: 10
  slug: reliability-chaos-experiment
- name: ServiceLevelObjective
  property_count: 9
  slug: reliability-slo
json_structures:
- name: Reliability Chaos Experiment Structure
  property_count: 10
  slug: reliability-chaos-experiment-structure
- name: Reliability Slo Structure
  property_count: 9
  slug: reliability-slo-structure
jsonld:
- class_count: 9
  name: Reliability Context
  property_count: 16
  slug: reliability-context
layout: provider
modified: '2026-05-19'
name: Reliability
nav: Providers
network: true
overview: 'Reliability is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include SRE, Reliability, SLO, Chaos Engineering, and Incident Response.


  The Reliability catalog on APIs.io includes 1 JSON-LD context.


  Reliability''s developer surface includes developer portal and 1 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: reliability
tags:
- SRE
- Reliability
- SLO
- Chaos Engineering
- Incident Response
- Error Budget
- On-Call
- Resilience
use_cases:
- description: Replace threshold alerts with SLO burn-rate alerts that fire only when error budget is being consumed faster than sustainable, reducing alert fatigue while preserving signal.
  name: SLO-Based Alerting
- description: Teams use Gremlin, Chaos Mesh, or AWS Fault Injection Simulator in staging environments to validate retries, timeouts, circuit breakers, and failover before production deploys.
  name: Pre-Production Resilience Testing
- description: SRE teams run scheduled game days and continuous chaos experiments to verify that documented runbooks, alerting, and failover behavior still work as systems evolve.
  name: Game Days and Continuous Verification
- description: PagerDuty, Incident.io, and FireHydrant coordinate large incidents across multiple teams with auto-created Slack channels, scribes, roles, and timeline capture.
  name: Incident Coordination at Scale
- description: When a service exhausts its error budget, automated policies in Nobl9 or Chronosphere can freeze deploys, page leadership, or trigger reliability investment until the budget recovers.
  name: Error Budget Policy Enforcement
- description: Platforms like PagerDuty, OpsGenie, and Squadcast manage rotation schedules, overrides, and escalation policies across global teams, with integrations into chat and ticketing tools.
  name: On-Call Schedule Management
- description: OpsLevel, Cortex, and Backstage track service ownership, tier, and adherence to reliability standards like SLO coverage, on-call defined, and runbooks linked.
  name: Service Catalog and Reliability Standards
- description: Statuspage, Better Stack, and OneUptime provide hosted status pages that publish incident updates, scheduled maintenance, and component health to customers and subscribers.
  name: Customer-Facing Status Communication
website: https://apievangelist.com
---
