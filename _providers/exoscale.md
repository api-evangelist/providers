---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 220
  human_in_the_loop: 25
  name: Exoscale Agentic Access
  operation_count: 342
  slug: exoscale-agentic-access
  summary_line: 342 operations · 220 acting · 25 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: The ai-api-key API from Exoscale — 3 operation(s) for ai-api-key.
  name: Exoscale AI API Key API
  slug: exoscale-ai-api-key-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: Anti-affinity groups let you define placement constraints for your Compute instances.
  name: Exoscale Anti Affinity Group API
  slug: exoscale-anti-affinity-group-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: API keys are credentials for programmatic access to Exoscale APIs and services.
  name: Exoscale API Key API
  slug: exoscale-api-key-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: The ccm API from Exoscale — 1 operation(s) for ccm.
  name: Exoscale Ccm API
  slug: exoscale-ccm-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: Clusters are managed Kubernetes control planes.
  name: Exoscale Cluster API
  slug: exoscale-cluster-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: Host anything from simple applications to complex architectures. Start a compute instance in seconds and scale as your infrastructure grows.
  name: Exoscale Compute API
  slug: exoscale-compute-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: A suite of cryptographic primitives offered by the Exoscale KMS.
  name: Exoscale Crypto API
  slug: exoscale-crypto-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: Databases as a Service (DBaaS) provides scalable and fully-managed database solutions with high availability and performance backed by Exoscale's Compute and Storage services.
  name: Exoscale Dbaas API
  slug: exoscale-dbaas-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: Deploy Target lets you spin up Compute instances on dedicated hypervisors.
  name: Exoscale Deploy Target API
  slug: exoscale-deploy-target-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: Deployments are loaded model instances ready for inference.
  name: Exoscale Deployment API
  slug: exoscale-deployment-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: DNS zone management.
  name: Exoscale Domain API
  slug: exoscale-domain-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: Elastic IPs are additional public IPv4/6 addresses that can be attached to Compute instances, with optional healthcheck support.
  name: Exoscale Elastic Ip API
  slug: exoscale-elastic-ip-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: Events form the basis of the Exoscale audit-trail, a mechanism to query past events performing mutations on resources which happened on an organization.
  name: Exoscale Event API
  slug: exoscale-event-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: Instances are the virtual machines at the core of the Exoscale Compute service.
  name: Exoscale Instance API
  slug: exoscale-instance-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: Instance Pools is an Exoscale service allowing users to provision managed groups of identical Compute instances automatically.
  name: Exoscale Instance Pool API
  slug: exoscale-instance-pool-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: An Instance Type is a resource describing the amount of CPU, RAM and GPUs allocated to a Compute instance.
  name: Exoscale Instance Type API
  slug: exoscale-instance-type-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: Operations for KMS Key lifecycle management.
  name: Exoscale Kms Key API
  slug: exoscale-kms-key-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: Lifecycle of AI Models.
  name: Exoscale Model API
  slug: exoscale-model-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: A Network Load Balancer (NLB) is a Layer 4 (TCP/UDP) load balancer that distributes incoming traffic to Compute instances managed by an Instance Pool.
  name: Exoscale Network Load Balancer API
  slug: exoscale-network-load-balancer-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: Nodepools are groups of compute instances managed by SKS, serving as worker nodes in your Kubernetes cluster.
  name: Exoscale Nodepool API
  slug: exoscale-nodepool-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: Nodepool templates are Exoscale-managed instance templates for SKS worker nodes.
  name: Exoscale Nodepool Template API
  slug: exoscale-nodepool-template-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: Operations describe the current state of an asynchronous operation.
  name: Exoscale Operation API
  slug: exoscale-operation-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: The organization API from Exoscale — 3 operation(s) for organization.
  name: Exoscale Organization API
  slug: exoscale-organization-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: The Organization Policy is an IAM policy that applies as a first layer across your entire Exoscale organization.
  name: Exoscale Organization Policy API
  slug: exoscale-organization-policy-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: Private Network provides private L2 networking functionality between Compute instances.
  name: Exoscale Private Network API
  slug: exoscale-private-network-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: The quotas API from Exoscale — 2 operation(s) for quotas.
  name: Exoscale Quotas API
  slug: exoscale-quotas-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: DNS zone records management.
  name: Exoscale Record API
  slug: exoscale-record-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: Reverse DNS lets you record PTR records for Compute instance public IP addresses or Elastic IPs.
  name: Exoscale Reverse Dns API
  slug: exoscale-reverse-dns-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: IAM roles lets you define logical sets of policies to grant to users and API keys.
  name: Exoscale Role API
  slug: exoscale-role-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: Security Groups are groups of firewall rules that regulate network traffic to and from your Compute instances.
  name: Exoscale Security Group API
  slug: exoscale-security-group-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: Snapshots provide a way to get point-in-time recovery for your Compute instance.
  name: Exoscale Snapshot API
  slug: exoscale-snapshot-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: Exoscale Simple Object Storage (SOS) is an S3-compatible object storage service.
  name: Exoscale Sos API
  slug: exoscale-sos-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: SSH Keypairs
  name: Exoscale Ssh Key API
  slug: exoscale-ssh-key-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: Templates contain the OS and the initial setup of a Compute instance.
  name: Exoscale Template API
  slug: exoscale-template-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: IAM users map to humans empowered with access to Exoscale resources.
  name: Exoscale User API
  slug: exoscale-user-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: A Zone represents an independent datacenter in which Exoscale infrastructure is deployed into.
  name: Exoscale Zone API
  slug: exoscale-zone-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: The Environmental Impact API from Exoscale — 2 operation(s) for environmental impact.
  name: Exoscale Environmental Impact API
  slug: exoscale-environmental-impact-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: '[BETA] Create and manipulate VPCs'
  name: Exoscale Vpc Management API
  slug: exoscale-vpc-management-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: '[BETA] Create and manipulate routing rules'
  name: Exoscale Vpc Route API
  slug: exoscale-vpc-route-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: '[BETA] Configure VPC subnets and attach instances to them'
  name: Exoscale Vpc Subnet API
  slug: exoscale-vpc-subnet-api
