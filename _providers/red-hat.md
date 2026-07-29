---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 63.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Red Hat Agentic Access
  operation_count: 77
  slug: red-hat-agentic-access
  summary_line: 77 operations · 27 acting
api_count: 75
apis:
- description: API for managing Red Hat subscriptions, entitlements, and system registrations.
  name: Red Hat Subscription Management API
  slug: red-hat-subscription-management-api
- description: API for managing multiple Kubernetes clusters across hybrid cloud environments, providing cluster lifecycle management, policy-based governance, and application deployment.
  name: Red Hat Advanced Cluster Management API
  slug: red-hat-advanced-cluster-management-api
- description: REST API for managing Kubernetes-native security including vulnerability management, compliance, network segmentation, and risk profiling across OpenShift and Kubernetes clusters.
  name: Red Hat Advanced Cluster Security API
  slug: red-hat-advanced-cluster-security-api
- description: API management platform providing access control, rate limiting, analytics, and developer portal capabilities for managing the full lifecycle of APIs.
  name: Red Hat 3scale API Management
  slug: red-hat-3scale-api-management
- description: API for tracking and analyzing costs associated with Red Hat OpenShift clusters and cloud infrastructure, providing visibility into resource consumption and spend.
  name: Red Hat Cost Management API
  slug: red-hat-cost-management-api
- description: API for building customized RHEL system images for deployment across cloud providers, virtualization platforms, and bare metal environments through the Hybrid Cloud Console.
  name: Red Hat Image Builder API
  slug: red-hat-image-builder-api
- description: API for assessing and monitoring security vulnerabilities across RHEL systems, providing CVE tracking, severity scoring, and remediation guidance.
  name: Red Hat Vulnerability Management API
  slug: red-hat-vulnerability-management-api
- description: API for managing and applying patches to RHEL systems, providing advisories, package updates, and system patch status through the Hybrid Cloud Console.
  name: Red Hat Patch API
  slug: red-hat-patch-api
- description: API for managing security policy compliance assessments on RHEL systems using SCAP profiles, providing compliance scoring, reporting, and policy management.
  name: Red Hat Compliance API
  slug: red-hat-compliance-api
- description: REST API for managing schemas and API design artifacts in a schema registry, supporting formats including Avro, JSON Schema, Protobuf, OpenAPI, and AsyncAPI.
  name: Red Hat Build of Apicurio Registry API
  slug: red-hat-build-of-apicurio-registry-api
- description: HTTP bridge API for producing and consuming messages to Apache Kafka topics without requiring a native Kafka client, deployed as part of Red Hat Streams for Apache Kafka on OpenShift.
  name: Red Hat Streams for Apache Kafka Bridge API
  slug: red-hat-streams-for-apache-kafka-bridge-api
- description: AI-powered API that provides generative AI assistance for creating Ansible automation content, helping users generate Ansible Playbooks and task recommendations.
  name: Red Hat Ansible Lightspeed API
  slug: red-hat-ansible-lightspeed-api
- description: REST API for managing host inventory data within the Hybrid Cloud Console, providing system profile information, tagging, grouping, and host lifecycle management.
  name: Red Hat Managed Inventory API
  slug: red-hat-managed-inventory-api
- description: API for creating and managing automated remediation playbooks that address security vulnerabilities, compliance issues, and configuration drift identified by Red Hat Insights services.
  name: Red Hat Remediations API
  slug: red-hat-remediations-api
- description: API for managing notification preferences, integrations, and event routing within the Hybrid Cloud Console, enabling alerts through email, webhook, and third-party services.
  name: Red Hat Notifications API
  slug: red-hat-notifications-api
- description: API for managing role-based access control policies within the Hybrid Cloud Console, including user groups, roles, permissions, and access policies.
  name: Red Hat Role-Based Access Control API
  slug: red-hat-role-based-access-control-api
- description: Predictive analytics API that provides proactive recommendations for improving the stability, performance, and security of RHEL systems through the Hybrid Cloud Console.
  name: Red Hat Advisor API
  slug: red-hat-advisor-api
- description: API for detecting potential malware signatures on RHEL systems registered with the Hybrid Cloud Console, providing scanning results and threat analysis.
  name: Red Hat Malware Detection API
  slug: red-hat-malware-detection-api
- description: API for managing source connections and integrations within the Hybrid Cloud Console, enabling connectivity to cloud providers and other external services.
  name: Red Hat Sources API
  slug: red-hat-sources-api
- description: API for configuring third-party integrations and notification endpoints within the Hybrid Cloud Console, supporting webhook, email, and service integrations.
  name: Red Hat Integrations API
  slug: red-hat-integrations-api
- description: API for analyzing resource utilization and providing optimization recommendations for RHEL systems, helping right-size workloads and reduce waste.
  name: Red Hat Resource Optimization API
  slug: red-hat-resource-optimization-api
- description: API for exporting data from Hybrid Cloud Console services in JSON or CSV formats, enabling bulk data retrieval for inventory, notifications, and other services.
  name: Red Hat Export Service API
  slug: red-hat-export-service-api
- description: API for dispatching and managing Ansible Playbook execution on hosts connected via Cloud Connector, enabling automated remediation and configuration management.
  name: Red Hat Playbook Dispatcher API
  slug: red-hat-playbook-dispatcher-api
- description: API for managing custom and Red Hat content repositories within the Hybrid Cloud Console, enabling organizations to curate and distribute software packages.
  name: Red Hat Content Sources API
  slug: red-hat-content-sources-api
- description: API for managing and issuing Red Hat-generated tasks on registered infrastructure, enabling automated system maintenance and configuration operations.
  name: Red Hat Tasks API
  slug: red-hat-tasks-api
