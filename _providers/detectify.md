---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'RESTful API (v3) for managing assets and retrieving attack-surface and scan data — surface-monitoring domains and IPs, IP addresses, technologies, ports, breaches, and cloud connectors. Authenticates '
  name: Detectify REST API
  slug: detectify-rest-api
artifact_total: 10
asyncapis:
- description: ''
  name: Detectify Webhooks
  slug: detectify-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/detectify/plans/detectify-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/detectify-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.detectify.com/feed/
- group: company
  title: ''
  type: Website
  url: https://detectify.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.detectify.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.detectify.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.detectify.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.detectify.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.detectify.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.detectify.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/detectify
- group: commercial
  title: ''
  type: Pricing
  url: https://detectify.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://detectify.com/createaccount
- group: commercial
  title: ''
  type: TermsOfService
  url: https://detectify.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://detectify.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.detectify.com/
- group: auth
  title: ''
  type: Security
  url: https://detectify.com/responsible-disclosure
- group: auth
  title: ''
  type: Compliance
  url: https://docs.detectify.com/security-and-compliance
- group: auth
  href: https://artifacts.apis.io/detectify/authentication/detectify-authentication.yml
  title: ''
  type: Authentication
  url: authentication/detectify-authentication.yml
- group: design
  href: https://artifacts.apis.io/detectify/lifecycle/detectify-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/detectify-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/detectify/conventions/detectify-conventions.yml
  title: ''
  type: Conventions
  url: conventions/detectify-conventions.yml
- group: design
  href: https://artifacts.apis.io/detectify/conformance/detectify-conformance.yml
  title: ''
  type: Conformance
  url: conformance/detectify-conformance.yml
- group: design
  href: https://artifacts.apis.io/detectify/asyncapi/detectify-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/detectify-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/detectify/mcp/detectify-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/detectify-mcp.yml
- group: agent
  href: https://artifacts.apis.io/detectify/llms/detectify-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/detectify-llms.txt
- group: agent
  href: https://artifacts.apis.io/detectify/well-known/detectify-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/detectify-well-known.yml
- group: auth
  href: https://artifacts.apis.io/detectify/well-known/detectify-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/detectify-security.txt
- group: build
  href: https://artifacts.apis.io/detectify/packages/detectify-packages.yml
  title: ''
  type: Packages
  url: packages/detectify-packages.yml
- group: auth
  href: https://artifacts.apis.io/detectify/security/detectify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/detectify-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/detectify/security/detectify-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/detectify-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/detectify/security/detectify-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/detectify-trust-center.yml
created: '2026-07-17'
description: Detectify is an External Attack Surface Management (EASM) and Dynamic Application Security Testing (DAST) platform that continuously discovers an organization's internet-facing assets and runs real, payload-based vulnerability tests against them. Its testing engine is fuelled by Crowdsource, a network of ~400 vetted ethical hackers who contribute 1,765+ vulnerability modules at a ~99.7% true-positive rate. Detectify ships four products — Surface Monitoring (attack surface management), Application Scanning (web app DAST), API Scanning (OpenAPI-driven API security testing), and Internal Scanning — plus a REST API (v3), a remotely-hosted MCP server for AI-driven workflows, and integrations for Jira, Slack, Splunk, and CI/CD. Founded in Stockholm and backed by Balderton Capital and Insight Partners.
finops:
- has_sources: true
  method: derived
  name: Detectify Finops
  primary_unit: platform fee
  service_category: ''
  slug: detectify-finops
  template: false
image: https://d35ayjp87i0qx4.cloudfront.net/detectify_global.png
layout: provider
mcp_servers:
- description: Remote MCP server over HTTP.
  name: detectify MCP Server
  slug: detectify
modified: '2026-10-06'
name: detectify
nav: Providers
network: true
overview: 'detectify is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Attack Surface Management, and EASM.


  The detectify catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  detectify''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
plans:
- name: Detectify Plans Pricing
  plan_count: 4
  slug: detectify-plans-pricing
- name: Detectify Price Estimates
  plan_count: 0
  slug: detectify-price-estimates
random_paper: 1
score:
  band: strong
  composite: 58.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.8
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 57.1
    discoverability: 71.7
    operational_transparency: 36.8
  previous_composite: 49.5
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/detectify/detectify-2026-07-25T211804.png
security:
- kind: authentication
  name: Detectify Authentication
  slug: detectify-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Detectify Domain Security
  slug: detectify-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Detectify Vulnerability Disclosure
  slug: detectify-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Detectify Trust Center
  slug: detectify-trust-center
  summary_line: ISO 27001, PCI DSS, GDPR
slug: detectify
tags:
- Company
- Security
- Cybersecurity
- Attack Surface Management
- EASM
- Vulnerability Scanning
- DAST
- Application Security
- API Security
website: https://detectify.com/
---