- baseURL: https://api-ch-gva-2.exoscale.com/v2
  baseurl_source: declared
  description: Exoscale's Block Storage offers persistent externally attached volumes for your Compute instances.
  name: Exoscale Blockstorage API
  slug: exoscale-blockstorage-api
artifact_total: 87
collections:
- collection_type: open
  name: Exoscale ai-api-key API
  slug: open-exoscale-ai-api-key-api
- collection_type: open
  name: Exoscale ai-api-key anti-affinity-group API
  slug: open-exoscale-anti-affinity-group-api
- collection_type: open
  name: Exoscale ai api-key API
  slug: open-exoscale-api-key-api
- collection_type: open
  name: Exoscale ai-api-key block-storage API
  slug: open-exoscale-block-storage-api
- collection_type: open
  name: Exoscale ai-api-key ccm API
  slug: open-exoscale-ccm-api
- collection_type: open
  name: Exoscale ai-api-key cluster API
  slug: open-exoscale-cluster-api
- collection_type: open
  name: Exoscale ai-api-key compute API
  slug: open-exoscale-compute-api
- collection_type: open
  name: Exoscale ai-api-key crypto API
  slug: open-exoscale-crypto-api
- collection_type: open
  name: Exoscale ai-api-key dbaas API
  slug: open-exoscale-dbaas-api
- collection_type: open
  name: Exoscale ai-api-key deploy-target API
  slug: open-exoscale-deploy-target-api
- collection_type: open
  name: Exoscale ai-api-key deployment API
  slug: open-exoscale-deployment-api
- collection_type: open
  name: Exoscale ai-api-key domain API
  slug: open-exoscale-domain-api
- collection_type: open
  name: Exoscale ai-api-key elastic-ip API
  slug: open-exoscale-elastic-ip-api
- collection_type: open
  name: Exoscale ai-api-key event API
  slug: open-exoscale-event-api
- collection_type: open
  name: Exoscale ai-api-key instance API
  slug: open-exoscale-instance-api
- collection_type: open
  name: Exoscale ai-api-key instance-pool API
  slug: open-exoscale-instance-pool-api
- collection_type: open
  name: Exoscale ai-api-key instance-type API
  slug: open-exoscale-instance-type-api
- collection_type: open
  name: Exoscale ai-api-key kms-key API
  slug: open-exoscale-kms-key-api
- collection_type: open
  name: Exoscale ai-api-key model API
  slug: open-exoscale-model-api
- collection_type: open
  name: Exoscale ai-api-key network-load-balancer API
  slug: open-exoscale-network-load-balancer-api
- collection_type: open
  name: Exoscale ai-api-key nodepool API
  slug: open-exoscale-nodepool-api
- collection_type: open
  name: Exoscale ai-api-key nodepool-template API
  slug: open-exoscale-nodepool-template-api
- collection_type: open
  name: Exoscale ai-api-key operation API
  slug: open-exoscale-operation-api
- collection_type: open
  name: Exoscale ai-api-key organization API
  slug: open-exoscale-organization-api
- collection_type: open
  name: Exoscale ai-api-key organization-policy API
  slug: open-exoscale-organization-policy-api
- collection_type: open
  name: Exoscale ai-api-key private-network API
  slug: open-exoscale-private-network-api
- collection_type: open
  name: Exoscale ai-api-key quotas API
  slug: open-exoscale-quotas-api