- description: API for monitoring and reporting Red Hat subscription utilization including OpenShift, RHEL, and other product usage metrics for capacity planning and compliance.
  name: Red Hat Subscriptions Usage API
  slug: red-hat-subscriptions-usage-api
- description: API for managing user subscriptions, clusters, and organizations through the OpenShift Cluster Manager, providing account-level operations and resource management.
  name: Red Hat Account Management Service API
  slug: red-hat-account-management-service-api
- description: API for managing access control on resources of OpenShift Cluster Manager services, enabling fine-grained authorization policies and permission management.
  name: Red Hat Authorization Service API
  slug: red-hat-authorization-service-api
- description: API for receiving and maintaining logs from internal sources related to OpenShift clusters, providing centralized log management and retrieval.
  name: Red Hat Service Logs API
  slug: red-hat-service-logs-api
- description: REST API for managing connectors that enable integration between Red Hat services and external systems, supporting connector lifecycle operations.
  name: Red Hat Connector Management API
  slug: red-hat-connector-management-api
- description: API for retrieving upgrade path information and recommendations for OpenShift clusters, helping plan and execute cluster version upgrades safely.
  name: Red Hat Upgrades Information Service API
  slug: red-hat-upgrades-information-service-api
- description: API for fetching, uploading, organizing, and distributing Ansible Collections through Red Hat Automation Hub, providing access to Red Hat Certified and partner content.
  name: Red Hat Automation Hub API
  slug: red-hat-automation-hub-api
- description: API providing gathering conditions to the Insights Operator, defining what data should be collected from OpenShift clusters for analysis and recommendations.
  name: Red Hat Operator Gathering Conditions Service API
  slug: red-hat-operator-gathering-conditions-service-api
- description: API for ingesting payloads and data uploads from registered systems into the Hybrid Cloud Console platform for processing by downstream services.
  name: Red Hat Payload Ingress Service API
  slug: red-hat-payload-ingress-service-api
- description: Aggregation API for Insights Advisor that exposes recommendations for single and multiple OpenShift clusters, providing AI-powered operational guidance.
  name: Red Hat Lightspeed Advisor for OpenShift API
  slug: red-hat-lightspeed-advisor-for-openshift-api
- description: API for tracking and analyzing vulnerabilities affecting OpenShift Container Platform clusters, providing CVE exposure data and remediation status.
  name: Red Hat OCP Vulnerability Dashboard API
  slug: red-hat-ocp-vulnerability-dashboard-api
- description: API for the Web Root Cause Analysis service, providing incident tracking, root cause analysis, and post-incident review capabilities for OpenShift managed services.
  name: Red Hat Web-RCA Service API
  slug: red-hat-web-rca-service-api
- description: API for managing support cases through the Red Hat Customer Portal, supporting case creation, updates, comments, attachments, and escalation workflows.
  name: Red Hat Case Management API
  slug: red-hat-case-management-api
- description: Public API for querying Red Hat security data including CVE details, CSAF advisories, OVAL data, and vulnerability severity scores across Red Hat products.
  name: Red Hat Security Data API
  slug: red-hat-security-data-api
- description: API for fleet edge management capabilities including device provisioning, image management, update orchestration, and fleet-level configuration of RHEL-based edge devices.
  name: Red Hat Edge Management API
  slug: red-hat-edge-management-api
- description: API providing RHEL product lifecycle data including release dates, end-of-life schedules, and upgrade path planning information.
  name: Red Hat Lightspeed for RHEL Planning API
  slug: red-hat-lightspeed-for-rhel-planning-api
- description: Operations for managing cluster add-ons that extend OpenShift cluster functionality.
  name: Red Hat Add-Ons API
  slug: red-hat-add-ons-api
- description: Operations for managing client applications registered in a realm for authentication and authorization.
  name: Red Hat Clients API
  slug: red-hat-clients-api
- description: Operations for listing available cloud providers and their regions for cluster deployment.
  name: Red Hat Cloud Providers API
  slug: red-hat-cloud-providers-api
- description: Operations for provisioning, managing, and retrieving OpenShift clusters across cloud providers.
  name: Red Hat Clusters API
  slug: red-hat-clusters-api
- description: Operations for managing content views that define curated snapshots of software repositories for controlled content delivery.
  name: Red Hat Content Views API
  slug: red-hat-content-views-api
- description: Operations for managing credentials used by automation jobs to authenticate with managed hosts and external services.
  name: Red Hat Credentials API
  slug: red-hat-credentials-api
- description: Operations for managing lifecycle environments that define the promotion path for content from development to production.
  name: Red Hat Environments API
  slug: red-hat-environments-api
- description: Operations for listing and managing errata (security advisories, bug fixes, and enhancements) applicable to registered hosts.
  name: Red Hat Errata API
  slug: red-hat-errata-api
- description: Operations for managing user groups that enable bulk role and attribute assignment.
  name: Red Hat Groups API
  slug: red-hat-groups-api
- description: Operations for managing host groups that provide shared configuration templates for provisioning and management.
  name: Red Hat Host Groups API
  slug: red-hat-host-groups-api
- description: Operations for managing hosts registered with Satellite, including provisioning, facts, and power management.
  name: Red Hat Hosts API
  slug: red-hat-hosts-api
- description: Operations for managing external identity providers for federated authentication such as SAML and OIDC.
  name: Red Hat Identity Providers API
  slug: red-hat-identity-providers-api
- description: Operations for managing inventories that define collections of hosts and groups for automation targeting.
  name: Red Hat Inventories API
  slug: red-hat-inventories-api
- description: Operations for managing job templates that define parameterized playbook runs against inventories of managed hosts.
  name: Red Hat Job Templates API
  slug: red-hat-job-templates-api
- description: Operations for launching, monitoring, and managing automation job executions and their output.
  name: Red Hat Jobs API
  slug: red-hat-jobs-api
