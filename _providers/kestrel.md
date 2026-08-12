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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: Kestrel AI provides an AI-native cloud incident response platform that uses autonomous agents to detect, investigate, and remediate Kubernetes and cloud infrastructure incidents. The platform monitors
  name: Kestrel Platform
  slug: platform
- description: The Kestrel Kubernetes Operator is an open-source Go-based operator that connects Kubernetes clusters to the Kestrel AI platform. It communicates via bidirectional gRPC streaming over mTLS with OAuth2
  name: Kestrel Kubernetes Operator
  slug: kubernetes-operator
artifact_total: 9
common:
- group: auth
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
  title: ''
  type: JSONLD
  url: json-ld/kestrel-context.jsonld
- group: docs
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
- name: Kestrel Finops
  service_category: API
  slug: kestrel-finops
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
modified: '2026-04-28'
name: Kestrel
nav: Providers
network: true
overview: 'Kestrel publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, Cloud Security, Incident Response, Kubernetes, and Observability.


  The Kestrel catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Kestrel''s developer surface includes documentation, signup flow, changelog, engineering blog, and 9 more developer resources.'
plans:
- name: Kestrel Plans Pricing
  plan_count: 3
  slug: kestrel-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 5
  name: Kestrel Rate Limits
  slug: kestrel-rate-limits
rules:
- name: Kestrel API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: kestrel-jsonschema-spectral-rules
score:
  band: thin
  composite: 30.8
  delta: -4.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 8.1
    developer_ergonomics: 10.9
    discoverability: 66.7
    governance: 58.3
    operational_transparency: 55.3
  previous_composite: 35.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kestrel/refs/heads/main/screenshots/kestrel-2026-06-20T184039.png
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
