---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://api.digitalocean.com/v2
  baseurl_source: declared
  description: Provides information about your current account.
  name: Digital Ocean Account API
  slug: digital-ocean-account-api
- baseURL: https://api.digitalocean.com/v2
  baseurl_source: declared
  description: Actions are records of events that have occurred on the resources in your account. These can be things like rebooting a Droplet, or transferring an image to a new region. An action object is created e
  name: Digital Ocean Actions API
  slug: digital-ocean-actions-api
- baseURL: https://api.digitalocean.com/v2
  baseurl_source: declared
  description: 'App Platform is a Platform-as-a-Service (PaaS) offering from DigitalOcean that allows developers to publish code directly to DigitalOcean servers without worrying about the underlying infrastructure. '
  name: Digital Ocean Apps API
  slug: digital-ocean-apps-api
- baseURL: https://api.digitalocean.com/v2
  baseurl_source: declared
  description: The billing endpoints allow you to retrieve your account balance, invoices and billing history. **Balance:** By sending requests to the `/v2/customers/my/balance` endpoint, you can retrieve the balanc
  name: Digital Ocean Billing API
  slug: digital-ocean-billing-api
- baseURL: https://api.digitalocean.com/v2
  baseurl_source: declared
  description: 'In order to perform SSL termination on load balancers, DigitalOcean offers two types of [SSL certificate management](https://docs.digitalocean.com/platform/teams/manage-certificates): * **Custom**: Us'
  name: Digital Ocean Certificates API
  slug: digital-ocean-certificates-api
- baseURL: https://api.digitalocean.com/v2
  baseurl_source: declared
  description: DigitalOcean's [managed database service](https://docs.digitalocean.com/products/databases) simplifies the creation and management of highly available database clusters. Currently, it offers support f
  name: Digital Ocean Databases API
  slug: digital-ocean-databases-api
