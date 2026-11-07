---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - finops
  - authentication
  - scopes
  - rate-limits
  - security
  - '{''url'': ''https://www.blameless.com'', ''status'': 302, ''note'': ''declared website redirects to https://firehydrant.com/ — a different registrable domain (blameless.com -> firehydrant.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The Blameless platform API — incidents, incident types, severities, roles, SLOs, SLIs and error budgets — served per tenant at https://{instance}.blameless.io/api/v1 with Auth0 client-credentials bear
  name: Blameless
  slug: blameless
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/blameless/plans/blameless-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blameless-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/blameless/rate-limits/blameless-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/blameless-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/blameless/finops/blameless-finops.yml
  title: ''
  type: FinOps
  url: finops/blameless-finops.yml
- group: auth
  href: https://artifacts.apis.io/blameless/security/blameless-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blameless-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blamelesshq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/blameless
- group: company
  title: ''
  type: Website
  url: https://www.blameless.com
- group: build
  href: https://artifacts.apis.io/blameless/packages/blameless-packages.yml
  title: ''
  type: Packages
  url: packages/blameless-packages.yml
- group: build
  href: https://artifacts.apis.io/blameless/cli/blameless-cli.yml
  title: ''
  type: CLI
  url: cli/blameless-cli.yml
- group: auth
  href: https://artifacts.apis.io/blameless/authentication/blameless-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blameless-authentication.yml
- group: auth
  href: https://artifacts.apis.io/blameless/scopes/blameless-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/blameless-scopes.yml
- group: design
  href: https://artifacts.apis.io/blameless/conformance/blameless-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blameless-conformance.yml
- group: design
  href: https://artifacts.apis.io/blameless/lifecycle/blameless-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/blameless-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/blameless/well-known/blameless-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blameless-well-known.yml
- group: agent
  href: https://artifacts.apis.io/blameless/llms/blameless-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blameless-llms.txt
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/firehydrant/
coverage:
  checked: '2026-08-29'
  detail: Blameless was acquired by FireHydrant on 2024-08-21 and fully absorbed — every path on www.blameless.com now 302s to firehydrant.com, and docs.blameless.com plus the *.blameless.io tenant domain that served the API have no DNS records at all, so the tenant-templated /api/v1 surface is unreachable; what this profile documents is the residue still online (the blamelesshq GitHub org, two npm packages, a Terraform Registry provider, and a live Auth0 identity tenant).
  evidence:
  - status: 302
    url: https://www.blameless.com/pricing
  - status: 0
    url: https://docs.blameless.com/api/api-reference/get-incident/
  - status: 0
    url: https://api.blameless.io/
  - status: 200
    url: https://blamelesshq.auth0.com/.well-known/openid-configuration
  - status: 200
    url: https://github.com/blamelesshq
  reason: defunct
  state: none
created: '2026-03-27'
description: Blameless was an SRE and incident management platform for reliability engineering teams, covering the full incident lifecycle — detection and response, on-call and severity workflows, blameless retrospectives, and SLOs with error budgets. It sold to enterprise reliability organizations including CrowdStrike, Palo Alto Networks, VMware and Ticketmaster. FireHydrant acquired Blameless on 2024-08-21 and has since absorbed the product; as of 2026-08-29 blameless.com redirects to firehydrant.com, docs.blameless.com and the *.blameless.io tenant hosts no longer resolve, and the tenant-templated REST/RPC API at https://{instance}.blameless.io/api/v1 is retired. What survives is the public blamelesshq GitHub organization, two npm packages, a Terraform Registry provider, and a live Auth0 identity tenant.
finops:
- has_sources: false
  method: generated
  name: Blameless Finops
  primary_unit: request
  service_category: API
  slug: blameless-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blameless.png
layout: provider
modified: '2026-08-29'
name: Blameless
nav: Providers
network: true
overview: 'Blameless is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AIOps, SRE, Incident Management, Reliability, and SLO.


  Blameless'' developer surface includes CLI, authentication, and 14 more developer resources.'
plans:
- name: Blameless Plans Pricing
  plan_count: 0
  slug: blameless-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Blameless Rate Limits
  slug: blameless-rate-limits
scopes:
- name: Blameless Scopes
  scope_count: 14
  slug: blameless-scopes
  summary_line: 14 scopes
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 2.6
  previous_composite: 13.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/blameless/blameless-2026-06-20T173342.png
security:
- kind: authentication
  name: Blameless Authentication
  slug: blameless-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Blameless Domain Security
  slug: blameless-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blameless
tags:
- AIOps
- SRE
- Incident Management
- Reliability
- SLO
- Retrospectives
- On-Call
- DevOps
website: https://www.blameless.com
---
