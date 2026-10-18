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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Plex offers several API options for ERP endpoints such as customer orders, shipping, and just-in-sequence parts delivery.
  name: Plex ERP API
  slug: plex-erp-api
artifact_total: 3
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/plex-systems/refs/heads/main/llms/plex-systems-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/plex-systems-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/plex-systems/refs/heads/main/well-known/plex-systems-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/plex-systems-www-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/plex-systems/refs/heads/main/well-known/plex-systems-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/plex-systems-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/plex-systems/refs/heads/main/hosts/plex-systems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/plex-systems-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/plex-systems/refs/heads/main/vendors/plex-systems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/plex-systems-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://engage.rockwellautomation.com/termsandconditions
- group: auth
  title: ''
  type: Security
  url: https://engage.rockwellautomation.com/HigherLogic/Security/SAML/localSAMLLoginService.aspx?ReturnUrl=https%3a%2f%2fengage.rockwellautomation.com%2fhome
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://plex.rockwellautomation.com/en-us/privacy-policy.html
- group: company
  title: ''
  type: Newsroom
  url: https://plex.rockwellautomation.com/en-us/company/newsroom/ai-job-creation.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/plex-systems/refs/heads/main/security/plex-systems-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/plex-systems-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/plex-systems/refs/heads/main/security/plex-systems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/plex-systems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://plex.rockwellautomation.com
- group: docs
  title: ''
  type: Documentation
  url: https://plex.rockwellautomation.com/en-us.html
- group: company
  title: ''
  type: Blog
  url: https://plex.rockwellautomation.com/en-us/blog.html
- group: operate
  title: ''
  type: Support
  url: https://plex.rockwellautomation.com/en-us/support.html
coverage:
  checked: '2026-10-12'
  detail: The ERP API documentation page provides information but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://plex.rockwellautomation.com/en-us/resources/enterprise-resource-planning-erp-apis.html
  - status: 404
    url: https://plex.rockwellautomation.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Plex Systems provides the Plex Smart Manufacturing Platform, a cloud‑based, elastic Manufacturing Execution System (MES) that integrates people, processes, machines and supply chains. Hosted by Rockwell Automation, Plex delivers real‑time visibility, AI‑driven insights, and scalable SaaS tools for manufacturers to improve operations, quality, and agility across the enterprise.
image: https://plex.rockwellautomation.com/content/dam/rockwell-automation/images/illustrations/background-textures/1920x1080-backTexture-social.jpg
layout: provider
modified: '2026-10-12'
name: Plex Systems
nav: Providers
network: true
overview: 'Plex Systems is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Manufacturing, Cloud, Software-as-a-Service, MES, and Automation.


  Plex Systems'' developer surface includes documentation, engineering blog, support, and 12 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 66.1
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Plex Systems Domain Security
  slug: plex-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Plex Systems Vulnerability Disclosure
  slug: plex-systems-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: plex-systems
tags:
- Manufacturing
- Cloud
- Software-as-a-Service
- MES
- Automation
- Company
website: https://plex.rockwellautomation.com
---
