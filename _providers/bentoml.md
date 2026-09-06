---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 106
  human_in_the_loop: 4
  name: Bentoml Agentic Access
  operation_count: 222
  slug: bentoml-agentic-access
  summary_line: 222 operations · 106 acting · 4 human-in-the-loop
api_count: 1
apis:
- description: Auto-generated REST API endpoints produced when BentoML services are deployed. Each decorated service method becomes an HTTP POST endpoint. Supports custom routes, path prefixes, adaptive batching, as
  name: BentoML Service REST API
  slug: bentoml-service-api
- description: 'Core Python SDK for packaging models as Bentos, managing the model store, building container images, and interacting with BentoML services programmatically including client-side API calls to deployed '
  name: BentoML Python SDK
  slug: bentoml-sdk
- description: API for creating, listing, retrieving, and deleting API tokens used to authenticate with BentoCloud services. Supports scoped tokens with granular permissions including API access, organization read/w
  name: BentoCloud API Token Management
  slug: bentocloud-token-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: admin api v1
  name: BentoML admin api v1 API
  slug: bentoml-admin-api-v1-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: admin deployment resource
  name: BentoML admin deployment resource API
  slug: bentoml-admin-deployment-resource-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: api token resource
  name: BentoML api token resource API
  slug: bentoml-api-token-resource-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: api tokens
  name: BentoML api tokens API
  slug: bentoml-api-tokens-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: api v1
  name: BentoML api v1 API
  slug: bentoml-api-v1-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: auth api
  name: BentoML auth API
  slug: bentoml-auth-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: bento repositories
  name: BentoML bento repositories API
  slug: bentoml-bento-repositories-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: bento repositories statistics
  name: BentoML bento repositories statistics API
  slug: bentoml-bento-repositories-statistics-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: bento repository resource
  name: BentoML bento repository resource API
  slug: bentoml-bento-repository-resource-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: bento resource
  name: BentoML bento resource API
  slug: bentoml-bento-resource-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: bentos
  name: BentoML bentos API
  slug: bentoml-bentos-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: certified bento repositories
  name: BentoML certified bento repositories API
  slug: bentoml-certified-bento-repositories-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: cluster deployments
  name: BentoML cluster deployments API
  slug: bentoml-cluster-deployments-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: cluster resource
  name: BentoML cluster resource API
  slug: bentoml-cluster-resource-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: cluster resource for admin panel
  name: BentoML cluster resource for admin panel API
  slug: bentoml-cluster-resource-for-admin-panel-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: clusters
  name: BentoML clusters API
  slug: bentoml-clusters-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: clusters for admin panel
  name: BentoML clusters for admin panel API
  slug: bentoml-clusters-for-admin-panel-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: current organization resource
  name: BentoML current organization resource API
  slug: bentoml-current-organization-resource-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: customer resource
  name: BentoML customer resource API
  slug: bentoml-customer-resource-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: customers api
  name: BentoML customers API
  slug: bentoml-customers-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: deployment resource
  name: BentoML deployment resource API
  slug: bentoml-deployment-resource-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: deployment revision resource
  name: BentoML deployment revision resource API
  slug: bentoml-deployment-revision-resource-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: deployment revisions
  name: BentoML deployment revisions API
  slug: bentoml-deployment-revisions-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: deployment revision resource
  name: BentoML deployment v2 revision resource API
  slug: bentoml-deployment-v2-revision-resource-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: deployment revisions
  name: BentoML deployment v2 revisions API
  slug: bentoml-deployment-v2-revisions-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: endpoint resource
  name: BentoML endpoint resource API
  slug: bentoml-endpoint-resource-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: gpu config resource
  name: BentoML gpu config resource API
  slug: bentoml-gpu-config-resource-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: gpu configs
  name: BentoML gpu configs API
  slug: bentoml-gpu-configs-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: host cluster resource
  name: BentoML host cluster resource API
  slug: bentoml-host-cluster-resource-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: host_clusters
  name: BentoML host_clusters API
  slug: bentoml-host-clusters-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: instance_types
  name: BentoML instance_types API
  slug: bentoml-instance-types-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: labels
  name: BentoML labels API
  slug: bentoml-labels-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: lago billable metrics api
  name: BentoML lago billable metrics API
  slug: bentoml-lago-billable-metrics-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: lago customer api
  name: BentoML lago customer API
  slug: bentoml-lago-customer-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: lago plan api
  name: BentoML lago plan API
  slug: bentoml-lago-plan-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: limit group resource
  name: BentoML limit group resource API
  slug: bentoml-limit-group-resource-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: limit groups
  name: BentoML limit groups API
  slug: bentoml-limit-groups-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: model repositories
  name: BentoML model repositories API
  slug: bentoml-model-repositories-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: model repository resource
  name: BentoML model repository resource API
  slug: bentoml-model-repository-resource-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: model resource
  name: BentoML model resource API
  slug: bentoml-model-resource-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: models
  name: BentoML models API
  slug: bentoml-models-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: org resource for admin panel
  name: BentoML org resource for admin panel API
  slug: bentoml-org-resource-for-admin-panel-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: organization resource
  name: BentoML organization resource API
  slug: bentoml-organization-resource-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: organization secrets
  name: BentoML organization secrets API
  slug: bentoml-organization-secrets-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: organization secrets with check message
  name: BentoML organization secrets with check message API
  slug: bentoml-organization-secrets-with-check-message-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: organization secrets with template
  name: BentoML organization secrets with template API
  slug: bentoml-organization-secrets-with-template-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: plans
  name: BentoML plans API
  slug: bentoml-plans-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: request quota
  name: BentoML request quota API
  slug: bentoml-request-quota-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: resource instance resource
  name: BentoML resource instance resource API
  slug: bentoml-resource-instance-resource-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: resource instances
  name: BentoML resource instances API
  slug: bentoml-resource-instances-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: secret names
  name: BentoML secret names API
  slug: bentoml-secret-names-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: slim bento repositories
  name: BentoML slim bento repositories API
  slug: bentoml-slim-bento-repositories-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: terminal record resource
  name: BentoML terminal record resource API
  slug: bentoml-terminal-record-resource-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: usage resource
  name: BentoML usage API
  slug: bentoml-usage-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: user resource
  name: BentoML user resource API
  slug: bentoml-user-resource-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: users api
  name: BentoML users API
  slug: bentoml-users-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: websocket v1
  name: BentoML websocket v1 API
  slug: bentoml-websocket-v1-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: websocket v2
  name: BentoML websocket v2 API
  slug: bentoml-websocket-v2-api
