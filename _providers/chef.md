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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Chef Agentic Access
  operation_count: 22
  slug: chef-agentic-access
  summary_line: 22 operations · 6 acting
api_count: 14
apis:
- description: InSpec is an open-source language and runner for security and compliance testing. It is consumed via the InSpec CLI and Ruby DSL, and surfaced inside Chef Automate as compliance profiles, scan jobs, a
  name: Chef InSpec
  slug: chef-inspec
- description: The Channels API from Chef — 1 operation(s) for channels.
  name: Chef Channels API
  slug: chef-channels-api
- description: The Clients API from Chef — 1 operation(s) for clients.
  name: Chef Clients API
  slug: chef-clients-api
- description: The Cookbooks API from Chef — 2 operation(s) for cookbooks.
  name: Chef Cookbooks API
  slug: chef-cookbooks-api
- description: The Data Bags API from Chef — 1 operation(s) for data bags.
  name: Chef Data Bags API
  slug: chef-data-bags-api
- description: The Environments API from Chef — 1 operation(s) for environments.
  name: Chef Environments API
  slug: chef-environments-api
- description: The IAM API from Chef — 1 operation(s) for iam.
  name: Chef IAM API
  slug: chef-iam-api
- description: The Nodes API from Chef — 3 operation(s) for nodes.
  name: Chef Nodes API
  slug: chef-nodes-api
- description: The Packages API from Chef — 2 operation(s) for packages.
  name: Chef Packages API
  slug: chef-packages-api
- description: The Profiles API from Chef — 1 operation(s) for profiles.
  name: Chef Profiles API
  slug: chef-profiles-api
- description: The Reports API from Chef — 1 operation(s) for reports.
  name: Chef Reports API
  slug: chef-reports-api
- description: The Roles API from Chef — 2 operation(s) for roles.
  name: Chef Roles API
  slug: chef-roles-api
- description: The Scans API from Chef — 1 operation(s) for scans.
  name: Chef Scans API
  slug: chef-scans-api
- description: The Users API from Chef — 1 operation(s) for users.
  name: Chef Users API
  slug: chef-users-api
arazzos:
- description: Enumerate Infra Server clients and users alongside Automate IAM users for one access review.
  name: Chef Review Access Across Infra Server and Automate
  slug: chef-access-review-workflow
- description: Resolve profiles and nodes, launch a scan job, then search reporting for the results.
  name: Chef Automate Run a Compliance Scan and Retrieve Reports
  slug: chef-compliance-scan-workflow
- description: List an origin's packages, resolve one package's releases, and map the origin's promotion channels.
  name: Chef Habitat Audit an Origin's Package Releases and Channels
  slug: chef-habitat-package-release-audit-workflow
- description: Walk nodes, cookbooks, roles, environments, and data bags to build one organization snapshot.
  name: Chef Snapshot an Infra Server Organization Inventory
  slug: chef-infra-inventory-snapshot-workflow
- description: Capture a node's final state, delete the node object, and confirm it left the inventory.
  name: Chef Decommission a Node
  slug: chef-node-decommission-workflow
- description: Check whether a node already exists, create it if it does not, and read it back.
  name: Chef Register a Node on the Infra Server
  slug: chef-node-registration-workflow
- description: Confirm a cookbook exists, read the node, append the recipe to its run list, and verify.
  name: Chef Add a Cookbook to a Node Run List
  slug: chef-node-runlist-update-workflow
- description: Create a role, read it back, then place it in a node's run list.
  name: Chef Define a Role and Assign It to a Node
  slug: chef-role-assignment-workflow
artifact_total: 66
collections:
- collection_type: postman
  name: Chef Automate Channels API
  slug: postman-chef-channels-api
- collection_type: postman
  name: Chef Automate Channels Clients API
  slug: postman-chef-clients-api
- collection_type: postman
  name: Chef Automate Channels Cookbooks API
  slug: postman-chef-cookbooks-api
- collection_type: postman
  name: Chef Automate Channels Data Bags API
  slug: postman-chef-data-bags-api
- collection_type: postman
  name: Chef Automate Channels Environments API
  slug: postman-chef-environments-api
- collection_type: postman
  name: Chef Automate Channels IAM API
  slug: postman-chef-iam-api
- collection_type: postman
  name: Chef Automate Channels Nodes API
  slug: postman-chef-nodes-api
- collection_type: postman
  name: Chef Automate Channels Packages API
  slug: postman-chef-packages-api
- collection_type: postman
  name: Chef Automate Channels Profiles API
  slug: postman-chef-profiles-api
- collection_type: postman
  name: Chef Automate Channels Reports API
  slug: postman-chef-reports-api
- collection_type: postman
  name: Chef Automate Channels Roles API
  slug: postman-chef-roles-api
- collection_type: postman
  name: Chef Automate Channels Scans API
  slug: postman-chef-scans-api
- collection_type: postman
  name: Chef Automate Channels Users API
  slug: postman-chef-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Chef Automate API
  slug: open-chef-automate-api
- collection_type: open
  name: Chef Automate Channels API
  slug: open-chef-channels-api
