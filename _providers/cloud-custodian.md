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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.7
  scored_at: '2026-08-12'
api_count: 6
apis:
- description: Cloud Custodian provides rules-engine capabilities for managing cloud resources with security, compliance, and cost optimization policies.
  name: Cloud Custodian
  slug: cloud-custodian
- description: 'The Cloud Custodian AWS provider enables policy-as-code management of Amazon Web Services resources including EC2, S3, IAM, RDS, Lambda, and hundreds of other AWS service resource types. Policies can '
  name: Cloud Custodian AWS Provider
  slug: cloud-custodian-aws
- description: The Cloud Custodian Azure provider enables policy-as-code management of Microsoft Azure resources including virtual machines, storage accounts, network security groups, and other Azure services. Polic
  name: Cloud Custodian Azure Provider
  slug: cloud-custodian-azure
- description: The Cloud Custodian GCP provider enables policy-as-code management of Google Cloud Platform resources including Compute Engine instances, GCS buckets, Cloud SQL instances, and other GCP services. Poli
  name: Cloud Custodian GCP Provider
  slug: cloud-custodian-gcp
- description: 'c7n-org is a Cloud Custodian tool for running policies across multiple cloud accounts, projects, or subscriptions in parallel. It uses an accounts configuration file with assumed roles to orchestrate '
  name: Cloud Custodian C7n-Org
  slug: cloud-custodian-c7n-org
- description: c7n-mailer is a Cloud Custodian notification tool that subscribes to an SQS queue populated by policy actions and sends notifications via SES email, Slack messages, or integrations with DataDog and Sp
  name: Cloud Custodian C7n-Mailer
  slug: cloud-custodian-c7n-mailer
artifact_total: 15
asyncapis:
- description: The Cloud Custodian c7n-mailer AsyncAPI defines the event-driven notification interface used by the Cloud Custodian policy engine to deliver policy violation alerts. When a policy's notify action fire
  name: Cloud Custodian c7n-mailer Notification Events
  slug: cloud-custodian-mailer-asyncapi
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/cloud-custodian/cloud-custodian/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/cloud-custodian/cloud-custodian/blob/main/SECURITY.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/cloud-custodian/cloud-custodian/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloud-custodian-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloudcustodian.io/
- group: docs
  title: ''
  type: Documentation
  url: https://cloudcustodian.io/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloud-custodian/cloud-custodian
- group: start
  title: ''
  type: GettingStarted
  url: https://cloudcustodian.io/docs/quickstart/index.html
- group: operate
  title: ''
  type: Community
  url: https://cloudcustodian.io/community/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/cloud-custodian/cloud-custodian
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/cloud-custodian/cloud-custodian/releases
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/cloud-custodian-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cloud-custodian-policy-schema.json
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/cloud-custodian-mailer-asyncapi.yml
created: '2025-01-01'
description: Cloud Custodian is an open-source rules engine for cloud security, compliance, and cost-optimization governance now stewarded by Stacklet. Operators express policies as YAML files that select a cloud resource type, apply filters, and execute actions; the engine then runs those policies against AWS, Azure, and GCP via provider-specific plugins. Custodian does not expose a developer REST API of its own - integration is via the c7n CLI, the policy YAML schema, c7n-org for multi-account fan-out, and c7n-mailer for SQS-driven notifications.
finops:
- name: Cloud Custodian Finops
  service_category: API
  slug: cloud-custodian-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloud-custodian.png
json_schemas:
- name: Cloud Custodian Policy File
  property_count: 2
  slug: cloud-custodian-policy
jsonld:
- class_count: 0
  name: Cloud Custodian Context
  property_count: 8
  slug: cloud-custodian-context
layout: provider
modified: '2026-04-27'
name: Cloud Custodian
nav: Providers
network: true
overview: 'Cloud Custodian publishes 1 API on the [APIs.io](https://apis.io/) network: C7n-Mailer. Tagged areas include Cloud Security, Compliance, Cost Optimization, Multi-Cloud, and Policy as Code.


  The Cloud Custodian catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Cloud Custodian''s developer surface includes documentation, getting-started guide, changelog, and 11 more developer resources.'
plans:
- name: Cloud Custodian Plans Pricing
  plan_count: 3
  slug: cloud-custodian-plans-pricing
random_paper: 110
rate_limits:
- limit_count: 5
  name: Cloud Custodian Rate Limits
  slug: cloud-custodian-rate-limits
rules:
- name: Cloud Custodian API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 2
  slug: cloud-custodian-asyncapi-spectral-rules
- name: Cloud Custodian API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: cloud-custodian-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.9
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 64.2
    developer_ergonomics: 23.9
    discoverability: 64.8
    governance: 20.8
    operational_transparency: 39.5
  previous_composite: 34.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 16.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloud-custodian/refs/heads/main/screenshots/cloud-custodian-2026-06-20T174534.png
security:
- kind: domain-security
  name: Cloud Custodian Domain Security
  slug: cloud-custodian-domain-security
  summary_line: TLSv1.3
slug: cloud-custodian
tags:
- Cloud Security
- Compliance
- Cost Optimization
- Multi-Cloud
- Policy as Code
website: https://cloudcustodian.io/
---