- description: Operations for managing machine pools that define groups of compute nodes within a cluster.
  name: Red Hat Machine Pools API
  slug: red-hat-machine-pools-api
- description: Operations for retrieving manifest information and security scan results for container images.
  name: Red Hat Manifests API
  slug: red-hat-manifests-api
- description: Operations for managing organizations that provide multi-tenancy and access control boundaries.
  name: Red Hat Organizations API
  slug: red-hat-organizations-api
- description: Operations for managing projects that represent collections of Ansible playbooks sourced from version control.
  name: Red Hat Projects API
  slug: red-hat-projects-api
- description: Operations for managing Keycloak realms that serve as tenants for isolating identity configurations.
  name: Red Hat Realms API
  slug: red-hat-realms-api
- description: Operations for managing container image repositories, including creation, listing, and deletion.
  name: Red Hat Repositories API
  slug: red-hat-repositories-api
- description: The Repository API from Red Hat — 2 operation(s) for repository.
  name: Red Hat Repository API
  slug: red-hat-repository-api
- description: Operations for managing robot accounts that provide automated access to repositories.
  name: Red Hat Robot Accounts API
  slug: red-hat-robot-accounts-api
- description: Operations for managing realm-level and client-level roles for authorization.
  name: Red Hat Roles API
  slug: red-hat-roles-api
- description: Operations for listing and retrieving Advisor rules that define the detection logic for system issues.
  name: Red Hat Rules API
  slug: red-hat-rules-api
- description: Operations for viewing and managing active user sessions across a realm.
  name: Red Hat Sessions API
  slug: red-hat-sessions-api
- description: Operations for retrieving aggregate statistics about system health and recommendation coverage.
  name: Red Hat Stats API
  slug: red-hat-stats-api
- description: Operations for managing OpenShift cluster subscriptions and entitlements.
  name: Red Hat Subscriptions API
  slug: red-hat-subscriptions-api
- description: Operations for retrieving registered systems and their Insights status.
  name: Red Hat Systems API
  slug: red-hat-systems-api
- description: Operations for managing teams within organizations and their repository permissions.
  name: Red Hat Teams API
  slug: red-hat-teams-api
- description: Operations for retrieving curated topics that group related recommendations by technology area or risk category.
  name: Red Hat Topics API
  slug: red-hat-topics-api
- description: Operations for managing user accounts, credentials, and profile attributes within a realm.
  name: Red Hat Users API
  slug: red-hat-users-api
- description: Operations for listing available OpenShift versions for cluster provisioning and upgrades.
  name: Red Hat Versions API
  slug: red-hat-versions-api
- description: Operations for managing workflow job templates that chain multiple job templates into orchestrated automation workflows.
  name: Red Hat Workflow Job Templates API
  slug: red-hat-workflow-job-templates-api
arazzos:
- description: Resolve an organization, create an inventory, build a job template on it, and launch a first run.
  name: Red Hat Ansible Automation Platform Build Inventory and Template
  slug: red-hat-aap-build-inventory-and-template-workflow
- description: Launch an existing job template, poll its job, and cancel it if it stalls.
  name: Red Hat Ansible Automation Platform Launch, Monitor, and Cancel Job
  slug: red-hat-aap-launch-monitor-cancel-job-workflow
- description: Create a job template, launch it, and poll the resulting job to completion.
  name: Red Hat Ansible Automation Platform Provision and Run Job
  slug: red-hat-aap-provision-and-run-job-workflow
- description: Pull fleet statistics, find a system by display name, and retrieve its detail.
  name: Red Hat Insights Inspect a System
  slug: red-hat-insights-inspect-system-workflow
- description: Find a high-risk advisor rule, list the systems it affects, and inspect the first one.
  name: Red Hat Insights Triage a Rule's Affected Systems
  slug: red-hat-insights-rule-affected-systems-workflow
- description: Confirm a realm exists, create a realm role, then create a user in that realm.
  name: Red Hat Keycloak Provision Realm Role and User
  slug: red-hat-keycloak-provision-role-and-user-workflow
- description: Look up a user by username and update it if it exists, otherwise create it.
  name: Red Hat Keycloak Upsert a Realm User
  slug: red-hat-keycloak-upsert-user-workflow
- description: Find a cluster by name, confirm it is ready, then attach an identity provider.
  name: Red Hat OpenShift Configure Cluster Identity Provider
  slug: red-hat-openshift-configure-cluster-identity-workflow
- description: Pick a version and cloud provider, create a cluster, poll until ready, then add a machine pool.
  name: Red Hat OpenShift Provision Cluster and Add Machine Pool
  slug: red-hat-openshift-provision-cluster-workflow
- description: Read a repository, list its tags, and pull the security report for the latest tag's manifest.
  name: Red Hat Quay Audit Repository Tags
  slug: red-hat-quay-audit-repository-tags-workflow
- description: Create a Quay repository, point a tag at a manifest, then poll its security scan.
  name: Red Hat Quay Create Repository, Tag Image, and Scan
  slug: red-hat-quay-create-repo-tag-and-scan-workflow
- description: Confirm an organization, create a robot account for it, then create a repository.
  name: Red Hat Quay Provision Organization Robot and Repository
  slug: red-hat-quay-provision-org-robot-repo-workflow
- description: Resolve an organization, select repositories, and create a content view from them.
  name: Red Hat Satellite Create Content View
  slug: red-hat-satellite-create-content-view-workflow
- description: Find a host, review its applicable errata, and update its content view assignment.
  name: Red Hat Satellite Host Errata Remediation
  slug: red-hat-satellite-host-errata-remediation-workflow
artifact_total: 281
asyncapis:
- description: The Red Hat Streams for Apache Kafka Bridge provides an HTTP-based interface for producing and consuming messages to and from Apache Kafka topics without requiring a native Kafka client. Deployed on O
  name: Red Hat Streams for Apache Kafka Bridge Events
  slug: red-hat-kafka-bridge-asyncapi
