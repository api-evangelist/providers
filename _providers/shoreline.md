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
api_count: 1
apis:
- description: The Shoreline cluster API — the backend that alarms, actions, bots, runbooks, notebooks, resources, files, integrations and principals are managed against. The endpoint was always customer-specific (t
  name: Shoreline
  slug: shoreline
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shoreline-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shoreline-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/shoreline-packages.yml
- group: agent
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
modified: '2026-08-29'
name: Shoreline
nav: Providers
network: true
overview: Shoreline publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AIOps, Automation, Incident Response, Site Reliability Engineering, and Cloud Operations.
plans:
- name: Shoreline Plans Pricing
  plan_count: 0
  slug: shoreline-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Shoreline Rate Limits
  slug: shoreline-rate-limits
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
---