- baseURL: https://cloud.bentoml.com
  baseurl_source: declared
  description: yatai components
  name: BentoML yatai components API
  slug: bentoml-yatai-components-api
artifact_total: 131
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: yatai api server admin api v1 API
  slug: open-bentoml-admin-api-v1-api
- collection_type: open
  name: yatai api server admin api v1 admin deployment resource API
  slug: open-bentoml-admin-deployment-resource-api
- collection_type: open
  name: yatai api server admin api v1 api token resource API
  slug: open-bentoml-api-token-resource-api
- collection_type: open
  name: yatai api server admin api v1 api tokens API
  slug: open-bentoml-api-tokens-api
- collection_type: open
  name: yatai api server admin api v1 API
  slug: open-bentoml-api-v1-api
- collection_type: open
  name: yatai api server admin api v1 auth API
  slug: open-bentoml-auth-api
- collection_type: open
  name: yatai api server admin api v1 bento repositories API
  slug: open-bentoml-bento-repositories-api
- collection_type: open
  name: yatai api server admin api v1 bento repositories statistics API
  slug: open-bentoml-bento-repositories-statistics-api
- collection_type: open
  name: yatai api server admin api v1 bento repository resource API
  slug: open-bentoml-bento-repository-resource-api
- collection_type: open
  name: yatai api server admin api v1 bento resource API
  slug: open-bentoml-bento-resource-api
- collection_type: open
  name: yatai api server admin api v1 bentos API
  slug: open-bentoml-bentos-api
- collection_type: open
  name: yatai api server admin api v1 certified bento repositories API
  slug: open-bentoml-certified-bento-repositories-api
- collection_type: open
  name: yatai api server admin api v1 cluster deployments API
  slug: open-bentoml-cluster-deployments-api
- collection_type: open
  name: yatai api server admin api v1 cluster resource API
  slug: open-bentoml-cluster-resource-api
- collection_type: open
  name: yatai api server admin api v1 cluster resource for admin panel API
  slug: open-bentoml-cluster-resource-for-admin-panel-api
