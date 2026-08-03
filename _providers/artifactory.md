---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 58.1
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 35
  human_in_the_loop: 1
  name: Artifactory Agentic Access
  operation_count: 69
  slug: artifactory-agentic-access
  summary_line: 69 operations · 35 acting · 1 human-in-the-loop
api_count: 17
apis:
- description: Execute AQL queries to search for artifacts, builds, and entries
  name: JFrog Artifactory AQL Search API
  slug: artifactory-aql-search-api
- description: Artifactory-specific Docker API extensions
  name: JFrog Artifactory Artifactory Extensions API
  slug: artifactory-artifactory-extensions-api
- description: Deploy, retrieve, copy, move, and delete artifacts
  name: JFrog Artifactory Artifacts & Storage API
  slug: artifactory-artifacts-storage-api
- description: API version check and health
  name: JFrog Artifactory Base API
  slug: artifactory-base-api
- description: Push and pull image layers (blobs)
  name: JFrog Artifactory Blobs API
  slug: artifactory-blobs-api
- description: Compare build versions
  name: JFrog Artifactory Build Diff API
  slug: artifactory-build-diff-api
- description: Publish and retrieve build information
  name: JFrog Artifactory Build Info API
  slug: artifactory-build-info-api
- description: List, delete, and manage builds
  name: JFrog Artifactory Build Management API
  slug: artifactory-build-management-api
- description: Promote builds between repositories
  name: JFrog Artifactory Build Promotion API
  slug: artifactory-build-promotion-api
- description: List available repositories
  name: JFrog Artifactory Catalog API
  slug: artifactory-catalog-api
- description: Push and pull image manifests
  name: JFrog Artifactory Manifests API
  slug: artifactory-manifests-api
- description: Repository replication configuration and management
  name: JFrog Artifactory Replication API
  slug: artifactory-replication-api
- description: Create, read, update, and delete repositories
  name: JFrog Artifactory Repositories API
  slug: artifactory-repositories-api
- description: Search for artifacts using various criteria
  name: JFrog Artifactory Search API
  slug: artifactory-search-api
- description: Users, groups, permissions, and tokens
  name: JFrog Artifactory Security API
  slug: artifactory-security-api
- description: System health, version, and configuration management
  name: JFrog Artifactory System & Configuration API
  slug: artifactory-system-configuration-api
- description: The Tags API from JFrog Artifactory — 1 operation(s) for tags.
  name: JFrog Artifactory Tags API
  slug: artifactory-tags-api
arazzos:
- description: Run an AQL query to find an artifact, then delete the first match if any.
  name: Artifactory AQL Find and Delete Artifact
  slug: artifactory-aql-find-and-delete-artifact-workflow
- description: Find an artifact by its SHA-256 checksum, then read its storage info.
  name: Artifactory Checksum Search and Retrieve
  slug: artifactory-checksum-search-retrieve-workflow
- description: Confirm a build exists, then diff it against a previous build number.
  name: Artifactory Compare Build Versions
  slug: artifactory-compare-build-versions-workflow
- description: Create a local repository then set up scheduled push replication for it.
  name: Artifactory Configure Repository Replication
  slug: artifactory-configure-repository-replication-workflow
- description: Create a group, then mint an access token scoped to that group for a user.
  name: Artifactory Create Group-Scoped Access Token
  slug: artifactory-create-group-scoped-access-token-workflow
- description: Create a group, create a user in that group, then read the user back to verify.
  name: Artifactory Create User and Verify Membership
  slug: artifactory-create-user-verify-membership-workflow
- description: Read a repository's config, confirm it exists, then delete it.
  name: Artifactory Decommission Repository
  slug: artifactory-decommission-repository-workflow
- description: Deploy an artifact, attach metadata properties to it, then find it by property.
  name: Artifactory Deploy, Tag, and Search Artifact
  slug: artifactory-deploy-tag-search-artifact-workflow
- description: Find a Maven artifact by GAVC coordinates, then set properties on it.
  name: Artifactory GAVC Search and Tag
  slug: artifactory-gavc-search-tag-workflow
- description: List an image's tags, then fetch the manifest for the first tag found.
  name: Artifactory Inspect Docker Image Manifest
  slug: artifactory-inspect-docker-image-manifest-workflow
- description: Move an artifact to a new repository path and verify the destination.
  name: Artifactory Move Artifact and Clean Up
  slug: artifactory-move-artifact-cleanup-workflow
- description: Create a user, create a group, and grant the group repository permissions.
  name: Artifactory Onboard User with Group and Permission
  slug: artifactory-onboard-user-group-permission-workflow
