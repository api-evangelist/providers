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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Red Hat Satellite Agentic Access
  operation_count: 22
  slug: red-hat-satellite-agentic-access
  summary_line: 22 operations · 13 acting
api_count: 9
apis:
- description: Command-line interface tool for Red Hat Satellite that provides scriptable access to Satellite functions including host management, content views, and provisioning.
  name: Red Hat Satellite Hammer CLI
  slug: red-hat-satellite-hammer-cli
- description: Core Foreman API integrated into Red Hat Satellite for host lifecycle management, provisioning, and configuration management. This is the upstream project API that powers Satellite's core functionalit
  name: Red Hat Satellite Foreman API
  slug: red-hat-satellite-foreman-api
- description: Content management API for Red Hat Satellite handling repositories, content views, lifecycle environments, subscriptions, and errata. Katello is the upstream plugin that provides Satellite's content a
  name: Red Hat Satellite Katello API
  slug: red-hat-satellite-katello-api
- description: The redhat.satellite Ansible collection provides modules, roles, and plugins for automating Red Hat Satellite configuration and management through the Satellite API. Based on the theforeman.foreman co
  name: Red Hat Satellite Ansible Collection
  slug: red-hat-satellite-ansible-collection
- description: Manage content views which define curated sets of repositories and packages available to hosts.
  name: Red Hat Satellite Content Views API
  slug: red-hat-satellite-content-views-api
- description: Manage hosts registered with Red Hat Satellite including physical, virtual, and cloud instances.
  name: Red Hat Satellite Hosts API
  slug: red-hat-satellite-hosts-api
- description: Manage lifecycle environments that define promotion paths for content views from development through production.
  name: Red Hat Satellite Lifecycle Environments API
  slug: red-hat-satellite-lifecycle-environments-api
- description: Manage organizations which provide multi-tenancy isolation for hosts, content, and subscriptions.
  name: Red Hat Satellite Organizations API
  slug: red-hat-satellite-organizations-api
- description: Manage Red Hat subscriptions and entitlements for organizations and hosts.
  name: Red Hat Satellite Subscriptions API
  slug: red-hat-satellite-subscriptions-api
artifact_total: 108
collections:
- collection_type: open
  name: Red Hat Satellite REST API
  slug: open-red-hat-satellite-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/red-hat-satellite-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/red-hat-satellite-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/red-hat-satellite-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/red-hat-satellite-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/red-hat-satellite-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/red-hat-satellite-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://access.redhat.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.redhat.com/en/documentation/red_hat_satellite/6.16
- group: operate
  title: ''
  type: Support
  url: https://access.redhat.com/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.redhat.com/
- group: company
  title: ''
  type: Blog
  url: https://www.redhat.com/en/blog/channel/red-hat-satellite
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/theforeman
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://access.redhat.com/solutions/
- group: operate
  title: Community
  type: Support
  url: https://access.redhat.com/community/
- group: operate
  title: Foreman Community
  type: Support
  url: https://community.theforeman.org/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.redhat.com/en/documentation/red_hat_satellite/6.18/html-single/release_notes/index
- group: docs
  title: Product Lifecycle
  type: Documentation
  url: https://access.redhat.com/support/policy/updates/satellite
- group: docs
  title: Release Dates
  type: Documentation
  url: https://access.redhat.com/articles/1365633
- group: docs
  title: Provisioning Guide
  type: Documentation
  url: https://docs.redhat.com/en/documentation/red_hat_satellite/6.16/html/provisioning_hosts/index
- group: docs
  title: Managing Hosts Guide
  type: Documentation
  url: https://docs.redhat.com/en/documentation/red_hat_satellite/6.16/html-single/managing_content/index
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.theforeman.org/
- group: build
  title: Hammer CLI
  type: CLI
  url: https://github.com/theforeman/hammer-cli-foreman
- group: build
  title: Ansible Modules
  type: GitHubRepository
  url: https://github.com/theforeman/foreman-ansible-modules
- group: design
  title: ''
  type: SpectralRules
  url: rules/red-hat-satellite-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/red-hat-satellite-vocabulary.yaml
