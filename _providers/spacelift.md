---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Spacelift Agentic Access
  operation_count: 1
  slug: spacelift-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 2
apis:
- description: Spacelift exposes a GraphQL API for programmatic control of all platform resources including stacks, runs, policies, contexts, worker pools, modules, and blueprints. Authentication uses JWT tokens obt
  name: Spacelift GraphQL API
  slug: spacelift-graphql
- description: Spacelift GraphQL endpoint
  name: Spacelift GraphQL API
  slug: spacelift-graphql-api
artifact_total: 20
collections:
- collection_type: postman
  name: Spacelift GraphQL API
  slug: postman-spacelift-graphql-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Spacelift GraphQL API
  slug: open-spacelift-graphql-api
- collection_type: open
  name: Spacelift GraphQL API
  slug: open-spacelift
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/spacelift-io/spacectl/blob/main/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/spacelift/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spacelift-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/spacelift-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spacelift-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spacelift-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spacelift-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spacelift-io
- group: company
  title: ''
  type: Website
  url: https://spacelift.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spacelift.io/
- group: docs
  title: ''
  type: GraphQL
  url: https://docs.spacelift.io/integrations/api
- group: build
  title: ''
  type: GitHub
  url: https://github.com/spacelift-io
- group: commercial
  title: ''
  type: Pricing
  url: https://spacelift.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://spacelift.io/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://spacelift.io/changelog
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.spacelift.io/llms.txt
created: '2026-03-27'
description: Spacelift is an infrastructure-as-code (IaC) orchestration platform that combines AI-assisted deployments, GitOps pipelines, and policy-as-code governance. It supports Terraform, OpenTofu, Pulumi, CloudFormation, Kubernetes, and Ansible. Key features include drift detection, OPA-based policies, self-service blueprints, dynamic credentials, and multi-tenancy. Available as fully managed SaaS and FedRAMP-authorized self-hosted.
examples:
- key_count: 4
  name: Spacelift Stack Example
  slug: spacelift-stack-example
finops:
- name: Spacelift Finops
  service_category: API
  slug: spacelift-finops
graphqls:
- description: Spacelift exposes a GraphQL API for programmatic control of all platform resources including stacks, runs, policies, contexts, worker pools, modules, and blueprints. Authentication uses JWT tokens obt
  name: Spacelift GraphQL API
  slug: spacelift-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spacelift.png
json_schemas:
- name: Spacelift Stack
  property_count: 18
  slug: spacelift-stack
json_structures:
- name: Spacelift Stack Structure
  property_count: 0
  slug: spacelift-stack-structure
jsonld:
- class_count: 10
  name: Spacelift Context
  property_count: 15
  slug: spacelift-context
layout: provider
modified: '2026-05-02'
name: Spacelift
nav: Providers
network: true
overview: 'Spacelift publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Infrastructure as Code, FinOps, DevOps, Platform Engineering, and Terraform.


  The Spacelift catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Spacelift''s developer surface includes authentication, documentation, GitHub presence, pricing, engineering blog, changelog, and 10 more developer resources.'
plans:
- name: Spacelift Plans Pricing
  plan_count: 3
  slug: spacelift-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 5
  name: Spacelift Rate Limits
  slug: spacelift-rate-limits
rules:
- name: Spacelift API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: spacelift-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.0
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 78.4
    developer_ergonomics: 26.1
    discoverability: 75.9
    governance: 58.3
    operational_transparency: 28.9
  previous_composite: 50.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spacelift/refs/heads/main/screenshots/spacelift-2026-06-20T194237.png
security:
- kind: authentication
  name: Spacelift Authentication
  slug: spacelift-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Spacelift Domain Security
  slug: spacelift-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Spacelift Vulnerability Disclosure
  slug: spacelift-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Spacelift Trust Center
  slug: spacelift-trust-center
  summary_line: SOC 2, FedRAMP
slug: spacelift
tags:
- Infrastructure as Code
- FinOps
- DevOps
- Platform Engineering
- Terraform
- GitOps
website: https://spacelift.io/
---