- collection_type: open
  name: Chef Automate Channels Clients API
  slug: open-chef-clients-api
- collection_type: open
  name: Chef Automate Channels Cookbooks API
  slug: open-chef-cookbooks-api
- collection_type: open
  name: Chef Automate Channels Data Bags API
  slug: open-chef-data-bags-api
- collection_type: open
  name: Chef Automate Channels Environments API
  slug: open-chef-environments-api
- collection_type: open
  name: Chef Habitat Builder API
  slug: open-chef-habitat-builder-api
- collection_type: open
  name: Chef Automate Channels IAM API
  slug: open-chef-iam-api
- collection_type: open
  name: Chef Infra Server API
  slug: open-chef-infra-server-api
- collection_type: open
  name: Chef Automate Channels Nodes API
  slug: open-chef-nodes-api
- collection_type: open
  name: Chef Automate Channels Packages API
  slug: open-chef-packages-api
- collection_type: open
  name: Chef Automate Channels Profiles API
  slug: open-chef-profiles-api
- collection_type: open
  name: Chef Automate Channels Reports API
  slug: open-chef-reports-api
- collection_type: open
  name: Chef Automate Channels Roles API
  slug: open-chef-roles-api
- collection_type: open
  name: Chef Automate Channels Scans API
  slug: open-chef-scans-api
- collection_type: open
  name: Chef Automate Channels Users API
  slug: open-chef-users-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/chef-automate-api-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/chef/overview
- group: build
  title: ''
  type: Packages
  url: packages/chef-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/chef-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/chef-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/chef-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chef-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/chef-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chef-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/chef-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/chef-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/chef-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chef-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/chef-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/chef-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chef-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chef-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chef-software
- group: company
  title: ''
  type: Website
  url: https://www.chef.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chef.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.chef.io/
- group: company
  title: ''
  type: Blog
  url: https://www.chef.io/blog
- group: build
  title: ''
  type: GitHub
  url: https://github.com/chef
- group: operate
  title: ''
  type: Support
  url: https://www.chef.io/support
- group: learn
  title: ''
  type: Training
  url: https://training.chef.io/
- group: operate
  title: ''
  type: Community
  url: https://community.chef.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chef.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chef.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chef.io/privacy-policy
- group: design
  title: ''
  type: JSONLD
  url: json-ld/chef-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/chef-node-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/chef-role-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/chef-compliance-profile-schema.json
- group: design
  title: ''
  type: Spectral
  url: spectral/chef-spectral.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/chef-node-registration-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/chef-node-runlist-update-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/chef-role-assignment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/chef-node-decommission-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/chef-compliance-scan-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/chef-habitat-package-release-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/chef-infra-inventory-snapshot-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/chef-access-review-workflow.yml
created: '2024-01-15'
description: Chef (Progress Chef) provides infrastructure automation, compliance, and application delivery tooling. Chef exposes REST APIs for the Infra Server (managing nodes, cookbooks, roles, environments, and data bags), Chef Automate (visibility into convergence, compliance, and deployment), Habitat Builder (application packaging and delivery), and InSpec (a language and runner for security and compliance testing).
finops:
- name: Chef Finops
  service_category: API
  slug: chef-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chef.png
json_schemas:
- name: Chef Compliance Profile
  property_count: 7
  slug: chef-compliance-profile
- name: Chef Node
  property_count: 7
  slug: chef-node
- name: Chef Role
  property_count: 5
  slug: chef-role
jsonld:
- class_count: 0
  name: Chef Context
  property_count: 7
  slug: chef-context
layout: provider
mcp_servers:
- description: ''
  name: chef-mcp.yml
  slug: chef-mcpyml
modified: '2026-06-20'
name: Chef
nav: Providers
network: true
overview: 'Chef publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Channels API, Clients API, Cookbooks API, and 10 more. Tagged areas include Application Delivery, Automation, Compliance, Configuration Management, and DevOps.


  The Chef catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Chef''s developer surface includes CLI, changelog, authentication, documentation, getting-started guide, engineering blog, GitHub presence, and 35 more developer resources.'
plans:
- name: Chef Plans Pricing
  plan_count: 3
  slug: chef-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Chef Rate Limits
  slug: chef-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Chef API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: chef-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.2
  delta: -4.9
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 26.5
    contract_quality: 54.4
    developer_ergonomics: 52.4
    discoverability: 72.2
    governance: 26.5
    operational_transparency: 44.7
  previous_composite: 54.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chef/refs/heads/main/screenshots/chef-2026-06-20T174250.png
security:
- kind: authentication
  name: Chef Authentication
  slug: chef-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Chef Domain Security
  slug: chef-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Chef Vulnerability Disclosure
  slug: chef-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Chef Trust Center
  slug: chef-trust-center
  summary_line: HIPAA
slug: chef
tags:
- Application Delivery
- Automation
- Compliance
- Configuration Management
- DevOps
- DevSecOps
- Habitat
- Infrastructure as Code
- InSpec
website: https://www.chef.io/
---