created: '2024-01-01'
description: Red Hat Satellite is a systems management product that helps deploy, configure, and maintain systems across physical, virtual, and cloud environments.
examples:
- key_count: 12
  name: Red Hat Satellite Content View Create Example
  slug: red-hat-satellite-content-view-create-example
- key_count: 25
  name: Red Hat Satellite Content View Example
  slug: red-hat-satellite-content-view-example
- key_count: 7
  name: Red Hat Satellite Content View Update Example
  slug: red-hat-satellite-content-view-update-example
- key_count: 6
  name: Red Hat Satellite Createcontentview Example
  slug: red-hat-satellite-createcontentview-example
- key_count: 6
  name: Red Hat Satellite Createhost Example
  slug: red-hat-satellite-createhost-example
- key_count: 6
  name: Red Hat Satellite Createlifecycleenvironment Example
  slug: red-hat-satellite-createlifecycleenvironment-example
- key_count: 6
  name: Red Hat Satellite Deletesubscriptionmanifest Example
  slug: red-hat-satellite-deletesubscriptionmanifest-example
- key_count: 11
  name: Red Hat Satellite Foreman Task Example
  slug: red-hat-satellite-foreman-task-example
- key_count: 22
  name: Red Hat Satellite Host Create Example
  slug: red-hat-satellite-host-create-example
- key_count: 47
  name: Red Hat Satellite Host Example
  slug: red-hat-satellite-host-example
- key_count: 23
  name: Red Hat Satellite Host Interface Create Example
  slug: red-hat-satellite-host-interface-create-example
- key_count: 17
  name: Red Hat Satellite Host Interface Example
  slug: red-hat-satellite-host-interface-example
- key_count: 17
  name: Red Hat Satellite Host Update Example
  slug: red-hat-satellite-host-update-example
- key_count: 6
  name: Red Hat Satellite Hostpoweraction Example
  slug: red-hat-satellite-hostpoweraction-example
- key_count: 12
  name: Red Hat Satellite Lifecycle Environment Example
  slug: red-hat-satellite-lifecycle-environment-example
- key_count: 6
  name: Red Hat Satellite Listcontentviews Example
  slug: red-hat-satellite-listcontentviews-example
- key_count: 6
  name: Red Hat Satellite Listhosts Example
  slug: red-hat-satellite-listhosts-example
- key_count: 6
  name: Red Hat Satellite Listlifecycleenvironmentpaths Example
  slug: red-hat-satellite-listlifecycleenvironmentpaths-example
- key_count: 6
  name: Red Hat Satellite Listlifecycleenvironments Example
  slug: red-hat-satellite-listlifecycleenvironments-example
- key_count: 6
  name: Red Hat Satellite Listorganizations Example
  slug: red-hat-satellite-listorganizations-example
- key_count: 6
  name: Red Hat Satellite Listsubscriptions Example
  slug: red-hat-satellite-listsubscriptions-example
- key_count: 7
  name: Red Hat Satellite Organization Example
  slug: red-hat-satellite-organization-example
- key_count: 6
  name: Red Hat Satellite Promotecontentviewversion Example
  slug: red-hat-satellite-promotecontentviewversion-example
- key_count: 6
  name: Red Hat Satellite Publishcontentview Example
  slug: red-hat-satellite-publishcontentview-example
- key_count: 6
  name: Red Hat Satellite Refreshsubscriptionmanifest Example
  slug: red-hat-satellite-refreshsubscriptionmanifest-example
- key_count: 6
  name: Red Hat Satellite Showcontentview Example
  slug: red-hat-satellite-showcontentview-example
- key_count: 6
  name: Red Hat Satellite Showhost Example
  slug: red-hat-satellite-showhost-example
- key_count: 6
  name: Red Hat Satellite Showorganization Example
  slug: red-hat-satellite-showorganization-example
- key_count: 25
  name: Red Hat Satellite Subscription Example
  slug: red-hat-satellite-subscription-example
- key_count: 6
  name: Red Hat Satellite Updatecontentview Example
  slug: red-hat-satellite-updatecontentview-example
- key_count: 6
  name: Red Hat Satellite Updatehost Example
  slug: red-hat-satellite-updatehost-example
