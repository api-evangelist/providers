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
  band: agent-aware
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
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Kestrel AI provides an AI-native cloud incident response platform that uses autonomous agents to detect, investigate, and remediate Kubernetes and cloud infrastructure incidents. The platform monitors
  name: Kestrel Platform
  slug: platform
- description: The Kestrel Kubernetes Operator is an open-source Go-based operator that connects Kubernetes clusters to the Kestrel AI platform. It communicates via bidirectional gRPC streaming over mTLS with OAuth2
  name: Kestrel Kubernetes Operator
  slug: kubernetes-operator
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/kestrel/plans/kestrel-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kestrel-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/kestrel/rate-limits/kestrel-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kestrel-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/kestrel/finops/kestrel-finops.yml
  title: ''
  type: FinOps
  url: finops/kestrel-finops.yml
- group: auth
  href: https://artifacts.apis.io/kestrel/security/kestrel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kestrel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usekestrel.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usekestrel.ai/
- group: start
  title: ''
  type: Signup
  url: https://platform.usekestrel.ai/register
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kestrelai
- group: other
  title: ''
  type: SelfHosted
  url: https://docs.usekestrel.ai/on-premise/setup
- group: operate
  title: ''
  type: StatusPage
  url: https://status.usekestrel.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: https://usekestrel.ai/changelog
- group: auth
  title: ''
  type: Security
  url: https://trust.delve.co/kestrel-ai
- group: design
  href: https://artifacts.apis.io/kestrel/json-ld/kestrel-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kestrel-context.jsonld
- group: docs
  href: https://artifacts.apis.io/kestrel/json-schema/kestrel-incident-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/kestrel-incident-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.usekestrel.ai/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://usekestrel.ai/blog
created: '2026-03-26'
description: Kestrel AI is a YC-backed startup building an AI-native cloud incident response platform. Founded by former Illumio Kubernetes Security engineers, Kestrel uses autonomous AI agents to detect, investigate, and remediate infrastructure incidents across Kubernetes and cloud environments. The platform provides continuous monitoring, root cause analysis, and automated remediation through GitOps workflows, integrating with Slack, PagerDuty, GitHub, GitLab, AWS, and major observability platforms.
finops:
- has_sources: false
  method: generated
  name: Kestrel Finops
  primary_unit: request
  service_category: API
  slug: kestrel-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kestrel.png
json_schemas:
- name: Kestrel Incident
  property_count: 13
  slug: kestrel-incident
jsonld:
- class_count: 0
  name: Kestrel Context
  property_count: 5
  slug: kestrel-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.usekestrel.ai over HTTP; 3 tools listed.
  name: Kestrel MCP Server
  slug: kestrel
modified: '2026-04-28'
name: Kestrel
nav: Providers
network: true
overview: 'Kestrel is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, Cloud Security, Incident Response, Kubernetes, and Observability.


  The Kestrel catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Kestrel''s developer surface includes documentation, signup flow, changelog, engineering blog, and 12 more developer resources.'
plans:
- name: Kestrel Plans Pricing
  plan_count: 3
  slug: kestrel-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Kestrel Rate Limits
  slug: kestrel-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Kestrel — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: kestrel-jsonschema-spectral-rules
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 46.3
    catalog_earned_first_party: 0.0
    catalog_gap: 68.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 9.8
    contract_quality: 6.7
    developer_ergonomics: 23.8
    discoverability: 66.7
    operational_transparency: 55.3
  previous_composite: 25.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kestrel/kestrel-2026-06-20T184039.png
security:
- kind: domain-security
  name: Kestrel Domain Security
  slug: kestrel-domain-security
  summary_line: TLSv1.3 · HSTS
slug: kestrel
tags:
- AI Agents
- Cloud Security
- Incident Response
- Kubernetes
- Observability
website: https://usekestrel.ai/
---
