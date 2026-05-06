---
aid: cartography
name: Cartography
description: Cartography is an open-source Python security-graph tool originally built at Lyft that consolidates infrastructure assets and the relationships between them into an intuitive Neo4j graph. It ingests data from 30+ cloud, identity, DevOps, and security providers (AWS, GCP, Azure, OCI, Okta, Entra ID, GitHub, Kubernetes, CrowdStrike, and more) and lets security teams answer cross-provider questions such as "which identities can reach which datastores," "which compute instances are exposed to the internet," and "what are the blast radii of a compromised credential."
type: Standard
position: Consumer
access: Open
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
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
created: '2025-01-01'
modified: '2026-04-23'
url: https://raw.githubusercontent.com/api-evangelist/cartography/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: cartography:cartography
    name: Cartography
    description: Python tool that ingests infrastructure data from 30+ providers into a Neo4j graph for cross-provider security analysis.
    humanURL: https://lyft.github.io/cartography/
    tags:
      - Security
      - Cloud Security
      - Graph
      - Neo4j
    properties:
      - type: Documentation
        url: https://lyft.github.io/cartography/
      - type: Repository
        url: https://github.com/lyft/cartography
      - type: QueryLanguage
        name: Cypher (Neo4j)
        url: https://neo4j.com/docs/cypher-manual/current/
  - aid: cartography:aws-ingest
    name: Cartography AWS Intel Module
    description: Cartography intel module that calls AWS APIs (EC2, IAM, S3, RDS, EKS, Lambda, ECS, DynamoDB, CloudWatch, ACM, KMS, CodeBuild, API Gateway, Bedrock, and more) to populate AWS nodes and relationships in the graph.
    humanURL: https://lyft.github.io/cartography/modules/aws/index.html
    tags:
      - AWS
      - Cloud
      - Ingest
    properties:
      - type: Documentation
        url: https://lyft.github.io/cartography/modules/aws/index.html
  - aid: cartography:gcp-ingest
    name: Cartography Google Cloud Intel Module
    description: Cartography intel module that calls Google Cloud APIs (Compute, IAM, Cloud SQL, GKE, Cloud Functions, Artifact Registry, Vertex AI) to populate GCP nodes and relationships in the graph.
    humanURL: https://lyft.github.io/cartography/modules/gcp/index.html
    tags:
      - GCP
      - Cloud
      - Ingest
    properties:
      - type: Documentation
        url: https://lyft.github.io/cartography/modules/gcp/index.html
  - aid: cartography:azure-ingest
    name: Cartography Azure Intel Module
    description: Cartography intel module that calls Azure APIs (App Service, AKS, CosmosDB, Container Instance, Key Vault, Storage, Virtual Machines) to populate Azure nodes and relationships in the graph.
    humanURL: https://lyft.github.io/cartography/modules/azure/index.html
    tags:
      - Azure
      - Cloud
      - Ingest
    properties:
      - type: Documentation
        url: https://lyft.github.io/cartography/modules/azure/index.html
  - aid: cartography:oci-ingest
    name: Cartography Oracle Cloud Intel Module
    description: Cartography intel module that calls Oracle Cloud Infrastructure APIs (starting with IAM) to populate OCI nodes and relationships.
    humanURL: https://lyft.github.io/cartography/modules/oci/index.html
    tags:
      - OCI
      - Cloud
      - Ingest
    properties:
      - type: Documentation
        url: https://lyft.github.io/cartography/modules/oci/index.html
  - aid: cartography:okta-ingest
    name: Cartography Okta Intel Module
    description: Ingests Okta users, groups, applications, and factors into the graph for identity-focused security analysis.
    humanURL: https://lyft.github.io/cartography/modules/okta/index.html
    tags:
      - Identity
      - Okta
      - Ingest
    properties:
      - type: Documentation
        url: https://lyft.github.io/cartography/modules/okta/index.html
  - aid: cartography:entra-id-ingest
    name: Cartography Entra ID Intel Module
    description: Ingests Microsoft Entra ID users, groups, applications, and role assignments into the graph.
    humanURL: https://lyft.github.io/cartography/modules/entra/index.html
    tags:
      - Identity
      - Entra ID
      - Ingest
    properties:
      - type: Documentation
        url: https://lyft.github.io/cartography/modules/entra/index.html
  - aid: cartography:github-ingest
    name: Cartography GitHub Intel Module
    description: Ingests GitHub organizations, repositories, users, and access relationships, enabling code-ownership and secret-exposure graph queries.
    humanURL: https://lyft.github.io/cartography/modules/github/index.html
    tags:
      - GitHub
      - SCM
      - Ingest
    properties:
      - type: Documentation
        url: https://lyft.github.io/cartography/modules/github/index.html
  - aid: cartography:kubernetes-ingest
    name: Cartography Kubernetes Intel Module
    description: Ingests Kubernetes cluster objects (nodes, pods, services, service accounts) for graph-based cluster-security analysis.
    humanURL: https://lyft.github.io/cartography/modules/kubernetes/index.html
    tags:
      - Kubernetes
      - Containers
      - Ingest
    properties:
      - type: Documentation
        url: https://lyft.github.io/cartography/modules/kubernetes/index.html
  - aid: cartography:crowdstrike-ingest
    name: Cartography CrowdStrike Intel Module
    description: Ingests CrowdStrike Falcon hosts and detections, connecting endpoint telemetry to the infrastructure graph.
    humanURL: https://lyft.github.io/cartography/modules/crowdstrike/index.html
    tags:
      - EDR
      - CrowdStrike
      - Ingest
    properties:
      - type: Documentation
        url: https://lyft.github.io/cartography/modules/crowdstrike/index.html
  - aid: cartography:cloudflare-ingest
    name: Cartography Cloudflare Intel Module
    description: Ingests Cloudflare zones, DNS, and security configurations into the graph for edge-exposure analysis.
    humanURL: https://lyft.github.io/cartography/modules/cloudflare/index.html
    tags:
      - DNS
      - Edge
      - Ingest
    properties:
      - type: Documentation
        url: https://lyft.github.io/cartography/modules/cloudflare/index.html
common:
  - type: Website
    url: https://lyft.github.io/cartography/
  - type: Documentation
    url: https://lyft.github.io/cartography/
  - type: GitHubOrg
    name: Lyft GitHub
    url: https://github.com/lyft
  - type: Repository
    url: https://github.com/lyft/cartography
  - type: Issues
    url: https://github.com/lyft/cartography/issues
  - type: GettingStarted
    url: https://lyft.github.io/cartography/install.html
  - type: Tutorial
    url: https://lyft.github.io/cartography/usage/tutorial.html
  - type: License
    name: Apache 2.0
    url: https://github.com/lyft/cartography/blob/master/LICENSE
  - type: Releases
    url: https://github.com/lyft/cartography/releases
  - type: Community
    name: Lyft Engineering Blog
    url: https://eng.lyft.com/open-sourcing-cartography-4611ba31a72
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
