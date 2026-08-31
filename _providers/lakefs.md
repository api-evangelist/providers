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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 71
  human_in_the_loop: 2
  name: Lakefs Agentic Access
  operation_count: 134
  slug: lakefs-agentic-access
  summary_line: 134 operations · 71 acting · 2 human-in-the-loop
api_count: 1
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
artifact_total: 42
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: lakeFS actions API
  slug: open-lakefs-actions-api
- collection_type: open
  name: lakeFS actions auth API
  slug: open-lakefs-auth-api
- collection_type: open
  name: lakeFS actions branches API
  slug: open-lakefs-branches-api
- collection_type: open
  name: lakeFS actions commits API
  slug: open-lakefs-commits-api
- collection_type: open
  name: lakeFS actions config API
  slug: open-lakefs-config-api
- collection_type: open
  name: lakeFS actions experimental API
  slug: open-lakefs-experimental-api
- collection_type: open
  name: lakeFS actions external API
  slug: open-lakefs-external-api
- collection_type: open
  name: lakeFS actions healthCheck API
  slug: open-lakefs-healthcheck-api
- collection_type: open
  name: lakeFS actions import API
  slug: open-lakefs-import-api
- collection_type: open
  name: lakeFS actions internal API
  slug: open-lakefs-internal-api
- collection_type: open
  name: lakeFS actions metadata API
  slug: open-lakefs-metadata-api
- collection_type: open
  name: lakeFS actions objects API
  slug: open-lakefs-objects-api
- collection_type: open
  name: lakeFS actions pulls API
  slug: open-lakefs-pulls-api
- collection_type: open
  name: lakeFS actions refs API
  slug: open-lakefs-refs-api
- collection_type: open
  name: lakeFS actions repositories API
  slug: open-lakefs-repositories-api
- collection_type: open
  name: lakeFS actions staging API
  slug: open-lakefs-staging-api
- collection_type: open
  name: lakeFS actions tags API
  slug: open-lakefs-tags-api
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
overview: 'lakeFS publishes 17 APIs on the [APIs.io](https://apis.io/) network, including actions API, auth API, branches API, and 14 more. Tagged areas include Data Version Control, Data Lake, Git-like, and Open-Source.


  lakeFS''s developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Lakefs Plans Pricing
  plan_count: 3
  slug: lakefs-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Lakefs Rate Limits
  slug: lakefs-rate-limits
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 11
    catalog_gap: 84.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 47.5
    developer_ergonomics: 23.8
    discoverability: 48.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 26.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
- Open-Source
website: https://lakefs.io/
---
