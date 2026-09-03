---
access_model:
  confidence: low
  label: Access model not determined — no plans published; product retired after acquisition
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - lifecycle
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The Blameless platform API — incidents, incident types, severities, roles, SLOs, SLIs and error budgets — served per tenant at https://{instance}.blameless.io/api/v1 with Auth0 client-credentials bear
  name: Blameless
  slug: blameless
artifact_total: 8
common:
- group: auth
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
  title: ''
  type: Packages
  url: packages/blameless-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/blameless-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/blameless-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/blameless-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/blameless-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/blameless-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/blameless-well-known.yml
- group: agent
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
- name: Blameless Finops
  service_category: API
  slug: blameless-finops
graphqls:
- description: '> **NOT A BLAMELESS CONTRACT — DO NOT WIRE THIS AS ONE.**'
  name: Blameless SRE GraphQL Schema
  slug: blameless-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blameless.png
layout: provider
modified: '2026-08-29'
name: Blameless
nav: Providers
network: true
overview: 'Blameless publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AIOps, SRE, Incident Management, Reliability, and Service Level Objectives.


  Blameless'' developer surface includes CLI, authentication, and 11 more developer resources.'
plans:
- name: Blameless Plans Pricing
  plan_count: 0
  slug: blameless-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Blameless Rate Limits
  slug: blameless-rate-limits
scopes:
- name: Blameless Scopes
  scope_count: 0
  slug: blameless-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 15
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 37.2
    developer_ergonomics: 19.0
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 23.1
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blameless/refs/heads/main/screenshots/blameless-2026-06-20T173342.png
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
- Service Level Objectives
- Retrospectives
- On-Call
- DevOps
website: https://www.blameless.com
---
