---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: CloudQix provides API integration and iPaaS services as described on the pricing page.
  name: CloudQix API
  slug: cloudqix-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cloudqix/refs/heads/main/plans/cloudqix-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cloudqix-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudqix/refs/heads/main/llms/cloudqix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudqix-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudqix/refs/heads/main/hosts/cloudqix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudqix-hosts.yml
- group: design
  title: ''
  type: Webhooks
  url: https://staging2.cloudqix.com/resources/glossary/webhook/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://staging2.cloudqix.com/terms-of-use/
- group: start
  title: ''
  type: SignUp
  url: https://staging2.cloudqix.com/sign-up/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://staging2.cloudqix.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://staging2.cloudqix.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://staging2.cloudqix.com/resources/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudqix/refs/heads/main/security/cloudqix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudqix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://staging2.cloudqix.com/
coverage:
  checked: '2026-10-16'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on any discovered host.
  evidence:
  - status: 404
    url: https://api.cloudqix.com/openapi.json
  - status: 404
    url: https://api.cloudqix.com/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: CloudQix provides an iPaaS platform enabling API connections and workflow automation for enterprises. It aims to reduce integration complexity, cost, and time by offering a unified solution for data movement, process orchestration, and application linking across finance, sales, IT, and marketing functions. The platform includes tools for building, managing, and monitoring integrations, with a focus on scalability and security.
image: https://staging2.cloudqix.com/wp-content/uploads/2025/03/node-connector-diagram.jpg
layout: provider
modified: '2026-10-16'
name: CloudQix
nav: Providers
network: true
overview: 'CloudQix is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, iPaaS, Integration, and Automation.


  CloudQix''s developer surface includes signup flow, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Cloudqix Plans Pricing
  plan_count: 1
  slug: cloudqix-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 55.4
    operational_transparency: 7.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cloudqix Domain Security
  slug: cloudqix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cloudqix
tags:
- Company
- iPaaS
- Integration
- Automation
website: https://staging2.cloudqix.com/
---
