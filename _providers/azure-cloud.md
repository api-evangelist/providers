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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Azure Cloud Agentic Access
  operation_count: 13
  slug: azure-cloud-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 13
apis:
- description: REST APIs for Azure networking resources including Virtual Networks, Load Balancers, Application Gateways, VPN Gateways, Azure Firewall, Front Door, and ExpressRoute.
  name: Azure Networking API
  slug: azure-networking-api
- description: Managed database REST APIs for Azure SQL Database, Azure Cosmos DB, Azure Database for PostgreSQL, Azure Database for MySQL, and Azure Cache for Redis.
  name: Azure Databases API
  slug: azure-databases-api
- description: REST APIs for Azure AI and Machine Learning services including Azure OpenAI Service, Azure Machine Learning, Azure AI Search, Computer Vision, Speech, and Document Intelligence.
  name: Azure AI Services API
  slug: azure-ai-api
- description: REST APIs for Azure security services including Microsoft Defender for Cloud, Key Vault, Microsoft Sentinel, and Web Application Firewall.
  name: Azure Security API
  slug: azure-security-api
- description: REST APIs for Azure integration services including Service Bus, Event Grid, Logic Apps, and API Management for building event-driven and workflow-based applications.
  name: Azure Integration API
  slug: azure-integration-api
- description: REST APIs for Azure analytics services including Synapse Analytics, Data Factory, Stream Analytics, Data Explorer, and Microsoft Fabric for big data and real-time analytics workloads.
  name: Azure Analytics API
  slug: azure-analytics-api
- description: REST APIs for Azure management and governance including Azure Resource Manager, Azure Monitor, Azure Policy, Cost Management, and Azure Advisor.
  name: Azure Management API
  slug: azure-management-api
- description: REST APIs for Azure IoT services including IoT Hub, IoT Central, IoT Edge, and Azure Digital Twins for connecting, monitoring, and managing IoT devices at scale.
  name: Azure IoT API
  slug: azure-iot-api
- description: Availability sets
  name: Microsoft Azure Cloud Availability Sets API
  slug: azure-cloud-availability-sets-api
- description: Managed disks
  name: Microsoft Azure Cloud Disks API
  slug: azure-cloud-disks-api
- description: Managed disk snapshots
  name: Microsoft Azure Cloud Snapshots API
  slug: azure-cloud-snapshots-api
- description: VMSS lifecycle operations
  name: Microsoft Azure Cloud Virtual Machine Scale Sets API
  slug: azure-cloud-virtual-machine-scale-sets-api
- description: VM lifecycle operations
  name: Microsoft Azure Cloud Virtual Machines API
  slug: azure-cloud-virtual-machines-api
artifact_total: 43
collections:
- collection_type: open
  name: Azure Compute REST API
  slug: open-azure-cloud
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-cloud-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-cloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/azure-cloud-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/azure-cloud-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft-azure-cloud
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/developer/intro/azure-developer-overview
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/rest/api/azure/
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-client-creds-grant-flow
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free/
- group: build
  title: ''
  type: CLI
  url: https://learn.microsoft.com/en-us/cli/azure/
- group: build
  title: ''
  type: SDKs
  url: https://azure.github.io/azure-sdk/
created: '2024-01-01'
description: A comprehensive collection of Microsoft Azure cloud service APIs covering compute, storage, databases, AI, networking, security, and developer tools. Azure provides IaaS, PaaS, and SaaS delivery models through a global network of datacenters, with REST APIs secured by Microsoft Entra ID authentication.
features:
- description: Operates across 60+ regions worldwide with 99.99% SLA guarantees for most services.
  name: Global Infrastructure
- description: All REST APIs use OAuth 2.0 / Microsoft Entra ID for secure, standards-based authentication.
  name: Microsoft Entra ID Authentication
- description: Consistent management layer for deploying and managing all Azure resources via ARM templates and REST.
  name: Azure Resource Manager
- description: Long-running operations follow the async pattern with polling endpoints for status checks.
  name: Async Operations
- description: Per-subscription throttling with remaining request counts returned in response headers.
  name: Throttling and Rate Limits
- description: List operations return nextLink for cursor-based pagination across large result sets.
  name: Pagination
- description: Official SDKs available for .NET, Java, Python, JavaScript/TypeScript, Go, C++, and Rust.
  name: Multi-Language SDKs
- description: Azure Arc extends Azure management to on-premises and multi-cloud environments.
  name: Hybrid and Multi-Cloud
finops:
- name: Azure Cloud Finops
  service_category: API
  slug: azure-cloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/azure-cloud.png
integrations:
- description: Native integration with GitHub for source control, Actions CI/CD, and Azure deployment.
  name: GitHub
- description: Integration with Microsoft 365 services via Microsoft Graph API.
  name: Microsoft 365
- description: Azure Provider for Terraform enables infrastructure-as-code deployments.
  name: Terraform
- description: First-class Azure extension support in Visual Studio and Visual Studio Code.
  name: Visual Studio / VS Code
- description: Azure Kubernetes Service provides managed Kubernetes with deep Azure ecosystem integration.
  name: Kubernetes
- description: Native Datadog integration for monitoring Azure infrastructure and applications.
  name: Datadog
- description: Splunk Add-on for Microsoft Azure for security and operational analytics.
  name: Splunk
layout: provider
modified: '2026-04-19'
name: Microsoft Azure Cloud
nav: Providers
network: true
overview: 'Microsoft Azure Cloud publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Availability Sets API, Disks API, Snapshots API, and 2 more. Tagged areas include AI, Cloud Computing, Databases, IaaS, and Infrastructure.


  Microsoft Azure Cloud''s developer surface includes authentication, developer portal, documentation, getting-started guide, API reference, engineering blog, support, and 13 more developer resources.'
plans:
- name: Azure Cloud Plans Pricing
  plan_count: 3
  slug: azure-cloud-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 5
  name: Azure Cloud Rate Limits
  slug: azure-cloud-rate-limits
scopes:
- name: Azure Cloud Scopes
  scope_count: 1
  slug: azure-cloud-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: developing
  composite: 50.1
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 55.2
    developer_ergonomics: 65.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 50.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-cloud/refs/heads/main/screenshots/azure-cloud-2026-06-20T172840.png
security:
- kind: authentication
  name: Azure Cloud Authentication
  slug: azure-cloud-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Azure Cloud Domain Security
  slug: azure-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: azure-cloud
tags:
- AI
- Cloud Computing
- Databases
- IaaS
- Infrastructure
- Machine Learning
- Microsoft
- Networking
- PaaS
- Platform as a Service
- SaaS
- Storage
use_cases:
- description: Migrate on-premises workloads to Azure using IaaS VMs or PaaS services with hybrid connectivity.
  name: Enterprise Cloud Migration
- description: Build microservices using Azure Kubernetes Service, Container Apps, and serverless Functions.
  name: Cloud-Native Application Development
- description: Train and deploy ML models using Azure Machine Learning and Azure OpenAI Service.
  name: AI and Machine Learning Workloads
- description: Build data pipelines with Data Factory and analyze at scale with Synapse Analytics.
  name: Data Analytics and Business Intelligence
- description: Automate build, test, and deployment pipelines using Azure DevOps and GitHub Actions.
  name: DevOps and CI/CD Automation
- description: Connect and manage millions of IoT devices with IoT Hub and IoT Central.
  name: IoT Device Management
- description: Protect workloads and meet compliance requirements with Defender for Cloud and Sentinel.
  name: Security and Compliance
website: https://portal.azure.com
---
