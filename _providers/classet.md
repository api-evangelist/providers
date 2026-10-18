---
agent_readiness:
  band: agent-aware
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.1
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 5
asyncapis:
- description: ''
  name: Classet Webhooks
  slug: classet-webhooks
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.classet.ai/terms-of-service
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/classet/refs/heads/main/plans/classet-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/classet-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/classet/refs/heads/main/asyncapi/classet-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/classet-webhooks.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/classet/refs/heads/main/authentication/classet-authentication.yml
  title: ''
  type: Authentication
  url: authentication/classet-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/classet/refs/heads/main/llms/classet-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/classet-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/classet/refs/heads/main/mcp/classet-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/classet-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/classet/refs/heads/main/well-known/classet-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/classet-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/classet/refs/heads/main/hosts/classet-hosts.yml
  title: ''
  type: Hosts
  url: hosts/classet-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/classet/refs/heads/main/vendors/classet-vendors.yml
  title: ''
  type: Vendors
  url: vendors/classet-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.classet.ai/changelog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/classet/refs/heads/main/security/classet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/classet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.classet.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.classet.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.classet.ai/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.classet.ai/reference/getting-started-with-classet
- group: company
  title: ''
  type: Blog
  url: https://www.classet.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.classet.ai/pricing
- group: operate
  title: ''
  type: Support
  url: https://help.classet.ai
- group: start
  title: ''
  type: SignUp
  url: https://app.classet.ai/signup/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.classet.ai/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/classet
coverage:
  checked: '2026-10-08'
  detail: Documentation pages are rendered via JavaScript on a ReadMe platform, preventing machine‑readable spec extraction.
  evidence:
  - status: 200
    url: https://docs.classet.ai/reference
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-08'
description: Classet provides an AI‑powered recruiting platform that automates candidate screening, outreach, and analytics. Their self‑driving ATS, Joy, integrates with 95 ATS systems and offers voice interview automation, customizable workflows, and detailed hiring insights for enterprises across healthcare, hospitality, retail, manufacturing, and more.
image: https://www.classet.ai/images/OG-Image.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.classet.ai.
  name: Classet MCP Server
  slug: classet-mcp-yml
modified: '2026-10-08'
name: Classet
nav: Providers
network: true
overview: 'Classet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Recruiting, Applicant Tracking, Automation, and Enterprise.


  The Classet catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Classet''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Classet Plans Pricing
  plan_count: 3
  slug: classet-plans-pricing
random_paper: 3
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 52.4
    discoverability: 58.3
    operational_transparency: 23.7
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Classet Authentication
  slug: classet-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Classet Domain Security
  slug: classet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: classet
tags:
- Artificial Intelligence
- Recruiting
- Applicant Tracking
- Automation
- Enterprise
website: https://www.classet.ai
---