- collection_type: open
  name: Exoscale ai-api-key record API
  slug: open-exoscale-record-api
- collection_type: open
  name: Exoscale ai-api-key reverse-dns API
  slug: open-exoscale-reverse-dns-api
- collection_type: open
  name: Exoscale ai-api-key role API
  slug: open-exoscale-role-api
- collection_type: open
  name: Exoscale ai-api-key security-group API
  slug: open-exoscale-security-group-api
- collection_type: open
  name: Exoscale ai-api-key snapshot API
  slug: open-exoscale-snapshot-api
- collection_type: open
  name: Exoscale ai-api-key sos API
  slug: open-exoscale-sos-api
- collection_type: open
  name: Exoscale ai-api-key ssh-key API
  slug: open-exoscale-ssh-key-api
- collection_type: open
  name: Exoscale ai-api-key template API
  slug: open-exoscale-template-api
- collection_type: open
  name: Exoscale ai-api-key user API
  slug: open-exoscale-user-api
- collection_type: open
  name: Exoscale ai-api-key zone API
  slug: open-exoscale-zone-api
- collection_type: open
  name: Exoscale API
  slug: open-exoscale
common:
- group: operate
  href: https://artifacts.apis.io/exoscale/rate-limits/exoscale-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/exoscale-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/exoscale/finops/exoscale-finops.yml
  title: ''
  type: FinOps
  url: finops/exoscale-finops.yml
- group: commercial
  href: https://artifacts.apis.io/exoscale/plans/exoscale-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/exoscale-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/exoscale/capabilities/exoscale-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/exoscale-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/exoscale/agentic-access/exoscale-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/exoscale-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/exoscale/security/exoscale-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/exoscale-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/exoscale/security/exoscale-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/exoscale-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/exoscale/security/exoscale-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/exoscale-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/exoscale
- group: company
  title: ''
  type: Website
  url: https://www.exoscale.com
- group: docs
  title: ''
  type: Documentation
  url: https://community.exoscale.com/documentation/
- group: start
  title: ''
  type: Portal
  url: https://portal.exoscale.com/
- group: start
  title: ''
  type: Signup
  url: https://portal.exoscale.com/register
- group: commercial
  title: ''
  type: Pricing
  url: https://www.exoscale.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.exoscale.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.exoscale.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.exoscalestatus.com/
- group: company
  title: ''
  type: Blog
  url: https://www.exoscale.com/syslog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/exoscale
- group: operate
  title: ''
  type: Support
  url: https://portal.exoscale.com/tickets
created: '2025-01-07'
description: Exoscale is a Swiss cloud infrastructure provider offering secure, reliable, and scalable cloud solutions to businesses of all sizes. Their services include virtual machines, object storage, networking, security, Kubernetes (SKS), Database as a Service (DBaaS), and IAM. Data centers are located in Switzerland, Austria, Germany, and Bulgaria, providing data sovereignty and compliance with European data protection regulations.
finops:
- has_sources: true
  method: derived
  name: Exoscale Finops
  primary_unit: gib.hour
  service_category: ''
  slug: exoscale-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/exoscale.png
layout: provider
modified: '2026-05-19'
name: Exoscale
nav: Providers
network: true
overview: 'Exoscale publishes 41 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI API Key API, Anti Affinity Group API, API Key API, and 38 more. Tagged areas include Cloud, Infrastructure, Compute, Storage, and Kubernetes.


  The Exoscale catalog on APIs.io includes 1 Spectral governance ruleset.


  Exoscale''s developer surface includes documentation, developer portal, signup flow, pricing, engineering blog, support, and 14 more developer resources.'
plans:
- name: Exoscale Plans Pricing
  plan_count: 10
  slug: exoscale-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Exoscale Rate Limits
  slug: exoscale-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Exoscale API Rules
  rule_count: 58
  severity_counts:
    error: 46
    hint: 0
    info: 6
    warn: 6
  slug: exoscale-rules
score:
  band: developing
  composite: 46.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 59.5
    catalog_earned_first_party: 12.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 13.6
    contract_quality: 45.1
    developer_ergonomics: 21.4
    discoverability: 66.1
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 79
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/exoscale/exoscale-2026-08-17T123426.png
security:
- kind: domain-security
  name: Exoscale Domain Security
  slug: exoscale-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Exoscale Vulnerability Disclosure
  slug: exoscale-vulnerability-disclosure
  summary_line: Intigriti
- kind: trust-center
  name: Exoscale Trust Center
  slug: exoscale-trust-center
  summary_line: ISO 27001, PCI DSS, HIPAA, FedRAMP, GDPR
slug: exoscale
tags:
- Cloud
- Infrastructure
- Compute
- Storage
- Kubernetes
- Database-as-a-Service
- Europe
website: https://www.exoscale.com
---
