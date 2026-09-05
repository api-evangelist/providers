---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 62
  human_in_the_loop: 2
  name: Paperspace Agentic Access
  operation_count: 113
  slug: paperspace-agentic-access
  summary_line: 113 operations · 62 acting · 2 human-in-the-loop
api_count: 4
apis:
- baseURL: https://api.paperspace.com/v1
  baseurl_source: spec
  description: 'Programmatically manage Paperspace virtual machines — GPU and CPU compute instances. Covers the machine lifecycle (create, start, stop, restart, delete), machine events, team-member access grants per '
  name: Paperspace Machines API
  slug: paperspace-machines-api
- baseURL: https://api.paperspace.com/v1
  baseurl_source: spec
  description: Container-as-a-service deployments that run user-provided images on Paperspace GPU machines with a managed endpoint, autoscaling, rolling updates, runs, metrics, logs, and revision history. Includes t
  name: Paperspace Deployments API
  slug: paperspace-deployments-api
- baseURL: https://api.paperspace.com/v1
  baseurl_source: spec
  description: Projects are the top-level organizing container in Paperspace. The Projects API covers project lifecycle, activity feeds, collaborator management, project-scoped secrets, tags, and model linkage.
  name: Paperspace Projects API
  slug: paperspace-projects-api
- baseURL: https://api.paperspace.com/v1
  baseurl_source: spec
  description: Versioned data collections used by Paperspace Gradient notebooks, workflows, and deployments. The Datasets API exposes the dataset lifecycle plus a versioned data revision sub-resource.
  name: Paperspace Datasets API
  slug: paperspace-datasets-api
- baseURL: https://api.paperspace.com/v1
  baseurl_source: spec
  description: Manage container registry credentials used by Paperspace Deployments to pull private images, including a test-connection endpoint that verifies the configured credentials.
  name: Paperspace Container Registries API
  slug: paperspace-container-registries-api
- baseURL: https://api.paperspace.com/v1
  baseurl_source: spec
  description: Register and manage trained ML models in the Paperspace Gradient model registry. Models can be associated with projects and consumed by Deployments.
  name: Paperspace Models API
  slug: paperspace-models-api
- baseURL: https://api.paperspace.com/v1
  baseurl_source: spec
  description: The Activity API from Paperspace — 1 operation(s) for activity.
  name: Paperspace Activity API
  slug: paperspace-activity-api
- baseURL: https://api.paperspace.com/v1
  baseurl_source: spec
  description: The Authentication API from Paperspace — 1 operation(s) for authentication.
  name: Paperspace Authentication API
  slug: paperspace-authentication-api
- baseURL: https://api.paperspace.com/v1
  baseurl_source: spec
  description: The Collaborators API from Paperspace — 2 operation(s) for collaborators.
  name: Paperspace Collaborators API
  slug: paperspace-collaborators-api
- baseURL: https://api.paperspace.com/v1
  baseurl_source: spec
  description: The Custom Templates API from Paperspace — 2 operation(s) for custom templates.
  name: Paperspace Custom Templates API
  slug: paperspace-custom-templates-api
- baseURL: https://api.paperspace.com/v1
  baseurl_source: spec
  description: The Dataset Versions API from Paperspace — 2 operation(s) for dataset versions.
  name: Paperspace Dataset Versions API
  slug: paperspace-dataset-versions-api
- baseURL: https://api.paperspace.com/v1
  baseurl_source: spec
  description: Team-member access grants on individual machines.
  name: Paperspace Machine Access API
  slug: paperspace-machine-access-api
- baseURL: https://api.paperspace.com/v1
  baseurl_source: spec
  description: Machine-event history stream.
  name: Paperspace Machine Events API
  slug: paperspace-machine-events-api
- baseURL: https://api.paperspace.com/v1
  baseurl_source: spec
  description: Region/availability lookups for machine types.
  name: Paperspace Machine Types API
  slug: paperspace-machine-types-api
- baseURL: https://api.paperspace.com/v1
  baseurl_source: spec
  description: The OS Templates API from Paperspace — 1 operation(s) for os templates.
  name: Paperspace OS Templates API
  slug: paperspace-os-templates-api
- baseURL: https://api.paperspace.com/v1
  baseurl_source: spec
  description: The Private Networks API from Paperspace — 2 operation(s) for private networks.
  name: Paperspace Private Networks API
  slug: paperspace-private-networks-api
- baseURL: https://api.paperspace.com/v1
  baseurl_source: spec
  description: The Public IPs API from Paperspace — 2 operation(s) for public ips.
  name: Paperspace Public IPs API
  slug: paperspace-public-ips-api
- baseURL: https://api.paperspace.com/v1
  baseurl_source: spec
  description: The Secrets API from Paperspace — 2 operation(s) for secrets.
  name: Paperspace Secrets API
  slug: paperspace-secrets-api
