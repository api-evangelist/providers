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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 149
  human_in_the_loop: 17
  name: Hashicorp Agentic Access
  operation_count: 264
  slug: hashicorp-agentic-access
  summary_line: 264 operations · 149 acting · 17 human-in-the-loop
api_count: 1
apis:
- description: Terraform is an infrastructure as code tool that lets you build, change, and version infrastructure safely and efficiently.
  name: HashiCorp Terraform
  slug: hashicorp-terraform
- description: A simple and flexible scheduler and orchestrator to deploy and manage containers and non-containerized applications across on-prem and clouds.
  name: HashiCorp Nomad
  slug: hashicorp-nomad
- description: Consul is a service networking solution that enables teams to manage secure network connectivity between services and across multi-cloud environments.
  name: HashiCorp Consul
  slug: hashicorp-consul
- description: Securely access any system from anywhere based on user identity.
  name: HashiCorp Boundary
  slug: hashicorp-boundary
- description: Vagrant is the command line utility for managing the lifecycle of virtual machines for isolated, consistent development environments.
  name: HashiCorp Vagrant
  slug: hashicorp-vagrant
- description: The Auth API from HashiCorp — 17 operation(s) for auth.
  name: HashiCorp Auth API
  slug: hashicorp-auth-api
- description: The Identity API from HashiCorp — 49 operation(s) for identity.
  name: HashiCorp Identity API
  slug: hashicorp-identity-api
- description: The Secrets API from HashiCorp — 7 operation(s) for secrets.
  name: HashiCorp Secrets API
  slug: hashicorp-secrets-api
- description: The System API from HashiCorp — 107 operation(s) for system.
  name: HashiCorp System API
  slug: hashicorp-system-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HashiCorp Vault Auth API
  slug: open-hashicorp-auth-api
- collection_type: open
  name: HashiCorp Vault Auth Identity API
  slug: open-hashicorp-identity-api
- collection_type: open
  name: HashiCorp Vault Auth Secrets API
  slug: open-hashicorp-secrets-api
- collection_type: open
  name: HashiCorp Vault Auth System API
  slug: open-hashicorp-system-api
- collection_type: open
  name: HashiCorp Vault API
  slug: open-hashicorp-vault
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/ibm/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hashicorp-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hashicorp-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hashicorp
- group: start
  title: ''
  type: Portal
  url: https://developer.hashicorp.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.hashicorp.com/tutorials
- group: operate
  title: ''
  type: Support
  url: https://support.hashicorp.com/hc/en-us
- group: operate
  title: ''
  type: Community
  url: https://discuss.hashicorp.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hashicorp.com/
- group: company
  title: ''
  type: Blog
  url: https://www.hashicorp.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hashicorp.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hashicorp.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hashicorp
created: '2024-02-01'
description: HashiCorp is the infrastructure cloud company, helping organizations automate multi-cloud and hybrid environments with Infrastructure Lifecycle Management and Security Lifecycle Management. Their suite of products includes Vault, Terraform, Nomad, Consul, Vagrant, Boundary, and Packer.
finops:
- name: Hashicorp Finops
  service_category: Infrastructure / DevOps Platform
  slug: hashicorp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hashicorp.png
json_structures:
- name: Hashicorp Structure
  property_count: 0
  slug: hashicorp-structure
layout: provider
modified: '2026-08-21'
name: HashiCorp
nav: Providers
network: true
overview: 'HashiCorp publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Identity API, Secrets API, and 1 more. Tagged areas include Cloud, DevOps, Infrastructure, and Platform.


  HashiCorp''s developer surface includes developer portal, getting-started guide, support, engineering blog, and 9 more developer resources.'
plans:
- name: Hashicorp Plans Pricing
  plan_count: 6
  slug: hashicorp-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Hashicorp Rate Limits
  slug: hashicorp-rate-limits
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 35.3
    developer_ergonomics: 36.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 29.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hashicorp/refs/heads/main/screenshots/hashicorp-2026-06-20T182530.png
security:
- kind: domain-security
  name: Hashicorp Domain Security
  slug: hashicorp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hashicorp
tags:
- Cloud
- DevOps
- Infrastructure
- Platform
website: https://developer.hashicorp.com/
---
