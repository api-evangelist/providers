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
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Terraform Agentic Access
  operation_count: 48
  slug: terraform-agentic-access
  summary_line: 48 operations · 23 acting
api_count: 2
apis:
- description: Browse and search Terraform modules in the public registry
  name: Terraform Modules API
  slug: terraform-modules-api
- description: Manage HCP Terraform organizations
  name: Terraform Organizations API
  slug: terraform-organizations-api
- description: Manage Sentinel and OPA policies
  name: Terraform Policies API
  slug: terraform-policies-api
- description: Manage projects within organizations
  name: Terraform Projects API
  slug: terraform-projects-api
- description: Manage Terraform runs and plan/apply lifecycle
  name: Terraform Runs API
  slug: terraform-runs-api
- description: Manage workspace state versions
  name: Terraform State Versions API
  slug: terraform-state-versions-api
- description: Manage teams and memberships
  name: Terraform Teams API
  slug: terraform-teams-api
- description: Manage workspace and variable sets
  name: Terraform Variables API
  slug: terraform-variables-api
- description: Manage infrastructure workspaces
  name: Terraform Workspaces API
  slug: terraform-workspaces-api
arazzos:
- description: List everything a namespace publishes, then read the flagship module's versions and download metrics.
  name: Terraform Audit a Namespace's Published Modules
  slug: terraform-audit-namespace-modules-workflow
- description: Sweep an organization for its projects, workspaces, teams, and policies in one pass.
  name: Terraform Audit an Organization's Full Inventory
  slug: terraform-audit-organization-inventory-workflow
- description: Locate an in-flight run on a workspace, cancel it, and unlock the workspace.
  name: Terraform Find and Cancel a Stuck Run
  slug: terraform-cancel-stuck-run-workflow
- description: Queue a destroy run, apply it, then delete the emptied workspace.
  name: Terraform Destroy Infrastructure and Delete the Workspace
  slug: terraform-destroy-workspace-workflow
- description: Search the public registry for a module, read its latest version, and check its versions and download counts.
  name: Terraform Discover a Registry Module and Vet It
  slug: terraform-discover-module-workflow
- description: Lock a workspace, read its current state serial, upload a new state version, and unlock.
  name: Terraform Push a New State Version Under Lock
  slug: terraform-migrate-state-version-workflow
- description: Check whether a policy already exists in an organization, create it if not, and read it back.
  name: Terraform Onboard a Sentinel or OPA Policy
  slug: terraform-onboard-policy-workflow
- description: Create a project in an organization, place a workspace in it, and list the project's workspaces.
  name: Terraform Onboard a Project and Its First Workspace
  slug: terraform-onboard-project-workflow
- description: Check an organization's teams for a name, create the team if missing, and read it back.
  name: Terraform Onboard a Team into an Organization
  slug: terraform-onboard-team-workflow
- description: Compare a module's latest version against the version you intend to pin, then resolve that exact version's download source.
  name: Terraform Pin a Module to a Specific Version and Resolve Its Source
  slug: terraform-pin-module-version-workflow
- description: Queue a run, poll the plan to completion, then confirm or throw it away.
  name: Terraform Plan a Run and Apply or Discard It
  slug: terraform-plan-and-apply-run-workflow
- description: Verify an organization, create a workspace, seed its variables, and read it back.
  name: Terraform Provision a Workspace with Initial Variables
  slug: terraform-provision-workspace-workflow
- description: Set a workspace variable to a value whether or not it already exists.
  name: Terraform Upsert a Workspace Variable
  slug: terraform-upsert-workspace-variable-workflow
artifact_total: 51
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HCP Terraform API
  slug: open-hcp-terraform
- collection_type: open
  name: HCP Terraform Modules API
  slug: open-terraform-modules-api
- collection_type: open
  name: HCP Terraform Modules Organizations API
  slug: open-terraform-organizations-api
- collection_type: open
  name: HCP Terraform Modules Policies API
  slug: open-terraform-policies-api
- collection_type: open
  name: HCP Terraform Modules Projects API
  slug: open-terraform-projects-api
- collection_type: open
  name: Terraform Registry API
  slug: open-terraform-registry
- collection_type: open
  name: HCP Terraform Modules Runs API
  slug: open-terraform-runs-api
- collection_type: open
  name: HCP Terraform Modules State Versions API
  slug: open-terraform-state-versions-api
- collection_type: open
  name: HCP Terraform Modules Teams API
  slug: open-terraform-teams-api
- collection_type: open
  name: HCP Terraform Modules Variables API
  slug: open-terraform-variables-api
