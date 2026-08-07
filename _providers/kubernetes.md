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
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Kubernetes Agentic Access
  operation_count: 34
  slug: kubernetes-agentic-access
  summary_line: 34 operations · 17 acting
api_count: 7
apis:
- description: Autoscaling resources including HorizontalPodAutoscalers for automatically scaling workloads based on observed metrics.
  name: Kubernetes Autoscaling API
  slug: kubernetes-autoscaling-api
- description: Cluster-level resources including Namespaces, Nodes, ServiceAccounts, and RBAC resources for cluster administration.
  name: Kubernetes Cluster API
  slug: kubernetes-cluster-api
- description: Configuration and storage resources including ConfigMaps, Secrets, PersistentVolumes, and PersistentVolumeClaims.
  name: Kubernetes Config API
  slug: kubernetes-config-api
- description: Event resources capturing occurrences within the cluster such as pod scheduling, container restarts, and resource state changes.
  name: Kubernetes Events API
  slug: kubernetes-events-api
- description: The Namespaces API from Kubernetes — 2 operation(s) for namespaces.
  name: Kubernetes Namespaces API
  slug: kubernetes-namespaces-api
- description: Role-based access control resources including Roles, RoleBindings, ClusterRoles, and ClusterRoleBindings for managing authorization.
  name: Kubernetes RBAC API
  slug: kubernetes-rbac-api
- description: Workload resources including Pods, Deployments, StatefulSets, DaemonSets, ReplicaSets, Jobs, and CronJobs for managing containerized applications.
  name: Kubernetes Workloads API
  slug: kubernetes-workloads-api
arazzos:
- description: Confirm a deployment exists, create an HPA targeting it, and list the namespace's autoscalers.
  name: Kubernetes Attach a HorizontalPodAutoscaler to a Deployment
  slug: kubernetes-autoscale-deployment-workflow
- description: List the cluster's nodes, read one node's capacity and conditions in full, and enumerate namespaces.
  name: Kubernetes Audit Cluster Node Capacity
  slug: kubernetes-cluster-capacity-audit-workflow
- description: Inventory existing ConfigMaps, publish the new configuration, then roll the deployment that reads it.
  name: Kubernetes Publish a ConfigMap and Roll Out Its Consumers
  slug: kubernetes-config-rollout-workflow
- description: Create a namespace, seed its config and secrets, deploy the workload, and expose it behind a service.
  name: Kubernetes Deploy an Application into a New Namespace
  slug: kubernetes-deploy-application-workflow
- description: Resolve a deployment, then create a fronting service or replace the existing one to match.
  name: Kubernetes Expose a Deployment Behind a Service
  slug: kubernetes-expose-deployment-workflow
- description: Read a namespace, replace it carrying governance labels, and confirm the labels stuck.
  name: Kubernetes Apply Governance Labels to a Namespace
  slug: kubernetes-namespace-labeling-workflow
- description: Check whether a ClusterRole already exists and create it only when it does not.
  name: Kubernetes Provision a ClusterRole If Missing
  slug: kubernetes-provision-cluster-role-workflow
- description: Relabel a misbehaving pod out of its service and ReplicaSet, then capture its logs while it stays alive.
  name: Kubernetes Quarantine a Failing Pod for Inspection
  slug: kubernetes-quarantine-pod-workflow
- description: Confirm a pod is controller-owned, delete it gracefully, and watch the replacement appear.
  name: Kubernetes Restart a Pod by Deleting It
  slug: kubernetes-restart-pod-workflow
- description: Find an application's deployment, remove its service and deployment, and confirm the pods are gone.
  name: Kubernetes Retire an Application from a Namespace
  slug: kubernetes-retire-application-workflow
- description: Read a deployment, replace it with an updated image, then watch the rollout and its events.
  name: Kubernetes Roll Out a New Container Image
  slug: kubernetes-rolling-update-workflow
- description: Inventory existing secrets, write the new credential, then roll the deployment that consumes it.
  name: Kubernetes Rotate a Secret and Restart Its Consumers
  slug: kubernetes-rotate-secret-workflow
