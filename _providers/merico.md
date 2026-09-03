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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
asyncapis:
- description: ''
  name: Merico Devlake Webhooks
  slug: merico-devlake-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/merico-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.devinsight.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://devlake.apache.org
- group: docs
  title: ''
  type: Documentation
  url: https://devlake.apache.org/docs/Overview/Introduction/
- group: docs
  title: ''
  type: APIReference
  url: https://devlake.apache.org/docs/Overview/References
- group: start
  title: ''
  type: GettingStarted
  url: https://devlake.apache.org/docs/GettingStarted
- group: company
  title: ''
  type: Blog
  url: https://www.devinsight.ai/blog/home
- group: commercial
  title: ''
  type: Pricing
  url: https://www.devinsight.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.devinsight.ai/
- group: start
  title: ''
  type: Login
  url: https://cloud.devinsight.ai/?type=login
- group: operate
  title: ''
  type: Support
  url: https://www.devinsight.ai/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.devinsight.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.devinsight.ai/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/devlake
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.devinsight.ai/security-trust
- group: auth
  title: ''
  type: Compliance
  url: https://www.devinsight.ai/security-trust
- group: design
  title: ''
  type: Webhooks
  url: https://devlake.apache.org/docs/Plugins/webhook/
- group: design
  title: ''
  type: Conformance
  url: conformance/merico-conformance.yml
created: '2026-07-17'
description: Merico is a developer-analytics company behind DevInsight, an engineering intelligence platform that ingests data from DevOps tools like GitHub, GitLab, Jira, and Jenkins to surface DORA metrics, resource allocation, sprint planning insight, and customizable engineering dashboards. Merico is the original creator and primary maintainer of Apache DevLake, the open-source dev-data platform that powers DevInsight, exposing a self-hosted REST API and an inbound webhook connector for pushing DevOps data from tools without a dedicated plugin. The company operates a cloud SaaS at cloud.devinsight.ai and maintains SOC 1 Type II and SOC 2 Type II attestations.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/merico.png
layout: provider
modified: '2026-07-20'
name: Merico
nav: Providers
network: true
overview: 'Merico is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DevTools, Engineering Intelligence, DevOps, and DORA Metrics.


  The Merico catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Merico''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 11 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 45.2
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 38.8
  provenance:
    conformance: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/merico/refs/heads/main/screenshots/merico-2026-08-07T172554.png
security:
- kind: domain-security
  name: Merico Domain Security
  slug: merico-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: trust-center
  name: Merico Trust Center
  slug: merico-trust-center
  summary_line: SOC 1 Type II, SOC 2 Type II
slug: merico
tags:
- Company
- DevTools
- Engineering Intelligence
- DevOps
- DORA Metrics
- Software Analytics
- Open-Source
- Data Platform
website: https://www.devinsight.ai
---