- description: The Red Hat Hybrid Cloud Console notifications service delivers event-driven notifications when significant events occur across Insights services, including advisor recommendations, vulnerability aler
  name: Red Hat Hybrid Cloud Console Notifications Events
  slug: red-hat-notifications-webhooks-asyncapi
collections:
- collection_type: postman
  name: Red Hat Ansible Automation Platform API
  slug: postman-red-hat-ansible-automation-platform
- collection_type: postman
  name: Red Hat Insights API
  slug: postman-red-hat-insights
- collection_type: postman
  name: Red Hat Build of Keycloak Admin REST API
  slug: postman-red-hat-keycloak-admin
- collection_type: postman
  name: Red Hat OpenShift Cluster Manager API
  slug: postman-red-hat-openshift-cluster-manager
- collection_type: postman
  name: Red Hat Quay API
  slug: postman-red-hat-quay
- collection_type: postman
  name: Red Hat Satellite API
  slug: postman-red-hat-satellite
- collection_type: open
  name: Red Hat Ansible Automation Platform API
  slug: open-red-hat-ansible-automation-platform
- collection_type: open
  name: Red Hat Insights API
  slug: open-red-hat-insights
- collection_type: open
  name: Red Hat Build of Keycloak Admin REST API
  slug: open-red-hat-keycloak-admin
- collection_type: open
  name: Red Hat OpenShift Cluster Manager API
  slug: open-red-hat-openshift-cluster-manager
- collection_type: open
  name: Red Hat Quay API
  slug: open-red-hat-quay
- collection_type: open
  name: Red Hat Satellite API
  slug: open-red-hat-satellite
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/red-hat-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/red-hat-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/red-hat-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/red-hat-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/red-hat-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/red-hat-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/red-hat-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/red-hat-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/red-hat-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/red-hat-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/red-hat-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/red-hat-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/red-hat-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/red-hat-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/red-hat-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/red-hat-cli.yml
- group: design
  title: ''
  type: Components
  url: components/red-hat-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/red-hat-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/red-hat-sandbox.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/red-hat-openshift-cluster-manager-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/red-hat-ansible-automation-platform-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/red-hat-keycloak-admin-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/red-hat-insights-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/red-hat-quay-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/red-hat-satellite-overlay.yaml
- group: agent
  title: ''
  type: AgentSkills
  url: https://www.redhat.com/en/blog/empower-your-ai-tools-new-agent-skills-red-hat-enterprise-linux
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/red-hat/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/red-hat-aap-build-inventory-and-template-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/red-hat-aap-launch-monitor-cancel-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/red-hat-aap-provision-and-run-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/red-hat-insights-inspect-system-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/red-hat-insights-rule-affected-systems-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/red-hat-keycloak-provision-role-and-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/red-hat-keycloak-upsert-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/red-hat-openshift-configure-cluster-identity-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/red-hat-openshift-provision-cluster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/red-hat-quay-audit-repository-tags-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/red-hat-quay-create-repo-tag-and-scan-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/red-hat-quay-provision-org-robot-repo-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/red-hat-satellite-create-content-view-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/red-hat-satellite-host-errata-remediation-workflow.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/red-hat-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/red-hat-openshift-cluster-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/red-hat-ansible-job-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/red-hat-insights-advisory-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/red-hat-quay-repository-schema.json
- group: start
  title: ''
  type: Portal
  url: https://developers.redhat.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.redhat.com/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.redhat.com/en/products
- group: company
  title: ''
  type: Blog
  url: https://developers.redhat.com/blog
- group: operate
  title: ''
  type: Support
  url: https://access.redhat.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.redhat.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.redhat.com/en/about/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.redhat.com/en/about/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: https://access.redhat.com/articles/3626371
- group: start
  title: ''
  type: Console
  url: https://console.redhat.com
- group: company
  title: ''
  type: Website
  url: https://www.redhat.com
- group: start
  title: ''
  type: Signup
  url: https://developers.redhat.com/register
- group: start
  title: ''
  type: Login
  url: https://sso.redhat.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/redhatofficial
- group: build
  title: ''
  type: SDKs
  url: https://github.com/openshift/client-go
- group: build
  title: ''
  type: CLI
  url: https://docs.openshift.com/container-platform/latest/cli_reference/openshift_cli/getting-started-cli.html
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/redhat-developer
- group: operate
  title: ''
  type: Community
  url: https://access.redhat.com/discussions
- group: operate
  title: ''
  type: StackOverflow
  url: https://developers.redhat.com/stack-overflow
- group: learn
  title: ''
  type: YouTube
  url: https://developers.redhat.com/videos
- group: auth
  title: ''
  type: Security
  url: https://access.redhat.com/security/vulnerabilities
- group: other
  title: ''
  type: API Catalog
  url: https://developers.redhat.com/api-catalog
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://access.redhat.com/knowledgebase
- group: learn
  title: ''
  type: Training
  url: https://www.redhat.com/en/services/training-and-certification
- group: other
  title: ''
  type: Events
  url: https://www.redhat.com/en/events
- group: other
  title: ''
  type: X
  url: https://twitter.com/RedHat
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/red-hat
- group: other
  title: ''
  type: Feed
  url: https://developers.redhat.com/blog/feed
- group: auth
  title: ''
  type: Security Data
  url: https://access.redhat.com/security/data
- group: other
  title: ''
  type: Ecosystem Catalog
  url: https://catalog.redhat.com
- group: design
  title: ''
  type: Product Lifecycle
  url: https://access.redhat.com/product-life-cycles
- group: start
  title: ''
  type: Customer Portal
  url: https://access.redhat.com
