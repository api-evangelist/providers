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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.7
  scored_at: '2026-07-28'
api_count: 37
apis:
- description: 1-Click applications are pre-built Droplet images or Kubernetes apps with software, features, and configuration details already set up for you. They can be found in the [DigitalOcean Marketplace](http
  name: Digital Ocean 1-Click Applications API
  slug: digital-ocean-1-click-applications-api
- description: Provides information about your current account.
  name: Digital Ocean Account API
  slug: digital-ocean-account-api
- description: Actions are records of events that have occurred on the resources in your account. These can be things like rebooting a Droplet, or transferring an image to a new region. An action object is created e
  name: Digital Ocean Actions API
  slug: digital-ocean-actions-api
- description: 'App Platform is a Platform-as-a-Service (PaaS) offering from DigitalOcean that allows developers to publish code directly to DigitalOcean servers without worrying about the underlying infrastructure. '
  name: Digital Ocean Apps API
  slug: digital-ocean-apps-api
- description: The billing endpoints allow you to retrieve your account balance, invoices and billing history. **Balance:** By sending requests to the `/v2/customers/my/balance` endpoint, you can retrieve the balanc
  name: Digital Ocean Billing API
  slug: digital-ocean-billing-api
- description: Block storage actions are commands that can be given to a DigitalOcean Block Storage Volume. An example would be detaching or attaching a volume from a Droplet. These requests are made on the `/v2/vol
  name: Digital Ocean Block Storage Actions API
  slug: digital-ocean-block-storage-actions-api
- description: '[DigitalOcean Block Storage Volumes](https://docs.digitalocean.com/products/volumes/) provide expanded storage capacity for your Droplets and can be moved between Droplets within a specific region. Vo'
  name: Digital Ocean Block Storage API
  slug: digital-ocean-block-storage-api
- description: Content hosted in DigitalOcean's object storage solution, [Spaces](https://docs.digitalocean.com/products/spaces/), can optionally be served by our globally distributed Content Delivery Network (CDN).
  name: Digital Ocean CDN Endpoints API
  slug: digital-ocean-cdn-endpoints-api
- description: 'In order to perform SSL termination on load balancers, DigitalOcean offers two types of [SSL certificate management](https://docs.digitalocean.com/platform/teams/manage-certificates): * **Custom**: Us'
  name: Digital Ocean Certificates API
  slug: digital-ocean-certificates-api
- description: DigitalOcean offers the ability for you to create a [private container registry](https://docs.digitalocean.com/products/container-registry/) to store your Docker images for use with your Kubernetes cl
  name: Digital Ocean Container Registry API
  slug: digital-ocean-container-registry-api
- description: DigitalOcean's [managed database service](https://docs.digitalocean.com/products/databases) simplifies the creation and management of highly available database clusters. Currently, it offers support f
  name: Digital Ocean Databases API
  slug: digital-ocean-databases-api
- description: Domain record resources are used to set or retrieve information about the individual DNS records configured for a domain. This allows you to build and manage DNS zone files by adding and modifying ind
  name: Digital Ocean Domain Records API
  slug: digital-ocean-domain-records-api
- description: Domain resources are domain names that you have purchased from a domain name registrar that you are managing through the [DigitalOcean DNS interface](https://docs.digitalocean.com/products/networking/
  name: Digital Ocean Domains API
  slug: digital-ocean-domains-api
- description: Droplet actions are tasks that can be executed on a Droplet. These can be things like rebooting, resizing, snapshotting, etc. Droplet action requests are generally targeted at one of the "actions" end
  name: Digital Ocean Droplet Actions API
  slug: digital-ocean-droplet-actions-api
- description: Droplet autoscale pools manage automatic horizontal scaling for your applications based on resource usage (CPU, memory, or both) or a static configuration.
  name: Digital Ocean Droplet Autoscale Pools API
  slug: digital-ocean-droplet-autoscale-pools-api
- description: A [Droplet](https://docs.digitalocean.com/products/droplets/) is a DigitalOcean virtual machine. By sending requests to the Droplet endpoint, you can list, create, or delete Droplets. Some of the attr
  name: Digital Ocean Droplets API
  slug: digital-ocean-droplets-api
- description: '[DigitalOcean Cloud Firewalls](https://docs.digitalocean.com/products/networking/firewalls/) provide the ability to restrict network access to and from a Droplet allowing you to define which ports wil'
  name: Digital Ocean Firewalls API
  slug: digital-ocean-firewalls-api
- description: As of 16 June 2022, we have renamed the Floating IP product to [Reserved IPs](https://docs.digitalocean.com/reference/api/api-reference/#tag/Reserved-IPs). The Reserved IP product's endpoints function
  name: Digital Ocean Floating IP Actions API
  slug: digital-ocean-floating-ip-actions-api
- description: As of 16 June 2022, we have renamed the Floating IP product to [Reserved IPs](https://docs.digitalocean.com/reference/api/api-reference/#tag/Reserved-IPs). The Reserved IP product's endpoints function
  name: Digital Ocean Floating IPs API
  slug: digital-ocean-floating-ips-api
- description: '[Serverless functions](https://docs.digitalocean.com/products/functions) are blocks of code that run on demand without the need to manage any infrastructure. You can develop functions on your local ma'
  name: Digital Ocean Functions API
  slug: digital-ocean-functions-api
- description: Image actions are commands that can be given to a DigitalOcean image. In general, these requests are made on the actions endpoint of a specific image. An image action object is returned. These objects
  name: Digital Ocean Image Actions API
  slug: digital-ocean-image-actions-api
- description: 'A DigitalOcean [image](https://docs.digitalocean.com/products/images/) can be used to create a Droplet and may come in a number of flavors. Currently, there are five types of images: snapshots, backup'
  name: Digital Ocean Images API
  slug: digital-ocean-images-api
- description: '[DigitalOcean Kubernetes](https://docs.digitalocean.com/products/kubernetes/) allows you to quickly deploy scalable and secure Kubernetes clusters. By sending requests to the `/v2/kubernetes/clusters`'
  name: Digital Ocean Kubernetes API
  slug: digital-ocean-kubernetes-api
- description: '[DigitalOcean Load Balancers](https://docs.digitalocean.com/products/networking/load-balancers/) provide a way to distribute traffic across multiple Droplets. By sending requests to the `/v2/load_bala'
  name: Digital Ocean Load Balancers API
  slug: digital-ocean-load-balancers-api
- description: The DigitalOcean Monitoring API makes it possible to programmatically retrieve metrics as well as configure alert policies based on these metrics. The Monitoring API can help you gain insight into how
  name: Digital Ocean Monitoring API
  slug: digital-ocean-monitoring-api
- description: Project Resources are resources that can be grouped into your projects. You can group resources (like Droplets, Spaces, load balancers, domains, and floating IPs) in ways that align with the applicati
  name: Digital Ocean Project Resources API
  slug: digital-ocean-project-resources-api
- description: 'Projects allow you to organize your resources into groups that fit the way you work. You can group resources (like Droplets, Spaces, load balancers, domains, and floating IPs) in ways that align with '
  name: Digital Ocean Projects API
  slug: digital-ocean-projects-api
- description: Provides information about DigitalOcean data center regions.
  name: Digital Ocean Regions API
  slug: digital-ocean-regions-api
- description: As of 16 June 2022, we have renamed the [Floating IP](https://docs.digitalocean.com/reference/api/api-reference/#tag/Floating-IPs) product to Reserved IPs. The Reserved IP product's endpoints function
  name: Digital Ocean Reserved IP Actions API
  slug: digital-ocean-reserved-ip-actions-api
- description: As of 16 June 2022, we have renamed the [Floating IP](https://docs.digitalocean.com/reference/api/api-reference/#tag/Floating-IPs) product to Reserved IPs. The Reserved IP product's endpoints function
  name: Digital Ocean Reserved IPs API
  slug: digital-ocean-reserved-ips-api
- description: The sizes objects represent different packages of hardware resources that can be used for Droplets. When a Droplet is created, a size must be selected so that the correct resources can be allocated. E
  name: Digital Ocean Sizes API
  slug: digital-ocean-sizes-api
- description: '[Snapshots](https://docs.digitalocean.com/products/snapshots/) are saved instances of a Droplet or a block storage volume, which is reflected in the `resource_type` attribute. In order to avoid proble'
  name: Digital Ocean Snapshots API
  slug: digital-ocean-snapshots-api
- description: Manage SSH keys available on your account.
  name: Digital Ocean SSH Keys API
  slug: digital-ocean-ssh-keys-api
- description: A tag is a label that can be applied to a resource (currently Droplets, Images, Volumes, Volume Snapshots, and Database clusters) in order to better organize or facilitate the lookups and actions on i
  name: Digital Ocean Tags API
  slug: digital-ocean-tags-api
- description: '[DigitalOcean Uptime Checks](https://docs.digitalocean.com/products/uptime/) provide the ability to monitor your endpoints from around the world, and alert you when they''re slow, unavailable, or SSL c'
  name: Digital Ocean Uptime API
  slug: digital-ocean-uptime-api
- description: '[VPC Peerings](https://docs.digitalocean.com/products/networking/vpc/how-to/create-peering/) join two VPC networks with a secure, private connection. This allows resources in those networks to connect'
  name: Digital Ocean VPC Peerings API
  slug: digital-ocean-vpc-peerings-api
- description: '[VPCs (virtual private clouds)](https://docs.digitalocean.com/products/networking/vpc/) allow you to create virtual networks containing resources that can communicate with each other in full isolation'
  name: Digital Ocean VPCs API
  slug: digital-ocean-vpcs-api
artifact_total: 42
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/digital-ocean-vulnerability-disclosure.yml
- group: auth
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
created: '2024-03-30'
description: DigitalOcean Holdings, Inc. is an American multinational technology company and cloud service provider. The company is headquartered in New York City, New York, US, with 15 globally distributed data centers. DigitalOcean provides developers, startups, and SMBs with cloud infrastructure-as-a-service platforms.
finops:
- name: Digital Ocean Finops
  service_category: API
  slug: digital-ocean-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/digital-ocean.png
layout: provider
modified: '2026-05-30'
name: Digital Ocean
nav: Providers
network: true
overview: 'Digital Ocean publishes 37 APIs on the [APIs.io](https://apis.io/) network, including 1-Click Applications API, Account API, Actions API, and 34 more. Tagged areas include Cloud, Compute, Servers, and Infrastructure.


  Digital Ocean''s developer surface includes documentation, support, engineering blog, pricing, GitHub presence, signup flow, and 13 more developer resources.'
plans:
- name: Digital Ocean Plans Pricing
  plan_count: 3
  slug: digital-ocean-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 5
  name: Digital Ocean Rate Limits
  slug: digital-ocean-rate-limits
score:
  band: developing
  composite: 46.8
  delta: -2.4
  facets:
    commercial_clarity: 84.2
    contract_quality: 56.7
    developer_ergonomics: 15.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 49.2
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 37
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/digital-ocean/refs/heads/main/screenshots/digital-ocean-2026-06-20T180020.png
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
website: https://docs.digitalocean.com/developer-center/
---
