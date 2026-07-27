---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-27'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gitops-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gitops.tech/
- group: other
  title: ''
  type: OpenGitOps Principles
  url: https://opengitops.dev/
- group: other
  title: ''
  type: CNCF Working Group
  url: https://github.com/cncf/tag-app-delivery
- group: other
  title: ''
  type: Argo CD
  url: https://argo-cd.readthedocs.io/
- group: other
  title: ''
  type: Flux
  url: https://fluxcd.io/
- group: design
  title: ''
  type: Rules
  url: https://raw.githubusercontent.com/api-evangelist/gitops/refs/heads/main/rules/gitops-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/gitops/refs/heads/main/vocabulary/gitops-vocabulary.yml
created: '2025-01-01'
description: A operational framework that takes DevOps best practices used for application development such as version control, collaboration, compliance, and CI/CD, and applies them to infrastructure automation. GitOps uses Git as a single source of truth for declarative infrastructure and applications.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gitops.png
layout: provider
modified: '2026-04-28'
name: GitOps
nav: Providers
network: true
overview: 'GitOps is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, Continuous Deployment, DevOps, Infrastructure as Code, and Version Control.


  The GitOps catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 50
rules:
- name: GitOps API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: gitops-rules
score:
  band: minimal
  composite: 9.9
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 26.3
    operational_transparency: 0.0
  previous_composite: 9.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gitops/refs/heads/main/screenshots/gitops-2026-06-20T181849.png
security:
- kind: domain-security
  name: Gitops Domain Security
  slug: gitops-domain-security
  summary_line: TLSv1.3
slug: gitops
tags:
- Automation
- Continuous Deployment
- DevOps
- Infrastructure as Code
- Version Control
website: https://www.gitops.tech/
---