created: '2024-01-15'
description: APIs and developer resources from Red Hat, a leading provider of enterprise open source solutions including Linux, cloud, container, and Kubernetes technologies.
examples:
- key_count: 1
  name: Red Hat Ansible Automation Platform Error Example
  slug: red-hat-ansible-automation-platform-error-example
- key_count: 10
  name: Red Hat Ansible Automation Platform Inventory Example
  slug: red-hat-ansible-automation-platform-inventory-example
- key_count: 13
  name: Red Hat Ansible Automation Platform Job Example
  slug: red-hat-ansible-automation-platform-job-example
- key_count: 17
  name: Red Hat Ansible Automation Platform Job Template Example
  slug: red-hat-ansible-automation-platform-job-template-example
- key_count: 4
  name: Red Hat Ansible Automation Platform Paginated Credential List Example
  slug: red-hat-ansible-automation-platform-paginated-credential-list-example
- key_count: 4
  name: Red Hat Ansible Automation Platform Paginated Inventory List Example
  slug: red-hat-ansible-automation-platform-paginated-inventory-list-example
- key_count: 4
  name: Red Hat Ansible Automation Platform Paginated Job List Example
  slug: red-hat-ansible-automation-platform-paginated-job-list-example
- key_count: 4
  name: Red Hat Ansible Automation Platform Paginated Job Template List Example
  slug: red-hat-ansible-automation-platform-paginated-job-template-list-example
- key_count: 4
  name: Red Hat Ansible Automation Platform Paginated List Example
  slug: red-hat-ansible-automation-platform-paginated-list-example
- key_count: 4
  name: Red Hat Ansible Automation Platform Paginated Project List Example
  slug: red-hat-ansible-automation-platform-paginated-project-list-example
- key_count: 1
  name: Red Hat Insights Paginated Rule List Example
  slug: red-hat-insights-paginated-rule-list-example
- key_count: 1
  name: Red Hat Insights Paginated System List Example
  slug: red-hat-insights-paginated-system-list-example
- key_count: 4
  name: Red Hat Insights Pagination Links Example
  slug: red-hat-insights-pagination-links-example
- key_count: 1
  name: Red Hat Insights Pagination Meta Example
  slug: red-hat-insights-pagination-meta-example
- key_count: 12
  name: Red Hat Insights Rule Example
  slug: red-hat-insights-rule-example
- key_count: 3
  name: Red Hat Insights Rule Stats Example
  slug: red-hat-insights-rule-stats-example
- key_count: 10
  name: Red Hat Insights System Example
  slug: red-hat-insights-system-example
- key_count: 3
  name: Red Hat Insights System Stats Example
  slug: red-hat-insights-system-stats-example
- key_count: 6
  name: Red Hat Insights Topic Example
  slug: red-hat-insights-topic-example
- key_count: 12
  name: Red Hat Keycloak Admin Client Example
  slug: red-hat-keycloak-admin-client-example
- key_count: 4
  name: Red Hat Keycloak Admin Group Example
  slug: red-hat-keycloak-admin-group-example
- key_count: 5
  name: Red Hat Keycloak Admin Identity Provider Representation Example
  slug: red-hat-keycloak-admin-identity-provider-representation-example
- key_count: 12
  name: Red Hat Keycloak Admin Realm Example
  slug: red-hat-keycloak-admin-realm-example
- key_count: 5
  name: Red Hat Keycloak Admin Role Example
  slug: red-hat-keycloak-admin-role-example
- key_count: 11
  name: Red Hat Keycloak Admin User Example
  slug: red-hat-keycloak-admin-user-example
- key_count: 5
  name: Red Hat Openshift Cluster Manager Addon List Example
  slug: red-hat-openshift-cluster-manager-addon-list-example
- key_count: 5
  name: Red Hat Openshift Cluster Manager Cloud Provider List Example
  slug: red-hat-openshift-cluster-manager-cloud-provider-list-example
- key_count: 5
  name: Red Hat Openshift Cluster Manager Cloud Region List Example
  slug: red-hat-openshift-cluster-manager-cloud-region-list-example
- key_count: 13
  name: Red Hat Openshift Cluster Manager Cluster Example
  slug: red-hat-openshift-cluster-manager-cluster-example
- key_count: 5
  name: Red Hat Openshift Cluster Manager Cluster List Example
  slug: red-hat-openshift-cluster-manager-cluster-list-example
- key_count: 5
  name: Red Hat Openshift Cluster Manager Error Example
  slug: red-hat-openshift-cluster-manager-error-example
- key_count: 7
  name: Red Hat Openshift Cluster Manager Identity Provider Example
  slug: red-hat-openshift-cluster-manager-identity-provider-example
- key_count: 5
  name: Red Hat Openshift Cluster Manager Identity Provider List Example
  slug: red-hat-openshift-cluster-manager-identity-provider-list-example
- key_count: 7
  name: Red Hat Openshift Cluster Manager Machine Pool Example
  slug: red-hat-openshift-cluster-manager-machine-pool-example
- key_count: 5
  name: Red Hat Openshift Cluster Manager Machine Pool List Example
  slug: red-hat-openshift-cluster-manager-machine-pool-list-example
- key_count: 5
  name: Red Hat Openshift Cluster Manager Subscription List Example
  slug: red-hat-openshift-cluster-manager-subscription-list-example
- key_count: 5
  name: Red Hat Openshift Cluster Manager Version List Example
  slug: red-hat-openshift-cluster-manager-version-list-example
- key_count: 5
  name: Red Hat Quay Organization Example
  slug: red-hat-quay-organization-example
- key_count: 7
  name: Red Hat Quay Repository Example
  slug: red-hat-quay-repository-example
- key_count: 2
  name: Red Hat Quay Repository List Example
  slug: red-hat-quay-repository-list-example
- key_count: 4
  name: Red Hat Quay Robot Account Example
  slug: red-hat-quay-robot-account-example
