---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Dagshub Agentic Access
  operation_count: 26
  slug: dagshub-agentic-access
  summary_line: 26 operations · 8 acting
api_count: 1
apis:
- description: DagsHub's primary REST API mirrors the Gitea API for repositories, issues, pulls, branches, and users, with DagsHub-specific extensions for data, experiments, and annotations. Token-based authenticati
  name: DagsHub REST API
  slug: dagshub-rest-api
- description: Each DagsHub repo provides a hosted MLflow tracking server endpoint. Point `MLFLOW_TRACKING_URI` at the repo's `.mlflow` URL and authenticate with a token.
  name: DagsHub MLflow Tracking Endpoint
  slug: dagshub-mlflow
- description: DagsHub provides a DVC remote and S3-compatible storage endpoint per repo for versioned data and model artifacts.
  name: DagsHub DVC / S3-Compatible Storage
  slug: dagshub-dvc-remote
- baseURL: https://dagshub.com/api/v1
  baseurl_source: declared
  description: The Branches API from DagsHub — 2 operation(s) for branches.
  name: DagsHub Branches API
  slug: dagshub-branches-api
- baseURL: https://dagshub.com/api/v1
  baseurl_source: declared
  description: The Issues API from DagsHub — 3 operation(s) for issues.
  name: DagsHub Issues API
  slug: dagshub-issues-api
- baseURL: https://dagshub.com/api/v1
  baseurl_source: declared
  description: The Orgs API from DagsHub — 2 operation(s) for orgs.
  name: DagsHub Orgs API
  slug: dagshub-orgs-api
- baseURL: https://dagshub.com/api/v1
  baseurl_source: declared
  description: The PullRequests API from DagsHub — 2 operation(s) for pullrequests.
  name: DagsHub PullRequests API
  slug: dagshub-pullrequests-api
- baseURL: https://dagshub.com/api/v1
  baseurl_source: declared
  description: The Repos API from DagsHub — 2 operation(s) for repos.
  name: DagsHub Repos API
  slug: dagshub-repos-api
- baseURL: https://dagshub.com/api/v1
  baseurl_source: declared
  description: The Storage API from DagsHub — 2 operation(s) for storage.
  name: DagsHub Storage API
  slug: dagshub-storage-api
- baseURL: https://dagshub.com/api/v1
  baseurl_source: declared
  description: The User API from DagsHub — 3 operation(s) for user.
  name: DagsHub User API
  slug: dagshub-user-api
- baseURL: https://dagshub.com/api/v1
  baseurl_source: declared
  description: The Users API from DagsHub — 2 operation(s) for users.
  name: DagsHub Users API
  slug: dagshub-users-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DagsHub REST Branches API
  slug: open-dagshub-branches-api
- collection_type: open
  name: DagsHub REST Branches Issues API
  slug: open-dagshub-issues-api
- collection_type: open
  name: DagsHub REST Branches Orgs API
  slug: open-dagshub-orgs-api
- collection_type: open
  name: DagsHub REST Branches PullRequests API
  slug: open-dagshub-pullrequests-api
- collection_type: open
  name: DagsHub REST Branches Repos API
  slug: open-dagshub-repos-api
- collection_type: open
  name: DagsHub REST Branches Storage API
  slug: open-dagshub-storage-api
- collection_type: open
  name: DagsHub REST Branches User API
  slug: open-dagshub-user-api
- collection_type: open
  name: DagsHub REST Branches Users API
  slug: open-dagshub-users-api
- collection_type: open
  name: DagsHub REST API
  slug: open-dagshub
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dagshub-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dagshub-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dagshub-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dagshub
- group: company
  title: ''
  type: Website
  url: https://dagshub.com/
- group: start
  title: ''
  type: Portal
  url: https://dagshub.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://dagshub.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DagsHub
- group: commercial
  title: ''
  type: Plans
  url: plans/dagshub-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dagshub-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dagshub-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://dagshub.com/blog/feed/
created: '2026-05-08'
description: DagsHub is a GitHub-like platform for ML and data teams that combines code, data (DVC), experiments (MLflow), and labeling. It exposes a Gitea-compatible REST API for repository operations plus DagsHub-specific endpoints for data and experiments.
finops:
- name: Dagshub Finops
  service_category: ML
  slug: dagshub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dagshub.png
layout: provider
modified: '2026-05-08'
name: DagsHub
nav: Providers
network: true
overview: 'DagsHub publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Branches API, Issues API, Orgs API, and 5 more. Tagged areas include ML, MLOps, Data Versioning, Git, and MLflow.


  DagsHub''s developer surface includes authentication, developer portal, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Dagshub Plans Pricing
  plan_count: 1
  slug: dagshub-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Dagshub Rate Limits
  slug: dagshub-rate-limits
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 44.9
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 28.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dagshub/refs/heads/main/screenshots/dagshub-2026-06-20T175441.png
security:
- kind: authentication
  name: Dagshub Authentication
  slug: dagshub-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Dagshub Domain Security
  slug: dagshub-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dagshub
tags:
- ML
- MLOps
- Data Versioning
- Git
- MLflow
website: https://dagshub.com/
---