- description: Copy an artifact from a staging repository to a release repository and verify it.
  name: Artifactory Promote Artifact Across Repositories
  slug: artifactory-promote-artifact-across-repositories-workflow
- description: Promote a Docker image to a target repository, then list its tags to verify.
  name: Artifactory Promote Docker Image
  slug: artifactory-promote-docker-image-workflow
- description: Create a local repository, deploy an artifact into it, and verify the deployment.
  name: Artifactory Provision Repository and Deploy Artifact
  slug: artifactory-provision-repository-deploy-artifact-workflow
- description: Publish build info, list the build runs, then apply a retention policy.
  name: Artifactory Publish Build and Set Retention
  slug: artifactory-publish-build-set-retention-workflow
- description: Publish build info to Artifactory and promote the build to a release repository.
  name: Artifactory Publish and Promote Build
  slug: artifactory-publish-promote-build-workflow
- description: Confirm a build exists, rename it, then read the runs under its new name.
  name: Artifactory Rename Build and Verify
  slug: artifactory-rename-build-verify-workflow
artifact_total: 65
collections:
- collection_type: postman
  name: JFrog Artifactory Query Language (AQL) API
  slug: postman-artifactory-aql-api
- collection_type: postman
  name: JFrog Artifactory Docker Registry API
  slug: postman-artifactory-docker-registry-api
- collection_type: postman
  name: JFrog Artifactory REST API
  slug: postman-artifactory-rest-api
- collection_type: open
  name: JFrog Artifactory Query Language (AQL) API
  slug: open-artifactory-aql-api
- collection_type: open
  name: JFrog Artifactory Docker Registry API
  slug: open-artifactory-docker-registry-api
- collection_type: open
  name: JFrog Artifactory REST API
  slug: open-artifactory-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/artifactory-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/artifactory-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/artifactory-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/artifactory-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/artifactory-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/artifactory-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/artifactory-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/artifactory-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/artifactory-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/artifactory-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/artifactory-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/artifactory-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/artifactory-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/artifactory-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/artifactory-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/artifactory-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/artifactory-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/artifactory-rest-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/artifactory-aql-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/artifactory-docker-registry-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/artifactory-build-integration-api-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/jfrog-artifactory/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/artifactory-aql-find-and-delete-artifact-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/artifactory-checksum-search-retrieve-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/artifactory-compare-build-versions-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/artifactory-configure-repository-replication-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/artifactory-create-group-scoped-access-token-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/artifactory-create-user-verify-membership-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/artifactory-decommission-repository-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/artifactory-deploy-tag-search-artifact-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/artifactory-gavc-search-tag-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/artifactory-inspect-docker-image-manifest-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/artifactory-move-artifact-cleanup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/artifactory-onboard-user-group-permission-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/artifactory-promote-artifact-across-repositories-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/artifactory-promote-docker-image-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/artifactory-provision-repository-deploy-artifact-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/artifactory-publish-build-set-retention-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/artifactory-publish-promote-build-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/artifactory-rename-build-verify-workflow.yml
- group: commercial
  title: Terms of Service
  type: TermsOfService
  url: https://jfrog.com/terms-of-service/
- group: commercial
  title: Privacy Policy
  type: PrivacyPolicy
  url: https://jfrog.com/privacy-policy/
- group: operate
  title: Status Page
  type: StatusPage
  url: https://status.jfrog.com/
- group: commercial
  title: Pricing
  type: Pricing
  url: https://jfrog.com/pricing/
- group: company
  title: Blog
  type: Blog
  url: https://jfrog.com/blog/
- group: build
  title: JFrog GitHub
  type: GitHubOrganization
  url: https://github.com/jfrog
- group: other
  title: JFrog on X
  type: X
  url: https://twitter.com/jfrog
- group: operate
  title: Support
  type: Support
  url: https://jfrog.com/support/
- group: start
  title: Developer Portal
  type: Portal
  url: https://jfrog.com/developers/
- group: docs
  title: Documentation
  type: Documentation
  url: https://jfrog.com/help/
- group: start
  title: Getting Started
  type: GettingStarted
  url: https://jfrog.com/help/r/jfrog-artifactory-documentation/getting-started-with-artifactory
- group: start
  title: Sign Up Free
  type: Signup
  url: https://jfrog.com/start-free/
- group: start
  title: Login
  type: Login
  url: https://my.jfrog.com/login/
- group: other
  title: JFrog Community
  type: Resources
  url: https://community.jfrog.com/
- group: learn
  title: YouTube
  type: YouTube
  url: https://www.youtube.com/@jfrog
- group: build
  title: JFrog CLI
  type: CLI
  url: https://jfrog.com/help/r/jfrog-cli/jfrog-cli