- key_count: 2
  name: Red Hat Quay Security Scan Result Example
  slug: red-hat-quay-security-scan-result-example
- key_count: 3
  name: Red Hat Quay Tag List Example
  slug: red-hat-quay-tag-list-example
- key_count: 4
  name: Red Hat Quay User Example
  slug: red-hat-quay-user-example
- key_count: 13
  name: Red Hat Satellite Host Example
  slug: red-hat-satellite-host-example
- key_count: 5
  name: Red Hat Satellite Paginated Content View List Example
  slug: red-hat-satellite-paginated-content-view-list-example
- key_count: 5
  name: Red Hat Satellite Paginated Environment List Example
  slug: red-hat-satellite-paginated-environment-list-example
- key_count: 5
  name: Red Hat Satellite Paginated Errata List Example
  slug: red-hat-satellite-paginated-errata-list-example
- key_count: 5
  name: Red Hat Satellite Paginated Host Group List Example
  slug: red-hat-satellite-paginated-host-group-list-example
- key_count: 5
  name: Red Hat Satellite Paginated Host List Example
  slug: red-hat-satellite-paginated-host-list-example
- key_count: 5
  name: Red Hat Satellite Paginated Organization List Example
  slug: red-hat-satellite-paginated-organization-list-example
- key_count: 5
  name: Red Hat Satellite Paginated Repository List Example
  slug: red-hat-satellite-paginated-repository-list-example
finops:
- name: Red Hat Finops
  service_category: Enterprise Software Subscription
  slug: red-hat-finops
image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
json_schemas:
- name: Error
  property_count: 1
  slug: red-hat-ansible-automation-platform-error
- name: Inventory
  property_count: 10
  slug: red-hat-ansible-automation-platform-inventory
- name: Job
  property_count: 13
  slug: red-hat-ansible-automation-platform-job
- name: JobTemplate
  property_count: 17
  slug: red-hat-ansible-automation-platform-job-template
- name: PaginatedCredentialList
  property_count: 4
  slug: red-hat-ansible-automation-platform-paginated-credential-list
- name: PaginatedInventoryList
  property_count: 4
  slug: red-hat-ansible-automation-platform-paginated-inventory-list
- name: PaginatedJobList
  property_count: 4
  slug: red-hat-ansible-automation-platform-paginated-job-list
- name: PaginatedJobTemplateList
  property_count: 4
  slug: red-hat-ansible-automation-platform-paginated-job-template-list
- name: PaginatedList
  property_count: 4
  slug: red-hat-ansible-automation-platform-paginated-list
- name: PaginatedProjectList
  property_count: 4
  slug: red-hat-ansible-automation-platform-paginated-project-list
- name: Red Hat Ansible Automation Platform Job
  property_count: 22
  slug: red-hat-ansible-job
- name: Red Hat Insights Advisory
  property_count: 13
  slug: red-hat-insights-advisory
- name: PaginatedRuleList
  property_count: 1
  slug: red-hat-insights-paginated-rule-list
- name: PaginatedSystemList
  property_count: 1
  slug: red-hat-insights-paginated-system-list
- name: PaginationLinks
  property_count: 4
  slug: red-hat-insights-pagination-links
- name: PaginationMeta
  property_count: 1
  slug: red-hat-insights-pagination-meta
- name: Rule
  property_count: 12
  slug: red-hat-insights-rule
- name: RuleStats
  property_count: 3
  slug: red-hat-insights-rule-stats
- name: System
  property_count: 10
  slug: red-hat-insights-system
- name: SystemStats
  property_count: 3
  slug: red-hat-insights-system-stats
- name: Topic
  property_count: 6
  slug: red-hat-insights-topic
- name: Client
  property_count: 12
  slug: red-hat-keycloak-admin-client
- name: Group
  property_count: 4
  slug: red-hat-keycloak-admin-group
- name: IdentityProviderRepresentation
  property_count: 5
  slug: red-hat-keycloak-admin-identity-provider-representation
- name: Realm
  property_count: 12
  slug: red-hat-keycloak-admin-realm
- name: Role
  property_count: 5
  slug: red-hat-keycloak-admin-role
- name: User
  property_count: 11
  slug: red-hat-keycloak-admin-user
- name: AddonList
  property_count: 5
  slug: red-hat-openshift-cluster-manager-addon-list
- name: CloudProviderList
  property_count: 5
  slug: red-hat-openshift-cluster-manager-cloud-provider-list
- name: CloudRegionList
  property_count: 5
  slug: red-hat-openshift-cluster-manager-cloud-region-list
- name: ClusterList
  property_count: 5
  slug: red-hat-openshift-cluster-manager-cluster-list
- name: Cluster
  property_count: 13
  slug: red-hat-openshift-cluster-manager-cluster
- name: Error
  property_count: 5
  slug: red-hat-openshift-cluster-manager-error
- name: IdentityProviderList
  property_count: 5
  slug: red-hat-openshift-cluster-manager-identity-provider-list
- name: IdentityProvider
  property_count: 7
  slug: red-hat-openshift-cluster-manager-identity-provider
- name: MachinePoolList
  property_count: 5
  slug: red-hat-openshift-cluster-manager-machine-pool-list
- name: MachinePool
  property_count: 7
  slug: red-hat-openshift-cluster-manager-machine-pool
- name: SubscriptionList
  property_count: 5
  slug: red-hat-openshift-cluster-manager-subscription-list
- name: VersionList
  property_count: 5
  slug: red-hat-openshift-cluster-manager-version-list
- name: Red Hat OpenShift Cluster
  property_count: 15
  slug: red-hat-openshift-cluster
- name: Organization
  property_count: 5
  slug: red-hat-quay-organization
- name: RepositoryList
  property_count: 2
  slug: red-hat-quay-repository-list
- name: Repository
  property_count: 7
  slug: red-hat-quay-repository