- collection_type: open
  name: HCP Terraform Modules Workspaces API
  slug: open-terraform-workspaces-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/terraform-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/terraform-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/terraform-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/terraform-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/terraform-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/terraform-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/terraform-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/terraform-hcp-terraform-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/terraform-terraform-registry-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/terraform-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/terraform-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/terraform-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/terraform-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/terraform-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/terraform-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/terraform-data-model.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/terraform-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/terraform-trust-center.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.hashicorp.com/terraform
- group: other
  title: ''
  type: Repository
  url: https://github.com/hashicorp/terraform
- group: start
  title: ''
  type: Portal
  url: https://registry.terraform.io
- group: start
  title: ''
  type: Portal
  url: https://app.terraform.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/hashicorp/terraform/blob/main/CHANGELOG.md
- group: operate
  title: ''
  type: Forums
  url: https://discuss.hashicorp.com/c/terraform-core
- group: other
  title: ''
  type: Repository
  url: https://github.com/hashicorp/terraform
- group: build
  title: ''
  type: SDKs
  url: https://github.com/hashicorp/terraform-cdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/hashicorp/go-tfe
- group: company
  title: ''
  type: Blog
  url: https://www.hashicorp.com/en/blog
- group: design
  title: ''
  type: Arazzo
  url: arazzo/terraform-provision-workspace-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/terraform-plan-and-apply-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/terraform-destroy-workspace-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/terraform-upsert-workspace-variable-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/terraform-cancel-stuck-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/terraform-migrate-state-version-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/terraform-onboard-project-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/terraform-onboard-policy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/terraform-onboard-team-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/terraform-audit-organization-inventory-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/terraform-discover-module-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/terraform-pin-module-version-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/terraform-audit-namespace-modules-workflow.yml
created: '2026-03-16'
description: HashiCorp Terraform is an open-source infrastructure-as-code tool that enables teams to define, provision, and manage cloud infrastructure using a declarative configuration language (HCL). HCP Terraform and Terraform Enterprise expose a comprehensive REST API for automating workspace management, runs, state, policies, and access control.
examples:
- key_count: 2
  name: Hcp Terraform Create Run Example
  slug: hcp-terraform-create-run-example
- key_count: 2
  name: Hcp Terraform List Workspaces Example
  slug: hcp-terraform-list-workspaces-example
finops:
- name: Terraform Finops
  service_category: API
  slug: terraform-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/terraform.png
json_schemas:
- name: Terraform Run
  property_count: 4
  slug: terraform-run
- name: Terraform Workspace
  property_count: 4
  slug: terraform-workspace
json_structures:
- name: Terraform Workspace Structure
  property_count: 0
  slug: terraform-workspace-structure
jsonld:
- class_count: 33
  name: Terraform Context
  property_count: 0
  slug: terraform-context
layout: provider
mcp_servers:
- description: 'HashiCorp publishes an official open-source Terraform MCP server that exposes the Terraform Registry APIs and HCP Terraform / Terraform Enterprise workspace operations to AI agents. It is self-hosted '
  name: Terraform MCP Server
  slug: terraform-mcp-server
modified: '2026-06-20'
name: Terraform
nav: Providers
network: true
overview: 'Terraform publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Modules API, Organizations API, Policies API, and 6 more. Tagged areas include Infrastructure as Code, Cloud Infrastructure, DevOps, Open-Source, and HashiCorp.


  The Terraform catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Terraform''s developer surface includes authentication, changelog, CLI, developer portal, engineering blog, and 36 more developer resources.'
plans:
- name: Terraform Plans Pricing
  plan_count: 3
  slug: terraform-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Terraform Rate Limits
  slug: terraform-rate-limits
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Terraform API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 8
  slug: hcp-terraform-rules
- effective_rule_count: 5
  extends: []
  name: Terraform API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: terraform-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.0
  coverage:
    artifact_dirs: 29
    catalog_gap: 43.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 59.1
    contract_quality: 64.4
    developer_ergonomics: 52.4
    discoverability: 68.5
    governance: 59.1
    operational_transparency: 28.9
  previous_composite: 49.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/terraform/refs/heads/main/screenshots/terraform-2026-06-20T195132.png
security:
- kind: authentication
  name: Terraform Authentication
  slug: terraform-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Terraform Domain Security
  slug: terraform-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Terraform Vulnerability Disclosure
  slug: terraform-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Terraform Trust Center
  slug: terraform-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, ISO 27017, ISO 27018
slug: terraform
tags:
- Infrastructure as Code
- Cloud Infrastructure
- DevOps
- Open-Source
- HashiCorp
website: https://developer.hashicorp.com/terraform
---