- baseURL: https://api.paperspace.com/v1
  baseurl_source: spec
  description: The Shared Drives API from Paperspace — 2 operation(s) for shared drives.
  name: Paperspace Shared Drives API
  slug: paperspace-shared-drives-api
- baseURL: https://api.paperspace.com/v1
  baseurl_source: spec
  description: The Snapshots API from Paperspace — 3 operation(s) for snapshots.
  name: Paperspace Snapshots API
  slug: paperspace-snapshots-api
- baseURL: https://api.paperspace.com/v1
  baseurl_source: spec
  description: The Startup Scripts API from Paperspace — 4 operation(s) for startup scripts.
  name: Paperspace Startup Scripts API
  slug: paperspace-startup-scripts-api
- baseURL: https://api.paperspace.com/v1
  baseurl_source: spec
  description: The Storage Providers API from Paperspace — 3 operation(s) for storage providers.
  name: Paperspace Storage Providers API
  slug: paperspace-storage-providers-api
- baseURL: https://api.paperspace.com/v1
  baseurl_source: spec
  description: The Tags API from Paperspace — 1 operation(s) for tags.
  name: Paperspace Tags API
  slug: paperspace-tags-api
- baseURL: https://api.paperspace.com/v1
  baseurl_source: spec
  description: The Team Members API from Paperspace — 2 operation(s) for team members.
  name: Paperspace Team Members API
  slug: paperspace-team-members-api
- baseURL: https://api.paperspace.com/v1
  baseurl_source: spec
  description: The Team Secrets API from Paperspace — 2 operation(s) for team secrets.
  name: Paperspace Team Secrets API
  slug: paperspace-team-secrets-api
artifact_total: 109
collections:
- collection_type: postman
  name: Paperspace Container Registries Activity API
  slug: postman-paperspace-activity-api
- collection_type: postman
  name: Paperspace Container Registries Activity Authentication API
  slug: postman-paperspace-authentication-api
- collection_type: postman
  name: Paperspace Container Registries Activity Collaborators API
  slug: postman-paperspace-collaborators-api
- collection_type: postman
  name: Paperspace Activity Container Registries API
  slug: postman-paperspace-container-registries-api
- collection_type: postman
  name: Paperspace Container Registries Activity Custom Templates API
  slug: postman-paperspace-custom-templates-api
- collection_type: postman
  name: Paperspace Container Registries Activity Dataset Versions API
  slug: postman-paperspace-dataset-versions-api
- collection_type: postman
  name: Paperspace Container Registries Activity Datasets API
  slug: postman-paperspace-datasets-api
- collection_type: postman
  name: Paperspace Container Registries Activity Deployments API
  slug: postman-paperspace-deployments-api
- collection_type: postman
  name: Paperspace Container Registries Activity Machine Access API
  slug: postman-paperspace-machine-access-api
- collection_type: postman
  name: Paperspace Container Registries Activity Machine Events API
  slug: postman-paperspace-machine-events-api
- collection_type: postman
  name: Paperspace Container Registries Activity Machine Types API
  slug: postman-paperspace-machine-types-api
- collection_type: postman
  name: Paperspace Container Registries Activity Machines API
  slug: postman-paperspace-machines-api
- collection_type: postman
  name: Paperspace Container Registries Activity Models API
  slug: postman-paperspace-models-api
- collection_type: postman
  name: Paperspace Container Registries Activity OS Templates API
  slug: postman-paperspace-os-templates-api
- collection_type: postman
  name: Paperspace Container Registries Activity Private Networks API
  slug: postman-paperspace-private-networks-api
- collection_type: postman
  name: Paperspace Container Registries Activity Projects API
  slug: postman-paperspace-projects-api
- collection_type: postman
  name: Paperspace Container Registries Activity Public IPs API
  slug: postman-paperspace-public-ips-api
- collection_type: postman
  name: Paperspace Container Registries Activity Secrets API
  slug: postman-paperspace-secrets-api
- collection_type: postman
  name: Paperspace Container Registries Activity Shared Drives API
  slug: postman-paperspace-shared-drives-api
- collection_type: postman
  name: Paperspace Container Registries Activity Snapshots API
  slug: postman-paperspace-snapshots-api
- collection_type: postman
  name: Paperspace Container Registries Activity Startup Scripts API
  slug: postman-paperspace-startup-scripts-api
- collection_type: postman
  name: Paperspace Container Registries Activity Storage Providers API
  slug: postman-paperspace-storage-providers-api
- collection_type: postman
  name: Paperspace Container Registries Activity Tags API
  slug: postman-paperspace-tags-api
- collection_type: postman
  name: Paperspace Container Registries Activity Team Members API
  slug: postman-paperspace-team-members-api