- collection_type: open
  name: yatai api server admin api v1 clusters API
  slug: open-bentoml-clusters-api
- collection_type: open
  name: yatai api server admin api v1 clusters for admin panel API
  slug: open-bentoml-clusters-for-admin-panel-api
- collection_type: open
  name: yatai api server admin api v1 current organization resource API
  slug: open-bentoml-current-organization-resource-api
- collection_type: open
  name: yatai api server admin api v1 customer resource API
  slug: open-bentoml-customer-resource-api
- collection_type: open
  name: yatai api server admin api v1 customers API
  slug: open-bentoml-customers-api
- collection_type: open
  name: yatai api server admin api v1 deployment resource API
  slug: open-bentoml-deployment-resource-api
- collection_type: open
  name: yatai api server admin api v1 deployment revision resource API
  slug: open-bentoml-deployment-revision-resource-api
- collection_type: open
  name: yatai api server admin api v1 deployment revisions API
  slug: open-bentoml-deployment-revisions-api
- collection_type: open
  name: yatai api server admin api v1 deployment v2 revision resource API
  slug: open-bentoml-deployment-v2-revision-resource-api
- collection_type: open
  name: yatai api server admin api v1 deployment v2 revisions API
  slug: open-bentoml-deployment-v2-revisions-api
- collection_type: open
  name: yatai api server admin api v1 endpoint resource API
  slug: open-bentoml-endpoint-resource-api
- collection_type: open
  name: yatai api server admin api v1 gpu config resource API
  slug: open-bentoml-gpu-config-resource-api
- collection_type: open
  name: yatai api server admin api v1 gpu configs API
  slug: open-bentoml-gpu-configs-api
- collection_type: open
  name: yatai api server admin api v1 host cluster resource API
  slug: open-bentoml-host-cluster-resource-api
- collection_type: open
  name: yatai api server admin api v1 host_clusters API
  slug: open-bentoml-host-clusters-api
- collection_type: open
  name: yatai api server admin api v1 instance_types API
  slug: open-bentoml-instance-types-api
- collection_type: open
  name: yatai api server admin api v1 labels API
  slug: open-bentoml-labels-api
- collection_type: open
  name: yatai api server admin api v1 lago billable metrics API
  slug: open-bentoml-lago-billable-metrics-api
- collection_type: open
  name: yatai api server admin api v1 lago customer API
  slug: open-bentoml-lago-customer-api
- collection_type: open
  name: yatai api server admin api v1 lago plan API
  slug: open-bentoml-lago-plan-api
- collection_type: open
  name: yatai api server admin api v1 limit group resource API
  slug: open-bentoml-limit-group-resource-api
- collection_type: open
  name: yatai api server admin api v1 limit groups API
  slug: open-bentoml-limit-groups-api
- collection_type: open
  name: yatai api server admin api v1 model repositories API
  slug: open-bentoml-model-repositories-api
- collection_type: open
  name: yatai api server admin api v1 model repository resource API
  slug: open-bentoml-model-repository-resource-api
- collection_type: open
  name: yatai api server admin api v1 model resource API
  slug: open-bentoml-model-resource-api
- collection_type: open
  name: yatai api server admin api v1 models API
  slug: open-bentoml-models-api
- collection_type: open
  name: yatai api server admin api v1 org resource for admin panel API
  slug: open-bentoml-org-resource-for-admin-panel-api
- collection_type: open
  name: yatai api server admin api v1 organization resource API
  slug: open-bentoml-organization-resource-api
- collection_type: open
  name: yatai api server admin api v1 organization secrets API
  slug: open-bentoml-organization-secrets-api
- collection_type: open
  name: yatai api server admin api v1 organization secrets with check message API
  slug: open-bentoml-organization-secrets-with-check-message-api
- collection_type: open
  name: yatai api server admin api v1 organization secrets with template API
  slug: open-bentoml-organization-secrets-with-template-api
- collection_type: open
  name: yatai api server admin api v1 plans API
  slug: open-bentoml-plans-api
- collection_type: open
  name: yatai api server admin api v1 request quota API
  slug: open-bentoml-request-quota-api
- collection_type: open
  name: yatai api server admin api v1 resource instance resource API
  slug: open-bentoml-resource-instance-resource-api
- collection_type: open
  name: yatai api server admin api v1 resource instances API
  slug: open-bentoml-resource-instances-api
