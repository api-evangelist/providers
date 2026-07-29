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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 71
  human_in_the_loop: 2
  name: Lakefs Agentic Access
  operation_count: 134
  slug: lakefs-agentic-access
  summary_line: 134 operations · 71 acting · 2 human-in-the-loop
api_count: 17
apis:
- description: The actions API from lakeFS — 4 operation(s) for actions.
  name: lakeFS actions API
  slug: lakefs-actions-api
- description: The auth API from lakeFS — 23 operation(s) for auth.
  name: lakeFS auth API
  slug: lakefs-auth-api
- description: The branches API from lakeFS — 5 operation(s) for branches.
  name: lakeFS branches API
  slug: lakefs-branches-api
- description: The commits API from lakeFS — 2 operation(s) for commits.
  name: lakeFS commits API
  slug: lakefs-commits-api
- description: The config API from lakeFS — 1 operation(s) for config.
  name: lakeFS config API
  slug: lakefs-config-api
- description: The experimental API from lakeFS — 14 operation(s) for experimental.
  name: lakeFS experimental API
  slug: lakefs-experimental-api
- description: The external API from lakeFS — 4 operation(s) for external.
  name: lakeFS external API
  slug: lakefs-external-api
- description: The healthCheck API from lakeFS — 1 operation(s) for healthcheck.
  name: lakeFS healthCheck API
  slug: lakefs-healthcheck-api
- description: The import API from lakeFS — 1 operation(s) for import.
  name: lakeFS import API
  slug: lakefs-import-api
- description: The internal API from lakeFS — 24 operation(s) for internal.
  name: lakeFS internal API
  slug: lakefs-internal-api
- description: The metadata API from lakeFS — 2 operation(s) for metadata.
  name: lakeFS metadata API
  slug: lakefs-metadata-api
- description: The objects API from lakeFS — 8 operation(s) for objects.
  name: lakeFS objects API
  slug: lakefs-objects-api
- description: The pulls API from lakeFS — 3 operation(s) for pulls.
  name: lakeFS pulls API
  slug: lakefs-pulls-api
- description: The refs API from lakeFS — 3 operation(s) for refs.
  name: lakeFS refs API
  slug: lakefs-refs-api
- description: The repositories API from lakeFS — 7 operation(s) for repositories.
  name: lakeFS repositories API
  slug: lakefs-repositories-api
- description: The staging API from lakeFS — 1 operation(s) for staging.
  name: lakeFS staging API
  slug: lakefs-staging-api
- description: The tags API from lakeFS — 2 operation(s) for tags.
  name: lakeFS tags API
  slug: lakefs-tags-api
artifact_total: 24
collections:
- collection_type: open
  name: lakeFS API
  slug: open-lakefs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lakefs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lakefs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lakefs-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lakefs-treeverse
- group: company
  title: ''
  type: Website
  url: https://lakefs.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lakefs.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/treeverse/lakeFS
- group: agent
  title: ''
  type: LlmsText
  url: https://lakefs.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://lakefs.io/feed
created: '2025-02-08'
description: Manage your data as code using Git-like operations and achieve reproducible, high-quality data pipelines. Start locally, run on-prem or in the cloud.
finops:
- name: Lakefs Finops
  service_category: API
  slug: lakefs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lakefs.png
layout: provider
modified: '2026-05-19'
name: lakeFS
nav: Providers
network: true
overview: 'lakeFS publishes 17 APIs on the [APIs.io](https://apis.io/) network, including actions API, auth API, branches API, and 14 more. Tagged areas include Data Version Control, Data Lake, Git-like, and Open Source.


  lakeFS''s developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Lakefs Plans Pricing
  plan_count: 3
  slug: lakefs-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 5
  name: Lakefs Rate Limits
  slug: lakefs-rate-limits
score:
  band: thin
  composite: 33.2
  delta: -2.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 46.1
    developer_ergonomics: 21.7
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lakefs/refs/heads/main/screenshots/lakefs-2026-06-20T184245.png
security:
- kind: authentication
  name: Lakefs Authentication
  slug: lakefs-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: Lakefs Domain Security
  slug: lakefs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lakefs
tags:
- Data Version Control
- Data Lake
- Git-like
- Open Source
website: https://lakefs.io/
---
