---
aid: cloud
name: Cloud
url: https://raw.githubusercontent.com/api-evangelist/cloud/refs/heads/main/apis.yml
description: Cloud is a topic profile in the API Evangelist Network covering the major public cloud platforms and their APIs. The topic indexes the hyperscalers (Amazon Web Services, Microsoft Azure, Google Cloud, Oracle Cloud, IBM Cloud, Alibaba Cloud) alongside developer-focused alternatives (DigitalOcean, Linode, Vultr, Hetzner, Scaleway), GPU and AI clouds (CoreWeave, Crusoe, Lambda Labs, RunPod), and edge / network-attached compute (Cloudflare Workers, Fastly Compute, Akamai Connected Cloud). It is the parent topic to specialized profiles in the network such as cloud-storage, cloud-cost-management, and cloud-native.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2024-01-01'
modified: '2026-04-23'
specificationVersion: '0.19'
x-type: topic
tags:
  - Cloud
  - Cloud Computing
  - Compute
  - Hyperscaler
  - IaaS
  - Infrastructure
  - PaaS
  - Public Cloud
  - SaaS
apis:
  - aid: cloud:aws
    name: Amazon Web Services
    tags:
      - AWS
      - Hyperscaler
      - IaaS
      - PaaS
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://aws.amazon.com/
    properties:
      - url: https://docs.aws.amazon.com/
        type: Documentation
    description: Amazon Web Services is the largest public cloud, exposing 200+ services through service-specific REST and AWS-query APIs signed with SigV4. Compute (EC2, Lambda, ECS, EKS), storage (S3, EBS, EFS), database (RDS, DynamoDB, Aurora), networking (VPC, Route 53, CloudFront), and AI/ML (Bedrock, SageMaker) all expose programmatic APIs.
  - aid: cloud:azure
    name: Microsoft Azure
    tags:
      - Azure
      - Hyperscaler
      - IaaS
      - PaaS
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://azure.microsoft.com/
    properties:
      - url: https://learn.microsoft.com/en-us/rest/api/azure/
        type: Documentation
    description: Microsoft Azure provides public-cloud compute, storage, database, AI, and identity services through Azure Resource Manager (ARM) REST APIs. Authentication uses Microsoft Entra ID (formerly Azure AD) OAuth tokens. Microsoft Graph exposes the M365 surface alongside the ARM control plane.
  - aid: cloud:gcp
    name: Google Cloud
    tags:
      - GCP
      - Google
      - Hyperscaler
      - IaaS
      - PaaS
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cloud.google.com/
    properties:
      - url: https://cloud.google.com/apis/docs/overview
        type: Documentation
    description: Google Cloud Platform exposes 100+ services through Google APIs (REST + gRPC) authenticated with OAuth 2.0 service accounts. Compute Engine, GKE, Cloud Run, BigQuery, Spanner, Firestore, Vertex AI, and Cloud Storage all share the consistent google apis.com endpoint pattern.
  - aid: cloud:oracle
    name: Oracle Cloud Infrastructure
    tags:
      - Oracle
      - OCI
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.oracle.com/cloud/
    properties:
      - url: https://docs.oracle.com/en-us/iaas/api/
        type: Documentation
    description: Oracle Cloud Infrastructure exposes IaaS and database APIs signed with OCI request signatures. Compute, networking, storage, autonomous database, and Oracle Database@Azure / GCP multicloud surfaces are accessible via region-specific REST endpoints.
  - aid: cloud:ibm
    name: IBM Cloud
    tags:
      - IBM
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.ibm.com/cloud
    properties:
      - url: https://cloud.ibm.com/apidocs
        type: Documentation
    description: IBM Cloud exposes Kubernetes Service, VPC compute, Cloud Object Storage, Watsonx AI, Db2, and Cloudability cost management APIs. Authentication uses IAM API keys exchanged for bearer tokens.
  - aid: cloud:alibaba
    name: Alibaba Cloud
    tags:
      - Alibaba
      - Asia
      - Hyperscaler
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.alibabacloud.com/
    properties:
      - url: https://www.alibabacloud.com/help/en/api-references
        type: Documentation
    description: Alibaba Cloud is the largest public cloud in Asia. APIs cover ECS, OSS object storage, ApsaraDB, Function Compute, and PAI AI services. RPC and ROA-style endpoints are signed with HMAC using AccessKey credentials.
  - aid: cloud:digitalocean
    name: DigitalOcean
    tags:
      - DigitalOcean
      - Developer Cloud
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.digitalocean.com/
    properties:
      - url: https://docs.digitalocean.com/reference/api/
        type: Documentation
    description: DigitalOcean offers a developer-friendly REST API for Droplets, Kubernetes, App Platform, Spaces, Volumes, Load Balancers, Databases, and Functions. Authentication uses bearer tokens.
  - aid: cloud:linode
    name: Linode (Akamai Cloud)
    tags:
      - Akamai
      - Linode
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.linode.com/
    properties:
      - url: https://www.linode.com/docs/api/
        type: Documentation
    description: Linode (now Akamai Connected Cloud) exposes a REST API for Linode instances, Kubernetes (LKE), Object Storage, NodeBalancers, and Cloud Firewalls.
  - aid: cloud:vultr
    name: Vultr
    tags:
      - Vultr
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.vultr.com/
    properties:
      - url: https://www.vultr.com/api/
        type: Documentation
    description: Vultr provides REST APIs for cloud compute, bare metal, Kubernetes, Object Storage, Block Storage, DNS, and Load Balancers across 30+ global regions.
  - aid: cloud:hetzner
    name: Hetzner Cloud
    tags:
      - Europe
      - Hetzner
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.hetzner.com/cloud
    properties:
      - url: https://docs.hetzner.cloud/
        type: Documentation
    description: Hetzner Cloud is a German hyperscaler offering low-cost cloud servers, volumes, networks, and load balancers via a documented REST API with bearer token authentication.
  - aid: cloud:scaleway
    name: Scaleway
    tags:
      - Europe
      - Scaleway
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.scaleway.com/
    properties:
      - url: https://www.scaleway.com/en/developers/api/
        type: Documentation
    description: Scaleway is a French cloud provider with REST APIs for Instances, Kubernetes (Kapsule), Object Storage, Serverless, Databases, and AI inference endpoints.
  - aid: cloud:cloudflare
    name: Cloudflare
    tags:
      - Cloudflare
      - Edge
      - Network
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cloudflare.com/
    properties:
      - url: https://developers.cloudflare.com/api/
        type: Documentation
    description: Cloudflare offers an edge-attached cloud (Workers, R2, D1, Durable Objects, Queues, AI Gateway) accessible via the Cloudflare REST API authenticated with API tokens.
  - aid: cloud:fastly
    name: Fastly Compute
    tags:
      - Edge
      - Fastly
      - WebAssembly
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.fastly.com/products/edge-compute
    properties:
      - url: https://www.fastly.com/documentation/reference/api/
        type: Documentation
    description: Fastly Compute runs WebAssembly workloads at the edge. The Fastly REST API manages services, configurations, dictionaries, and Compute deployments.
  - aid: cloud:coreweave
    name: CoreWeave
    tags:
      - AI
      - CoreWeave
      - GPU
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.coreweave.com/
    properties:
      - url: https://docs.coreweave.com/
        type: Documentation
    description: CoreWeave is a GPU-first cloud focused on AI training and inference workloads. APIs are exposed primarily through Kubernetes-native CRDs and the CoreWeave Cloud REST API.
  - aid: cloud:crusoe
    name: Crusoe Cloud
    tags:
      - AI
      - Crusoe
      - GPU
      - Sustainable
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://crusoecloud.com/
    properties:
      - url: https://docs.crusoecloud.com/reference/api/
        type: Documentation
    description: Crusoe Cloud is a sustainable AI-first cloud powered by stranded and renewable energy. The REST API provisions GPU virtual machines, networking, storage, and projects programmatically.
  - aid: cloud:lambda-labs
    name: Lambda Labs Cloud
    tags:
      - AI
      - GPU
      - Lambda
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://lambdalabs.com/service/gpu-cloud
    properties:
      - url: https://cloud.lambdalabs.com/api/v1/docs
        type: Documentation
    description: Lambda Cloud provides on-demand and reserved NVIDIA GPU instances. The REST API launches and terminates GPU instances, manages SSH keys, and lists instance types.
common:
  - type: Topic
    url: https://apievangelist.com/topics/cloud/
  - type: API Evangelist
    url: https://apievangelist.com/
  - type: Network
    url: https://network.apievangelist.com/
  - type: GitHub
    url: https://github.com/api-evangelist
  - type: Related Topic
    url: https://github.com/api-evangelist/cloud-storage
  - type: Related Topic
    url: https://github.com/api-evangelist/cloud-native
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
