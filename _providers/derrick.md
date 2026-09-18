---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.5
  scored_at: '2026-09-17'
api_count: 2
apis:
- description: REST API for B2B data enrichment (emails, phones, profile/company enrichment, verification, search, SIRET/SIREN). Bearer API-key auth; requires Standard plan or above.
  name: Derrick REST API
  slug: derrick-rest-api
- description: Hosted streamable-HTTP MCP server exposing 12 enrichment tools; also available as a local npm package (derrick-mcp). Bearer API-key auth; requires Standard plan or above.
  name: Derrick MCP Server
  slug: derrick-mcp-server
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://derrick-app.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/derrick/refs/heads/main/security/derrick-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/derrick-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/derrick/refs/heads/main/security/derrick-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/derrick-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/derrick/refs/heads/main/security/derrick-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/derrick-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/derrick/refs/heads/main/well-known/derrick-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/derrick-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/derrick/refs/heads/main/well-known/derrick-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/derrick-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/derrick/refs/heads/main/mcp/derrick-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/derrick-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/derrick/refs/heads/main/llms/derrick-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/derrick-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/derrick/refs/heads/main/packages/derrick-packages.yml
  title: ''
  type: Packages
  url: packages/derrick-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/derrick/refs/heads/main/plans/derrick-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/derrick-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/derrick/refs/heads/main/rate-limits/derrick-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/derrick-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/derrick/refs/heads/main/authentication/derrick-authentication.yml
  title: ''
  type: Authentication
  url: authentication/derrick-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/derrick/refs/heads/main/conformance/derrick-conformance.yml
  title: ''
  type: Conformance
  url: conformance/derrick-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/derrick/refs/heads/main/conventions/derrick-conventions.yml
  title: ''
  type: Conventions
  url: conventions/derrick-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/derrick/refs/heads/main/errors/derrick-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/derrick-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/derrick/refs/heads/main/lifecycle/derrick-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/derrick-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/derrick/refs/heads/main/changelog/derrick-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/derrick-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/derrick/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://derrick-app.com/#pricing
- group: operate
  title: ''
  type: Roadmap
  url: https://derrick.productlift.dev/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://derrick-app.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://derrick-app.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://derrick-app.com/get-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DerrickAppOrg
created: '2026-09-09'
description: B2B data-enrichment engine providing professional emails, phone numbers, LinkedIn/company enrichment, tech-stack detection, email verification, lead/company search, and French SIRET/SIREN data. Delivered via a Google Sheets add-on, a REST API, and an MCP server for AI agents.
image: https://derrick-app.com/og/index.png
layout: provider
mcp_servers:
- description: ''
  name: Derrick MCP Server
  slug: derrick-mcp-server
- description: ''
  name: Derrick MCP Server
  slug: derrick-mcp-server-2
modified: '2026-09-09'
name: Derrick
nav: Providers
network: true
overview: 'Derrick publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include b2b-data-enrichment, Email Finder, Phone Finder, company-firmographics, and Lead Generation.


  Derrick''s developer surface includes authentication, changelog, pricing, engineering blog, signup flow, and 19 more developer resources.'
plans:
- name: Derrick Plans Pricing
  plan_count: 6
  slug: derrick-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Derrick Rate Limits
  slug: derrick-rate-limits
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 25.6
    discoverability: 75.9
    operational_transparency: 55.3
  previous_composite: 34.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Derrick Authentication
  slug: derrick-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Derrick Domain Security
  slug: derrick-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Derrick Vulnerability Disclosure
  slug: derrick-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: derrick
tags:
- b2b-data-enrichment
- Email Finder
- Phone Finder
- company-firmographics
- Lead Generation
- Sales Intelligence
- CRM Enrichment
- tech-stack-detection
- Email Verification
- siret-siren-france
- MCP Server
- llms-txt
- Google Sheets
- gtm-tools
website: https://derrick-app.com
---