- collection_type: postman
  name: Paperspace Container Registries Activity Team Secrets API
  slug: postman-paperspace-team-secrets-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Paperspace Container Registries Activity API
  slug: open-paperspace-activity-api
- collection_type: open
  name: Paperspace Container Registries Activity Authentication API
  slug: open-paperspace-authentication-api
- collection_type: open
  name: Paperspace Container Registries Activity Collaborators API
  slug: open-paperspace-collaborators-api
- collection_type: open
  name: Paperspace Activity Container Registries API
  slug: open-paperspace-container-registries-api
- collection_type: open
  name: Paperspace Container Registries Activity Custom Templates API
  slug: open-paperspace-custom-templates-api
- collection_type: open
  name: Paperspace Container Registries Activity Dataset Versions API
  slug: open-paperspace-dataset-versions-api
- collection_type: open
  name: Paperspace Container Registries Activity Datasets API
  slug: open-paperspace-datasets-api
- collection_type: open
  name: Paperspace Container Registries Activity Deployments API
  slug: open-paperspace-deployments-api
- collection_type: open
  name: Paperspace Container Registries Activity Machine Access API
  slug: open-paperspace-machine-access-api
- collection_type: open
  name: Paperspace Container Registries Activity Machine Events API
  slug: open-paperspace-machine-events-api
- collection_type: open
  name: Paperspace Container Registries Activity Machine Types API
  slug: open-paperspace-machine-types-api
- collection_type: open
  name: Paperspace Container Registries Activity Machines API
  slug: open-paperspace-machines-api
- collection_type: open
  name: Paperspace Container Registries Activity Models API
  slug: open-paperspace-models-api
- collection_type: open
  name: Paperspace Networking API
  slug: open-paperspace-networking-api
- collection_type: open
  name: Paperspace Container Registries Activity OS Templates API
  slug: open-paperspace-os-templates-api
- collection_type: open
  name: Paperspace Container Registries Activity Private Networks API
  slug: open-paperspace-private-networks-api
- collection_type: open
  name: Paperspace Container Registries Activity Projects API
  slug: open-paperspace-projects-api
- collection_type: open
  name: Paperspace Container Registries Activity Public IPs API
  slug: open-paperspace-public-ips-api
- collection_type: open
  name: Paperspace Container Registries Activity Secrets API
  slug: open-paperspace-secrets-api
- collection_type: open
  name: Paperspace Container Registries Activity Shared Drives API
  slug: open-paperspace-shared-drives-api
- collection_type: open
  name: Paperspace Container Registries Activity Snapshots API
  slug: open-paperspace-snapshots-api
- collection_type: open
  name: Paperspace Container Registries Activity Startup Scripts API
  slug: open-paperspace-startup-scripts-api
- collection_type: open
  name: Paperspace Storage API
  slug: open-paperspace-storage-api
- collection_type: open
  name: Paperspace Container Registries Activity Storage Providers API
  slug: open-paperspace-storage-providers-api
- collection_type: open
  name: Paperspace Container Registries Activity Tags API
  slug: open-paperspace-tags-api
- collection_type: open
  name: Paperspace Team and Authentication API
  slug: open-paperspace-team-auth-api
- collection_type: open
  name: Paperspace Container Registries Activity Team Members API
  slug: open-paperspace-team-members-api
- collection_type: open
  name: Paperspace Container Registries Activity Team Secrets API
  slug: open-paperspace-team-secrets-api
- collection_type: open
  name: Paperspace Templates and Startup Scripts API
  slug: open-paperspace-templates-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/digital-ocean/
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/paperspace-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/paperspace/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paperspace-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/paperspace-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paperspace-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paperspace-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.paperspace.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.digitalocean.com/products/paperspace/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.digitalocean.com/reference/paperspace/api-reference/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.digitalocean.com/reference/paperspace/api-keys/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.digitalocean.com/reference/paperspace/cli/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.paperspace.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://console.paperspace.com/signup
- group: start
  title: ''
  type: Console
  url: https://console.paperspace.com
- group: company
  title: ''
  type: Blog
  url: https://blog.paperspace.com
- group: operate
  title: ''
  type: Forums
  url: https://community.paperspace.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.paperspace.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.paperspace.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.paperspace.com/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.paperspace.com/contact-sales
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Paperspace
- group: build
  title: ''
  type: CLI
  url: https://github.com/Paperspace/cli
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Paperspace/CORE-API-Docs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Paperspace/paperspace-node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Paperspace/paperspace-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Paperspace/paperspace-python
- group: build
  title: ''
  type: CLI
  url: https://github.com/Paperspace/gradient-cli
- group: build
  title: ''
  type: Tools
  url: https://github.com/Paperspace/terraform-provider-paperspace
- group: build
  title: ''
  type: Tools
  url: https://github.com/Paperspace/deploy-action
- group: build
  title: ''
  type: Tools
  url: https://github.com/Paperspace/ml-in-a-box
