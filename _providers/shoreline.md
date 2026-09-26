---
access_model:
  confidence: high
  label: No pricing published — company absorbed into NVIDIA, website redirects
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: The Shoreline cluster API — the backend that alarms, actions, bots, runbooks, notebooks, resources, files, integrations and principals are managed against. The endpoint was always customer-specific (t
  name: Shoreline
  slug: shoreline
artifact_total: 6
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/shoreline/refs/heads/main/security/shoreline-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shoreline-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shoreline/refs/heads/main/lifecycle/shoreline-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/shoreline-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/shoreline/refs/heads/main/packages/shoreline-packages.yml
  title: ''
  type: Packages
  url: packages/shoreline-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/shoreline/refs/heads/main/llms/shoreline-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shoreline-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shoreline-software
coverage:
  checked: '2026-08-29'
  detail: Shoreline was acquired by NVIDIA in July 2024; shoreline.io and docs.shoreline.io no longer have DNS records at all and www.shoreline.io answers HTTP 301 to https://www.nvidia.com/en-us/ for every path including /pricing, /docs and every /.well-known/ probe, so the entire developer surface is gone rather than hidden.
  evidence:
  - status: 0
    url: https://shoreline.io/
  - status: 0
    url: https://docs.shoreline.io/
  - status: 301
    url: https://www.shoreline.io/
  - status: 301
    url: https://www.shoreline.io/.well-known/api-catalog
  - status: 301
    url: https://www.shoreline.io/pricing
  - status: 404
    url: https://github.com/shorelinesoftware
  - status: 200
    url: https://api.github.com/repos/NVIDIA/terraform-provider-shoreline
  reason: defunct
  state: none
created: '2026-03-27'
description: 'Shoreline Software Inc. built an incident-automation platform for cloud operations, letting SRE and platform teams close the loop between detection and repair: an alarm defines when there is an issue, an action defines the command that fixes it, and a bot binds the two into an auto-remediation loop that runs without a human. The platform also shipped runbooks, notebooks, resource queries, file distribution and an Op query language, driven from a UI, a CLI, notebooks or Terraform. NVIDIA acquired Shoreline in July 2024 and the independent product surface has since been decommissioned — shoreline.io and docs.shoreline.io no longer resolve, and www.shoreline.io redirects in full to nvidia.com. The only first-party developer artifact still published is the Terraform provider, now archived.'
finops:
- name: Shoreline Finops
  service_category: API
  slug: shoreline-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shoreline.png
layout: provider
modified: '2026-09-15'
name: Shoreline
nav: Providers
network: true
overview: Shoreline publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AIOps, Automation, Incident Response, Site Reliability Engineering, and Cloud Operations.
plans:
- name: Shoreline Plans Pricing
  plan_count: 0
  slug: shoreline-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Shoreline Rate Limits
  slug: shoreline-rate-limits
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Shoreline Authentication
  slug: shoreline-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Shoreline Domain Security
  slug: shoreline-domain-security
  summary_line: DMARC
slug: shoreline
tags:
- AIOps
- Automation
- Incident Response
- Site Reliability Engineering
- Cloud Operations
- Remediation
- Observability
- Terraform
- Defunct
---