- name: RobotAccount
  property_count: 4
  slug: red-hat-quay-robot-account
- name: SecurityScanResult
  property_count: 2
  slug: red-hat-quay-security-scan-result
- name: TagList
  property_count: 3
  slug: red-hat-quay-tag-list
- name: User
  property_count: 4
  slug: red-hat-quay-user
- name: Host
  property_count: 13
  slug: red-hat-satellite-host
- name: PaginatedContentViewList
  property_count: 5
  slug: red-hat-satellite-paginated-content-view-list
- name: PaginatedEnvironmentList
  property_count: 5
  slug: red-hat-satellite-paginated-environment-list
- name: PaginatedErrataList
  property_count: 5
  slug: red-hat-satellite-paginated-errata-list
- name: PaginatedHostGroupList
  property_count: 5
  slug: red-hat-satellite-paginated-host-group-list
- name: PaginatedHostList
  property_count: 5
  slug: red-hat-satellite-paginated-host-list
- name: PaginatedOrganizationList
  property_count: 5
  slug: red-hat-satellite-paginated-organization-list
- name: PaginatedRepositoryList
  property_count: 5
  slug: red-hat-satellite-paginated-repository-list
json_structures:
- name: Red Hat Ansible Automation Platform Error Structure
  property_count: 1
  slug: red-hat-ansible-automation-platform-error-structure
- name: Red Hat Ansible Automation Platform Inventory Structure
  property_count: 10
  slug: red-hat-ansible-automation-platform-inventory-structure
- name: Red Hat Ansible Automation Platform Job Structure
  property_count: 13
  slug: red-hat-ansible-automation-platform-job-structure
- name: Red Hat Ansible Automation Platform Job Template Structure
  property_count: 17
  slug: red-hat-ansible-automation-platform-job-template-structure
- name: Red Hat Ansible Automation Platform Paginated Credential List Structure
  property_count: 4
  slug: red-hat-ansible-automation-platform-paginated-credential-list-structure
- name: Red Hat Ansible Automation Platform Paginated Inventory List Structure
  property_count: 4
  slug: red-hat-ansible-automation-platform-paginated-inventory-list-structure
- name: Red Hat Ansible Automation Platform Paginated Job List Structure
  property_count: 4
  slug: red-hat-ansible-automation-platform-paginated-job-list-structure
- name: Red Hat Ansible Automation Platform Paginated Job Template List Structure
  property_count: 4
  slug: red-hat-ansible-automation-platform-paginated-job-template-list-structure
- name: Red Hat Ansible Automation Platform Paginated List Structure
  property_count: 4
  slug: red-hat-ansible-automation-platform-paginated-list-structure
- name: Red Hat Ansible Automation Platform Paginated Project List Structure
  property_count: 4
  slug: red-hat-ansible-automation-platform-paginated-project-list-structure
- name: Red Hat Insights Paginated Rule List Structure
  property_count: 1
  slug: red-hat-insights-paginated-rule-list-structure
- name: Red Hat Insights Paginated System List Structure
  property_count: 1
  slug: red-hat-insights-paginated-system-list-structure
- name: Red Hat Insights Pagination Links Structure
  property_count: 4
  slug: red-hat-insights-pagination-links-structure
- name: Red Hat Insights Pagination Meta Structure
  property_count: 1
  slug: red-hat-insights-pagination-meta-structure
- name: Red Hat Insights Rule Stats Structure
  property_count: 3
  slug: red-hat-insights-rule-stats-structure
- name: Red Hat Insights Rule Structure
  property_count: 12
  slug: red-hat-insights-rule-structure
- name: Red Hat Insights System Stats Structure
  property_count: 3
  slug: red-hat-insights-system-stats-structure
- name: Red Hat Insights System Structure
  property_count: 10
  slug: red-hat-insights-system-structure
- name: Red Hat Insights Topic Structure
  property_count: 6
  slug: red-hat-insights-topic-structure
- name: Red Hat Keycloak Admin Client Structure
  property_count: 12
  slug: red-hat-keycloak-admin-client-structure
- name: Red Hat Keycloak Admin Group Structure
  property_count: 4
  slug: red-hat-keycloak-admin-group-structure
- name: Red Hat Keycloak Admin Identity Provider Representation Structure
  property_count: 5
  slug: red-hat-keycloak-admin-identity-provider-representation-structure
- name: Red Hat Keycloak Admin Realm Structure
  property_count: 12
  slug: red-hat-keycloak-admin-realm-structure
- name: Red Hat Keycloak Admin Role Structure
  property_count: 5
  slug: red-hat-keycloak-admin-role-structure
- name: Red Hat Keycloak Admin User Structure
  property_count: 11
  slug: red-hat-keycloak-admin-user-structure
- name: Red Hat Openshift Cluster Manager Addon List Structure
  property_count: 5
  slug: red-hat-openshift-cluster-manager-addon-list-structure
- name: Red Hat Openshift Cluster Manager Cloud Provider List Structure
  property_count: 5
  slug: red-hat-openshift-cluster-manager-cloud-provider-list-structure
- name: Red Hat Openshift Cluster Manager Cloud Region List Structure
  property_count: 5
  slug: red-hat-openshift-cluster-manager-cloud-region-list-structure
- name: Red Hat Openshift Cluster Manager Cluster List Structure
  property_count: 5
  slug: red-hat-openshift-cluster-manager-cluster-list-structure
- name: Red Hat Openshift Cluster Manager Cluster Structure
  property_count: 13
  slug: red-hat-openshift-cluster-manager-cluster-structure
- name: Red Hat Openshift Cluster Manager Error Structure
  property_count: 5
  slug: red-hat-openshift-cluster-manager-error-structure