- key_count: 6
  name: Red Hat Satellite Uploadsubscriptionmanifest Example
  slug: red-hat-satellite-uploadsubscriptionmanifest-example
features:
- description: Manage physical, virtual, and cloud hosts across the entire lifecycle from provisioning to decommissioning.
  name: Host Management
- description: Curate and distribute RPM packages, errata, and container images through content views and lifecycle environments.
  name: Content Management
- description: Apply security patches and errata across managed systems with controlled rollouts through lifecycle stages.
  name: Patch Management
- description: Track and manage Red Hat subscriptions and entitlements across organizations and hosts.
  name: Subscription Management
- description: Automate bare-metal and virtual machine provisioning with kickstart templates, PXE boot, and compute resources.
  name: Provisioning
- description: Enforce desired-state configuration using Puppet classes and Ansible roles across managed hosts.
  name: Configuration Management
- description: Organize hosts, content, and subscriptions into isolated organizations and locations.
  name: Multi-Tenancy
finops:
- name: Red Hat Satellite Finops
  service_category: System Management
  slug: red-hat-satellite-finops
image: https://www.redhat.com/profiles/rh/themes/redhatdotcom/img/logo.png
integrations:
- description: Automate Satellite operations and host configuration using the redhat.satellite Ansible collection.
  name: Ansible
- description: Proactive risk analysis and remediation recommendations for managed hosts.
  name: Red Hat Insights
- description: Apply and enforce configuration management policies using Puppet modules and classes.
  name: Puppet
- description: Security compliance scanning and reporting using SCAP content and policies.
  name: OpenSCAP
- description: Provision and manage virtual machines on VMware infrastructure as compute resources.
  name: VMware vSphere
- description: Provision and manage instances on OpenStack as compute resources.
  name: Red Hat OpenStack
- description: Provision and manage cloud instances on AWS as compute resources.
  name: Amazon EC2
- description: Provision and manage cloud instances on Google Cloud as compute resources.
  name: Google GCE
json_schemas:
- name: ContentViewCreate
  property_count: 12
  slug: red-hat-satellite-content-view-create
- name: ContentView
  property_count: 25
  slug: red-hat-satellite-content-view
- name: ContentViewUpdate
  property_count: 7
  slug: red-hat-satellite-content-view-update
- name: ContentView
  property_count: 25
  slug: red-hat-satellite-contentview
- name: ContentViewCreate
  property_count: 12
  slug: red-hat-satellite-contentviewcreate
- name: ContentViewUpdate
  property_count: 7
  slug: red-hat-satellite-contentviewupdate
- name: ForemanTask
  property_count: 11
  slug: red-hat-satellite-foreman-task
- name: ForemanTask
  property_count: 11
  slug: red-hat-satellite-foremantask
- name: HostCreate
  property_count: 22
  slug: red-hat-satellite-host-create
- name: HostInterfaceCreate
  property_count: 23
  slug: red-hat-satellite-host-interface-create
- name: HostInterface
  property_count: 17
  slug: red-hat-satellite-host-interface
- name: Host
  property_count: 47
  slug: red-hat-satellite-host
- name: HostUpdate
  property_count: 17
  slug: red-hat-satellite-host-update
- name: HostCreate
  property_count: 22
  slug: red-hat-satellite-hostcreate
- name: HostInterface
  property_count: 17
  slug: red-hat-satellite-hostinterface
- name: HostInterfaceCreate
  property_count: 23
  slug: red-hat-satellite-hostinterfacecreate
- name: HostUpdate
  property_count: 17
  slug: red-hat-satellite-hostupdate
- name: LifecycleEnvironment
  property_count: 12
  slug: red-hat-satellite-lifecycle-environment
- name: LifecycleEnvironment
  property_count: 12
  slug: red-hat-satellite-lifecycleenvironment
- name: Organization
  property_count: 7
  slug: red-hat-satellite-organization
- name: Subscription
  property_count: 25
  slug: red-hat-satellite-subscription
json_structures:
- name: Red Hat Satellite Content View Create Structure
  property_count: 12
  slug: red-hat-satellite-content-view-create-structure
