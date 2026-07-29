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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 107
  human_in_the_loop: 7
  name: Hetzner Agentic Access
  operation_count: 189
  slug: hetzner-agentic-access
  summary_line: 189 operations · 107 acting · 7 human-in-the-loop
api_count: 32
apis:
- description: The Hetzner DNS API provides programmatic access to manage DNS zones, records, and configurations for domains hosted with Hetzner's DNS service.
  name: Hetzner DNS API
  slug: hetzner-dns-api
- description: Actions represent asynchronous tasks within the API, targeting one or more resources. See [Actions](#description/actions) for more details.
  name: Hetzner Actions API
  slug: hetzner-actions-api
- description: The Certificate Actions API from Hetzner — 5 operation(s) for certificate actions.
  name: Hetzner Certificate Actions API
  slug: hetzner-certificate-actions-api
- description: TLS/SSL Certificates prove the identity of a Server and are used to encrypt client traffic.
  name: Hetzner Certificates API
  slug: hetzner-certificates-api
- description: Each Datacenter represents a _virtual_ Datacenter which may consist of possibly many physical Datacenters. A physical Datacenter is where [Servers](#tag/servers) are hosted. See the [Hetzner Locations
  name: Hetzner Data Centers API
  slug: hetzner-data-centers-api
- description: The Firewall Actions API from Hetzner — 7 operation(s) for firewall actions.
  name: Hetzner Firewall Actions API
  slug: hetzner-firewall-actions-api
- description: Firewalls can limit the network access to or from your resources. - When applying a firewall with no `in` rule all inbound traffic will be dropped. The default for `in` is `DROP`. - When applying a fi
  name: Hetzner Firewalls API
  slug: hetzner-firewalls-api
- description: The Floating IP Actions API from Hetzner — 8 operation(s) for floating ip actions.
  name: Hetzner Floating IP Actions API
  slug: hetzner-floating-ip-actions-api
- description: 'Floating IPs help you to create highly available setups. You can assign a Floating IP to any Server. The Server can then use this IP. You can reassign it to a different Server at any time, or you can '
  name: Hetzner Floating IPs API
  slug: hetzner-floating-ips-api
- description: The Image Actions API from Hetzner — 5 operation(s) for image actions.
  name: Hetzner Image Actions API
  slug: hetzner-image-actions-api
- description: 'Images are blueprints for your VM disks. They can be of different types: ### System Images Distribution Images maintained by us, e.g. “Ubuntu 20.04” ### Snapshot Images Maintained by you, for example '
  name: Hetzner Images API
  slug: hetzner-images-api
- description: ISOs are read-only Images of DVDs. While we recommend using our Image functionality to install your Servers we also provide some stock ISOs so you can install more exotic operating systems by yourself
  name: Hetzner ISOs API
  slug: hetzner-isos-api
- description: The Load Balancer Actions API from Hetzner — 17 operation(s) for load balancer actions.
  name: Hetzner Load Balancer Actions API
  slug: hetzner-load-balancer-actions-api
- description: 'Load Balancer types define kinds of Load Balancers offered. Each type has an hourly and a monthly cost. You will pay whichever amount is lower for your usage of this specific Load Balancer. Costs may '
  name: Hetzner Load Balancer Types API
  slug: hetzner-load-balancer-types-api
- description: The Load Balancers API from Hetzner — 3 operation(s) for load balancers.
  name: Hetzner Load Balancers API
  slug: hetzner-load-balancers-api
- description: Datacenters are organized by Locations. Datacenters in the same Location are connected with very low latency links.
  name: Hetzner Locations API
  slug: hetzner-locations-api
- description: The Network Actions API from Hetzner — 10 operation(s) for network actions.
  name: Hetzner Network Actions API
  slug: hetzner-network-actions-api
- description: Networks is a private networks feature. These Networks are optional and they coexist with the public network that every Server has by default. They allow Servers to talk to each other over a dedicated
  name: Hetzner Networks API
  slug: hetzner-networks-api
- description: Placement groups are used to influence the location of interdependent virtual servers in our data centers. The distribution of the different servers within a group is based on a pattern specified in t
  name: Hetzner Placement Groups API
  slug: hetzner-placement-groups-api
- description: Returns prices for resources.
  name: Hetzner Pricing API
  slug: hetzner-pricing-api
- description: The Primary IP Actions API from Hetzner — 8 operation(s) for primary ip actions.
  name: Hetzner Primary IP Actions API
  slug: hetzner-primary-ip-actions-api
- description: Primary IPs help you to create more flexible networking setups. You can assign at most one Primary IP of type `ipv4` and one of type `ipv6` per Server. This Server then uses these IPs. You can only un
  name: Hetzner Primary IPs API
  slug: hetzner-primary-ips-api
- description: The Server Actions API from Hetzner — 27 operation(s) for server actions.
  name: Hetzner Server Actions API
  slug: hetzner-server-actions-api
- description: Server types define kinds of Servers offered. Each type has an hourly and a monthly cost. You will pay whichever cost is lower for your usage of this specific Server. Costs may differ between Location
  name: Hetzner Server Types API
  slug: hetzner-server-types-api
- description: Servers are virtual machines that can be provisioned.
  name: Hetzner Servers API
  slug: hetzner-servers-api
- description: SSH keys are public keys you provide to the cloud system. They can be injected into Servers at creation time. We highly recommend that you use keys instead of passwords to manage your Servers.
  name: Hetzner SSH Keys API
  slug: hetzner-ssh-keys-api
- description: The Volume Actions API from Hetzner — 8 operation(s) for volume actions.
  name: Hetzner Volume Actions API
  slug: hetzner-volume-actions-api
- description: A Volume is a highly-available, scalable, and SSD-based block storage for Servers. Pricing for Volumes depends on the Volume size and Location, not the actual used storage. Please see [Hetzner Docs](h
  name: Hetzner Volumes API
  slug: hetzner-volumes-api
- description: The Zone Actions API from Hetzner — 8 operation(s) for zone actions.
  name: Hetzner Zone Actions API
  slug: hetzner-zone-actions-api
- description: The Zone RRSet Actions API from Hetzner — 6 operation(s) for zone rrset actions.
  name: Hetzner Zone RRSet Actions API
  slug: hetzner-zone-rrset-actions-api
- description: 'This API operates on resource record sets (RRSets) instead of individual resource records (RRs). An RRSet is identified by a name and type. For example, the two RRs - (name: `@`, type: `MX`, value: `1'
  name: Hetzner Zone RRSets API
  slug: hetzner-zone-rrsets-api
- description: A Zone represents a [Domain Name System (DNS) zone](https://wikipedia.org/wiki/DNS_zone) managed by Hetzner authoritative nameservers. Please see [Hetzner Docs](https://docs.hetzner.com/dns-console/dn
  name: Hetzner Zones API
  slug: hetzner-zones-api
artifact_total: 40
collections:
- collection_type: open
  name: Hetzner Cloud API
  slug: open-hetzner
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hetzner-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hetzner-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hetzner-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hetzner-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hetzneronline
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hetzner-online
- group: company
  title: ''
  type: Website
  url: https://www.hetzner.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hetzner.com/
- group: start
  title: ''
  type: Signup
  url: https://accounts.hetzner.com/signUp
- group: start
  title: ''
  type: Login
  url: https://accounts.hetzner.com/login
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hetzner.com/
- group: operate
  title: ''
  type: Support
  url: https://www.hetzner.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hetzner.com/cloud
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hetzner.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hetzner.com/legal/terms-and-conditions
- group: company
  title: ''
  type: Blog
  url: https://www.hetzner.com/blog/
created: '2025-02-09'
description: Hetzner Online is a German hosting provider offering cloud servers, dedicated servers, and domain services. Hetzner provides a Cloud API for programmatic management of cloud resources, as well as a DNS API for managing DNS zones and records.
finops:
- name: Hetzner Finops
  service_category: API
  slug: hetzner-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hetzner.png
layout: provider
modified: '2026-05-19'
name: Hetzner
nav: Providers
network: true
overview: 'Hetzner publishes 31 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Certificate Actions API, Certificates API, and 28 more. Tagged areas include Cloud Hosting, DNS, Infrastructure, and Servers.


  Hetzner''s developer surface includes authentication, documentation, signup flow, support, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Hetzner Plans Pricing
  plan_count: 3
  slug: hetzner-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 5
  name: Hetzner Rate Limits
  slug: hetzner-rate-limits
score:
  band: developing
  composite: 49.4
  delta: -1.7
  facets:
    commercial_clarity: 84.2
    contract_quality: 55.9
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 31
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hetzner/refs/heads/main/screenshots/hetzner-2026-06-20T182656.png
security:
- kind: authentication
  name: Hetzner Authentication
  slug: hetzner-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hetzner Domain Security
  slug: hetzner-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hetzner Vulnerability Disclosure
  slug: hetzner-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: hetzner
tags:
- Cloud Hosting
- DNS
- Infrastructure
- Servers
website: https://www.hetzner.com/
---
