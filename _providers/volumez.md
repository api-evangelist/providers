---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 28.9
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://api.dev.volumez.com
  baseurl_source: declared
  description: REST API for the Volumez orchestrator — create and modify volumes from declarative policies, plan and auto-provision infrastructure, manage media and nodes, take and roll back snapshots, attach volume
  name: Volumez Orchestrator API
  slug: volumez-orchestrator-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://volumez.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VolumezTech
- group: operate
  title: ''
  type: Support
  url: https://volumez.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://volumez.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://volumez.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://volumez.statuspage.io/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/volumez-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/volumez-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/volumez-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/volumez-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/volumez-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/volumez-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/volumez-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/volumez-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/volumez-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/volumez-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/volumez-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/volumez-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/volumez-mcp.yml
created: '2026-09-04'
description: Volumez is a SaaS data-infrastructure-as-a-service (DIaaS) company, founded in 2020, headquartered in the San Francisco Bay Area with R&D in Tel Aviv, that composes block and file storage directly out of cloud instance-local NVMe media instead of a storage controller. Its orchestrator exposes a declarative REST API — volumes, policies, media, nodes, networks, snapshots, attachments, exports, connectivities, capacity groups, jobs and tenant/user administration — so applications can request precise IO characteristics (IOPS, latency, resiliency) the same way they request CPU and memory. The platform ships a Kubernetes CSI driver (Helm chart), Terraform and Bicep infrastructure modules for AWS, Azure and OCI, and a generated Go REST client. Through 2026 the company repositioned its public site around enterprise agentic-AI infrastructure and retired its public developer portal, API host and status page; the machine-readable contract now lives only in its own GitHub organization.
image: https://cdn.prod.website-files.com/697f0ed00fa3efb03f6269c4/698dc3c03de73edbaf042a8a_Share%20thumbnail%20(1).jpg
layout: provider
modified: '2026-09-04'
name: Volumez
nav: Providers
network: true
overview: 'Volumez publishes 1 API on the [APIs.io](https://apis.io/) network: Orchestrator API. Tagged areas include Storage, Block Storage, Data Infrastructure, Cloud Infrastructure, and Kubernetes.


  Volumez''s developer surface includes support, changelog, authentication, and 17 more developer resources.'
plans:
- name: Volumez Plans Pricing
  plan_count: 0
  slug: volumez-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Volumez Rate Limits
  slug: volumez-rate-limits
score:
  band: thin
  composite: 35.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 42.2
    developer_ergonomics: 35.1
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 36.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: authentication
  name: Volumez Authentication
  slug: volumez-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Volumez Domain Security
  slug: volumez-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: volumez
tags:
- Storage
- Block Storage
- Data Infrastructure
- Cloud Infrastructure
- Kubernetes
- Container Storage Interface
- AI Infrastructure
- Snapshots
- Infrastructure as Code
- DIaaS
website: https://volumez.com/
---