- name: Red Hat Openshift Cluster Manager Identity Provider List Structure
  property_count: 5
  slug: red-hat-openshift-cluster-manager-identity-provider-list-structure
- name: Red Hat Openshift Cluster Manager Identity Provider Structure
  property_count: 7
  slug: red-hat-openshift-cluster-manager-identity-provider-structure
- name: Red Hat Openshift Cluster Manager Machine Pool List Structure
  property_count: 5
  slug: red-hat-openshift-cluster-manager-machine-pool-list-structure
- name: Red Hat Openshift Cluster Manager Machine Pool Structure
  property_count: 7
  slug: red-hat-openshift-cluster-manager-machine-pool-structure
- name: Red Hat Openshift Cluster Manager Subscription List Structure
  property_count: 5
  slug: red-hat-openshift-cluster-manager-subscription-list-structure
- name: Red Hat Openshift Cluster Manager Version List Structure
  property_count: 5
  slug: red-hat-openshift-cluster-manager-version-list-structure
- name: Red Hat Quay Organization Structure
  property_count: 5
  slug: red-hat-quay-organization-structure
- name: Red Hat Quay Repository List Structure
  property_count: 2
  slug: red-hat-quay-repository-list-structure
- name: Red Hat Quay Repository Structure
  property_count: 7
  slug: red-hat-quay-repository-structure
- name: Red Hat Quay Robot Account Structure
  property_count: 4
  slug: red-hat-quay-robot-account-structure
- name: Red Hat Quay Security Scan Result Structure
  property_count: 2
  slug: red-hat-quay-security-scan-result-structure
- name: Red Hat Quay Tag List Structure
  property_count: 3
  slug: red-hat-quay-tag-list-structure
- name: Red Hat Quay User Structure
  property_count: 4
  slug: red-hat-quay-user-structure
- name: Red Hat Satellite Host Structure
  property_count: 13
  slug: red-hat-satellite-host-structure
- name: Red Hat Satellite Paginated Content View List Structure
  property_count: 5
  slug: red-hat-satellite-paginated-content-view-list-structure
- name: Red Hat Satellite Paginated Environment List Structure
  property_count: 5
  slug: red-hat-satellite-paginated-environment-list-structure
- name: Red Hat Satellite Paginated Errata List Structure
  property_count: 5
  slug: red-hat-satellite-paginated-errata-list-structure
- name: Red Hat Satellite Paginated Host Group List Structure
  property_count: 5
  slug: red-hat-satellite-paginated-host-group-list-structure
- name: Red Hat Satellite Paginated Host List Structure
  property_count: 5
  slug: red-hat-satellite-paginated-host-list-structure
- name: Red Hat Satellite Paginated Organization List Structure
  property_count: 5
  slug: red-hat-satellite-paginated-organization-list-structure
- name: Red Hat Satellite Paginated Repository List Structure
  property_count: 5
  slug: red-hat-satellite-paginated-repository-list-structure
jsonld:
- class_count: 0
  name: Red Hat Ansible Automation Platform Context
  property_count: 0
  slug: red-hat-ansible-automation-platform-context
- class_count: 1
  name: Red Hat Context
  property_count: 55
  slug: red-hat-context
- class_count: 0
  name: Red Hat Insights Context
  property_count: 0
  slug: red-hat-insights-context
- class_count: 0
  name: Red Hat Keycloak Admin Context
  property_count: 0
  slug: red-hat-keycloak-admin-context
- class_count: 0
  name: Red Hat Openshift Cluster Manager Context
  property_count: 0
  slug: red-hat-openshift-cluster-manager-context
- class_count: 0
  name: Red Hat Quay Context
  property_count: 0
  slug: red-hat-quay-context
- class_count: 0
  name: Red Hat Satellite Context
  property_count: 0
  slug: red-hat-satellite-context
layout: provider
mcp_servers:
- description: ''
  name: red-hat-mcp.yml
  slug: red-hat-mcpyml
modified: '2026-06-20'
name: Red Hat
nav: Providers
network: true
overview: 'Red Hat publishes 36 APIs on the [APIs.io](https://apis.io/) network, including Streams for Apache Kafka Bridge API, Notifications API, Add-Ons API, and 33 more. Tagged areas include Cloud, Containers, Enterprise, Hybrid Cloud, and Kubernetes.


  The Red Hat catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 7 JSON-LD contexts, and 3 Spectral governance rulesets.


  Red Hat''s developer surface includes authentication, changelog, CLI, sandbox, developer portal, getting-started guide, documentation, and 71 more developer resources.'
plans:
- name: Red Hat Plans Pricing
  plan_count: 1
  slug: red-hat-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 1
  name: Red Hat Rate Limits
  slug: red-hat-rate-limits
rules:
- name: Red Hat API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: red-hat-asyncapi-spectral-rules
- name: Red Hat API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: red-hat-jsonschema-spectral-rules
- name: Red Hat API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 8
  slug: red-hat-spectral-rules
score:
  band: exemplar
  composite: 69.9
  delta: -0.3
  facets:
    commercial_clarity: 71.1
    contract_quality: 75.5
    developer_ergonomics: 78.3
    discoverability: 59.3
    governance: 53.1
    operational_transparency: 68.4
  previous_composite: 70.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 34
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/red-hat/refs/heads/main/screenshots/red-hat-2026-06-20T192716.png
security:
- kind: authentication
  name: Red Hat Authentication
  slug: red-hat-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Red Hat Domain Security
  slug: red-hat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Red Hat Vulnerability Disclosure
  slug: red-hat-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Red Hat Trust Center
  slug: red-hat-trust-center
  summary_line: SOC 2 Type 2, SOC 3, ISO 27001, ISO 27017, ISO 27018, PCI DSS 4.0, FIPS 140-2, FIPS 140-3, Common Criteria, FedRAMP High
slug: red-hat
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
website: https://www.redhat.com
---