- group: operate
  title: Release Notes
  type: ChangeLog
  url: https://jfrog.com/help/r/jfrog-release-information/jfrog-release-notes
created: '2024-01-15'
description: JFrog Artifactory is a universal artifact repository manager supporting all major package formats and build tools including Maven, Gradle, npm, NuGet, PyPI, Docker, Helm, RubyGems, CocoaPods, and more. As the central hub of the JFrog Platform, Artifactory stores, manages, and distributes binary artifacts across the entire software development lifecycle. It integrates with CI/CD pipelines through native plugins for Jenkins, GitHub Actions, CircleCI, and other tools. Artifactory provides comprehensive REST APIs for managing repositories, artifacts, builds, security, and system configuration programmatically.
features:
- description: Single repository manager supporting 30+ package formats including Maven, npm, NuGet, PyPI, Docker, Helm, Conda, Conan, and more.
  name: Universal Package Management
- description: Rich metadata tagging and AQL query language for finding artifacts based on properties, statistics, dates, and custom attributes.
  name: Artifact Metadata and Search
- description: Native CI/CD integration publishing build information to track which artifacts were produced by which build, enabling full artifact traceability.
  name: Build Integration
- description: Fine-grained permission targets, LDAP/SAML/SSO integration, API key management, and access tokens for secure artifact access control.
  name: Security and Permissions
- description: Push and pull replication across multiple Artifactory instances for geo-distributed teams and disaster recovery.
  name: Replication
- description: Full Docker Registry v2 API compliance for pushing, pulling, and managing Docker images with automated vulnerability scanning.
  name: Docker Registry
finops:
- name: Artifactory Finops
  service_category: Developer Tools / Artifact Management
  slug: artifactory-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/artifactory.png
json_schemas:
- name: Artifactory Build Info
  property_count: 18
  slug: artifactory-build-info
- name: Artifactory File Info
  property_count: 14
  slug: artifactory-file-info
- name: Artifactory Permission Target
  property_count: 3
  slug: artifactory-permission-target
- name: Artifactory Repository Configuration
  property_count: 31
  slug: artifactory-repository-configuration
layout: provider
mcp_servers:
- description: ''
  name: artifactory-mcp.yml
  slug: artifactory-mcpyml
modified: '2026-06-20'
name: JFrog Artifactory
nav: Providers
network: true
overview: 'JFrog Artifactory publishes 17 APIs on the [APIs.io](https://apis.io/) network, including AQL Search API, Artifactory Extensions API, Artifacts & Storage API, and 14 more. Tagged areas include Artifacts, DevOps, CI/CD, Docker Registry, and Maven.


  The JFrog Artifactory catalog on APIs.io includes 1 Spectral governance ruleset.


  JFrog Artifactory''s developer surface includes authentication, changelog, CLI, pricing, engineering blog, support, developer portal, and 50 more developer resources.'
plans:
- name: Artifactory Plans Pricing
  plan_count: 6
  slug: artifactory-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 3
  name: Artifactory Rate Limits
  slug: artifactory-rate-limits
rules:
- name: JFrog Artifactory API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: artifactory-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 75.3
  delta: 0.0
  facets:
    commercial_clarity: 92.1
    contract_quality: 69.4
    developer_ergonomics: 65.2
    discoverability: 92.6
    governance: 69.8
    operational_transparency: 68.4
  previous_composite: 75.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/artifactory/refs/heads/main/screenshots/artifactory-2026-06-20T172451.png
security:
- kind: authentication
  name: Artifactory Authentication
  slug: artifactory-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Artifactory Domain Security
  slug: artifactory-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Artifactory Vulnerability Disclosure
  slug: artifactory-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Artifactory Trust Center
  slug: artifactory-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001:2013, ISO/IEC 27017:2014, ISO/IEC 27701:2019, FedRAMP, CSA STAR
slug: artifactory
tags:
- Artifacts
- DevOps
- CI/CD
- Docker Registry
- Maven
- Package Management
- Repository
use_cases:
- description: Development teams integrate Artifactory with Jenkins, GitHub Actions, and other CI/CD tools to store, version, and distribute build artifacts.
  name: CI/CD Pipeline Integration
- description: Platform engineering teams use Artifactory as an enterprise Docker registry with security scanning, access controls, and promotion workflows.
  name: Container Registry
- description: Organizations proxy public package registries (npm, PyPI, Maven Central) through Artifactory to cache dependencies, apply security policies, and ensure build reproducibility.
  name: Dependency Proxy
- description: Release engineers promote artifacts through staging environments using build promotion, managing the lifecycle from snapshot to release.
  name: Release Management
website: https://jfrog.com/developers/
---
