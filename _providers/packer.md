---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - '{''url'': ''https://www.packer.io/'', ''status'': 308, ''note'': ''declared website redirects to https://developer.hashicorp.com/packer — a different registrable domain (packer.io -> hashicorp.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Packer Agentic Access
  operation_count: 24
  slug: packer-agentic-access
  summary_line: 24 operations · 13 acting
api_count: 1
apis:
- description: Open-source tool for creating identical machine images for multiple platforms from a single source configuration.
  name: Packer
  slug: packer
- baseURL: https://api.cloud.hashicorp.com
  baseurl_source: declared
  description: The PackerService API from Packer — 13 operation(s) for packerservice.
  name: Packer PackerService API
  slug: packer-packerservice-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HashiCorp Cloud Platform Packer Artifact Registry PackerService API
  slug: open-packer-packerservice-api
- collection_type: open
  name: HashiCorp Cloud Platform Packer Artifact Registry
  slug: open-packer
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/packer/refs/heads/main/plans/packer-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/packer-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/packer/refs/heads/main/rate-limits/packer-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/packer-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/packer/refs/heads/main/finops/packer-finops.yml
  title: ''
  type: FinOps
  url: finops/packer-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/packer/refs/heads/main/capabilities/packer-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/packer-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/packer/refs/heads/main/agentic-access/packer-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/packer-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/packer/refs/heads/main/security/packer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/packer-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/packer/refs/heads/main/authentication/packer-authentication.yml
  title: ''
  type: Authentication
  url: authentication/packer-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.packer.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hashicorp.com/packer/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hashicorp/packer
- group: operate
  title: ''
  type: Community
  url: https://discuss.hashicorp.com/c/packer
created: '2026-03-16'
description: Packer is an open-source tool by HashiCorp for creating identical machine images for multiple platforms from a single source configuration. It automates the creation of pre-configured virtual machine and container images. HCP Packer adds a hosted artifact registry with a REST API for tracking image metadata, versions, channels, and security signals.
finops:
- has_sources: false
  method: generated
  name: Packer Finops
  primary_unit: ''
  service_category: API
  slug: packer-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/packer.png
layout: provider
modified: '2026-05-19'
name: Packer
nav: Providers
network: true
overview: 'Packer publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including PackerService API, and 1 more. Tagged areas include Automation, DevOps, HashiCorp, Image Building, and Infrastructure as Code.


  Packer''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Packer Plans Pricing
  plan_count: 3
  slug: packer-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Packer Rate Limits
  slug: packer-rate-limits
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 43.5
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 26.3
  previous_composite: 29.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/packer/refs/heads/main/screenshots/packer-2026-06-20T191313.png
security:
- kind: authentication
  name: Packer Authentication
  slug: packer-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Packer Domain Security
  slug: packer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: packer
tags:
- Automation
- DevOps
- HashiCorp
- Image Building
- Infrastructure as Code
website: https://www.packer.io/
---
