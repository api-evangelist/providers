---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Simpplr Agentic Access
  operation_count: 74
  slug: simpplr-agentic-access
  summary_line: 74 operations · 29 acting
api_count: 8
apis:
- description: Simpplr's REST API for managing intranet content and community — sites, pages, blogs, events, alerts, notifications, people and audiences, content approval/engagement, search, media uploads, and adopt
  name: Simpplr Extensibility Center API
  slug: simpplr-extensibility-center-api
- baseURL: https://api.ec.simpplr.com/api
  baseurl_source: declared
  description: The Alerts API from Simpplr — 3 operation(s) for alerts.
  name: Simpplr Alerts API
  slug: simpplr-alerts-api
- baseURL: https://api.ec.simpplr.com/api
  baseurl_source: declared
  description: The Analytics API from Simpplr — 25 operation(s) for analytics.
  name: Simpplr Analytics API
  slug: simpplr-analytics-api
- baseURL: https://api.ec.simpplr.com/api
  baseurl_source: declared
  description: The Audience API from Simpplr — 2 operation(s) for audience.
  name: Simpplr Audience API
  slug: simpplr-audience-api
- baseURL: https://api.ec.simpplr.com/api
  baseurl_source: declared
  description: The Blogs API from Simpplr — 2 operation(s) for blogs.
  name: Simpplr Blogs API
  slug: simpplr-blogs-api
- baseURL: https://api.ec.simpplr.com/api
  baseurl_source: declared
  description: The Carousels API from Simpplr — 1 operation(s) for carousels.
  name: Simpplr Carousels API
  slug: simpplr-carousels-api
- baseURL: https://api.ec.simpplr.com/api
  baseurl_source: declared
  description: The Contents API from Simpplr — 16 operation(s) for contents.
  name: Simpplr Contents API
  slug: simpplr-contents-api
- baseURL: https://api.ec.simpplr.com/api
  baseurl_source: declared
  description: The Notifications API from Simpplr — 2 operation(s) for notifications.
  name: Simpplr Notifications API
  slug: simpplr-notifications-api
- baseURL: https://api.ec.simpplr.com/api
  baseurl_source: declared
  description: The People API from Simpplr — 2 operation(s) for people.
  name: Simpplr People API
  slug: simpplr-people-api
- baseURL: https://api.ec.simpplr.com/api
  baseurl_source: declared
  description: The Search API from Simpplr — 3 operation(s) for search.
  name: Simpplr Search API
  slug: simpplr-search-api
- baseURL: https://api.ec.simpplr.com/api
  baseurl_source: declared
  description: The Simpplr Api Gw Search People By Id API from Simpplr — 1 operation(s) for simpplr api gw search people by id.
  name: Simpplr Simpplr Api Gw Search People By Id API
  slug: simpplr-simpplr-api-gw-search-people-by-id-api
- baseURL: https://api.ec.simpplr.com/api
  baseurl_source: declared
  description: The Sites API from Simpplr — 6 operation(s) for sites.
  name: Simpplr Sites API
  slug: simpplr-sites-api
artifact_total: 19
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/simpplr/refs/heads/main/agentic-access/simpplr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/simpplr-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/simpplr/refs/heads/main/rules/simpplr-rules.yml
  title: ''
  type: Spectral
  url: rules/simpplr-rules.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/simpplr/refs/heads/main/security/simpplr-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/simpplr-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/simpplr/refs/heads/main/errors/simpplr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/simpplr-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/simpplr/refs/heads/main/conformance/simpplr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/simpplr-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/simpplr/refs/heads/main/hosts/simpplr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/simpplr-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/simpplr/refs/heads/main/vendors/simpplr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/simpplr-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.simpplr.com/tos/
- group: company
  title: ''
  type: Newsroom
  url: https://www.simpplr.com/newsroom/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/simpplr/refs/heads/main/scopes/simpplr-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/simpplr-scopes.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.simpplr.com/feed/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/simpplr/refs/heads/main/security/simpplr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/simpplr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://simpplr.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.simpplr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.simpplr.com/reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer.simpplr.com/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.simpplr.com/reference/authenticating-via-an-external-application
- group: operate
  title: ''
  type: Support
  url: https://help.simpplr.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.simpplr.com/
- group: company
  title: ''
  type: Blog
  url: https://www.simpplr.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.simpplr.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.simpplr.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.simpplr.com/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.simpplr.com/security-compliance/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.simpplr.com/security-compliance/
- group: auth
  title: ''
  type: Security
  url: https://simpplr.com/vulnerability-disclosure-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/simpplr/refs/heads/main/well-known/simpplr-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/simpplr-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/simpplr/refs/heads/main/well-known/simpplr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/simpplr-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/simpplr/refs/heads/main/security/simpplr-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/simpplr-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/simpplr/refs/heads/main/authentication/simpplr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/simpplr-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/simpplr/refs/heads/main/mcp/simpplr-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/simpplr-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/simpplr/refs/heads/main/llms/simpplr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/simpplr-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/simpplr/refs/heads/main/conventions/simpplr-conventions.yml
  title: ''
  type: Conventions
  url: conventions/simpplr-conventions.yml
created: '2026-07-17'
description: Simpplr is an AI-powered employee experience platform (modern intranet, employee communications, recognition, and virtual assistant) used by enterprises to inform, engage, and connect their workforce. Built on the Salesforce platform, Simpplr publishes a REST "Extensibility Center" API at developer.simpplr.com that lets developers programmatically manage sites, pages, blogs, events, alerts, notifications, people/audiences, content, search, media, and adoption/engagement analytics. Authentication is OAuth 2.0 (bearer token) via a connected app on the Salesforce platform. Simpplr was founded in 2014, is headquartered in Redwood City, California, and is backed by venture investors including Norwest Venture Partners and Sapphire Ventures. This profile was added to the API Evangelist network from the VC portfolio pipeline and enriched from Simpplr's public developer surface.
image: https://www.simpplr.com/wp-content/uploads/2023/01/simpplr-logo.png
layout: provider
modified: '2026-10-06'
name: Simpplr
nav: Providers
network: true
overview: 'Simpplr publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alerts API, Analytics API, Audience API, and 9 more. Tagged areas include Company, Employee Experience, Intranet, Employee Communications, and Digital Workplace.


  The Simpplr catalog on APIs.io includes 1 Spectral governance ruleset.


  Simpplr''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Simpplr API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 2
  slug: simpplr-rules
scopes:
- name: Simpplr Scopes
  scope_count: 0
  slug: simpplr-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 20.2
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 52.4
    developer_ergonomics: 38.1
    discoverability: 80.4
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 24.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 11
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 45.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/simpplr/refs/heads/main/screenshots/simpplr-2026-09-02T155601.png
security:
- kind: authentication
  name: Simpplr Authentication
  slug: simpplr-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Simpplr Domain Security
  slug: simpplr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Simpplr Vulnerability Disclosure
  slug: simpplr-vulnerability-disclosure
  summary_line: security.txt
- kind: trust-center
  name: Simpplr Trust Center
  slug: simpplr-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR, PCI DSS, CCPA
slug: simpplr
tags:
- Company
- Employee Experience
- Intranet
- Employee Communications
- Digital Workplace
- Internal Communications
- Human Resources
- Collaboration
- Enterprise Software
- Salesforce
website: https://simpplr.com
---