- name: Red Hat Satellite Content View Structure
  property_count: 25
  slug: red-hat-satellite-content-view-structure
- name: Red Hat Satellite Content View Update Structure
  property_count: 7
  slug: red-hat-satellite-content-view-update-structure
- name: Red Hat Satellite Foreman Task Structure
  property_count: 11
  slug: red-hat-satellite-foreman-task-structure
- name: Red Hat Satellite Host Create Structure
  property_count: 22
  slug: red-hat-satellite-host-create-structure
- name: Red Hat Satellite Host Interface Create Structure
  property_count: 23
  slug: red-hat-satellite-host-interface-create-structure
- name: Red Hat Satellite Host Interface Structure
  property_count: 17
  slug: red-hat-satellite-host-interface-structure
- name: Red Hat Satellite Host Structure
  property_count: 47
  slug: red-hat-satellite-host-structure
- name: Red Hat Satellite Host Update Structure
  property_count: 17
  slug: red-hat-satellite-host-update-structure
- name: Red Hat Satellite Lifecycle Environment Structure
  property_count: 12
  slug: red-hat-satellite-lifecycle-environment-structure
- name: Red Hat Satellite Organization Structure
  property_count: 7
  slug: red-hat-satellite-organization-structure
- name: Red Hat Satellite Structure
  property_count: 0
  slug: red-hat-satellite-structure
- name: Red Hat Satellite Subscription Structure
  property_count: 25
  slug: red-hat-satellite-subscription-structure
jsonld:
- class_count: 0
  name: Red Hat Satellite Context
  property_count: 0
  slug: red-hat-satellite-context
layout: provider
modified: '2026-05-19'
name: Red Hat Satellite
nav: Providers
network: true
overview: 'Red Hat Satellite publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Content Views API, Hosts API, Lifecycle Environments API, and 2 more. Tagged areas include Configuration Management, Lifecycle Management, Patch Management, Subscription Management, and Systems Management.


  The Red Hat Satellite catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Red Hat Satellite''s developer surface includes authentication, developer portal, documentation, support, engineering blog, release notes, API reference, and 18 more developer resources.'
plans:
- name: Red Hat Satellite Plans Pricing
  plan_count: 1
  slug: red-hat-satellite-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Red Hat Satellite Rate Limits
  slug: red-hat-satellite-rate-limits
rules:
- name: Red Hat Satellite API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: red-hat-satellite-jsonschema-spectral-rules
- name: Red Hat Satellite API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 8
  slug: red-hat-satellite-spectral-rules
scopes:
- name: Red Hat Satellite Scopes
  scope_count: 0
  slug: red-hat-satellite-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 57.2
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 67.3
    developer_ergonomics: 47.8
    discoverability: 55.0
    governance: 86.8
    operational_transparency: 57.9
  previous_composite: 57.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/red-hat-satellite/refs/heads/main/screenshots/red-hat-satellite-2026-06-20T192721.png
security:
- kind: authentication
  name: Red Hat Satellite Authentication
  slug: red-hat-satellite-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Red Hat Satellite Domain Security
  slug: red-hat-satellite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Red Hat Satellite Vulnerability Disclosure
  slug: red-hat-satellite-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Red Hat Satellite Trust Center
  slug: red-hat-satellite-trust-center
  summary_line: ISO 27001, ISO 27018, HIPAA
slug: red-hat-satellite
tags:
- Configuration Management
- Lifecycle Management
- Patch Management
- Subscription Management
- Systems Management
use_cases:
- description: Provision new servers automatically using compute resources, host groups, and kickstart templates.
  name: Automated Server Provisioning
- description: Identify, test, and deploy security errata across thousands of hosts using content views and promotion workflows.
  name: Security Patching at Scale
- description: Manage hosts across on-premises data centers and cloud providers from a single console.
  name: Hybrid Cloud Management
- description: Generate compliance reports using OpenSCAP integration to verify hosts meet security baselines.
  name: Compliance Reporting
- description: Manage systems in disconnected environments using content synchronization and inter-satellite sync.
  name: Air-Gapped Environment Management
website: https://access.redhat.com/
---