- description: Create a run-to-completion pod, poll it until it finishes, read its log, then clean it up.
  name: Kubernetes Run a One-Off Task Pod and Collect Its Output
  slug: kubernetes-run-one-off-pod-workflow
- description: Read the current scale of a deployment, set a new replica count, and confirm the pods landed.
  name: Kubernetes Scale a Deployment and Verify Replicas
  slug: kubernetes-scale-deployment-workflow
- description: Record what a namespace contains, delete the namespace, and confirm it entered Terminating.
  name: Kubernetes Inventory and Tear Down a Namespace
  slug: kubernetes-teardown-namespace-workflow
- description: Find pods that are not Running, read the failing pod's detail, tail its logs, and pull namespace events.
  name: Kubernetes Troubleshoot a Failing Pod
  slug: kubernetes-troubleshoot-pod-workflow
artifact_total: 44
asyncapis:
- description: The Kubernetes Watch API provides a streaming event interface for receiving real-time notifications about changes to cluster resources. Clients subscribe to resource types and receive a stream of ADDE
  name: Kubernetes Watch Events
  slug: kubernetes-watch-asyncapi
collections:
- collection_type: postman
  name: Kubernetes Autoscaling API
  slug: postman-kubernetes-autoscaling-api
- collection_type: postman
  name: Kubernetes Autoscaling Cluster API
  slug: postman-kubernetes-cluster-api
- collection_type: postman
  name: Kubernetes Autoscaling Config API
  slug: postman-kubernetes-config-api
- collection_type: postman
  name: Kubernetes Autoscaling Events API
  slug: postman-kubernetes-events-api
- collection_type: postman
  name: Kubernetes Autoscaling Namespaces API
  slug: postman-kubernetes-namespaces-api
- collection_type: postman
  name: Kubernetes Autoscaling RBAC API
  slug: postman-kubernetes-rbac-api
- collection_type: postman
  name: Kubernetes Autoscaling Workloads API
  slug: postman-kubernetes-workloads-api
- collection_type: open
  name: Kubernetes API
  slug: open-kubernetes-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/kubernetes/overview
- group: build
  title: ''
  type: Packages
  url: packages/kubernetes-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kubernetes-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kubernetes-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kubernetes-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/kubernetes-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/kubernetes-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kubernetes-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kubernetes-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kubernetes-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kubernetes-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/kubernetes-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kubernetes-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kubernetes-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kubernetes-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kubernetes-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kubernetes-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kubernetes
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kubernetes
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/kubernetes/kubernetes
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/kubernetes/community
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/kubernetes/kube-openapi
- group: company
  title: ''
  type: Bluesky
  url: https://bsky.app/profile/kubernetes.io
- group: other
  title: ''
  type: X
  url: https://x.com/kubernetesio
- group: company
  title: ''
  type: Website
  url: https://kubernetes.io/
- group: docs
  title: ''
  type: Documentation
  url: https://kubernetes.io/docs/home/
- group: docs
  title: ''
  type: APIReference
  url: https://kubernetes.io/docs/reference/kubernetes-api/
- group: company
  title: ''
  type: Blog
  url: https://kubernetes.io/blog/
- group: learn
  title: ''
  type: Training
  url: https://kubernetes.io/training/
- group: company
  title: ''
  type: Partners
  url: https://kubernetes.io/partners/
- group: operate
  title: ''
  type: ChangeLog
  url: https://kubernetes.io/releases/
- group: operate
  title: ''
  type: Community
  url: https://kubernetes.io/community/
- group: operate
  title: ''
  type: Forums
  url: https://discuss.kubernetes.io/
- group: operate
  title: ''
  type: Slack
  url: https://kubernetes.slack.com
- group: start
  title: ''
  type: Signup
  url: https://slack.k8s.io
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@KubernetesCommunity
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/kubernetes
- group: commercial
  title: ''
  type: License
  url: https://github.com/kubernetes/kubernetes/blob/master/LICENSE
