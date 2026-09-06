---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
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
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'Sitetracker''s programmable surface is the Salesforce Platform API over the Sitetracker managed package''s standard and custom objects. Sitetracker states: "You can build apps, automations, and integrat'
  name: Sitetracker Platform API
  slug: sitetracker-platform-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sitetracker-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sitetracker.com/
- group: company
  title: ''
  type: Blog
  url: https://www.sitetracker.com/knowledge-center/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.sitetracker.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.sitetracker.com/company/contact/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.sitetracker.com/
- group: start
  title: ''
  type: Login
  url: https://sitetracker-login.cloudforce.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sitetracker
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sitetracker.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sitetracker.com/privacy-policy/
- group: auth
  title: ''
  type: Trust
  url: https://trust.sitetracker.com/
- group: other
  title: ''
  type: Marketplace
  url: https://appexchange.salesforce.com/appxListingDetail?listingId=a0N3A00000DvOROUA3
- group: build
  title: ''
  type: Packages
  url: packages/sitetracker-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sitetracker-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/sitetracker-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sitetracker-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sitetracker-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sitetracker-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sitetracker-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sitetracker-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sitetracker-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sitetracker-llms.txt
coverage:
  checked: '2026-08-27'
  detail: Sitetracker markets REST, SOAP and Bulk APIs over its Salesforce managed package but operates no API host of its own and publishes no reference — both help.sitetracker.com and community.sitetracker.com hand every request, including every /.well-known path, to a Salesforce Customer Secure Login page, so the object model and integration guide are readable only inside an existing customer tenant.
  evidence:
  - note: 302s to login.salesforce.com/setup/secur/RemoteAccessAuthorizationPage.apexp — the Salesforce OAuth connected-app login.
    status: 200
    url: https://community.sitetracker.com/
  - note: Serves a login page whose only action is /oauth2/authorization/salesforce.
    status: 200
    url: https://help.sitetracker.com/
  - note: Salesforce login HTML shell, not a spec — catch-all false positive.
    status: 200
    url: https://help.sitetracker.com/openapi.json
  - status: 404
    url: https://www.sitetracker.com/openapi.json
  - note: DNS NXDOMAIN — no Sitetracker-operated API host exists.
    status: 0
    url: https://api.sitetracker.com/
  reason: customer-only-docs
  state: gated
created: '2026-08-27'
description: Sitetracker is a global software company whose deployment operations management platform is built natively on Salesforce, used to plan, build, operate and maintain critical infrastructure at scale — fiber and wireless networks, towers, data centers, space and satellite, utilities, renewable energy, battery storage and EV charging. The product set spans Project Management, Financial Management, Agreement Management, Field Work Management, Site & Asset Management, Reporting & Analytics, Sitetracker GIS Link, Sitetracker Mobile and the Scout AI assistant. Because the platform is a Salesforce managed package, its programmable surface is the Salesforce Platform API — Sitetracker states that its standard and custom objects are API-ready and reachable over REST, SOAP and Bulk APIs, called against each customer's own Salesforce org rather than a Sitetracker-operated API host. Sitetracker publishes no public developer portal, API reference or machine-readable contract; the object and
  integration documentation sits behind a Salesforce Community login.
image: https://www.sitetracker.com/wp-content/uploads/2022/06/Sitetracker-Logo-Approved-2022_rgb-fullcolor.svg
layout: provider
modified: '2026-08-27'
name: Sitetracker
nav: Providers
network: true
overview: 'Sitetracker publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telecommunications, Utilities, Energy, and EV Charging.


  Sitetracker''s developer surface includes engineering blog, support, authentication, and 19 more developer resources.'
plans:
- name: Sitetracker Plans Pricing
  plan_count: 0
  slug: sitetracker-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Sitetracker Rate Limits
  slug: sitetracker-rate-limits
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 28.9
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 48.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sitetracker/refs/heads/main/screenshots/sitetracker-2026-09-02T155659.png
security:
- kind: authentication
  name: Sitetracker Authentication
  slug: sitetracker-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Sitetracker Domain Security
  slug: sitetracker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sitetracker Vulnerability Disclosure
  slug: sitetracker-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Sitetracker Trust Center
  slug: sitetracker-trust-center
  summary_line: SOC 1 Type II, SOC 2 Type II, ISO/IEC 27001, ISO/IEC 27701
slug: sitetracker
tags:
- Company
- Telecommunications
- Utilities
- Energy
- EV Charging
- Fiber Networks
- Asset Management
- Project Management
- Field Service
- Salesforce
- Critical Infrastructure
website: https://www.sitetracker.com/
---