- group: build
  title: ''
  type: Tools
  url: https://github.com/Paperspace/fastai-docker
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Paperspace/app-template
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Paperspace/stable-diffusion-app
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Paperspace/FastAPI-Template-App
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Paperspace/FastAPI-Hugging-Face-Template-App
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Paperspace/Flask-Template-App
- group: learn
  title: ''
  type: Courses
  url: https://github.com/Paperspace/PyTorch-101-Tutorial-Series
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Paperspace/DataAugmentationForObjectDetection
- group: other
  title: ''
  type: X
  url: https://x.com/HelloPaperspace
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/paperspace
- group: commercial
  title: ''
  type: Plans
  url: plans/paperspace-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/paperspace-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/paperspace-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/paperspace-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/paperspace-rules.yml
created: '2026-05-25T00:00:00.000Z'
description: Paperspace is a GPU cloud platform for AI, ML, and 3D rendering workloads, acquired by DigitalOcean in 2023. The platform combines on-demand GPU/CPU machines (Core), the Gradient ML workflow stack (Notebooks, Datasets, Models, Workflows), and container-as-a-service Deployments under a single team-scoped REST API at api.paperspace.com/v1. Compute is billed per second across H100, A100, A6000, V100, A5000, A4000, and P6000 SKUs, with Bearer-token authentication using team-scoped API keys.
examples:
- key_count: 2
  name: Paperspace Create Machine Example
  slug: paperspace-create-machine-example
- key_count: 2
  name: Paperspace Upsert Deployment Example
  slug: paperspace-upsert-deployment-example
features:
- GPU and CPU virtual machines (Machines API) — H100, A100-80G, A6000, A5000, A4000, V100, P6000 SKUs
- Container-as-a-service Deployments with autoscaling, managed endpoint, rolling updates, runs, metrics, logs, and revision history
- Gradient ML platform — Notebooks (Jupyter), versioned Datasets, and a model registry
- Projects as the organizing container with collaborators, secrets, tags, activity feeds, and model linkage
- Private networks (VPCs) and claim/assign/release lifecycle for public IPv4 addresses
- Shared drives attached to a private network and per-machine snapshots with point-in-time restore
- External storage providers (S3, GCS, Azure Blob) plus a team-level storage utilization breakdown
- OS and custom machine templates plus startup scripts with assign/unassign-to-machine semantics
- Container registry credentials with a test-connection endpoint, consumed by Deployments
- Team-scoped API keys (Bearer auth) and a session lookup endpoint that returns user, team, and preferences
- Team-member roster management plus team-scoped secrets shared across projects in a team
- Per-second compute billing with up to 70% advertised savings vs. major cloud providers
- Terraform provider, GitHub Action for deployments, Paperspace CLI, and a Gradient Python CLI
- DigitalOcean acquisition — Paperspace billing is consolidated into the DigitalOcean account billing surface
finops:
- name: Paperspace Finops
  service_category: ''
  slug: paperspace-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paperspace.png
json_schemas:
- name: Paperspace Deployment
  property_count: 11
  slug: paperspace-deployment
- name: Paperspace Machine
  property_count: 18
  slug: paperspace-machine
json_structures:
- name: Paperspace Machine Structure
  property_count: 0
  slug: paperspace-machine-structure
jsonld:
- class_count: 22
  name: Paperspace Context
  property_count: 2
  slug: paperspace-context
layout: provider
modified: '2026-05-25'
name: Paperspace
nav: Providers
network: true
overview: 'Paperspace publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Machines API, Deployments API, Projects API, and 22 more. Tagged areas include GPU, Cloud, Artificial Intelligence, Machine-Learning, and Deep Learning.


  The Paperspace catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Paperspace''s developer surface includes authentication, developer portal, documentation, pricing, signup flow, developer console, engineering blog, and 39 more developer resources.'
plans:
- name: Paperspace Plans Pricing
  plan_count: 6
  slug: paperspace-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Paperspace Rate Limits
  slug: paperspace-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Paperspace API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: paperspace-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Paperspace API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: paperspace-rules
score:
  band: strong
  composite: 59.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 70.5
    catalog_earned_first_party: 0.0
    catalog_gap: 44.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 28.8
    contract_quality: 66.8
    developer_ergonomics: 63.1
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 18.4
  previous_composite: 60.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paperspace/refs/heads/main/screenshots/paperspace-2026-06-20T191351.png
security:
- kind: authentication
  name: Paperspace Authentication
  slug: paperspace-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Paperspace Domain Security
  slug: paperspace-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Paperspace Trust Center
  slug: paperspace-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: paperspace
tags:
- GPU
- Cloud
- Artificial Intelligence
- Machine-Learning
- Deep Learning
- Compute
- DigitalOcean
- Containers
- Notebooks
- Gradient
website: https://www.paperspace.com
---
