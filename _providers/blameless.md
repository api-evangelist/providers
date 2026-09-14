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
  - '{''url'': ''https://www.blameless.com'', ''status'': 302, ''note'': ''declared website redirects to https://firehydrant.com/ — a different registrable domain (blameless.com -> firehydrant.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
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
overview: 'Blameless publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AIOps, SRE, Incident Management, Reliability, and SLO.


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
- SLO
- Retrospectives
- On-Call
- DevOps
website: https://www.blameless.com
---
