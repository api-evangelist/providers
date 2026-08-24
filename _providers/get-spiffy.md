---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/get-spiffy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getspiffy.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.getspiffy.com/
- group: operate
  title: ''
  type: Support
  url: https://www.getspiffy.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getspiffy.com/spiffy-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getspiffy.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/get-spiffy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getspiffy.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/get-spiffy-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/get-spiffy-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/get-spiffy-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/get-spiffy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/get-spiffy-rate-limits.yml
coverage:
  checked: '2026-08-21'
  detail: Get Spiffy sells a turnkey dealer mobile-service program (software plus vans, devices and training) with no developer program of any kind — no developer/docs/api subdomain resolves, the company's own llms.txt enumerates every key page and names no API, and the only API that exists is the undocumented, credentialed Fleet portal backend at my.getspiffy.com/api/fleet/v1/ found in Spiffy's public JavaScript bundle, which returns 404 for every spec path.
  evidence:
  - status: 200
    url: https://www.getspiffy.com/llms.txt
  - status: 404
    url: https://my.getspiffy.com/api/fleet/v1/
  - status: 404
    url: https://my.getspiffy.com/openapi.json
  - status: 404
    url: https://www.getspiffy.com/.well-known/api-catalog
  - status: 200
    url: https://github.com/get-spiffy
  reason: no-developer-program
  state: none
created: '2026-08-21'
description: Get Spiffy, Inc. (Spiffy) is a B2B SaaS and operations company that sells a mobile service operating system to franchise car dealerships. Its core product, Mobile 360, is an enterprise platform covering scheduling, dispatch, route optimization, technician management, digital vehicle inspections, DMS integration and customer communication, sold as a turnkey program alongside van upfits, connected devices (Easy Tread, Easy Flow, Smart Tumbler) and technician training. Spiffy also runs fleet and Amazon DSP service programs, and operates a customer booking portal and a fleet portal. Founded in 2014 and headquartered in Apex, North Carolina, the company has raised more than $90M and reports over 4 million completed services, with OEM work including a Hyundai Motor America pilot. Spiffy publishes no public developer program, API reference or machine-readable specification; its Fleet portal API is an internal, credentialed surface with no published contract.
image: https://2762956.fs1.hubspotusercontent-na1.net/hubfs/2762956/Spiffy-Logo-Master.svg
layout: provider
modified: '2026-08-21'
name: Spiffy
nav: Providers
network: true
overview: 'Spiffy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Mobile Vehicle Service, Dealership Software, and Fleet Management.


  Spiffy''s developer surface includes engineering blog, support, and 11 more developer resources.'
plans:
- name: Get Spiffy Plans Pricing
  plan_count: 0
  slug: get-spiffy-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Get Spiffy Rate Limits
  slug: get-spiffy-rate-limits
score:
  band: emerging
  composite: 13.8
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 18.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: domain-security
  name: Get Spiffy Domain Security
  slug: get-spiffy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: get-spiffy
tags:
- Company
- Automotive
- Mobile Vehicle Service
- Dealership Software
- Fleet Management
- Field Service Management
- Vehicle Inspection
- Scheduling and Dispatch
- B2B SaaS
website: https://www.getspiffy.com/
---
