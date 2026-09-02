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
    agent_skills: true
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Infracost Agentic Access
  operation_count: 2
  slug: infracost-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: The Breakdown API from Infracost — 1 operation(s) for breakdown.
  name: Infracost Breakdown API
  slug: infracost-breakdown-api
- description: The Diff API from Infracost — 1 operation(s) for diff.
  name: Infracost Diff API
  slug: infracost-diff-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Infracost Cloud Pricing Breakdown API
  slug: open-infracost-breakdown-api
- collection_type: open
  name: Infracost Cloud Pricing Breakdown Diff API
  slug: open-infracost-diff-api
- collection_type: open
  name: Infracost Cloud Pricing API
  slug: open-infracost
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/infracost-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/infracost-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infracost-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/infracost-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/infracost
- group: company
  title: ''
  type: Website
  url: https://www.infracost.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.infracost.io/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/infracost
- group: operate
  title: ''
  type: Support
  url: https://www.infracost.io/community/
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/infracost/agent-skills
- group: company
  title: ''
  type: Blog
  url: https://www.infracost.io/blog/
created: '2026-03-16'
description: Infracost is a cloud cost estimation tool for Terraform that shows infrastructure cost breakdowns and diffs directly in pull requests. Infracost provides an API for programmatic access to cloud pricing data and cost estimates.
finops:
- name: Infracost Finops
  service_category: API
  slug: infracost-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/infracost.png
layout: provider
modified: '2026-05-19'
name: Infracost
nav: Providers
network: true
overview: 'Infracost publishes 2 APIs on the [APIs.io](https://apis.io/) network: Breakdown API and Diff API. Tagged areas include Cloud Cost, FinOps, Infrastructure, and Terraform.


  Infracost''s developer surface includes authentication, documentation, support, engineering blog, and 7 more developer resources.'
plans:
- name: Infracost Plans Pricing
  plan_count: 3
  slug: infracost-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Infracost Rate Limits
  slug: infracost-rate-limits
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 11
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 57.8
    developer_ergonomics: 42.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 33.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/infracost/refs/heads/main/screenshots/infracost-2026-06-20T183350.png
security:
- kind: authentication
  name: Infracost Authentication
  slug: infracost-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Infracost Domain Security
  slug: infracost-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Infracost Vulnerability Disclosure
  slug: infracost-vulnerability-disclosure
  summary_line: disclosure policy published
skill_count: 4
skills:
- name: iac-generation
  slug: iac-generation
- name: infracost-price-lookup
  slug: infracost-price-lookup
- name: infracost-scan
  slug: infracost-scan
- name: infracost
  slug: infracost
slug: infracost
tags:
- Cloud Cost
- FinOps
- Infrastructure
- Terraform
website: https://www.infracost.io/
---