- group: auth
  title: ''
  type: Security
  url: https://kubernetes.io/docs/concepts/security/
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/kubernetes/kubernetes/security/policy
- group: other
  title: ''
  type: Foundation
  url: https://www.cncf.io/projects/kubernetes/
- group: company
  title: ''
  type: Newsletter
  url: https://www.cncf.io/kubeweekly/
- group: start
  title: ''
  type: GettingStarted
  url: https://kubernetes.io/docs/setup/
- group: learn
  title: ''
  type: Tutorials
  url: https://kubernetes.io/docs/tutorials/
- group: other
  title: ''
  type: CaseStudies
  url: https://kubernetes.io/case-studies/
- group: build
  title: ''
  type: CodeOfConduct
  url: https://kubernetes.io/community/code-of-conduct/
- group: operate
  title: ''
  type: DeprecationPolicy
  url: https://kubernetes.io/docs/reference/using-api/deprecation-policy/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/kubernetes-resource-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/kubernetes-context.jsonld
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kubernetes-deploy-application-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kubernetes-scale-deployment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kubernetes-rolling-update-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kubernetes-troubleshoot-pod-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kubernetes-restart-pod-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kubernetes-run-one-off-pod-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kubernetes-teardown-namespace-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kubernetes-autoscale-deployment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kubernetes-cluster-capacity-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kubernetes-provision-cluster-role-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kubernetes-expose-deployment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kubernetes-rotate-secret-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kubernetes-config-rollout-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kubernetes-namespace-labeling-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kubernetes-quarantine-pod-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kubernetes-retire-application-workflow.yml
created: '2025-06-05'
description: Kubernetes, also known as K8s, is an open source system for automating deployment, scaling, and management of containerized applications. It groups containers that make up an application into logical units for easy management and discovery. Kubernetes builds upon 15 years of experience of running production workloads at Google, combined with best-of-breed ideas and practices from the community.
finops:
- name: Kubernetes Finops
  service_category: API
  slug: kubernetes-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kubernetes.png
json_schemas:
- name: Kubernetes Resource
  property_count: 5
  slug: kubernetes-resource
jsonld:
- class_count: 0
  name: Kubernetes Context
  property_count: 36
  slug: kubernetes-context
layout: provider
mcp_servers:
- description: ''
  name: kubernetes-mcp.yml
  slug: kubernetes-mcpyml
modified: '2026-06-20'
name: Kubernetes
nav: Providers
network: true
overview: 'Kubernetes publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Autoscaling API, Cluster API, Config API, and 4 more. Tagged areas include Automation, Cloud Native, CNCF, Containers, and Deployment.


  The Kubernetes catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Kubernetes'' developer surface includes changelog, CLI, authentication, documentation, API reference, engineering blog, training material, and 58 more developer resources.'
plans:
- name: Kubernetes Plans Pricing
  plan_count: 3
  slug: kubernetes-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 5
  name: Kubernetes Rate Limits
  slug: kubernetes-rate-limits
rules:
- name: Kubernetes API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: kubernetes-asyncapi-spectral-rules
- name: Kubernetes API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: kubernetes-jsonschema-spectral-rules
score:
  band: strong
  composite: 65.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 85.3
    developer_ergonomics: 56.5
    discoverability: 92.6
    governance: 53.1
    operational_transparency: 71.1
  previous_composite: 65.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kubernetes/refs/heads/main/screenshots/kubernetes-2026-06-20T184206.png
security:
- kind: authentication
  name: Kubernetes Authentication
  slug: kubernetes-authentication
  summary_line: http/mutualTLS · 2 schemes
- kind: domain-security
  name: Kubernetes Domain Security
  slug: kubernetes-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Kubernetes Vulnerability Disclosure
  slug: kubernetes-vulnerability-disclosure
  summary_line: disclosure policy published
slug: kubernetes
tags:
- Automation
- Cloud Native
- CNCF
- Containers
- Deployment
- Open Source
- Orchestration
- Scaling
website: https://kubernetes.io/
---
