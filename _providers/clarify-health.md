---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 21.1
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clarify-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clarifyhealth.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clarifyhealth.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clarifyhealth.com/privacy-policy
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://clarifyhealth.com/acceptable-use-policy
- group: other
  title: ''
  type: Resources
  url: https://clarifyhealth.com/resources
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clarify-health-solutions/
- group: company
  title: ''
  type: Blog
  url: https://clarifyhealth.com/resources
- group: company
  title: ''
  type: BlogRSS
  url: https://clarifyhealth.com/resource-source?format=rss
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clarifyhealth
- group: operate
  title: ''
  type: Contact
  url: https://clarifyhealth.com/contact-clarify
- group: company
  title: ''
  type: Careers
  url: https://clarifyhealth.com/careers
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clarifyhealth.com
- group: auth
  title: ''
  type: Compliance
  url: https://clarifyhealth.com/qe-public-reports
- group: agent
  title: ''
  type: WellKnown
  url: well-known/clarify-health-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clarify-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/clarify-health-scopes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clarify-health-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/clarify-health-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/clarify-health-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/clarify-health-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clarify-health-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/clarify-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clarify-health-rate-limits.yml
coverage:
  checked: '2026-08-15'
  detail: Clarify Health's entire public surface is a 79-page Squarespace marketing site whose sitemap contains no developer, API or documentation path and whose pages contain zero occurrences of the word "API"; api., docs., developer., developers. and portal.clarifyhealth.com are all NXDOMAIN, and the only machine-readable documents the company serves anywhere are the OIDC discovery files on its Auth0 and Okta login hosts.
  evidence:
  - status: 200
    url: https://clarifyhealth.com/sitemap.xml
  - status: 404
    url: https://clarifyhealth.com/openapi.json
  - status: 404
    url: https://clarifyhealth.com/llms.txt
  - status: 404
    url: https://clarifyhealth.com/.well-known/agent-card.json
  - status: 200
    url: https://auth.clarifyhealth.com/.well-known/openid-configuration
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Clarify Health Solutions is a healthcare analytics and outcomes company that helps health systems, payers, and life sciences organizations understand cost, quality, and utilization across the care journey. Its flagship platform, Clarify Meridian, unifies referral intelligence, physician activation, consumer engagement, and outcomes attribution into a single analytics environment built on billions of longitudinal patient records and claims data. Clarify Health is backed by SoftBank Vision Fund and, in 2026, acquired Loyal Health to expand its consumer engagement capabilities. The company operates a SaaS analytics product rather than a public developer API; this profile tracks its identity and public web surface within the API Evangelist network.
image: https://clarifyhealth.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: CMS Data.gov MCP Server
  slug: cms-datagov-mcp-server
modified: '2026-08-15'
name: Clarify Health
nav: Providers
network: true
overview: 'Clarify Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Tech, Healthcare Analytics, Health Data, and Outcomes.


  Clarify Health''s developer surface includes engineering blog, authentication, and 22 more developer resources.'
plans:
- name: Clarify Health Plans Pricing
  plan_count: 0
  slug: clarify-health-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Clarify Health Rate Limits
  slug: clarify-health-rate-limits
scopes:
- name: Clarify Health Scopes
  scope_count: 0
  slug: clarify-health-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 13
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 24.2
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clarify-health/refs/heads/main/screenshots/clarify-health-2026-07-25T205504.png
security:
- kind: authentication
  name: Clarify Health Authentication
  slug: clarify-health-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Clarify Health Domain Security
  slug: clarify-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clarify-health
tags:
- Company
- Health Tech
- Healthcare Analytics
- Health Data
- Outcomes
- Referral Intelligence
- Payers
- Life Sciences
website: https://clarifyhealth.com
---