- baseURL: https://api.digitalocean.com/v2
  baseurl_source: declared
  description: Domain resources are domain names that you have purchased from a domain name registrar that you are managing through the [DigitalOcean DNS interface](https://docs.digitalocean.com/products/networking/
  name: Digital Ocean Domains API
  slug: digital-ocean-domains-api
- baseURL: https://api.digitalocean.com/v2
  baseurl_source: declared
  description: A [Droplet](https://docs.digitalocean.com/products/droplets/) is a DigitalOcean virtual machine. By sending requests to the Droplet endpoint, you can list, create, or delete Droplets. Some of the attr
  name: Digital Ocean Droplets API
  slug: digital-ocean-droplets-api
- baseURL: https://api.digitalocean.com/v2
  baseurl_source: declared
  description: '[DigitalOcean Cloud Firewalls](https://docs.digitalocean.com/products/networking/firewalls/) provide the ability to restrict network access to and from a Droplet allowing you to define which ports wil'
  name: Digital Ocean Firewalls API
  slug: digital-ocean-firewalls-api
- baseURL: https://api.digitalocean.com/v2
  baseurl_source: declared
  description: As of 16 June 2022, we have renamed the Floating IP product to [Reserved IPs](https://docs.digitalocean.com/reference/api/api-reference/#tag/Reserved-IPs). The Reserved IP product's endpoints function
  name: Digital Ocean Floating IPs API
  slug: digital-ocean-floating-ips-api
- baseURL: https://api.digitalocean.com/v2
  baseurl_source: declared
  description: '[Serverless functions](https://docs.digitalocean.com/products/functions) are blocks of code that run on demand without the need to manage any infrastructure. You can develop functions on your local ma'
  name: Digital Ocean Functions API
  slug: digital-ocean-functions-api
- baseURL: https://api.digitalocean.com/v2
  baseurl_source: declared
  description: 'A DigitalOcean [image](https://docs.digitalocean.com/products/images/) can be used to create a Droplet and may come in a number of flavors. Currently, there are five types of images: snapshots, backup'
  name: Digital Ocean Images API
  slug: digital-ocean-images-api
- baseURL: https://api.digitalocean.com/v2
  baseurl_source: declared
  description: '[DigitalOcean Kubernetes](https://docs.digitalocean.com/products/kubernetes/) allows you to quickly deploy scalable and secure Kubernetes clusters. By sending requests to the `/v2/kubernetes/clusters`'
  name: Digital Ocean Kubernetes API
  slug: digital-ocean-kubernetes-api
- baseURL: https://api.digitalocean.com/v2
  baseurl_source: declared
  description: '[DigitalOcean Load Balancers](https://docs.digitalocean.com/products/networking/load-balancers/) provide a way to distribute traffic across multiple Droplets. By sending requests to the `/v2/load_bala'
  name: Digital Ocean Load Balancers API
  slug: digital-ocean-load-balancers-api
- baseURL: https://api.digitalocean.com/v2
  baseurl_source: declared
  description: The DigitalOcean Monitoring API makes it possible to programmatically retrieve metrics as well as configure alert policies based on these metrics. The Monitoring API can help you gain insight into how
  name: Digital Ocean Monitoring API
  slug: digital-ocean-monitoring-api
- baseURL: https://api.digitalocean.com/v2
  baseurl_source: declared
  description: 'Projects allow you to organize your resources into groups that fit the way you work. You can group resources (like Droplets, Spaces, load balancers, domains, and floating IPs) in ways that align with '
  name: Digital Ocean Projects API
  slug: digital-ocean-projects-api
- baseURL: https://api.digitalocean.com/v2
  baseurl_source: declared
  description: Provides information about DigitalOcean data center regions.
  name: Digital Ocean Regions API
  slug: digital-ocean-regions-api
- baseURL: https://api.digitalocean.com/v2
  baseurl_source: declared
  description: As of 16 June 2022, we have renamed the [Floating IP](https://docs.digitalocean.com/reference/api/api-reference/#tag/Floating-IPs) product to Reserved IPs. The Reserved IP product's endpoints function
  name: Digital Ocean Reserved IPs API
  slug: digital-ocean-reserved-ips-api
- baseURL: https://api.digitalocean.com/v2
  baseurl_source: declared
  description: The sizes objects represent different packages of hardware resources that can be used for Droplets. When a Droplet is created, a size must be selected so that the correct resources can be allocated. E
  name: Digital Ocean Sizes API
  slug: digital-ocean-sizes-api
- baseURL: https://api.digitalocean.com/v2
  baseurl_source: declared
  description: '[Snapshots](https://docs.digitalocean.com/products/snapshots/) are saved instances of a Droplet or a block storage volume, which is reflected in the `resource_type` attribute. In order to avoid proble'
  name: Digital Ocean Snapshots API
  slug: digital-ocean-snapshots-api
- baseURL: https://api.digitalocean.com/v2
  baseurl_source: declared
  description: A tag is a label that can be applied to a resource (currently Droplets, Images, Volumes, Volume Snapshots, and Database clusters) in order to better organize or facilitate the lookups and actions on i
  name: Digital Ocean Tags API
  slug: digital-ocean-tags-api
- baseURL: https://api.digitalocean.com/v2
  baseurl_source: declared
  description: '[DigitalOcean Uptime Checks](https://docs.digitalocean.com/products/uptime/) provide the ability to monitor your endpoints from around the world, and alert you when they''re slow, unavailable, or SSL c'
  name: Digital Ocean Uptime API
  slug: digital-ocean-uptime-api
- baseURL: https://api.digitalocean.com/v2
  baseurl_source: declared
  description: '[VPC Peerings](https://docs.digitalocean.com/products/networking/vpc/how-to/create-peering/) join two VPC networks with a secure, private connection. This allows resources in those networks to connect'
  name: Digital Ocean VPC Peerings API
  slug: digital-ocean-vpc-peerings-api
- baseURL: https://api.digitalocean.com/v2
  baseurl_source: declared
  description: '[VPCs (virtual private clouds)](https://docs.digitalocean.com/products/networking/vpc/) allow you to create virtual networks containing resources that can communicate with each other in full isolation'
  name: Digital Ocean VP Cs API
  slug: digital-ocean-vpcs-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The 1 Clicks API from Digital Ocean — 2 operation(s) for 1 clicks.
  name: Digital Ocean 1 Clicks API
  slug: digital-ocean-1-clicks-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: 'Action Gateway gives AI agents governed access to tools over the Model Context Protocol (MCP). The `/v2/action-gateway` endpoints manage the tool catalog and the resources that control how agents use '
  name: Digital Ocean Action Gateway API
  slug: digital-ocean-action-gateway-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Add Ons API from Digital Ocean — 5 operation(s) for add ons.
  name: Digital Ocean Add Ons API
  slug: digital-ocean-add-ons-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Agents API from Digital Ocean — 41 operation(s) for agents.
  name: Digital Ocean Agents API
  slug: digital-ocean-agents-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Approvals API from Digital Ocean — 2 operation(s) for approvals.
  name: Digital Ocean Approvals API
  slug: digital-ocean-approvals-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Async Invoke API from Digital Ocean — 1 operation(s) for async invoke.
  name: Digital Ocean Async Invoke API
  slug: digital-ocean-async-invoke-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Audio API from Digital Ocean — 1 operation(s) for audio.
  name: Digital Ocean Audio API
  slug: digital-ocean-audio-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Batches API from Digital Ocean — 5 operation(s) for batches.
  name: Digital Ocean Batches API
  slug: digital-ocean-batches-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Byoip Prefixes API from Digital Ocean — 3 operation(s) for byoip prefixes.
  name: Digital Ocean Byoip Prefixes API
  slug: digital-ocean-byoip-prefixes-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Cdn API from Digital Ocean — 3 operation(s) for cdn.
  name: Digital Ocean Cdn API
  slug: digital-ocean-cdn-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Code API from Digital Ocean — 1 operation(s) for code.
  name: Digital Ocean Code API
  slug: digital-ocean-code-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Consent API from Digital Ocean — 2 operation(s) for consent.
  name: Digital Ocean Consent API
  slug: digital-ocean-consent-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Customers API from Digital Ocean — 9 operation(s) for customers.
  name: Digital Ocean Customers API
  slug: digital-ocean-customers-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Dedicated Inferences API from Digital Ocean — 9 operation(s) for dedicated inferences.
  name: Digital Ocean Dedicated Inferences API
  slug: digital-ocean-dedicated-inferences-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: Text embedding vectors via `POST /v1/embeddings` on the [Serverless Inference](https://docs.digitalocean.com/reference/api/api-reference/#tag/Serverless-Inference) base URL `https://inference.do-ai.ru
  name: Digital Ocean Embeddings API
  slug: digital-ocean-embeddings-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Gen Ai API from Digital Ocean — 96 operation(s) for gen ai.
  name: Digital Ocean Gen Ai API
  slug: digital-ocean-gen-ai-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The DigitalOcean Insights API provides observability resources for monitoring your infrastructure, including alert rules that evaluate metrics, notification channels that deliver alert events, read-on
  name: Digital Ocean Insights API
  slug: digital-ocean-insights-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Messages API from Digital Ocean — 1 operation(s) for messages.
  name: Digital Ocean Messages API
  slug: digital-ocean-messages-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Microvms API from Digital Ocean — 10 operation(s) for microvms.
  name: Digital Ocean Microvms API
  slug: digital-ocean-microvms-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Models API from Digital Ocean — 1 operation(s) for models.
  name: Digital Ocean Models API
  slug: digital-ocean-models-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Nfs API from Digital Ocean — 7 operation(s) for nfs.
  name: Digital Ocean Nfs API
  slug: digital-ocean-nfs-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: Organizations group multiple teams under a shared administrative boundary. The Organizations API lets you create teams within an organization and list the teams that belong to it. These endpoints must
  name: Digital Ocean Organizations API
  slug: digital-ocean-organizations-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: Partner Network Connect lets you establish high-bandwidth, low-latency network connections directly between DigitalOcean VPC networks and other public cloud providers or on-premises datacenters.
  name: Digital Ocean Partner Network Connect API
  slug: digital-ocean-partner-network-connect-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Registries API from Digital Ocean — 15 operation(s) for registries.
  name: Digital Ocean Registries API
  slug: digital-ocean-registries-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Registry API from Digital Ocean — 14 operation(s) for registry.
  name: Digital Ocean Registry API
  slug: digital-ocean-registry-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Reports API from Digital Ocean — 1 operation(s) for reports.
  name: Digital Ocean Reports API
  slug: digital-ocean-reports-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Reserved Ipv6 API from Digital Ocean — 3 operation(s) for reserved ipv6.
  name: Digital Ocean Reserved Ipv6 API
  slug: digital-ocean-reserved-ipv6-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Responses API from Digital Ocean — 1 operation(s) for responses.
  name: Digital Ocean Responses API
  slug: digital-ocean-responses-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: Security CSPM endpoints for scans, scan findings, and settings.
  name: Digital Ocean Security API
  slug: digital-ocean-security-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The DigitalOcean Signals API provides observability for environment conversations, such as Harness Runtime conversations and Serverless Inference chat completions, detecting behavioral signals such as
  name: Digital Ocean Signals API
  slug: digital-ocean-signals-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Spaces API from Digital Ocean — 2 operation(s) for spaces.
  name: Digital Ocean Spaces API
  slug: digital-ocean-spaces-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Systemone API from Digital Ocean — 1 operation(s) for systemone.
  name: Digital Ocean Systemone API
  slug: digital-ocean-systemone-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Tools API from Digital Ocean — 3 operation(s) for tools.
  name: Digital Ocean Tools API
  slug: digital-ocean-tools-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The <upload Url> API from Digital Ocean — 1 operation(s) for <upload url>.
  name: Digital Ocean <upload Url> API
  slug: digital-ocean-upload-url-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: Vector DB provides APIs for provisioning and managing vector database instances on DigitalOcean. By sending requests to the `/v2/vector-databases` endpoint, you can list, create, update, resize, and d
  name: Digital Ocean Vector Databases API
  slug: digital-ocean-vector-databases-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Videos API from Digital Ocean — 3 operation(s) for videos.
  name: Digital Ocean Videos API
  slug: digital-ocean-videos-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Volumes API from Digital Ocean — 7 operation(s) for volumes.
  name: Digital Ocean Volumes API
  slug: digital-ocean-volumes-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Vpc Nat Gateways API from Digital Ocean — 2 operation(s) for vpc nat gateways.
  name: Digital Ocean Vpc Nat Gateways API
  slug: digital-ocean-vpc-nat-gateways-api
- baseURL: https://api.digitalocean.com
  baseurl_source: declared
  description: The Chat Completions API from Digital Ocean — 2 operation(s) for chat completions.
  name: Digital Ocean Chat Completions API
  slug: digital-ocean-chat-completions-api
artifact_total: 108
collections:
- collection_type: open
  name: DigitalOcean 1-Click Applications API
  slug: open-digital-ocean-1-click-applications-api
- collection_type: open
  name: DigitalOcean Account API
  slug: open-digital-ocean-account-api
- collection_type: open
  name: DigitalOcean Actions API
  slug: open-digital-ocean-actions-api
- collection_type: open
  name: DigitalOcean Apps API
  slug: open-digital-ocean-apps-api
- collection_type: open
  name: DigitalOcean Billing API
  slug: open-digital-ocean-billing-api
- collection_type: open
  name: DigitalOcean Block Storage Actions API
  slug: open-digital-ocean-block-storage-actions-api
- collection_type: open
  name: DigitalOcean Block Storage API
  slug: open-digital-ocean-block-storage-api
- collection_type: open
  name: DigitalOcean CDN Endpoints API
  slug: open-digital-ocean-cdn-endpoints-api
- collection_type: open
  name: DigitalOcean Certificates API
  slug: open-digital-ocean-certificates-api
- collection_type: open
  name: DigitalOcean Container Registry API
  slug: open-digital-ocean-container-registry-api
- collection_type: open
  name: DigitalOcean Databases API
  slug: open-digital-ocean-databases-api
- collection_type: open
  name: DigitalOcean Domain Records API
  slug: open-digital-ocean-domain-records-api
- collection_type: open
  name: DigitalOcean Domains API
  slug: open-digital-ocean-domains-api
- collection_type: open
  name: DigitalOcean Droplet Actions API
  slug: open-digital-ocean-droplet-actions-api
- collection_type: open
  name: DigitalOcean Droplet Autoscale Pools API
  slug: open-digital-ocean-droplet-autoscale-pools-api
- collection_type: open
  name: DigitalOcean Droplets API
  slug: open-digital-ocean-droplets-api
- collection_type: open
  name: DigitalOcean Firewalls API
  slug: open-digital-ocean-firewalls-api
- collection_type: open
  name: DigitalOcean Floating IP Actions API
  slug: open-digital-ocean-floating-ip-actions-api
- collection_type: open
  name: DigitalOcean Floating IPs API
  slug: open-digital-ocean-floating-ips-api
- collection_type: open
  name: DigitalOcean Functions API
  slug: open-digital-ocean-functions-api
- collection_type: open
  name: DigitalOcean Image Actions API
  slug: open-digital-ocean-image-actions-api
- collection_type: open
  name: DigitalOcean Images API
  slug: open-digital-ocean-images-api
- collection_type: open
  name: DigitalOcean Kubernetes API
  slug: open-digital-ocean-kubernetes-api
- collection_type: open
  name: DigitalOcean Load Balancers API
  slug: open-digital-ocean-load-balancers-api
- collection_type: open
  name: DigitalOcean Monitoring API
  slug: open-digital-ocean-monitoring-api
- collection_type: open
  name: DigitalOcean Project Resources API
  slug: open-digital-ocean-project-resources-api
- collection_type: open
  name: DigitalOcean Projects API
  slug: open-digital-ocean-projects-api
- collection_type: open
  name: DigitalOcean Regions API
  slug: open-digital-ocean-regions-api
- collection_type: open
  name: DigitalOcean Reserved IP Actions API
  slug: open-digital-ocean-reserved-ip-actions-api
- collection_type: open
  name: DigitalOcean Reserved IPs API
  slug: open-digital-ocean-reserved-ips-api
- collection_type: open
  name: DigitalOcean Sizes API
  slug: open-digital-ocean-sizes-api
- collection_type: open
  name: DigitalOcean Snapshots API
  slug: open-digital-ocean-snapshots-api
- collection_type: open
  name: DigitalOcean SSH Keys API
  slug: open-digital-ocean-ssh-keys-api
- collection_type: open
  name: DigitalOcean Tags API
  slug: open-digital-ocean-tags-api
- collection_type: open
  name: DigitalOcean Uptime API
  slug: open-digital-ocean-uptime-api
- collection_type: open
  name: DigitalOcean VPC Peerings API
  slug: open-digital-ocean-vpc-peerings-api
- collection_type: open
  name: DigitalOcean VPCs API
  slug: open-digital-ocean-vpcs-api
common:
- group: commercial
  href: https://artifacts.apis.io/digital-ocean/finops/digital-ocean-finops.yml
  title: ''
  type: FinOps
  url: finops/digital-ocean-finops.yml
- group: operate
  href: https://artifacts.apis.io/digital-ocean/rate-limits/digital-ocean-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/digital-ocean-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/digital-ocean/plans/digital-ocean-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/digital-ocean-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.digitalocean.com/
- group: other
  href: https://artifacts.apis.io/digital-ocean/capabilities/digital-ocean-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/digital-ocean-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/digitalocean/openapi/issues
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/digitalocean/openapi/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/digitalocean/openapi/blob/main/LICENSE
- group: auth
  href: https://artifacts.apis.io/digital-ocean/security/digital-ocean-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/digital-ocean-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/digital-ocean/security/digital-ocean-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/digital-ocean-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/digitalocean
- group: docs
  title: ''
  type: Documentation
  url: https://docs.digitalocean.com/
- group: operate
  title: ''
  type: Support
  url: https://docs.digitalocean.com/support/
- group: other
  title: ''
  type: Developer
  url: https://docs.digitalocean.com/developer-center/
- group: company
  title: ''
  type: Blog
  url: https://blog.digitalocean.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.digitalocean.com/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/digitalocean
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.digitalocean.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.digitalocean.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.digitalocean.com/legal/terms-of-service-agreement
- group: learn
  title: ''
  type: Tutorials
  url: https://www.digitalocean.com/community
- group: other
  title: ''
  type: OpenSource
  url: https://docs.digitalocean.com/reference/opensource/
- group: build
  title: ''
  type: Libraries
  url: https://docs.digitalocean.com/reference/libraries/
- group: other
  title: ''
  type: Ideas
  url: https://ideas.digitalocean.com/documentation
- group: start
  title: ''
  type: Signup
  url: https://cloud.digitalocean.com/registrations/new
- group: start
  title: ''
  type: Login
  url: https://cloud.digitalocean.com/login
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.digitalocean.com/llms.txt
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/digitalocean/openapi/blob/8c0c40c521e0682242d5e9dc6fd9e99e16423f8e/.spectral.yml
created: '2024-03-30'
description: DigitalOcean Holdings, Inc. is an American multinational technology company and cloud service provider. The company is headquartered in New York City, New York, US, with 15 globally distributed data centers. DigitalOcean provides developers, startups, and SMBs with cloud infrastructure-as-a-service platforms.
finops:
- has_sources: true
  method: derived
  name: Digital Ocean Finops
  primary_unit: gib
  service_category: ''
  slug: digital-ocean-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/digital-ocean.png
layout: provider
mcp_servers:
- description: Remote MCP server at apps.mcp.digitalocean.com over HTTP.
  name: Digital Ocean MCP Server
  slug: digital-ocean
modified: '2026-05-30'
name: Digital Ocean
nav: Providers
network: true
overview: 'Digital Ocean publishes 63 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Actions API, Apps API, and 60 more. Tagged areas include Cloud, Compute, Servers, and Infrastructure.


  The Digital Ocean catalog on APIs.io includes 1 Spectral governance ruleset.


  Digital Ocean''s developer surface includes documentation, support, engineering blog, pricing, GitHub presence, signup flow, and 22 more developer resources.'
plans:
- name: Digital Ocean Plans Pricing
  plan_count: 20
  slug: digital-ocean-plans-pricing
- name: Digital Ocean Price Estimates
  plan_count: 0
  slug: digital-ocean-price-estimates
random_paper: 1
rate_limits:
- limit_count: 8
  name: Digital Ocean Rate Limits
  slug: digital-ocean-rate-limits
rules:
- authorship: provider
  effective_rule_count: 41
  extends:
  - spectral:oas
  - ./spectral/ruleset.yml
  name: Digital Ocean — openapi rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: digital-ocean-openapi-spectral-rules
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 64.0
    catalog_earned_first_party: 29.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 77.6
    contract_governance: 15.2
    contract_quality: 43.0
    developer_ergonomics: 16.7
    discoverability: 66.7
    operational_transparency: 63.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  open_source:
    applies: true
    score: 25.0
  previous_composite: 47.9
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 64
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/digital-ocean/digital-ocean-2026-06-20T180020.png
security:
- kind: domain-security
  name: Digital Ocean Domain Security
  slug: digital-ocean-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Digital Ocean Vulnerability Disclosure
  slug: digital-ocean-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
slug: digital-ocean
tags:
- Cloud
- Compute
- Servers
- Infrastructure
website: https://www.digitalocean.com/
---
