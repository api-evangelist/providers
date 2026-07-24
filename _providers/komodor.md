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
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: REST API for managing Komodor clusters, services, monitors, RBAC policies, and integrations programmatically. Authentication uses an API key generated from the API Keys tab in the User Settings page a
  name: Komodor REST API
  slug: rest-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/komodor-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/komodor-ltd
- group: company
  title: ''
  type: Website
  url: https://komodor.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.komodor.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/komodorio
- group: other
  title: ''
  type: Helm Charts
  url: https://github.com/komodorio/helm-charts
- group: commercial
  title: ''
  type: Pricing
  url: https://komodor.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.komodor.com/signup
- group: learn
  title: ''
  type: Learn
  url: https://komodor.com/learn/kubernetes-observability/
- group: agent
  title: ''
  type: LlmsText
  url: https://komodor.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://komodor.com/blog/
created: '2026-05-11'
description: Komodor is an autonomous AI SRE platform for Kubernetes observability, troubleshooting, and operations across multiple clusters. The platform surfaces cluster events, deployment timelines, dependency maps, and remediation runbooks to help platform and SRE teams diagnose incidents faster. Komodor exposes a REST API plus a Terraform provider for managing clusters, services, monitors, and policies, authenticated with API keys generated from the User Settings page.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/komodor.png
layout: provider
modified: '2026-05-11'
name: Komodor
nav: Providers
network: true
overview: 'Komodor publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Kubernetes, Observability, SRE, Troubleshooting, and DevOps.


  Komodor''s developer surface includes documentation, pricing, signup flow, engineering blog, and 7 more developer resources.'
random_paper: 49
score:
  band: minimal
  composite: 14.2
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/komodor/refs/heads/main/screenshots/komodor-2026-06-20T184129.png
security:
- kind: domain-security
  name: Komodor Domain Security
  slug: komodor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: komodor
tags:
- Kubernetes
- Observability
- SRE
- Troubleshooting
- DevOps
- Cloud Native
website: https://komodor.com
---
