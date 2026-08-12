---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-11'
api_count: 11
apis:
- description: Python tool that ingests infrastructure data from 30+ providers into a Neo4j graph for cross-provider security analysis.
  name: Cartography
  slug: cartography
- description: Cartography intel module that calls AWS APIs (EC2, IAM, S3, RDS, EKS, Lambda, ECS, DynamoDB, CloudWatch, ACM, KMS, CodeBuild, API Gateway, Bedrock, and more) to populate AWS nodes and relationships in
  name: Cartography AWS Intel Module
  slug: aws-ingest
- description: Cartography intel module that calls Google Cloud APIs (Compute, IAM, Cloud SQL, GKE, Cloud Functions, Artifact Registry, Vertex AI) to populate GCP nodes and relationships in the graph.
  name: Cartography Google Cloud Intel Module
  slug: gcp-ingest
- description: Cartography intel module that calls Azure APIs (App Service, AKS, CosmosDB, Container Instance, Key Vault, Storage, Virtual Machines) to populate Azure nodes and relationships in the graph.
  name: Cartography Azure Intel Module
  slug: azure-ingest
- description: Cartography intel module that calls Oracle Cloud Infrastructure APIs (starting with IAM) to populate OCI nodes and relationships.
  name: Cartography Oracle Cloud Intel Module
  slug: oci-ingest
- description: Ingests Okta users, groups, applications, and factors into the graph for identity-focused security analysis.
  name: Cartography Okta Intel Module
  slug: okta-ingest
- description: Ingests Microsoft Entra ID users, groups, applications, and role assignments into the graph.
  name: Cartography Entra ID Intel Module
  slug: entra-id-ingest
- description: Ingests GitHub organizations, repositories, users, and access relationships, enabling code-ownership and secret-exposure graph queries.
  name: Cartography GitHub Intel Module
  slug: github-ingest
- description: Ingests Kubernetes cluster objects (nodes, pods, services, service accounts) for graph-based cluster-security analysis.
  name: Cartography Kubernetes Intel Module
  slug: kubernetes-ingest
- description: Ingests CrowdStrike Falcon hosts and detections, connecting endpoint telemetry to the infrastructure graph.
  name: Cartography CrowdStrike Intel Module
  slug: crowdstrike-ingest
- description: Ingests Cloudflare zones, DNS, and security configurations into the graph for edge-exposure analysis.
  name: Cartography Cloudflare Intel Module
  slug: cloudflare-ingest
artifact_total: 15
common:
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/cartography-cncf/cartography/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/cartography-cncf/cartography/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/cartography-cncf/cartography/blob/master/CONTRIBUTING.md
- group: company
  title: ''
  type: Website
  url: https://lyft.github.io/cartography/
- group: docs
  title: ''
  type: Documentation
  url: https://lyft.github.io/cartography/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/lyft
- group: other
  title: ''
  type: Repository
  url: https://github.com/lyft/cartography
- group: operate
  title: ''
  type: Issues
  url: https://github.com/lyft/cartography/issues
- group: start
  title: ''
  type: GettingStarted
  url: https://lyft.github.io/cartography/install.html
- group: learn
  title: ''
  type: Tutorial
  url: https://lyft.github.io/cartography/usage/tutorial.html
- group: commercial
  title: ''
  type: License
  url: https://github.com/lyft/cartography/blob/master/LICENSE
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/lyft/cartography/releases
- group: operate
  title: ''
  type: Community
  url: https://eng.lyft.com/open-sourcing-cartography-4611ba31a72
created: '2025-01-01'
description: Cartography is an open-source Python security-graph tool originally built at Lyft that consolidates infrastructure assets and the relationships between them into an intuitive Neo4j graph. It ingests data from 30+ cloud, identity, DevOps, and security providers (AWS, GCP, Azure, OCI, Okta, Entra ID, GitHub, Kubernetes, CrowdStrike, and more) and lets security teams answer cross-provider questions such as "which identities can reach which datastores," "which compute instances are exposed to the internet," and "what are the blast radii of a compromised credential."
finops:
- name: Cartography Finops
  service_category: API
  slug: cartography-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cartography.png
jsonld:
- class_count: 0
  name: Cartography Context
  property_count: 9
  slug: cartography-context
layout: provider
modified: '2026-04-23'
name: Cartography
nav: Providers
network: true
overview: 'Cartography publishes 11 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Cloud Security, Graph, CSPM, and Neo4j.


  The Cartography catalog on APIs.io includes 1 JSON-LD context.


  Cartography''s developer surface includes documentation, getting-started guide, tutorials, release notes, and 9 more developer resources.'
plans:
- name: Cartography Plans Pricing
  plan_count: 3
  slug: cartography-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 5
  name: Cartography Rate Limits
  slug: cartography-rate-limits
score:
  band: emerging
  composite: 21.6
  delta: -6.4
  facets:
    commercial_clarity: 15.8
    contract_quality: 8.1
    developer_ergonomics: 23.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 28.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/cartography/refs/heads/main/screenshots/cartography-2026-07-25T204658.png
slug: cartography
tags:
- Security
- Cloud Security
- Graph
- CSPM
- Neo4j
- Open Source
- Lyft
- Asset Inventory
- Identity
website: https://lyft.github.io/cartography/
---