- collection_type: open
  name: yatai api server admin api v1 secret names API
  slug: open-bentoml-secret-names-api
- collection_type: open
  name: yatai api server admin api v1 slim bento repositories API
  slug: open-bentoml-slim-bento-repositories-api
- collection_type: open
  name: yatai api server admin api v1 terminal record resource API
  slug: open-bentoml-terminal-record-resource-api
- collection_type: open
  name: yatai api server admin api v1 usage API
  slug: open-bentoml-usage-api
- collection_type: open
  name: yatai api server admin api v1 user resource API
  slug: open-bentoml-user-resource-api
- collection_type: open
  name: yatai api server admin api v1 users API
  slug: open-bentoml-users-api
- collection_type: open
  name: yatai api server admin api v1 websocket v1 API
  slug: open-bentoml-websocket-v1-api
- collection_type: open
  name: yatai api server admin api v1 websocket v2 API
  slug: open-bentoml-websocket-v2-api
- collection_type: open
  name: yatai api server admin api v1 yatai components API
  slug: open-bentoml-yatai-components-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/bentoml-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bentoml-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bentoml-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bentoml-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.bentoml.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bentoml.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bentoml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bentoml
- group: company
  title: ''
  type: Blog
  url: https://www.bentoml.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bentoml.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bentoml.com/
- group: other
  title: ''
  type: X
  url: https://x.com/bentomlai
- group: build
  title: ''
  type: CLI
  url: https://docs.bentoml.com/en/latest/reference/bentoml/cli.html
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/bentoml/refs/heads/main/plans/bentoml-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/bentoml/refs/heads/main/rate-limits/bentoml-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/bentoml/refs/heads/main/finops/bentoml-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/bentoml/refs/heads/main/vocabulary/bentoml-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/bentoml/refs/heads/main/json-schema/bentoml-schemas.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/bentoml/refs/heads/main/json-ld/bentoml-context.jsonld
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/bentoml/refs/heads/main/examples/bentoml-api-examples.json
created: 2026-06-12
description: BentoML is an open-source unified inference platform for building, packaging, and deploying machine learning models as scalable REST API services. Developers define services using Python class decorators that automatically expose model inference logic as HTTP endpoints. BentoCloud, the managed cloud offering, provides autoscaling infrastructure, GPU instance provisioning, scale-to-zero cost optimization, and a control-plane API for programmatic deployment lifecycle management. The platform supports all major ML frameworks including PyTorch, TensorFlow, Transformers, ONNX, XGBoost, and Scikit-Learn, and is licensed under Apache 2.0.
finops:
- name: Bentoml Finops
  service_category: ''
  slug: bentoml-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bentoml.png
json_schemas:
- name: BentoML / BentoCloud API Schemas
  property_count: 0
  slug: bentoml-schemas
jsonld:
- class_count: 6
  name: Bentoml Context
  property_count: 24
  slug: bentoml-context
layout: provider
modified: 2026-06-12
name: BentoML
nav: Providers
network: true
overview: 'BentoML publishes 59 APIs on the [APIs.io](https://apis.io/) network, including admin api v1 API, admin deployment resource API, api token resource API, and 56 more. Tagged areas include Machine-Learning, Model Serving, Inference, Artificial Intelligence, and REST API.


  The BentoML catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BentoML''s developer surface includes authentication, documentation, engineering blog, pricing, CLI, code examples, and 14 more developer resources.'
plans:
- name: Bentoml Plans Pricing
  plan_count: 3
  slug: bentoml-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 6
  name: Bentoml Rate Limits
  slug: bentoml-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: BentoML API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: bentoml-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 75.3
    catalog_earned_first_party: 0.0
    catalog_gap: 39.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 25.0
    contract_quality: 59.6
    developer_ergonomics: 31.0
    discoverability: 53.7
    governance: 25.0
    operational_transparency: 50.0
  previous_composite: 44.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 59
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bentoml/refs/heads/main/screenshots/bentoml-2026-06-20T173142.png
security:
- kind: authentication
  name: Bentoml Authentication
  slug: bentoml-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bentoml Domain Security
  slug: bentoml-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bentoml
tags:
- Machine-Learning
- Model Serving
- Inference
- Artificial Intelligence
- REST API
- MLOps
- Deployment
- GPU
- LLM
- BentoCloud
website: https://www.bentoml.com/
---
